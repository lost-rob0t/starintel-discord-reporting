# Prolog-RLM Android special: keep project provenance and incomplete coverage visible

## FOLLOW-UP

Mobile integration companion to the semantic-project-knowledge deep dive.

## Changes

The review hardening journals a semantic publication atomically, isolates projects and rehydrates knowledge on reads. It also distinguishes complete indexes from indexes with stale or missing files. Those are host-side project-analysis contracts; this change does not package the native Tree-sitter stack into Zara Android.

A mobile project browser consuming this knowledge should show the source file, span and extraction identity behind an observation. A useful answer to where is this defined includes its evidence, not just an unqualified symbol name.

Preserve unresolved, ambiguous, external and incomplete results in the UI. A partial index returning one candidate is not necessarily proof that the whole project has only one candidate. Likewise, stale knowledge loaded after restart must not acquire a current badge simply because it is now in memory.

Suggested acceptance cases are a fresh connection after host restart, two projects containing the same symbol name, an edited file with old observations and a project with one unindexed file. These are integration checks derived from the newly examined persistence/isolation repair, not claims of completed phone tests.

Zara's local Prolog environment and Prolog-RLM's project-analysis runtime should not be treated as interchangeable engines without an explicit supported bridge.

## Sources

Persistence, isolation and completeness repair: <https://github.com/lost-rob0t/prolog-rlm/commit/fa41aa355e9fb3b9e248d07d7134792abbc14dd0>
