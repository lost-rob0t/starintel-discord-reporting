import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verify = load("verify_private", "scripts/verify_report.py")


class PrivateChangelogTests(unittest.TestCase):
    def test_private_source_changelog_can_omit_private_links(self):
        text = """# StarIntel updates

## Changes
- edge deployment is now declaratively managed and repeatable
- deployment validation is more robust across repeated runs

## Private Source Attestation
Verified against a configured private canonical branch. Private repository and commit links are intentionally omitted under STYLE.md.
"""
        self.assertEqual([], verify.verify(text, "changelog", False))

    def test_private_source_changelog_rejects_github_links(self):
        text = """# StarIntel updates

## Changes
- edge deployment is now declaratively managed

## Private Source Attestation
Verified against a configured private canonical branch. Private links are intentionally omitted.
https://github.com/private-org/private-repo/commit/0123456789abcdef0123456789abcdef01234567
"""
        errors = verify.verify(text, "changelog", False)
        self.assertTrue(any("private-source changelog must not expose GitHub links" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
