# Hourly GPT reporting workflow

GPT owns report generation and editorial selection. GitHub Actions validate and publish report files committed here.

Most runs should publish nothing.

## 1. Refresh state and drain backlog first

Use the GitHub connector as the source of truth.

Inspect:

- `lost-rob0t/starintel-discord-reporting` current `main`;
- every report under all three channel directories;
- `state/published.json` verified delivery receipts;
- `STYLE.md`;
- `config/starintel-repos.txt` and repo tracking configuration;
- relevant current source repositories and landed commits.

Before new content, exhaustively enumerate the reporting backlog. A report is delivered only when its exact path has a `verified-delivered` receipt containing Discord message ID(s) and channel ID returned from a `wait=true` webhook response. Legacy `published_reports`, content digests, GitHub commits, or generic HTTP 2xx responses are not delivery proof.

Malformed legacy reports, stale delivery blockers, failed deliveries, and unfinished publisher repairs are backlog too. Fix valid formatting/style problems when the underlying facts are already verified. Do not invent allegations to rescue weak reports. Drain eligible backlog oldest first before normal editorial work.

## 2. Editorial target

For police, prosecutors, courts, city government, and public safety, prioritize:

- police corruption or misconduct;
- selective enforcement or obvious non-enforcement;
- ignored complaints, unserved warrants, repeated failure to act;
- lax or permissive policy with documented operational consequences;
- charging, release, bail, sentencing, parole, probation, or prosecution decisions that materially undermine enforcement;
- audit failures, contradictory records, hidden policy changes, stale or misleading public records;
- officials saying one thing while primary records show something materially different;
- repeated institutional failure.

Do not publish routine enforcement chronology, staffing announcements, generic crackdowns, or `police enforced something` as scandal. A timeline is only interesting when it reveals corruption, non-enforcement, selective enforcement, lax policy, accountability failure, or a material contradiction.

The lens is skeptical of bureaucratic excuses, permissive policy, and institutional self-protection. Do not default to activist framing that treats enforcement itself as the scandal. Do not manufacture corruption, motive, criminality, or intentional misconduct either. Use the narrowest characterization the evidence supports.

## 3. Auto-Dig serious findings

Source repository: `lost-rob0t/starintel-gpt-auto-dig` on `main`, READ-ONLY.

Only consider material actually landed on `main`.

For every candidate:

1. Read the underlying Auto-Dig packet and provenance, not a search snippet.
2. Open the important primary/reputable sources.
3. Verify the exact claim independently.
4. Look for contradiction, ambiguity, stale dates, entity collisions, and overstatement.
5. Prefer primary records plus independent corroboration.
6. Distinguish accusation, charge, allegation, audit finding, policy fact, and proven conduct.
7. If evidence is weak, narrow the claim or publish nothing.

When a finding passes, create:

```text
reports/auto-dig-findings/<UTC-datestring>-report.md
```

House style is short, tabloid, blunt, cynical, concrete, and evidence-disciplined. Do not write like public radio, a city press release, activist copy, corporate prose, or a municipal audit summary. Headlines should expose the corruption, non-enforcement, lax-policy failure, contradiction, or accountability gap that makes the item worth reading.

Use the literal `## Sources` heading. Preserve visible source URLs and the direct landed Auto-Dig commit link.

Footer exactly:

```text
This was written by AI. check it yourself.
Please double check findings as this was llm derived.
dont trust this report as a source. dont even trust nsaspy.
SIGNED OFF BY: N545PY
```

`nsaspy` is one word and is never the signer.

## 4. Auto-Dig shitposts

Only use findings that passed serious verification in the same run.

Current house mode is 4chan-style greentext unless the user explicitly changes it. No image/comic mode by default.

Create:

```text
reports/findings-shitposts/<UTC-datestring>-report.md
```

Use `>` lines, clipped syntax, rough cadence, dry sarcasm, flat setup, and deadpan escalation. The verified institutional failure stays the factual spine. Learn cadence from live boards without copying ideology, slurs, protected-class hatred, extremist praise, targeted harassment, or identifying details.

