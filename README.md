# starintel-discord-reporting

Discord publishing for StarIntel. GPT writes reports. GitHub Actions or the local publisher can send them.

```text
reports/
  auto-dig-findings/<datestring>-report.md
  findings-shitposts/<datestring>-report.md
  starintel-updates-changelog/<datestring>-report.md
```

The hourly research/reporting loop runs from GPT, not GitHub Actions. `GPT-WORKFLOW.md` is the contract. Most hourly runs should do nothing.

## Channels

### `auto-dig-findings`

Short verified Auto-Dig findings. Reports keep visible sources, the landed Auto-Dig commit, uncertainty when needed, and the required AI warning/signoff from `STYLE.md`.

### `findings-shitposts`

Only uses Auto-Dig findings already verified in the same run. It may be text, `/pol/` greentext, a Star Trek meme, or a short Star Trek comic. Data is always Auto-Dig in the image modes.

### `starintel-updates-changelog`

Short summaries of useful work that actually landed on a configured canonical branch. Group related commits. Do not dump commit history or make up test coverage.

`config/starintel-repos.txt` is the automatic changelog allow-list. `config/starintel-repo-tracking.tsv` is the wider StarIntel repository inventory.

## Webhook secrets

```text
AUTO_DIG_FINDINGS
FINDINGS_SHITPOSTS
STARINTEL_UPDATES_CHANGELOG
```

The webhook username is the channel name. No avatar override is used.

## Publishing

GitHub Actions publishes new report files when runners are available.

For Termux or any local checkout, the fallback is intentionally zero-argument:

```bash
python scripts/publish_new.py
```

It loads `.env`, finds only report files newer than its durable cursor, checks both immutable report paths and content hashes, publishes each report at most once, records state in `state/published.json`, commits that state, and pushes it to `main`.

The GitHub publisher refreshes `state/published.json` from current `main` before sending, so an old queued run can see reports already published locally and skip them.

## Repository snapshots

Refresh local StarIntel repo evidence with:

```bash
bash scripts/update_repo_snapshots.sh
```

The tracked repo/branch map is in `config/starintel-repo-tracking.tsv`. Generated snapshots go under `tracking/repos/` and contain the canonical head, last 14 days of git log, changed repository paths, and test/CI paths touched.

A scheduled workflow can refresh those snapshots when `STARINTEL_GH_TOKEN` is configured with access to the tracked private repos. The snapshots are evidence caches, not proof that a test passed.

## Style

Read `STYLE.md` before generating anything. No em dashes, no corporate LLM sludge, visible sources, and no invented coverage numbers.

## Tests

```bash
python -m unittest discover -s tests -v
python -m py_compile scripts/*.py
```

Webhook smoke-test automation was removed after it caused duplicate test posts. Tests now stay local/CI unless deliberately reintroduced.
