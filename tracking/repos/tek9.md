# lost-rob0t/tek9

- generated: `2026-09-20T22:29:10Z`
- canonical branch: `master`
- changelog eligible: `yes`
- head: [`e6d1cb86a2e268a894eae3acae9617238b2adcff`](https://github.com/lost-rob0t/tek9/commit/e6d1cb86a2e268a894eae3acae9617238b2adcff)
- head date: `2026-09-19T16:07:11-04:00`
- head subject: Merge pull request #56 from lost-rob0t/feat/54-streaming-checkpoint-ingest

## Git log, last 14 days

```text
2026-09-19 e6d1cb86a2e268a894eae3acae9617238b2adcff Merge pull request #56 from lost-rob0t/feat/54-streaming-checkpoint-ingest
2026-09-18 05498f6f7e0428466817861e1b39e5022a858a3d fix(nix): escape worker environment expansion
2026-09-18 ae5232e1cbaad3af6e107aa21b43a69d76fbe988 nix: package the local Tek9 ingest worker
2026-09-18 d4473e93895fffe48fa033ebcd9488403e740f4f test: run ingest worker suite
2026-09-18 55bbca6393a98586f2663afa04510896ae83cc8d feat: export local ingest worker API
2026-09-18 ddd643f1ee371aa166dd4afc3e15c904ac8283f2 build: load JSONL ingest worker
2026-09-18 8ed28490bd060630ab713801aec3683540e47e66 feat: add closed JSONL ingest worker
2026-09-18 9fb9df13e6d8e9e443a23851efd15725feb3cc2e test: specify fixed-command JSONL ingest worker
2026-09-18 c05976aeb25f75d3871c05412ba7128fc4cc9fbd docs: document checkpointed source ingest
2026-09-18 1a1adeba83f41c456812667ea46f6522ffbaf40b test: run checkpointed ingest suite
2026-09-18 99490c4c5c38bbecf5f86762be573c24723bc55c feat: export checkpointed ingest API
2026-09-18 5715e2d7580ead31db78b93ba560fe5450fbc2ae build: load ingest transaction layer
2026-09-18 1a00e566e656ea2fbf39c882365f5052532d55eb feat: add atomic checkpointed ingest batches
2026-09-18 5067d6ae75b96fb159064b26bcb07ef27fe77e7c test: specify atomic checkpointed ingest batches
2026-09-17 8178cf0af2fcad48b509b439423c030008d62620 star-git: add verified custody and safe hot eviction
2026-09-17 b19f4dc7178a2ca07141cdb3ad700aef699f3178 star-git: expose Nix package with liblzma closure
2026-09-17 79bf85fefa249a554f70c258cf5ea4e4cf0510bb star-git: add commit-v2 provenance and Couch revision index
2026-09-17 429ad72cef9e52c510391fdaf0311715eb5dd496 star-git: add immutable tree snapshots and explicit ref restore
2026-09-17 c9364c229464e2334f93006267638ffa70e316ba star-git: add deterministic LZMA archive packs
2026-09-17 3a1adc6488b16073eb05ad9aedb10d06758b0136 star-git: add immutable revision core
```

## Repository paths changed, last 14 days

```text
README.org
flake.nix
src/ingest-worker.lisp
src/ingest.lisp
src/package.lisp
src/star-git.asd
src/star-git/commit-v2.lisp
src/star-git/compression.lisp
src/star-git/custody.lisp
src/star-git/package.lisp
src/star-git/packs.lisp
src/star-git/repository.lisp
src/star-git/snapshots.lisp
src/tek9.asd
tests/nix-package-smoke.sh
tests/package.lisp
tests/tek9-tests.asd
tests/test-ingest-worker.lisp
tests/test-ingest.lisp
tests/test-star-git-custody.lisp
tests/test-star-git-snapshots.lisp
tests/test-star-git-v2.lisp
tests/test-star-git.lisp
```

## Test and CI paths touched, last 14 days

```text
flake.nix
src/star-git.asd
src/tek9.asd
tests/nix-package-smoke.sh
tests/package.lisp
tests/tek9-tests.asd
tests/test-ingest-worker.lisp
tests/test-ingest.lisp
tests/test-star-git-custody.lisp
tests/test-star-git-snapshots.lisp
tests/test-star-git-v2.lisp
tests/test-star-git.lisp
```
