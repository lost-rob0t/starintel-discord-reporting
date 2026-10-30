# lost-rob0t/starintel-server

- generated: `2026-10-30T23:51:11Z`
- canonical branch: `master`
- changelog eligible: `yes`
- head: [`f97596b0a63c9a0184fcc813bb3783e3df31eb9c`](https://github.com/lost-rob0t/starintel-server/commit/f97596b0a63c9a0184fcc813bb3783e3df31eb9c)
- head date: `2026-10-30T19:28:08-04:00`
- head subject: Merge pull request #357 from lost-rob0t/rage/37-consumer-reconnect

## Git log, last 14 days

```text
2026-10-30 f97596b0a63c9a0184fcc813bb3783e3df31eb9c Merge pull request #357 from lost-rob0t/rage/37-consumer-reconnect
2026-10-30 eedf8440ea424a84f32926c0364c1c2c8e1fbc0d fix(consumers): bounded transport reconnect in run-consumer (issue #37)
2026-10-30 630e97898e7361ed2557212523789e1d050adafc fix(consumers): reopen stream at top of each reconnect session; repair paren/declare placement
2026-10-30 1a34b3908eef049bc4dd10f0d5bd7eb8848f5dc8 fix(consumers): classify reconnect by origin, not condition name
2026-10-30 9da03504fb902b1e2a848b70a3753a7d803a8a34 kb: consumer reconnect root cause, invariants, ingest-host and prod-couchdb tooling (issue #37 slice)
2026-10-30 1475bd8911fd1a1487df1c4bcc3b0dd165e5f50b Raise RabbitMQ consumer_timeout to 4h in the compose stack
2026-10-30 c91b0b2ebed24ea0c50a3368aeea06a3aef92955 Add CouchDB Prometheus metrics and drop starintel.internal domainnames
2026-10-24 16d3fbc0061e672e82053e2ba8c1711889e2cf1d Merge pull request 'Record public stats count mismatch in project KB' (#31) from public-test-stats-kb into master
2026-10-24 bdd9457c8751b8c8507daf53430b422218be4e92 Record public stats count mismatch
2026-10-24 89ecaf22851231acb471ddbf8f109f56898c156f Merge pull request 'Record future own-plus-public user tenant contract' (#29) from docs-user-tenant-scope-contract into master
2026-10-24 839c03c0cedd3876348c01bb9a479552d8e787dd Document future authenticated tenant read scope
2026-10-24 d4a2e2f600286661ebc014fef5270f7925643ef1 Merge pull request 'Scope anonymous reads to public tenant and approved datasets' (#27) from fix/public-tenant-read-boundary into master
2026-10-24 76be395de8179b0ee0fa9b4c10f944504077818c Scope anonymous reads to public tenant and approved datasets
2026-10-20 b5d60e3e452c39e7f6a195aa28d73c5ed2163e9c Merge pull request #345 from lost-rob0t/agent/issue-343-isolation
2026-10-20 23947111fdbf086850762d3b04666b54c1b1118d fix: bound authenticated search query text before backend work
2026-10-19 25d65c592a4c01f023db3c0f6388259180bd7b72 Merge pull request #346 from lost-rob0t/agent/issue-343-recovery
2026-10-19 3fd63b6392f2e9d64f59b0476f3c23fb7be1f8cc Merge pull request #347 from lost-rob0t/agent/issue-343-release
2026-10-20 d7d7f584cb70ee1d7f98abbdbf2c620fabf15847 test: reproduce unbounded authenticated search query for #343
2026-10-20 a6033c10b08cf73ba074a0ead340ba6318dd5b00 Require durable retry and forced-crash release proof (#343)
2026-10-20 2bd4af744aa88c2d61ab105b21d3ee791a4bc747 docs(recovery): record real clean-instance CouchDB drill
2026-10-20 87dca5d0162e2ffa289066f0159834722b119890 Require sustained soak and concrete release subproofs (#343)
2026-10-20 04c82f6fc6922c575aa0bf822d98204811535b7d Guard release evidence and stop mutable version publication (#343)
2026-10-20 f879f021b1200e79f7c6f739a01c851c0e4f507f test: add private tenant readiness probe for #343
2026-10-20 a090b7877926a15977fa7233bd30d8bda4a0873c test(recovery): add fail-closed synthetic restore drill for #343
2026-10-19 87d78a1a3a7a649d836c5049b4228f33aeb51631 Merge pull request 'Add scoped actor credential resolver plugin' (#22) from feat/actor-credentials-plugin into master
2026-10-19 e298c6f7ca154de5280f98192d8503fa949e5b97 Merge pull request 'Add scoped actor credential resolver plugin' (#22) from feat/actor-credentials-plugin into master
2026-10-19 da12b5705248ec13bf828e32ea53985fb0aee01c Expose Nix to Forgejo doc coverage steps
2026-10-19 88aef7b6ed22d2da42fd7051013fb0cea218dce9 Expose Nix to Forgejo doc coverage steps
2026-10-19 e97258f7c08dab2bbbb2631ca652bd1238250a0c Document exported credential contract helpers
2026-10-19 7ae3a1671119676bc11ec2816a8b8a34427a70a5 Document exported credential contract helpers
2026-10-19 9840a43d0ce80d072fe733600d1a81c39980b7cc Add scoped actor credential resolver add-on
2026-10-19 1182580df70d9b125e6972be1459c7c716af6ecd Add scoped actor credential resolver add-on
```

## Repository paths changed, last 14 days

```text
.forgejo/workflows/doc-coverage.yml
.forgejo/workflows/public-read-boundary.yml
.github/workflows/docker.yml
.prolog/facts.kb
.prolog/kb/actor-credentials.pl
.prolog/kb/consumer-lifecycle.pl
.prolog/kb/index.pl
.prolog/kb/public-api-tenancy.pl
.prolog/kb/tooling.pl
.prolog/result.json
.prolog/verify.pl
addons/actor-credentials/actor-credentials.lisp
addons/actor-credentials/package.lisp
cli/http-contract-package.lisp
cli/http-contract.lisp
doc/actor-credentials.org
doc/api/index.org
doc/api/star-authorization.org
doc/api/star-http-contract.org
doc/api/starintel-gserver-http-api.org
doc/production-isolation.md
doc/production-recovery.md
doc/production-release.md
doc/public-read-boundary.org
docker-compose.yml
docker/couchdb-prometheus.ini
docker/otelcol-sidecar.yaml
flake.nix
nix/images.nix
scripts/readiness_isolation.py
scripts/readiness_recovery.py
scripts/readiness_release.py
source/authorization/policy.lisp
source/frontends/http-authorization-routes.lisp
source/frontends/http-authorization.lisp
source/frontends/http-contract-routes.lisp
source/package.lisp
source/runtime-lifecycle.lisp
source/views/data.json
starintel-actor-credentials.asd
starintel-gserver-tests.asd
t/actor-credentials-test.lisp
t/consumers-test.lisp
t/http-auth-test.lisp
t/http-capabilities-test.lisp
t/http-public-api-integration-test.lisp
t/run-tests.lisp
tests/test_readiness_isolation.py
tests/test_readiness_recovery.py
tests/test_readiness_release.py
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/docker.yml
flake.nix
scripts/readiness_isolation.py
scripts/readiness_recovery.py
scripts/readiness_release.py
starintel-actor-credentials.asd
starintel-gserver-tests.asd
t/actor-credentials-test.lisp
t/consumers-test.lisp
t/http-auth-test.lisp
t/http-capabilities-test.lisp
t/http-public-api-integration-test.lisp
t/run-tests.lisp
tests/test_readiness_isolation.py
tests/test_readiness_recovery.py
tests/test_readiness_release.py
```
