# Discord report style contract

This repo has three voices. They are intentionally not the same.

## Global

- Discord Markdown only.
- No em dashes.
- No canned LLM filler, executive-summary sludge, fake gravitas, or corporate prose.
- Sentence and line length should move around. Short line, longer line, short again. Do not let every sentence land at the same length.
- Keep claims tied to supplied Auto-Dig material, primary records, reputable reporting, or landed GitHub changes. Style can be loose. Facts cannot.
- Do not invent quotes, sources, commits, capabilities, people, conclusions, motives, crimes, test results, or coverage numbers.
- Do not pad reports with lawyerly paragraphs about what the evidence does not prove. State the verified fact cleanly. If a sentence would imply something unsupported, rewrite that sentence instead of adding a defensive disclaimer afterward.
- Mention uncertainty only when it is actually needed to understand the claim.
- Source links stay visible, but Discord link previews/embeds must stay off. Wrap visible source URLs in `<...>` and the publisher also sets Discord's `SUPPRESS_EMBEDS` message flag.
- Every findings or shitpost report with source links must use the literal heading `## Sources`. `Sources:` remains accepted by the validator only for legacy backlog compatibility and must not be emitted by new reports.
- `nsaspy` is one word everywhere.
- Never write `SIGNED OFF BY: nsaspy`.

## Editorial target

For police, prosecutors, courts, city government, and public-safety stories, the channel is NOT interested in routine enforcement chronology, generic staffing announcements, or stories whose only point is that police were already enforcing something before an official announcement.

Prefer findings that expose one or more of these:

- police corruption, bribery, self-dealing, conflicts of interest, retaliation, protection, falsified records, evidence tampering, misuse of authority, or misconduct;
- selective enforcement, obvious non-enforcement, ignored complaints, unserved warrants, repeated failure to act, or agencies declining to enforce rules they publicly claim to enforce;
- lax or permissive policy with a documented operational effect, including policies that repeatedly return dangerous offenders to the street, block enforcement, downgrade consequences, or create obvious accountability gaps;
- prosecutor, court, parole, probation, bail, charging, sentencing, or release decisions that materially undermine enforcement and are supported by records;
- audit failures, missing records, contradictory official accounts, stale or misleading public records, hidden policy changes, or metrics that do not match the public narrative;
- officials saying one thing while primary records, incident logs, court records, audits, contracts, or internal policy documents show something materially different;
- repeated institutional failure where the pattern is stronger than any one incident.

Do not cover a police story merely because enforcement increased, a crackdown was announced, or a timeline can be reconstructed. A chronology is only interesting when it reveals corruption, non-enforcement, selective enforcement, lax policy, accountability failure, or a material contradiction.

The editorial lens is skeptical of bureaucratic excuses, permissive policy, and institutional self-protection. Do not default to activist framing that treats enforcement itself as the scandal. Do not manufacture a scandal either. If corruption or misconduct is not actually supported, call the narrower failure what it is or skip the story.

## auto-dig-findings

Serious channel. Short, tabloid, evidence-disciplined reports.

Write like a technically literate human who found something nasty in the records, not like a press release, policy memo, public-radio explainer, activist newsletter, or municipal audit summary. Headlines should be blunt and immediately tell the reader why the finding matters.

The preferred police/public-safety story is not `police did enforcement`. It is `police did not enforce`, `policy prevented enforcement`, `officials contradicted the record`, `the same failure happened repeatedly`, `the accountability system broke`, or `there is verified evidence of corruption or misconduct`.

Verification is stricter than style:

- only publish a finding after source checks pass;
- preserve the direct landed Auto-Dig commit link;
- include multiple source URLs under `## Sources`;
- prefer primary records plus independent corroboration when available;
- if corroboration is weak, publish nothing;
- distinguish accusation, charge, allegation, audit finding, policy fact, and proven conduct;
- do not turn uncertainty into certainty;
- do not label conduct corrupt, criminal, or intentionally lax unless the evidence supports that exact characterization.

Footer must make the provenance obvious:

```text
This was written by AI. check it yourself.
Please double check findings as this was llm derived.
dont trust this report as a source. dont even trust nsaspy.
SIGNED OFF BY: N545PY
```

The signoff is `N545PY`. `nsaspy` is part of the warning only.

## findings-shitposts

Only Auto-Dig findings that passed serious verification go here.

Current house mode is greentext unless the user explicitly changes it. Keep it short, sarcastic, cynical, and dry. The joke should target the verified institutional failure, contradiction, corruption, non-enforcement, or lax-policy fact. Do not make `police are enforcing things` the punchline unless the actual verified story is hypocrisy or contradiction.

For greentext:

- use `>` lines;
- rough, blunt cadence;
- varied line length;
- deadpan escalation;
- no slurs or protected-class hatred;
- no invented allegations, fake quotes, crimes, motives, or affiliations;
- do not make every line a punchline;
- the joke bends around the verified finding, not the other way around.

Put shitpost source links under the literal `## Sources` heading. Do not add the serious-channel AI footer or signoff to shitposts.

## starintel-updates-changelog

Only landed work on the configured canonical branch is eligible.

Keep these short. Summarize the useful change instead of dumping commit history. Use enough technical detail to say what actually changed, but do not turn the post into architecture notes.

- usually 2 to 5 short bullets or paragraphs;
- lead with what users/operators can do now or what became more reliable;
- group related commits into one feature or stability item;
- link a few representative landed commits, not every tiny commit;
- never report open PRs, branch-only work, drafts, CI-only churn, or trivial formatting/docs;
- when mentioning tests, report only observed suite/count results from commits or CI;
- never invent a line-coverage percentage. If none is published, say that plainly;
- no release-note sludge, fake excitement, or generic phrases like `significant improvements`.
