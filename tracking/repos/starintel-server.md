# lost-rob0t/starintel-server

- generated: `2026-11-13T01:08:02Z`
- canonical branch: `master`
- changelog eligible: `yes`
- head: [`f50a441e1fcaad73277932195e05f2578eb972bf`](https://github.com/lost-rob0t/starintel-server/commit/f50a441e1fcaad73277932195e05f2578eb972bf)
- head date: `2026-11-12T16:41:59Z`
- head subject: Merge pull request 'fix(search): bounded public FTS reads with canonical revalidation (#420)' (#422) from fix/public-search-catchup-420 into master

## Git log, last 14 days

```text
2026-11-12 f50a441e1fcaad73277932195e05f2578eb972bf Merge pull request 'fix(search): bounded public FTS reads with canonical revalidation (#420)' (#422) from fix/public-search-catchup-420 into master
2026-11-12 c1cf84e1248faa2b3ad85c94a1193532566acc81 Merge pull request 'perf(ingest): eliminate redundant CouchDB outbox marker read' (#428) from perf/couchdb-ingest into master
2026-11-12 de4cfd579859178546c4bd5030bbac2cee613af1 perf(ingest): reuse persisted revision for outbox publication marker
2026-11-12 7abb040ada60d13e7d2174f9de84ca66ac16c309 Merge pull request 'fix(bulk): bound terminal job retention (GitHub #378)' (#421) from fix/378-terminal-bulk-retention into master
2026-11-12 8230a7cd708f6973eddaea5e30feee72be5bc9b2 fix(search): reject contradictory canonical tenant aliases (#420)
2026-11-12 976e87bf7acae3e90e06281840b911bc7bc73a1a chore: enable Mara/Star copilot opt-in [skip ci]
2026-11-11 7086bc62ef4901aa55af26a728f96e58e1356d8d chore: opt in to Mara and Star copilot reviews [skip ci]
2026-11-11 ed4f1faa2f859c6d9815a2f535db619abc2f0b54 fix(search): bound public FTS catch-up and revalidate current documents (#420)
2026-11-11 75c6dac2922b07db65ec29c9ed7fc51d9c876b85 fix(bulk): bound terminal job retention (#378)
2026-11-11 e08bd1f7ad01854a3a4866f04eae863423d6d8b8 Merge pull request 'fix(frontends): map admin user routes and self password change to explicit policy actions (#386)' (#419) from rage/386-admin-user-route-mapping into master
2026-11-11 f0f0875e0fe8f05dacebb5d741fd47e532e3d610 fix(frontends): map admin user routes and self password change to explicit policy actions (#386)
2026-11-11 024459c99065902f6eca07c1224cc0816c7a0bd4 Merge pull request 'fix(runtime): authenticate the couchdb readiness probe' (#417) from fix/couchdb-readiness-probe-auth into master
2026-11-11 02cb1f635e7a4cadc185006094318fb0f9ddc944 fix(runtime): authenticate the couchdb readiness probe
2026-11-11 b11d8ff79b533767354bd140f5f0312004729b59 Merge pull request 'fix(consumers): explicit queue topology ownership with contained mismatch startup (#385)' (#415) from rage/385-queue-topology-containment into master
2026-11-10 616aad8554a93430ef7be75dcab89e411aead382 fix(consumers): explicit queue topology ownership with contained mismatch startup (#385)
2026-11-11 1fd793fcd010bf08627bd1b25f5ec2091208ad59 Merge pull request 'feat(auth): creator/owner dimension for targets (#401)' (#412) from rage/401-owner-dimension into master
2026-11-10 0d5cc5c990fbbf108b42535be0eaf238228abfdc feat(auth): creator/owner dimension for targets (#401)
2026-11-05 427bcb7c865672fe289c43e55a6204dccbabb74e Merge pull request 'kb: #38 drain-resilience deployment knowledge' (#41) from kb/38-drain-resilience-ops into master
2026-11-04 c25b3b0f6b86005407827d8c5f7115d70865b92d Merge pull request #368 from lost-rob0t/issue-367-actor-option-hints
2026-11-04 6a2279a7e716f1e4a50150d37bc3a1f45ecca46d Advertise per-actor target option hints in the actor registry
2026-11-04 1c50aca55d8951d4f4fdbc7348c8f6e99cce551d Merge pull request 'Merge GitHub master (rage/59 target-update fixes) into canonical master' (#42) from sync/github-reconcile into master
2026-11-04 43682f81ac38f636e4b49b1d8d31193eb20a4813 Merge GitHub master (rage/59 target-update fixes) into canonical master
2026-11-04 d549650674723c1e1d85f6bbe492d261042e9393 kb: #38 drain-resilience deployment knowledge — upsert/quarantine/supervision contracts, 12-worker scaling, deploy-order and gate lessons
2026-11-04 6ea741e0f1583623ae9d26fcb9c88ee2a9066e82 Merge pull request 'kb: 2026-11-04 ingest backlog incident evidence (#37)' (#37) from kb/37-ingest-backlog-incident into master
2026-11-04 b42f9217d5bd8cddd4f4debbce5241d8c1623d0b Merge pull request #366 from lost-rob0t/rage/59-target-update-response
2026-11-04 bb8f61e39e59bf151d319daab999fcbc0a3f9405 Merge pull request 'fix(consumers): drain resilience — upsert, quarantine idempotency, supervised restart (#38)' (#39) from rage/38-drain-resilience into master
2026-11-04 cf820a31fe6af168109db8bab2b70a4c2001ad56 fix(targets): update route must return one JSON string body
2026-11-04 e7fdf906e97163b5538d4beca578e11815a51f5b docs(api): regenerate star-consumers + star-databases-couchdb reference (issue #38)
2026-11-04 dc74abfc8ec2bd864fdb7bb19b3033e063983b1d Merge pull request #365 from lost-rob0t/rage/59-target-update-fix
2026-11-04 2d113ec3aa8399fea4d04cca864db2b9ed988b87 fix(targets): authorized-save must bind the decision, not call it
2026-11-04 772421c0034a795df53fc08dcfde052fa5665847 fix(consumers): drain resilience — upsert re-observations, quarantine idempotency, supervised restart (issue #38)
2026-11-04 d0c08f5a1d7b823fe9e53d8f9ebc675ef62b53d0 Merge pull request #363 from lost-rob0t/rage/59-target-update
2026-11-04 4bf0dcd0b5f368201ce8d7beb3dc90bf558aae92 docs(api): regenerate for targets.update and target document store
2026-11-04 98f22360459b781de96c9cd628d8e11ef873def9 feat(targets): contracted targets.update for per-target options pinning (#59)
2026-11-04 dc81b63af149d62f7ec1746102ae7426c917cad7 kb: 2026-11-04 ingest backlog incident — settlement stop has no supervised restart (#37 evidence)
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
```

## Repository paths changed, last 14 days

```text
.copilot
.prolog/facts.kb
.prolog/kb/authorization-scope-dimensions.pl
.prolog/kb/bulk-jobs.pl
.prolog/kb/consumer-lifecycle.pl
.prolog/kb/index.pl
.prolog/kb/outbox-ingest.pl
.prolog/kb/public-api-tenancy.pl
.prolog/kb/root-causes.pl
.prolog/kb/tooling.pl
.prolog/result.json
.prolog/verify.pl
cli/http-contract-targets.lisp
doc/api/index.org
doc/api/star-actors.org
doc/api/star-authorization.org
doc/api/star-consumers.org
doc/api/star-databases-couchdb.org
doc/http-authorization-runtime.org
doc/public-search-catchup.md
docker-compose.yml
docker/couchdb-prometheus.ini
docker/otelcol-sidecar.yaml
nix/images.nix
source/actor-registry.lisp
source/actor-systems/event-actor.lisp
source/actors.lisp
source/authorization/package.lisp
source/authorization/policy.lisp
source/authorization/services.lisp
source/consumers/consumers.lisp
source/consumers/owner-fixes.lisp
source/consumers/package.lisp
source/consumers/rabbit-settlement.lisp
source/consumers/retry-policy.lisp
source/consumers/startup-retry.lisp
source/databases/outbox.lisp
source/databases/quarantine.lisp
source/databases/target-acceptance.lisp
source/databases/view-request.lisp
source/frontends/http-authorization-routes.lisp
source/frontends/http-authorization.lisp
source/frontends/http-bulk-jobs.lisp
source/frontends/http-capabilities.lisp
source/frontends/http-contract-routes.lisp
source/frontends/http-target-v1-auth.lisp
source/frontends/http-target-v1-route.lisp
source/frontends/http-target-v1.lisp
source/runtime-lifecycle.lisp
source/target-dispatch.lisp
source/target-recovery.lisp
source/target-repository.lisp
source/views/search.json
starintel-gserver-tests.asd
t/actor-registry-test.lisp
t/authorization-policy-test.lisp
t/consumers-test.lisp
t/couchdb-outbox-recovery-test.lisp
t/couchdb-view-literal-integration-test.lisp
t/couchdb-view-request-test.lisp
t/drain-resilience-test.lisp
t/event-actor-test.lisp
t/http-auth-test.lisp
t/http-boundary-test.lisp
t/http-capabilities-test.lisp
t/http-target-tenant-test.lisp
t/http-target-v1-test.lisp
t/run-tests.lisp
t/runtime-lifecycle-test.lisp
```

## Test and CI paths touched, last 14 days

```text
starintel-gserver-tests.asd
t/actor-registry-test.lisp
t/authorization-policy-test.lisp
t/consumers-test.lisp
t/couchdb-outbox-recovery-test.lisp
t/couchdb-view-literal-integration-test.lisp
t/couchdb-view-request-test.lisp
t/drain-resilience-test.lisp
t/event-actor-test.lisp
t/http-auth-test.lisp
t/http-boundary-test.lisp
t/http-capabilities-test.lisp
t/http-target-tenant-test.lisp
t/http-target-v1-test.lisp
t/run-tests.lisp
t/runtime-lifecycle-test.lisp
```
