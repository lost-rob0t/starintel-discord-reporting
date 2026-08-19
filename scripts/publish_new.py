#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import post_report
import verify_report

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "state" / "published.json"
BASELINE = ROOT / "state" / "manual-publisher-baseline.txt"
REPORT_GLOBS = (
    "reports/auto-dig-findings/*-report.md",
    "reports/findings-shitposts/*-report.md",
    "reports/starintel-updates-changelog/*-report.md",
)
CHANNELS = {
    "auto-dig-findings": ("findings", "AUTO_DIG_FINDINGS"),
    "findings-shitposts": ("shitpost", "FINDINGS_SHITPOSTS"),
    "starintel-updates-changelog": ("changelog", "STARINTEL_UPDATES_CHANGELOG"),
}
MEDIA_EXTENSIONS = ("png", "jpg", "jpeg", "gif", "webp")


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def load_dotenv() -> None:
    """Load the repo .env without requiring an active direnv shell."""
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
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        if key:
            os.environ.setdefault(key, value)


def load_state() -> dict:
    if not STATE.exists():
        return {"posted": [], "published_reports": []}

    data = json.loads(STATE.read_text(encoding="utf-8"))
    data.setdefault("posted", [])
    data.setdefault("published_reports", [])
    return data


def write_state(state: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def report_attachment(report: Path) -> Path | None:
    for extension in MEDIA_EXTENSIONS:
        candidate = report.with_suffix(f".{extension}")
        if candidate.is_file():
            return candidate
    return None


def changed_reports(cursor: str, head: str) -> list[str]:
    result = git(
        "diff",
        "--name-only",
        "--diff-filter=AM",
        cursor,
        head,
        "--",
        *REPORT_GLOBS,
    )
    paths = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return sorted(dict.fromkeys(paths), key=lambda value: (Path(value).name, value))


def ensure_cursor_is_ancestor(cursor: str, head: str) -> None:
    result = git("merge-base", "--is-ancestor", cursor, head, check=False)
    if result.returncode != 0:
        raise RuntimeError(
            f"publisher cursor {cursor} is not an ancestor of HEAD {head}; "
            "refusing to guess and risk duplicate posts"
        )


def persist_state_commit() -> None:
    git("add", "--", "state/published.json")
    staged = git("diff", "--cached", "--quiet", "--", "state/published.json", check=False)
    if staged.returncode == 0:
        return
    if staged.returncode != 1:
        raise RuntimeError(staged.stderr.strip() or "failed checking publisher state")

    commit = subprocess.run(
        [
            "git",
            "-C",
            str(ROOT),
            "commit",
            "-m",
            "state: record manual Discord publish",
            "--",
            "state/published.json",
        ]
    )
    if commit.returncode != 0:
        raise RuntimeError("failed to commit publisher state")

    push = subprocess.run(["git", "-C", str(ROOT), "push", "origin", "HEAD:main"])
    if push.returncode != 0:
        raise RuntimeError(
            "Discord publication succeeded and state is committed locally, but pushing "
            "state failed. Do not reset the repo. Pull/rebase, then push before publishing again."
        )


def main() -> int:
    if len(sys.argv) != 1:
        print("publish_new.py takes zero arguments", file=sys.stderr)
        return 2

    load_dotenv()

    branch = git("branch", "--show-current").stdout.strip()
    if branch != "main":
        print(f"refusing to publish from branch {branch!r}; switch to main first", file=sys.stderr)
        return 2

    head = git("rev-parse", "HEAD").stdout.strip()
    state = load_state()
    cursor = state.get("manual_cursor")
    bootstrap = cursor is None

    if cursor is None:
        if not BASELINE.is_file():
            print("missing manual publisher baseline", file=sys.stderr)
            return 2
        cursor = BASELINE.read_text(encoding="utf-8").strip()

    ensure_cursor_is_ancestor(cursor, head)
    reports = changed_reports(cursor, head)
    published_paths = set(state.get("published_reports", []))

    if not reports:
        if bootstrap:
            state["manual_cursor"] = head
            write_state(state)
            persist_state_commit()
            print(f"initialized publisher cursor at {head}; historical reports were not posted")
        else:
            print("no new report files")
        return 0

    print(f"found {len(reports)} new report file(s) since {cursor[:12]}")

    for relative in reports:
        report = ROOT / relative
        channel = report.parent.name
        mapping = CHANNELS.get(channel)
        if mapping is None:
            continue
        kind, secret_name = mapping

        if relative in published_paths or post_report.already_reported(STATE, relative):
            print(f"skip already-published path: {relative}")
            continue

        markdown = report.read_text(encoding="utf-8")
        if post_report.already_posted(STATE, channel, markdown):
            print(f"skip duplicate content: {relative}")
            published_paths.add(relative)
            state = load_state()
            state["published_reports"] = sorted(published_paths)
            write_state(state)
            continue

        errors = verify_report.verify(markdown, kind, False)
        if errors:
            print(f"{relative}: NOT READY", file=sys.stderr)
            for error in errors:
                print(f"- {error}", file=sys.stderr)
            return 1

        webhook = os.environ.get(secret_name, "").strip()
        if not webhook:
            print(f"missing {secret_name}; add it to .env", file=sys.stderr)
            return 2

        args = [
            "--channel-name",
            channel,
            "--webhook-url",
            webhook,
            "--report",
            str(report),
            "--report-id",
            relative,
            "--state-file",
            str(STATE),
        ]
        attachment = report_attachment(report)
        if attachment is not None:
            args.extend(["--attachment", str(attachment)])

        result = post_report.main(args)
        if result != 0:
            return result

        published_paths.add(relative)
        state = load_state()
        state["published_reports"] = sorted(published_paths)
        write_state(state)

    state = load_state()
    state["published_reports"] = sorted(published_paths)
    state["manual_cursor"] = head
    write_state(state)
    persist_state_commit()
    print(f"publisher cursor advanced to {head}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
