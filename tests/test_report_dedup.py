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


class ReportDedupTests(unittest.TestCase):
    def _state_with_verified(self, root: Path, reports: list[tuple[str, str, str]]) -> Path:
        state_path = root / "state" / "published.json"
        state_path.parent.mkdir(parents=True, exist_ok=True)
        receipts = {}
        for report_id, display_name, body in reports:
            receipts[report_id] = {
                "status": "verified-delivered",
                "message_ids": [f"msg-{len(receipts) + 1}"],
                "channel_id": "chan-1",
                "channel_name": display_name,
                "report_digest": post_report.report_digest(display_name, body),
            }
        state_path.write_text(json.dumps({"delivery_receipts": receipts}), encoding="utf-8")
        return state_path

    def _report(self, root: Path, channel: str, name: str, body: str) -> Path:
        path = root / "reports" / channel / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
        return path

    def test_same_autodig_commit_in_same_channel_is_blocked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            commit = "0123456789abcdef0123456789abcdef01234567"
            body = f"https://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/{commit}\n"
            old = self._report(root, "auto-dig-findings", "old-report.md", body)
            new = self._report(root, "auto-dig-findings", "new-report.md", "rewritten\n" + body)
            state = self._state_with_verified(root, [(old.relative_to(root).as_posix(), "The Receipt Desk", body)])
            reason = dedup.duplicate_reason(new, "auto-dig-findings", state, root)
            self.assertIsNotNone(reason)
            self.assertIn("already-delivered provenance", reason)

    def test_serious_and_shitpost_are_separate_products(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            commit = "0123456789abcdef0123456789abcdef01234567"
            body = f"https://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/{commit}\n"
            old = self._report(root, "auto-dig-findings", "old-report.md", body)
            new = self._report(root, "findings-shitposts", "new-report.md", ">joke\n" + body)
            state = self._state_with_verified(root, [(old.relative_to(root).as_posix(), "The Receipt Desk", body)])
            self.assertIsNone(dedup.duplicate_reason(new, "findings-shitposts", state, root))

    def test_changelog_reusing_any_landed_commit_is_blocked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            old_commit = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            new_commit = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
            old_body = f"Landed: <https://github.com/lost-rob0t/prolog-rlm/commit/{old_commit}>\n"
            new_body = (
                f"New: <https://github.com/lost-rob0t/prolog-rlm/commit/{new_commit}>\n"
                f"Context: <https://github.com/lost-rob0t/prolog-rlm/commit/{old_commit}>\n"
            )
            old = self._report(root, "starintel-updates-changelog", "old-report.md", old_body)
            new = self._report(root, "starintel-updates-changelog", "new-report.md", new_body)
            state = self._state_with_verified(root, [(old.relative_to(root).as_posix(), "StarIntel Shipyard", old_body)])
            reason = dedup.duplicate_reason(new, "starintel-updates-changelog", state, root)
            self.assertIsNotNone(reason)
            self.assertIn(old_commit, reason)

    def test_regression_typed_plan_benchmark_overslice_is_blocked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            contract = "e6e4c2a7d53de4830181bfe7e015e336176d1301"
            handoff = "474facb0ddc6fae677b326ee49979220ea443cba"
            benchmark = "4074c4635c1dbb5c30a0e3fc26d55511ecefe85f"
            old_body = (
                f"Landed: <https://github.com/lost-rob0t/prolog-rlm/commit/{contract}>\n"
                f"Final handoff: <https://github.com/lost-rob0t/prolog-rlm/commit/{handoff}>\n"
            )
            new_body = (
                f"Recovered benchmark: <https://github.com/lost-rob0t/prolog-rlm/commit/{benchmark}>\n"
                f"Core contract ownership: <https://github.com/lost-rob0t/prolog-rlm/commit/{contract}>\n"
                f"Final handoff fix: <https://github.com/lost-rob0t/prolog-rlm/commit/{handoff}>\n"
            )
            old = self._report(root, "starintel-updates-changelog", "old-report.md", old_body)
            new = self._report(root, "starintel-updates-changelog", "new-report.md", new_body)
            state = self._state_with_verified(root, [(old.relative_to(root).as_posix(), "StarIntel Shipyard", old_body)])
            reason = dedup.duplicate_reason(new, "starintel-updates-changelog", state, root)
            self.assertIsNotNone(reason)
            self.assertIn(contract, reason)
            self.assertIn(handoff, reason)

    def test_followup_requires_new_provenance_when_reusing_old(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            commit = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            old_body = f"Landed: <https://github.com/lost-rob0t/prolog-rlm/commit/{commit}>\n"
            new_body = f"## FOLLOW-UP\nLanded: <https://github.com/lost-rob0t/prolog-rlm/commit/{commit}>\n"
            old = self._report(root, "starintel-updates-changelog", "old-report.md", old_body)
            new = self._report(root, "starintel-updates-changelog", "new-report.md", new_body)
            state = self._state_with_verified(root, [(old.relative_to(root).as_posix(), "StarIntel Shipyard", old_body)])
            reason = dedup.duplicate_reason(new, "starintel-updates-changelog", state, root)
            self.assertIsNotNone(reason)
            self.assertIn("FOLLOW-UP reuses only already-delivered provenance", reason)

    def test_followup_with_new_provenance_is_allowed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            old_commit = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            new_commit = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
            old_body = f"Landed: <https://github.com/lost-rob0t/prolog-rlm/commit/{old_commit}>\n"
            new_body = (
                "## FOLLOW-UP\n"
                f"Prior: <https://github.com/lost-rob0t/prolog-rlm/commit/{old_commit}>\n"
                f"New: <https://github.com/lost-rob0t/prolog-rlm/commit/{new_commit}>\n"
            )
            old = self._report(root, "starintel-updates-changelog", "old-report.md", old_body)
            new = self._report(root, "starintel-updates-changelog", "new-report.md", new_body)
            state = self._state_with_verified(root, [(old.relative_to(root).as_posix(), "StarIntel Shipyard", old_body)])
            self.assertIsNone(dedup.duplicate_reason(new, "starintel-updates-changelog", state, root))

    def test_correction_can_reuse_provenance(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            commit = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            old_body = f"Landed: <https://github.com/lost-rob0t/prolog-rlm/commit/{commit}>\n"
            new_body = f"## CORRECTION\nLanded: <https://github.com/lost-rob0t/prolog-rlm/commit/{commit}>\n"
            old = self._report(root, "starintel-updates-changelog", "old-report.md", old_body)
            new = self._report(root, "starintel-updates-changelog", "new-report.md", new_body)
            state = self._state_with_verified(root, [(old.relative_to(root).as_posix(), "StarIntel Shipyard", old_body)])
            self.assertIsNone(dedup.duplicate_reason(new, "starintel-updates-changelog", state, root))

    def test_exact_body_replay_under_new_filename_is_blocked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            body = "same body with no commit provenance\n"
            old = self._report(root, "starintel-updates-changelog", "old-report.md", body)
            new = self._report(root, "starintel-updates-changelog", "new-report.md", body)
            state = self._state_with_verified(root, [(old.relative_to(root).as_posix(), "StarIntel Shipyard", body)])
            reason = dedup.duplicate_reason(new, "starintel-updates-changelog", state, root)
            self.assertEqual(f"exact report body already delivered as {old.relative_to(root).as_posix()}", reason)


if __name__ == "__main__":
    unittest.main()