Never invent crimes, motives, affiliations, quotes, or evidence. Put links under literal `## Sources`. Do not add the serious findings footer or signoff.

## 5. StarIntel changelog

Read the allow-list from `config/starintel-repos.txt`.

Only landed work on each configured canonical `main` or `master` branch is eligible. Do not report open PRs, branch-only work, CI-only churn, formatting-only changes, trivial docs, or material already covered.

### Changelog unit and dedupe contract

A changelog report is for exactly one project. Never combine unrelated projects into one Discord post or one report file.

Examples of separate project units include `prolog-rlm`, `hackmode`, `zara`, and the StarIntel project family. If more than one project has useful new landed work, create a separate report file and Discord message for each project. Do not create a cross-project roundup.

Before creating a report for a project:

1. inspect prior changelog report files and `state/published.json`;
2. identify the landed commits or completed change already represented for that project;
3. exclude anything already reported, even if it could be worded differently or grouped differently;
4. only report the remaining genuinely new landed work.

Do not duplicate a StarIntel update merely because another project changed in the same run. Do not repost unchanged material to make a run look productive.

If a project has no genuinely new landed work after per-project deduplication, create no report for that project and send nothing for it. If every project is empty after deduplication, output nothing.

When useful new work exists for one project, create one file for that project:

```text
reports/starintel-updates-changelog/<UTC-datestring>-report.md
```

Keep it compact, usually 2 to 5 bullets or short paragraphs. Lead with what became possible or more reliable. Include direct landed commit links for public source repositories. For private configured sources, never include private repository or commit links and follow the `Private-source changelogs` sanitization contract in `STYLE.md`. Only state test results or counts actually observed. Never invent coverage.


### Full Lost-Rob0t owner changelog

The one-project rule above remains the default for `starintel-updates-changelog`. The full Lost-Rob0t roundup is a separate product and is the explicit cross-project exception.

When the user asks for a full Lost-Rob0t changelog:

1. enumerate repositories owned by `lost-rob0t` that had push activity during the requested window;
2. for every public candidate, inspect commits on its actual default/canonical branch and keep only commits landed inside the fixed report window;
3. include every public repository with at least one qualifying canonical-branch commit, even when it is not in the StarIntel allow-list;
4. group noisy commit sequences into the capability, reliability, security, release, or workflow change they produced;
5. use representative direct landed commit links instead of dumping every commit;
6. state the exact report window and observed per-repository counts when counts were actually enumerated;
7. keep this product's dedupe independent from StarIntel Shipyard so the owner roundup may summarize commits that previously appeared in a project post, while repeated owner roundups still dedupe against prior owner roundups.

Private repositories are never expanded in the public owner roundup. Push activity may be acknowledged only in aggregate. Do not publish private repository names, links, commit IDs, branch names, commit messages, issue/PR metadata, or implementation details. The private-source rules in `STYLE.md` remain mandatory.

Create the report at:

```text
reports/lost-robot-changelog/<UTC-datestring>-report.md
```

A full roundup means full changed-repository coverage for the fixed window, not a raw commit dump. Long reports may span multiple Discord messages; the publisher's Markdown-aware splitter owns transport chunking.

## 6. Publication contract

Before every write, verify the target repository is exactly `lost-rob0t/starintel-discord-reporting`. All source/research repositories are READ-ONLY.

GitHub Actions may publish reports, but delivery is successful only when Discord returns valid message JSON for every chunk with non-empty `id` and `channel_id`, and the publisher persists a durable `verified-delivered` receipt keyed by report path.

The receipt stores:

- report digest;
- Discord message ID(s);
- channel ID;
- attempted/accepted/delivered timestamps;
- verified delivery status.

If the returned channel ID does not match the configured expected destination, stop publishing to that webhook and record the mismatch without exposing secrets.

If publication or receipt persistence fails, debug the reporting repo. Do not claim the report posted until the verified receipt exists.

If nothing deserves a post and backlog is clean, make no report commit and send nothing to Discord.
