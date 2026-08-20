#!/usr/bin/env python3
from __future__ import annotations

import base64
import json
import os
import subprocess
import sys
from pathlib import Path

import post_report
import verify_report

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "state" / "published.json"
REPORT_GLOBS = (
    "reports/auto-dig-findings/*-report.md",
    "reports/findings-shitposts/*-report.md",
    "reports/starintel-updates-changelog/*-report.md",
)
CHANNELS = {
    "auto-dig-findings": ("findings", "AUTO_DIG_FINDINGS", "The Receipt Desk"),
    "findings-shitposts": ("shitpost", "FINDINGS_SHITPOSTS", "Data After Dark"),
    "starintel-updates-changelog": ("changelog", "STARINTEL_UPDATES_CHANGELOG", "StarIntel Shipyard"),
}
MEDIA_EXTENSIONS = ("png", "jpg", "jpeg", "gif", "webp")


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", "-C", str(ROOT), *args], check=check, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def load_dotenv() -> None:
    path = ROOT / ".env"
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key, value = key.strip(), value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        if key:
            os.environ.setdefault(key, value)


def load_state() -> dict:
    return post_report.load_state(STATE)


def write_state(state: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def all_reports() -> list[str]:
    paths = []
    for pattern in REPORT_GLOBS:
        paths.extend(path.relative_to(ROOT).as_posix() for path in ROOT.glob(pattern))
    return sorted(dict.fromkeys(paths), key=lambda value: (Path(value).name, value))


def prune_verified_blockers(reports: list[str]) -> int:
    state = load_state()
    blockers = state.setdefault("backlog_blockers", {})
    stale = [
        path
        for path in tuple(blockers)
        if path in reports and post_report.already_reported(STATE, path)
    ]
    for path in stale:
        del blockers[path]
    if stale:
        write_state(state)
    return len(stale)


def _decode_b64(path: Path, target: Path) -> Path:
    target.write_bytes(base64.b64decode(path.read_bytes()))
    return target


def report_attachment(report: Path) -> Path | None:
    stem = report.with_suffix("")
    for ext in MEDIA_EXTENSIONS:
        direct = Path(f"{stem}.{ext}")
        if direct.is_file():
            return direct
        encoded = Path(f"{direct}.b64")
        if encoded.is_file():
            return _decode_b64(encoded, direct)
        first = Path(f"{encoded}.part00")
        if first.is_file():
            chunks = sorted(first.parent.glob(first.name[:-2] + "*"))
            data = b"".join(chunk.read_bytes() for chunk in chunks)
            direct.write_bytes(base64.b64decode(data))
            return direct
    return None


def persist_state_commit(message: str = "state: record verified Discord deliveries") -> None:
    git("add", "--", "state/published.json")
    staged = git("diff", "--cached", "--quiet", "--", "state/published.json", check=False)
    if staged.returncode == 0:
        return
    if staged.returncode != 1:
        raise RuntimeError(staged.stderr.strip() or "failed checking publisher state")
    commit = subprocess.run(["git", "-C", str(ROOT), "commit", "-m", message, "--", "state/published.json"])
    if commit.returncode != 0:
        raise RuntimeError("failed to commit publisher state")
    pull = subprocess.run(["git", "-C", str(ROOT), "pull", "--rebase", "origin", "main"])
    if pull.returncode != 0:
        raise RuntimeError("verified delivery state committed locally but rebase failed")
    push = subprocess.run(["git", "-C", str(ROOT), "push", "origin", "HEAD:main"])
    if push.returncode != 0:
        raise RuntimeError("verified delivery state committed locally but push failed")


def record_blocker(relative: str, reason: str) -> None:
    state = load_state()
    blockers = state.setdefault("backlog_blockers", {})
    blockers[relative] = {"status": "blocked", "reason": reason}
    write_state(state)


def clear_blocker(relative: str) -> None:
    state = load_state()
    blockers = state.setdefault("backlog_blockers", {})
    if relative in blockers:
        del blockers[relative]
        write_state(state)


def main() -> int:
    if len(sys.argv) != 1:
        print("publish_new.py takes zero arguments", file=sys.stderr)
        return 2
    load_dotenv()
    branch = git("branch", "--show-current").stdout.strip()
    if branch != "main":
        print(f"refusing to publish from branch {branch!r}", file=sys.stderr)
        return 2

    reports = all_reports()
    pruned = prune_verified_blockers(reports)
    eligible = [path for path in reports if not post_report.already_reported(STATE, path)]
    print(
        f"backlog scan: total={len(reports)} verified={len(reports) - len(eligible)} "
        f"remaining={len(eligible)} stale_blockers_pruned={pruned}"
    )

    delivered = {name: 0 for name in CHANNELS}
    blocked = 0
    for relative in eligible:
        report = ROOT / relative
        channel = report.parent.name
        mapping = CHANNELS.get(channel)
        if mapping is None:
            continue
        kind, secret_name, display_name = mapping
        markdown = report.read_text(encoding="utf-8")
        errors = verify_report.verify(markdown, kind, False)
        if errors:
            blocked += 1
            reason = "; ".join(errors)
            record_blocker(relative, reason)
            print(f"BLOCKED {relative}: {reason}", file=sys.stderr)
            continue

        secret = os.environ.get(secret_name, "").strip()
        if not secret:
            reason = f"missing configured destination secret for {channel}"
            record_blocker(relative, reason)
            persist_state_commit("state: record Discord backlog blocker")
            print(f"BLOCKED {relative}: {reason}", file=sys.stderr)
            return 2

        args = [
            "--channel-name", display_name,
            "--webhook-url", secret,
            "--report", str(report),
            "--report-id", relative,
            "--state-file", str(STATE),
        ]
        attachment = report_attachment(report)
        if attachment is not None:
            args.extend(["--attachment", str(attachment)])
        try:
            result = post_report.main(args)
        except post_report.DestinationMismatch as exc:
            reason = str(exc)
            record_blocker(relative, reason)
            persist_state_commit("state: record Discord destination mismatch")
            print(f"DESTINATION MISMATCH {channel}: {reason}", file=sys.stderr)
            return 3
        except Exception as exc:
            reason = f"delivery failed: {exc}"
            record_blocker(relative, reason)
            persist_state_commit("state: record Discord delivery blocker")
            print(f"BLOCKED {relative}: {reason}", file=sys.stderr)
            return 4
        if result != 0:
            record_blocker(relative, f"publisher exited {result}")
            persist_state_commit("state: record Discord delivery blocker")
            return result
        clear_blocker(relative)
        delivered[channel] += 1

    state = load_state()
    state["last_backlog_scan"] = {
        "total_reports": len(reports),
        "verified_deliveries": len([p for p in reports if post_report.already_reported(STATE, p)]),
        "blocked": blocked,
        "delivered_this_run": delivered,
        "stale_blockers_pruned": pruned,
    }
    write_state(state)
    persist_state_commit()
    remaining = [path for path in reports if not post_report.already_reported(STATE, path)]
    print(f"backlog complete: delivered={delivered} blocked={blocked} remaining={len(remaining)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())