# Prolog-RLM: semantic project knowledge survives restarts without pretending stale facts are current

## FOLLOW-UP

This expands the summary with the review-repair evidence for publication atomicity, multi-project isolation, incomplete indexes and the native grouped-capture regression.

September 17, 2026. The new semantic-project-knowledge slice adds a usable layer between parsed syntax and symbolic reasoning about a project. The follow-up review repairs persistence, index completeness and isolation instead of stopping at an attractive symbol graph.

## Changes

### Grouped syntax captures become typed project observations

Normalization turns grouped Tree-sitter matches into definitions, references, calls, imports and exports. The observations carry project identity, file hash/generation, parse identity, grammar and adapter identity, syntax-node information and byte/point spans.

That provenance lets a consumer ask where a fact came from and whether the underlying extraction still applies. It is not enough to know that a symbol called start existed somewhere in a repository at some point. A plan or navigation result needs the file and extraction that support the observation.

Standard adapter packs cover Python, JavaScript and Common Lisp. Registered host adapters can shadow a standard pack. Unsupported analysis and supported analysis that happens to find zero matches remain distinguishable outcomes.

### Resolution and graph traversal are bounded and explicit

Resolution can report resolved, unresolved, ambiguous or external results. Derived containment, file-dependency relations and cycle-safe call reachability retain supporting observation IDs. The symbol index is built from knowledge that is still current.

The review hardening makes incomplete knowledge visible. Missing project files can produce an incomplete resolution result even when some matching observations exist. Index coherence is partial when stale or unindexed files remain, and complete only when both sets are empty.

That prevents a particularly misleading failure mode: an index presenting a clean answer because it silently ignored the files it had not analyzed. A consumer can now distinguish a bounded answer from a claim of complete project coverage.

### One publication is one atomic journal record

Persistence now records one semantic publication row per extraction publication. A crash cannot leave half of an extraction's semantic rows journaled as though they were a coherent publication. Replaying a publication during hydration is idempotent.

The target project's journal is attached for publication and snapshot operations, preventing a multi-project process from accidentally writing one project's facts into another project's journal. Public reads make a best-effort hydration attempt, so querying after restart does not depend on an unrelated earlier call having loaded the knowledge first.

Currentness is not blindly persisted as a permanent true flag. The extraction journal remains authoritative, so a restart must not resurrect superseded observations as current facts. The tests include fresh-process restart cases and true two-project isolation.

### A native capture bug was fixed at the source

The Tree-sitter query FFI had reused a capture argument slot while constructing grouped results, dropping multi-capture matches. Semantic adapters need those grouped captures, so repairing only the higher-level normalizer would have left a hole below it. A native regression was added alongside the fix.

## Verification and Android scope

The final review commit records 88 native Tree-sitter cases and a broader 1,235-test verification gate, plus deterministic benchmark and CLI checks. These are implementation-recorded results, not fresh execution for this post.

This is the Prolog-RLM project-analysis layer. It does not establish that an Android APK embeds the same native parser stack, nor that Zara's mobile Prolog engine is interchangeable with this runtime. A mobile consumer should preserve provenance and partial/stale states when displaying remote project knowledge; a phone UI must not promote partial coverage to complete knowledge.

## Sources

Semantic normalization and native capture repair: <https://github.com/lost-rob0t/prolog-rlm/commit/42a7cf64edb60b9976957a73dd4f41a38579eb7e>
Atomic publication, isolation and coherence repairs: <https://github.com/lost-rob0t/prolog-rlm/commit/fa41aa355e9fb3b9e248d07d7134792abbc14dd0>
Canonical merge: <https://github.com/lost-rob0t/prolog-rlm/commit/51d2530f0e18c84cff860b7c0bf3afcc3c488057>
