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
SOURCE_HEADING_RE = re.compile(r"^(?:##\s+Sources|Sources:)\s*$", re.MULTILINE)
OPERATIONAL_SOURCES_HEADING = "## Operational Sources"
PRIVATE_SOURCE_ATTESTATION_HEADING = "## Private Source Attestation"
ACTIONS_RUN_RE = re.compile(r"https://github\.com/[^\s]+/actions/runs/\d+")
GITHUB_URL_RE = re.compile(r"https://github\.com/[^\s)>\]}]+")
SLOP = (
    "it's important to note",
    "it is important to note",
    "in conclusion",
    "key takeaway",
    "comprehensive overview",
    "delve into",
    "furthermore",
    "moreover",
    "seamlessly",
)
AI_WARNING = "This was written by AI. check it yourself."
DERIVED_WARNING = "Please double check findings as this was llm derived."
TRUST_WARNING = "dont trust this report as a source. dont even trust nsaspy."
SIGNOFF = "SIGNED OFF BY: N545PY"


def _source_section(text: str) -> str:
    match = SOURCE_HEADING_RE.search(text)
    return text[match.start() :] if match else ""


def _probe(url: str, timeout: float = 15.0) -> None:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "starintel-discord-reporting/1.0"},
        method="HEAD",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            if 200 <= response.status < 400:
                return
    except urllib.error.HTTPError as exc:
        if exc.code not in {403, 405}:
            raise RuntimeError(f"source HTTP {exc.code}: {url}") from exc

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "starintel-discord-reporting/1.0",
            "Range": "bytes=0-0",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            if 200 <= response.status < 400:
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
    if "nsa spy" in lowered:
        errors.append("write nsaspy as one word")
    for phrase in SLOP:
        if phrase in lowered:
            errors.append(f"slop phrase: {phrase}")

    source_text = _source_section(text)

    if kind == "findings":
        required = (AI_WARNING, DERIVED_WARNING, TRUST_WARNING, SIGNOFF)
        for value in required:
            if value not in text:
                errors.append(f"missing findings footer line: {value}")
        if re.search(r"^SIGNED OFF BY:\s*nsaspy\s*$", text, re.I | re.MULTILINE):
            errors.append("nsaspy must never be the signer")
        if not source_text:
            errors.append("missing sources")
        source_urls = list(dict.fromkeys(URL_RE.findall(source_text)))
        if len(source_urls) < 2:
            errors.append("findings need at least two source URLs")
        if not re.search(
            r"https://github\.com/[^\s]+/commit/[0-9a-f]{7,40}", text
        ):
            errors.append("findings need the direct landed Auto-Dig commit link")

    elif kind == "changelog":
        if "## Changes" not in text:
            errors.append("missing changes heading")
        operational = OPERATIONAL_SOURCES_HEADING in text
        private_source = PRIVATE_SOURCE_ATTESTATION_HEADING in text
        if operational and private_source:
            errors.append("changelog cannot mix operational and private-source attestations")
        elif private_source:
            private_text = text[text.find(PRIVATE_SOURCE_ATTESTATION_HEADING) :]
            if GITHUB_URL_RE.search(private_text) or GITHUB_URL_RE.search(text[: text.find(PRIVATE_SOURCE_ATTESTATION_HEADING)]):
                errors.append("private-source changelog must not expose GitHub links")
            if "configured private canonical branch" not in private_text:
                errors.append("private-source changelog needs canonical-branch attestation")
        elif operational:
            operational_text = text[text.find(OPERATIONAL_SOURCES_HEADING) :]
            if not ACTIONS_RUN_RE.search(operational_text):
                errors.append("operational changelog needs a direct GitHub Actions run source")
        elif not re.search(
            r"https://github\.com/[^\s]+/commit/[0-9a-f]{7,40}", text
        ):
            errors.append("changelog needs a direct landed commit link")

    elif kind == "shitpost":
        if not source_text:
            errors.append("shitpost needs source links")
        if not URL_RE.search(source_text):
            errors.append("shitpost needs at least one source URL")
        if "SIGNED OFF BY:" in text:
            errors.append("shitposts must not carry a signoff")
        if any(
            value in text
            for value in (AI_WARNING, DERIVED_WARNING, TRUST_WARNING)
        ):
            errors.append("shitposts must not copy the serious findings footer")

    else:
        errors.append(f"unknown kind: {kind}")

    if network and not errors and source_text:
        for url in dict.fromkeys(URL_RE.findall(source_text)):
            try:
                _probe(url)
            except RuntimeError as exc:
                errors.append(str(exc))

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument(
        "--kind",
        choices=["findings", "changelog", "shitpost"],
        required=True,
    )
    parser.add_argument("--no-network", action="store_true")
    args = parser.parse_args(argv or sys.argv[1:])

    errors = verify(
        args.report.read_text(encoding="utf-8"),
        args.kind,
        not args.no_network,
    )
    if errors:
        print(f"{args.report}: NOT READY", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"{args.report}: verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
