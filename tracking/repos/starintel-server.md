# lost-rob0t/starintel-server

- generated: `2026-09-08T16:41:05Z`
- canonical branch: `master`
- changelog eligible: `yes`
- head: [`4721efaf8141fd7199b6e1ceb1011b9ad970796e`](https://github.com/lost-rob0t/starintel-server/commit/4721efaf8141fd7199b6e1ceb1011b9ad970796e)
- head date: `2026-09-06T20:00:59-04:00`
- head subject: Merge pull request #145 from lost-rob0t/fix/target-dispatch-data-shape

## Git log, last 14 days

```text
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
2026-08-29 204fa0d0376772bd3586e56a6912bb9a739eb0b0 fix: preserve JSON false/null through the document pipeline
2026-08-29 8fb297d146e7332fae7e38170b5b49d49530ac53 Merge pull request #132 from lost-rob0t/agent/emacs-client-contract
2026-08-29 3768df68dc0172c64fa803d6e10c285d1f84d3b0 feat: rewrite emacs client as async contract layer with ERT suite
2026-08-28 e99aadd3f44505bc692708aad5e34ab0c4ab0036 Approve v0.9 runtime implementation conformance
2026-08-28 0caed07ff6ca31ca488c369c79fb1c1a8ff0f78d Merge pull request #127 from lost-rob0t/rage/59-target-create-v1
2026-08-25 38666dab3610bd7771fa1c8ab3bbe67ebad0b594 fix: default Bixby operations to canonical target scope
2026-08-25 b2b5c58ca1931ff19d41a5fa90ae609edb2d78bb build: share target create contract with clients
2026-08-25 c62a714fd168d380ccdce86c050967b53747f644 fix: close target fingerprint form correctly
2026-08-25 e047d5c51d2b04ee00becdab7edc79012ed23c4f build: load v1 target route
2026-08-25 d151cc2293a89d0c8088b65dc0bd91d594631f0a feat: serve generic target creation endpoint
2026-08-25 04b932a6cf63527fa877c8343c76534f19132ade build: load target authorization extension
2026-08-25 e59433012b471440f79724219c897d006afa529d auth: scope v1 target creation
2026-08-25 abf701ec35f76f3145de881f7ebe9dbf646660fd build: load target create contract
2026-08-25 0817f7bd4c2571856d2c6d10a03388dbe59d3827 feat: contract generic target creation
2026-08-25 ea8ac9481cf71705a5aa18c3da1e01a3b38ee11b build: load generic v1 target boundary
2026-08-25 3f1804a7ae33dd696c81fa931f7746626c1ffb5e feat: add generic v1 target request helpers
2026-08-25 ce819cb538390af5b619e651fae42af9a6b37d63 fix: fingerprint full target semantics
2026-08-25 68f6edb74904731053d0ca1e80395831cb873a12 test: require v1 target suite in hermetic gate
2026-08-25 3f22edce2ffd7e8ab244fc61e6c79c49764d2320 test: require Bixby plug-in to use canonical core scopes
2026-08-25 01a1b921717749e7fff95ce369ca10db1e688f64 test: refine v1 target idempotency around durable request ledger
2026-08-25 cec80fe9e59ccebec767c8cc99a35a30505e071d test: load v1 target creation contract
2026-08-25 156df4eac0a476e7caf65944832414ebdc2af3df test: specify idempotent v1 target creation boundary
```

## Repository paths changed, last 14 days

```text
.forgejo/workflows/doc-coverage.yml
.github/workflows/doc-coverage.yml
.gitignore
Makefile
README.org
addons/bixby/bixby.lisp
cli/client-convenience.lisp
cli/http-contract-targets.lisp
cli/http-contract.lisp
cli/starintel-gserver-client.asd
client-test.el
client.el
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
doc/relation-deduplication.org
doc/server-admin.org
doc/target-lease-semantics.org
doc/testing.md
doc/v09-runtime.org
docs/v09-runtime.org
flake.lock
flake.nix
scripts/doc-authoring.py
scripts/insert-docstrings.py
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
source/consumers/retry-policy.lisp
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
source/frontends/http-target-v1-auth.lisp
source/frontends/http-target-v1-route.lisp
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
source/target-dispatch-fixes.lisp
source/target-dispatch.lisp
source/target-recovery.lisp
starintel-gserver-tests.asd
t/addon-system-test.lisp
t/http-boundary-test.lisp
t/http-target-v1-test.lisp
t/json-literal-preservation-test.lisp
t/run-tests.lisp
t/v09-runtime-test.lisp
t/valkey-lease-integration-test.lisp
tests/test_operational_salvage_contract.py
tests/test_v09_runtime_contract.py
ui/ui-server.lisp
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/doc-coverage.yml
cli/starintel-gserver-client.asd
flake.nix
scripts/doc-authoring.py
scripts/insert-docstrings.py
source/starintel-gserver.asd
starintel-gserver-tests.asd
t/addon-system-test.lisp
t/http-boundary-test.lisp
t/http-target-v1-test.lisp
t/json-literal-preservation-test.lisp
t/run-tests.lisp
t/v09-runtime-test.lisp
t/valkey-lease-integration-test.lisp
tests/test_operational_salvage_contract.py
tests/test_v09_runtime_contract.py
```
