# lost-rob0t/star-lang

- generated: `2026-09-14T00:14:30Z`
- canonical branch: `main`
- changelog eligible: `yes`
- head: [`0343d653e14bcc96eea02dd63b956aa3867ebc15`](https://github.com/lost-rob0t/star-lang/commit/0343d653e14bcc96eea02dd63b956aa3867ebc15)
- head date: `2026-09-10T22:22:55-04:00`
- head subject: compiler: extract closed parser and actor lowering from prototype (#64)

## Git log, last 14 days

```text
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
prototype/core-surface-prototype.lisp
prototype/message-lifecycle-bindings-prototype.lisp
prototype/message-lifecycle-tests.lisp
prototype/resolver-effect-ports-prototype.lisp
prototype/sento-remoting-domain-adapter.lisp
prototype/service-uri-prototype.lisp
star-artifact/src/json-file-output.lisp
star-artifact/src/packages.lisp
star-artifact/star-artifact.asd
star-artifact/tests/star-artifact-tests.lisp
star-ipx/src/ipx.lisp
star-ipx/src/packages.lisp
star-ipx/star-ipx.asd
star-ipx/tests/star-ipx-tests.asd
star-ipx/tests/star-ipx-tests.lisp
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
starlang-compiler/src/actor-ir.lisp
starlang-compiler/src/actor-manifest.lisp
starlang-compiler/src/actor-source.lisp
starlang-compiler/src/core-surface.lisp
starlang-compiler/src/lifecycle-bindings.lisp
starlang-compiler/src/packages.lisp
starlang-compiler/src/public-surface.lisp
starlang-compiler/src/resolver-effects.lisp
starlang-compiler/starlang-compiler.asd
starlang-compiler/tests/actor-compiler-proof.lisp
starlang-compiler/tests/actor-compiler-tests.lisp
starlang-compiler/tests/starlang-compiler-tests.asd
starlang-compiler/tests/starlang-compiler-tests.lisp
starlang-prototype.asd
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
star-artifact/star-artifact.asd
star-artifact/tests/star-artifact-tests.lisp
star-ipx/star-ipx.asd
star-ipx/tests/star-ipx-tests.asd
star-ipx/tests/star-ipx-tests.lisp
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
starlang-compiler/starlang-compiler.asd
starlang-compiler/tests/actor-compiler-proof.lisp
starlang-compiler/tests/actor-compiler-tests.lisp
starlang-compiler/tests/starlang-compiler-tests.asd
starlang-compiler/tests/starlang-compiler-tests.lisp
starlang-prototype.asd
```
