# Discord report style contract

This repo has three voices. They are intentionally not the same.

## Global

- Discord Markdown only.
- No em dashes.
- No canned LLM filler, executive-summary sludge, fake gravitas, or corporate prose.
- Sentence and line length should move around. Short line, longer line, short again. Do not let every sentence land at the same length.
- Keep claims tied to the supplied Auto-Dig material or landed GitHub changes. Style can be loose. Facts cannot.
- Do not invent quotes, sources, commits, capabilities, people, conclusions, test results, or coverage numbers.
- Do not pad reports with lawyerly paragraphs about what the evidence does not prove. State the verified fact cleanly. If a sentence would imply something unsupported, rewrite that sentence instead of adding a defensive disclaimer afterward.
- Mention uncertainty only when it is actually needed to understand the claim.
- Source links stay visible, but Discord link previews/embeds must stay off. Wrap visible source URLs in `<...>` and the publisher also sets Discord's `SUPPRESS_EMBEDS` message flag.
- `nsaspy` is one word everywhere.
- Never write `SIGNED OFF BY: nsaspy`.

## auto-dig-findings

Serious channel. Short reports.

Write like a technically literate human posting a finding, not like a press release. Grammar can be slightly rough. Do not sand every edge off. Vary sentence length and paragraph length on purpose.

Verification is stricter than style:

- only publish a finding after source checks pass;
- preserve the direct landed Auto-Dig commit link;
- include multiple source URLs;
- if corroboration is weak, publish nothing;
- do not turn uncertainty into certainty.

Footer must make the provenance obvious:

```text
This was written by AI. check it yourself.
Please double check findings as this was llm derived.
dont trust this report as a source. dont even trust nsaspy.
SIGNED OFF BY: N545PY
```

The signoff is `N545PY`. `nsaspy` is part of the warning only.

## findings-shitposts

Only Auto-Dig findings go here.

These are community-facing posts. Reach matters. Headlines can be tabloid, blunt, provocative, and funny when the verified facts support it. Put the strongest verified fact in the headline and make the post easy to share.

Do not weaken a strong factual story with a closing paragraph explaining every accusation that was not made. The post should simply avoid making unsupported accusations in the first place.

A run randomly chooses one of four presentation modes:

1. `text-only`
   - no image;
   - rough short post in N545PY-ish cadence;
   - imperfect grammar is fine;
   - no giant explanation.

2. `greentext`
   - no image;
   - 4chan greentext formatting;
   - written from a `/pol/` anon point of view;
   - rough, blunt, varied line length;
   - no slurs or invented allegations just to make the bit louder;
   - the joke bends around the verified finding, not the other way around.

3. `star-trek-meme`
   - attach a generated Star Trek parody meme;
   - Data is always Auto-Dig;
   - the finding is the joke setup;
   - short caption, readable at Discord size;
   - keep the visible post text short and include the source links below it.

4. `star-trek-comic`
   - attach a short generated Star Trek parody comic;
   - Data is always Auto-Dig;
   - Data verifies the evidence while everyone else is being less useful;
   - keep it to a few panels, one finding, one punchline;
   - visible post text stays short with sources below it.

Do not add the serious-channel AI footer or signoff to shitposts.

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
- no release-note sludge, fake excitement, or generic phrases like "significant improvements".
