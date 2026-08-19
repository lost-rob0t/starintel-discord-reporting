#!/usr/bin/env python3
from __future__ import annotations

import argparse
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


def _split_plain_text(text: str, limit: int) -> list[str]:
    parts: list[str] = []
    rest = text
    while len(rest) > limit:
        window = rest[: limit + 1]
        cut = max(
            window.rfind("\n\n", 0, limit + 1),
            window.rfind("\n", 0, limit + 1),
            window.rfind(" ", 0, limit + 1),
        )
        if cut <= 0:
            cut = limit
        elif window[cut : cut + 2] == "\n\n":
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
    result = []
    for piece in _split_plain_text(body, body_limit) or [""]:
        if piece and not piece.endswith("\n"):
            piece += "\n"
        result.append(opening + piece + closing)
    return result


def _segments(markdown: str, limit: int) -> list[str]:
    out: list[str] = []
    pos = 0
    for match in FENCE_RE.finditer(markdown):
        if match.start() > pos:
            out.extend(_split_plain_text(markdown[pos : match.start()], limit))
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
    chunks: list[str] = []
    current = ""
    for segment in _segments(markdown, limit):
        if len(segment) > limit:
            raise AssertionError("oversized segment")
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
        return {"posted": [], "published_reports": []}
    data = json.loads(path.read_text(encoding="utf-8"))
    data.setdefault("posted", [])
    data.setdefault("published_reports", [])
    return data


def already_posted(path: Path, channel_name: str, markdown: str) -> bool:
    return report_digest(channel_name, markdown) in set(load_state(path).get("posted", []))


def already_reported(path: Path, report_id: str | None) -> bool:
    if not report_id:
        return False
    return report_id in set(load_state(path).get("published_reports", []))


def mark_posted(
    path: Path,
    channel_name: str,
    markdown: str,
    *,
    report_id: str | None = None,
) -> None:
    state = load_state(path)
    posted = list(dict.fromkeys([*state.get("posted", []), report_digest(channel_name, markdown)]))
    state["posted"] = posted[-2000:]
    if report_id:
        reports = list(dict.fromkeys([*state.get("published_reports", []), report_id]))
        state["published_reports"] = reports[-5000:]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _wait_url(webhook_url: str) -> str:
    parsed = urllib.parse.urlsplit(webhook_url)
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    if not any(key == "wait" for key, _ in query):
        query.append(("wait", "true"))
    return urllib.parse.urlunsplit(
        (parsed.scheme, parsed.netloc, parsed.path, urllib.parse.urlencode(query), parsed.fragment)
    )


def _multipart(payload: dict, attachment: Path) -> tuple[bytes, str]:
    boundary = "----starintel-" + uuid.uuid4().hex
    filename = attachment.name
    content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    payload = {
        **payload,
        "attachments": [{"id": 0, "filename": filename}],
    }
    body = bytearray()

    def add(value: bytes) -> None:
        body.extend(value)

    add(f"--{boundary}\r\n".encode())
    add(b'Content-Disposition: form-data; name="payload_json"\r\n')
    add(b"Content-Type: application/json\r\n\r\n")
    add(json.dumps(payload).encode("utf-8"))
    add(b"\r\n")

    add(f"--{boundary}\r\n".encode())
    add(
        f'Content-Disposition: form-data; name="files[0]"; filename="{filename}"\r\n'.encode(
            "utf-8"
        )
    )
    add(f"Content-Type: {content_type}\r\n\r\n".encode())
    add(attachment.read_bytes())
    add(b"\r\n")
    add(f"--{boundary}--\r\n".encode())
    return bytes(body), f"multipart/form-data; boundary={boundary}"


def _message_payload(channel_name: str, content: str) -> dict:
    return {
        "content": content,
        "username": channel_name,
        "allowed_mentions": {"parse": []},
        "flags": SUPPRESS_EMBEDS_FLAG,
    }


def post_chunk(
    webhook_url: str,
    channel_name: str,
    content: str,
    *,
    attachment: Path | None = None,
    timeout: float = 30.0,
    retries: int = 5,
) -> None:
    payload = _message_payload(channel_name, content)
    if attachment and attachment.is_file():
        body, content_type = _multipart(payload, attachment)
    else:
        body = json.dumps(payload).encode("utf-8")
        content_type = "application/json"

    request = urllib.request.Request(
        _wait_url(webhook_url),
        data=body,
        headers={
            "Content-Type": content_type,
            "User-Agent": "starintel-discord-reporting/1.0",
        },
        method="POST",
    )
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                if 200 <= response.status < 300:
                    return
                raise RuntimeError(f"Discord webhook returned HTTP {response.status}")
        except urllib.error.HTTPError as exc:
            error_body = exc.read().decode("utf-8", errors="replace")
            if exc.code == 429 and attempt < retries:
                try:
                    delay = float(json.loads(error_body).get("retry_after", 1))
                except Exception:
                    delay = 1
                time.sleep(max(delay, 0.05))
                continue
            raise RuntimeError(
                f"Discord webhook failed with HTTP {exc.code}: {error_body}"
            ) from exc
        except urllib.error.URLError as exc:
            if attempt < retries:
                time.sleep(min(2**attempt, 8))
                continue
            raise RuntimeError(f"Discord webhook request failed: {exc.reason}") from exc


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--channel-name", required=True)
    parser.add_argument("--webhook-url", required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--report-id")
    parser.add_argument("--attachment", type=Path)
    parser.add_argument("--state-file", type=Path, default=Path("state/published.json"))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    markdown = args.report.read_text(encoding="utf-8")

    if not args.force and already_reported(args.state_file, args.report_id):
        print(f"skip published report: {args.report_id}")
        return 0
    if not args.force and already_posted(args.state_file, args.channel_name, markdown):
        print(f"skip duplicate content: {args.report}")
        return 0

    chunks = split_markdown(markdown)
    print(
        f"{args.report}: {len(markdown)} chars -> {len(chunks)} message(s); "
        f"largest={max(map(len, chunks), default=0)}"
    )
    if args.attachment and args.attachment.is_file():
        print(f"attachment: {args.attachment}")
    if args.dry_run:
        return 0

    for index, chunk in enumerate(chunks, 1):
        post_chunk(
            args.webhook_url,
            args.channel_name,
            chunk,
            attachment=args.attachment if index == 1 else None,
        )
        print(f"posted {index}/{len(chunks)}")
        if index != len(chunks):
            time.sleep(0.35)

    mark_posted(
        args.state_file,
        args.channel_name,
        markdown,
        report_id=args.report_id,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
