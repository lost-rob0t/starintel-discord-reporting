# lost-rob0t/star-lang

- generated: `2026-09-16T21:22:15Z`
- canonical branch: `main`
- changelog eligible: `yes`
- head: [`d320172e42ddc4448da0334fc67c8b7bd6a001e5`](https://github.com/lost-rob0t/star-lang/commit/d320172e42ddc4448da0334fc67c8b7bd6a001e5)
- head date: `2026-09-16T06:58:39-04:00`
- head subject: Merge pull request #106 from lost-rob0t/impl5/80-actor-option-keys

## Git log, last 14 days

```text
2026-09-16 d320172e42ddc4448da0334fc67c8b7bd6a001e5 Merge pull request #106 from lost-rob0t/impl5/80-actor-option-keys
2026-09-16 2c9d4bb2cf9ff57b1c6b5103df6a4276247a4bbf Merge main into impl5/80-actor-option-keys
2026-09-16 7799dcac1edabd281f6ba2f198c7d3f5d5d653c9 process: harden supervised lifecycle port (#101)
2026-09-16 06072bd1438b410c6312f6c72249d59d9c423362 Merge main into impl5/80-actor-option-keys
2026-09-16 ac1d2cfe78e77bed5f44e4d1dc2ec2ea461e7698 http: extract and harden Dexador backend (#100)
2026-09-16 9d627d50552ea037511e04dcc4d89619f8305dc3 Merge current main into impl/70-dexador-backend
2026-09-16 7638658b28ccb97babadb228bf9f35a7592a3104 compiler: preserve existing actor diagnostic phase outside option errors
2026-09-16 fd3f1be80523e7e9d6d0c30f7386aaaa6511c024 compiler: validate actor option keys before lowering
2026-09-16 b1972dd26f255e2e0fad1431b8f9d5d798757f2f test: make actor option diagnostics assertions executable
2026-09-16 97604f583cb295b463521c1b2073202390af2f26 test: run actor option key regressions
2026-09-16 c21050c4085c28d0f7a1ad756f5986d987565caf test: add actor option key closure regressions
2026-09-16 06a4d0af55100a936cf918144afbd7406481f35f runtime: enforce raw actor instance ownership (#105)
2026-09-16 2068f70b5c5949e7f5a5d2a98220e31e7f67d566 compiler: close field-marker grammar (#94)
2026-09-16 bd3d40088e83c4b0d616ffdd3fb42a23a79151b5 fix(runtime): enforce raw actor instance ownership
2026-09-16 992edff151f83f65ced66c1c4d479a3344d6f298 Merge current main into #90 field-marker branch
2026-09-16 dde8eaf9da68124799d769bc9aa492d93edd436e test(runtime): run ownership regressions
2026-09-16 0f306f68676c243c529404224e108dab4dd4e017 test(runtime): expose raw actor ownership violations
2026-09-16 65ee3474a8ce4fb1ee1e12d08b36acd230507e85 process: distinguish forced capture truncation
2026-09-16 7a5d275b9e1031186f621ee52f6974f7cc7c68b2 process: treat forced capture stop as truncation
2026-09-16 b153e18ae142793f077e53a4aedbdd11b0861242 docs(process): document bounded inherited-pipe cleanup
2026-09-16 ba8a0b275ad3c36c02a5046e62d4857e8b1146ec process: bound capture cleanup after root reap
2026-09-16 5ee19da9a1848f187d0b0f7c080b04d60db3d5f6 process: add bounded capture thread controls
2026-09-16 c4a25807dc78ba420a45812f5202c65487562941 test(process): isolate inherited-pipe watchdog red
2026-09-16 d5be573fa06f715dcb98745d483c7923fa99b911 test(process): reproduce inherited pipe hang
2026-09-16 b675d3000c1f932097ceb780806898bd43cc0f56 test(process): add inherited-pipe fixture modes
2026-09-16 f2f606f34adabc27edff671b8433555da0eb7d85 compiler: reject malformed actor capabilities (#98)
2026-09-16 01f43f7bdeda98602a753cc636a1f7812fb7d68f test(http): retire ownership RED runner
2026-09-16 0827fcaa1d1e5224c2ebaf5642c18da6a3551a66 test(http): enable full Dexador ownership suite
2026-09-16 23f79c0e3dca3f0ca0e29886d77bb64075da3627 docs(http): document Dexador resource and body ownership
2026-09-16 8d6809e7fbad8b3a95ea40289c6745226afb9c1e fix(http): make Dexador policy client-local
2026-09-16 3ff7403558653cd484375ad1394eeab1edfca8ba runtime: fence stale in-flight completion (#99)
2026-09-16 76617ec07178d2e4b8ae3a457bf4e2e910b91740 test(http): execute ownership RED runner
2026-09-16 49305897f47563f47230ceee439f7c5042a95688 test(http): isolate non-hanging ownership RED cases
2026-09-16 9a666bc9ed08dc99ba393b89b4903c9cf61c21ef test(http): complete ownership RED harness
2026-09-16 ffd822f929a014a72ae93d83b93496d75c90652d test(http): fix ownership regression harness syntax
2026-09-16 8a32445b3f3d83e1404914d9bfd8379a722c7ac4 test(http): run Dexador ownership regressions
2026-09-16 b801b4be8898c6015b472ac56774c023a5180da2 test(http): expose Dexador ownership policy gaps
2026-09-16 b6c4ffee51c3ca5d21bc3efb128ee38e3c72e499 Merge main into #90 field-marker branch
2026-09-16 fa1766bf4d5541acfc5f820332298abca13ca9cb Merge current main into #76 completion-fence branch
2026-09-16 d377bb7e15dd62990f3dc301c9df1b37a677b878 feat(process): add bounded supervised lifecycle
2026-09-16 174e79a9f4f0624c6d316f5250318f27dc6c3d38 Merge main into #79 capability hardening
2026-09-16 e880f1be195bea7906bd356ae0b5f827a26c35e0 test(process): prove launch failures redact argv
2026-09-16 5edee211805f5fd32d5964b674d17259368941a6 Merge pull request #92 from lost-rob0t/impl4/81-journal-owned-values
2026-09-16 ed6c4130e068a8e3bd28242aa198cd5e54170e31 Merge pull request #96 from lost-rob0t/impl/85-wire-handler-failure-settlement
2026-09-16 879aa130031cec34b6a0f1614b163b885195e67f Merge pull request #68 from lost-rob0t/fix/final-macro-expander
2026-09-16 78ffc0eb2e0139514c72be25d2b0748a96c6c7c2 test: distinguish mapper semantics from connect timing
2026-09-16 05b685015fffcf091bd207b096361732dc2e1f12 http: classify SBCL stream timeouts as transport timeouts
2026-09-16 bad36215bc69fb6af65523731854b73405d44036 test: extend Dexador real-loopback acceptance coverage
2026-09-16 39c9bbfb135ae4fdfc0ed01baf5eb4262678a234 docs: record HTTP backend ownership matrix
2026-09-16 d3e72d9cc492e8750b5a5fd25b90fba6ae67dff2 http: prove the base port loads without Dexador
2026-09-16 ea9828792dc22d2cb26a3aabbfd868ad013f4752 http: point regressions at extracted backend and typed failures
2026-09-16 ec0b143d2b50794df1d3487cb0ba4614d5213d12 http: test the concrete Dexador system directly
2026-09-16 ed3a8072ec87003b8fd1fabf378a0c725dd64c22 http: move Dexador request execution into concrete backend
2026-09-16 21be44e6148a44f59f56b5a382d2acf40d7cff91 http: define Dexador backend package boundary
2026-09-16 8885a827d106cf1fd68cca557d4e16d5186962d8 http: add first-class Dexador backend system
2026-09-16 87c64dcb457a43b9b72d449140a35e195ca399f0 http: document backend-neutral port ownership
2026-09-16 30681ce55a78f47f20be3a147174c49bc7ce0639 http: remove concrete Dexador ownership from base port
2026-09-16 a40175b745c0c4c37f7efb5b1a165860f5e378af http: make port package backend-neutral
2026-09-16 c63d9dc1f774f38b1c08a66ea0cae089f08e3924 ci: retain flake-check failure diagnostics for #70
2026-09-16 af64882eb69499c9ec119c0e92f67582660b9894 fix(runtime): fence completion across actor re-registration
2026-09-16 d3721583942ce8cc8fe8fea2fb8d7147650eda16 test(runtime): expose unregister reregister completion ABA
2026-09-16 faa59def6a2735edb02fd256381025ef89fe0ce7 compiler: allow required fields with explicit defaults
2026-09-16 1e563dc961880d42bb209769b2c09c08cc5741e0 test(http): capture Dexador response/redaction regressions
2026-09-16 dbdb14f843129747f53f3d42abf28a2f76e91c7f test: cover required field defaults
2026-09-16 848e5179c86daee176e0412f1c51e12dfa46ae2f test: reconcile guard fixtures with stale completion
2026-09-16 d28dba4609c77163e59f4167c0ea404bc5136493 test: run stale completion acceptance suite
2026-09-16 56f745803f977955afac19f0e200d1602b9e3630 test: cover stale lifecycle completion boundaries
2026-09-16 6764507f6151459afdc3783789d32f15a84bbd2a runtime: fence stale dispatch completion
2026-09-16 9d44b697953d949c077d9ab6ca83ff8ed55120b0 runtime: expose stale completion condition
2026-09-16 f4cd07f38a4db4773a23037f64b1ccb8c8c3f7db test: expose stale completion after restart
2026-09-16 e204a3734c4190e373ac8ba65ff48ac708b00662 compiler: fail closed on malformed actor capabilities
2026-09-16 bcf0a318667d269ff24d8c3c4270b8bee8b7a13d docs: record stack-bounded list snapshots
2026-09-16 52bb433c18a037246c38c42bc9cfa4ebd699ff10 fix: bound proper-list snapshot stack use
2026-09-16 a9d409e23397d400055cffc5278efff721276d0f test: fix actor capability regression form
2026-09-16 1d888258a9f0641a30105e1efb6a7e4c0b9ab9f8 test: cover stack-bounded flat snapshots
2026-09-16 3ebb49f778e4e1ed00b257c6ac0c65928acb5488 test: run actor capability regressions
2026-09-16 437252a277e74cb963dd0980a357372314cb84a1 test: cover actor capability validation
2026-09-16 169f2a4d85a6c4b120b6107cf8325f8d11803ab9 runtime: bound handler failure settlement diagnostics
2026-09-16 5fbe9c21ea9646c7e7905bac79747891825400e2 test: expose unsafe handler failure reporting
2026-09-16 2655315d5b677607814936c5c37cc21b27693687 canonical-json: preserve typed explicit field defaults (#95)
2026-09-15 123ebf719d431b48497fd0b5bf89d892cc43dfde runtime: preserve active dispatch guard on repeated start (#93)
2026-09-15 b650ebbc25483f2b90406e14397af2705c162aa0 chore: remove collateral field-marker diff
2026-09-15 c7a25007b01ec58c336c3f2bba84cf5505ae4d11 Retire duplicate prototype macro test suite
2026-09-15 7c1b5e39eac288b190bc771f9f647f252bd0c161 Make prototype core shell recognize final macro owner
2026-09-15 999f86a5efddcd1528a706aeb810032af5c46945 docs: define snapshot aggregate and structural bounds (#81)
2026-09-15 bba803ce34458cabdadde539e441286840087c40 fix: bound snapshot depth and alias amplification (#81)
2026-09-15 98a816c88fdb2964e60804a6a577d8727a620dd3 Reconcile macro final ownership with migration ledger
2026-09-15 ca88063781c44a90a2f637cf3374eedfebd160e9 Stop loading macro compatibility shell through prototype ASDF
2026-09-15 b255eb83fa99c39e7f22e8a60bc9028644b123d6 test: reproduce shallow journal replay depth failure (#81)
2026-09-15 02a18fa7f3f5e632e8ffe5f495d8642a0bb37cbd test: expose snapshot depth and amplification regressions (#81)
2026-09-15 be7395d5868a461d0729fd4f36a87b1a1d9b78cc runtime: settle accepted handler failures terminally
2026-09-15 f3172dc4bafe0628bfff45eb5993ff6bac04a50e test: cover wire failure settlement lifecycle matrix
2026-09-15 eebbb9af1cbb0a1e5659754dbc11bace0a7b2a5f test: wire failure settlement regression is part of runtime gate
2026-09-15 fa34f1a36c9a29b3f3bcc82b97b1e97c0141f4d5 test: prove wire handler failure wedges idempotency record
2026-09-15 56279098493c862b38c9febb104af1b15bb00b07 test: fix field marker span assertion
2026-09-15 299d0aa35449c3e966653cc905af5066a75db646 fix: parse field markers as closed grammar
2026-09-15 b86ff42c61edea55ec1444e5b853fd1695496232 test: run field marker grammar regression
2026-09-15 2e3c6a4c2e422a667bb6efaa94b88724771773c2 test: expose open field marker grammar
2026-09-15 5a1286e708c0fd962eb9bdf29d1d2273265955cc docs: record journal value ownership and bounds (#81)
2026-09-15 79fba95c74ef39d5bba8df414385616fc6cb1bda journal: snapshot before validating owned append data (#81)
2026-09-15 e5505b918a2d246804c833ff9c348e8815dabe41 test: run journal ownership boundary regressions (#81)
2026-09-15 e46b65475196d4846dec892a2f1dbd4ec8496c26 test: bound journal value ownership failures (#81)
2026-09-15 7d89259ec63b64b6df43e25e226b7e58d889b344 journal: snapshot values at ownership boundaries (#81)
2026-09-15 f8f69e2bf6f2c18114ca79e03dd1bcd20839dd00 test: run portable snapshot conformance (#81)
2026-09-15 cb42f7d872f9336b5bc8244d3d36408704ba73bf test: cover bounded portable wire snapshots (#81)
2026-09-15 7d99207815f1b9626bc52838adca880a0aabedfd protocol: load portable snapshot in final system (#81)
2026-09-15 c0f1a91395161d3c4696bfccdd2a6aeb9c6d181c protocol: add bounded portable wire snapshot (#81)
2026-09-15 4868bf3c0091f164e72b751e849607a1eacb73f7 protocol: export bounded portable wire snapshot (#81)
2026-09-15 dd1860a30360346da09c2db1d5fe66c65651db55 test: expose journal mutable-value aliasing (#81)
2026-09-14 7db89986450d4e513ff4b5c9617bf4d196b3cfb4 Merge branch 'main' of github.com:lost-rob0t/star-lang (PR #65/#66 KB promotions)
2026-09-14 de3b3335ddb14cc54632ae1a79ddf6259c93c84c docs: record macro expander final-system migration
2026-09-14 5f3e3470bac11199a975c0ecb6d356912d343eab kb: record final macro-expander authority
2026-09-14 e6b1f2ebfb136a57abe9909861c6e8ace49477d9 docs: record final macro-expander ownership
2026-09-14 51160c8f0351e9ca76fb88cb4b2a817efb27d3bf migration: mark macro expander final-owned
2026-09-14 793ccb4962de977506b9975a5d0f8fd0a898a194 test: add final macro expander suite to compiler gate
2026-09-14 cf7a779cbaef08ce2f53b27bc1ba98fc3e97e6c9 test: prove final compiler owns macro expansion
2026-09-14 69a246f1d5163ce62c900c73f71dc8b72784a279 prototype: reduce macro expander to final-system compatibility shell
2026-09-14 7211ee3eac25da2f565452d65a0bbe37e8c1acfe compiler: expose final macro expansion API
2026-09-14 9c9f83181aafcaf702b5b0535aca5492340c4a71 compiler: extract declarative macro expander into final system
2026-09-14 b1ef1a947655b34aabeea26400c1bf1d1c063419 compiler: load final macro expander from starlang-compiler
2026-09-14 f701583aa7ab6132967742e73c3309aea0b2d6b6 cli: add first-class final-system starlang-cli command surface (#66)
2026-09-14 9238112c16546673bcef6e4a41b8f0f91ce7ef56 prototype: register repository tree first in the ASDF source registry (#65)
2026-09-11 b4d25ad4be855285ae6e38aa07dfc764b7a4330e cli: add first-class final-system starlang-cli command surface
2026-09-11 a3c42bfec77fc3b82e3d8fee79a3730166f1a2f3 prototype: register repository tree first in the ASDF source registry
2026-09-10 0343d653e14bcc96eea02dd63b956aa3867ebc15 compiler: extract closed parser and actor lowering from prototype (#64)
2026-09-10 87b4628edd66fd97708396fb333c7090edf76a9e cleanup: remove IPX application code from StarLang (#63)
2026-09-10 7d800f9267d1d2b860f0a8ea460b3ec7e3bb9f9a artifact: add canonical JSON file writer actor (#44)
2026-09-10 08fb157b5209a8f9fe7a38dd28023ab4dbe39417 ci: expose supported Linux StarLang Hydra jobs (#60)
2026-09-10 160663ac2ec48b549fc58f76ab7f3cb775a4aad6 compiler: start final extraction and production-readiness gate (#48)
2026-09-10 6d6486fc9330fb45434ca3c07332f0206428bc4b logic: add SWI-Prolog MQI worker adapter (#46)
2026-09-10 35e26d74f307604adf04c3eb76018944a1973d3e ipx: add lossless actor pipeline foundation (#55)
2026-09-10 d48d3e41900c92f2dba184554d7eccaa1bd0d3fa runtime: complete concrete Sento boundary and real actor tests (#43)
```

## Repository paths changed, last 14 days

```text
.github/workflows/artifact.yml
.github/workflows/ci.yml
.github/workflows/logic-swi.yml
.github/workflows/nix.yml
.github/workflows/production-readiness.yml
.prolog/kb/cli-surface.pl
.prolog/kb/compiler-ownership.pl
.prolog/kb/load.pl
.prolog/kb/testing.pl
.prolog/kb/toolchain.pl
.prolog/kb/verification-workflow.pl
AGENTS.md
CHANGELOG.md
README.md
ci/check-prototype-migration.sh
ci/check-repository-contracts.sh
ci/check-swi-adapter-contracts.sh
ci/prototype-migration.tsv
ci/run-real-sento-remoting-smoke.sh
ci/target-systems.txt
ci/with-nix-sbcl.sh
docs/PRODUCTION-READINESS.md
docs/implementation-slices/ACTOR-RUNTIME-MIGRATION-MATRIX.md
docs/implementation-slices/FINAL-RUNTIME-OWNERSHIP-ACTORS-INGEST.md
docs/implementation-slices/REAL-ACTOR-SYSTEM-TEST-INVARIANT.md
fixtures/actor-compiler/enrichment-worker.star
flake.lock
flake.nix
nix/sento-remoting.nix
prototype/actor-wire-prototype.lisp
prototype/bbp-domain-remoting-tests.lisp
prototype/cl-gserver-runtime-facade-prototype.lisp
prototype/core-surface-load-tests.lisp
prototype/core-surface-prototype.lisp
prototype/macro-expander-prototype.lisp
prototype/macro-expander-tests.lisp
prototype/message-lifecycle-bindings-prototype.lisp
prototype/message-lifecycle-tests.lisp
prototype/resolver-effect-ports-prototype.lisp
prototype/sento-remoting-domain-adapter.lisp
prototype/service-uri-prototype.lisp
star-actor-protocol/src/packages.lisp
star-actor-protocol/src/portable-snapshot.lisp
star-actor-protocol/star-actor-protocol.asd
star-actor-protocol/tests/portable-snapshot-tests.lisp
star-actor-protocol/tests/star-actor-protocol-tests.asd
star-artifact/src/json-file-output.lisp
star-artifact/src/packages.lisp
star-artifact/star-artifact.asd
star-artifact/tests/star-artifact-tests.lisp
star-canonical-json/src/starlang-wire-json.lisp
star-canonical-json/tests/starlang-wire-json-tests.lisp
star-http-dexador/src/dexador-client.lisp
star-http-dexador/src/packages.lisp
star-http-dexador/star-http-dexador.asd
star-http-dexador/tests/star-http-dexador-ownership-tests.lisp
star-http-dexador/tests/star-http-dexador-red-runner.lisp
star-http-dexador/tests/star-http-dexador-tests.asd
star-http-dexador/tests/star-http-dexador-tests.lisp
star-http-port/README.md
star-http-port/src/http-port.lisp
star-http-port/src/packages.lisp
star-http-port/star-http-port.asd
star-http-port/tests/star-http-port-tests.lisp
star-ipx/src/ipx.lisp
star-ipx/src/packages.lisp
star-ipx/star-ipx.asd
star-ipx/tests/star-ipx-tests.asd
star-ipx/tests/star-ipx-tests.lisp
star-journal/README.md
star-journal/src/journal.lisp
star-journal/tests/journal-boundary-tests.lisp
star-journal/tests/star-journal-tests.asd
star-journal/tests/star-journal-tests.lisp
star-logic-adapter-swi/README.md
star-logic-adapter-swi/prolog/star_logic_bootstrap.pl
star-logic-adapter-swi/src/adapter.lisp
star-logic-adapter-swi/src/bootstrap.lisp
star-logic-adapter-swi/src/conditions.lisp
star-logic-adapter-swi/src/identity.lisp
star-logic-adapter-swi/src/mqi-codec.lisp
star-logic-adapter-swi/src/packages.lisp
star-logic-adapter-swi/src/worker.lisp
star-logic-adapter-swi/star-logic-adapter-swi.asd
star-logic-adapter-swi/tests/codec-tests.lisp
star-logic-adapter-swi/tests/integration-tests.lisp
star-logic-adapter-swi/tests/star-logic-adapter-swi-integration-tests.asd
star-logic-adapter-swi/tests/star-logic-adapter-swi-tests.asd
star-logic-adapter-swi/tests/worker-tests.lisp
star-process-port/README.md
star-process-port/src/packages.lisp
star-process-port/src/process.lisp
star-process-port/star-process-port.asd
star-process-port/tests/fixtures/process-fixture.sh
star-process-port/tests/star-process-port-tests.asd
star-process-port/tests/star-process-port-tests.lisp
star-sento-compat/src/packages.lisp
star-sento-compat/src/runtime-port.lisp
star-sento-compat/src/sento-adapter.lisp
star-sento-compat/tests/integration/harness.lisp
star-sento-compat/tests/integration/packages.lisp
star-sento-compat/tests/integration/real-actor-system-tests.lisp
star-sento-compat/tests/star-sento-compat-integration-tests.asd
star-sento-compat/tests/star-sento-compat-tests.lisp
starlang-cli/src/cli.lisp
starlang-cli/src/packages.lisp
starlang-cli/starlang-cli.asd
starlang-cli/starlang-cli.lisp
starlang-cli/tests/cli-proof.lisp
starlang-cli/tests/cli-tests.lisp
starlang-cli/tests/fixtures/actor-unknown-option.star
starlang-cli/tests/starlang-cli-tests.asd
starlang-compiler/src/actor-ir.lisp
starlang-compiler/src/actor-manifest.lisp
starlang-compiler/src/actor-source.lisp
starlang-compiler/src/core-surface.lisp
starlang-compiler/src/lifecycle-bindings.lisp
starlang-compiler/src/macro-expander.lisp
starlang-compiler/src/packages.lisp
starlang-compiler/src/public-surface.lisp
starlang-compiler/src/resolver-effects.lisp
starlang-compiler/starlang-compiler.asd
starlang-compiler/tests/actor-capabilities-tests.lisp
starlang-compiler/tests/actor-compiler-proof.lisp
starlang-compiler/tests/actor-compiler-tests.lisp
starlang-compiler/tests/actor-option-key-tests.lisp
starlang-compiler/tests/field-marker-tests.lisp
starlang-compiler/tests/macro-expander-tests.lisp
starlang-compiler/tests/starlang-compiler-tests.asd
starlang-compiler/tests/starlang-compiler-tests.lisp
starlang-prototype.asd
starlang-runtime/src/packages.lisp
starlang-runtime/src/runtime.lisp
starlang-runtime/src/wire-dispatcher.lisp
starlang-runtime/tests/runtime-ownership-tests.lisp
starlang-runtime/tests/stale-completion-tests.lisp
starlang-runtime/tests/starlang-runtime-tests.asd
starlang-runtime/tests/starlang-runtime-tests.lisp
starlang-runtime/tests/wire-dispatcher-failure-settlement-tests.lisp
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/artifact.yml
.github/workflows/ci.yml
.github/workflows/logic-swi.yml
.github/workflows/nix.yml
.github/workflows/production-readiness.yml
ci/check-prototype-migration.sh
ci/check-repository-contracts.sh
ci/check-swi-adapter-contracts.sh
ci/prototype-migration.tsv
ci/run-real-sento-remoting-smoke.sh
ci/target-systems.txt
ci/with-nix-sbcl.sh
flake.nix
star-actor-protocol/star-actor-protocol.asd
star-actor-protocol/tests/portable-snapshot-tests.lisp
star-actor-protocol/tests/star-actor-protocol-tests.asd
star-artifact/star-artifact.asd
star-artifact/tests/star-artifact-tests.lisp
star-canonical-json/tests/starlang-wire-json-tests.lisp
star-http-dexador/star-http-dexador.asd
star-http-dexador/tests/star-http-dexador-ownership-tests.lisp
star-http-dexador/tests/star-http-dexador-red-runner.lisp
star-http-dexador/tests/star-http-dexador-tests.asd
star-http-dexador/tests/star-http-dexador-tests.lisp
star-http-port/star-http-port.asd
star-http-port/tests/star-http-port-tests.lisp
star-ipx/star-ipx.asd
star-ipx/tests/star-ipx-tests.asd
star-ipx/tests/star-ipx-tests.lisp
star-journal/tests/journal-boundary-tests.lisp
star-journal/tests/star-journal-tests.asd
star-journal/tests/star-journal-tests.lisp
star-logic-adapter-swi/star-logic-adapter-swi.asd
star-logic-adapter-swi/tests/codec-tests.lisp
star-logic-adapter-swi/tests/integration-tests.lisp
star-logic-adapter-swi/tests/star-logic-adapter-swi-integration-tests.asd
star-logic-adapter-swi/tests/star-logic-adapter-swi-tests.asd
star-logic-adapter-swi/tests/worker-tests.lisp
star-process-port/star-process-port.asd
star-process-port/tests/fixtures/process-fixture.sh
star-process-port/tests/star-process-port-tests.asd
star-process-port/tests/star-process-port-tests.lisp
star-sento-compat/tests/integration/harness.lisp
star-sento-compat/tests/integration/packages.lisp
star-sento-compat/tests/integration/real-actor-system-tests.lisp
star-sento-compat/tests/star-sento-compat-integration-tests.asd
star-sento-compat/tests/star-sento-compat-tests.lisp
starlang-cli/starlang-cli.asd
starlang-cli/tests/cli-proof.lisp
starlang-cli/tests/cli-tests.lisp
starlang-cli/tests/fixtures/actor-unknown-option.star
starlang-cli/tests/starlang-cli-tests.asd
starlang-compiler/starlang-compiler.asd
starlang-compiler/tests/actor-capabilities-tests.lisp
starlang-compiler/tests/actor-compiler-proof.lisp
starlang-compiler/tests/actor-compiler-tests.lisp
starlang-compiler/tests/actor-option-key-tests.lisp
starlang-compiler/tests/field-marker-tests.lisp
starlang-compiler/tests/macro-expander-tests.lisp
starlang-compiler/tests/starlang-compiler-tests.asd
starlang-compiler/tests/starlang-compiler-tests.lisp
starlang-prototype.asd
starlang-runtime/tests/runtime-ownership-tests.lisp
starlang-runtime/tests/stale-completion-tests.lisp
starlang-runtime/tests/starlang-runtime-tests.asd
starlang-runtime/tests/starlang-runtime-tests.lisp
starlang-runtime/tests/wire-dispatcher-failure-settlement-tests.lisp
```
