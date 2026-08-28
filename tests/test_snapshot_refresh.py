import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).parents[1]


class SnapshotRefreshTests(unittest.TestCase):
    def _run(self, rows: str, bad_repo: str):
        directory = tempfile.TemporaryDirectory()
        root = Path(directory.name)
        script = root / "scripts" / "update_repo_snapshots.sh"
        script.parent.mkdir(parents=True)
        shutil.copy2(ROOT / "scripts" / "update_repo_snapshots.sh", script)

        config = root / "config" / "starintel-repo-tracking.tsv"
        config.parent.mkdir(parents=True)
        config.write_text("repo\tbranch\tchangelog\n" + rows, encoding="utf-8")

        fake_bin = root / "bin"
        fake_bin.mkdir()
        gh = fake_bin / "gh"
        gh.write_text(
            "#!/usr/bin/env bash\n"
            "set -euo pipefail\n"
            "repo=$3\n"
            "dir=$4\n"
            f"if [[ $repo == {bad_repo} ]]; then exit 1; fi\n"
            "mkdir -p \"$dir/.git\"\n",
            encoding="utf-8",
        )
        gh.chmod(0o755)

        git = fake_bin / "git"
        git.write_text(
            "#!/usr/bin/env bash\n"
            "set -euo pipefail\n"
            "args=(\"$@\")\n"
            "case \" ${args[*]} \" in\n"
            "  *' rev-parse '*) echo 0123456789abcdef0123456789abcdef01234567 ;;\n"
            "  *' show -s --format=%cI '*) echo 2026-08-28T00:00:00Z ;;\n"
            "  *' show -s --format=%s '*) echo snapshot-test ;;\n"
            "  *' log '*) : ;;\n"
            "  *) : ;;\n"
            "esac\n",
            encoding="utf-8",
        )
        git.chmod(0o755)

        env = os.environ.copy()
        env["PATH"] = f"{fake_bin}:{env['PATH']}"
        env["XDG_CACHE_HOME"] = str(root / "cache")
        result = subprocess.run(
            ["bash", str(script)],
            cwd=root,
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return directory, root, result

    def test_required_failure_does_not_block_later_snapshots(self):
        directory, root, result = self._run(
            "example/first\tmain\tyes\n"
            "example/bad\tmain\tyes\n"
            "example/last\tmain\tyes\n",
            "example/bad",
        )
        with directory:
            self.assertEqual(1, result.returncode)
            self.assertTrue((root / "tracking" / "repos" / "first.md").is_file())
            self.assertFalse((root / "tracking" / "repos" / "bad.md").exists())
            self.assertTrue((root / "tracking" / "repos" / "last.md").is_file())
            self.assertIn("required snapshot refresh failed for example/bad", result.stderr)
            self.assertIn("required changelog snapshots partially refreshed", result.stderr)

    def test_optional_failure_is_visible_but_non_blocking(self):
        directory, root, result = self._run(
            "example/first\tmain\tyes\n"
            "example/optional\tmain\tno\n"
            "example/last\tmain\tyes\n",
            "example/optional",
        )
        with directory:
            self.assertEqual(0, result.returncode)
            self.assertTrue((root / "tracking" / "repos" / "first.md").is_file())
            self.assertFalse((root / "tracking" / "repos" / "optional.md").exists())
            self.assertTrue((root / "tracking" / "repos" / "last.md").is_file())
            self.assertIn("optional snapshot refresh failed for example/optional", result.stderr)
            self.assertIn("optional repo snapshots unavailable: example/optional", result.stderr)
            self.assertIn("repo snapshots refreshed", result.stdout)

    def test_workflow_persists_successful_snapshots_after_partial_failure(self):
        workflow = (ROOT / ".github" / "workflows" / "update-repo-snapshots.yml").read_text(encoding="utf-8")
        self.assertIn("if: always() && steps.token.outputs.ready == 'true'", workflow)


if __name__ == "__main__":
    unittest.main()
