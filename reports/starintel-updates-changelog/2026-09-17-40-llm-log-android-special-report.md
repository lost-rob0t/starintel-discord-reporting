# LLM-Log Android special: distinguish missing usage data from zero usage

## FOLLOW-UP

Mobile integration companion to the expert-corpus and quota-coverage deep dive.

## Changes

The analytics changes track per-field coverage and use bounded nonblocking corpus readers. This matters for a phone usage display: a missing field is not automatically zero consumption, unlimited quota or a complete history.

Provider-reported allowance, locally observed request usage and historical-corpus coverage are different measurements. A mobile UI should identify which measurement it is showing and its coverage, rather than combine them into one precise-looking meter.

Historical expert backfill also keeps weak transport outcomes separate from task success. An HTTP success can support a transport observation; it does not prove that the user's task succeeded. Preserve that distinction when presenting an activity history on a small screen.

The expert maintenance API is loopback-only and served by the existing database-owning child. Do not expose it as an unauthenticated phone endpoint merely to make a remote dashboard work. A mobile-facing interface needs its own supported authentication and access boundary.

This is integration guidance for the host-side analytics/expert work. No new LLM-Log Android APK or verified phone dashboard is announced.

## Sources

Per-field coverage and bounded readers: <https://github.com/lost-rob0t/llm-log/commit/171cf7a21a8a0f669ff07f3358fc82852c3406ef>
Backfill and evidence semantics: <https://github.com/lost-rob0t/llm-log/pull/84>
