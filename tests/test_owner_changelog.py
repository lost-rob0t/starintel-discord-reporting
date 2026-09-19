import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import check_report_dedup as dedup
import post_report
import verify_report


class OwnerChangelogTests(unittest.TestCase):
    def test_owner_changelog_accepts_public_landed_commit(self):
        text = """# Lost Rob0t changelog

Window: 2026-09-18 00:00 UTC to 2026-09-19 04:25 UTC

## Changes

### zara
- Local runtime work landed.
  <https://github.com/lost-rob0t/zara/commit/623a535879d2ce1db829b0962c67b8c816232d15>
"""
        self.assertEqual([], verify_report.verify(text, "owner-changelog", False))

    def test_owner_changelog_requires_heading_and_landed_commit(self):
        errors = verify_report.verify("## Changes\n- stuff\n", "owner-changelog", False)
        self.assertTrue(any("Lost Rob0t changelog heading" in error for error in errors))
        self.assertTrue(any("direct landed lost-rob0t commit link" in error for error in errors))

    def test_owner_changelog_rejects_private_attestation_mode(self):
        text = """# Lost Rob0t changelog

## Changes
- Public work landed.
  <https://github.com/lost-rob0t/zara/commit/623a535879d2ce1db829b0962c67b8c816232d15>

## Private Source Attestation
Configured private details.
"""
        errors = verify_report.verify(text, "owner-changelog", False)
        self.assertTrue(any("must not use private-source attestation" in error for error in errors))

    def test_owner_roundup_dedupe_is_independent_from_shipyard(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            state = root / "state" / "published.json"
            state.parent.mkdir(parents=True)
            shipyard_body = (
                "## Changes\n"
                "<https://github.com/lost-rob0t/zara/commit/"
                "623a535879d2ce1db829b0962c67b8c816232d15>\n"
            )
            shipyard = root / "reports" / "starintel-updates-changelog" / "old-report.md"
            shipyard.parent.mkdir(parents=True)
            shipyard.write_text(shipyard_body, encoding="utf-8")
            state.write_text(
                json.dumps(
                    {
                        "delivery_receipts": {
                            shipyard.relative_to(root).as_posix(): {
                                "status": "verified-delivered",
                                "message_ids": ["msg-1"],
                                "channel_id": "chan-1",
                                "channel_name": "StarIntel Shipyard",
                                "report_digest": post_report.report_digest(
                                    "StarIntel Shipyard", shipyard_body
                                ),
                            }
                        }
                    }
                ),
                encoding="utf-8",
            )
            owner = root / "reports" / "lost-robot-changelog" / "new-report.md"
            owner.parent.mkdir(parents=True)
            owner.write_text(
                "# Lost Rob0t changelog\n\n## Changes\n"
                "<https://github.com/lost-rob0t/zara/commit/"
                "623a535879d2ce1db829b0962c67b8c816232d15>\n",
                encoding="utf-8",
            )
            self.assertIsNone(
                dedup.duplicate_reason(owner, "lost-robot-changelog", state, root)
            )


if __name__ == "__main__":
    unittest.main()
