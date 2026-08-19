#!/usr/bin/env python3
"""Post a Markdown report to Discord without breaking its message limit."""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

MAX_DISCORD_CONTENT_CHARS = 2_000
FENCE_RE = re.compile(r"(^```[^\n]*\n.*?^```[ \t]*(?:\n|$))", re.MULTILINE | re.DOTALL)


def _split_plain_text(text: str, limit: int) -> list[str]:
    """Split plain text at useful boundaries, then hard-split only as a last resort."""
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

        part = rest[:cut]
        if part:
            parts.append(part)
        rest = rest[cut:]

    if rest:
        parts.append(rest)
    return parts


def _split_code_block(block: str, limit: int) -> list[str]:
    """Split an oversized fenced code block into individually valid fenced blocks."""
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

    overhead = len(opening) + len(closing)
    body_limit = limit - overhead
    if body_limit <= 0:
        raise ValueError("Discord message limit is too small for fenced code-block markers")

    pieces = _split_plain_text(body, body_limit)
    if not pieces:
        pieces = [""]

    result = []
    for piece in pieces:
        if piece and not piece.endswith("\n"):
            piece += "\n"
        candidate = opening + piece + closing
        if len(candidate) > limit:
            raise AssertionError("code-block splitter produced an oversized chunk")
        result.append(candidate)
    return result


def _segments(markdown: str, limit: int) -> list[str]:
    """Tokenize Markdown into plain-text and fenced-code segments."""
    result: list[str] = []
    pos = 0

    for match in FENCE_RE.finditer(markdown):
        if match.start() > pos:
            result.extend(_split_plain_text(markdown[pos : match.start()], limit))

        block = match.group(0)
        if len(block) <= limit:
            result.append(block)
        else:
            result.extend(_split_code_block(block, limit))
        pos = match.end()

    if pos < len(markdown):
        result.extend(_split_plain_text(markdown[pos:], limit))

    return [segment for segment in result if segment]


def split_markdown(markdown: str, limit: int = MAX_DISCORD_CONTENT_CHARS) -> list[str]:
    """Split Markdown into Discord-safe messages no longer than ``limit`` characters."""
    if limit <= 0:
        raise ValueError("limit must be positive")
    if len(markdown) <= limit:
        return [markdown]

    chunks: list[str] = []
    current = ""

    for segment in _segments(markdown, limit):
        if len(segment) > limit:
            raise AssertionError("segmenter produced an oversized segment")

        if not current:
            current = segment
            continue

        if len(current) + len(segment) <= limit:
            current += segment
            continue

        chunks.append(current)
        current = segment

    if current:
        chunks.append(current)

    if not chunks:
        return [""]
    if any(len(chunk) > limit for chunk in chunks):
        raise AssertionError("Markdown splitter exceeded the Discord content limit")
    return chunks


def _wait_url(webhook_url: str) -> str:
    parsed = urllib.parse.urlsplit(webhook_url)
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    if not any(key == "wait" for key, _ in query):
        query.append(("wait", "true"))
    return urllib.parse.urlunsplit(
        (parsed.scheme, parsed.netloc, parsed.path, urllib.parse.urlencode(query), parsed.fragment)
    )


def post_chunk(
    webhook_url: str,
    channel_name: str,
    content: str,
    *,
    timeout: float = 30.0,
    retries: int = 5,
) -> None:
    """Post one chunk and honor Discord rate-limit responses."""
    payload = json.dumps(
        {
            "content": content,
            "username": channel_name,
            "allowed_mentions": {"parse": []},
        }
    ).encode("utf-8")

    url = _wait_url(webhook_url)
    request = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Content-Type": "application/json",
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
            body = exc.read().decode("utf-8", errors="replace")
            if exc.code == 429 and attempt < retries:
                try:
                    retry_after = float(json.loads(body).get("retry_after", 1.0))
                except (TypeError, ValueError, json.JSONDecodeError):
                    retry_after = 1.0
                time.sleep(max(retry_after, 0.05))
                continue
            raise RuntimeError(f"Discord webhook failed with HTTP {exc.code}: {body}") from exc
        except urllib.error.URLError as exc:
            if attempt < retries:
                time.sleep(min(2**attempt, 8))
                continue
            raise RuntimeError(f"Discord webhook request failed: {exc.reason}") from exc

    raise RuntimeError("Discord webhook retry loop exhausted")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--channel-name", required=True)
    parser.add_argument("--webhook-url", required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    markdown = args.report.read_text(encoding="utf-8")
    chunks = split_markdown(markdown)

    print(
        f"{args.report}: {len(markdown)} chars -> {len(chunks)} Discord message(s); "
        f"largest={max(map(len, chunks), default=0)}"
    )

    if args.dry_run:
        for index, chunk in enumerate(chunks, start=1):
            print(f"--- chunk {index}/{len(chunks)} ({len(chunk)} chars) ---")
            print(chunk)
        return 0

    for index, chunk in enumerate(chunks, start=1):
        post_chunk(args.webhook_url, args.channel_name, chunk)
        print(f"posted chunk {index}/{len(chunks)} ({len(chunk)} chars)")
        if index != len(chunks):
            time.sleep(0.35)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
