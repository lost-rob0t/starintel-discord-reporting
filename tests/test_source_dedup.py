import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


dedup = load("source_dedup", "scripts/check_source_dedup.py")


class SourceDedupTests(unittest.TestCase):
    def _state(self, root: Path, report_ids: list[str]) -> Path:
        state = root / "state" / "published.json"
        state.parent.mkdir(parents=True, exist_ok=True)
        state.write_text(
            json.dumps(
                {
                    "delivery_receipts": {
                        report_id: {
                            "status": "verified-delivered",
                            "message_ids": [f"m{index}"],
                            "channel_id": "c1",
                        }
                        for index, report_id in enumerate(report_ids, 1)
                    }
                }
            ),
            encoding="utf-8",
        )
        return state

    def test_rejects_same_autodig_commit_in_same_channel(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            channel = root / "reports" / "auto-dig-findings"
            channel.mkdir(parents=True)
            commit = "0123456789abcdef0123456789abcdef01234567"
            old = channel / "old-report.md"
            new = channel / "new-report.md"
            old.write_text(f"https://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/{commit}\n", encoding="utf-8")
            new.write_text(f"https://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/{commit}\n", encoding="utf-8")
            state = self._state(root, [old.relative_to(root).as_posix()])
            self.assertEqual(
                (old.relative_to(root).as_posix(), f"autodig@{commit}"),
                dedup.duplicate_source(new, "auto-dig-findings", state, root),
            )

    def test_allows_serious_and_shitpost_to_share_autodig_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            findings = root / "reports" / "auto-dig-findings"
            shitposts = root / "reports" / "findings-shitposts"
            findings.mkdir(parents=True)
            shitposts.mkdir(parents=True)
            commit = "0123456789abcdef0123456789abcdef01234567"
            old = findings / "old-report.md"
            new = shitposts / "new-report.md"
            old.write_text(f"https://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/{commit}\n", encoding="utf-8")
            new.write_text(f"https://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/{commit}\n", encoding="utf-8")
            state = self._state(root, [old.relative_to(root).as_posix()])
            self.assertIsNone(dedup.duplicate_source(new, "findings-shitposts", state, root))

    def test_rejects_changelog_reusing_any_landed_commit(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            channel = root / "reports" / "starintel-updates-changelog"
            channel.mkdir(parents=True)
            reused = "0123456789abcdef0123456789abcdef01234567"
            novel = "89abcdef0123456789abcdef0123456789abcdef"
            old = channel / "old-report.md"
            new = channel / "new-report.md"
            old.write_text(f"https://github.com/lost-rob0t/prolog-rlm/commit/{reused}\n", encoding="utf-8")
            new.write_text(
                f"https://github.com/lost-rob0t/prolog-rlm/commit/{reused}\n"
                f"https://github.com/lost-rob0t/prolog-rlm/commit/{novel}\n",
                encoding="utf-8",
            )
            state = self._state(root, [old.relative_to(root).as_posix()])
            duplicate = dedup.duplicate_source(new, "starintel-updates-changelog", state, root)
            self.assertEqual((old.relative_to(root).as_posix(), f"lost-rob0t/prolog-rlm@{reused}"), duplicate)

    def test_followup_requires_new_provenance(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            channel = root / "reports" / "starintel-updates-changelog"
            channel.mkdir(parents=True)
            reused = "0123456789abcdef0123456789abcdef01234567"
            novel = "89abcdef0123456789abcdef0123456789abcdef"
            old = channel / "old-report.md"
            bad = channel / "bad-report.md"
            good = channel / "good-report.md"
            old.write_text(f"https://github.com/lost-rob0t/prolog-rlm/commit/{reused}\n", encoding="utf-8")
            bad.write_text(
                f"# FOLLOW-UP\nhttps://github.com/lost-rob0t/prolog-rlm/commit/{reused}\n",
                encoding="utf-8",
            )
            good.write_text(
                f"# FOLLOW-UP\nhttps://github.com/lost-rob0t/prolog-rlm/commit/{reused}\n"
                f"https://github.com/lost-rob0t/prolog-rlm/commit/{novel}\n",
                encoding="utf-8",
            )
            state = self._state(root, [old.relative_to(root).as_posix()])
            self.assertIsNotNone(dedup.duplicate_source(bad, "starintel-updates-changelog", state, root))
            self.assertIsNone(dedup.duplicate_source(good, "starintel-updates-changelog", state, root))

    def test_correction_may_reuse_provenance(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            channel = root / "reports" / "starintel-updates-changelog"
            channel.mkdir(parents=True)
            commit = "0123456789abcdef0123456789abcdef01234567"
            old = channel / "old-report.md"
            correction = channel / "correction-report.md"
            old.write_text(f"https://github.com/lost-rob0t/prolog-rlm/commit/{commit}\n", encoding="utf-8")
            correction.write_text(
                f"# CORRECTION\nhttps://github.com/lost-rob0t/prolog-rlm/commit/{commit}\n",
                encoding="utf-8",
            )
            state = self._state(root, [old.relative_to(root).as_posix()])
            self.assertIsNone(dedup.duplicate_source(correction, "starintel-updates-changelog", state, root))


if __name__ == "__main__":
    unittest.main()
