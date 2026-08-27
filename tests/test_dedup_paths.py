from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import check_report_dedup as dedup


class DedupPathTests(unittest.TestCase):
    def test_repo_relative_report_path_resolves_under_root(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            relative = Path("reports/starintel-updates-changelog/new-report.md")
            expected = root / relative
            self.assertEqual(expected, dedup.normalize_report_path(relative, root))

    def test_absolute_report_path_is_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            absolute = root / "reports/starintel-updates-changelog/new-report.md"
            self.assertEqual(absolute, dedup.normalize_report_path(absolute, root))


if __name__ == "__main__":
    unittest.main()
