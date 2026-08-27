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
GITHUB_COMMIT_RE = re.compile(
    r"https://github\.com/([^/\s]+)/([^/\s]+)/commit/([0-9a-f]{7,40})",
    re.IGNORECASE,
)
CORRECTION_RE = re.compile(r"(?im)^#{1,3}\s*correction\b")
FOLLOWUP_RE = re.compile(r"(?im)^#{1,3}\s*follow[- ]?up\b")


def normalized_github_commits(markdown: str) -> set[str]:
    return {
        f"{owner.lower()}/{repo.lower()}@{sha.lower()}"
        for owner, repo, sha in GITHUB_COMMIT_RE.findall(markdown)
    }


def autodig_commits(markdown: str) -> set[str]:
    return {sha.lower() for sha in AUTO_DIG_COMMIT_RE.findall(markdown)}


def explicit_mode(markdown: str) -> str | None:
    if CORRECTION_RE.search(markdown):
        return "correction"
    if FOLLOWUP_RE.search(markdown):
        return "followup"
    return None


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


def report_provenance(markdown: str, channel: str) -> set[str]:
    if channel in {"auto-dig-findings", "findings-shitposts"}:
        return {f"autodig@{sha}" for sha in autodig_commits(markdown)}
    if channel == "starintel-updates-changelog":
        return normalized_github_commits(markdown)
    return set()


def prior_provenance(channel: str, state_path: Path, root: Path, report_id: str) -> dict[str, set[str]]:
    verified = verified_report_ids(state_path)
    report_dir = root / "reports" / channel
    prior: dict[str, set[str]] = {}
    if not report_dir.is_dir():
        return prior
    for other in sorted(report_dir.glob("*-report.md")):
        other_id = other.relative_to(root).as_posix()
        if other_id == report_id or other_id not in verified:
            continue
        provenance = report_provenance(other.read_text(encoding="utf-8"), channel)
        if provenance:
            prior[other_id] = provenance
    return prior


def duplicate_source(report: Path, channel: str, state_path: Path, root: Path) -> tuple[str, str] | None:
    markdown = report.read_text(encoding="utf-8")
    current = report_provenance(markdown, channel)
    if not current:
        return None

    report_id = report.relative_to(root).as_posix()
    prior = prior_provenance(channel, state_path, root, report_id)
    used = set().union(*prior.values()) if prior else set()
    overlap = current & used
    if not overlap:
        return None

    mode = explicit_mode(markdown)
    if mode == "correction":
        return None
    if mode == "followup" and (current - used):
        return None

    duplicated = sorted(overlap)[0]
    for other_id, provenance in prior.items():
        if duplicated in provenance:
            return other_id, duplicated
    raise AssertionError("overlap source has no originating report")


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

    other_id, provenance = duplicate
    print(
        f"duplicate source provenance: {args.report} reuses {provenance} already delivered by {other_id}; "
        "use CORRECTION for a correction, or FOLLOW-UP with at least one genuinely new landed source",
        flush=True,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
