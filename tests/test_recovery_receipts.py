import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).parents[1]
REPORT_ID = "reports/starintel-updates-changelog/recovery-test-report.md"
CHANNEL_NAME = "StarIntel Shipyard"
MARKDOWN = "## RECOVERY TEST\n\n## Changes\n\nAlready delivered.\n"


def load_module(name: str, path: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


post_report = load_module("post_report", "scripts/post_report.py")
merge_delivery_state = load_module("merge_delivery_state", "scripts/merge_delivery_state.py")


class RecoveryReceiptTests(unittest.TestCase):
    def test_recovery_receipt_suppresses_delivery_scan(self):
        receipt = {
            "status": "verified-delivered",
            "channel_name": CHANNEL_NAME,
            "channel_id": "channel-1",
            "message_ids": ["message-1"],
            "report_digest": post_report.report_digest(CHANNEL_NAME, MARKDOWN),
        }
        merged = merge_delivery_state.merge_delivery_receipts(
            {"delivery_receipts": {}},
            {"delivery_receipts": {REPORT_ID: receipt}},
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            state_path = Path(temp_dir) / "published.json"
            state_path.write_text(json.dumps(merged), encoding="utf-8")
            self.assertTrue(
                post_report.already_reported(
                    state_path,
                    REPORT_ID,
                    CHANNEL_NAME,
                    MARKDOWN,
                )
            )

    def test_catchup_applies_recovery_before_drain(self):
        workflow = (ROOT / ".github" / "workflows" / "publish-catchup.yml").read_text(
            encoding="utf-8"
        )
        self.assertLess(
            workflow.index("Apply verified recovery receipts"),
            workflow.index("Drain all unverified reports oldest first"),
        )

    def test_resolved_recovery_manifest_is_empty(self):
        recovery = json.loads(
            (ROOT / "state" / "recovery-receipts.json").read_text(encoding="utf-8")
        )
        self.assertEqual({}, recovery["delivery_receipts"])


if __name__ == "__main__":
    unittest.main()
