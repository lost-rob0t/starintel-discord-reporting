# lost-rob0t/starintel-server

- generated: `2026-09-20T22:29:01Z`
- canonical branch: `master`
- changelog eligible: `yes`
- head: [`f899612d6e5924ffcc81432d78541b6616311892`](https://github.com/lost-rob0t/starintel-server/commit/f899612d6e5924ffcc81432d78541b6616311892)
- head date: `2026-09-19T02:14:21-04:00`
- head subject: docs: define source actor and target protocols

## Git log, last 14 days

```text
2026-09-19 f899612d6e5924ffcc81432d78541b6616311892 docs: define source actor and target protocols
2026-09-16 e49c67d88d60dbcc0fcba1b4ba76c1a0a6d6655c observability: audit search queries and wire hosted telemetry
2026-09-16 61499b8509e6f7c7bb6c0ac54248d1f99863fc99 fix: keep observability transport installation idempotent
2026-09-16 cd4546871543f6a314fb2eafe901417935042166 observability: pass explicit gate and sidecar endpoint into server
2026-09-16 5a2cb973ceb82c44b61d1419e4ed8a20d11b0c0e test: call hosted observability helper as internal seam
2026-09-16 3d09cdad7ea235524abd3a9dfd9a9454a203756f test: cover hosted observability autoload gate
2026-09-16 e00d4ad79d291134dfcea5e77b847c704b93c31c docs: describe hosted observability autoload gate
2026-09-16 b88a1d39c34302d2f74a27dfade68f798e131f8b observability: autoload addon for explicit hosted opt-in
2026-09-16 0ab34b42e9fc47e9c373d868451e3f7dff1c4ac4 docs: define search query audit telemetry
2026-09-16 ead99ef657f7d5d5235b6993b1481d483016098d test: cover search query audit events
2026-09-16 6ca67e4328ac7514256594ea3562a4913161a4c2 observability: audit every authorized search query entry
2026-09-16 414bfba309e2c7de8a40e2625458a7c806ebbf08 observability: make telemetry export explicit opt-in
2026-09-16 1ac298b797bd4bc0e71cfde083c6a59af55ccc6f Merge pull request #190 from lost-rob0t/fix/189-release-terminal-bulk-payloads
2026-09-16 5d22fc362259d21d4c18d1fa3e5b7511b797f426 Regenerate bulk job API reference
2026-09-16 7c2e839ab99e081970c2cd71801ab49ca7c5ed7e Release terminal bulk job request payloads
2026-09-16 d48fa939402abf701fa1cc4079dfb8bedfad8d4a Merge pull request #188 from lost-rob0t/fix/187-concurrent-ulid-quarantine
2026-09-16 ace720b1dbe4be0139b5f52ea3ab6d0a1f5e3038 test: prove concurrent quarantine IDs are distinct
2026-09-16 b0dab216b40952e5eaba30632a16cf327c154638 kb: correct loader invocation
2026-09-16 6f428549f6a62b2ea75b37f8ee6004e30215151b kb: preserve shared predicates across focused files
2026-09-16 72e784c87673737e7c68d55ba74dc12989dfefa4 kb: record quarantine collision and safe bulk reconciliation
2026-09-16 8c7d6e1969ce7a57b9b0295ff995ba7fb756551b docs: regenerate API reference for ULID helper
2026-09-16 7ab5e79acce842352380ffad659b4844a254675d docs: document synchronized ULID helper
2026-09-16 d90a9f762df12891fca9bcd54e0182cb5b9e219d fix: serialize server ULIDs and contain settlement failures
2026-09-16 d4e8447c6049eaed65a93e81668ae1ec4b65c25c Merge verified Prolog shard actor deployment (#186)
2026-09-16 d984f1308655cafdebf44b57cb86669cbcd87c29 Install pinned YAML parser for deployment contract tests
2026-09-16 94ff88d421abe795882ecd6f289f38dbf61550f7 Wire persistent Prolog shard actor into existing actor deployment
2026-09-14 60191023ac73bcc719fd550d6788322a95c92bc0 Merge pull request #184 from lost-rob0t/fix/docs-starintel-0.9.1-terminology
2026-09-14 aee5e5b61931fe13994238961e97b34b1feef735 docs(spec): distinguish 0.9.1 release from v0.9 wire schema
2026-09-14 d94922d21c65f0c0a2c35f0eacaf9beb727e656a Merge pull request #181 from lost-rob0t/feat/ingest-tenant-adapter
2026-09-14 136d182e28c9ebea74d2b78ab6d606e355e32f14 ci: remove temporary PR hardening workflow
2026-09-14 6af2600f869db9856030e137d6995a4ff49b4762 fix: authorize persisted tenant before egress redaction
2026-09-14 44dc21e511a7f376defdc97d98de6a4fe2aa7512 ci: fix temporary hardening workflow syntax
2026-09-14 593720a2233467bb9652e5f30f0293e3ccbc4395 ci: harden PR 181 authorization ordering
2026-09-14 7cea12d857965c4816fd804364569a66a1256818 docs: regenerate API reference with org-doc
2026-09-14 a7315ecd5e864e0b35373ba187195b3a6b055785 ci: temporary org-doc sync for PR 181
2026-09-14 2a1e400191c3f06dc7eca8355f37d0500d524561 fix: strip tenant across FTS fields and outbox payloads (#180)
2026-09-14 00b6f51dee23a7339f2398ed2e5739fb72b941ef fix: redact tenant from FTS fields and outbox payloads on egress (#180)
2026-09-14 d5bfa0ae4c875f757545c79a0d45056c593bd0bc fix: tolerate raw JSON strings when stripping tenant on egress (#180)
2026-09-14 19bc77e8139eb52dfef7d9705b2bbea69a7cbc5e test: cover consumer tenant exemption with canonical encoder (#180)
2026-09-14 e0cd015da368a6c9aa477066d417bb4895abd449 fix: exempt server-injected tenant_id from consumer strict validation (#180)
2026-09-14 2dc861b1800e9084f28202614df99bd252b4d1e2 fix: apply STAR_TENANT_* from runtime env in server init (#180)
2026-09-14 b9124e1ae2cef8bca7d27a75bda7a0dd59c87361 feat: wire STAR_TENANT_* through compose and treat empty env as unset (#180)
2026-09-14 507d2e4d5a2f21e12515de930ccaf138677a554e feat: inject tenant_id server-side before MQ/DB and redact it on egress (#180)
2026-09-14 fb9401f227cc90b7c9fb5ae3e3a5cc9edc1d06a1 agents: require StarIntel schema lock preflight
2026-09-14 1631854bead966de5b2d31b047c9e7e4a966cb53 feat: server-side tenant adapter for tenant-less documents (#180)
2026-09-14 7602e3432087dd052e25b4d3fe735c603a82e034 Merge pull request 'chore: record reconciliation evidence; prune merged mirror branches' (#16) from chore/reconcile-evidence into master
2026-09-14 f8e20c0b5629a34580c937a5e9ec56834e324802 chore: record reconciliation evidence; prune merged mirror branches
2026-09-14 51713d561b06a24f2954e8aa37a8339329c3a435 Merge pull request 'fix: treat running no-healthcheck containers as healthy in stack wait' (#15) from fix/stack-wait-no-healthcheck into master
2026-09-14 160df606a3fd9e909439748be0aa22fc364c9218 fix: treat running no-healthcheck containers as healthy in stack wait
2026-09-14 c3c6f154fbdab865fce69c3b1491ccee18593afb Merge pull request 'fix: use env: provider syntax in otelcol gateway endpoint' (#14) from fix/otelcol-env-syntax into master
2026-09-14 17bc37168ddea01f97236d5a5ef167f79d9b77a2 fix: use env: provider syntax in otelcol gateway endpoint
2026-09-14 99937377c23b81596df034836cc39d045ac34974 Merge pull request 'fix: drop duplicate healthcheck key in docker-compose' (#13) from fix/compose-duplicate-healthcheck into master
2026-09-14 09b236bffdfee147fcb94e508086175afd7fc1c4 fix: drop duplicate healthcheck key in docker-compose server service
2026-09-14 e4ba2f63d344169e07ffb00d353ddfbad3127cb8 Merge pull request 'Reconcile master divergence (merge github mirror) + fix ingest observability path' (#12) from reconcile/master-2026-09-14 into master
2026-09-14 cca6b600992bfa8dedf507e4cff386187e29ec73 chore: track .prolog verification and KB state
2026-09-14 448a0ffb86f3c62ebcd29e51c222d25bfd222a4f fix: qualify observability-active-p for the actor publish path
2026-09-14 1599100ec1c9267d773573fdd9d679d00791106c Merge github/master to reconcile master divergence
2026-09-14 f8caa4dfd5c6bc32be1e621a9ed27bcba7339dc5 Merge pull request #178 from lost-rob0t/chore/opencode-issue-loop-2026-09-14
2026-09-14 bac77beb382242582c61e56bc3d37934f070dd19 chore: add YAGNI issue voter
2026-09-14 1858494c6f54e875d6e6ae985dc952596193a505 chore: add issue verification voter
2026-09-14 844d335182a618a81e94864900aced7434a21056 chore: add issue research voter
2026-09-14 53916dd742b64217ee05c8a9ee3fa7f5703813ff chore: add issue ownership voter
2026-09-14 e3904855f2e46c200e83a7677169e2bae49d3113 chore: add issue reality voter
2026-09-14 9ee741aae5fc87143b65d0122db5bbef989cc1e8 chore: add OpenCode issue loop command
2026-09-14 8033fad2c6094c1d84700cc2c3f22db90e86a312 chore: add issue-first agent contract
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
2026-09-11 8533dc40943dc7230b62533458e287a58db527ce Merge pull request 'leases: wire the Valkey lease store into the runtime with the observability metrics hook' (#11) from feat/valkey-lease-runtime into master
2026-09-11 5a753c4498645ad829c0181dd061fd2d14d1f9f3 leases: wire the Valkey lease store into the runtime with the observability metrics hook
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
2026-09-11 15a417102881f216e0fe8977d2e95af4a71dd603 Merge pull request 'observability: StarIntel telemetry abstraction + OTLP instrumentation (addon, opt-in)' (#9) from feat/observability-slice into master
2026-09-10 bc64bd02fd6c469946ec518e9c42abd9e6724b32 docs: regenerate API reference for the observability systems
2026-09-10 87622e0c9d1f9a5184a062b5d58f6cfaecb6d67d observability: StarIntel telemetry abstraction + OTLP instrumentation
2026-09-09 d62c8a8cc50a1ec7dde395d0e84180ed0e109e4f Merge pull request 'Staging stack: youtube-actor service (actors profile) + image build target' (#7) from rage/staging-youtube-actor into master
2026-09-09 b79094ebce6560d863cc7a2ccef1209d86da5028 Add starintel-youtube actor service to the staging stack (actors profile)
2026-09-09 73de00962f532b1d75e5b862937e71f9b9cdb280 Merge pull request 'Contract versioned document operations (registry-first) + fix /dataset-size shadowing' (#6) from rage/5-http-contract-documents into master
2026-09-09 f2ee0ca8cb8a120c7d96a4e1cb639b508f692622 docs: per-run integration provisioning decision (operator convention)
2026-09-08 273e70309fa633fc40fe6b0e69e0c4002e368279 docs: record exact-head gate evidence in RAGE run log
2026-09-08 972da6a8d325464bc4df4e18f5b1a9b139307b66 feat: contract versioned document operations + fix /dataset-size shadowing
2026-09-06 4721efaf8141fd7199b6e1ceb1011b9ad970796e Merge pull request #145 from lost-rob0t/fix/target-dispatch-data-shape
2026-09-06 9d80cc1710cfe2a5c62c54fc8a2a23b9b7c564f3 fix: emit v0.9-valid data.*-shaped target documents from both routes
```

## Repository paths changed, last 14 days

```text
.github/workflows/operation-091-star-cl-sync.yml
.github/workflows/operational-salvage.yml
.github/workflows/starintel-schema-lock.yml
.github/workflows/sync-operation-runtime-once.yml
.github/workflows/tmp-org-doc-sync.yml
.gitignore
.opencode/agents/issue-ownership.md
.opencode/agents/issue-reality.md
.opencode/agents/issue-research.md
.opencode/agents/issue-verification.md
.opencode/agents/issue-yagni.md
.opencode/commands/issue.md
.prolog/facts.kb
.prolog/kb/bulk-jobs.pl
.prolog/kb/git-remotes.pl
.prolog/kb/index.pl
.prolog/kb/root-causes.pl
.prolog/kb/tooling.pl
.prolog/kb/ulid-quarantine.pl
.prolog/result.json
.prolog/runs/run-09b236bffdfee147fcb94e508086175afd7fc1c4.pl
.prolog/runs/run-1599100ec1c9267d773573fdd9d679d00791106c.pl
.prolog/runs/run-160df606a3fd9e909439748be0aa22fc364c9218.pl
.prolog/runs/run-17bc37168ddea01f97236d5a5ef167f79d9b77a2.pl
.prolog/runs/run-3e1f78523f377a94f43fda7a3cc1fc6622d7269d.pl
.prolog/runs/run-4721efaf8141fd7199b6e1ceb1011b9ad970796e.pl
.prolog/runs/run-51713d561b06a24f2954e8aa37a8339329c3a435.pl
.prolog/runs/run-81d500c412f69b96a917173326a4b5b0929dd09d.pl
.prolog/runs/run-8533dc40943dc7230b62533458e287a58db527ce.pl
.prolog/runs/run-cca6b600992bfa8dedf507e4cff386187e29ec73.pl
.prolog/runs/run-d62c8a8cc50a1ec7dde395d0e84180ed0e109e4f.pl
.prolog/runs/run-e4ba2f63d344169e07ffb00d353ddfbad3127cb8.pl
.prolog/verify.pl
AGENTS.md
Makefile
README.org
cli/http-contract-documents.lisp
cli/http-contract-final.lisp
cli/http-contract-package.lisp
cli/http-contract.lisp
cli/starintel-gserver-client.asd
doc/api/index.org
doc/api/star-actors.org
doc/api/star-consumers.org
doc/api/star-http-contract.org
doc/api/star-ids.org
doc/api/star-leases.org
doc/api/star-rabbit.org
doc/api/starintel-gserver-http-api.org
doc/api/starintel-gserver.org
doc/configuration.org
doc/http-api-docs.org
doc/lease-store-usage.org
doc/observability.org
doc/operation-object.org
doc/v09-runtime.org
docker-compose.yml
docker/otelcol-sidecar.yaml
docker/star-server-init.lisp
docs/prolog-shard-actor.org
example_configs/init.lisp
flake.lock
flake.nix
qlfile.lock
rage/5-http-contract-documents.org
schema/starintel-schema.lock.json
scripts/check-starintel-schema-lock.py
scripts/stack-test.sh
source/actor-systems/event-actor.lisp
source/actors.lisp
source/auth/core.lisp
source/auth/oauth.lisp
source/authorization/policy.lisp
source/authorization/services-final.lisp
source/authorization/services.lisp
source/consumers/consumers.lisp
source/consumers/owner-fixes.lisp
source/consumers/retry-policy.lisp
source/consumers/startup-retry.lisp
source/document-access.lisp
source/frontends/http-api.lisp
source/frontends/http-auth.lisp
source/frontends/http-authorization-routes.lisp
source/frontends/http-authorization.lisp
source/frontends/http-boundary-core.lisp
source/frontends/http-boundary-routes.lisp
source/frontends/http-bulk-jobs.lisp
source/frontends/http-capabilities.lisp
source/frontends/http-contract-routes.lisp
source/frontends/http-target-v1.lisp
source/gserver-settings.lisp
source/ids.lisp
source/lease-store-runtime.lisp
source/leases/memory-store.lisp
source/leases/valkey-store.lisp
source/observability-consumers.lisp
source/observability-gserver.lisp
source/observability/api.lisp
source/observability/config.lisp
source/observability/http-middleware.lisp
source/observability/otlp.lisp
source/observability/package.lisp
source/observability/redaction.lisp
source/observability/trace.lisp
source/package.lisp
source/rabbit.lisp
source/runtime-lifecycle.lisp
source/starintel-gserver.asd
source/target-dispatch.lisp
source/views/targets.json
starintel-gserver-tests.asd
starintel-observability.asd
t/addon-system-test.lisp
t/authorization-policy-test.lisp
t/authorization-services-final-test.lisp
t/consumers-test.lisp
t/http-boundary-test.lisp
t/http-contract-documents-test.lisp
t/http-target-tenant-test.lisp
t/http-target-v1-test.lisp
t/http-tenant-injection-test.lisp
t/lease-store-runtime-test.lisp
t/observability-test.lisp
t/run-tests.lisp
t/v09-runtime-test.lisp
t/valkey-lease-integration-test.lisp
t/valkey-lease-review-regression-test.lisp
tests/test_prolog_shard_deployment.py
tests/test_v09_runtime_contract.py
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/operation-091-star-cl-sync.yml
.github/workflows/operational-salvage.yml
.github/workflows/starintel-schema-lock.yml
.github/workflows/sync-operation-runtime-once.yml
.github/workflows/tmp-org-doc-sync.yml
cli/starintel-gserver-client.asd
flake.nix
scripts/check-starintel-schema-lock.py
scripts/stack-test.sh
source/starintel-gserver.asd
starintel-gserver-tests.asd
starintel-observability.asd
t/addon-system-test.lisp
t/authorization-policy-test.lisp
t/authorization-services-final-test.lisp
t/consumers-test.lisp
t/http-boundary-test.lisp
t/http-contract-documents-test.lisp
t/http-target-tenant-test.lisp
t/http-target-v1-test.lisp
t/http-tenant-injection-test.lisp
t/lease-store-runtime-test.lisp
t/observability-test.lisp
t/run-tests.lisp
t/v09-runtime-test.lisp
t/valkey-lease-integration-test.lisp
t/valkey-lease-review-regression-test.lisp
tests/test_prolog_shard_deployment.py
tests/test_v09_runtime_contract.py
```
