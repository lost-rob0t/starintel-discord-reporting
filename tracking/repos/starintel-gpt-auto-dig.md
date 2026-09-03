# lost-rob0t/starintel-gpt-auto-dig

- generated: `2026-09-03T21:05:09Z`
- canonical branch: `main`
- changelog eligible: `yes`
- head: [`8f31d347f64dd9de25cf570c7990d2e6f93cb962`](https://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/8f31d347f64dd9de25cf570c7990d2e6f93cb962)
- head date: `2026-09-01T12:29:54-04:00`
- head subject: [auto-dig-live-test] accept heading-anchored reports (#2330)

## Git log, last 14 days

```text
2026-09-01 8f31d347f64dd9de25cf570c7990d2e6f93cb962 [auto-dig-live-test] accept heading-anchored reports (#2330)
2026-09-01 bba0b493a5956ca28acbc58c055f465cbc2b1cc4 fix(auto-dig): consume merged synthesis runtime (#2329)
2026-09-01 e7cbefbc16787fb6463c76e48f66ff2fd9402358 [auto-dig-live-test] inject synthesis transition at tool cutoff (#2328)
2026-09-01 94d593227375d87a1aeca28fc45baa7b91514189 [auto-dig-live-test] make synthesis transition explicit (#2327)
2026-09-01 7e1b027005c4b342ce8d5cc8a8e2eb3f9f297767 [auto-dig-live-test] force GLM synthesis earlier (#2326)
2026-09-01 eb639f448bef12711a44744c16564daeb37812fb [auto-dig-live-test] reserve provider latency before synthesis (#2325)
2026-09-01 325c9968125239647629366927ff77b75352b86b [auto-dig-live-test] reserve wall-clock headroom for synthesis (#2324)
2026-09-01 3f3cbbdfb40e90c4a64a2b6edd2001a69794e8a1 [auto-dig-live-test] recover read-only context alias errors (#2323)
2026-09-01 cf3035d8c75bd7440b2ec577e4a67700dded7d50 [auto-dig-live-test] render full actor report for humans
2026-09-01 7fd164cb16f62551832c6409670baa256e35f393 test(auto-dig): require terminal report emission
2026-09-01 329ec1063e7347f94a7408c90e3bfe094296a573 fix(auto-dig): print validated actor report to terminal
2026-09-01 eb70d42050f9f4e0bac149d2842a8575e69b7b2e [auto-dig-live-test] make forced target selection authoritative (#2321)
2026-09-01 70df13d86a56077e963b44a9cd67cdee3ba532c4 [auto-dig-live-test] require real research output (#2318)
2026-09-01 47016b3280997a2ca09cb13d1a5465acfda83a94 [auto-dig-live-test] enforce native tool cutoff before synthesis (#2317)
2026-09-01 f12383eeafb2d37228c76059772796feb1c5783c [auto-dig-live-test] verify synthesis reservation (#2315)
2026-09-01 d796fb908599dbc862c4838e2537835fb0f0bd5e Dogfood: reserve Auto-Dig synthesis headroom (#2314)
2026-09-01 2d04d04ee153ec96ed1e2925c7cacbc5c8a7eb4e Merge pull request #2312 from lost-rob0t/fix/import-counterevidence-duplicate
2026-09-01 fbdbe5673be75db546a4032528e01bd3d7ad08cb fix(auto-dig): leave bounded synthesis headroom [auto-dig-live-test]
2026-09-01 aa6fd1f185494a4864e6d85586ee51ff770d8443 test(auto-dig): require synthesis headroom after research
2026-09-01 46bdd798aed8d0977527de550d6396849f8613cf Merge current main into importer duplicate fix
2026-09-01 62ff4b96c88fe7d4e9f749ddb55dc01ff66469eb fix(auto-dig): restore executable live actor workflow [auto-dig-live-test]
2026-09-01 c3e84fa7b838effd61eb9b1f980f5d5688d24ea2 test(auto-dig): preserve recovery result bindings [auto-dig-live-test]
2026-09-01 4266bc608de7a582f239d50feaca04a5af04c845 test(import): reject counterevidence entity shadowing
2026-09-01 0d43dff0446e56724adfcd45dbe5c3bc2a4fb9bd ci(auto-dig): gate pinned runtime hotfix changes [auto-dig-live-test]
2026-09-01 9b179d194b71df454dc99bd8b5608f9e874b78b8 fix(data): align counterevidence manifest after dedupe
2026-09-01 6c0b8ffc0b321ea8bc5377cbc2f67c3187d46cc9 fix(data): stop counterevidence from shadowing canonical person
2026-09-01 be4673e1920e6992d5e6e36f8140b2e045362a6b fix(auto-dig): bind read-tool error data before observation [auto-dig-live-test]
2026-09-01 c658b2f9e70dfe12fee2315a748cc2cf1a43525b Merge pull request #2219 from lost-rob0t/agent/siders-2026-08-21-indictment-update
2026-09-01 554ed071eda110ab5cb3772be9eaee81656cebdb test(auto-dig): expose read-tool recovery failures [auto-dig-live-test]
2026-09-01 56a2e55a5155605d97ecfd0243789e5407a35ddf fix(auto-dig): recover read-only MCP tool errors [auto-dig-live-test]
2026-09-01 f3e260d01ca2887b2a40e26e786f312f15f08231 fix(auto-dig): encode provider-native tool names [auto-dig-live-test]
2026-09-01 20342c76181dd4de9f519ab3f7c4a769258a2a33 fix(auto-dig): retry transient provider failures [auto-dig-live-test]
2026-09-01 950778074cc706dfe5a52b0c1a41517fde1e2cef Temporarily disable publishing CI
2026-09-01 bf2a99c98f86bfb237f24f21d79f9969a1fa03af Fix full ingest duplicate precedence (#2310)
2026-09-01 e19f2c134b5f77f5b7508237711749e3bcd56a28 Merge pull request #2307 from lost-rob0t/chore/update-prolog-rlm-2026-08-31
2026-09-01 73ac5b65ee984cbd668eaa7ffacc8102561ba2c7 Retry truncated InfluenceWatch HTTP responses
2026-09-01 5f42855f9358cda9b9fd9988d26577c6502ad281 Merge pull request #2308 from lost-rob0t/feat/ingest-documents-ci
2026-09-01 0b8e6f0dc824c76ecf5c5658042bdfa96ac47272 Add Forgejo StarIntel ingest workflow
2026-09-01 cec7398b35742572f4fc873cf50979ffc04efab2 Add manual StarIntel ingest workflow dispatch
2026-09-01 960537291a11a9c843e049e411b1907f59a72868 Add ingest backfill script and diff-only CI
2026-08-31 76f5ae00cd6b7ec4a140ca2aded4c2e92cdb2185 chore: pin Auto-Dig actor to latest Prolog-RLM
2026-08-31 79de77717cc8178e162f77ca49697774615418fc chore: pin Auto-Dig checks to latest Prolog-RLM
2026-08-31 ff1e1d11be560d1691887736c4616b9806443710 Pin validated tool-result wire fix [auto-dig-live-test]
2026-08-31 4daa25e8b67db1568fec32e430a7f13deb9dbdc2 Test bounded Auto-Dig raw-JSON repair [auto-dig-live-test]
2026-08-31 e6b9ba5944045c46cacd3649ffcabd10060535a1 Harden Auto-Dig native-call harness
2026-08-31 7fbdc2684d22c1c3e43cee38002bb41dd90b663e Include actor code in guarded live-test trigger [auto-dig-live-test]
2026-08-31 4278516533cae083014fcc88cef60324d71306d1 Fix stale Auto-Dig MCP allow-list regression test
2026-08-31 c5eec01de8971f5b5c91d7cf570a6846c289b55d Re-enable Auto-Dig actor with current RLM harness [auto-dig-live-test]
2026-08-29 e75a02a22813a2e5b337ba1939490f357675efa7 Temporarily disable Auto-Dig Prolog actor runner
2026-08-29 a4b73884d1556cf8eb3bc1ec924d4dd947800733 Merge pull request #2305 from lost-rob0t/fix/use-prolog-rlm-298-schema-fix
2026-08-29 c5210c524fb0445597853128c44c66ab7ce5a5cb chore: remove temporary Prolog-RLM upgrade workflow
2026-08-29 9ede514e70ac2d92f61366b1e259815394e6b60e test: restore complete 14-tool direct inventory
2026-08-29 e12b7edcc096231f88726e2d6e6248b890c93b0e fix: restore full Brave direct tool inventory
2026-08-29 f8d8e623cb45e47d43de37d8c4a02de568b4f48a fix: pin Prolog-RLM any-schema renderer
2026-08-29 4ad80f280ee983a4f9b5d997405cd7b18b0b29c5 ci: apply and test Prolog-RLM schema upgrade
2026-08-29 46fdb4f497d2628c1797bd570467121f3ebdf373 Merge pull request #2304 from lost-rob0t/fix/auto-dig-skip-unprojectable-llm-context
2026-08-29 fb4944574bf21b8775d6cb9a9c7624f7bb4f3ff9 test: require 13 projectable research tools
2026-08-29 99336a4dfdbb3e6df292bb9d84a0e991a0faedb4 fix: skip MCP schema Prolog-RLM cannot project yet
2026-08-29 22d70678c0aa26c15c9e24d06ccea0d10dbcf885 Merge pull request #2303 from lost-rob0t/fix/auto-dig-direct-rlm-2026-08-29
2026-08-29 f0cb6cad309df6d76d48c2739bdaf88eb0d479f4 test: require complete direct research tool inventory
2026-08-29 afd59d775f781b49b5eba5a26460b881e28e7f15 feat: expose full read-only research MCP inventory
2026-08-29 d616cc4e431ba0c776962ed733b10aa62ae92e27 ci: pin latest Prolog-RLM direct runtime
2026-08-29 b5e455358a2055670d4b0e96bbf6a4ab5ba0da7a test: cover direct-mode Auto-Dig runtime policy
2026-08-29 1f8882388a4d80bf589c733df4a8c6a8c38024a5 fix: run Auto-Dig research through direct RLM mode
2026-08-27 f9854092a34b60767e95a19ddea4332cdb6720eb Merge pull request #2301 from lost-rob0t/fix/auto-dig-rlm-observability-2026-08-27
2026-08-27 b52b96140681b149170979010a6976ac7f317f91 Make emission scrubber progress-safe on SWI 9.0
2026-08-27 c33a0b578dce1ebe81eed26037e8ae7b9f2dd5bb Fix UTC timestamp formatting on SWI 9.0
2026-08-27 501c0a8be018a546a7869f337c4133af5d28fc6d Sanitize persisted RLM diagnostics before write
2026-08-27 bfe97b0850ea9777fbeb7804625c065ce0a7ea8c Emit sanitized failures from actor workflow
2026-08-27 5e0b760691b699c21a41dbd9e4067e8f1b0506fb Sanitize live diagnostics before emission
2026-08-27 3c8654c62edb0ceb7399626aae1ff54212dee409 Inline failure reporting with actor emission path
2026-08-27 cbd4e39aacf83fb73862d6cff32ef8bd8ec913ee Route MCP diagnostics through safe emitter
2026-08-27 ed6f4fd4281d0d670fb935351f05512bf3ad7543 Route RLM diagnostics through safe emitter
2026-08-27 52fb094fa289c91e34641065aed7f7c4d7a9bee2 Sanitize Auto-Dig logs at emission boundary
2026-08-27 34dedda1042818f8830d3ba0108006d59ab834ee Remove post-hoc redaction gate test
2026-08-27 edab8674ceb1b869e7311859438aa8713f5b0ea9 Remove post-hoc redaction gate
2026-08-27 d31fdde4d49c7888faa19edbc549bfbb6fe3d3b0 Remove accidental marker
2026-08-27 7d4f0ac259871ded1493fab09609b90e2b956343 No-op marker
2026-08-27 26c4591e06cac6d39645f6ed8c84200542a5a41c Add failure report redaction CI gate
2026-08-27 105401f97cf1261a5409e53a5cfdac27abdfabb2 Report sanitized actor failures back to issues
2026-08-27 d81155ca5bb82bd209ede49ea8e16005ca3001ae Stream MCP lifecycle logs to Actions output
2026-08-27 304b3f1211da784d81a7140b8065a193c9823e4c Stream RLM phase logs to Actions output
2026-08-27 48464dd78ce302fd1279618ff4fcabb9b78e0af6 Log MCP lifecycle phases safely
2026-08-27 cc10f4e477efd7c444b9cef5552be714b3717a31 Test Auto-Dig failure report redaction
2026-08-27 4456c5b6a107098cad5fb6a7fd8110253d409996 Add secret-safe Auto-Dig failure reporter
2026-08-27 bda20bf63fcc52076d584efb6ab7b8e408b5588d Surface structured RLM failures in actor logs
2026-08-27 54dcf62874b96da458ee1d36ab300f8fe3bfee49 Lock Auto-Dig RLM budget at 50k tokens
2026-08-27 5f0cf64cfd10c3725dfcee7c21cd7a82ac49dd3c Raise Auto-Dig RLM token budget to 50k
2026-08-27 8e6c735465340a9660a649576267e08efe609992 Merge pull request #2298 from lost-rob0t/auto-dig-prolog/2026-08-27-latest-rlm
2026-08-27 632efcc6a71022b703a8a09c5e792e5045f5bbea Document live Brave and Fetch MCP research
2026-08-27 0d6477b1eca85e02a8c20950a20c85c84ab148fa Enable Brave MCP in live Auto-Dig research
2026-08-27 c68ee2208a435b9f031b90edcdb07e4780fc9e6d Test MCP projection in native RLM runner
2026-08-27 1b16ed332eb9f41dcda409937a7803fd418ae2b3 Wire Brave and Fetch MCP into native RLM runner
2026-08-27 d486cfa37df22d6fe7d8ae0f546922bb2167c5ff fix: keep Auto-Dig RLM query valid Prolog
2026-08-27 1321cc05aafdd85e28136b0c98f7e66ab292c3f8 docs: describe current RLM actor features and secrets
2026-08-27 41a27a27aef94117243b8fe4575dfa7b54bd4f35 agent: run current Prolog-RLM native planner features
2026-08-27 68d2d32cd1620a9d299a1631798031f58aa3a8bc ci: gate Auto-Dig against current Prolog-RLM
2026-08-27 fce24df9f13a23ddf25e1a7f9235f839ed1b2046 test: lock latest RLM feature contract
2026-08-27 aa28f12911c9f24e806bc5f6ac5897275a7e03a1 agent: use native latest Prolog-RLM planner path
2026-08-27 4e9873c2f13a7aa30bcca46f0e1df712d3ab2cca Merge pull request #2287 from lost-rob0t/auto-dig-prolog/2026-08-24-bootstrap
2026-08-26 b79a0ec9e8b289c4e6eaa7eaa7e0158eb43c7d5e test: avoid unbound dict projection in MCP catalog assertion
2026-08-25 ad90cdcfb38fee5a7ad730b234b7d5cada14bcce test: isolate Auto-Dig MCP lifecycle boundaries
2026-08-25 2cb735eb3c11e6d12d6914a059a3d91c3fde4eb3 fix: make MCP lifecycle inputs ground and phase failures explicit
2026-08-25 797ded062f31477dd773870679824c206c28c0af fix: resolve Prolog-RLM MCP modules through library path
2026-08-25 e1acbe82f350796511429699f3ef470ae2accfb2 ci: exercise explicit Auto-Dig MCP lifecycle
2026-08-25 dfaa31a275c6693fec7b5ded4fba71646e38d2db test: exercise Auto-Dig MCP lifecycle and capability boundary
2026-08-25 f80c45157373d9ff245f536768508ec15d58a978 feat: add explicit Auto-Dig MCP lifecycle runner
2026-08-25 d695ec1abadcaf03b875b58aa78d882e9019c09a feat: scope Auto-Dig MCP capabilities by server set
2026-08-25 eed4e6e81b59acd6164ac249fdc47399e91e2e57 Harvest mature Flock request #2112 Dunwoody evidence (#2292)
2026-08-25 eb18b4c82300d27280f7e1983f06182eb1d388ba Harvest mature Tompkins County request #1904 evidence (#2291)
2026-08-25 edd02d9a42654dfb40b697977b3d4fbc9b4a493a ci: pin production Auto-Dig to landed Prolog-RLM
2026-08-25 e7d51107a801d783174ac9cdd230f877b289c0e2 ci: pin Auto-Dig checks to Prolog-RLM capability fix
2026-08-25 c4e4c7a8e21da9c968f95b7fada22389eacbee07 test: verify fetch config remains reference-based
2026-08-25 680dea12d69c1ebefc4911600956e400c27e879a feat: configure bounded fetch output through config ref
2026-08-25 d6ec8e3b9337a83606e71aa29e811d779b73ef7d ci: verify trusted MCP research policy
2026-08-25 88e1e280750bde83b91d9dfb05209143ea37afd9 test: lock down Auto-Dig MCP host policy
2026-08-25 7ea5c2f9a36dbcebe3fd01a82d12f92f96de1452 feat: declare trusted read-only research MCP servers
2026-08-25 b18175560c3521f32f81cc84880979396a1e3382 test: cover ground JSON supervision boundary
2026-08-25 00bf8ecc60b612d11def78cfbefcc16949317e93 fix: ground JSON before supervised actor calls
2026-08-25 d7f939028297fe2ae8445f7fb5ab4645e663c9e7 ci: validate reasoning CLI with upstream tests
2026-08-25 b9630311d7a1558fdad99338e1fee042dc898d96 ci: use real CLI tests for reasoning contract
2026-08-25 7035c46ea42acc4492fbf2c1cdec4c3b4c5766fe docs: describe expert model routing contract
2026-08-25 5fce67a5c64840a805d1b7c0712d26fec7e5d90d feat: enforce Prolog expert model routing in live actor
2026-08-25 8eb420f68dc3674cc68293967e79f30e13c1ecf1 ci: exercise expert model routing with reasoning controls
2026-08-24 e59e2b7069e96246ba7c3d219302d4f051d30cf2 Harvest The Wire Oregon verification for request #2286
2026-08-24 08fb635d943a1a67e7a0a589aea567d16f0f6d26 Harvest mature Seattle request #2106 RTCC/FUSUS evidence
2026-08-24 216577814426ef75c261e2277eda5e8c36b2f87f Harvest mature Worldcoin request #2095 evidence (#2288)
2026-08-24 01512391157c6a1f63d150cf87525dbee986d82c test: cover expert model routing policy
2026-08-24 004608ee3a0f6e5af40060ae35cb601761817596 feat: add expert model routing KB
2026-08-24 e7de0ad406ecda4bf8107171d8a5fe2678f9f037 fix: use canonical supervised actor call
2026-08-24 4aa9510c14702f3883e3419a1cd273ff7fafc97c ci: expose actor CLI smoke diagnostics
2026-08-24 c72c6253b30c4ff6e04f84e561e10b70e796e084 fix: use SWI main/1 actor entrypoint
2026-08-24 c978cda8e700753c5829d640e08b9df9a118e85b test: cover fair high-priority recurrence
2026-08-24 bd9e4e8440603d6754f1811ed2ab74fd93068162 fix: keep high-priority recurrence fair
2026-08-24 10680bdae16eee9e5f01a3196264d9de4feef8d5 ci: add credential-free Auto-Dig Prolog actor gate
2026-08-24 335c3ab997281bfa4cf3f7c61e78ea12b9b56148 fix: parse SWI argv atoms in actor CLI
2026-08-24 455ddc74795aff4b405bcaa362820a9e0ea9020c docs: add Auto-Dig Prolog actor state schema
2026-08-24 cd91765ca845a4522885cac55a8c27f61f079bc5 docs: define Auto-Dig Prolog actor contract
2026-08-24 92bb871ae978597a9d5310ad1ddfc8e80b99b538 ci: run Auto-Dig through Prolog-RLM actor
2026-08-24 11ec3dd71991a7f98206bd623969b9896227c8e5 fix: emit closed JSON actor decisions
2026-08-24 e6010bd5769c44f070908c163e3a2bca2a00b96a test: cover Auto-Dig Prolog actor selection policy
2026-08-24 093b32e0386666bf0d7b3b58010325b6ae773683 feat: add supervised Auto-Dig Prolog actor
2026-08-24 ed60a476792ccee83e41973f96e86914b8943dba chore: pin OpenCode web MCP versions
2026-08-24 4fb9a45fdb0784c45b86ba34b3a3aa10081f3d38 chore: add Brave Search and web fetch MCPs for OpenCode
2026-08-24 cdaa15e118f00eb471320c44a7b17d2aaad4e4a9 Harvest mature Rensselaer Sheriff evidence from request #1901
2026-08-21 dbec0aa6eb61e3670a499e25fe6356af31d74087 docs: register linked indictment shard
2026-08-21 6273cd6045e8396d4f97a8249b7fd82dd75811ff data: register linked indictment shard in packet manifest
2026-08-21 5e8b351abe9ba435cddeaeb6e93eb13f6b77edaf data: add linked Investigation One adult indictment records
2026-08-21 2a294db3940720f983995f845fe5befc59c014f3 data: add adult defendants from linked Vinton investigation
2026-08-21 7c763e00b6679b0a65d00e2f8191984d4c4b60cf data: normalize Aug 21 Siders indictment update
2026-08-21 02c81282c9ce91eb18d09101e55616abca1fe234 data: update Siders legal case to Aug 21 indictment posture
2026-08-21 1d58efa3248c5fbe1e0273a1cb8a769faad14838 data: add Aug 21 indictment sources to Siders packet
2026-08-21 c85ee38c6b015429fe05216f9fde611fe415692a docs: add Aug 21 indictment sources and strict minor-victim redaction
2026-08-21 8ed203d52d6f65116a780b6f058a1c46b2f3c3b1 docs: update Siders packet for Aug 21 indictments and victim privacy
2026-08-20 79db594ffaacdf9fa7ccb55a9ff411a7fb85e458 DNC key people WEF and accountability pass (#1944)
2026-08-20 267d031cdc04dd55fd446137f47ff503f94a9adf Auto-Dig #2106: use GitHub CI and advance RTCC control chain (#2110)
2026-08-20 66047287cc19f02ec272d67ccbd554a92d01472b Add BHR Partners depth-12 Indul shareholder and Nijjar chain (#1945)
2026-08-20 c11023bcac6b35f174dad2c03c01f9e3846df13e Add FBI TSC procurement depths 2–5 and evidence collectors (#1962)
2026-08-20 846281d0b037b6d74de8b478e502ced909615f96 dig: add Hanceville police corruption rebrand source packet
2026-08-20 3e370318a4837e923e86c159a367cfc7fc8a558e research: WEF ECP Fall 2026 methodology audit depth 2 (#2024)
2026-08-20 4f98843a4efc256236842c1eca77eda8f034ef54 Add Columbus Flock hearing follow-up packet (#2023)
2026-08-20 eec2fc4148360b9b1399485ddda1f1c42c6284a8 OSF public rosters, legal funding channels, and cross-ties (#1987)
2026-08-20 a3a2ed3325a013f80cc1f4946f707f8f0cd0a1fe Add Trilateral Commission dataset research pass (#1981)
2026-08-20 5c25a30830995aa147f2a0c1133180ee422944be add Flock X/Aerodome video lead (#1973)
2026-08-20 23d7d27f9ea9d3c98481f0486d0c78830cb6b13d Corroborate pending violent-offenders local-news cases (#1979)
```

## Repository paths changed, last 14 days

```text
.forgejo/workflows/import-starintel-documents.yml
.github/workflows/auto-dig-failure-report-check.yml
.github/workflows/auto-dig-prolog-actor-check.yml
.github/workflows/auto-dig-prolog-actor.yml
.github/workflows/auto-dig-prolog-failure-report.yml
.github/workflows/dnc-key-people-wef-accountability.yml
.github/workflows/fbi-procurement-collector.yml
.github/workflows/import-starintel-documents.yml
.github/workflows/materialize-harvest.yml
.github/workflows/publish-pages.yml
.github/workflows/upgrade-prolog-rlm-298.yml
agents/.keep-observability
agents/README.md
agents/auto_dig_failure_report.py
agents/auto_dig_mcp_runner.pl
agents/auto_dig_mcp_tools.pl
agents/auto_dig_model_router.pl
agents/auto_dig_prolog_actor.pl
agents/auto_dig_prolog_state.schema.json
agents/auto_dig_rlm_runner.pl
agents/auto_dig_safe_log.pl
agents/test_auto_dig_deadline_synthesis_hotfix.pl
agents/test_auto_dig_failure_report.py
agents/test_auto_dig_mcp_runner.pl
agents/test_auto_dig_mcp_tools.pl
agents/test_auto_dig_model_router.pl
agents/test_auto_dig_native_cutoff_hotfix.pl
agents/test_auto_dig_prolog_actor.pl
agents/test_auto_dig_provider_retry_hotfix.pl
agents/test_auto_dig_rlm_runner.pl
digs/dnc/2026-08-01-key-people-accountability-counterevidence/README.md
digs/dnc/2026-08-01-key-people-accountability-counterevidence/manifest.json
digs/dnc/2026-08-01-key-people-accountability-counterevidence/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability-seed/README.md
digs/dnc/2026-08-01-key-people-wef-accountability-seed/manifest.json
digs/dnc/2026-08-01-key-people-wef-accountability-seed/materialized-head-validation.txt
digs/dnc/2026-08-01-key-people-wef-accountability-seed/source/current-officer-wef-probes.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability-seed/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/README.md
digs/dnc/2026-08-01-key-people-wef-accountability/manifest.json
digs/dnc/2026-08-01-key-people-wef-accountability/part-00/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-01/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-02/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-03/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-04/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-05/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-06/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-07/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-08/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-09/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-10/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-11/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-12/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-13/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-14/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-15/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-16/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-17/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-18/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-19/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-20/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-21/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-22/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-23/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-24/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-25/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-26/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-27/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-28/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-29/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-30/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-31/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-32/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-33/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-34/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-35/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-36/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-37/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-38/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-39/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-40/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-41/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-42/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-43/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-44/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-45/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-46/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-47/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-48/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-49/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-50/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-51/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-52/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-53/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-54/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-55/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-56/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-57/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-58/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-59/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-60/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-61/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-62/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/part-63/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/source/people-priority-inventory.jsonl
digs/dnc/2026-08-01-key-people-wef-accountability/starintel-documents.jsonl
digs/dnc/2026-08-01-key-people-wef-expansion/manifest.json
digs/dnc/2026-08-01-key-people-wef-expansion/starintel-documents.jsonl
digs/fed/2026-08-02-bae-thiel-wef-think-tank-cross-dataset-depth-4/README.md
digs/fed/2026-08-02-bae-thiel-wef-think-tank-cross-dataset-depth-4/merge-plan.json
digs/fed/2026-08-02-bae-thiel-wef-think-tank-cross-dataset-depth-4/source-notes.md
digs/fed/2026-08-02-bae-thiel-wef-think-tank-cross-dataset-depth-4/starintel-documents.jsonl
digs/fed/2026-08-02-fbi-tsc-ai-procurement-lineage-depth-2/README.md
digs/fed/2026-08-02-fbi-tsc-ai-procurement-lineage-depth-2/records-request.md
digs/fed/2026-08-02-fbi-tsc-ai-procurement-lineage-depth-2/source-notes.md
digs/fed/2026-08-02-fbi-tsc-ai-procurement-lineage-depth-2/starintel-documents.jsonl
digs/fed/2026-08-02-fbi-tsc-bae-analysis-services-depth-3/README.md
digs/fed/2026-08-02-fbi-tsc-bae-analysis-services-depth-3/records-request.md
digs/fed/2026-08-02-fbi-tsc-bae-analysis-services-depth-3/source-notes.md
digs/fed/2026-08-02-fbi-tsc-bae-analysis-services-depth-3/starintel-documents.jsonl
digs/fed/2026-08-02-fbi-tsc-historical-vendor-lineage-depth-4/README.md
digs/fed/2026-08-02-fbi-tsc-historical-vendor-lineage-depth-4/source-notes.md
digs/fed/2026-08-02-fbi-tsc-historical-vendor-lineage-depth-4/starintel-documents.jsonl
digs/fed/2026-08-02-fbi-tsc-intelliware-agile-award-replacement-depth-5/README.md
digs/fed/2026-08-02-fbi-tsc-intelliware-agile-award-replacement-depth-5/job-surface.md
digs/fed/2026-08-02-fbi-tsc-intelliware-agile-award-replacement-depth-5/next-pass.md
digs/fed/2026-08-02-fbi-tsc-intelliware-agile-award-replacement-depth-5/records-request.md
digs/fed/2026-08-02-fbi-tsc-intelliware-agile-award-replacement-depth-5/source-notes.md
digs/fed/2026-08-02-fbi-tsc-intelliware-agile-award-replacement-depth-5/starintel-documents.jsonl
digs/fed/2026-08-02-fbi-tsc-intelliware-agile-award-replacement-depth-5/subcontractor-leads.md
digs/flock/2026-08-07-loyal-moses-x-aerodome-conflict/README.md
digs/flock/2026-08-07-loyal-moses-x-aerodome-conflict/manifest.json
digs/flock/2026-08-07-loyal-moses-x-aerodome-conflict/sources.md
digs/flock/2026-08-07-loyal-moses-x-aerodome-conflict/starintel-documents.jsonl
digs/flock/2026-08-10-columbus-flock-hearing/README.md
digs/flock/2026-08-10-columbus-flock-hearing/manifest.json
digs/flock/2026-08-10-columbus-flock-hearing/sources.md
digs/flock/2026-08-10-columbus-flock-hearing/starintel-documents.jsonl
digs/flock/2026-08-12-columbus-renewal-control-surface/README.md
digs/flock/2026-08-12-columbus-renewal-control-surface/sources.md
digs/flock/2026-08-12-columbus-renewal-control-surface/starintel-documents.jsonl
digs/flock/2026-08-24-request-1901-harvest/README.md
digs/flock/2026-08-24-request-1901-harvest/starintel-documents.jsonl
digs/flock/2026-08-25-request-1904-harvest/starintel-documents.jsonl
digs/flock/2026-08-25-request-2112-harvest/starintel-documents.jsonl
digs/hanceville/2026-08-20-police-corruption-rebrand/sources.md
digs/hunter-biden/2026-08-01-bhr-partners-depth-12/README.md
digs/hunter-biden/2026-08-01-bhr-partners-depth-12/attack-results.md
digs/hunter-biden/2026-08-01-bhr-partners-depth-12/entities.jsonl
digs/hunter-biden/2026-08-01-bhr-partners-depth-12/investigation-targets.jsonl
digs/hunter-biden/2026-08-01-bhr-partners-depth-12/manifest.json
digs/hunter-biden/2026-08-01-bhr-partners-depth-12/relations.jsonl
digs/hunter-biden/2026-08-01-bhr-partners-depth-12/sources.jsonl
digs/hunter-biden/2026-08-01-bhr-partners-depth-12/sources.md
digs/open-society-foundations/2026-08-08-public-roster-depth-2/depth-3-ivan-krastev.json
digs/open-society-foundations/2026-08-08-public-roster-depth-2/depth-3-ivan-krastev.md
digs/open-society-foundations/2026-08-08-public-roster-depth-2/depth-3-osf-ecfr-cluster.json
digs/open-society-foundations/2026-08-08-public-roster-depth-2/depth-3-osf-ecfr-cluster.md
digs/open-society-foundations/2026-08-08-public-roster-depth-2/depth-4-ecfr-audited-funding.json
digs/open-society-foundations/2026-08-08-public-roster-depth-2/depth-4-ecfr-audited-funding.md
digs/open-society-foundations/2026-08-08-public-roster-depth-2/depth-5-ecfr-osf-funding-trend.json
digs/open-society-foundations/2026-08-08-public-roster-depth-2/depth-5-ecfr-osf-funding-trend.md
digs/open-society-foundations/2026-08-08-public-roster-depth-2/public-rosters.json
digs/open-society-foundations/2026-08-08-public-roster-depth-2/report.md
digs/open-society-foundations/2026-08-08-public-roster-depth-2/supplemental-ecfr-osf-grant-id-index.json
digs/open-society-foundations/2026-08-08-public-roster-depth-2/supplemental-ecfr-osf-grant-id-index.md
digs/open-society-foundations/2026-08-08-public-roster-depth-2/supplemental-fpos-2024-outflows.json
digs/open-society-foundations/2026-08-08-public-roster-depth-2/supplemental-fpos-2024-outflows.md
digs/open-society-foundations/2026-08-08-public-roster-depth-2/supplemental-fpr-entity-split.json
digs/open-society-foundations/2026-08-08-public-roster-depth-2/supplemental-fpr-entity-split.md
digs/open-society-foundations/2026-08-08-public-roster-depth-2/supplemental-fpr-osi-resource-sharing.json
digs/open-society-foundations/2026-08-08-public-roster-depth-2/supplemental-fpr-osi-resource-sharing.md
digs/open-society-foundations/2026-08-08-public-roster-depth-2/supplemental-legal-funding-channels.json
digs/open-society-foundations/2026-08-08-public-roster-depth-2/supplemental-legal-funding-channels.md
digs/seattle/2026-08-20-request-2106-rtcc-narcotics-control/README.md
digs/seattle/2026-08-20-request-2106-rtcc-narcotics-control/starintel-documents.jsonl
digs/seattle/2026-08-25-request-2106-harvest/starintel-documents.jsonl
digs/trilateral-commission/2026-08-08-cross-network-freshness/README.md
digs/trilateral-commission/2026-08-08-cross-network-freshness/starintel-documents.jsonl
digs/trilateral-commission/2026-08-08-donor-side-and-entity-resolution/README.md
digs/trilateral-commission/2026-08-08-donor-side-and-entity-resolution/starintel-documents.jsonl
digs/trilateral-commission/2026-08-08-government-archive-interface/README.md
digs/trilateral-commission/2026-08-08-government-archive-interface/starintel-documents.jsonl
digs/trilateral-commission/2026-08-08-hewlett-grant-verification/README.md
digs/trilateral-commission/2026-08-08-hewlett-grant-verification/starintel-documents.jsonl
digs/trilateral-commission/2026-08-08-mellon-historical-grants/README.md
digs/trilateral-commission/2026-08-08-mellon-historical-grants/starintel-documents.jsonl
digs/trilateral-commission/2026-08-08-membership-policy-semantics/README.md
digs/trilateral-commission/2026-08-08-membership-policy-semantics/starintel-documents.jsonl
digs/trilateral-commission/2026-08-08-monetary-gold-attribution/README.md
digs/trilateral-commission/2026-08-08-monetary-gold-attribution/starintel-documents.jsonl
digs/trilateral-commission/2026-08-08-north-america-finance-history/README.md
digs/trilateral-commission/2026-08-08-north-america-finance-history/starintel-documents.jsonl
digs/trilateral-commission/2026-08-08-north-america-governance-chronology/README.md
digs/trilateral-commission/2026-08-08-north-america-governance-chronology/starintel-documents.jsonl
digs/trilateral-commission/2026-08-08-policy-attribution-methodology/README.md
digs/trilateral-commission/2026-08-08-policy-attribution-methodology/starintel-documents.jsonl
digs/trilateral-commission/2026-08-08-regional-legal-and-secretariat-structure/README.md
digs/trilateral-commission/2026-08-08-regional-legal-and-secretariat-structure/starintel-documents.jsonl
digs/trilateral-commission/2026-08-08-roster-provenance-audit/README.md
digs/trilateral-commission/2026-08-08-roster-provenance-audit/starintel-documents.jsonl
digs/trilateral-commission/2026-08-08-source-integrity/README.md
digs/trilateral-commission/2026-08-08-source-integrity/starintel-documents.jsonl
digs/violent-offenders/2026-08-08-local-news-expanded-scan/README.md
digs/violent-offenders/2026-08-08-local-news-expanded-scan/sources.md
digs/violent-offenders/2026-08-08-local-news-expanded-scan/starintel-documents-part-007.jsonl
digs/violent-offenders/2026-08-19-siders-vinton-child-abuse/README.md
digs/violent-offenders/2026-08-19-siders-vinton-child-abuse/sources.md
digs/violent-offenders/2026-08-19-siders-vinton-child-abuse/starintel-documents-001.jsonl
digs/violent-offenders/2026-08-19-siders-vinton-child-abuse/starintel-documents-002.jsonl
digs/violent-offenders/2026-08-19-siders-vinton-child-abuse/starintel-documents-003.jsonl
digs/violent-offenders/2026-08-19-siders-vinton-child-abuse/starintel-documents-004.jsonl
digs/violent-offenders/2026-08-25-request-2286-wire-oregon/starintel-documents.jsonl
digs/wef/2026-08-11-ecp-methodology-requisition-depth-2/README.md
digs/wef/2026-08-11-ecp-methodology-requisition-depth-2/starintel-documents.jsonl
digs/worldcoin/2026-08-25-request-2095-harvest/starintel-documents.jsonl
docs/fbi-procurement-scraper.md
docs/repository-contract.md
docs/tsc-job-postings.md
docs/usaspending-award-transactions.md
harvest-manifests/request-1904-2026-08-25.json
harvest-manifests/request-2095-2026-08-25.json
harvest-manifests/request-2106-2026-08-25.json
harvest-manifests/request-2112-2026-08-25.json
harvest-manifests/request-2286-oregon-2026-08-25.json
opencode.jsonc
scripts/apply_prolog_rlm_deadline_hotfix.py
scripts/apply_prolog_rlm_hotfix.py
scripts/generate_dnc_key_people_wef_accountability.py
scripts/import-starintel-documents.py
scripts/influencewatch/network.py
scripts/materialize_harvest.py
scripts/scrape_fbi_procurement.py
scripts/scrape_tsc_job_postings.py
scripts/scrape_usaspending_award_transactions.py
skills/validate-starintel-changes/SKILL.md
tests/test_counterevidence_packet_identity.py
tests/test_import_starintel_documents.py
tests/test_influencewatch_import.py
tests/test_scrape_fbi_procurement.py
tests/test_scrape_tsc_job_postings.py
tests/test_scrape_usaspending_award_transactions.py
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/auto-dig-failure-report-check.yml
.github/workflows/auto-dig-prolog-actor-check.yml
.github/workflows/auto-dig-prolog-actor.yml
.github/workflows/auto-dig-prolog-failure-report.yml
.github/workflows/dnc-key-people-wef-accountability.yml
.github/workflows/fbi-procurement-collector.yml
.github/workflows/import-starintel-documents.yml
.github/workflows/materialize-harvest.yml
.github/workflows/publish-pages.yml
.github/workflows/upgrade-prolog-rlm-298.yml
scripts/apply_prolog_rlm_deadline_hotfix.py
scripts/apply_prolog_rlm_hotfix.py
scripts/generate_dnc_key_people_wef_accountability.py
scripts/import-starintel-documents.py
scripts/influencewatch/network.py
scripts/materialize_harvest.py
scripts/scrape_fbi_procurement.py
scripts/scrape_tsc_job_postings.py
scripts/scrape_usaspending_award_transactions.py
tests/test_counterevidence_packet_identity.py
tests/test_import_starintel_documents.py
tests/test_influencewatch_import.py
tests/test_scrape_fbi_procurement.py
tests/test_scrape_tsc_job_postings.py
tests/test_scrape_usaspending_award_transactions.py
```
