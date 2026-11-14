# lost-rob0t/star-lang

- generated: `2026-11-14T06:31:15Z`
- canonical branch: `main`
- changelog eligible: `yes`
- head: [`ecc87055b2ebacec72c246be83251dbf7415d2a3`](https://github.com/lost-rob0t/star-lang/commit/ecc87055b2ebacec72c246be83251dbf7415d2a3)
- head date: `2026-11-14T00:57:54Z`
- head subject: Merge pull request 'feat: URI-native actor bodies + star-transport-zmq ingest (W14 gate, #72)' (#217) from feat/72-uri-native-bodies-zmq-ingest into main

## Git log, last 14 days

```text
2026-11-14 ecc87055b2ebacec72c246be83251dbf7415d2a3 Merge pull request 'feat: URI-native actor bodies + star-transport-zmq ingest (W14 gate, #72)' (#217) from feat/72-uri-native-bodies-zmq-ingest into main
2026-11-13 4e3e49553d5d4c6709e09ca588e6669e7cf6c7ff ci: vendor pzmq so the apt ASDF gate can load star-transport-zmq
2026-11-13 f8070b25696f7b5fb4ffc7c75a1aeea062f9c431 feat: star-lang #72 native actor bodies + star-transport-zmq ingest (W14 gate)
```

## Repository paths changed, last 14 days

```text
.github/workflows/ci.yml
ci/target-systems.txt
ci/with-nix-sbcl.sh
fixtures/ingest/envelope-codec.lisp
fixtures/ingest/ingest-client.lisp
fixtures/ingest/ingest-core.star
fixtures/ingest/ingest-service.lisp
fixtures/ingest/ingest-service.star
flake.nix
prototype/domain-server-core-prototype.lisp
prototype/transport-port-prototype.lisp
star-actor-protocol/src/actor-reference.lisp
star-actor-protocol/src/packages.lisp
star-actor-protocol/src/resource-uri.lisp
star-actor-protocol/star-actor-protocol.asd
star-actor-protocol/tests/resource-uri-tests.lisp
star-actor-protocol/tests/star-actor-protocol-tests.asd
star-adapter-sdk/src/packages.lisp
star-adapter-sdk/src/transport.lisp
star-adapter-sdk/star-adapter-sdk.asd
star-adapter-sdk/tests/star-adapter-sdk-tests.asd
star-adapter-sdk/tests/transport-port-tests.lisp
star-canonical-json/src/starlang-wire-json.lisp
star-transport-zmq/src/packages.lisp
star-transport-zmq/src/zmq-transport.lisp
star-transport-zmq/star-transport-zmq.asd
star-transport-zmq/tests/ingest-fixture-tests.lisp
star-transport-zmq/tests/star-transport-zmq-tests.asd
star-transport-zmq/tests/zmq-transport-tests.lisp
starlang-compiler/src/actor-body.lisp
starlang-compiler/src/actor-ir.lisp
starlang-compiler/src/actor-manifest.lisp
starlang-compiler/src/domain-ir.lisp
starlang-compiler/src/public-surface.lisp
starlang-compiler/starlang-compiler.asd
starlang-compiler/tests/actor-body-tests.lisp
starlang-compiler/tests/starlang-compiler-tests.asd
starlang-prototype.asd
starlang-runtime/src/domain-engine.lisp
starlang-runtime/src/native-body.lisp
starlang-runtime/src/packages.lisp
starlang-runtime/src/runtime-directory.lisp
starlang-runtime/src/runtime.lisp
starlang-runtime/starlang-runtime.asd
starlang-runtime/tests/native-body-tests.lisp
starlang-runtime/tests/starlang-runtime-tests.asd
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/ci.yml
ci/target-systems.txt
ci/with-nix-sbcl.sh
flake.nix
star-actor-protocol/star-actor-protocol.asd
star-actor-protocol/tests/resource-uri-tests.lisp
star-actor-protocol/tests/star-actor-protocol-tests.asd
star-adapter-sdk/star-adapter-sdk.asd
star-adapter-sdk/tests/star-adapter-sdk-tests.asd
star-adapter-sdk/tests/transport-port-tests.lisp
star-transport-zmq/star-transport-zmq.asd
star-transport-zmq/tests/ingest-fixture-tests.lisp
star-transport-zmq/tests/star-transport-zmq-tests.asd
star-transport-zmq/tests/zmq-transport-tests.lisp
starlang-compiler/starlang-compiler.asd
starlang-compiler/tests/actor-body-tests.lisp
starlang-compiler/tests/starlang-compiler-tests.asd
starlang-prototype.asd
starlang-runtime/starlang-runtime.asd
starlang-runtime/tests/native-body-tests.lisp
starlang-runtime/tests/starlang-runtime-tests.asd
```
