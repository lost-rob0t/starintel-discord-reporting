# lost-rob0t/star-lang

- generated: `2026-08-29T11:08:28Z`
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
2026-08-15 067f12506f429c8d34f0383729972e3ee1337c05 Merge pull request #38 from lost-rob0t/agent/freeze-verification-certificate-claims
2026-08-15 fc5537a885f214b69c382e7d54b04435107f5018 Keep final dispatcher tests in runtime gate
2026-08-15 6076285069e01ad2d088e328de566646d09fe10b Run final wire dispatcher tests through ASDF
2026-08-15 4df1941596f0f6034322b8e2fd7773a453d5392e Delegate prototype idempotency identity to final dispatcher
2026-08-15 d4dfd192c4c68fd3030e6ed096095232d699193f Reduce prototype dispatcher to final-runtime compatibility
2026-08-15 4b657eb2f2cea38f3fa36ee43234ed040f16cf86 Load final wire dispatcher from starlang-runtime
2026-08-15 45a5c043147d6c6c52eb35177e8b8c5895a28244 Fix final wire dispatcher package surface
2026-08-15 4c0ec7411ee216c91c01769293d5054a0899e136 Run verification scope tests
2026-08-15 0b858b7b1d36227cbe8095aacd4e3d004f05e69c Test verification evidence scope rules
2026-08-15 cd8a5bd3124681b86409a962a0b217e7431d7bcc Require plans for analyzed certificates
2026-08-15 2b5896724824207e777eff2e52310fdedcb8b1c0 State verification authority boundary
2026-08-15 f596d6efc18f94601a9a70c58f2a0a20a7986095 Document verification certificate authority
2026-08-15 35dc2ac98f970d3fbc249fec800bf885ef6d309e Harden verification certificate scope
2026-08-15 42ed5a295dcd4d874222acd49fa995344416a857 Test star-verification independently
2026-08-15 1a23ca5163e315af6796b2deb4f35e82ce703767 Load star-verification independently
2026-08-15 50077761f744f30efb839643573fe4a0968a19db Harden verification certificate tests
2026-08-15 3ffcd0b42595d91e21f1143c2b144eaacc6627db Test verification certificate contract
2026-08-15 295c54a0b65aa4aab87e97562856e9427b03358a Add verification certificate test system
2026-08-15 4426e1d1c96e47774348a31147892785469af160 Implement immutable verification certificates
2026-08-15 6487521d865e8e94687845d879ec8481181efcaf Define verification certificate package
2026-08-15 ec223dfff0706642f031921d1f8c19991d3ce440 Add verification certificate system
2026-08-15 28bb8adc6be8bdfbac68e87b2ea89a8dd1cd66da Extract deterministic wire dispatcher into starlang-runtime (#37)
2026-08-15 197a4759f1b756bb24e20477c3ddff58c410c493 Extract canonical StarLang wire encoding into star-canonical-json (#36)
2026-08-15 9d3b82b99298a700b843ed0a5358a2b5b202cc02 Extract portable payload validation into star-actor-protocol (#35)
2026-08-15 0f499dd826e8828f98959ceddb9b3bcb1e74c9ee Extract portable wire contract into star-actor-protocol (#34)
2026-08-15 f28c6212a249b6dd5673f9d98806a1b1c6d90da3 Extract runtime directory resolution into starlang-runtime (#33)
2026-08-15 31888f9a7d7671fa8599bd49f4f396bc31652cf7 Extract heartbeat lease primitive into star-lease (#32)
2026-08-15 137a82f4c869d69c48ff7a453fc4aa1332c4d26e Extract runtime journal core into star-journal (#31)
2026-08-15 6251c4d140b43856e2003d7a359547a39e8bb993 Extract canonical JSON serializer core (#30)
2026-08-15 bdf38e6b9f9eb1d474b4870b91d44acd306634ba Extract wire lifecycle contract into star-actor-protocol (#29)
2026-08-15 4cf0f1b30d4edd0714272a876f9d8418fc9befb5 Extract concrete Sento remoting adapter (#28)
2026-08-15 724347d3f19969501c4124cb525b27173ece3d05 Extract mailbox actor execution and Sento runtime port (#27)
```

## Repository paths changed, last 14 days

```text
.github/workflows/ci.yml
.github/workflows/logic-ir.yml
.github/workflows/verification.yml
README.md
ci/target-systems.txt
docs/implementation-slices/ACTOR-RUNTIME-MIGRATION-MATRIX.md
fixtures/canonical/SHA256SUMS
fixtures/canonical/logic-call-materialized-v1.json
flake.nix
prototype/actor-wire-prototype.lisp
prototype/bbp-remoting-runtime-example.lisp
prototype/canonical-json-prototype.lisp
prototype/cl-gserver-runtime-facade-prototype.lisp
prototype/deferred-dispatch-completion-prototype.lisp
prototype/deterministic-dispatcher-prototype.lisp
prototype/dispatcher-idempotency-identity-prototype.lisp
prototype/domain-remoting-lease-prototype.lisp
prototype/message-lifecycle-prototype.lisp
prototype/runtime-directory-prototype.lisp
prototype/runtime-journal-port-prototype.lisp
prototype/sento-remoting-domain-adapter.lisp
star-actor-protocol/src/actor-reference.lisp
star-actor-protocol/src/message-lifecycle.lisp
star-actor-protocol/src/packages.lisp
star-actor-protocol/src/portable-payload.lisp
star-actor-protocol/src/portable-wire.lisp
star-actor-protocol/star-actor-protocol.asd
star-actor-protocol/tests/portable-payload-tests.lisp
star-actor-protocol/tests/portable-wire-tests.lisp
star-actor-protocol/tests/star-actor-protocol-tests.asd
star-actor-protocol/tests/star-actor-protocol-tests.lisp
star-canonical-json/src/canonical-json.lisp
star-canonical-json/src/packages.lisp
star-canonical-json/src/starlang-wire-json.lisp
star-canonical-json/star-canonical-json.asd
star-canonical-json/tests/star-canonical-json-tests.asd
star-canonical-json/tests/star-canonical-json-tests.lisp
star-canonical-json/tests/starlang-wire-json-tests.lisp
star-journal/src/journal.lisp
star-journal/src/packages.lisp
star-journal/star-journal.asd
star-journal/tests/star-journal-tests.asd
star-journal/tests/star-journal-tests.lisp
star-lease/src/heartbeat-lease.lisp
star-lease/src/packages.lisp
star-lease/star-lease.asd
star-lease/tests/star-lease-tests.asd
star-lease/tests/star-lease-tests.lisp
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
star-mailbox/src/mailbox.lisp
star-mailbox/src/packages.lisp
star-mailbox/star-mailbox.asd
star-mailbox/tests/star-mailbox-tests.lisp
star-sento-compat/src/packages.lisp
star-sento-compat/src/runtime-port.lisp
star-sento-compat/src/sento-adapter.lisp
star-sento-compat/star-sento-compat.asd
star-sento-compat/tests/star-sento-compat-tests.lisp
star-verification/src/certificate.lisp
star-verification/src/packages.lisp
star-verification/star-verification.asd
star-verification/tests/scope-tests.lisp
star-verification/tests/star-verification-tests.asd
star-verification/tests/star-verification-tests.lisp
starlang-compiler/src/logic-policy.lisp
starlang-compiler/src/packages.lisp
starlang-compiler/starlang-compiler.asd
starlang-compiler/tests/starlang-compiler-tests.asd
starlang-compiler/tests/starlang-compiler-tests.lisp
starlang-prototype.asd
starlang-runtime/src/packages.lisp
starlang-runtime/src/runtime-directory.lisp
starlang-runtime/src/runtime.lisp
starlang-runtime/src/wire-dispatcher.lisp
starlang-runtime/starlang-runtime.asd
starlang-runtime/tests/starlang-runtime-tests.asd
starlang-runtime/tests/starlang-runtime-tests.lisp
starlang-runtime/tests/wire-dispatcher-tests.lisp
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/ci.yml
.github/workflows/logic-ir.yml
.github/workflows/verification.yml
ci/target-systems.txt
flake.nix
star-actor-protocol/star-actor-protocol.asd
star-actor-protocol/tests/portable-payload-tests.lisp
star-actor-protocol/tests/portable-wire-tests.lisp
star-actor-protocol/tests/star-actor-protocol-tests.asd
star-actor-protocol/tests/star-actor-protocol-tests.lisp
star-canonical-json/star-canonical-json.asd
star-canonical-json/tests/star-canonical-json-tests.asd
star-canonical-json/tests/star-canonical-json-tests.lisp
star-canonical-json/tests/starlang-wire-json-tests.lisp
star-journal/star-journal.asd
star-journal/tests/star-journal-tests.asd
star-journal/tests/star-journal-tests.lisp
star-lease/star-lease.asd
star-lease/tests/star-lease-tests.asd
star-lease/tests/star-lease-tests.lisp
star-logic-ir/star-logic-ir.asd
star-logic-ir/tests/conformance.lisp
star-logic-ir/tests/helpers.lisp
star-logic-ir/tests/star-logic-ir-tests.asd
star-logic-ir/tests/star-logic-ir-tests.lisp
star-logic-protocol/star-logic-protocol.asd
star-logic-protocol/tests/star-logic-protocol-tests.asd
star-logic-protocol/tests/star-logic-protocol-tests.lisp
star-logic-testing/star-logic-testing.asd
star-mailbox/star-mailbox.asd
star-mailbox/tests/star-mailbox-tests.lisp
star-sento-compat/star-sento-compat.asd
star-sento-compat/tests/star-sento-compat-tests.lisp
star-verification/star-verification.asd
star-verification/tests/scope-tests.lisp
star-verification/tests/star-verification-tests.asd
star-verification/tests/star-verification-tests.lisp
starlang-compiler/starlang-compiler.asd
starlang-compiler/tests/starlang-compiler-tests.asd
starlang-compiler/tests/starlang-compiler-tests.lisp
starlang-prototype.asd
starlang-runtime/starlang-runtime.asd
starlang-runtime/tests/starlang-runtime-tests.asd
starlang-runtime/tests/starlang-runtime-tests.lisp
starlang-runtime/tests/wire-dispatcher-tests.lisp
```
