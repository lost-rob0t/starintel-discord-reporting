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

    def test_dedupe_report_id(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            report_id = "reports/starintel-updates-changelog/a-report.md"
            self.assertFalse(post.already_reported(path, report_id))
            post.mark_posted(path, "x", "hello", report_id=report_id)
            self.assertTrue(post.already_reported(path, report_id))
            self.assertTrue(post.already_posted(path, "x", "hello"))

    def test_mark_posted_preserves_other_state(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            path.write_text('{"manual_cursor":"abc","posted":[]}\n', encoding="utf-8")
            post.mark_posted(path, "x", "hello", report_id="r")
            state = post.load_state(path)
            self.assertEqual("abc", state["manual_cursor"])
            self.assertEqual(["r"], state["published_reports"])

    def test_message_payload_suppresses_embeds(self):
        payload = post._message_payload("findings-shitposts", "https://example.com")
        self.assertEqual(4, payload["flags"])
        self.assertEqual({"parse": []}, payload["allowed_mentions"])

    def test_findings_gate(self):
        text = """# Auto-Dig findings

## Findings
- checked claim
- merged: https://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/0123456789abcdef0123456789abcdef01234567

## Sources
- https://example.com/a
- https://example.org/b

This was written by AI. check it yourself.
Please double check findings as this was llm derived.
dont trust this report as a source. dont even trust nsaspy.
SIGNED OFF BY: N545PY
"""
        self.assertEqual([], verify.verify(text, "findings", False))

    def test_findings_accept_legacy_sources_heading(self):
        text = """# Auto-Dig findings

- merged: https://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/0123456789abcdef0123456789abcdef01234567

Sources:
- https://example.com/a
- https://example.org/b

This was written by AI. check it yourself.
Please double check findings as this was llm derived.
dont trust this report as a source. dont even trust nsaspy.
SIGNED OFF BY: N545PY
"""
        self.assertEqual([], verify.verify(text, "findings", False))

    def test_shitpost_accept_legacy_sources_heading(self):
        text = """>anon discovers validator drift
>amazing

Sources:
- https://example.com/a
"""
        self.assertEqual([], verify.verify(text, "shitpost", False))

    def test_findings_reject_spaced_nsaspy(self):
        text = """# Auto-Dig findings
## Sources
- https://example.com/a
- https://example.org/b
Dont trust NSA Spy.
"""
        errors = verify.verify(text, "findings", False)
        self.assertTrue(any("one word" in error for error in errors))

    def test_shitpost_rejects_signoff(self):
        text = """# x
## Sources
- https://example.com/a
SIGNED OFF BY: N545PY
"""
        errors = verify.verify(text, "shitpost", False)
        self.assertTrue(any("signoff" in error for error in errors))

    def test_changelog_requires_commit(self):
        self.assertTrue(verify.verify("# x\n## Changes\n- feature\n", "changelog", False))
        valid = """# StarIntel updates
## Changes
- new capability
- https://github.com/lost-rob0t/quasar/commit/0123456789abcdef0123456789abcdef01234567
"""
        self.assertEqual([], verify.verify(valid, "changelog", False))

    def test_multipart_contains_attachment_and_payload(self):
        with tempfile.TemporaryDirectory() as directory:
            attachment = Path(directory) / "meme.png"
            attachment.write_bytes(b"png-bytes")
            body, content_type = post._multipart(
                {
                    "content": "hi",
                    "username": "findings-shitposts",
                    "allowed_mentions": {"parse": []},
                    "flags": post.SUPPRESS_EMBEDS_FLAG,
                },
                attachment,
            )
            self.assertIn("multipart/form-data", content_type)
            self.assertIn(b"meme.png", body)
            self.assertIn(b"png-bytes", body)
            self.assertIn(b"findings-shitposts", body)
            self.assertIn(b'"flags": 4', body)


if __name__ == "__main__":
    unittest.main()
