# lost-rob0t/star-lang

- generated: `2026-09-16T07:43:45Z`
- canonical branch: `main`
- changelog eligible: `yes`
- head: [`f2f606f34adabc27edff671b8433555da0eb7d85`](https://github.com/lost-rob0t/star-lang/commit/f2f606f34adabc27edff671b8433555da0eb7d85)
- head date: `2026-09-16T03:01:54-04:00`
- head subject: compiler: reject malformed actor capabilities (#98)

## Git log, last 14 days

```text
2026-09-16 f2f606f34adabc27edff671b8433555da0eb7d85 compiler: reject malformed actor capabilities (#98)
2026-09-16 3ff7403558653cd484375ad1394eeab1edfca8ba runtime: fence stale in-flight completion (#99)
2026-09-16 fa1766bf4d5541acfc5f820332298abca13ca9cb Merge current main into #76 completion-fence branch
2026-09-16 174e79a9f4f0624c6d316f5250318f27dc6c3d38 Merge main into #79 capability hardening
2026-09-16 5edee211805f5fd32d5964b674d17259368941a6 Merge pull request #92 from lost-rob0t/impl4/81-journal-owned-values
2026-09-16 ed6c4130e068a8e3bd28242aa198cd5e54170e31 Merge pull request #96 from lost-rob0t/impl/85-wire-handler-failure-settlement
2026-09-16 879aa130031cec34b6a0f1614b163b885195e67f Merge pull request #68 from lost-rob0t/fix/final-macro-expander
2026-09-16 af64882eb69499c9ec119c0e92f67582660b9894 fix(runtime): fence completion across actor re-registration
2026-09-16 d3721583942ce8cc8fe8fea2fb8d7147650eda16 test(runtime): expose unregister reregister completion ABA
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
star-process-port/src/packages.lisp
star-process-port/src/process.lisp
star-process-port/star-process-port.asd
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
starlang-compiler/tests/macro-expander-tests.lisp
starlang-compiler/tests/starlang-compiler-tests.asd
starlang-compiler/tests/starlang-compiler-tests.lisp
starlang-prototype.asd
starlang-runtime/src/packages.lisp
starlang-runtime/src/runtime.lisp
starlang-runtime/src/wire-dispatcher.lisp
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
starlang-compiler/tests/macro-expander-tests.lisp
starlang-compiler/tests/starlang-compiler-tests.asd
starlang-compiler/tests/starlang-compiler-tests.lisp
starlang-prototype.asd
starlang-runtime/tests/stale-completion-tests.lisp
starlang-runtime/tests/starlang-runtime-tests.asd
starlang-runtime/tests/starlang-runtime-tests.lisp
starlang-runtime/tests/wire-dispatcher-failure-settlement-tests.lisp
```
