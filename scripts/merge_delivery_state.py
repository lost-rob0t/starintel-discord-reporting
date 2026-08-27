#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def verified(receipt: object) -> bool:
    return (
        isinstance(receipt, dict)
        and receipt.get("status") == "verified-delivered"
        and bool(receipt.get("message_ids"))
        and bool(receipt.get("channel_id"))
    )


def merge_delivery_receipts(latest: dict, run: dict) -> dict:
    merged = json.loads(json.dumps(latest))
    destination = merged.setdefault("delivery_receipts", {})

    for report_id, receipt in run.get("delivery_receipts", {}).items():
        if not verified(receipt):
            continue

        current = destination.get(report_id)
        if current is None:
            destination[report_id] = receipt
            continue
        if current == receipt:
            continue
        if verified(current):
            raise ValueError(f"conflicting verified receipt for {report_id}")
        destination[report_id] = receipt

    return merged


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--latest-state", type=Path, required=True)
    parser.add_argument("--run-state", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    merged = merge_delivery_receipts(load(args.latest_state), load(args.run_state))
    args.output.write_text(json.dumps(merged, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
