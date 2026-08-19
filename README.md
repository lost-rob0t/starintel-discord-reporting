# starintel-discord-reporting

Small reporting/publishing layer for StarIntel Discord channels.

The repo keeps generated reports in:

```text
reports/<channel-name>/<datestring>-report.md
```

Discord posts use the **channel name as the webhook username**. No per-channel avatar machinery is required.

## Current channel

`auto-dig` is the first reporting channel. Its scheduled publisher runs every three hours and looks for the report for the current UTC slot.

Example:

```text
reports/auto-dig/2026-08-19T18-report.md
```

Before anything is posted, the report validator checks the Markdown structure, balanced source-code fences, source URLs, sign-off, and the LLM-derived warning. Source URLs are probed when network verification is enabled.

Discord webhook `content` is limited to 2,000 characters. `scripts/post_report.py` treats that as a hard protocol limit and splits longer reports into multiple messages. It prefers natural Markdown boundaries and keeps fenced source-code blocks valid across split messages instead of detonating formatting halfway through a function.

## Secrets

Add the Auto-Dig webhook to repository Actions secrets as:

```text
DISCORD_WEBHOOK_AUTO_DIG
```

Additional channels get their own secret and workflow entry when their channel name and webhook URL are added.

## Report footer

Every findings report ends with:

```text
SIGNED OFF BY: <NAME>
Please double check findings as this was llm derived
```

Replace `<NAME>` in the generated report with the actual signer before publication.

## Local checks

```bash
python -m unittest discover -s tests -v
python scripts/verify_report.py reports/auto-dig/example-report.md --no-network
python scripts/post_report.py \
  --channel-name auto-dig \
  --webhook-url "$DISCORD_WEBHOOK_AUTO_DIG" \
  --report reports/auto-dig/example-report.md \
  --dry-run
```

The publisher disables Discord mention parsing so report text cannot accidentally ping everyone, roles, or users.
