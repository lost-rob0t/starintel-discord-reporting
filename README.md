# starintel-discord-reporting

Discord publishing for StarIntel. GPT writes reports. GitHub Actions validates and sends them.

```text
reports/
  auto-dig-findings/<datestring>-report.md
  findings-shitposts/<datestring>-report.md
  starintel-updates-changelog/<datestring>-report.md
```

The hourly research/reporting loop runs from GPT, not from GitHub Actions. `GPT-WORKFLOW.md` is the contract for that run. Most hourly runs should do nothing because no new material is worth posting.

GitHub Actions only reacts after GPT commits a new report to `main`.

## Channels

### `auto-dig-findings`

Serious, short Auto-Dig findings. GPT verifies the underlying Auto-Dig material against its sources before writing a report. Weak or contradictory material gets skipped.

Reports include visible source URLs, the landed Auto-Dig commit, and this footer:

```text
This was written by AI. check it yourself.
Please double check findings as this was llm derived.
dont trust this report as a source. dont even trust nsaspy.
SIGNED OFF BY: N545PY
```

`nsaspy` is one word and is never the signer.

### `findings-shitposts`

Only uses Auto-Dig findings that already passed verification in the same GPT run.

A post may be skipped entirely. When GPT does publish one, it chooses among:

- no-image rough text;
- `/pol/`-POV 4chan greentext with no image;
- Star Trek meme image, where Data is always Auto-Dig;
- Star Trek comic image, where Data is always Auto-Dig.

For image modes, the image is stored beside the Markdown report using the same basename. The publisher attaches it automatically.

The joke can be feral. The factual claim cannot be fabricated.

### `starintel-updates-changelog`

Only reports meaningful work that actually landed on a configured StarIntel repository's canonical `main` or `master` branch.

Each item names the feature/capability and links directly to the landed merge/squash commit. Open PRs, branch-only work, CI-only churn, and trivial formatting/docs noise do not get posted.

The monitored repository set lives in:

```text
config/starintel-repos.txt
```

## Webhook secrets

```text
AUTO_DIG_FINDINGS
FINDINGS_SHITPOSTS
STARINTEL_UPDATES_CHANGELOG
```

The webhook username is the channel name. No avatar override is used.

## Publisher workflow

`.github/workflows/publish-reports.yml` runs when a new report file lands on `main`.

It:

- maps report directories to the repository webhook secrets;
- validates reports before publication;
- attaches a sibling PNG/JPG/JPEG/GIF/WebP when present;
- splits Discord `content` at the hard 2,000-character limit;
- preserves fenced Markdown across split messages;
- disables mention parsing;
- hashes published content in `state/published.json` and skips exact duplicates.

The publisher does not research, summarize, or decide what deserves a post. That is the GPT workflow's job.

## Style

Read `STYLE.md` before generating anything. No em dashes, no corporate LLM sludge, varied sentence rhythm, visible sources, and no anti-detector rewrite nonsense.

## Test

```bash
python -m unittest discover -s tests -v
python -m py_compile scripts/*.py
```

`test-webhooks.yml` sends a clearly marked **TEST RUN** message only when a file under `reports/test/` is pushed to `main`.
