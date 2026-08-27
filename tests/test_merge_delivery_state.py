import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).parents[1]


def load_module():
    spec = importlib.util.spec_from_file_location(
        "merge_delivery_state", ROOT / "scripts" / "merge_delivery_state.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


merge = load_module()


def receipt(message_id: str) -> dict:
    return {
        "status": "verified-delivered",
        "channel_name": "StarIntel Shipyard",
        "channel_id": "channel-1",
        "message_ids": [message_id],
        "report_digest": f"digest-{message_id}",
    }


class MergeDeliveryStateTests(unittest.TestCase):
    def test_preserves_concurrent_latest_receipt_and_adds_run_receipt(self):
        latest = {"delivery_receipts": {"a": receipt("m-a")}, "backlog_blockers": {}}
        run = {"delivery_receipts": {"b": receipt("m-b")}}

        result = merge.merge_delivery_receipts(latest, run)

        self.assertEqual(receipt("m-a"), result["delivery_receipts"]["a"])
        self.assertEqual(receipt("m-b"), result["delivery_receipts"]["b"])
        self.assertEqual({}, result["backlog_blockers"])

    def test_ignores_unverified_run_state(self):
        latest = {"delivery_receipts": {}}
        run = {"delivery_receipts": {"a": {"status": "attempted"}}}

        result = merge.merge_delivery_receipts(latest, run)

        self.assertEqual({}, result["delivery_receipts"])

    def test_rejects_conflicting_verified_receipts(self):
        latest = {"delivery_receipts": {"a": receipt("m-a")}}
        run = {"delivery_receipts": {"a": receipt("m-other")}}

        with self.assertRaisesRegex(ValueError, "conflicting verified receipt"):
            merge.merge_delivery_receipts(latest, run)


if __name__ == "__main__":
    unittest.main()
