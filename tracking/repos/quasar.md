# lost-rob0t/quasar

- generated: `2026-10-11T05:52:37Z`
- canonical branch: `main`
- changelog eligible: `yes`
- head: [`f387ad2e36aaef7d1ccd3908e70c979b3e12f577`](https://github.com/lost-rob0t/quasar/commit/f387ad2e36aaef7d1ccd3908e70c979b3e12f577)
- head date: `2026-10-10T23:22:01-04:00`
- head subject: Merge pull request #107 from lost-rob0t/feat/bounded-workbench-reads

## Git log, last 14 days

```text
2026-10-10 f387ad2e36aaef7d1ccd3908e70c979b3e12f577 Merge pull request #107 from lost-rob0t/feat/bounded-workbench-reads
2026-10-10 2d6c23517c24d80653d227bbb4f492b1003ac4de fix: validate workspace admission and bound query continuations
2026-10-10 ee715bfcd1e0f943d4e17cdd1cdd3ae8de75bdd6 test: expose workspace admission and cursor size regressions
2026-10-10 3b844b7d5fabf43769ef060119dd79b6a1f46d6a fix: verify pinned Nix Tek9 source before bootstrap
2026-10-10 64859785eb40b3ce14090d09f021b088dfa47a66 feat: add bounded Tek9 bootstrap and document queries
2026-10-10 8199962373a9733b6dddda54e25ee6a7508cd835 Merge pull request #105 from lost-rob0t/fix/websocket-disconnections
2026-10-10 71fa10936df54ac130eaaa515c67cc6fd62d0873 fix: reconcile websocket recovery and workspace loading status
2026-10-06 9079604f766990db7f9b8998705862c4fa914c45 Merge pull request #103 from lost-rob0t/feat/tek9-wireless-source-imports
2026-10-06 593e6836fd95d5e20d8bf84f56aa37378594336b fix: adapt target submissions to the server v1 command contract
2026-10-04 2c3222dc471a4e4baa96fd9fa98b020bdc9763a9 Compose startup actor settings migrations with conflict-safe one-time persistence
2026-10-04 64f991bac289d05f16d96389d921d184d011e6f4 Reconcile identical concurrent view installations without hiding genuine errors
2026-10-04 106788cea9117bfa779499b3f0666a2defd82cea Destroy shared PouchDB test database without closing its cached connection
2026-10-04 f54b3d767f492e8c75b1b860d0ff0c4dc408a973 Reproduce concurrent view initialization against real IndexedDB
2026-10-04 62b0431f5c707153a7311d2129c1e63b2f618f02 Preserve new legacy graph drafts through canonical editor migration
2026-10-04 20fcfe5f879af8929bdffb6b425eaaac5f406bb5 Align existing browser journeys with canonical editor fields
2026-10-04 6ed2db0f17389f62746b88d84ef29b158229d6d0 Add bounded desktop wireless imports with canonical migration prerequisites
2026-10-04 4adb3690fdc4c8efee5cf2e0c87bac8243f99ccb Merge pull request #102 from lost-rob0t/feat/actor-registry-browser
2026-10-04 f4286d8e9fa1b5f1793a8bf7e9332e8813b8aec7 fix: preserve actor studio button semantics
2026-10-04 880f1abbf72c73a71ea6b9d062d843f3cc3f113e feat(actors): consume canonical server registry
2026-10-03 4792cfe8e2320208e0247f6e38f2b53fae40360a Merge pull request #101 from lost-rob0t/feat/multi-user-funding-licensing
2026-10-03 e66923844e8d087f5e65199998accc3d07191a4f feat: connect hosted UI to private auth bridge
2026-10-03 31ba6476718b18ab429f8a88e3280bab843bd6db feat: enforce hosted multi-user policy hooks
```

## Repository paths changed, last 14 days

```text
.prolog/kb/bounded_reads.pl
.prolog/kb/index.pl
.prolog/kb/starintel_actor_registry.pl
.prolog/kb/websocket_lifecycle.pl
AGENTS.md
README.md
control-plane/src/actors/melissa/bridge.lisp
control-plane/src/actors/melissa/entity.lisp
control-plane/src/actors/melissa/normalize.lisp
control-plane/src/actors/melissa/packages.lisp
control-plane/src/actors/melissa/transport.lisp
control-plane/src/bounded-read-commands.lisp
control-plane/src/bounded-reads.lisp
control-plane/src/clog-host.lisp
control-plane/src/control-plane.lisp
control-plane/src/debug-logging.lisp
control-plane/src/main.lisp
control-plane/src/packages.lisp
control-plane/src/phase2-stage-write.lisp
control-plane/src/phase2-store-core.lisp
control-plane/src/plugin.lisp
control-plane/src/pro-actors.lisp
control-plane/src/protocol.lisp
control-plane/src/starintel-contract.lisp
control-plane/src/store.lisp
control-plane/src/websocket-server.lisp
control-plane/src/workspace.lisp
control-plane/tests/bounded-read-benchmark.lisp
control-plane/tests/bounded-read-tests.lisp
control-plane/tests/control-plane-tests.lisp
control-plane/tests/logging-tests.lisp
control-plane/tests/melissa-restart-tests.lisp
control-plane/tests/melissa-tests.lisp
control-plane/tests/phase2-adversarial-v2.lisp
control-plane/tests/phase2-large-corpus-tests.lisp
control-plane/tests/phase2-protocol-tests.lisp
control-plane/tests/phase2-storage-spec-tests.lisp
control-plane/tests/plugin-tests.lisp
control-plane/tests/pro-actor-tests.lisp
control-plane/tests/standalone/canonical-boundary.lisp
control-plane/tests/standalone/wireless-import-persistence.lisp
control-plane/tests/standalone/workspace-contract.lisp
control-plane/tests/tek9-store-adversarial-tests.lisp
control-plane/tests/tek9-store-tests.lisp
docs/ADR-TEK9-WORKSPACE-STORAGE.md
docs/ARCHITECTURE.md
docs/BOUNDED-READ-PERFORMANCE.md
docs/BOUNDED-WORKBENCH.md
docs/SQLITE-IMPORT-BOUNDARY.md
docs/WEBSOCKET-DEBUGGING.md
docs/WIRELESS-IMPORTS.md
docs/bounded-read-measurements.json
example_configs/init.lisp
flake.nix
frontend/docs/STARINTEL-0101-MIGRATION.md
frontend/e2e/actor-settings.spec.ts
frontend/e2e/application.spec.ts
frontend/e2e/canonical-documents.spec.ts
frontend/e2e/graph-destructive-ops.spec.ts
frontend/e2e/live-actor-discovery.spec.ts
frontend/e2e/route-density.spec.ts
frontend/e2e/startup-evidence.ts
frontend/e2e/target-actors.spec.ts
frontend/e2e/view-installation.spec.ts
frontend/e2e/wireless-imports.spec.ts
frontend/package-lock.json
frontend/package.json
frontend/playwright.config.ts
frontend/scripts/export-wireless-test-fixtures.mjs
frontend/src/App.jsx
frontend/src/actor-manager.css
frontend/src/app/hosted-session.ts
frontend/src/app/main.tsx
frontend/src/components/ActorManager.jsx
frontend/src/components/CanonicalDocumentEditor.jsx
frontend/src/components/CanonicalDocumentEditor.test.jsx
frontend/src/components/DocumentEditor.jsx
frontend/src/components/Documents.jsx
frontend/src/components/GraphObjectTypePickerBridge.jsx
frontend/src/components/GraphPage.jsx
frontend/src/components/ImportSettings.jsx
frontend/src/components/ImportSettings.test.jsx
frontend/src/components/MelissaActorMigrationBridge.jsx
frontend/src/components/ProActorManager.jsx
frontend/src/components/ReviewActorBridge.jsx
frontend/src/components/RunAllTransformationsBridge.jsx
frontend/src/components/graph-editors/CompactNodeEditor.jsx
frontend/src/components/graph-editors/CompactRelationEditor.jsx
frontend/src/components/graph-editors/CompactResearchNodeEditor.jsx
frontend/src/components/graph-editors/PredicateAutocomplete.jsx
frontend/src/components/graph-editors/shared.jsx
frontend/src/control-plane/client.ts
frontend/src/lib/actor-settings.js
frontend/src/lib/actor-settings.test.js
frontend/src/lib/actor-transforms.js
frontend/src/lib/actors.test.js
frontend/src/lib/agent-graph-operations.js
frontend/src/lib/canonical-document.js
frontend/src/lib/canonical-document.test.js
frontend/src/lib/db.js
frontend/src/lib/document-batch.js
frontend/src/lib/document-batch.test.js
frontend/src/lib/graph.js
frontend/src/lib/importer.js
frontend/src/lib/importer.test.js
frontend/src/lib/operations.js
frontend/src/lib/operations.test.js
frontend/src/lib/person-identifier-compat.test.js
frontend/src/lib/predicate-catalog.js
frontend/src/lib/rabbitmq-ingest.js
frontend/src/lib/research-node-runner.test.js
frontend/src/lib/research-nodes.js
frontend/src/lib/research-nodes.test.js
frontend/src/lib/review-actor-pack.test.js
frontend/src/lib/schema-form.js
frontend/src/lib/schema-form.test.js
frontend/src/lib/starintel-server.js
frontend/src/lib/starintel-server.test.js
frontend/src/lib/starintel-target-v1.fixture.js
frontend/src/lib/views.js
frontend/src/lib/views.test.js
frontend/src/lib/wireless-import.js
frontend/src/lib/wireless-import.test.js
frontend/src/lib/workflow-migration.test.js
frontend/src/store-canonical.test.jsx
frontend/src/store.jsx
frontend/src/testing/graph-fixtures.test.js
frontend/src/ui-core/QuasarShell.jsx
frontend/src/ui-core/StatusCenter.jsx
frontend/src/ui-core/adapters/shared.js
frontend/src/ui-core/surfaces.css
frontend/tests/fixtures/wireless/kismet.jsonl
frontend/tests/fixtures/wireless/wigle.csv
frontend/tests/unit/control-plane-client.test.ts
frontend/tests/unit/status-center.test.jsx
package-lock.json
package.json
scripts/benchmark-bounded-reads
scripts/bootstrap-lisp-deps
scripts/check-control-plane-deps.mjs
scripts/check-tek9-nix-source.mjs
scripts/dev.mjs
scripts/inspect-websocket.mjs
scripts/run-control-plane
scripts/run-production
scripts/smoke-startup.mjs
scripts/test-bootstrap-lisp-deps.mjs
scripts/test-lisp
scripts/test-wireless-persistence
systems/quasar-control.asd
systems/quasar-tests.asd
vendor/star-cl/LICENSE
vendor/star-cl/UPSTREAM.md
vendor/star-cl/bin/sync-starintel-schema.py
vendor/star-cl/schema/starintel-schema.lock.json
vendor/star-cl/schemas/starintel-0.10.1/compatibility-fixtures.json
vendor/star-cl/schemas/starintel-0.10.1/compatibility.json
vendor/star-cl/schemas/starintel-0.10.1/core.star
vendor/star-cl/schemas/starintel-0.10.1/generated/portable-manifest.json
vendor/star-cl/schemas/starintel-0.10.1/generated/schema.json
vendor/star-cl/schemas/starintel-0.10.1/generated/starintel.lisp
vendor/star-cl/schemas/starintel-0.10.1/generated/starintel_types.nim
vendor/star-cl/schemas/starintel-0.10.1/generated/starintel_types.py
vendor/star-cl/schemas/starintel-0.10.1/generated/starintel_types.ts
vendor/star-cl/schemas/starintel-0.10.1/legacy-workflow-oracle.json
vendor/star-cl/schemas/starintel-0.10.1/operation_semantics.py
vendor/star-cl/schemas/starintel-0.10.1/release-lock.json
vendor/star-cl/schemas/starintel-0.10.1/research-fixtures.json
vendor/star-cl/schemas/starintel-0.10.1/schema-lock-manifest.json
vendor/star-cl/schemas/starintel-0.10.1/supported-workflow-fixtures.json
vendor/star-cl/schemas/starintel-0.10.1/supported-workflow-inventory.json
vendor/star-cl/schemas/starintel-0.10.1/supported-workflow-mappings.json
vendor/star-cl/schemas/starintel-0.10.1/workflow_semantics.py
vendor/star-cl/src/operation-semantics.lisp
vendor/star-cl/src/v0101-package.lisp
vendor/star-cl/src/v0101.lisp
vendor/star-cl/src/v090-package.lisp
vendor/star-cl/src/v090.lisp
vendor/star-cl/starintel-0101.asd
vendor/star-cl/starintel-v090.asd
```

## Test and CI paths touched, last 14 days

```text
control-plane/tests/bounded-read-benchmark.lisp
control-plane/tests/bounded-read-tests.lisp
control-plane/tests/control-plane-tests.lisp
control-plane/tests/logging-tests.lisp
control-plane/tests/melissa-restart-tests.lisp
control-plane/tests/melissa-tests.lisp
control-plane/tests/phase2-adversarial-v2.lisp
control-plane/tests/phase2-large-corpus-tests.lisp
control-plane/tests/phase2-protocol-tests.lisp
control-plane/tests/phase2-storage-spec-tests.lisp
control-plane/tests/plugin-tests.lisp
control-plane/tests/pro-actor-tests.lisp
control-plane/tests/standalone/canonical-boundary.lisp
control-plane/tests/standalone/wireless-import-persistence.lisp
control-plane/tests/standalone/workspace-contract.lisp
control-plane/tests/tek9-store-adversarial-tests.lisp
control-plane/tests/tek9-store-tests.lisp
flake.nix
frontend/scripts/export-wireless-test-fixtures.mjs
frontend/tests/fixtures/wireless/kismet.jsonl
frontend/tests/fixtures/wireless/wigle.csv
frontend/tests/unit/control-plane-client.test.ts
frontend/tests/unit/status-center.test.jsx
scripts/benchmark-bounded-reads
scripts/bootstrap-lisp-deps
scripts/check-control-plane-deps.mjs
scripts/check-tek9-nix-source.mjs
scripts/dev.mjs
scripts/inspect-websocket.mjs
scripts/run-control-plane
scripts/run-production
scripts/smoke-startup.mjs
scripts/test-bootstrap-lisp-deps.mjs
scripts/test-lisp
scripts/test-wireless-persistence
systems/quasar-control.asd
systems/quasar-tests.asd
vendor/star-cl/starintel-0101.asd
vendor/star-cl/starintel-v090.asd
```
