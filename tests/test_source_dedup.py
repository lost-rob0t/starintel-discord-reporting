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
    def _write_state(self, root: Path, report_id: str) -> Path:
        state = root / "state" / "published.json"
        state.parent.mkdir(parents=True, exist_ok=True)
        state.write_text(
            json.dumps(
                {
                    "delivery_receipts": {
                        report_id: {
                            "status": "verified-delivered",
                            "message_ids": ["m1"],
                            "channel_id": "c1",
                        }
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
            old.write_text(f"source https://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/{commit}\n", encoding="utf-8")
            new.write_text(f"rewritten https://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/{commit}\n", encoding="utf-8")
            old_id = old.relative_to(root).as_posix()
            state = self._write_state(root, old_id)
            duplicate = dedup.duplicate_source(new, "auto-dig-findings", state, root)
            self.assertEqual((old_id, commit), duplicate)

    def test_allows_serious_and_shitpost_products_to_share_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            findings = root / "reports" / "auto-dig-findings"
            shitposts = root / "reports" / "findings-shitposts"
            findings.mkdir(parents=True)
            shitposts.mkdir(parents=True)
            commit = "0123456789abcdef0123456789abcdef01234567"
            old = findings / "old-report.md"
            new = shitposts / "new-report.md"
            old.write_text(f"source https://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/{commit}\n", encoding="utf-8")
            new.write_text(f">joke\nhttps://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/{commit}\n", encoding="utf-8")
            state = self._write_state(root, old.relative_to(root).as_posix())
            self.assertIsNone(dedup.duplicate_source(new, "findings-shitposts", state, root))

    def test_explicit_followup_can_reuse_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            channel = root / "reports" / "auto-dig-findings"
            channel.mkdir(parents=True)
            commit = "0123456789abcdef0123456789abcdef01234567"
            old = channel / "old-report.md"
            new = channel / "new-report.md"
            old.write_text(f"source https://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/{commit}\n", encoding="utf-8")
            new.write_text(f"# FOLLOW-UP: new records\nhttps://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/{commit}\n", encoding="utf-8")
            state = self._write_state(root, old.relative_to(root).as_posix())
            self.assertIsNone(dedup.duplicate_source(new, "auto-dig-findings", state, root))


if __name__ == "__main__":
    unittest.main()
