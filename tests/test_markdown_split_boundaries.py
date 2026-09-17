import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).parents[1]
SPEC = importlib.util.spec_from_file_location("post_report_boundaries", ROOT / "scripts/post_report.py")
post = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(post)


class MarkdownSplitBoundaryTests(unittest.TestCase):
    def test_plain_delimiters_at_limit_preserve_content_and_budget(self):
        for limit in (2, 8, 19, 2000):
            for prefix_length in (limit - 1, limit, limit + 1):
                for delimiter in (" ", "\n", "\n\n"):
                    with self.subTest(limit=limit, prefix=prefix_length, delimiter=delimiter):
                        text = "x" * prefix_length + delimiter + "tail" * (limit + 1)
                        chunks = post.split_markdown(text, limit)
                        self.assertEqual(text, "".join(chunks))
                        self.assertTrue(all(0 < len(chunk) <= limit for chunk in chunks))

    def test_long_code_lines_leave_room_for_closing_fence_newline(self):
        for limit in (32, 79, 2000):
            for body in ("x" * (limit * 3), "print('x')\n" * (limit * 3)):
                with self.subTest(limit=limit, body_length=len(body)):
                    chunks = post.split_markdown("```python\n" + body + "\n```\n", limit)
                    self.assertTrue(all(len(chunk) <= limit for chunk in chunks))
                    self.assertTrue(all(chunk.count("```") % 2 == 0 for chunk in chunks))

    def test_public_split_rejects_nonpositive_limit(self):
        for limit in (0, -1):
            with self.subTest(limit=limit), self.assertRaises(ValueError):
                post.split_markdown("hello", limit)

    def test_actual_long_form_changelogs_fit_discord(self):
        for name in ("2026-09-17T05-57-14Z-report.md", "2026-09-17T05-57-15Z-report.md"):
            with self.subTest(report=name):
                text = (ROOT / "reports/starintel-updates-changelog" / name).read_text(encoding="utf-8")
                chunks = post.split_markdown(text)
                self.assertGreater(len(chunks), 1)
                self.assertEqual(text, "".join(chunks))
                self.assertTrue(all(len(chunk) <= post.MAX_DISCORD_CONTENT_CHARS for chunk in chunks))


if __name__ == "__main__":
    unittest.main()
