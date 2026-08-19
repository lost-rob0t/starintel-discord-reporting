#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

URL_RE = re.compile(r"https://[^\s)>\]}]+")
FENCE_RE = re.compile(r"^```", re.MULTILINE)
SLOP = ("it's important to note", "it is important to note", "in conclusion", "key takeaway", "comprehensive overview", "delve into", "furthermore", "moreover", "seamlessly")
AI_WARNING = "This report was written by AI. Check it yourself."
TRUST_WARNING = "Do not trust this report as a source. Don't even trust NSA Spy."


def _probe(url: str, timeout: float = 15.0) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": "starintel-discord-reporting/1.0"}, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            if 200 <= r.status < 400:
                return
    except urllib.error.HTTPError as exc:
        if exc.code not in {403, 405}:
            raise RuntimeError(f"source HTTP {exc.code}: {url}") from exc
    req = urllib.request.Request(url, headers={"User-Agent": "starintel-discord-reporting/1.0", "Range": "bytes=0-0"}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            if 200 <= r.status < 400:
                return
    except Exception as exc:
        raise RuntimeError(f"source unreachable: {url}: {exc}") from exc


def verify(text: str, kind: str, network: bool) -> list[str]:
    errors: list[str] = []
    if len(FENCE_RE.findall(text)) % 2:
        errors.append("unbalanced fenced code block")
    lowered = text.lower()
    if "—" in text:
        errors.append("em dash found")
    for phrase in SLOP:
        if phrase in lowered:
            errors.append(f"slop phrase: {phrase}")
    if kind == "findings":
        if AI_WARNING not in text:
            errors.append("missing AI warning")
        if TRUST_WARNING not in text:
            errors.append("missing verify-it-yourself warning")
        if not re.search(r"^SIGNED OFF BY:\s*\S+", text, re.MULTILINE):
            errors.append("missing signoff")
        if "## Sources" not in text:
            errors.append("missing sources")
        urls = list(dict.fromkeys(URL_RE.findall(text[text.find("## Sources"):])) if "## Sources" in text else [])
        if len(urls) < 2:
            errors.append("findings need at least two source URLs")
    elif kind == "changelog":
        if "## Changes" not in text:
            errors.append("missing changes heading")
        if not re.search(r"https://github\.com/[^\s]+/commit/[0-9a-f]{7,40}", text):
            errors.append("changelog needs a direct commit link")
    elif kind == "shitpost":
        if "## Sources" not in text:
            errors.append("shitpost needs source links")
    else:
        errors.append(f"unknown kind: {kind}")
    if network and not errors and "## Sources" in text:
        for url in dict.fromkeys(URL_RE.findall(text[text.find("## Sources"):])):
            try:
                _probe(url)
            except RuntimeError as exc:
                errors.append(str(exc))
    return errors


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("report", type=Path)
    p.add_argument("--kind", choices=["findings", "changelog", "shitpost"], required=True)
    p.add_argument("--no-network", action="store_true")
    a = p.parse_args(argv or sys.argv[1:])
    errors = verify(a.report.read_text(encoding="utf-8"), a.kind, not a.no_network)
    if errors:
        print(f"{a.report}: NOT READY", file=sys.stderr)
        for e in errors:
            print(f"- {e}", file=sys.stderr)
        return 1
    print(f"{a.report}: verified")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
