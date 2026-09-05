# lost-rob0t/starintel-server

- generated: `2026-09-05T10:40:03Z`
- canonical branch: `master`
- changelog eligible: `yes`
- head: [`8fb297d146e7332fae7e38170b5b49d49530ac53`](https://github.com/lost-rob0t/starintel-server/commit/8fb297d146e7332fae7e38170b5b49d49530ac53)
- head date: `2026-08-29T06:43:04-04:00`
- head subject: Merge pull request #132 from lost-rob0t/agent/emacs-client-contract

## Git log, last 14 days

```text
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
2026-08-25 52948721d8981e9aa5ccad4efd77185e52af845b Merge pull request #119 from lost-rob0t/agent/v09-canonical-runtime-cutover
2026-08-25 922bda3c8bb346b4eb1700281417d7a018253621 test: separate canonical and legacy HTTP fixtures
2026-08-25 2d6d88dbc188f64fcf76b53a8411b576b62c6a44 fix: correct star-cl flake nar hash
2026-08-25 69b8a03d4d152c5015f500f3b59334d6177731ce feat: enforce canonical v0.9 runtime boundaries
2026-08-24 4f2f70126bc59e18681844019460a33709e1eba6 Merge PR #118: core OAuth provider plus reload-safe Bixby add-on
2026-08-24 2c00cda2f2f18424a2279b933322235fee4b15c6 docs: clarify ASDF-safe add-on reload semantics
2026-08-24 bb15a1a0e9f7975fd06d35ae6aa3b6fcd0e00240 fix: make add-on reload ASDF-safe in nested operations
2026-08-24 21c6ad766748e00ff7579c5d9ce1a954c1185ac4 test: expose Bixby add-on reload failure cause
2026-08-24 a8489ff29ae8c082d4590f46adecf5aae2274fc0 build: package optional Bixby ASDF add-on in Nix closures
2026-08-24 e59e6285d036735830efbdcc05cc074a14849558 test: keep Bixby add-on optional outside test-system dependencies
2026-08-24 141ccda56e3102902c0db26210538e586e3b88b2 test: include optional Bixby ASDF system in hermetic test closure
2026-08-24 7da237f1e93ce1ab6e0bc3d373d0fbabe1cf64ab test: surface Bixby add-on load cause without weakening failure
2026-08-24 d4425f7514e0db1a8675ed4fa2fcbda1b279370c fix: parse OAuth space-delimited scopes at provider boundary
2026-08-24 685c672c1b24acc6cc7f253936de365ee3fa2c8b test: repair OAuth wrong-password regression reader syntax
2026-08-24 f9da9c7e136dd08abe256d205f55f2df47aa51d9 Serialize add-on lifecycle operations
2026-08-24 f1b54e6d1176c1d05fb940b4dddb2594eab9d269 Use public core OAuth API from Bixby add-on
2026-08-24 96c70d5a4fbe318af3cc44b30ab41f247e59a7c9 Export reusable OAuth validation helpers
2026-08-24 d4d4555353f3a1cf58ba3ae9a885e2b61cc7d81e Prove add-on configuration survives reload
2026-08-24 8b8d3f40acb2f486bb11ff6c79a7189c58220a38 Preserve Bixby configuration across reloads
2026-08-24 f4c123b0bda9767099bc9515ea852b6fbe8578e5 Document built-in OAuth authorization-code provider
2026-08-24 fe6b6b547355c3752f22e5ecedb6d2d1fe195fe3 Document StarIntel Common Lisp add-on lifecycle
2026-08-24 298fab5a61f85eaf61c6e4e67921d30f9ccda805 Keep optional Bixby package out of test reader dependencies
2026-08-24 433ad78be951dacb95dd6345b3818b53852dc20e Require add-on lifecycle suite in unit gate
2026-08-24 b9079a7aa9ab9f917269f3eb4b498e8ec7a1c452 Wire add-on lifecycle tests
2026-08-24 1e6c2839e052687b916daee00a62dd2664258ebf Test add-on loading reload and Bixby package boundary
2026-08-24 abc8e7be26fea9ba896c5a814cf7a46d6792d4a7 Make add-on reload rollback restore prior definition
2026-08-24 b24a41bc1bf58bf2b2da3d198e6179cd959bb68e Load add-on lifecycle before init configuration
2026-08-24 0a196fe8032625b19426d4b345134eddb7bd73eb Implement Bixby add-on configuration over core OAuth
2026-08-24 3105fede8b996d7b51eb340b82798c3ce7475698 Define Bixby add-on package boundary
2026-08-24 0d6d2ff3d22d940679b7910e6c30ef3718accc76 Add optional StarIntel Bixby add-on system
2026-08-24 208d83dcd118558714c0328f5bf5f7c6cfeb7f62 Formalize ASDF add-on lifecycle and stable reloads
2026-08-24 9258d76901568eadddf2e71ee1ef2d54c9802955 Load OAuth provider HTTP routes
2026-08-24 bc206691c5a0746552afb9b99f921f3551cc3ba4 Expose OAuth protocol paths without bearer auth
2026-08-24 995b65ee7379e35a92913b4b1bba38e5f6e63362 Implement standard OAuth authorization-code HTTP provider
2026-08-24 2f3d9a5379372982d4bd9cbe7b4f8e032ef0a542 Wire OAuth provider contract tests
2026-08-24 140c8d515a871ee83a2572c6c15e7089dd58ce2e Add OAuth provider HTTP contract tests
2026-08-24 20cc5fccbe3865f149852bc4cfc49039fc4a4ebe API v1: public search and watch-safe stats (#110)
2026-08-24 b27b2121af19195e70955177f1c4a6c178a49f44 ci: use CouchDB 3.5 Clouseau distribution
2026-08-24 a435575ffe244dccac107e2ff938855f0a49defa ci: provision Clouseau for service-backed search gate
2026-08-24 c5e1e2f08ebeb3ef1c4c07d663cda8ceecba4a6a test: assert public mode with valid FiveAM form
2026-08-24 8e209ca24ae469e815a668dc45305ab1262fee00 ci: retain service-backed smoke failure logs
2026-08-24 13c4fd1b76d95fc5a219330b34a4a3fe1a3a85d1 test: expose public API integration failures
2026-08-24 1c565541c0ec32697ed458d5a980f5d4d6af2a95 Merge pull request #115 from lost-rob0t/rage/111-bixby-oauth-authority
2026-08-24 99b5a3ecbc29774b75054366f433db426a5c7f69 fix: authenticate OAuth bearer tokens at HTTP boundary
2026-08-24 d1e5e00b94d432199cb3d34158aa697fc83ca034 fix: load OAuth bearer dispatcher before HTTP auth
2026-08-24 a4ec98b77626646315a2cc6a0a6610346ccf477f fix: dispatch bearer credentials across OAuth and API keys
2026-08-24 4d4e5cd48c4e6b7a39f53d22e60eb4590b8eb821 test: cover OAuth bearer middleware dispatch
2026-08-24 aeae9bdeb621db142e1f94e5e75eec2a74a275b5 test: load OAuth bearer dispatch coverage
2026-08-24 34d20c90603eb3dd5a82053b713ca75dbdbef8a7 test: require OAuth bearer HTTP dispatch
2026-08-24 9cbf1a2b4e9f0b4b0e23325999f4bd3fa5917b92 test: bind OAuth clock through auth package
2026-08-24 a31b6ad1199bf2cc6910e4c95117f6c59c2a224b test: require OAuth suite in hermetic gate
2026-08-24 cb787d8d0c05d97f4d3e2939cda08e067d4c3680 feat: load OAuth authorization-code core
2026-08-24 aa16c041d43cc14c38ee37dca4b3072594036142 feat: expose OAuth auth contract
2026-08-24 912a6db155147bbe625386ca990a1d20252c1844 feat: add bounded OAuth credential lifetimes
2026-08-24 67ef1029658ccc0d74a024f65c80f39cd2aded32 feat: implement OAuth authorization-code security core
2026-08-24 3038baed85b9aabe5f279df5735ae012f2199562 feat: reserve OAuth records in auth store
2026-08-24 858486dffde5f3b72adc4745feed0b35ab09532a test: load OAuth authorization-code suite
2026-08-24 969738105b9a8f0cef5ddf18908fd873606bec72 test: require OAuth authorization-code security core
2026-08-24 7f8cee487a8e4559b3a6ab04f557bac7df6f2a28 Fix admin CLI Compose secret-file resolution (#113)
2026-08-24 118fc8ce725d84e067d423384719920cda021740 fix: make public mode override default public read paths
2026-08-24 8e77fd360916cd8447a215b733ba2154ffef17e0 feat: report effective public mode in capabilities
2026-08-24 9d67b2fa396ffe9c99be61f46b8509533e45a8b5 fix: stop hardcoding public read paths
2026-08-24 636034bd23fbd9a3cc0772366e827f98fb0a759c fix: evaluate public mode at auth boundary
2026-08-24 7d854ed75987d439e440d557cfa69b3139cc05db docs: make public mode explicit in init example
2026-08-24 716c48df3783678c96521340d901159958da2043 test: reference init public mode setting internally
2026-08-24 033ff09bab6e27936e42c86223fbc52ec3b5dbb6 feat: add default-on public read mode setting
2026-08-24 9d8bc81354fb621d6b54cc116693e10a182f3a22 test: gate public read API behind init public mode
2026-08-24 610b4945e0578c4d8e31a69a1b522877b54fc8d1 test: load public API integration coverage
2026-08-24 ef462b7ffe88b99d6299d49b08fb2c837c5a510b test: prove public reads and protected mutations over HTTP
2026-08-24 b3b626d685a210e04095ee7062bf731f332d5506 test: bind public search scope at its owning boundary
2026-08-24 c8e9e2803029b0f61e34a79e38cf173c22a35ac3 feat: advertise public and privileged API authority
2026-08-24 5ab38615990b8c37695e0b28f3de33faa39d5584 feat: serve scoped public search and aggregate stats
2026-08-24 a0ba6a8efb0dd73ea078edeacd906c81920dcbe3 feat: contract public v1 search and stats
2026-08-24 bdf763baf47758a5898a5e5bf96bb0b0ff263603 test: define public v1 search and stats authority contract
2026-08-24 8f6e50701081f0335c7552082dba5ff392b859e5 Merge pull request #104 from lost-rob0t/agent/gserver-client-admin-contract
2026-08-24 5e5838c627a2bf57d7360e64b150b5f073a1cb56 fix(client): reject truncated JSON responses
2026-08-24 068afa1aef1c417b1492335d6170325ed8736af9 test(client): cover request options constructor lifecycle
2026-08-24 9c4fa2dd276be14b329d8cc66a4e67c4cae2f36c fix(client): keep request options constructor callable
2026-08-23 820b54519c8811cb87d8fdf15d8b48c5285e85f9 fix(client): avoid constructor redefinition warning
2026-08-23 e5f36356772ba9933b3631dbaf1bfeb3ea158c0d Merge pull request #102 from lost-rob0t/agent/api-v1-capabilities
2026-08-23 2fbc4b74fe4517cf7c39266a1807bf640ba747dc test: make capability route assertions valid FiveAM forms
2026-08-23 3c4dd634e3c77a6078ad02ab3535fb257866a1c8 Merge pull request #107 from lost-rob0t/fix/106-couchdb-session-renewal
2026-08-23 b320e3a5c373a5fa527ed091d3bea10cfb7fec2a test: fix CouchDB session pool LET binding
2026-08-23 d6670a69fa2d66a24050a3947214788d56262a22 test: close CouchDB session renewal regression form
2026-08-23 795a90b08550f8d8def0d9431ef0a0b434621f52 ci: retain hermetic failure log for diagnosis
2026-08-23 5e6b7b731b822e96c351bac729dbed34efc71768 ci: surface hermetic test failure tail
2026-08-23 9472cd384b5af3ffa7441097f4c110f6ccfea614 test: assert shared CouchDB pool validator identity
2026-08-23 c2fba5c9d9ff34ac68a99afd7ac4c29ccd05ec0a fix: share CouchDB session validator directly
2026-08-23 839f3d88cef66b4b38b167af0ca7d3390bb4cba2 test: assert CouchDB session replacement contract
2026-08-23 ff62de333b231b550a7e0e464c64dc13d291fc52 fix: preserve live CouchDB pool identity
2026-08-23 69a6e149aa612452ac9c14537b4bcaa09ea705d9 test: cover live HTTP and auth CouchDB pool probes
2026-08-23 50e4c60ad7733b371a21c70c74f35bbe960e6e64 fix: install CouchDB renewal after HTTP pool exists
2026-08-23 d1867ea28e6a18cc347d48401fc69779488892c0 fix: install renewal policy on live HTTP CouchDB pool
2026-08-23 74d971109a4e6c40bb544d49d79a87b954f7d2f5 fix: load CouchDB session policy before pool owners
2026-08-23 27a75bd8907b47e9c79ed36ab675e22dc88aedb5 fix: route all CouchDB pools through session renewal
2026-08-23 b90a000d081b38900d7b79227607f67a5a145e0a test: prove replacement operations and auth pool renewal
2026-08-23 396b922f7eafb9747b4df3d2d085938e03defd61 test: bind CouchDB integration connector counter sequentially
2026-08-22 4d20a932c70f94fe92e88635992c4ec41968887e test: verify CouchDB session renewal against real service
2026-08-22 1cbe33e9fee24b05174625ba292ef7866884de5b fix: probe CouchDB session without broken request macro
2026-08-22 686719c1d1c0be975b339e9e036771d4246f7fe0 test: require CouchDB session renewal suite
2026-08-22 6d37419810340139d7aea542024042734f3948eb test: load CouchDB session renewal regression
2026-08-22 2291212c174f79804910dbbe6f14d5cea3fb0914 build: load CouchDB session hardening
2026-08-22 f4f5526814ff1eabd2bcebc230879bf4b6230b98 test: prove expired CouchDB sessions are renewed
2026-08-22 6e5f5daebe77d4efecb31f2b4582afe9aca52591 fix: add session-aware CouchDB pool hardening
```

## Repository paths changed, last 14 days

```text
.github/workflows/smoke-tests.yml
Makefile
addons/bixby/bixby.lisp
addons/bixby/package.lisp
cli/client-runtime-final.lisp
cli/http-contract-final.lisp
cli/http-contract-targets.lisp
cli/starintel-gserver-client.asd
client-test.el
client.el
docker/star-server-init.lisp
docs/addons.org
docs/document-spec.org
docs/http-api-docs.org
docs/messaging.org
docs/oauth-provider.org
docs/v09-runtime.org
example_configs/init.lisp
flake.lock
flake.nix
qlfile.lock
scripts/stack-test.sh
source/addons.lisp
source/auth/oauth-bearer.lisp
source/auth/oauth-package.lisp
source/auth/oauth.lisp
source/auth/store.lisp
source/authorization/package.lisp
source/authorization/services.lisp
source/couchdb-session-hardening.lisp
source/databases/document-update-package.lisp
source/databases/document-update.lisp
source/document-access-package.lisp
source/document-access.lisp
source/frontends/http-auth.lisp
source/frontends/http-authorization-routes.lisp
source/frontends/http-authorization.lisp
source/frontends/http-boundary-core.lisp
source/frontends/http-boundary-routes.lisp
source/frontends/http-bulk-jobs.lisp
source/frontends/http-capabilities.lisp
source/frontends/http-contract-routes.lisp
source/frontends/http-document-update.lisp
source/frontends/http-oauth-provider.lisp
source/frontends/http-target-v1-auth.lisp
source/frontends/http-target-v1-route.lisp
source/frontends/http-target-v1.lisp
source/gserver-settings.lisp
source/package.lisp
source/rabbit.lisp
source/starintel-gserver.asd
source/target-dispatch-fixes.lisp
source/target-dispatch.lisp
starintel-bixby.asd
starintel-gserver-integration-tests.asd
starintel-gserver-tests.asd
t/addon-system-test.lisp
t/authorization-policy-test.lisp
t/couchdb-session-test.lisp
t/couchdb-view-integration-test.lisp
t/gserver-client-final-test.lisp
t/http-api-test.lisp
t/http-boundary-test.lisp
t/http-capabilities-test.lisp
t/http-public-api-integration-test.lisp
t/http-target-v1-test.lisp
t/oauth-authorization-code-test.lisp
t/oauth-http-bearer-test.lisp
t/oauth-http-provider-test.lisp
t/run-tests.lisp
t/v09-runtime-test.lisp
tests/test_v09_runtime_contract.py
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/smoke-tests.yml
cli/starintel-gserver-client.asd
flake.nix
scripts/stack-test.sh
source/starintel-gserver.asd
starintel-bixby.asd
starintel-gserver-integration-tests.asd
starintel-gserver-tests.asd
t/addon-system-test.lisp
t/authorization-policy-test.lisp
t/couchdb-session-test.lisp
t/couchdb-view-integration-test.lisp
t/gserver-client-final-test.lisp
t/http-api-test.lisp
t/http-boundary-test.lisp
t/http-capabilities-test.lisp
t/http-public-api-integration-test.lisp
t/http-target-v1-test.lisp
t/oauth-authorization-code-test.lisp
t/oauth-http-bearer-test.lisp
t/oauth-http-provider-test.lisp
t/run-tests.lisp
t/v09-runtime-test.lisp
tests/test_v09_runtime_contract.py
```
