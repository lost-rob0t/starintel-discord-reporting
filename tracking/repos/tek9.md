# lost-rob0t/tek9

- generated: `2026-08-30T00:23:07Z`
- canonical branch: `master`
- changelog eligible: `yes`
- head: [`a9f5b595f5d965163d2b7c518c72a2efd9be13fe`](https://github.com/lost-rob0t/tek9/commit/a9f5b595f5d965163d2b7c518c72a2efd9be13fe)
- head date: `2026-08-29T10:15:48-04:00`
- head subject: Merge pull request #9 from lost-rob0t/merge/issue-7-nix-package

## Git log, last 14 days

```text
2026-08-29 a9f5b595f5d965163d2b7c518c72a2efd9be13fe Merge pull request #9 from lost-rob0t/merge/issue-7-nix-package
2026-08-29 5931490eee6f160edf37830fbe96e7142fe68533 fix(nix): link LMDB while building Lisp dependency
2026-08-29 10cc1332f1e437d4e15b48f8e91c2a24f3ee74bb fix(nix): prove downstream Tek9 consumption
2026-08-29 c4f8489b7a4e2ff56e01a0c1a280d7b274370f31 feat(nix): expose Tek9 as consumable ASDF package
2026-08-29 dd596fc8c164565d7ef0c1c3d6871b752af42202 test: define red consumable Tek9 flake contract
2026-08-17 ca24ef35ea6877420cbca057dd7fb702fe29a740 Merge pull request #6 from lost-rob0t/agent/composable-transactions-graph-lifecycle
2026-08-17 24ff1f7fb3a95f9b0a12efd2769eb2894743c22d docs: document cross-database transaction guard
2026-08-17 ca25671e5d4c76fad81b45030f7cd2aa47363f69 api: export cross-database transaction error
2026-08-17 d7cb8c24ec32b89a5fea1ee62851b191b2bd57ce fix: reject cross-database transaction nesting
2026-08-17 7d8f390173bab9a4876decc807034d5095e2c776 test: reject cross-database nested transactions
2026-08-17 bed82c71d20a7640d6378aaf5934f984c5874e6e test: cover first-use DBIs in outer transactions
2026-08-17 90bc9915e50b6f55729bd3297d8d7bbcdd2f6f92 docs: describe transaction and graph lifecycle APIs
2026-08-17 cbd79025e9615e7c71d021ac30410bf314a7d8d3 feat: add composable transactions and graph lifecycle
2026-08-17 2d3d0a0101f017a65c90a1e8864e2e7dd5c21af2 test: define transaction and graph lifecycle invariants
2026-08-17 093020b82543a56b295c1726b7ff9b10078e1a4c Merge pull request #3 from lost-rob0t/agent/public-view-query-api
2026-08-17 63c144ba2da506d6ca4cbedc79a5079d6be7b7e6 test: fix FiveAM boolean assertions
2026-08-16 fc0774a1f87ad0e70ebf401fc34cb2d9c1f2f873 fix public view range expectations
2026-08-16 d753e206a12c779acfaedee9fa6364e373f611d2 test public materialized view reads
2026-08-16 2906c6446c3082c1e7a85b93f2766214d084a60b export public view query api
2026-08-16 99b0792f59f7128c8758873a7dd610593ca0eb9c add public materialized view read api
```

## Repository paths changed, last 14 days

```text
.github/workflows/ci.yml
README.org
TRANSACTIONS.org
flake.lock
flake.nix
src/graph-lifecycle.lisp
src/objects.lisp
src/package.lisp
src/tek9.asd
src/views.lisp
tests/nix-package-smoke.sh
tests/tek9-tests.asd
tests/test-graph-lifecycle.lisp
tests/test-transactions.lisp
tests/test-views.lisp
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/ci.yml
flake.nix
src/tek9.asd
tests/nix-package-smoke.sh
tests/tek9-tests.asd
tests/test-graph-lifecycle.lisp
tests/test-transactions.lisp
tests/test-views.lisp
```
