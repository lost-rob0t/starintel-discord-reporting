#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

AUTO_DIG_COMMIT_RE = re.compile(
    r"https://github\.com/lost-rob0t/starintel-gpt-auto-dig/commit/([0-9a-f]{7,40})",
    re.IGNORECASE,
)
FOLLOWUP_RE = re.compile(r"(?im)^#{1,3}\s*(?:correction|follow[- ]?up)\b")


def source_commits(markdown: str) -> set[str]:
    return {match.lower() for match in AUTO_DIG_COMMIT_RE.findall(markdown)}


def explicit_followup(markdown: str) -> bool:
    return bool(FOLLOWUP_RE.search(markdown))


def verified_report_ids(state_path: Path) -> set[str]:
    if not state_path.is_file():
        return set()
    state = json.loads(state_path.read_text(encoding="utf-8"))
    receipts = state.get("delivery_receipts", {})
    return {
        report_id
        for report_id, receipt in receipts.items()
        if isinstance(receipt, dict)
        and receipt.get("status") == "verified-delivered"
        and receipt.get("message_ids")
        and receipt.get("channel_id")
    }


def duplicate_source(report: Path, channel: str, state_path: Path, root: Path) -> tuple[str, str] | None:
    if channel not in {"auto-dig-findings", "findings-shitposts"}:
        return None

    markdown = report.read_text(encoding="utf-8")
    if explicit_followup(markdown):
        return None

    commits = source_commits(markdown)
    if not commits:
        return None

    verified = verified_report_ids(state_path)
    report_id = report.relative_to(root).as_posix()
    report_dir = root / "reports" / channel
    for other in sorted(report_dir.glob("*-report.md")):
        other_id = other.relative_to(root).as_posix()
        if other_id == report_id or other_id not in verified:
            continue
        overlap = commits & source_commits(other.read_text(encoding="utf-8"))
        if overlap:
            return other_id, sorted(overlap)[0]
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("--channel", required=True)
    parser.add_argument("--state-file", type=Path, required=True)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    duplicate = duplicate_source(args.report, args.channel, args.state_file, root)
    if duplicate is None:
        return 0

    other_id, commit = duplicate
    print(
        f"duplicate source provenance: {args.report} reuses Auto-Dig commit {commit} "
        f"already delivered by {other_id}; use an explicit CORRECTION or FOLLOW-UP heading only for materially new follow-up content",
        flush=True,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
