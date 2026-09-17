# LLM-Log: historical expert backfill, auditable exports and honest quota coverage

## FOLLOW-UP

This edition covers historical backfill, dataset provenance and the separate quota/coverage contracts in depth.

September 17, 2026. LLM-Log can now project historical captures into its expert corpus and export evidence-backed outcome datasets. The work keeps transport success, task outcomes, usage and pricing context separate instead of manufacturing missing labels.

## Changes

### Historical backfill can resume without duplicating the corpus

The new backfill path reads historical events.jsonl data with stable capture IDs and atomic checkpoints. Re-running or resuming the projection is intended to be idempotent, rather than producing another independent observation for every previously processed capture.

Maintenance is handled by the already-running expert child through a loopback-only API. A second process does not independently open the live Tek9 database. The command-line query entry point exposes declared read-only expert operations through that owner.

That ownership boundary matters as much as the command name. A convenient maintenance CLI should not introduce a competing live database owner simply because it runs outside the main proxy process.

### Token usage does not require invented task context

A standalone request-level observe_usage operation lets historical token usage be projected without making up a task, a price or an outcome that the original capture never established.

Optional provider-transport outcome evidence remains weak evidence. An HTTP success is not promoted to task success. This keeps a useful dataset distinction intact: the provider accepted or answered a request is not the same proposition as the agent completed the user's task correctly.

### Exports retain a path back to the raw capture

Outcome queries now support cursor pagination, including traversal past the former 256-candidate ceiling. The integration contract traverses 257 examples to exercise the boundary and check for duplicate or lost assertions.

The export command joins expert provenance back to exact raw captures and writes a SHA-256 manifest. That makes the exported dataset inspectable: a derived row can be traced back to the capture that supports it, and the exported files have a recorded integrity manifest.

This completes a historical-backfill/query/export slice. It does not announce finished SFT, DPO or tool-trajectory training transforms. Those later projections require their own semantics and verification rather than a new filename on the same raw export.

### Quota displays and timelines distinguish what is actually known

Separate landed work adds provider-reported quota telemetry for the desktop widget pair and per-field graph coverage with bounded nonblocking corpus readers. These are useful distinctions when a timeline contains partial information: absence of a reported field should not automatically become zero usage or a full allowance.

Provider quota, locally observed consumption and historical dataset coverage answer different questions. A graph should state which one it is presenting rather than collapse them into a single precise-looking number.

## Android scope and verification

These are proxy/expert/analytics capabilities, not a newly released Android LLM-Log APK. An Android client using a configured proxy still needs the appropriate authenticated product-facing interface; the loopback maintenance API is not a mobile endpoint to expose publicly.

The merged export PR links passing expert-plane, analytics and quota workflows at its verified head. The 257-row traversal is test evidence for pagination, not a claim about the size or quality of a user's production corpus.

## Sources

Historical backfill and export: <https://github.com/lost-rob0t/llm-log/commit/692d3820f638c011fc248a7694ecabd72a6e2895>
Ownership, evidence semantics and recorded verification: <https://github.com/lost-rob0t/llm-log/pull/84>
Provider quota telemetry: <https://github.com/lost-rob0t/llm-log/commit/9f9971053dc3796c70955105943de42716775513>
Per-field coverage and bounded readers: <https://github.com/lost-rob0t/llm-log/commit/171cf7a21a8a0f669ff07f3358fc82852c3406ef>
