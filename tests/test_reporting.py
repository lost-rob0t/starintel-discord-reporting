import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


post = load("post", "scripts/post_report.py")
verify = load("verify", "scripts/verify_report.py")


class ReportingTests(unittest.TestCase):
    def test_split_never_exceeds_discord_limit(self):
        text = ("para words here\n\n" * 300) + "```python\n" + ("print('x')\n" * 300) + "```\n"
        chunks = post.split_markdown(text)
        self.assertTrue(len(chunks) > 1)
        self.assertTrue(all(len(chunk) <= 2000 for chunk in chunks))
        self.assertTrue(all(chunk.count("```") % 2 == 0 for chunk in chunks))

    def test_dedupe_digest(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            self.assertFalse(post.already_posted(path, "x", "hello"))
            post.mark_posted(path, "x", "hello")
            self.assertTrue(post.already_posted(path, "x", "hello"))
            self.assertFalse(post.already_posted(path, "y", "hello"))

    def test_findings_gate(self):
        text = """# x
## Sources
- https://example.com/a
- https://example.org/b

This report was written by AI. Check it yourself.
Do not trust this report as a source. Don't even trust NSA Spy.
SIGNED OFF BY: N545PY
"""
        self.assertEqual([], verify.verify(text, "findings", False))

    def test_changelog_requires_commit(self):
        self.assertTrue(verify.verify("# x\n## Changes\n- feature\n", "changelog", False))


if __name__ == "__main__":
    unittest.main()
