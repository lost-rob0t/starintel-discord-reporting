# lost-rob0t/quasar

- generated: `2026-08-29T16:45:08Z`
- canonical branch: `main`
- changelog eligible: `yes`
- head: [`b608fd91379e35ff65ef71f34867050d2983c077`](https://github.com/lost-rob0t/quasar/commit/b608fd91379e35ff65ef71f34867050d2983c077)
- head date: `2026-08-27T02:03:59-04:00`
- head subject: Merge pull request #66 from lost-rob0t/ci/exhaustive-runtime-startup-2026-08-27

## Git log, last 14 days

```text
2026-08-27 b608fd91379e35ff65ef71f34867050d2983c077 Merge pull request #66 from lost-rob0t/ci/exhaustive-runtime-startup-2026-08-27
2026-08-27 b864b62ec90e122504e7c0eaeba502512c22a913 fix: enforce repository Nix runtime contract
2026-08-27 11efe0254b2f0f2d332b66683ede20573433c940 ci: test Ubuntu and fresh Nix runtime startup paths
2026-08-27 0f19e95d526d0f5e15fa697b80c33d080aca7a18 test: enforce Lisp and native runtime dependency contracts
2026-08-27 90e493e228e3ca3be7fd1a282aa40b12409d5b6b build: align production Lisp and native runtime contracts
2026-08-27 720a864a6367bbdb2d1f0a4751401517402bd419 test: fail startup smoke immediately on child exit
2026-08-27 5de67530e97abd55386ec14bb8fd401338e0cbbf build: make Nix dev shell self-contained for bootstrap
2026-08-27 1095da21f5507ad52bc7967aa0c6a3d29cdfc0b1 fix: cover all declared Nix runtime libraries
2026-08-27 15cda7cbcc3f1427ffb1e6c95bd0f35111158ccf fix: preflight native runtime before dev startup
2026-08-27 c9e673b949f43b8134b9203d82fe32470b0046a1 test: add native runtime preflight
2026-08-26 9311c9cc26d6c15b6625b814452072bb4e7513ba RAGE #61: filesystem Auto-Dig persistence and initfile config (#62)
2026-08-26 c1e5439b4ae84af2ba069c4b3bd363e78aef702d RAGE #52: carry delegated principal through live WebSocket dispatch (#53)
2026-08-26 3acef088009137a737647b79c404dde615b96c1d RAGE #50: delegated Auto-Dig user session authority (#51)
2026-08-26 aa33622089b7a09745ec41f049c3e03ec3280cd1 Merge pull request #43 from lost-rob0t/rage/41-autodig-lifecycle
2026-08-26 e0e662be968568adbe0f9a22b00b417c92db9ad7 Merge pull request #47 from lost-rob0t/main
2026-08-25 ddcfd62bb63818714605c75de637ed595082177c test: expire worker lease across Sento actor thread
2026-08-25 aea61e9602696a76f5d561e7f0873e501a7ab536 fix: accept persisted numeric Auto-Dig lease timestamps
2026-08-25 19e2a1f057d207794964ad5b4498c388efcd3847 fix: reclaim expired Auto-Dig worker leases
2026-08-25 7f321ecf452bb3263b8c34edee9f738d27a1391a test: make Auto-Dig reclaim RED deterministic
2026-08-25 a548bf608fbc6f1e9a3f230615ca98b929863637 test: run stale Auto-Dig worker reclaim spec
2026-08-25 ff779d67c94ed2f65e4f97aae352cb6f0d3770fa test: specify stale Auto-Dig worker reclaim
2026-08-25 562c3ea00a773b44198430f940b3ce43cc00e21c fix: validate test bootstrap against web test graph
2026-08-25 9a7f7afc82e6d404a80d0afd732ef14e26b92743 fix: preload web deps for autodig auth tests
2026-08-25 91d723a88572d9671c898bd31b2da9dbaf0597f2 test: load WebSocket auth surface for worker session tests
2026-08-25 2ae4ed3e4383057c7759f2d747b95d26661a2f31 build: load Auto-Dig worker session policy in quasar-web
2026-08-25 ebd4163d407a18ffeddc3b4a0ed58627a17f037b feat: register least-privilege Auto-Dig worker sessions
2026-08-25 7e06ba6a699f9b3aa074303aa79304da2909a361 fix: preserve package declarations while exporting worker session
2026-08-25 38177e6172a08dd1bfdf0486909506101ae7f6be feat: export Auto-Dig worker session registration
2026-08-25 1409f5385de4c055ec8956b4dc5f84b48ad534e8 Merge PR #46: repair real-stack E2E baseline
2026-08-25 fdbb0b7266957172852af79847a5e8edd4130568 style: restore final newline for prettier
2026-08-25 cf7f1ba4c20ce0be2ad2af36fec110c64461966b style: keep graph count assertion within formatter width
2026-08-25 23321324dae2f3562be4226e01302ea00a1e62e1 style: format large-import e2e assertion
2026-08-25 04a543c4a6822301fde34b03ae240e8d8df5d19f test: match canonical graph node count rendering
2026-08-25 71f118726c1c2a45556229876d89da64c2e9eecc test: inspect private default WebSocket capability set correctly
2026-08-25 74bba8dcaf8fb55ce67295946d9c7d929bac8c07 test: load Auto-Dig WebSocket auth contract
2026-08-25 f1890a9ab929af1cb1f31ba07cf9b8238c635d0d test: specify least-privilege Auto-Dig worker WebSocket session
2026-08-25 04b5ae2b9b50fdb4e6330dceb0ca0b936fe3947f ci: retain Playwright diagnostics while fixing baseline
2026-08-25 ad4742ab4ab35b8abcd85416176db9e41afcc305 test: clear unrelated notice before full viewport toggle
2026-08-25 40b696e08fce83cba5d636a1b29389ceff67e1da test: clear unrelated notice before graph viewport interaction
2026-08-25 fe24e24a9db623df6d27ff415cb5c49b4ba5c6c5 test: use current graph focus control
2026-08-25 ceb85b7e54d46a500f9b7c1b181e043980d5e073 test: assert formatted large-import counts
2026-08-25 c5546690d2f6d6a2a62d4d254ca1ec1da3e381ab test: target exact radial graph categories
2026-08-25 0f01529312413e47f44ad89e8cecfc235b15412e test: align application E2E with current graph layout control
2026-08-25 10f3f223ec066d6250cb0ce238802456d0ce9bf8 feat: fence Auto-Dig worker lifecycle
2026-08-25 db93ffcf838a57e2fad1c72fcfa6b0181010016b test: specify fenced Auto-Dig worker lifecycle
2026-08-25 d3e6610f1919673aec2efb58d3d191625087d897 build: load Auto-Dig control-plane lifecycle
2026-08-25 387c0e8bfd2fbd082e6ba176c3936f79dde81b5a feat: add durable Auto-Dig control-plane lifecycle
2026-08-25 15941301907063f436029e086a716720bfe26648 test: expand durable Auto-Dig lifecycle contract
2026-08-25 a640874c4004a05045fcd2732fdb0009bedb5c0c test: run Auto-Dig control contract suite
2026-08-25 c7855139ffb7d1052d2f88f61a93bbb7901ce350 test: specify typed Auto-Dig control lifecycle
2026-08-19 560208d0906cf564dd59050bca9a0f9341a3c55d Unify Quasar UI core and application shell (#40)
2026-08-17 468889de0afa27748cbba85306eda512372422d9 Merge pull request #36 from lost-rob0t/agent/issue-35-tek9-streaming
2026-08-17 528116996da1aa6359f02215e9008be3e71c594f fix: reject missing import chunk operations
2026-08-17 04699688e928a3ffc9b11f3c1ba15716e9a48816 test: load Phase 2 journal assertion fix
2026-08-17 90df9791a75ed86bf4f12df0070e18dd2eb39f34 test: fix Phase 2 journal command assertion
2026-08-17 768983759c9ed7692456c6098409e8786ba86951 test: run ten-thousand-document Phase 2 fixture
2026-08-17 700bd789abec012fe373ca3a5bd260ed32fa0d53 test: add real ten-thousand-document read fixture
2026-08-17 833834da7d70720682d99c230576096a8ddfae7a refactor: remove superseded mixed stage implementation
2026-08-17 0ef62909a13441d60777f4aa55bb67a9d2bf4ccd refactor: load clean durable stage lifecycle units
2026-08-17 dfd10d2072f72e3ce7d1a7f2fdb91dcea5aae2d6 refactor: isolate durable stage abort and expiry cleanup
2026-08-17 b409f9a5000cb7677eee1250bc198180c5bc8c53 refactor: isolate durable stage write path from promotion
2026-08-17 c7dca8963559e0e68eb06f0265926e01ba392523 test: remove superseded adversarial harness
2026-08-17 17e60f4e786c08337975b970693b2389aa25a6ee ci: guard Phase 2 bounded storage architecture
2026-08-17 6d18b070efd85729f04fca3481a0ed225886a880 test: fix durable import protocol harness declarations
2026-08-17 425b58aa0bf88dc12d3cf19a3bb4224db736a0ec test: run corrected Phase 2 adversarial matrix
2026-08-17 7294d394408a3ab646a38f27f2d09a18b6cec8e8 test: rebuild Phase 2 adversarial matrix without invalid declarations
2026-08-17 286b681cc8e9ef84020329ac1640ff87e09081ae ci: restore normal validation workflow after formatter diagnosis
2026-08-17 8f38d3544e4e238ac0ff507d7f1a6f309bf228e1 style: apply canonical Prettier output to import test
2026-08-17 d8ec1fb0fc23c4992ccf41bb2cfdc8b211230b49 style: apply canonical Prettier output
2026-08-17 54241645622eafc87ed5c2c6b7b0f8f0b60ec9a9 ci: expose canonical Prettier diff for Phase 2 files
2026-08-17 59f1dd42176a41a738b27ee3837bbf3b4a3498e1 test: run Phase 2 malformed protocol coverage
2026-08-17 4015eb5c38df526f2ed25ad0fe50462f67b3e8a9 test: fuzz durable import protocol boundaries
2026-08-17 c5c365a378dfd9be7e5dad4157a1ae2236dce3b2 style: format import sequence regression test
2026-08-17 ef14691f6b86fe28eb2939534d46447d05da8d0b style: format sequenced import mutation
2026-08-17 fb2ea97c6075f5d4fcfc1f0a831311ad8b5847e1 test: prove browser imports send stable chunk sequences
2026-08-17 f71af0936898171f959ba03f783aaaa5966ac117 feat: send explicit import chunk sequence numbers
2026-08-17 f0f96c1a130ecdecb8b0df3d7459751f5634a4c4 feat: sequence durable browser import chunks
2026-08-17 00dd0ae6025888002a090f440e3960ccf560705c test: load Phase 2 restart compatibility assertions
2026-08-17 adf3b3b704edaa8d14d3445ce05301ef958f1254 test: keep restart coverage without requiring heap-backed reads
2026-08-17 c9b4d1a917e47a9d27de01b51a36a85579418bb2 test: run Phase 2 adversarial storage matrix
2026-08-17 253919d3964e0aa5b6af5ccd2f4339d81e53ca97 test: attack Phase 2 restart atomicity and memory bounds
2026-08-17 8e2655395a92cfd60850ff14d9bb44945e32e9f0 feat: load bounded read and protocol hardening
2026-08-17 c522e2af8721de5493b28785f998cbb8185f76f5 fix: make all Tek9 snapshot and list reads bounded
2026-08-17 89a529195a8ea4def6325525cc2f4853378efcf2 feat: register durable import protocol errors
2026-08-17 d53868c39ae4d812db94cccbe41e21adb070b0dd fix: load corrected import promotion method
2026-08-17 77da6f5bf59c95a9d70e1b3a021e3338e344a80e fix: keep promotion outcome inside transaction result scope
2026-08-17 d9f9d5d0690c20eed5c92718a6d24487ca351feb refactor: remove malformed Phase 2 prototype
2026-08-17 a28318c0ae5099ab74dc130cc1d52e43dd413b81 refactor: stop loading malformed Phase 2 prototype
2026-08-17 e31f009aca011f46e97889d3ec231a3e47fe4062 refactor: isolate clean Phase 2 store core
2026-08-17 993e9eb5c60823ea11fea4cfb1c0c1a4f3ab65b6 fix: load durable stage methods at top level
2026-08-17 6e7476ccf98123d488f0d14d9c49e513d2866294 fix: hoist durable stage implementation to top level
2026-08-17 d724791ba732bd78516ae40c3c3343a190920495 fix: close bounded page iteration correctly
2026-08-17 7d7536510782963930cba163ffe909f012961536 fix: load Phase 2 restart and replay hardening
2026-08-17 66cb2f4dce1b98365b9c77a2eba9bae26ae85c80 fix: harden staged import schema cleanup and commit replay
2026-08-17 82d6324b30322b6ceedc193689e2d7b2e987a2cd fix: load bounded snapshot paging repair
2026-08-17 d4ceac1dd1b626f2edf7db125be17caaae334f46 fix: define bounded Tek9 snapshot paging at top level
2026-08-17 0098a2ff5211b3be585ea545bf377820f3ab0e61 test: remove superseded broken Phase 2 draft
2026-08-17 d90981c168b312ac4de9992d51ee80d3650d5d71 feat: load Phase 2 Tek9 storage boundary
2026-08-17 4be355cdf519f1ddcbd104d9f8cdd33522b50597 fix: keep Phase 2 handler declarations valid
2026-08-17 6624c2a6fb05befa914356d8ec8c6fed3757c6e3 feat: route durable reads and imports through Tek9
2026-08-17 37838b0e8c3404edb404e93302a1051bcb9fb986 feat: add direct revision and graph reads
2026-08-17 4074c086dd03d04a80b9ce116970a3340bfe3d21 feat: export Phase 2 store boundary
2026-08-17 4fd2d597115f97a755c362fc316aada35c77bcad test: run compilable Phase 2 red specification
2026-08-17 267f314db15e058410418a24e868f710481f6758 test: add compilable Phase 2 red storage specification
2026-08-17 8586a4b9f8aa1d1929022939567d54fab0df3e7b feat: add bounded Tek9 read and durable import primitives
2026-08-17 c6f544b47479e0b307d486f655bf03eacbdeec08 test: run Phase 2 durable storage specification
2026-08-17 fcaa14c4ec72f70317bf2632122574e034d187ef test: specify durable bounded-memory phase 2 storage
2026-08-17 3d0e1cf6dccce5e0168720598bf43298670b9988 docs: define Phase 2 Tek9 staging and read model
2026-08-17 32ecd2995916768d7f3020f2fbe1f563dc18771e Merge pull request #34 from lost-rob0t/agent/issue-33-tek9-store
2026-08-17 4894c1d5983525194ab3fecf13d2706d4f0aa3ba build: pin Quasar to merged Tek9 transaction release
2026-08-17 45de9731721bfa82e74f7d8129e9831167054359 fix: keep full-save graph cleanup inside write transaction
2026-08-17 c0d87adfccdb4bcfef94d157917ff8fe5d9eb54d test: run full-save topology cleanup regression
2026-08-17 ccad126678a76588e56bd3bf2adf6101146aea95 build: load Tek9 full-save maintenance method
2026-08-17 4ea5e957b659413cc15688456bdf53563791207f test: prove full save removes old graph topology
2026-08-17 d70cdb1317aa5b7eceb40a4952f9233d8b2ca086 fix: clear superseded graph topology on full workspace save
2026-08-17 e37f4531b247ce9c8b80ea924e449ad9cc670213 test: remove invalid DECLARE forms from adversarial fixtures
2026-08-17 244ad2e3f5757d51c4a36074578a453dd78175a3 style: remove unused persistence-plan binding
2026-08-17 29b2d0e23b08f9c42eb47a5bbc978bea657d892b test: remove invalid DECLARE forms from Tek9 fixtures
2026-08-17 94c49513e61649a9cd6b078e17623c775a3f352a test: simplify Tek9 store fixtures and fix reader error
2026-08-17 2312fc1aaa9d851e87ac93841d07cab1ce58d4c7 docs: document Tek9 runtime and dependency setup
2026-08-17 0e11a0a0d8c52fd7c732099527acc768a80a7aa1 build: guard pinned Tek9 bootstrap against CI drift
2026-08-17 c460df527c1489d86246fb0733547d6eecbf091f ci: install LMDB and bootstrap pinned Tek9
2026-08-17 af8686278c2289cc7dc2e5483413bc819a03a791 build: centralize pinned Lisp git dependencies
2026-08-17 665fb35188094e4813a30c7a5d4d0da33aeaf85a build: add LMDB native runtime to Nix shell
2026-08-17 c3f40dd1d42099065d0eeef5dfc28a8a5d767d77 build: load Tek9 from canonical Lisp test runner
2026-08-17 5a6e498ec3bd1a2c7b648367825a1371d2750845 build: load Tek9 from canonical control-plane launcher
2026-08-17 46322eedf8c0738a7cd5a440700ba646b1b27fd1 test: run Tek9 adversarial storage cases
2026-08-17 4d11f3520fcf3e2028ed6805c6e6eca016493509 test: add Tek9 deletion revision and schema adversarial cases
2026-08-17 c85b2b01ac5ed0c401a4adc8334491eab27a9724 docs: add Tek9 workspace storage ADR
2026-08-17 c134e52e291df82b0a1a37fd29ce54636c962173 docs: mark Tek9 persistence phase in UI migration ledger
2026-08-17 b9eedd5faac9b6a301e4a768e759dc347539b6c5 docs: record Tek9 as canonical local persistence
2026-08-17 e80e2e5542b8fc098795c32702808631631b28d2 feat: make production control plane own a Tek9 store
2026-08-17 24f18b50d2533112655e365e7403110a38d45cda fix: harden Tek9 range and schema restoration paths
2026-08-17 c86f2848f3c5f497d91e00dd45a92f8a0a6c60a6 fix: export workspace array helper for store adapter
2026-08-17 ff28117cb8eb8ae3252466f74c503758a976659a feat: add structured Tek9 workspace persistence
2026-08-17 145fd50308d0012d83b828ed3837977ac10dcced test: define Tek9 workspace-store invariants
```

## Repository paths changed, last 14 days

```text
.github/workflows/ci.yml
.github/workflows/ui-overhaul-format.yml
README.md
control-plane/src/autodig-control.lisp
control-plane/src/autodig-persistence-bridge.lisp
control-plane/src/autodig-principal-isolation.lisp
control-plane/src/autodig-store.lisp
control-plane/src/autodig-websocket-session.lisp
control-plane/src/command-authority-context.lisp
control-plane/src/config.lisp
control-plane/src/configured-main.lisp
control-plane/src/debug-logging.lisp
control-plane/src/main.lisp
control-plane/src/packages.lisp
control-plane/src/persistence-plan.lisp
control-plane/src/phase2-control-plane.lisp
control-plane/src/phase2-hardening.lisp
control-plane/src/phase2-promotion.lisp
control-plane/src/phase2-protocol.lisp
control-plane/src/phase2-read-hardening.lisp
control-plane/src/phase2-stage-cleanup.lisp
control-plane/src/phase2-stage-write.lisp
control-plane/src/phase2-stage.lisp
control-plane/src/phase2-store-core.lisp
control-plane/src/phase2-store-page-fix.lisp
control-plane/src/phase2-store-reads.lisp
control-plane/src/phase2-store.lisp
control-plane/src/store-maintenance.lisp
control-plane/src/store.lisp
control-plane/src/websocket-server.lisp
control-plane/tests/autodig-control-tests.lisp
control-plane/tests/autodig-persistence-adversarial-tests.lisp
control-plane/tests/autodig-persistence-tests.lisp
control-plane/tests/autodig-principal-isolation-tests.lisp
control-plane/tests/autodig-websocket-auth-tests.lisp
control-plane/tests/autodig-worker-reclaim-tests.lisp
control-plane/tests/phase2-adversarial-tests.lisp
control-plane/tests/phase2-adversarial-v2-regression-fix.lisp
control-plane/tests/phase2-adversarial-v2.lisp
control-plane/tests/phase2-large-corpus-tests.lisp
control-plane/tests/phase2-protocol-tests.lisp
control-plane/tests/phase2-storage-spec-tests.lisp
control-plane/tests/phase2-storage-tests.lisp
control-plane/tests/phase2-test-compat.lisp
control-plane/tests/tek9-store-adversarial-tests.lisp
control-plane/tests/tek9-store-maintenance-tests.lisp
control-plane/tests/tek9-store-tests.lisp
docs/ADR-TEK9-WORKSPACE-STORAGE.md
docs/ARCHITECTURE.md
docs/CONFIGURATION.md
docs/UI-CORE.md
docs/UI-MIGRATION.md
example_configs/init.lisp
flake.nix
frontend/e2e/application.spec.ts
frontend/e2e/dataset-picker.spec.ts
frontend/e2e/graph-controls.spec.ts
frontend/e2e/graph-fullscreen.spec.ts
frontend/e2e/graph-viewport.spec.ts
frontend/e2e/large-import.spec.ts
frontend/e2e/mobile-fit-agent-disclosure.spec.ts
frontend/e2e/mobile-navigation.spec.ts
frontend/e2e/ui-consistency.spec.ts
frontend/src/App.jsx
frontend/src/app/main.tsx
frontend/src/components/AgentDisclosureBridge.jsx
frontend/src/components/DatasetsPage.jsx
frontend/src/components/MobileGestureMenu.jsx
frontend/src/components/MobileGraphToolTray.jsx
frontend/src/control-plane/client.ts
frontend/src/control-plane/mutations.ts
frontend/src/ui-core/QuasarShell.jsx
frontend/src/ui-core/StatusCenter.jsx
frontend/src/ui-core/adapters/auto-dig.js
frontend/src/ui-core/adapters/control-plane.js
frontend/src/ui-core/adapters/index.js
frontend/src/ui-core/adapters/shared.js
frontend/src/ui-core/adapters/standalone.js
frontend/src/ui-core/graph.css
frontend/src/ui-core/navigation.jsx
frontend/src/ui-core/responsive.css
frontend/src/ui-core/runtime.jsx
frontend/src/ui-core/shell.css
frontend/src/ui-core/surfaces.css
frontend/tests/unit/control-plane-import-sequence.test.ts
scripts/bootstrap-lisp-deps
scripts/check-control-plane-deps.mjs
scripts/check-native-runtime.mjs
scripts/dev.mjs
scripts/run-control-plane
scripts/run-production
scripts/smoke-production.mjs
scripts/smoke-startup.mjs
scripts/test-lisp
systems/quasar-control.asd
systems/quasar-tests.asd
systems/quasar-web.asd
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/ci.yml
.github/workflows/ui-overhaul-format.yml
control-plane/tests/autodig-control-tests.lisp
control-plane/tests/autodig-persistence-adversarial-tests.lisp
control-plane/tests/autodig-persistence-tests.lisp
control-plane/tests/autodig-principal-isolation-tests.lisp
control-plane/tests/autodig-websocket-auth-tests.lisp
control-plane/tests/autodig-worker-reclaim-tests.lisp
control-plane/tests/phase2-adversarial-tests.lisp
control-plane/tests/phase2-adversarial-v2-regression-fix.lisp
control-plane/tests/phase2-adversarial-v2.lisp
control-plane/tests/phase2-large-corpus-tests.lisp
control-plane/tests/phase2-protocol-tests.lisp
control-plane/tests/phase2-storage-spec-tests.lisp
control-plane/tests/phase2-storage-tests.lisp
control-plane/tests/phase2-test-compat.lisp
control-plane/tests/tek9-store-adversarial-tests.lisp
control-plane/tests/tek9-store-maintenance-tests.lisp
control-plane/tests/tek9-store-tests.lisp
flake.nix
frontend/tests/unit/control-plane-import-sequence.test.ts
scripts/bootstrap-lisp-deps
scripts/check-control-plane-deps.mjs
scripts/check-native-runtime.mjs
scripts/dev.mjs
scripts/run-control-plane
scripts/run-production
scripts/smoke-production.mjs
scripts/smoke-startup.mjs
scripts/test-lisp
systems/quasar-control.asd
systems/quasar-tests.asd
systems/quasar-web.asd
```
