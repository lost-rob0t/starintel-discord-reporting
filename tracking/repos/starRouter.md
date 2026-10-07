# lost-rob0t/starRouter

- generated: `2026-10-07T08:44:52Z`
- canonical branch: `master`
- changelog eligible: `no`
- head: [`59a8cb7790cfbfca6fa8f141094d95f525d9bd2c`](https://github.com/lost-rob0t/starRouter/commit/59a8cb7790cfbfca6fa8f141094d95f525d9bd2c)
- head date: `2026-10-06T02:32:12-04:00`
- head subject: Merge pull request #7 from lost-rob0t/codex/fix-cosign-tuf-compat

## Git log, last 14 days

```text
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
```

## Repository paths changed, last 14 days

```text
.dockerignore
.github/workflows/docker-publish.yml
.github/workflows/validate.yml
.gitignore
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
src/starRouterpkg/server.nim
src/starRouterpkg/wire.nim
starRouter.nimble
tests/broker_wire.py
tests/client_wire.nim
tests/test_wire.nim
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/docker-publish.yml
.github/workflows/validate.yml
flake.nix
scripts/check-runtime-release.py
scripts/sync-starintel-schema.py
tests/broker_wire.py
tests/client_wire.nim
tests/test_wire.nim
```
