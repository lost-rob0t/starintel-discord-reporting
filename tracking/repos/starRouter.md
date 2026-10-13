# lost-rob0t/starRouter

- generated: `2026-10-13T06:50:49Z`
- canonical branch: `master`
- changelog eligible: `no`
- head: [`0a4e9abd073924e9186482fe847034b4fc4c401b`](https://github.com/lost-rob0t/starRouter/commit/0a4e9abd073924e9186482fe847034b4fc4c401b)
- head date: `2026-10-10T11:10:37-04:00`
- head subject: Merge pull request #3 from lost-rob0t/codex/starintel-0101

## Git log, last 14 days

```text
2026-10-10 0a4e9abd073924e9186482fe847034b4fc4c401b Merge pull request #3 from lost-rob0t/codex/starintel-0101
2026-10-10 d52a6d6111a159f259b3fd1610fc671b2da22f0b ci(router): verify exact candidate SHA in all admission gates (#11)
2026-10-10 faa2116b1a701b71b270abd838c0db063d7bcf1c fix(router): reconcile SC01 identity and multipart contracts (#11)
2026-10-10 bba57a52639cb480069556c442978cf10bd55f71 Reconcile StarRouter A2A regressions with generated StarLang 0.10.1 master
2026-10-10 039ebe9fe42e1acb8685e9d12b2cb70d026a44e3 fix(router): timestamp SC01 registration and heartbeat frames
2026-10-10 5bda35a93a12135c08c4851b9493ff89566f82eb Preserve SC01 event timestamps in StarRouter PUB forwarding
2026-10-10 db923a9c2c62cd9134b09bfc25e5bea6ebab1132 fix(client): propagate SC01 NACK and invalid broker acknowledgements
2026-10-10 8f8166ab908dd33130929e5aa99737719c6db0b8 docs: add StarIntel fleet agent contract (#8)
2026-10-09 4eb4abfe3f576bd0ae337fe8096e0517ef214f4c Remove unused Nim 2-incompatible server logging import
2026-10-09 7583306631aa2bd1915dec1e8686e416b9047543 Route SC01 commands once and preserve typed target handoffs
2026-10-09 20f20bae2f428768f1fc204a1e944ca89e30c900 Fix SC01 client event types and execute consumer contract regression
2026-10-06 59a8cb7790cfbfca6fa8f141094d95f525d9bd2c Merge pull request #7 from lost-rob0t/codex/fix-cosign-tuf-compat
2026-10-06 d2e847b7dc23035212a0d7e13a36c627bbf122dc ci: update Cosign trust-root support and verify release signatures
2026-10-06 e8c40b6e4e0d35319d4f0352fe1c44f5404d4b98 Merge pull request #6 from lost-rob0t/codex/starintel-0101-generated-consumer
2026-10-06 b35b19778c64127225a0f6d84c235bebf5f683d7 test: load native wire fixture in a compile-time constant
2026-10-06 0874270c065c9901cf4bd7b1a85fbeb2692f54ff fix: preserve exact document numbers in native JsonNode fetch
2026-10-05 f46fdf864e5284e2f690c11b24ffd73d7d161c5b test: exercise canonical raw JSON corpus over live broker
2026-10-05 c52dc97238ff545400c98d1d720076248564030d test: align broker wire fixtures with persistent document inventory
2026-10-05 2119a879d3ce30140d845e2df89e3d3ba302229c test: vendor raw JSON key fixture corpus
2026-10-05 91b5658064c9e954fdc7e0d6058d9461588b1c6d Use current Nim source-tree path in Router flake
2026-10-05 7194c6c73b994b56bb5269e7cf5655603700b189 Commit current Nim flake lock
2026-10-05 98e5d317a131da7f3faefba6b72f454330c89c8f Sync complete current StarLang release closure
2026-10-05 299af2d4aee2800df283fd758cae15e197fe1c8e Pin current Nim runtime and strict raw ingress
2026-10-05 a45efa93d65e3378d6eefaa60c00ad0a8bc4423e Revert partial raw-ingress update pending runtime repin
2026-10-05 0a18611be563edf38af18c4b5cf3b6c584a9cc4d Use strict maintained raw JSON ingress
2026-10-03 20e5c9e8bf49660fd230d8e7306dd9209648f6e9 Build and validate Router container from the pinned Nix package
2026-10-03 ebbd461ab1b93930440f451c7b976016a299acbc Validate StarRouter document frames against the generated StarLang release
2026-10-03 fcd9d51274bd962e53e1f7eaf2b8dda1364fdc20 Replace removed onbuild image with verified Nim 2 container build
2026-10-03 cda4722013a94df46c309a7c14c177caf79bfae5 Pin Nim 2-compatible ZMQ binding and check actual generic client sends
2026-10-03 90a899614e053fdea5debc5b405bd94fec79cdee Preserve opaque canonical document payloads during relay and replay
```

## Repository paths changed, last 14 days

```text
.dockerignore
.github/workflows/docker-publish.yml
.github/workflows/payload.yml
.github/workflows/validate.yml
.gitignore
AGENTS.md
Dockerfile
README.org
fixtures/raw-json-unique-keys.json
flake.lock
flake.nix
schema/starintel-schema.lock.json
schemas/legacy/starintel-doc-v0.9.0.schema.json
schemas/starintel-0.10.1/compatibility-fixtures.json
schemas/starintel-0.10.1/compatibility.json
schemas/starintel-0.10.1/core.star
schemas/starintel-0.10.1/generated/portable-manifest.json
schemas/starintel-0.10.1/generated/schema.json
schemas/starintel-0.10.1/generated/starintel.lisp
schemas/starintel-0.10.1/generated/starintel_types.nim
schemas/starintel-0.10.1/generated/starintel_types.py
schemas/starintel-0.10.1/generated/starintel_types.ts
schemas/starintel-0.10.1/legacy-workflow-oracle.json
schemas/starintel-0.10.1/operation_semantics.py
schemas/starintel-0.10.1/release-lock.json
schemas/starintel-0.10.1/research-fixtures.json
schemas/starintel-0.10.1/schema-lock-manifest.json
schemas/starintel-0.10.1/supported-workflow-fixtures.json
schemas/starintel-0.10.1/supported-workflow-inventory.json
schemas/starintel-0.10.1/supported-workflow-mappings.json
schemas/starintel-0.10.1/workflow_semantics.py
scripts/check-runtime-release.py
scripts/sync-starintel-schema.py
src/starRouter.nim
src/starRouterpkg/client.nim
src/starRouterpkg/payload.nim
src/starRouterpkg/proto.nim
src/starRouterpkg/server.nim
src/starRouterpkg/wire.nim
starRouter.nimble
tests/broker_wire.py
tests/client_wire.nim
tests/test1.nim
tests/test_client_contract.nim
tests/test_dispatch_contract.nim
tests/test_payload.nim
tests/test_wire.nim
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/docker-publish.yml
.github/workflows/payload.yml
.github/workflows/validate.yml
flake.nix
scripts/check-runtime-release.py
scripts/sync-starintel-schema.py
tests/broker_wire.py
tests/client_wire.nim
tests/test1.nim
tests/test_client_contract.nim
tests/test_dispatch_contract.nim
tests/test_payload.nim
tests/test_wire.nim
```
