# lost-rob0t/starintel-server

- generated: `2026-09-13T04:52:57Z`
- canonical branch: `master`
- changelog eligible: `yes`
- head: [`436a96bd2feffb18c1fc41beaaf48a28781906c7`](https://github.com/lost-rob0t/starintel-server/commit/436a96bd2feffb18c1fc41beaaf48a28781906c7)
- head date: `2026-09-12T08:56:58-04:00`
- head subject: Merge pull request #173 from lost-rob0t/test/172-target-tenant-http-stack

## Git log, last 14 days

```text
2026-09-12 436a96bd2feffb18c1fc41beaaf48a28781906c7 Merge pull request #173 from lost-rob0t/test/172-target-tenant-http-stack
2026-09-12 46a1bbfd54434a21fc40d2941bf3b05b905268fe test: exercise non-default target tenant over HTTP stack
2026-09-12 75bea2624ec773f4737aaa2bd6b0a65ac5c6c462 Merge pull request #176 from lost-rob0t/fix/174-rabbit-startup-retry
2026-09-12 2eec346eb38e91a84ca8609268ddad8e0f83df62 test: cover Rabbit consumer startup retry boundaries
2026-09-12 ab928d8381a5fa7c889a51d6b3c2d8d6861f4ea6 fix: destroy partial Rabbit connection after open failure
2026-09-12 7ad03c3fae771a3e4ff3bab175eb6eed73be5ef5 fix: scope startup retry to retrying Rabbit streams
2026-09-12 a21c16b5e8895afcb029ad30b025ea1065f8208f build: load Rabbit startup retry before runtime lifecycle
2026-09-12 a785b27b3463cc474d441caaad71c237f78f5766 fix: add bounded Rabbit consumer startup retry
2026-09-12 09e44169e9b1b65b4ceecd964b9a782f5655cc0e Merge pull request #171 from lost-rob0t/fix/169-target-tenant-isolation-20260912
2026-09-12 77f4be34c4b98b0988f974b24acc1707c3a5361c docs: keep exported target-list contract text stable
2026-09-12 b8d29c1970000087b564793758dbcacec53c107c test: cover optional target-list scope narrowing
2026-09-12 059a09552dc82a3ced250cd62575dd4f827ca58d fix: preserve optional target-list scope restrictions
2026-09-12 e4d6b213d4a1fc23b1a8113def9b846d273e1c8c test: require tenant isolation suite in canonical unit gate
2026-09-12 303596cb9e93fab27493d6717e6a3900bba89eed test: load target tenant isolation suite
2026-09-12 0148fa146278bb355edffe4038ccb4df14d2d2b5 fix: reject poisoned cross-actor target rows
2026-09-12 0ee99822babbbbe1250e3bc16eefd1a060d87c6b test: cover target tenant isolation regressions and adverse responses
2026-09-12 9a60e506174177d35981a96082c96926071662ae fix: keep target-list authorization to tenant and actor scopes
2026-09-12 39c3db953032f4d257ac212836d05b365a207b81 fix: add tenant-scoped target view
2026-09-12 cc5a00974b320de0598ffd25af229eb02dc58a0e fix: scope target reads by requested tenant
2026-09-11 3e1f78523f377a94f43fda7a3cc1fc6622d7269d Merge pull request #153 from lost-rob0t/feat/operation-object-151
2026-09-11 8dd6b4afb871f0b2b059fb2ff08ed2d75cd19006 test: pin operation 0.9.1 release in contract checks
2026-09-09 6748f685051fd147447c77d3b1de9e557648415d ci: remove one-shot operation runtime sync
2026-09-09 fdcef990b867f9293a8c181e56438e1dd253a218 fix: consume corrected operation runtime and refresh API docs
2026-09-09 bff798240bc13a5f2e0914211ed1ca8a7f65a55f ci: fix portable stale-pin scan
2026-09-09 a2584bcc2b451bc531291a58d7104657b015e615 ci: trigger operation runtime sync
2026-09-09 eea6d56fcecd391f97432a1d34e9ce15ec5f8241 ci: sync merged operation runtime and generated docs
2026-09-08 31b5a7a2f0cc88377c1e100134d649b8249b8fb5 chore(qlot): pin merged star-cl operation runtime
2026-09-08 814aff2b421560f19cf491e1b67a829973803c37 test(v0.9): expect merged star-cl operation runtime
2026-09-08 010a298691d57eda45f2052241042e1c7be2b963 ci(schema): verify canonical required dtypes
2026-09-08 94bfbba5dbd45eeec91706c9ff98cf0f4b5fa9f2 chore(ci): remove star-cl lock sync workflow
2026-09-09 3c753e94133af59939df25d57b15626208c07c7b chore(nix): pin merged star-cl operation runtime [star-cl-sync]
2026-09-08 7c9c4310ff28c8e9b2aa116cb11d5f165722f298 ci: pin merged star-cl operation runtime
2026-09-08 122e017167b245971f9fd207263aa3c24725ecc8 test(schema): verify all required canonical dtypes
2026-09-08 3e65466b8d8a214592363e7cc3ab6a4752662d86 chore(schema): pin merged operation 0.9.1 canonical contract
2026-09-08 074fdfcf0ab30b257dae722a63e6ce9ab281a738 docs: describe operation control-plane object
2026-09-08 4a04dfdec480296e6a347372670c03dfbcd0fc23 test: prove operation passes strict server boundary
2026-09-11 aeae5bf2757f23121d5ef2eabf24a0a35231d9d4 Merge pull request #154 from lost-rob0t/fix/valkey-pool-wait-recheck
2026-09-11 05b079ab270991bd3ffd56166fb26cb9c77b9291 docs: regenerate api docs for lease fix base
2026-09-11 b3e9ab3e50b1f7ec4ed28346d5d18ebfef35e9de fix: make valkey lease concurrency outcomes deterministic
2026-09-06 4721efaf8141fd7199b6e1ceb1011b9ad970796e Merge pull request #145 from lost-rob0t/fix/target-dispatch-data-shape
2026-09-06 9d80cc1710cfe2a5c62c54fc8a2a23b9b7c564f3 fix: emit v0.9-valid data.*-shaped target documents from both routes
2026-09-06 c06b8fc466ea765ef2a857b137d43d6b2535c90f Merge pull request #134 from lost-rob0t/fix/v09-false-value-pipeline
2026-09-06 0b1ab8d6bbbaac9b5b73df5d7f66af29057522a1 test: follow consolidated documentation paths
2026-09-06 cc86eca9e623ba3b990a2029b4b51f0f46fada77 Merge commit 'e1af325ea1e1d9ff83c1b41c999d5519af76f8d6' into debug/json-pr-refresh
2026-09-06 e1af325ea1e1d9ff83c1b41c999d5519af76f8d6 Merge branch 'docs/consolidate': merge doc and docs into doc/
2026-09-06 b923e0e99a760937f85c8af91094ca1b888b9184 docs: consolidate manual docs and generated API into doc/
2026-09-06 21461ee1046036c08d17a930dce220c445e5758f Merge branch 'docs/api-rendering': org docstrings in source + org-doc API pipeline
2026-09-06 2065321629ec28ca711ab5549e47a490a878c2c2 docs: document all 835 exported symbols; doc-coverage CI gate
2026-09-06 d156cab56fb2ca21b922ffe16d9ec2d1fae46c00 docs: regenerate API docs with lisp org babel language
2026-09-06 b1b6d16e9f31cc0cf0bd478b3a6f273341b22966 docs: org docstrings in source + org-doc API rendering pipeline
2026-09-06 04ebf29642eb97cae32511135760c2169ea5379e fix: preserve master test manifest during merge
2026-09-06 66535b1e3873f2da1f9970bd8b6d1a2ad70d0dc3 Merge master into fix/v09-false-value-pipeline
2026-09-06 d0be4b5fb5c7c61ea11c2a140c5854ee3a2c0b51 test: load JSON literal preservation regression
2026-09-06 7437b65edbd1b7f83383f12482ba1f421982e048 test: cover JSON false/null preservation
2026-09-06 89a8fa0939823f3ad3b68b54b176c44196146220 fix: restore canonical star-cl flake hash
```

## Repository paths changed, last 14 days

```text
.forgejo/workflows/doc-coverage.yml
.github/workflows/doc-coverage.yml
.github/workflows/operation-091-star-cl-sync.yml
.github/workflows/starintel-schema-lock.yml
.github/workflows/sync-operation-runtime-once.yml
.gitignore
Makefile
README.org
cli/client-convenience.lisp
cli/http-contract.lisp
doc/actors.org
doc/addons.org
doc/api/index.org
doc/api/star-actors-matcher.org
doc/api/star-actors.org
doc/api/star-auth.org
doc/api/star-authorization.org
doc/api/star-consumers.org
doc/api/star-databases-couchdb.org
doc/api/star-documents.org
doc/api/star-http-contract.org
doc/api/star-leases.org
doc/api/star-producers.org
doc/api/star-rabbit.org
doc/api/starintel-gserver-http-api.org
doc/api/starintel-gserver.org
doc/architecture.org
doc/configuration.org
doc/development.org
doc/document-spec.org
doc/http-api-docs.org
doc/http-auth-kv-lease-boundary.org
doc/http-auth-threat-model.org
doc/http-authentication-runtime.org
doc/http-authorization-runtime.org
doc/http-principal-capability-contract.org
doc/http-users.org
doc/index.org
doc/lease-store-usage.org
doc/messaging.org
doc/next-implementation-loop-prompt.org
doc/oauth-provider.org
doc/operation-object.org
doc/relation-deduplication.org
doc/server-admin.org
doc/target-lease-semantics.org
doc/testing.md
doc/v09-runtime.org
flake.lock
flake.nix
qlfile.lock
schema/starintel-schema.lock.json
scripts/check-starintel-schema-lock.py
scripts/doc-authoring.py
scripts/insert-docstrings.py
scripts/stack-test.sh
source/actor-systems/event-actor.lisp
source/actor-systems/matcher-actor.lisp
source/actors.lisp
source/actors/couchdb-service.lisp
source/addons.lisp
source/auth/core.lisp
source/auth/oauth.lisp
source/auth/store.lisp
source/auth/users.lisp
source/authorization/policy.lisp
source/authorization/services.lisp
source/consumers/consumers.lisp
source/consumers/owner-fixes.lisp
source/consumers/retry-policy.lisp
source/consumers/startup-retry.lisp
source/databases/couchdb.lisp
source/databases/document-update.lisp
source/databases/outbox.lisp
source/databases/quarantine.lisp
source/databases/target-acceptance.lisp
source/databases/view-registry.lisp
source/databases/view-request.lisp
source/document-access.lisp
source/frontends/http-api.lisp
source/frontends/http-auth.lisp
source/frontends/http-authorization-routes.lisp
source/frontends/http-boundary-core.lisp
source/frontends/http-boundary-routes.lisp
source/frontends/http-bulk-jobs.lisp
source/frontends/http-target-v1.lisp
source/gserver-settings.lisp
source/init-loader.lisp
source/leases/memory-store.lisp
source/leases/protocol.lisp
source/leases/valkey-store.lisp
source/main.lisp
source/producers/producers.lisp
source/rabbit.lisp
source/starintel-gserver.asd
source/target-dispatch.lisp
source/target-recovery.lisp
source/views/targets.json
starintel-gserver-tests.asd
t/consumers-test.lisp
t/http-boundary-test.lisp
t/http-target-tenant-test.lisp
t/http-target-v1-test.lisp
t/json-literal-preservation-test.lisp
t/run-tests.lisp
t/v09-runtime-test.lisp
t/valkey-lease-integration-test.lisp
t/valkey-lease-review-regression-test.lisp
tests/test_operational_salvage_contract.py
tests/test_v09_runtime_contract.py
ui/ui-server.lisp
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/doc-coverage.yml
.github/workflows/operation-091-star-cl-sync.yml
.github/workflows/starintel-schema-lock.yml
.github/workflows/sync-operation-runtime-once.yml
flake.nix
scripts/check-starintel-schema-lock.py
scripts/doc-authoring.py
scripts/insert-docstrings.py
scripts/stack-test.sh
source/starintel-gserver.asd
starintel-gserver-tests.asd
t/consumers-test.lisp
t/http-boundary-test.lisp
t/http-target-tenant-test.lisp
t/http-target-v1-test.lisp
t/json-literal-preservation-test.lisp
t/run-tests.lisp
t/v09-runtime-test.lisp
t/valkey-lease-integration-test.lisp
t/valkey-lease-review-regression-test.lisp
tests/test_operational_salvage_contract.py
tests/test_v09_runtime_contract.py
```
