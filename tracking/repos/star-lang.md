# lost-rob0t/star-lang

- generated: `2026-10-14T23:16:27Z`
- canonical branch: `main`
- changelog eligible: `yes`
- head: [`4c8d1e19249a5030b7d97f953f694c09849b9131`](https://github.com/lost-rob0t/star-lang/commit/4c8d1e19249a5030b7d97f953f694c09849b9131)
- head date: `2026-10-11T03:28:27-04:00`
- head subject: Merge pull request #216 from lost-rob0t/feat/kb-producer-runtime

## Git log, last 14 days

```text
2026-10-11 4c8d1e19249a5030b7d97f953f694c09849b9131 Merge pull request #216 from lost-rob0t/feat/kb-producer-runtime
2026-10-11 73a1406dd29903e9b7024fe59ff9c804837b33c8 build(runtime): export existing installed SBCL and SWI producer boundary
2026-10-10 1876a5545db5e5a64b6a75e675f8d60a6bad3385 Merge pull request #214 from lost-rob0t/fix/process-drain-termination-ack-20261011
2026-10-10 e8bb001cb521381af984de1649ec642138c52519 fix(process-port): reserve cleanup budget for termination joins
2026-10-10 5c5e7454f7cd735cf53a2b2e992401718a5f47a6 test(process-port): reproduce asynchronous capture termination race
2026-10-10 bfba04a15f43215cd323e1dde2d98a7343abb3ea Merge pull request #213 from lost-rob0t/feat/swi-relation-neighbors-20261011
2026-10-10 6da7190ffa5a59ff45f6a2beb19b5720d6e8ac26 fix: reject malformed SWI sessions before generic diagnostic fallback
2026-10-10 78af108c1e43bc04fb35dbc611a97d293c639277 feat: execute bounded relation-neighbors through supervised SWI sessions
2026-10-10 a551fdf0a60a4901dd57c559bad36f8c905b0dc6 test: bound circular backend diagnostics for unsupported-method RED
2026-10-10 1fe0061c5fee594ea810d05d029b55f173213a0e test: register relation regressions in the real integration suite
2026-10-10 6c95539ae2ec23a0867a38ba41df2aca5803ba12 test: prove bounded relation query is missing from real SWI adapter
2026-10-10 bd82ff644ac149b59cc5c58b49f246f031e43f7f Merge pull request #206 from lost-rob0t/feat/204-complete-0101-compatibility-bundle
2026-10-10 d238e8c3dcfd1d8ca787b084a56614360cbbe295 Merge pull request #209 from lost-rob0t/fix/208-drift-bundle-parity
2026-10-10 27a9f6422b15ae6fcd15bb075e57fab2bde47e11 Merge pull request #205 from lost-rob0t/fix/204-consumer-bundle-path-prerequisites
2026-10-10 069a538a8475a50152d62f521302991fd9dbd9fe test: retain aggregate diagnostics for malformed bundle entries (#208)
2026-10-10 0c76f62558e925e22d8ac1206238546ba22d1f90 fix: keep malformed bundle mappings in structured drift diagnostics (#208)
2026-10-10 fad4d5b332877f3378371b7a0b0083eb56ef6242 fix: share bundle filesystem verification with drift reporting (#208)
2026-10-10 281656d17aff9f19b9f07cd6adabf1a37a3521da fix: share bundle filesystem verification with drift reporting (#208)
2026-10-10 1fd3c2ffcc5087f531b0da4e25c90f892dca70c0 ci: run drift diagnostics before bundle generation (#208)
2026-10-10 8cf91fb12e4638cea2f8850d12dfa3c0131cd00f test: expose bundle drift layout and import-shadow false negatives (#208)
2026-10-10 2e5ea976b69b90317dc250b134eb104a91074b82 test(starintel): keep vendored migration checks active under Python -O
2026-10-10 0c1924562c0378312a7883638ce09340c793f494 fix(starintel): bound immutable HTTP artifact downloads
2026-10-10 38cc7b850419b8332f8cc770b82da5717ca1a2d2 fix(starintel): keep raw JSON conformance checks active under Python -O
2026-10-10 9d6a0d684146cafe2ff5c42c1079f6972bed1ed6 fix(starintel): validate authority release locks before reading
2026-10-10 73b1c39b2f80b518a45a600b288383054c0a3626 test(starintel): aggregate deterministic offline consumer drift reports
2026-10-10 0132cb1edbfe011739b216813ec7b5d6bc5623fd ci(starintel): reject stale committed compatibility bundle lock
2026-10-09 22942af6f9411588b4abca4717eef0b73cefa727 fix: reject nonregular consumer files before any blocking read (#204)
2026-10-09 e767392f8f8023b202876091319c46a93fa0d3c4 fix: keep consumer locks outside bundles and reject linked targets (#204)
2026-10-09 0badc219b191e319b9b96fbe2fe1a3be389be086 fix: reject unlisted import shadows in closed bundle destinations (#204)
2026-10-09 ce8c4f544f6dd4a6bf103d70a0c4cc62ace495f0 fix: preserve executable mode of authority release finalizer
2026-10-09 ecdf0b502e4e887fd5ea51d5915f1c0c6feafa18 build: commit CI-generated bundle and enforce regeneration drift checks (#204)
2026-10-09 1d4e677a3dc137b852431e36e92a48a6946bf78b fix: enforce complete bundle layout and explicit-mode validation (#204)
2026-10-09 ee28e47395a846a73a94bf6d0bc34e050cfea3aa feat: generate and verify complete 0.10.1 reader bundles (#204)
2026-10-09 4e6ca650ccd3dee861e3253678e8a3d785b67d62 test: require complete relocated 0.10.1 compatibility bundles (#204)
2026-10-09 c4216bfca1e70500cc373f14c5c093dec6b4f5c9 docs: withdraw next-version planning and focus only on 0.10.1 (#204)
2026-10-09 646ebd54824eeeb281fee5fd9fb5fa8d5cb6b794 docs: record gated 0.10.2 transition and bundle prerequisites (#204)
2026-10-09 99f0995edc984d5b4e9160a55d5eb3628afaa390 ci: require Nix gates for specification and consumer tool changes (#204)
2026-10-09 592a142cab8f6aa161238ff5da189062e6abf443 fix: reject unsafe consumer targets and duplicate source mappings (#204)
2026-10-09 e13f1109b896251f3544ee9702fcef8c23becf3f test: expose unsafe consumer paths and duplicate source mappings (#204)
2026-10-04 fa1c8f4fb0590526c39aa3e9bc4a7e6eac30bea7 Merge pull request #202 from lost-rob0t/perf/starrouter-wire-prerequisites
2026-10-04 96d26c338078676ec1dc6928755901636c9f7ef0 Add canonical actor wire, document bus guards and strict raw JSON conformance
2026-10-04 e9ec1d883627d186aafe0b3647bdc29baea03543 Merge pull request #200 from lost-rob0t/codex/versioned-exact-wire-20261004
2026-10-04 8d632c0592cbdb8b2896736ea3173991e3f06442 Enforce strict date-time bounds independent of optional checker behavior
2026-10-04 4e04009716a3e9aa810f38bc1acda3ea46d41388 Preserve exact numeric values in versioned historical readers and reversible migrations
2026-10-04 9198370f7a6f3e2a5ea00af3efdb6d705e102650 Publish generated 0.10.1 canonical authority dependency
2026-10-03 debb752b1264a9d237cb51dce7d3bde345b2d8b5 Define canonical research operation and investigation target contracts
2026-10-03 5837e9924cf4ead99ccf085521121c7f6ad4703e Verify the complete vendored release offline for package builds
2026-10-03 ebec36cd8cb5964384aa28278325258c2e54c0e8 Preserve final compiler binding generators in the compatibility shell
2026-10-03 afb0587b90f2b45d4f5e9481738dbd598f51401c Document mandatory generated release consumption for every downstream
2026-10-03 721699216436f4f9c516d678bb7caaaa581370df Ignore Python release-tool caches
2026-10-03 765f1673851192bcaf1cdd2f35c47608f979b079 Use portable email pattern in the canonical StarLang source
2026-10-03 13cbd34ef8f411ba87b8cd7b001a6a7d17475574 Regenerate StarIntel 0.10.1 and add immutable downstream consumption gate
2026-10-03 3b4c643e79769e1e86c910ea47014095aedad49f test(starintel): fix network capture FiveAM assertions
2026-10-03 40b699e5d5bc8e6de324c5d43e40938aefbcfa45 fix(starintel): restore canonical 0.10.1 network-capture contracts
2026-10-03 d31d6227bdf01fed8c6884b5df6ac44d0a29f951 ci(starintel): remove temporary generation helper
2026-10-03 959cca6fe1dbd52c04b0a1ef02e4ba3a7d25a88e chore(starintel): regenerate 0.10.1 release artifacts
2026-10-03 818d6f424e523f5eac38eb01595b9a0b7bd97d03 ci(starintel): regenerate release artifacts
2026-10-03 54fe9a2c8596297b345d86540908effedce9e484 fix(starintel): inherit map-layer validity fields
2026-10-03 b2f31a582006e99af62c15d28d81e7254e23da66 ci(starintel): remove temporary generation helper
2026-10-03 fc7a56c8f4eb2fe407573fc320e4fb76cb852c45 chore(starintel): regenerate 0.10.1 release artifacts
2026-10-03 2a39ae8313962e3cd3d569c317d321fe2b3a1089 ci(starintel): commit regenerated release artifacts
2026-10-03 c9ecf8c0c4fa12453c8091351c889afb08bea4a6 ci(starintel): upload regenerated release preview
2026-10-03 f0f14fb08d71df8dc861087f37e424bfddb8c53a feat(starintel): add mission and spatial contracts
```

## Repository paths changed, last 14 days

```text
.github/workflows/ci.yml
.github/workflows/nix.yml
.github/workflows/starintel-bundle.yml
.github/workflows/starintel-release-preview.yml
.gitignore
CHANGELOG.md
ci/target-systems.txt
docs/DOCUMENT-BUS-CONFORMANCE.md
docs/DOMAIN-SERVICE-CONTRACT.md
docs/LANGUAGE-SUPPORT.md
docs/implementation-slices/ACTOR-RUNTIME-MIGRATION-MATRIX.md
docs/implementation-slices/FINAL-RUNTIME-OWNERSHIP-ACTORS-INGEST.md
fixtures/actor2actor/lifecycle-v1/README.md
fixtures/actor2actor/lifecycle-v1/accepted.json
fixtures/actor2actor/lifecycle-v1/cancel.json
fixtures/actor2actor/lifecycle-v1/completed.json
fixtures/actor2actor/lifecycle-v1/exact-document.json
fixtures/actor2actor/lifecycle-v1/exact-reply.json
fixtures/actor2actor/lifecycle-v1/exact-request.json
fixtures/actor2actor/lifecycle-v1/reply.json
fixtures/actor2actor/lifecycle-v1/request.json
fixtures/actor2actor/lifecycle-v1/unknown.json
flake.nix
prototype/binding-generator-prototype.lisp
prototype/canonical-json-binding-tests.lisp
specs/starintel/0.10.1/GEO-MISSION-MIGRATION.md
specs/starintel/0.10.1/NETWORK-CAPTURE-MIGRATION.md
specs/starintel/0.10.1/RESEARCH-CONTRACTS.md
specs/starintel/0.10.1/SUPPORTED-WORKFLOWS.md
specs/starintel/0.10.1/bundle-lock.json
specs/starintel/0.10.1/core.star
specs/starintel/0.10.1/generated/portable-manifest.json
specs/starintel/0.10.1/generated/schema.json
specs/starintel/0.10.1/generated/starintel.lisp
specs/starintel/0.10.1/generated/starintel_types.nim
specs/starintel/0.10.1/generated/starintel_types.py
specs/starintel/0.10.1/generated/starintel_types.ts
specs/starintel/0.10.1/legacy-workflow-oracle.json
specs/starintel/0.10.1/operation_semantics.py
specs/starintel/0.10.1/release-lock.json
specs/starintel/0.10.1/research-fixtures.json
specs/starintel/0.10.1/supported-workflow-fixtures.json
specs/starintel/0.10.1/supported-workflow-inventory.json
specs/starintel/0.10.1/supported-workflow-mappings.json
specs/starintel/0.10.1/workflow_semantics.py
specs/starintel/BUNDLE-CONSUMPTION.md
specs/starintel/README.md
specs/starintel/VERSION-TRANSITION-PLAN.md
specs/starintel/compatibility/0.9.0/schema.json
specs/starintel/compatibility/README.md
specs/starintel/compatibility/canonical-migration-fixtures.json
specs/starintel/compatibility/capabilities.json
specs/starintel/compatibility/historical-reader-fixtures.json
specs/starintel/compatibility/numeric-canonical-migration-fixtures.json
specs/starintel/compatibility/numeric-historical-reader-fixtures.json
specs/starintel/compatibility/raw_json_numbers.py
specs/starintel/compatibility/registry.json
specs/starintel/compatibility/versioned_reader.py
specs/starintel/wire/README.md
specs/starintel/wire/raw-json-unique-keys.json
star-actor-protocol/src/actor2actor.lisp
star-actor-protocol/src/packages.lisp
star-actor-protocol/src/portable-json.lisp
star-actor-protocol/src/portable-payload.lisp
star-actor-protocol/src/portable-snapshot.lisp
star-actor-protocol/src/service-description.lisp
star-actor-protocol/star-actor-protocol.asd
star-actor-protocol/tests/actor2actor-tests.lisp
star-actor-protocol/tests/service-description-tests.lisp
star-actor-protocol/tests/star-actor-protocol-tests.asd
star-actor-wire/src/binding.lisp
star-actor-wire/src/wire.lisp
star-actor-wire/star-actor-wire.asd
star-actor-wire/tests/binding.lisp
star-actor-wire/tests/exact-json.lisp
star-actor-wire/tests/exact-wire-smoke.lisp
star-actor-wire/tests/test_exact_document.py
star-canonical-json/src/canonical-json.lisp
star-canonical-json/src/packages.lisp
star-canonical-json/src/starlang-wire-json.lisp
star-document-bus/src/document-bus.lisp
star-document-bus/star-document-bus.asd
star-document-bus/tests/document-bus-tests.lisp
star-logic-adapter-swi/README.md
star-logic-adapter-swi/prolog/star_logic_bootstrap.pl
star-logic-adapter-swi/src/adapter.lisp
star-logic-adapter-swi/src/conditions.lisp
star-logic-adapter-swi/src/identity.lisp
star-logic-adapter-swi/src/relations.lisp
star-logic-adapter-swi/star-logic-adapter-swi.asd
star-logic-adapter-swi/tests/relation-tests.lisp
star-logic-adapter-swi/tests/star-logic-adapter-swi-integration-tests.asd
star-process-port/README.md
star-process-port/src/process.lisp
star-process-port/star-process-port.asd
star-process-port/tests/star-process-port-tests.lisp
star-zmq/src/wire.lisp
star-zmq/star-zmq-actors.asd
starlang-compiler/tests/starlang-compiler-tests.lisp
tools/finalize-starintel-release.py
tools/report-starintel-consumer-drift.py
tools/sync-starintel-consumer.py
tools/test-starintel-consumer-drift.py
tools/test-starintel-consumer-optimized.py
tools/test-starintel-consumer.py
tools/test-starintel-raw-json-harness.py
tools/test-starintel-raw-json.py
tools/test-starintel-research-contracts.py
tools/test-starintel-versioned-reader.py
tools/test-supported-workflow-contracts.py
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/ci.yml
.github/workflows/nix.yml
.github/workflows/starintel-bundle.yml
.github/workflows/starintel-release-preview.yml
ci/target-systems.txt
flake.nix
star-actor-protocol/star-actor-protocol.asd
star-actor-protocol/tests/actor2actor-tests.lisp
star-actor-protocol/tests/service-description-tests.lisp
star-actor-protocol/tests/star-actor-protocol-tests.asd
star-actor-wire/star-actor-wire.asd
star-actor-wire/tests/binding.lisp
star-actor-wire/tests/exact-json.lisp
star-actor-wire/tests/exact-wire-smoke.lisp
star-actor-wire/tests/test_exact_document.py
star-document-bus/star-document-bus.asd
star-document-bus/tests/document-bus-tests.lisp
star-logic-adapter-swi/star-logic-adapter-swi.asd
star-logic-adapter-swi/tests/relation-tests.lisp
star-logic-adapter-swi/tests/star-logic-adapter-swi-integration-tests.asd
star-process-port/star-process-port.asd
star-process-port/tests/star-process-port-tests.lisp
star-zmq/star-zmq-actors.asd
starlang-compiler/tests/starlang-compiler-tests.lisp
```
