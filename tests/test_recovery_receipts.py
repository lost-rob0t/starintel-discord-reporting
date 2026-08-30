import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).parents[1]
REPORT_ID = "reports/starintel-updates-changelog/2026-08-27T04-52-01Z-report.md"


def load_post_report():
    spec = importlib.util.spec_from_file_location(
        "post_report", ROOT / "scripts" / "post_report.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


post_report = load_post_report()


class RecoveryReceiptTests(unittest.TestCase):
    def test_recovered_receipt_matches_restored_report_exactly(self):
        recovery = json.loads(
            (ROOT / "state" / "recovery-receipts.json").read_text(encoding="utf-8")
        )
        receipt = recovery["delivery_receipts"][REPORT_ID]
        markdown = (ROOT / REPORT_ID).read_text(encoding="utf-8")

        self.assertEqual("verified-delivered", receipt["status"])
        self.assertEqual(["1542396790853210122"], receipt["message_ids"])
        self.assertEqual("1539717118218469416", receipt["channel_id"])
        self.assertEqual("StarIntel Shipyard", receipt["channel_name"])
        self.assertEqual(
            post_report.report_digest("StarIntel Shipyard", markdown),
            receipt["report_digest"],
        )


if __name__ == "__main__":
    unittest.main()
