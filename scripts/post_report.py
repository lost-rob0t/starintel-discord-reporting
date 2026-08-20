#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import mimetypes
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

MAX_DISCORD_CONTENT_CHARS = 2_000
SUPPRESS_EMBEDS_FLAG = 1 << 2
FENCE_RE = re.compile(r"(^```[^\n]*\n.*?^```[ \t]*(?:\n|$))", re.MULTILINE | re.DOTALL)
MEDIA_EXTENSIONS = ("png", "jpg", "jpeg", "gif", "webp")


class DestinationMismatch(RuntimeError):
    pass


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _split_plain_text(text: str, limit: int) -> list[str]:
    parts = []
    rest = text
    while len(rest) > limit:
        window = rest[: limit + 1]
        cut = max(window.rfind("\n\n", 0, limit + 1), window.rfind("\n", 0, limit + 1), window.rfind(" ", 0, limit + 1))
        if cut <= 0:
            cut = limit
        elif window[cut:cut + 2] == "\n\n":
            cut += 2
        else:
            cut += 1
        parts.append(rest[:cut])
        rest = rest[cut:]
    if rest:
        parts.append(rest)
    return parts


def _split_code_block(block: str, limit: int) -> list[str]:
    lines = block.splitlines(keepends=True)
    if len(lines) < 2 or not lines[0].startswith("```"):
        return _split_plain_text(block, limit)
    opening = lines[0]
    if lines[-1].lstrip().startswith("```"):
        closing = lines[-1]
        body = "".join(lines[1:-1])
    else:
        closing = "```\n"
        body = "".join(lines[1:])
    if not closing.endswith("\n"):
        closing += "\n"
    body_limit = limit - len(opening) - len(closing)
    if body_limit <= 0:
        raise ValueError("message limit too small for fenced block")
    out = []
    for piece in _split_plain_text(body, body_limit) or [""]:
        if piece and not piece.endswith("\n"):
            piece += "\n"
        out.append(opening + piece + closing)
    return out


def _segments(markdown: str, limit: int) -> list[str]:
    out = []
    pos = 0
    for match in FENCE_RE.finditer(markdown):
        if match.start() > pos:
            out.extend(_split_plain_text(markdown[pos:match.start()], limit))
        block = match.group(0)
        out.extend([block] if len(block) <= limit else _split_code_block(block, limit))
        pos = match.end()
    if pos < len(markdown):
        out.extend(_split_plain_text(markdown[pos:], limit))
    return [segment for segment in out if segment]


def split_markdown(markdown: str, limit: int = MAX_DISCORD_CONTENT_CHARS) -> list[str]:
    if limit <= 0:
        raise ValueError("limit must be positive")
    if len(markdown) <= limit:
        return [markdown]
    chunks = []
    current = ""
    for segment in _segments(markdown, limit):
        if not current:
            current = segment
        elif len(current) + len(segment) <= limit:
            current += segment
        else:
            chunks.append(current)
            current = segment
    if current:
        chunks.append(current)
    if any(len(chunk) > limit for chunk in chunks):
        raise AssertionError("splitter exceeded Discord limit")
    return chunks


def report_digest(channel_name: str, markdown: str) -> str:
    return hashlib.sha256((channel_name + "\0" + markdown).encode()).hexdigest()


def load_state(path: Path) -> dict:
    if not path.exists():
        return {"posted": [], "published_reports": [], "delivery_receipts": {}}
    data = json.loads(path.read_text(encoding="utf-8"))
    data.setdefault("posted", [])
    data.setdefault("published_reports", [])
    data.setdefault("delivery_receipts", {})
    return data


def _is_verified(receipt: object) -> bool:
    return isinstance(receipt, dict) and receipt.get("status") == "verified-delivered" and bool(receipt.get("message_ids")) and bool(receipt.get("channel_id"))


def already_reported(path: Path, report_id: str | None) -> bool:
    if not report_id:
        return False
    return _is_verified(load_state(path).get("delivery_receipts", {}).get(report_id))


def already_posted(path: Path, channel_name: str, markdown: str) -> bool:
    digest = report_digest(channel_name, markdown)
    for receipt in load_state(path).get("delivery_receipts", {}).values():
        if _is_verified(receipt) and receipt.get("report_digest") == digest:
            return True
    return False


def expected_channel_id(path: Path, channel_name: str) -> str | None:
    ids = {
        str(receipt.get("channel_id"))
        for receipt in load_state(path).get("delivery_receipts", {}).values()
        if _is_verified(receipt) and receipt.get("channel_name") == channel_name
    }
    ids.discard("")
    if len(ids) > 1:
        raise DestinationMismatch(f"stored verified receipts disagree for {channel_name}")
    return next(iter(ids), None)


