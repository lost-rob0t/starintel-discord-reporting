#!/usr/bin/env python3
"""One-shot, explicitly requested editorial batch. Does not alter global dedupe."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "editorial/2026-09-17"
REPORTS = ROOT / "reports/starintel-updates-changelog"
STATE = ROOT / "state/published.json"
PLAN = Path("/tmp/shipyard-september-plan.json")
WORKFLOW = ".github/workflows/september-editorial-once.yml"
PREFIX = "2026-09-17-"
EXISTING = {
    "10-starintel-server": ("79913f924f3a85aa9257797dd70a86aec5b39c4a", "The additional coverage includes the quarantine concurrency failure and its settlement regression, alongside the previously announced retention and telemetry work."),
    "11-star-lang": ("8f4e6c420e71edbb92945fae17f1632ceddf574e", "This expands the transport summary with runtime authority, failure-path verification and actor-option rejection. Unsupported actor options must be rejected rather than silently accepted as an executable contract."),
    "12-tek9-star-git": ("fc868f16650dd65459492e01028a1aa2eaf9e38e", "This adds the archive runtime-packaging and round-trip evidence, with a closer account of custody validation and restore boundaries."),
    "13-prolog-rlm": ("f1ba63ce02ff797a1d89cf113d076417f050832c", "This expands the summary with the review-repair evidence for publication atomicity, multi-project isolation, incomplete indexes and the native grouped-capture regression."),
    "14-quasar-runtime": ("371035db85ad2f1d0c92ac17d5d543544c1d4699", "This adds the concrete runtime-build and startup-validation implementation behind the earlier packaging summary."),
    "15-zara-plugins": ("4f0687050908a4c46e2d6b6f920aa6a00677332b", "The new coverage includes Local Recall's transactional library/wrapper rollback, in addition to the already summarized Agent Zero error sanitization."),
    "16-a0-symbolics": ("43800dad7a2297a4fdf971cc0c415c43612748aa", "This adds the detailed replay proof, resume handling and fork-surface maintenance evidence behind the distribution-update summary."),
    "17-hackmode": ("308de7275bd5a85f4c55535399180950794f7923", "This adds the implementation-level checkpoint format and replacement/truncation regression evidence behind the earlier replay-integrity summary."),
    "18-llm-log": ("ae6f20cf06f589ea42f68e687dce82807671e8e8", "This edition covers historical backfill, dataset provenance and the separate quota/coverage contracts in depth."),
    "19-starintel-document-profile": ("06044aa27e44e549523c542299a1a41c058c4c0e", "This adds the release manifest's exact envelope/profile distinction, artifact-reference policy and sensitive-header classes to the earlier profile summary."),
}


def run(args: list[str], *, checked: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(args, cwd=ROOT, text=True, check=False)
    if checked and result.returncode:
        raise RuntimeError(f"Command failed with exit {result.returncode}: {args[0]}")
    return result


def git_output(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def receipts() -> dict:
    return json.loads(STATE.read_text()).get("delivery_receipts", {})


def delivered(receipt: dict | None) -> bool:
    return bool(receipt and receipt.get("status") == "verified-delivered"
                and receipt.get("message_ids") and receipt.get("channel_id"))


def report_id(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def prepare() -> None:
    observed = receipts()
    paths: list[Path] = []
    for slug, (expected_blob, note) in EXISTING.items():
        path = REPORTS / f"{PREFIX}{slug}-report.md"
        if delivered(observed.get(report_id(path))):
            raise RuntimeError(f"Refusing to edit delivered article: {path.name}")
        if git_output("hash-object", str(path)) != expected_blob:
            raise RuntimeError(f"Unreviewed concurrent article edit: {path.name}")
        text = path.read_text()
        head, tail = text.split("\n", 1)
        path.write_text(f"{head}\n\n## FOLLOW-UP\n\n{note}\n{tail}")
        paths.append(path)
    sources = sorted(SOURCE.glob(f"{PREFIX}*-report.md"))
    if len(sources) != 22:
        raise RuntimeError("Expected exactly 22 reviewed companion/additional articles")
    for source in sources:
        path = REPORTS / source.name
        if path.exists():
            raise RuntimeError(f"Refusing to overwrite existing article: {path.name}")
        text = source.read_text().replace("## Downloads and sources", "## Sources")
        path.write_text(text)
        paths.append(path)
    if len(paths) != 32:
        raise RuntimeError("Editorial batch cardinality mismatch")
    digests = [hashlib.sha256(path.read_bytes()).hexdigest() for path in paths]
    if len(set(digests)) != len(digests):
        raise RuntimeError("Exact duplicate body inside editorial batch")
    # Both requested editions are reviewed against the same pre-batch history.
    # Nothing is delivered until every article passes the unchanged global guard.
    for path in paths:
        relative = report_id(path)
        run([sys.executable, "scripts/check_report_dedup.py", relative,
             "--channel", "starintel-updates-changelog", "--state-file", str(STATE)])
        run([sys.executable, "scripts/verify_report.py", relative,
             "--kind", "changelog", "--no-network"])
    PLAN.write_text(json.dumps([report_id(path) for path in paths], indent=2))
    print(f"Preflight passed for {len(paths)} reviewed articles", flush=True)


def commit_reports() -> None:
    paths = json.loads(PLAN.read_text())
    run(["git", "config", "user.name", "starintel-report-bot"])
    run(["git", "config", "user.email", "actions@users.noreply.github.com"])
    run(["git", "add", "--", *paths])
    run(["git", "commit", "-m", "reports: expand project changelogs and add seventeen Android companions"])
    for _ in range(5):
        run(["git", "pull", "--rebase", "origin", "main"])
        if run(["git", "push", "origin", "HEAD:main"], checked=False).returncode == 0:
            return
    raise RuntimeError("Unable to persist reviewed article bodies")


def publish() -> None:
    paths = json.loads(PLAN.read_text())
    webhook = os.environ.get("SHIPYARD_WEBHOOK", "")
    if not webhook:
        raise RuntimeError("Missing configured Shipyard webhook")
    # Revalidate all members against the latest durable pre-batch receipts.
    run(["git", "fetch", "--quiet", "origin", "main"])
    latest = subprocess.check_output(["git", "show", "origin/main:state/published.json"], cwd=ROOT)
    STATE.write_bytes(latest)
    for path in paths:
        if delivered(receipts().get(path)):
            raise RuntimeError("An article was concurrently delivered; reconcile before sending")
        run([sys.executable, "scripts/check_report_dedup.py", path,
             "--channel", "starintel-updates-changelog", "--state-file", str(STATE)])
    for path in paths:
        # Do not print arguments containing the secret or auto-repeat an ambiguous failure.
        result = run([sys.executable, "scripts/post_report.py", "--channel-name",
                      "StarIntel Shipyard", "--webhook-url", webhook, "--report", path,
                      "--report-id", path, "--state-file", str(STATE)], checked=False)
        if result.returncode:
            raise RuntimeError(f"Delivery stopped at {path}; inspect receipts before retry")
        receipt = receipts().get(path)
        if not delivered(receipt) or receipt.get("channel_id") != "1539717118218469416":
            raise RuntimeError(f"Missing matching-channel verified receipt: {path}")
        print(f"VERIFIED {path} {','.join(receipt['message_ids'])}", flush=True)


def persist() -> None:
    if not PLAN.exists():
        print("No validated batch to persist")
        return
    run_state = Path("/tmp/shipyard-september-receipts.json")
    run_state.write_bytes(STATE.read_bytes())
    paths = json.loads(PLAN.read_text())
    data = json.loads(run_state.read_text()).get("delivery_receipts", {})
    complete = all(delivered(data.get(path)) for path in paths)
    for _ in range(5):
        run(["git", "fetch", "--quiet", "origin", "main"])
        latest = Path("/tmp/shipyard-september-latest.json")
        latest.write_bytes(subprocess.check_output(["git", "show", "origin/main:state/published.json"], cwd=ROOT))
        merged = Path("/tmp/shipyard-september-merged.json")
        run([sys.executable, "scripts/merge_delivery_state.py", "--latest-state", str(latest),
             "--run-state", str(run_state), "--output", str(merged)])
        run(["git", "reset", "--hard", "origin/main"])
        STATE.write_bytes(merged.read_bytes())
        ledger = SOURCE / "delivery-ledger.json"
        ledger.write_text(json.dumps({"edition": "2026-09-17-expanded-and-android",
            "complete": complete, "receipts": {path: data.get(path) for path in paths}}, indent=2) + "\n")
        run(["git", "add", "state/published.json", str(ledger.relative_to(ROOT))])
        if complete and (ROOT / WORKFLOW).exists():
            run(["git", "rm", "--", WORKFLOW])
        if run(["git", "diff", "--cached", "--quiet"], checked=False).returncode == 0:
            return
        run(["git", "commit", "-m", "state: preserve verified editorial deliveries and retire completed one-shot"])
        if run(["git", "push", "origin", "HEAD:main"], checked=False).returncode == 0:
            print(f"Persisted batch receipts; complete={complete}", flush=True)
            return
    raise RuntimeError("Receipt persistence raced repeatedly; retain uploaded recovery artifact")


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2 or sys.argv[1] not in {"prepare", "commit", "publish", "persist"}:
            raise ValueError("Expected prepare, commit, publish or persist")
        {"prepare": prepare, "commit": commit_reports, "publish": publish, "persist": persist}[sys.argv[1]]()
    except (RuntimeError, ValueError, OSError) as error:
        print(f"Editorial batch stopped: {error}", file=sys.stderr)
        raise SystemExit(1)
