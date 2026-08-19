# Repository tracking

`config/starintel-repo-tracking.tsv` is the tracked StarIntel repository set and canonical branch map.

Run:

```bash
bash scripts/update_repo_snapshots.sh
```

The script keeps lightweight repo caches outside this repository and writes readable snapshots under `tracking/repos/`. Each snapshot contains the canonical head, the last 14 days of commit subjects, repository paths changed, and test/CI paths touched.

The snapshots are evidence caches. They do not prove a test passed, and they do not provide a line-coverage percentage. Changelog writing must verify any stronger claim against the landed commit, CI result, or explicit test output.
