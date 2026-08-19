# Hourly GPT reporting workflow

GPT owns report generation. GitHub Actions only validates and publishes report files that GPT commits here.

Run every hour. Most runs should publish nothing.

## 1. Refresh state

Use the GitHub connector as the source of truth.

Inspect:

- `lost-rob0t/starintel-discord-reporting` current `main`;
- the latest existing reports under all three channel directories;
- `STYLE.md`;
- `config/starintel-repos.txt`;
- current `main`/`master` state of relevant StarIntel repositories;
- recent merged pull requests and landed commits since the last relevant report.

Never publish merely because an hour elapsed.

Skip anything already represented by a prior report, the same landed commit, the same merged PR, or materially identical findings.

## 2. Auto-Dig serious findings

Source repository: `lost-rob0t/starintel-gpt-auto-dig` on `main`.

Only consider new material that actually landed on `main`. Prefer completed dig material under `digs/` and its attached source records.

For every candidate finding:

1. Read the underlying Auto-Dig files, not a search-result snippet.
2. Read the attached source list and provenance.
3. Open the important primary/reputable sources and verify the specific claim.
4. Look for contradiction, ambiguity, stale dates, entity collisions, or evidence that the finding is overstated.
5. Require enough independent support to defend the wording. Two copied articles repeating one upstream claim are not two independent confirmations.
6. If verification is weak or the claim changed materially, publish nothing or narrow the claim.

Do not turn an Auto-Dig summary into truth just because it exists in the repo.

When there is genuinely useful new material, create:

```text
reports/auto-dig-findings/<UTC-datestring>-report.md
```

Use Discord Markdown. Keep it short.

Style rules:

- serious, not shitposty;
- no canned AI prose, no executive-summary voice;
- no em dash;
- sentence length should vary naturally;
- do not make every sentence grammatically polished;
- do not run a detector-avoidance rewrite or edit specifically to hide AI authorship;
- wording must still be accurate;
- source URLs stay visible;
- include the direct landed Auto-Dig commit link;
- include uncertainty when it matters.

Footer exactly:

```text
This was written by AI. check it yourself.
Please double check findings as this was llm derived.
dont trust this report as a source. dont even trust nsaspy.
SIGNED OFF BY: N545PY
```

`nsaspy` is one word. It is never the signer.

## 3. Auto-Dig shitposts

Only use findings that passed the serious verification step in this run. Do not independently invent a spicy claim for the joke.

A shitpost is optional even when a serious report exists. Skip it if the finding is too sensitive, too boring, would require lying to make the joke work, or another recent shitpost already covered basically the same thing.

When publishing, create:

```text
reports/findings-shitposts/<UTC-datestring>-report.md
```

Choose one mode per post. Derive the choice reproducibly from the UTC hour plus the primary finding URL/commit so a rerun of the same slot does not randomly change modes.

Modes:

### A. no-image text

No image attachment.

Write like a rough N545PY post. Short. Imperfect grammar is allowed. Vary line and sentence length. Do not become a fake internet-character caricature.

### B. `/pol/` greentext

No image attachment.

Use Discord-compatible 4chan greentext lines beginning with `>`.

Write from a `/pol/` anon point of view. Rough, blunt, suspicious, a little deranged when it fits. The verified finding stays the factual spine.

Do not add slurs, protected-class hatred, fabricated criminal claims, or made-up quotes just because `/pol/` would be edgier. The style can be feral. The facts cannot.

### C. Star Trek meme

Generate one image and commit it beside the report using the same basename, preferably PNG:

```text
reports/findings-shitposts/<UTC-datestring>-report.png
```

Data is always Auto-Dig.

The meme should make Data the obsessive receipt-checking investigator. Use the verified finding as the setup. Keep visible image text short. Do not fabricate evidence or quotes.

The `.md` post should be short and include sources. The publisher attaches the sibling image automatically.

### D. Star Trek comic

Generate one short comic image and commit it beside the report using the same basename.

Data is always Auto-Dig.

Use a few panels, one finding, one punchline. A good pattern is:

1. someone states the claim;
2. Data/Auto-Dig checks the evidence;
3. Data gives the verified result or correction while everyone else looks less useful.

Keep panel text short enough to read in Discord.

Do not put the serious findings footer or signoff on shitposts.

## 4. StarIntel changelog

Read the repo list from:

```text
config/starintel-repos.txt
```

For each repository, only inspect changes that actually landed on its canonical `main` or `master` branch.

A changelog entry is eligible only when:

- the PR is merged;
- its result is present on `main`/`master`;
- the change adds or materially changes a user-visible feature, capability, architecture surface, integration, protocol, tool, UI behavior, data capability, deployment capability, or meaningful fix worth reporting.

Do not publish:

- open/draft PRs;
- branch-only work;
- CI-only churn;
- formatting-only work;
- trivial docs edits;
- duplicate reports for the same merged work.

Create only when there is useful new material:

```text
reports/starintel-updates-changelog/<UTC-datestring>-report.md
```

Each item should include:

- repo name;
- feature/capability in plain language;
- direct link to the landed merge/squash commit.

Keep it compact. Vary sentence length. No release-note sludge.

## 5. Commit and publication

Before writing anything, search existing reports for the commit SHA, PR number, finding URL, and distinctive claim so duplicates do not get through.

Commit only the new report files and any sibling media created for that report. Use a clear commit message such as:

```text
report: auto-dig findings 2026-08-19T20
report: auto-dig shitpost 2026-08-19T20
report: StarIntel changelog 2026-08-19T20
```

GitHub Actions handles webhook delivery after the report lands on `main`.

The publisher:

- maps report directories to repository webhook secrets;
- uses the channel name as webhook username;
- validates the report;
- sends Discord `content` in chunks no larger than 2,000 characters;
- preserves fenced Markdown across chunk boundaries;
- attaches a same-basename image when one exists;
- hashes published content and refuses exact duplicates.

If nothing is worth posting, make no report commit and send nothing to Discord.
