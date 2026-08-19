# starintel-discord-reporting

Discord publishing for StarIntel. Reports are files first, webhook messages second.

```text
reports/
  auto-dig-findings/<datestring>-report.md
  findings-shitposts/<datestring>-report.md
  starintel-updates-changelog/<datestring>-report.md
```

The hourly workflow checks for new material every hour. No new relevant material means no report and no Discord post.

## Channels

### `auto-dig-findings`

Serious, short Auto-Dig findings. It only emits when new `digs/**/README.md` material lands on `starintel-gpt-auto-dig/main`, contains extractable findings, and has at least two source URLs. The report keeps source links and the merge commit.

Every findings report includes:

```text
This report was written by AI. Check it yourself.
Do not trust this report as a source. Don't even trust NSA Spy.
SIGNED OFF BY: N545PY
```

The validator checks required source links before publication and probes them over the network. Reports with broken verification fail closed.

### `findings-shitposts`

Uses the same newly-landed Auto-Dig material, but renders it in a deliberately rougher format. Each report randomly picks either greentext or loose anon-style prose. It does not invent extra claims. Source links stay attached.

### `starintel-updates-changelog`

Only reports pull requests that have actually landed on a configured repository's `main` or `master` branch. Each item includes the feature/capability title and a direct link to the landed commit.

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

## Discord size and splitting

Discord webhook `content` supports up to 2,000 characters. `scripts/post_report.py` treats 2,000 as a hard limit and splits longer reports into multiple Discord messages. It prefers paragraph/newline boundaries and preserves fenced code blocks across chunks.

## Duplicate protection

The publisher hashes `channel-name + report-content` and stores successful hashes in:

```text
state/published.json
```

Identical content will not be posted twice. Source cursors are only advanced after the publication phase succeeds.

## Test

```bash
python -m unittest discover -s tests -v
python -m py_compile scripts/*.py
```

`test-webhooks.yml` sends a clearly marked **TEST RUN** message only when a file under `reports/test/` is pushed to `main`.
