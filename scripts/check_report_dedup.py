#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

import post_report

GITHUB_COMMIT_RE = re.compile(
    r"https://github\.com/([^/\s<>]+)/([^/\s<>]+)/commit/([0-9a-f]{7,40})",
    re.IGNORECASE,
)
ACTIONS_RUN_RE = re.compile(
    r"https://github\.com/([^/\s<>]+)/([^/\s<>]+)/actions/runs/(\d+)",
    re.IGNORECASE,
)
CORRECTION_RE = re.compile(r"(?im)^#{1,3}\s*correction\b")
FOLLOWUP_RE = re.compile(r"(?im)^#{1,3}\s*follow[- ]?up\b")

CHANNEL_DISPLAY_NAMES = {
    "auto-dig-findings": "The Receipt Desk",
    "findings-shitposts": "Data After Dark",
    "starintel-updates-changelog": "StarIntel Shipyard",
}


def normalize_report_path(report: Path, root: Path) -> Path:
    if report.is_absolute():
        return report
    return root / report


def provenance(markdown: str) -> set[str]:
    tokens = {
        f"commit:{owner.lower()}/{repo.lower()}@{sha.lower()}"
        for owner, repo, sha in GITHUB_COMMIT_RE.findall(markdown)
    }
    tokens.update(
        f"actions:{owner.lower()}/{repo.lower()}@{run_id}"
        for owner, repo, run_id in ACTIONS_RUN_RE.findall(markdown)
    )
    return tokens


def verified_report_ids(state_path: Path) -> set[str]:
    receipts = post_report.load_state(state_path).get("delivery_receipts", {})
    return {
        report_id
        for report_id, receipt in receipts.items()
        if isinstance(receipt, dict)
        and receipt.get("status") == "verified-delivered"
        and receipt.get("message_ids")
        and receipt.get("channel_id")
    }


def prior_provenance(report: Path, channel: str, state_path: Path, root: Path) -> tuple[set[str], dict[str, set[str]]]:
    report = normalize_report_path(report, root)
    verified = verified_report_ids(state_path)
    report_id = report.relative_to(root).as_posix()
    report_dir = root / "reports" / channel
    by_report: dict[str, set[str]] = {}
    combined: set[str] = set()
    for other in sorted(report_dir.glob("*-report.md")):
        other_id = other.relative_to(root).as_posix()
        if other_id == report_id or other_id not in verified:
            continue
        tokens = provenance(other.read_text(encoding="utf-8"))
        if not tokens:
            continue
        by_report[other_id] = tokens
        combined.update(tokens)
    return combined, by_report


def exact_duplicate(report: Path, channel: str, state_path: Path, root: Path) -> str | None:
    report = normalize_report_path(report, root)
    display_name = CHANNEL_DISPLAY_NAMES.get(channel)
    if display_name is None:
        return None
    markdown = report.read_text(encoding="utf-8")
    digest = post_report.report_digest(display_name, markdown)
    report_id = report.relative_to(root).as_posix()
    receipts = post_report.load_state(state_path).get("delivery_receipts", {})
    for other_id, receipt in receipts.items():
        if other_id == report_id or not isinstance(receipt, dict):
            continue
        if (
            receipt.get("status") == "verified-delivered"
            and receipt.get("message_ids")
            and receipt.get("channel_id")
            and receipt.get("report_digest") == digest
        ):
            return other_id
    return None


def duplicate_reason(report: Path, channel: str, state_path: Path, root: Path) -> str | None:
    report = normalize_report_path(report, root)
    if channel not in CHANNEL_DISPLAY_NAMES:
        return None

    exact = exact_duplicate(report, channel, state_path, root)
    if exact is not None:
        return f"exact report body already delivered as {exact}"

    markdown = report.read_text(encoding="utf-8")
    current = provenance(markdown)
    if not current:
        return None

    previous, by_report = prior_provenance(report, channel, state_path, root)
    overlap = current & previous
    new_tokens = current - previous

    if CORRECTION_RE.search(markdown):
        return None

    if FOLLOWUP_RE.search(markdown):
        if overlap and not new_tokens:
            return "FOLLOW-UP reuses only already-delivered provenance; add genuinely new landed provenance or make it a CORRECTION"
        return None

    if not overlap:
        return None

    offenders = sorted(
        report_id for report_id, tokens in by_report.items() if tokens & overlap
    )
    overlap_text = ", ".join(sorted(overlap))
    offender_text = ", ".join(offenders[:3])
    if len(offenders) > 3:
        offender_text += f", +{len(offenders) - 3} more"
    return (
        f"reuses already-delivered provenance ({overlap_text}) from {offender_text}; "
        "new reports must use new provenance, or use an explicit CORRECTION/FOLLOW-UP heading when editorially justified"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("--channel", required=True)
    parser.add_argument("--state-file", type=Path, required=True)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    report = normalize_report_path(args.report, root)
    state_file = args.state_file if args.state_file.is_absolute() else root / args.state_file
    reason = duplicate_reason(report, args.channel, state_file, root)
    if reason is None:
        return 0
    print(f"duplicate report blocked: {args.report}: {reason}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
