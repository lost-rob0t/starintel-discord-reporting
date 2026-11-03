# lost-rob0t/starintel-server

- generated: `2026-11-03T06:53:23Z`
- canonical branch: `master`
- changelog eligible: `yes`
- head: [`091d74dd07fc9b13fbb820dc433b5f6585690626`](https://github.com/lost-rob0t/starintel-server/commit/091d74dd07fc9b13fbb820dc433b5f6585690626)
- head date: `2026-11-03T00:12:47-05:00`
- head subject: kb: steady-v2 portfolio live; paging + storage-revision fingerprint fixes verified

## Git log, last 14 days

```text
2026-11-03 091d74dd07fc9b13fbb820dc433b5f6585690626 kb: steady-v2 portfolio live; paging + storage-revision fingerprint fixes verified
2026-11-03 467e1b8e17491780700186eef758d71ece72427e Merge pull request 'fix(targets): storage revision must not break recurring rehydration (#360)' (#36) from issue-360-recovery-fingerprint into master
2026-11-02 5a2a14dbedfaa2d246d9326a13b4d1f05922f255 fix(targets): storage revision must not break recurring rehydration (#360)
2026-11-03 cd3085429feeaf38a3882c17f3e162769848a4ac Merge pull request 'fix(targets): drain every by_actor page in recovery and listing (#360)' (#35) from issue-360-recovery-paging into master
2026-11-02 10b8191bf5d2d1dbe264b77ca807b5f19f7291b5 fix(targets): drain every by_actor page in recovery and listing (#360)
2026-11-02 c5b474b4b1e63b72b00f168cd9cc66603b2b563f kb: record #360 production rollout evidence and known limitations
2026-11-03 c4e8c875e6d90ef754f6a27fb991431ceea1f479 Merge pull request 'fix(targets): recovery rehydrates recurring schedules only; per-record invalids cannot abort boot (#360)' (#34) from issue-360-recovery-resilience into master
2026-11-02 b89fbc3050135bca2f49889ca9276eddb1cc205a docs(api): regenerate star-actors recover-target-record docstring
2026-11-02 c6a206e1f25eea1509ef0d16fff31f7a215aefe5 fix(targets): recovery rehydrates recurring schedules only; per-record invalids cannot abort boot (#360)
2026-11-03 92bc895e5928767e9dff40d5645be2343200b399 Merge pull request 'fix(targets): durable recurring schedules survive restart via boot rehydration (#360)' (#33) from issue-360-target-rehydration into master
2026-11-02 eddfc47137413aa911216d8d6a7568b7451f1668 docs(api): regenerate star-consumers run-consumer docstring (issue #37)
2026-11-02 e6711fb516f0616fd082f80baa8f1c66c7789ee6 fix(targets): durable recurring schedules survive restart via boot rehydration (#360)
2026-10-31 55deeee3aa6ff7141279562dabba071c2feeb025 Merge pull request #358 from lost-rob0t/fts-default-field
2026-10-31 dd5c41c596652281cf32de4db693b4c09a9a42af fts: index document text into the Lucene default field
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
```

## Repository paths changed, last 14 days

```text
.forgejo/workflows/public-read-boundary.yml
.prolog/facts.kb
.prolog/kb/consumer-lifecycle.pl
.prolog/kb/index.pl
.prolog/kb/public-api-tenancy.pl
.prolog/kb/root-causes.pl
.prolog/kb/tooling.pl
.prolog/result.json
.prolog/verify.pl
cli/http-contract-targets.lisp
doc/api/star-actors.org
doc/api/star-consumers.org
doc/api/star-databases-couchdb.org
doc/public-read-boundary.org
docker-compose.yml
docker/couchdb-prometheus.ini
docker/otelcol-sidecar.yaml
nix/images.nix
source/actors.lisp
source/databases/target-acceptance.lisp
source/databases/view-request.lisp
source/frontends/http-authorization-routes.lisp
source/frontends/http-contract-routes.lisp
source/frontends/http-target-v1-auth.lisp
source/frontends/http-target-v1-route.lisp
source/runtime-lifecycle.lisp
source/target-dispatch.lisp
source/target-recovery.lisp
source/target-repository.lisp
source/views/data.json
source/views/search.json
t/consumers-test.lisp
t/couchdb-view-literal-integration-test.lisp
t/couchdb-view-request-test.lisp
t/http-capabilities-test.lisp
t/http-public-api-integration-test.lisp
t/http-target-tenant-test.lisp
t/http-target-v1-test.lisp
t/runtime-lifecycle-test.lisp
```

## Test and CI paths touched, last 14 days

```text
t/consumers-test.lisp
t/couchdb-view-literal-integration-test.lisp
t/couchdb-view-request-test.lisp
t/http-capabilities-test.lisp
t/http-public-api-integration-test.lisp
t/http-target-tenant-test.lisp
t/http-target-v1-test.lisp
t/runtime-lifecycle-test.lisp
```