def mark_verified_delivery(path: Path, report_id: str, channel_name: str, markdown: str, messages: list[dict]) -> None:
    if not messages:
        raise ValueError("verified delivery requires at least one Discord message")
    message_ids = []
    channel_ids = set()
    for message in messages:
        message_id = str(message.get("id", "")).strip()
        channel_id = str(message.get("channel_id", "")).strip()
        if not message_id or not channel_id:
            raise ValueError("verified delivery requires non-empty id and channel_id")
        message_ids.append(message_id)
        channel_ids.add(channel_id)
    if len(channel_ids) != 1:
        raise DestinationMismatch("one report returned multiple Discord channel IDs")
    channel_id = next(iter(channel_ids))
    expected = expected_channel_id(path, channel_name)
    if expected and channel_id != expected:
        raise DestinationMismatch(f"destination mismatch for {channel_name}: expected channel {expected}, got {channel_id}")
    now = _now()
    state = load_state(path)
    state["delivery_receipts"][report_id] = {
        "status": "verified-delivered",
        "channel_name": channel_name,
        "report_digest": report_digest(channel_name, markdown),
        "message_ids": message_ids,
        "channel_id": channel_id,
        "attempted_at": now,
        "accepted_at": now,
        "delivered_at": now,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _wait_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    if not any(key == "wait" for key, _ in query):
        query.append(("wait", "true"))
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, urllib.parse.urlencode(query), parsed.fragment))


def _multipart(payload: dict, attachment: Path) -> tuple[bytes, str]:
    boundary = "----starintel-" + uuid.uuid4().hex
    filename = attachment.name
    content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    payload = {**payload, "attachments": [{"id": 0, "filename": filename}]}
    body = bytearray()
    def add(value: bytes) -> None:
        body.extend(value)
    add(f"--{boundary}\r\n".encode())
    add(b'Content-Disposition: form-data; name="payload_json"\r\n')
    add(b"Content-Type: application/json\r\n\r\n")
    add(json.dumps(payload).encode())
    add(b"\r\n")
    add(f"--{boundary}\r\n".encode())
    add(f'Content-Disposition: form-data; name="files[0]"; filename="{filename}"\r\n'.encode())
    add(f"Content-Type: {content_type}\r\n\r\n".encode())
    add(attachment.read_bytes())
    add(b"\r\n")
    add(f"--{boundary}--\r\n".encode())
    return bytes(body), f"multipart/form-data; boundary={boundary}"


def _message_payload(channel_name: str, content: str) -> dict:
    return {"content": content, "username": channel_name, "allowed_mentions": {"parse": []}, "flags": SUPPRESS_EMBEDS_FLAG}


def _parse_message(body: bytes) -> dict:
    try:
        data = json.loads(body.decode("utf-8"))
    except Exception as exc:
        raise RuntimeError("Discord accepted the request but did not return valid message JSON") from exc
    if not isinstance(data, dict):
        raise RuntimeError("Discord response is not a message object")
    message_id = str(data.get("id", "")).strip()
    channel_id = str(data.get("channel_id", "")).strip()
    if not message_id or not channel_id:
        raise RuntimeError("Discord response lacks non-empty id/channel_id; delivery is unverified")
    return {"id": message_id, "channel_id": channel_id}


def post_chunk(url: str, channel_name: str, content: str, *, attachment: Path | None = None, timeout: float = 30.0, retries: int = 5) -> dict:
    payload = _message_payload(channel_name, content)
    if attachment and attachment.is_file():
        body, content_type = _multipart(payload, attachment)
    else:
        body = json.dumps(payload).encode()
        content_type = "application/json"
    request = urllib.request.Request(_wait_url(url), data=body, headers={"Content-Type": content_type, "User-Agent": "starintel-discord-reporting/1.0"}, method="POST")
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                response_body = response.read()
                if 200 <= response.status < 300:
                    return _parse_message(response_body)
                raise RuntimeError(f"Discord returned HTTP {response.status}")
        except urllib.error.HTTPError as exc:
            error_body = exc.read().decode("utf-8", errors="replace")
            if exc.code == 429 and attempt < retries:
                try:
                    delay = float(json.loads(error_body).get("retry_after", 1))
                except Exception:
                    delay = 1
                time.sleep(max(delay, 0.05))
                continue
            raise RuntimeError(f"Discord request failed with HTTP {exc.code}: {error_body}") from exc
        except urllib.error.URLError as exc:
            if attempt < retries:
                time.sleep(min(2 ** attempt, 8))
                continue
            raise RuntimeError(f"Discord request failed: {exc.reason}") from exc
    raise AssertionError("unreachable")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--channel-name", required=True)
    parser.add_argument("--webhook-url", required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--report-id", required=True)
    parser.add_argument("--attachment", type=Path)
    parser.add_argument("--state-file", type=Path, default=Path("state/published.json"))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    markdown = args.report.read_text(encoding="utf-8")
    if not args.force and already_reported(args.state_file, args.report_id):
        print(f"skip verified delivery: {args.report_id}")
        return 0
    chunks = split_markdown(markdown)
    print(f"{args.report}: {len(markdown)} chars -> {len(chunks)} message(s)")
    if args.dry_run:
        return 0
    receipts = []
    expected = expected_channel_id(args.state_file, args.channel_name)
    for index, chunk in enumerate(chunks, 1):
        receipt = post_chunk(args.webhook_url, args.channel_name, chunk, attachment=args.attachment if index == 1 else None)
        if expected and receipt["channel_id"] != expected:
            raise DestinationMismatch(f"destination mismatch for {args.channel_name}: expected channel {expected}, got {receipt['channel_id']}")
        expected = expected or receipt["channel_id"]
        receipts.append(receipt)
        print(f"accepted {index}/{len(chunks)} message_id={receipt['id']} channel_id={receipt['channel_id']}")
        if index != len(chunks):
            time.sleep(0.35)
    mark_verified_delivery(args.state_file, args.report_id, args.channel_name, markdown, receipts)
    print(f"verified-delivered: {args.report_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
