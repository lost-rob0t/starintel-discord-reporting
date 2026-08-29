# lost-rob0t/star-lang

- generated: `2026-08-29T20:57:22Z`
- canonical branch: `main`
- changelog eligible: `yes`
- head: [`0472ed8f4472252038b62bb19a17aa09d2ddf1b4`](https://github.com/lost-rob0t/star-lang/commit/0472ed8f4472252038b62bb19a17aa09d2ddf1b4)
- head date: `2026-08-16T16:42:46-04:00`
- head subject: Merge pull request #41 from lost-rob0t/agent/logic-call-ir-policy

## Git log, last 14 days

```text
2026-08-16 0472ed8f4472252038b62bb19a17aa09d2ddf1b4 Merge pull request #41 from lost-rob0t/agent/logic-call-ir-policy
2026-08-16 1654a51938c3b611cae9d9d58522633ed100e3a1 test(compiler): run final logic-policy suite explicitly
2026-08-16 b1caa41ea5cc5f19e99fb9334c4eecda270f21be test(compiler): invoke suite through its package
2026-08-16 4709d9640dedeeffbc4084001052adff876efb39 test(logic): mutate fresh data in defensive-copy test
2026-08-16 974d646fc987da6abb739a760965af6ffcbe73ab ci(logic): retain failure logs for diagnosis
2026-08-16 6bf21df7291ab593ef57c0fe2c558eb88b1c26cb test(logic): load split conformance suite
2026-08-16 c50a2770dc07286b939a1b9a5dbc3cf44c7c8cd3 test(logic): simplify raw backend form fixtures
2026-08-16 eaee56baadf538fddd057fd7e8cb057a09078249 test(logic): add IR materialization conformance coverage
2026-08-16 55f57c14dcfa80b4a777a1c2fab17f38fdb0e413 test(logic): add conformance test helpers
2026-08-16 e702c89e4dc3429df4f62e2877d6e37b656060e1 test(logic): replace monolithic conformance test file
2026-08-16 a58bb62736432920a42edede3174bf576a171651 test(logic): checksum materialized plan fixture
2026-08-16 3df3cb024ec8ebc4a79f0e2cf756a0cfd3741514 ci(logic): add independent IR materialization gate
2026-08-16 198e03624e3e2b0b3b56bfce0e17338dfa729938 ci(logic): load final logic IR independently
2026-08-16 f9eb25c2c2ca28b4b87ba7e54b4c9a4034bbbbc5 test(compiler): prove logic compatibility layer stays thin
2026-08-16 7045b6efb876f46cb18d1df0b18f343ccfd680cb test(compiler): exercise logic policy forwarding
2026-08-16 b842cfc4af93150d3fc8b1507f87b94aac739246 feat(compiler): forward checked logic calls to final IR
2026-08-16 567da2d50c60bf143fc43041edf489b1b130de18 feat(compiler): expose logic policy forwarding API
2026-08-16 003801830738159e4f9ae5002a1809caab806d13 feat(compiler): depend on final logic IR authority
2026-08-16 a667cbd41e7138a947a41998eb20373b87766719 test(logic): freeze materialized logic plan fixture
2026-08-16 f8f9e0193197b8aded1a1a3ce533e8b38d7f4288 test(logic): cover policy and materialization failures
2026-08-16 896ffa7ffde35bcf49d5bddbfd428a507c3fcc0c test(logic): add engine-free IR conformance system
2026-08-16 90e4fa453a01f82642fd15bbf3190926408ff8c9 feat(logic): serialize logic plans with canonical JSON
2026-08-16 244aae868171a7d3f05a7caf3e7d58a0dab3296d feat(logic): implement normalized calls and materialization
2026-08-16 7e1d0911cdd78bccba3fe2af00a068d1d7f30899 feat(logic): define logic IR package surface
2026-08-16 d0f41883eb6773356fb876a0b3a5830a31f7d59f feat(logic): add final-owned logic IR system
2026-08-16 fc5a6e00ff212278dd1c263223272501d81ad678 Add portable logic protocol and fake backend foundation
```

## Repository paths changed, last 14 days

```text
.github/workflows/ci.yml
.github/workflows/logic-ir.yml
ci/target-systems.txt
fixtures/canonical/SHA256SUMS
fixtures/canonical/logic-call-materialized-v1.json
star-logic-ir/src/canonical-json.lisp
star-logic-ir/src/logic-ir.lisp
star-logic-ir/src/packages.lisp
star-logic-ir/star-logic-ir.asd
star-logic-ir/tests/conformance.lisp
star-logic-ir/tests/helpers.lisp
star-logic-ir/tests/star-logic-ir-tests.asd
star-logic-ir/tests/star-logic-ir-tests.lisp
star-logic-protocol/src/packages.lisp
star-logic-protocol/src/protocol.lisp
star-logic-protocol/star-logic-protocol.asd
star-logic-protocol/tests/star-logic-protocol-tests.asd
star-logic-protocol/tests/star-logic-protocol-tests.lisp
star-logic-testing/src/fake-backend.lisp
star-logic-testing/src/packages.lisp
star-logic-testing/star-logic-testing.asd
starlang-compiler/src/logic-policy.lisp
starlang-compiler/src/packages.lisp
starlang-compiler/starlang-compiler.asd
starlang-compiler/tests/starlang-compiler-tests.asd
starlang-compiler/tests/starlang-compiler-tests.lisp
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/ci.yml
.github/workflows/logic-ir.yml
ci/target-systems.txt
star-logic-ir/star-logic-ir.asd
star-logic-ir/tests/conformance.lisp
star-logic-ir/tests/helpers.lisp
star-logic-ir/tests/star-logic-ir-tests.asd
star-logic-ir/tests/star-logic-ir-tests.lisp
star-logic-protocol/star-logic-protocol.asd
star-logic-protocol/tests/star-logic-protocol-tests.asd
star-logic-protocol/tests/star-logic-protocol-tests.lisp
star-logic-testing/star-logic-testing.asd
starlang-compiler/starlang-compiler.asd
starlang-compiler/tests/starlang-compiler-tests.asd
starlang-compiler/tests/starlang-compiler-tests.lisp
```
