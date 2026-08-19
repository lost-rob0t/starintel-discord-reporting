#!/usr/bin/env python3
"""Fail closed when a report is not ready to publish."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

URL_RE = re.compile(r"https://[^\s)>\]}]+")
FENCE_RE = re.compile(r"^```", re.MULTILINE)
SENTENCE_RE = re.compile(r"[^.!?\n]+[.!?]")

REQUIRED_HEADINGS = {
    "findings": ("## Findings", "## Verification", "## Sources"),
    "changelog": ("## Changes", "## Sources"),
    "features": ("## New Features", "## Sources"),
}

SLOP_PHRASES = (
    "it's important to note",
    "it is important to note",
    "in today's fast-paced",
    "in conclusion",
    "key takeaway",
    "comprehensive overview",
    "delve into",
    "furthermore",
    "moreover",
    "seamlessly",
)

FOOTER_WARNING = "Please double check findings as this was llm derived"


def _without_code_blocks(text: str) -> str:
    lines = text.splitlines()
    result: list[str] = []
    in_fence = False
    for line in lines:
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            result.append(line)
    return "\n".join(result)


def _probe_url(url: str, timeout: float = 15.0) -> None:
    headers = {"User-Agent": "starintel-discord-reporting/1.0"}
    request = urllib.request.Request(url, headers=headers, method="HEAD")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            if 200 <= response.status < 400:
                return
    except urllib.error.HTTPError as exc:
        if exc.code not in {403, 405}:
            raise RuntimeError(f"source returned HTTP {exc.code}: {url}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"source could not be reached: {url}: {exc.reason}") from exc

    # Some sites reject HEAD even though the source is readable. Fetch one byte.
    request = urllib.request.Request(
        url,
        headers={**headers, "Range": "bytes=0-0"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            if 200 <= response.status < 400:
                return
            raise RuntimeError(f"source returned HTTP {response.status}: {url}")
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"source returned HTTP {exc.code}: {url}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"source could not be reached: {url}: {exc.reason}") from exc


def _sentence_lengths(text: str) -> list[int]:
    prose = _without_code_blocks(text)
    lengths = []
    for match in SENTENCE_RE.findall(prose):
        words = re.findall(r"\b[\w'-]+\b", match)
        if words:
            lengths.append(len(words))
    return lengths


def verify_report(text: str, *, kind: str, network: bool) -> list[str]:
    errors: list[str] = []

    if kind not in REQUIRED_HEADINGS:
        errors.append(f"unknown report kind: {kind}")
        return errors

    for heading in REQUIRED_HEADINGS[kind]:
        if heading not in text:
            errors.append(f"missing required heading: {heading}")

    fence_count = len(FENCE_RE.findall(text))
    if fence_count % 2:
        errors.append("unbalanced fenced Markdown code block")

    prose = _without_code_blocks(text)
    lowered = prose.lower()
    if "—" in prose:
        errors.append("em dash found; Discord report style forbids it")
    for phrase in SLOP_PHRASES:
        if phrase in lowered:
            errors.append(f"LLM-slop phrase found: {phrase!r}")

    if kind == "findings":
        if FOOTER_WARNING not in text:
            errors.append(f"missing findings warning: {FOOTER_WARNING}")

        signoff_matches = re.findall(r"^SIGNED OFF BY:\s*(.+?)\s*$", text, re.MULTILINE)
        if not signoff_matches:
            errors.append("missing SIGNED OFF BY footer")
        elif any(name.strip() in {"", "<NAME>"} for name in signoff_matches):
            errors.append("SIGN OFF name is still a placeholder")

        lengths = _sentence_lengths(text)
        if len(lengths) >= 6 and max(lengths) - min(lengths) < 6:
            errors.append("sentence lengths are too uniform; vary the rhythm before publishing")

    sources_at = text.find("## Sources")
    source_text = text[sources_at:] if sources_at >= 0 else ""
    urls = list(dict.fromkeys(URL_RE.findall(source_text)))
    minimum_sources = 2 if kind == "findings" else 1
    if len(urls) < minimum_sources:
        errors.append(f"expected at least {minimum_sources} source URL(s) in ## Sources")

    if network and not errors:
        for url in urls:
            try:
                _probe_url(url)
            except RuntimeError as exc:
                errors.append(str(exc))

    return errors


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("--kind", choices=sorted(REQUIRED_HEADINGS), default="findings")
    parser.add_argument("--no-network", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    text = args.report.read_text(encoding="utf-8")
    errors = verify_report(text, kind=args.kind, network=not args.no_network)

    if errors:
        print(f"{args.report}: NOT READY", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"{args.report}: verified for publication")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
