import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


post = load("post", "scripts/post_report.py")
verify = load("verify", "scripts/verify_report.py")


class FakeResponse:
    def __init__(self, status, body):
        self.status = status
        self._body = body

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self):
        return self._body


class ReportingTests(unittest.TestCase):
    def test_split_never_exceeds_discord_limit(self):
        text = ("para words here\n\n" * 300) + "```python\n" + ("print('x')\n" * 300) + "```\n"
        chunks = post.split_markdown(text)
        self.assertTrue(len(chunks) > 1)
        self.assertTrue(all(len(chunk) <= 2000 for chunk in chunks))
        self.assertTrue(all(chunk.count("```") % 2 == 0 for chunk in chunks))

    def test_bare_2xx_without_message_json_is_not_verified_delivery(self):
        with mock.patch.object(post.urllib.request, "urlopen", return_value=FakeResponse(204, b"")):
            with self.assertRaises(RuntimeError):
                post.post_chunk("https://example.invalid/hook", "x", "hello", retries=0)

    def test_valid_response_persists_message_and_channel_ids(self):
        with tempfile.TemporaryDirectory() as directory:
            state_path = Path(directory) / "state.json"
            response = json.dumps({"id": "msg-123", "channel_id": "chan-9"}).encode()
            with mock.patch.object(post.urllib.request, "urlopen", return_value=FakeResponse(200, response)):
                receipt = post.post_chunk("https://example.invalid/hook", "x", "hello", retries=0)
            post.mark_verified_delivery(
                state_path,
                "reports/findings-shitposts/a-report.md",
                "x",
                "hello",
                [receipt],
            )
            saved = post.load_state(state_path)["delivery_receipts"]["reports/findings-shitposts/a-report.md"]
            self.assertEqual("verified-delivered", saved["status"])
            self.assertEqual(["msg-123"], saved["message_ids"])
            self.assertEqual("chan-9", saved["channel_id"])
            self.assertTrue(saved["delivered_at"])

    def test_legacy_published_report_does_not_suppress_recovery_without_receipt(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            report_id = "reports/starintel-updates-changelog/a-report.md"
            path.write_text(json.dumps({"published_reports": [report_id], "posted": ["legacy"]}), encoding="utf-8")
            self.assertFalse(post.already_reported(path, report_id))
            self.assertFalse(post.already_posted(path, "x", "hello"))

    def test_verified_receipt_suppresses_exact_recovery(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            report_id = "reports/starintel-updates-changelog/a-report.md"
            post.mark_verified_delivery(path, report_id, "x", "hello", [{"id": "m1", "channel_id": "c1"}])
            self.assertTrue(post.already_reported(path, report_id, "x", "hello"))
            self.assertTrue(post.already_posted(path, "x", "hello"))
            self.assertFalse(post.already_posted(path, "x", "different"))

    def test_verified_receipt_does_not_suppress_rewritten_report(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            report_id = "reports/starintel-updates-changelog/a-report.md"
            post.mark_verified_delivery(path, report_id, "StarIntel Shipyard", "old prose", [{"id": "m1", "channel_id": "c1"}])
            self.assertFalse(
                post.already_reported(path, report_id, "StarIntel Shipyard", "corrected prose")
            )

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

    def test_operational_changelog_accepts_sourced_actions_incident(self):
        text = """# StarIntel ops: the Mara 2.5k job incident

## Changes
- queue recovered after the fan-out incident

## Operational Sources
- https://github.com/lost-rob0t/zara/actions/runs/32534697924
- https://github.com/lost-rob0t/zara/pull/126
"""
        self.assertEqual([], verify.verify(text, "changelog", False))

    def test_operational_changelog_requires_actions_run_source(self):
        text = """# StarIntel ops: incident

## Changes
- queue recovered

## Operational Sources
- https://github.com/lost-rob0t/zara/pull/126
"""
        errors = verify.verify(text, "changelog", False)
        self.assertTrue(any("Actions run" in error for error in errors))

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
