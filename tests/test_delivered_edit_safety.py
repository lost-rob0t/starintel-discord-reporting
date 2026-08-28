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


post = load("post_report_for_edit_safety", "scripts/post_report.py")
publish = load("publish_new_for_edit_safety", "scripts/publish_new.py")


class DeliveredEditSafetyTests(unittest.TestCase):
    def test_catchup_treats_verified_report_id_as_complete_after_prose_edit(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            report = root / "reports" / "auto-dig-findings" / "old-report.md"
            report.parent.mkdir(parents=True)
            report.write_text("old prose\n", encoding="utf-8")
            state = root / "state" / "published.json"
            state.parent.mkdir(parents=True)
            post.mark_verified_delivery(
                state,
                "reports/auto-dig-findings/old-report.md",
                "The Receipt Desk",
                "old prose\n",
                [{"id": "m1", "channel_id": "c1"}],
            )
            report.write_text("old prose\n\n## Sources\n", encoding="utf-8")

            original_root, original_state = publish.ROOT, publish.STATE
            publish.ROOT, publish.STATE = root, state
            try:
                self.assertTrue(publish.report_verified("reports/auto-dig-findings/old-report.md"))
            finally:
                publish.ROOT, publish.STATE = original_root, original_state

    def test_push_workflow_only_selects_added_reports(self):
        workflow = (ROOT / ".github" / "workflows" / "publish-reports.yml").read_text(encoding="utf-8")
        self.assertIn("git diff --name-only --diff-filter=A ", workflow)
        self.assertNotIn("--diff-filter=AM", workflow)


if __name__ == "__main__":
    unittest.main()
