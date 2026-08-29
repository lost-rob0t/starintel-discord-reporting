# lost-rob0t/starintel-gpt-auto-dig

- generated: `2026-08-29T20:57:17Z`
- canonical branch: `main`
- changelog eligible: `yes`
- head: [`e75a02a22813a2e5b337ba1939490f357675efa7`](https://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/e75a02a22813a2e5b337ba1939490f357675efa7)
- head date: `2026-08-29T16:25:47-04:00`
- head subject: Temporarily disable Auto-Dig Prolog actor runner

## Git log, last 14 days

```text
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
2026-08-20 988dec4c442b0797cdd35be854853a81c5e49ae1 Document Siders Vinton County child-abuse case (#2074)
2026-08-20 a0d1a72dfb2a38d5c2e2e9e37fc7b3ed92f43f44 Violent offenders: document Elijah Foster / Mercedes Chico-Sims case (#2055)
2026-08-20 192258c9f4c3016a8b20bf78ebc2158d666ae4e9 Auto-Dig request #2106: Seattle command timeline depth 1 (#2108)
2026-08-20 59ee73efdf40fda472057df9a2f5b606b56c3f7a Auto-Dig request #2095: World ID privileged control depth 1 (#2107)
2026-08-20 8c9c6a9ddf4002b3cdd3dd2c1c397d89fc1a9087 Add current news scan packet (#2096)
2026-08-19 7dc8e2755ef0017d74a8a1c88e1d8a59534817a6 Auto-Dig request #1907: separate Onondaga County ALPR networks (#2103)
2026-08-19 fa3293f3134274db70c8706922bbfcacb9bbd5dd Auto-Dig request #1905: Troy ALPR governance and audit update (#2102)
2026-08-19 62625e75052caaa401f3a8695c7cdf12b022e1e2 Auto-Dig request #2095: World Orb MPC technical authority depth 1 (#2101)
2026-08-19 ddbdecd646d64707712418cafc71e1b5f90358eb Auto-Dig request #1903: Syracuse Flock offboarding and Axon transition (#2099)
2026-08-19 9eacc0ba433ac8f21fb10bda1a1df90022eb9a11 Auto-Dig request #1902: Stewart's Shops rejected ALPR proposals (#2098)
2026-08-19 d03799959ad8f50133ddbdbd70375c058afa198f Auto-Dig request #2095: World control, WLD, and Orb custody baseline (#2097)
2026-08-19 d43ebdf3f4365a9dc2e3a0147a33d8ead5c2120a Auto-Dig request #1901: advance Rensselaer Sheriff Flock network (#2094)
2026-08-19 d322cdd1764da262e399a39335b4ba23f2bc876b Auto-Dig request #1900: advance Cornell Flock controls (#2093)
2026-08-19 5f08c96609ad955840f2be62cc4f40e017d9fa8c Auto-Dig request #1899: advance Ithaca Flock offboarding (#2092)
2026-08-19 6517e09f928f0215177f6be046d84aca8a08c56e Auto-Dig request #1898: resolve East Greenbush Flock vendor (#2091)
2026-08-19 ae85729fb4b6619ff3f63cbcd3394c40e5319bf2 Auto-Dig request #1897: resolve North Greenbush Flock vendor (#2090)
2026-08-19 b3d06edecab8c997cd884957cb8e63e0b0bfdf19 Auto-Dig request #1896: verify Petersburgh Flock installation (#2089)
2026-08-19 241868ad4ea5e8267651272f8d695597fd6c277a Hourly Auto-Dig: Anduril Sparrows Point primary records (#2086)
2026-08-19 64e9c53003523d9878ca8eabbd5885bcd5339aef Auto-Dig request #1895: reconcile Poestenkill Flock rejection (#2088)
2026-08-19 00bd908ae9b50b13319a0324c11265e6b42f79dc Hourly Auto-Dig: One America location semantics (#2084)
2026-08-19 ef7b733699b0505cd307690d868abffa05b159c8 Hourly Auto-Dig: RNC receipts and location semantics (#2085)
2026-08-19 6cb77593aedd9613fa939c14407cb55b164d1c05 Hourly Auto-Dig: Palantir identity and WEF HQ staleness (#2083)
2026-08-19 ded47611a0033310fef3b0df109265d5759645f8 Add idempotent Auto-Dig request queue (#2087)
2026-08-19 5b17fca81bcf875c828fc786546658b6d6dab29b Hourly Auto-Dig: ECFR Berlin office enrichment (#2059)
2026-08-19 f206af66fb1cf56acbb9a64ca37316410532da05 Hourly Auto-Dig: Cloarida Strive Dallas principal-office pass (#2082)
2026-08-19 eba31bdf6b6e475a850699ee6276034f21f66386 Hourly Auto-Dig: Energia Global registration geography (#2081)
2026-08-19 2a8c1d8faaa8f3126d217a40dab91e61d2ec9434 Hourly Auto-Dig: PIIE Washington location and Inu Manak update (#2080)
2026-08-19 d91d85c6d11ca4652f04ebf93801ac4b3d823ef3 Hourly Auto-Dig: RAND headquarters and current-news scan (#2079)
2026-08-19 a33caed9ca2f0b8ced19aa9bc6b2115e1b44f0a8 Hourly Auto-Dig: Brownes registered-office and receiver-authority pass (#2078)
2026-08-19 a567839db8db84c8f0efe787cfadc32ac441c7be Hourly Auto-Dig: Milken Institute location and health update (#2077)
2026-08-19 ee669b5a01d3dc36446c59cccc3c91292570d5b3 Hourly Auto-Dig: Kearns UPD precinct enrichment (#2076)
2026-08-19 36152f6a83d30e7cfcac78415fab51677e3cb883 Hourly Auto-Dig: IISS Arundel House headquarters (#2075)
2026-08-19 a1af6028c7ccceb3c9a759896abc5dc15205e656 Hourly Auto-Dig: Bruegel Brussels office semantics (#2073)
2026-08-19 3f74988be0b4d6aad8dc3a3eeabc80553e1422a3 Hourly Auto-Dig: Rockefeller Foundation global HQ and COO transition (#2072)
2026-08-19 e108edaeb6afee5ca501f4b21505ac1a989019f1 Hourly Auto-Dig: USAID former HQ and State OIG transfer update (#2070)
2026-08-19 15fa1b8d608174bd7c383399126cf4cc24abcd7c revert: remove accidental main-branch hourly packet
2026-08-19 83c65d8741c433db4ad2b940cd791c459cd69687 revert: restore branch-only hourly research flow
2026-08-19 e8aabc3c9f63a9e2192636d36fa5803a32388e90 research: add RAND headquarters evidence packet
2026-08-19 53c44d05b6985d57bc99dab6d22afde5d0693e95 research: add RAND headquarters hourly pass
2026-08-19 ab8683950a61ec019b6107ba27476e9179a3a154 Hourly Auto-Dig: Chatham House location and programme update (#2063)
2026-08-18 432f68871e048a18ac04e56dc215d25c6843432d Hourly Auto-Dig: Boao Forum HQ semantics and news scan (#2062)
2026-08-18 2e35e428ab2523c57b281f3aa8d40e5f8e9bc63a Hourly Auto-Dig: Graphika HQ evidence and news scan (#2061)
2026-08-18 ef8629d9ce862b2be30c376df7bb4e4d630581e1 Hourly Auto-Dig: FED national security adviser and EOP location (#2060)
2026-08-18 e881e2b709e839226b38533e301a165367c64030 Hourly Auto-Dig: Kearns court facility location pass (#2058)
2026-08-18 b26c5a3d67da0161984851a7aceaa2e864854a24 Revert accidental direct-main Auto-Dig packet write
2026-08-18 8746af28bfe348cc2f7f9341303639b2887574ca Add Kearns court facility Auto-Dig pass
2026-08-18 52420c03c47e092bf88b2471691fbd527acbb222 Add Greater Israel Trump Foundation municipality pass (#2057)
2026-08-18 b79ae106b2b541a7ffaf3ff03f27715569e655a5 Hourly Auto-Dig: CIA Anduril HQ semantic conflict (#2056)
2026-08-18 0ca71fafa40cdad7b8d80b7c83c7502ebb92b02f Revert accidental direct-main Auto-Dig packet write
2026-08-18 387ca6affb5c4f6b1692be349b1a12df34f218b9 Add CIA Anduril HQ semantic-conflict research pass
2026-08-18 c5b543ee1182e9a577995cbf9963e6660eba4fd4 Auto-Dig: BlackRock succession HQ enrichment (#2054)
2026-08-18 bf103af31999b136568976a562ababc1facb17a0 Hourly Auto-Dig: Graphika headquarters locality (#2053)
2026-08-18 32ff1462bf945ce642293d40aa035148628c661d DNC Auto-Dig: expand FEC MUR 7157 document graph (#2052)
2026-08-18 880b012ed436214e9ca29250d995ba1a5a1ed5cc Hourly Auto-Dig: WEF-Columbus Global Shapers archival status (#2051)
2026-08-18 c80ec98372c0b2b1cde273470181b4dddad8ba8b Hourly Auto-Dig: Palantir Vulcan HQ and OSC status (#2050)
2026-08-18 eca73e87f8bd689490c603af54f15cfa477c8436 Hourly Auto-Dig: Devil-Corp Credico location pass (#2049)
2026-08-18 e40ac4d096e4ee41ef7c9bfd8a095ea28165de66 Hourly Auto-Dig: Cloarida Fishback/Azoria principal-place pass (#2048)
2026-08-18 a16ea8955b2976f47eae9c0cfc18b495ef046c1c Hourly Auto-Dig: Trump-Netanyahu municipal records and Gaza-plan update (#2047)
2026-08-18 1ced5ee5b386283498389d6bc6e34f95178bda7d Hourly Auto-Dig: CIA Anduril principal-place and Sparrows Point pass (#2046)
2026-08-18 2d09b53b531008b94dc0f51784fede6d42b37e57 Hourly Auto-Dig: WEF-Columbus AndHealth location and incentive pass (#2045)
2026-08-18 c6477597bc1fc9aaed7febfda67fa011b037b4e0 Hourly Auto-Dig: Hunter Biden reporting and publisher provenance (#2044)
2026-08-18 7485cb2fcbd6ca521e615f701f748db799f5db97 Hourly Auto-Dig: GOP C00096412 location and overlap resolution (#2043)
2026-08-18 331f6df871e8cb9850b450f5ca69a27251c74f0c Hourly Auto-Dig: DNC suite history and ICE resolutions (#2042)
2026-08-18 9ad617a08eddeb10901f81ca00f8ccd172fd2edd Hourly Auto-Dig: Cloarida Incubate location and lawsuit (#2041)
2026-08-18 7f519ef2e3d0231da2c94457dc5f0de11372b106 Hourly Auto-Dig: Greater Israel Trump Foundation location scan (#2040)
2026-08-18 cf17c761a93a4482130fa2a97d08a2060ea182a7 Hourly Auto-Dig: Tech-Bro capital location and Vista disclosure (#2039)
2026-08-18 aecf543701606c1255cf49b2a267d3d146db4b33 Hourly Auto-Dig: Graphika public offices and news scan (#2038)
2026-08-18 dc5d57abb276dd2459a8e72fa8da6020fb108d31 Hourly Auto-Dig: FED ODNI location and Clayton handoff (#2037)
2026-08-17 1e852369214223290037b8e83a31bd9123e73394 Hourly Auto-Dig: DNC Democracy Partners HQ and 2028 calendar (#2036)
2026-08-17 fca979e016baaf605dee32b4c13d954bbaad2ad9 Hourly Auto-Dig: Ohio Development location semantics and demolition grants (#2035)
2026-08-17 46a436ca9b8fb19a61fcdc6a88a7f66f1950430a Hourly Auto-Dig: JobsOhio location semantics and Fury milestone (#2034)
2026-08-17 f39aef7902632aef328ba455c7ad2d50056c0167 Hourly Auto-Dig: Anduril HQ semantics and Thunder update (#2033)
2026-08-17 75e6a359a1ec0b928fa8c4095a348287306dc65d Add Flock roster, New York decisionmaker tracking, and sharing recursions (#81)
2026-08-17 bda97837309107e7fd1e5918f975f87f693c47a8 Add WEF Columbus depth 6 primary records (#82)
2026-08-17 53775fb9dd661a324a1f3f547668c5b490b59363 Recurse WEF crossmatch and add Palantir HQ/news Auto-Dig pass
2026-08-17 fa51e55e61bc127a6d46624b486f358120b184c8 Consolidate Flock datasets under canonical root (#2032)
2026-08-17 43de8920667cf7c4f6f820032e357293d900d23c Add sanitized Flock VP enrichment export
2026-08-17 bc39e053f6817317429b002164e23ce4a9375e8c Publish Flock board public-contact surface (#2030)
2026-08-17 3bcd36b0b253285ca4a57412c9f3e9cdf74c7775 Add Flock VP location enrichment pass 1 (#2029)
2026-08-17 35e2fbb6ea8e8ae4073afd1ab85de21239976a1f AutoDig: Flock Dunwoody MJCCA camera access (#2028)
```

## Repository paths changed, last 14 days

```text
.github/ISSUE_TEMPLATE/auto-dig-request.yml
.github/ISSUE_TEMPLATE/flock-locality.yml
.github/workflows/auto-dig-failure-report-check.yml
.github/workflows/auto-dig-prolog-actor-check.yml
.github/workflows/auto-dig-prolog-actor.yml
.github/workflows/auto-dig-prolog-failure-report.yml
.github/workflows/auto-dig-request-check.yml
.github/workflows/auto-dig-request.yml
.github/workflows/dnc-key-people-wef-accountability.yml
.github/workflows/fbi-procurement-collector.yml
.github/workflows/flock-dunwoody-mjcca-one-shot.yml
.github/workflows/materialize-harvest.yml
.github/workflows/palantir-sec-principal-offices-one-shot.yml
.github/workflows/sync-flock-locality-issues.yml
.github/workflows/upgrade-prolog-rlm-298.yml
.github/workflows/validate-db.yml
AGENTS.md
README.md
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
agents/test_auto_dig_failure_report.py
agents/test_auto_dig_mcp_runner.pl
agents/test_auto_dig_mcp_tools.pl
agents/test_auto_dig_model_router.pl
agents/test_auto_dig_prolog_actor.pl
agents/test_auto_dig_rlm_runner.pl
config/locality-tracking/new-york.json
db/address/starintel:address:palantir-principal-office-19505-biscayne-aventura.ndjson
db/analysis/starintel:analysis:andhealth-incentive-ledger-conflict-depth-6.ndjson
db/analysis/starintel:analysis:central-ohio-living-lab-project-disclosure-gap-depth-6.ndjson
db/analysis/starintel:analysis:flock-dunwoody-mjcca-access-initial-assessment.ndjson
db/analysis/starintel:analysis:global-shapers-columbus-status-depth-6.ndjson
db/analysis/starintel:analysis:green-it-operating-model-depth-6.ndjson
db/analysis/starintel:analysis:hntb-smart-lighting-procurement-continuity-depth-6.ndjson
db/analysis/starintel:analysis:palantir-principal-office-enrichment-2026-08-17.ndjson
db/analysis/starintel:analysis:palantir-wef-current-news-materiality-2026-08-17.ndjson
db/analysis/starintel:analysis:smart-columbus-current-staff-role-map-depth-6.ndjson
db/analysis/starintel:analysis:urbanos-reuse-lineage-depth-6.ndjson
db/analysis/starintel:analysis:wef-columbus-depth-6-primary-records-and-status.ndjson
db/analysis/starintel:analysis:wef-columbus-direct-agreement-search-depth-6.ndjson
db/asset/starintel:asset:mjcca-gymnastics-camera.ndjson
db/asset/starintel:asset:mjcca-main-pool-right-camera.ndjson
db/claim/starintel:claim:carter-accessed-mjcca-gymnastics-camera-2025-09-30.ndjson
db/claim/starintel:claim:carter-single-camera-view-2025-09-30.ndjson
db/claim/starintel:claim:demo-partner-documentation-not-produced-report.ndjson
db/claim/starintel:claim:flock-changed-sensitive-demo-location-policy.ndjson
db/claim/starintel:claim:flock-characterizes-carter-access-as-authorized-demo.ndjson
db/claim/starintel:claim:mjcca-camera-sharing-critical-incident-scope.ndjson
db/event/starintel:event:cleveland-supported-columbus-global-shapers-launch.ndjson
db/event/starintel:event:connectus-device-donation-program-launch-2025.ndjson
db/event/starintel:event:flock-carter-mjcca-gymnastics-live-view-2025-09-30.ndjson
db/event/starintel:event:flock-gluck-mjcca-camera-live-views-2025-07-23.ndjson
db/event/starintel:event:hntb-smart-lighting-phase-2-contract-2022.ndjson
db/event/starintel:event:hntb-smart-lighting-phase-3-modification-2024.ndjson
db/financial-observation/starintel:financial-observation:andhealth-columbus-project-cost-components-2022.ndjson
db/financial-observation/starintel:financial-observation:andhealth-downtown-office-incentive-known-payments-2023-2024.ndjson
db/financial-observation/starintel:financial-observation:andhealth-downtown-office-incentive-payment-2023.ndjson
db/financial-observation/starintel:financial-observation:hntb-smart-lighting-lifecycle-authorization-2022-2026.ndjson
db/investigation-target/starintel:investigation-target:dunwoody-flock-demo-authorization-chain.ndjson
db/investigation-target/starintel:investigation-target:dunwoody-flock-raw-audit-logs.ndjson
db/investigation-target/starintel:investigation-target:ecfr-explicit-headquarters-designation.ndjson
db/investigation-target/starintel:investigation-target:flock-dunwoody-mjcca-access.ndjson
db/investigation-target/starintel:investigation-target:flock-live-view-audit-semantics.ndjson
db/investigation-target/starintel:investigation-target:mjcca-dunwoody-camera-sharing-terms.ndjson
db/investigation-target/starintel:investigation-target:palantir-org-id-resolution.ndjson
db/investigation-target/starintel:investigation-target:wef-depth-7-andhealth-compliance-ledger.ndjson
db/investigation-target/starintel:investigation-target:wef-depth-7-columbus-shapers-archive.ndjson
db/investigation-target/starintel:investigation-target:wef-depth-7-green-it-adoption-roster.ndjson
db/investigation-target/starintel:investigation-target:wef-depth-7-hntb-executed-files-and-workshare.ndjson
db/investigation-target/starintel:investigation-target:wef-depth-7-living-lab-project-identifiers.ndjson
db/investigation-target/starintel:investigation-target:wef-depth-7-smart-columbus-project-assignments.ndjson
db/investigation-target/starintel:investigation-target:wef-depth-7-urbanos-deployment-proof.ndjson
db/investigation-target/starintel:investigation-target:wef-depth-7-wef-columbus-public-records.ndjson
db/location/starintel:location:ecfr-berlin-office.ndjson
db/media/starintel:media:columbus-green-it-playbook-2-0-2025.ndjson
db/observation/starintel:observation:hunyar-carter-live-view-log-2025-09-30.ndjson
db/observation/starintel:observation:palantir-principal-office-effective-2026-02-17.ndjson
db/org/starintel:org:city-of-dunwoody-georgia.ndjson
db/org/starintel:org:dunwoody-police-department.ndjson
db/org/starintel:org:emh-and-t-inc.ndjson
db/org/starintel:org:energi-ai.ndjson
db/org/starintel:org:european-council-on-foreign-relations.ndjson
db/org/starintel:org:flock-safety.ndjson
db/org/starintel:org:global-shapers-cleveland-hub.ndjson
db/org/starintel:org:global-shapers-columbus-hub-provisional.ndjson
db/org/starintel:org:marcus-jewish-community-center-of-atlanta.ndjson
db/org/starintel:org:national-engineering-services-inc.ndjson
db/org/starintel:org:palantir-technologies-inc.ndjson
db/org/starintel:org:smart-columbus.ndjson
db/org/starintel:org:urbanos-examples.ndjson
db/org/starintel:org:usdot-jpo-codehub.ndjson
db/person/starintel:person:bob-carter-flock.ndjson
db/person/starintel:person:jason-hunyar-dunwoody.ndjson
db/person/starintel:person:randy-gluck-flock.ndjson
db/product/starintel:product:energi-ai-emissions-mapping-project.ndjson
db/product/starintel:product:urbanos-examples-smartcitiesdata-repository.ndjson
db/product/starintel:product:urbanos-smart-cities-data-platform.ndjson
db/product/starintel:product:usdot-jpo-codehub-smartcitiesdata-repository.ndjson
db/relation/starintel:relation:bob-carter-employed-by-flock.ndjson
db/relation/starintel:relation:bob-carter-viewed-mjcca-gymnastics-camera.ndjson
db/relation/starintel:relation:cleveland-hub-supported-columbus-hub-launch.ndjson
db/relation/starintel:relation:dpd-part-of-city-of-dunwoody.ndjson
db/relation/starintel:relation:dunwoody-pd-uses-flock.ndjson
db/relation/starintel:relation:green-it-playbook-operationalized-by-energi-ai-connectus.ndjson
db/relation/starintel:relation:hntb-phase-3-used-emht-national-engineering-services.ndjson
db/relation/starintel:relation:mjcca-shares-cameras-with-dunwoody-pd.ndjson
db/relation/starintel:relation:palantir-principal-office-effective-2026-02-17.ndjson
db/relation/starintel:relation:randy-gluck-employed-by-flock.ndjson
db/relation/starintel:relation:randy-gluck-viewed-mjcca-pool-camera.ndjson
db/relation/starintel:relation:smart-columbus-partnered-energi-ai-emissions-mapping.ndjson
db/relation/starintel:relation:urbanos-smartcitiesdata-replicated-to-public-repositories.ndjson
db/research-pass/starintel:research-pass:flock-dunwoody-mjcca-initial-2026-08-17.ndjson
db/research-pass/starintel:research-pass:hourly-dark-academia-ecfr-2026-08-19.ndjson
db/research-pass/starintel:research-pass:palantir-principal-office-enrichment-2026-08-17.ndjson
db/research-pass/starintel:research-pass:palantir-wef-current-news-materiality-2026-08-17.ndjson
db/research-pass/starintel:research-pass:wef-columbus-depth-6-2026-07-31.ndjson
db/social-media-post/starintel:social-media-post:deflock-2079202670380814382.ndjson
db/source/starintel:source:404media-dunwoody-flock-demo-camera-access-2026.ndjson
db/source/starintel:source:acpc-dunwoody-flock-contract-camera-access-2026-04-14.ndjson
db/source/starintel:source:deflock-x-2079202670380814382.ndjson
db/source/starintel:source:dunwoody-brookhaven-ledger-flock-gymnastics-camera-2026.ndjson
db/source/starintel:source:flock-testing-development-program-dunwoody-2026.ndjson
db/source/starintel:source:hunyar-why-are-flock-employees-watching-our-children-2026.ndjson
db/source/starintel:source:muckrock-dunwoody-camera-partnership-request-d038447-061624.ndjson
db/source/starintel:source:muckrock-dunwoody-flock-contracts-d045363-090725.ndjson
digs/bruegel/2026-08-19-brussels-location-news/README.md
digs/bruegel/2026-08-19-brussels-location-news/starintel-documents.jsonl
digs/cia/2026-08-17-anduril-hq-thunder/starintel-documents.jsonl
digs/cia/2026-08-18-anduril-hq-semantic-conflict/starintel-documents.jsonl
digs/cia/2026-08-18-anduril-principal-sparrows-point/starintel-documents.jsonl
digs/cia/2026-08-19-anduril-sparrows-point-primary-records/README.md
digs/cia/2026-08-19-anduril-sparrows-point-primary-records/starintel-documents.jsonl
digs/cloarida/2026-08-18-azoria-principal-place-news-scan/starintel-documents.jsonl
digs/cloarida/2026-08-18-incubate-location-lawsuit/starintel-documents.jsonl
digs/cloarida/2026-08-19-strive-principal-executive-office-news/README.md
digs/cloarida/2026-08-19-strive-principal-executive-office-news/starintel-documents.jsonl
digs/dark-academia/2026-08-19-boao-forum-hq-location-news-scan/README.md
digs/dark-academia/2026-08-19-boao-forum-hq-location-news-scan/starintel-documents.jsonl
digs/dark-academia/2026-08-19-chatham-house-location-programme/README.md
digs/dark-academia/2026-08-19-chatham-house-location-programme/starintel-documents.jsonl
digs/dark-academia/2026-08-19-ecfr-berlin-office/report.md
digs/dark-academia/2026-08-19-milken-institute-location-health/README.md
digs/dark-academia/2026-08-19-milken-institute-location-health/starintel-documents.jsonl
digs/dark-academia/2026-08-19-piie-location-news/README.md
digs/dark-academia/2026-08-19-piie-location-news/starintel-documents.jsonl
digs/dark-academia/2026-08-19-rand-headquarters-news-scan/README.md
digs/dark-academia/2026-08-19-rand-headquarters-news-scan/starintel-documents.jsonl
digs/devil-corp/2026-08-18-credico-chicago-location-news-scan/starintel-documents.jsonl
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
digs/dnc/2026-08-17-democracy-partners-hq-calendar/starintel-documents.jsonl
digs/dnc/2026-08-18-democracy-partners-suite-history-ice-resolutions/starintel-documents.jsonl
digs/dnc/2026-08-18-mur-7157-document-graph/starintel-documents.jsonl
digs/drunk-drivers/2026-08-18-kearns-court-facility-news-scan/starintel-documents.jsonl
digs/drunk-drivers/2026-08-19-kearns-upd-precinct-news-scan/README.md
digs/drunk-drivers/2026-08-19-kearns-upd-precinct-news-scan/starintel-documents.jsonl
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
digs/fed/2026-08-18-odni-clayton-handoff/starintel-documents.jsonl
digs/fed/2026-08-19-national-security-adviser-eop-location/README.md
digs/fed/2026-08-19-national-security-adviser-eop-location/starintel-documents.jsonl
digs/flock-safety/2026-08-17-vp-location-enrichment-pass-1/flock-799118-valid-sanitized.csv
digs/flock-safety/2026-08-17-vp-location-enrichment-pass-1/starintel-documents.part-001.jsonl
digs/flock-safety/2026-08-17-vp-location-enrichment-pass-1/starintel-documents.part-002.jsonl
digs/flock-safety/2026-08-17-vp-location-enrichment-pass-1/starintel-documents.part-003.jsonl
digs/flock-safety/2026-08-17-vp-location-enrichment-pass-1/starintel-documents.part-004.jsonl
digs/flock/2026-07-25-columbus-local-government-lobbying/README.md
digs/flock/2026-07-25-columbus-local-government-lobbying/manifest.json
digs/flock/2026-07-25-columbus-local-government-lobbying/sources.md
digs/flock/2026-07-25-columbus-local-government-lobbying/starintel-documents.jsonl
digs/flock/2026-07-25-national-state-locality-seed/README.md
digs/flock/2026-07-25-national-state-locality-seed/manifest.json
digs/flock/2026-07-25-national-state-locality-seed/sources.md
digs/flock/2026-07-25-national-state-locality-seed/starintel-documents.jsonl
digs/flock/2026-07-26-columbus-cpd-control-plane/README.md
digs/flock/2026-07-26-columbus-cpd-control-plane/manifest.json
digs/flock/2026-07-26-columbus-cpd-control-plane/sources.md
digs/flock/2026-07-26-columbus-cpd-control-plane/starintel-documents.jsonl
digs/flock/2026-07-26-columbus-cpd-next-level/README.md
digs/flock/2026-07-26-columbus-cpd-next-level/manifest.json
digs/flock/2026-07-26-columbus-cpd-next-level/sources.md
digs/flock/2026-07-26-columbus-cpd-next-level/starintel-documents.jsonl
digs/flock/2026-07-26-shotspotter-surveillance-locality-recursion/README.md
digs/flock/2026-07-26-shotspotter-surveillance-locality-recursion/manifest.json
digs/flock/2026-07-26-shotspotter-surveillance-locality-recursion/sources.md
digs/flock/2026-07-26-shotspotter-surveillance-locality-recursion/starintel-documents.jsonl.gz.b64.part-001
digs/flock/2026-07-26-shotspotter-surveillance-locality-recursion/starintel-documents.jsonl.gz.b64.part-002
digs/flock/2026-07-26-shotspotter-surveillance-locality-recursion/starintel-documents.jsonl.gz.b64.part-003
digs/flock/2026-07-26-shotspotter-surveillance-locality-recursion/starintel-documents.jsonl.gz.b64.part-004a
digs/flock/2026-07-26-shotspotter-surveillance-locality-recursion/starintel-documents.jsonl.gz.b64.part-004b
digs/flock/2026-07-26-shotspotter-surveillance-locality-recursion/starintel-documents.jsonl.gz.b64.parts
digs/flock/2026-07-31-columbus-287g-sharing-control-recursion/README.md
digs/flock/2026-07-31-columbus-287g-sharing-control-recursion/manifest.json
digs/flock/2026-07-31-columbus-287g-sharing-control-recursion/sources.md
digs/flock/2026-07-31-columbus-287g-sharing-control-recursion/starintel-documents.jsonl.gz.b64
digs/flock/2026-07-31-columbus-asymmetric-sharing/README.md
digs/flock/2026-07-31-columbus-asymmetric-sharing/manifest.json
digs/flock/2026-07-31-columbus-asymmetric-sharing/sources.md
digs/flock/2026-07-31-columbus-asymmetric-sharing/starintel-documents.jsonl.gz.b64.part-001
digs/flock/2026-07-31-columbus-asymmetric-sharing/starintel-documents.jsonl.gz.b64.part-002
digs/flock/2026-07-31-columbus-asymmetric-sharing/starintel-documents.jsonl.gz.b64.part-003
digs/flock/2026-07-31-columbus-asymmetric-sharing/starintel-documents.jsonl.gz.b64.part-004
digs/flock/2026-07-31-columbus-asymmetric-sharing/starintel-documents.jsonl.gz.b64.parts
digs/flock/2026-07-31-columbus-audit-surface-opacity/README.md
digs/flock/2026-07-31-columbus-audit-surface-opacity/manifest.json
digs/flock/2026-07-31-columbus-audit-surface-opacity/sources.md
digs/flock/2026-07-31-columbus-transparency-portal-observability/README.md
digs/flock/2026-07-31-columbus-transparency-portal-observability/manifest.json
digs/flock/2026-07-31-columbus-transparency-portal-observability/sources.md
digs/flock/2026-07-31-columbus-transparency-portal-observability/starintel-documents.jsonl.gz.b64
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/README.md
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/manifest.json
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/sources.md
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/starintel-documents.part-001.jsonl
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/starintel-documents.part-002.jsonl
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/starintel-documents.part-003.jsonl
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/starintel-documents.part-004.jsonl
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/starintel-documents.part-005.jsonl
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/starintel-documents.part-006.jsonl
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/starintel-documents.part-007.jsonl
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/starintel-documents.part-008.jsonl
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/starintel-documents.part-009.jsonl
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/starintel-documents.part-010.jsonl
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/starintel-documents.part-011.jsonl
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/starintel-documents.part-012.jsonl
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/starintel-documents.part-013.jsonl
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/starintel-documents.part-014.jsonl
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/starintel-documents.part-015.jsonl
digs/flock/2026-07-31-new-york-governance-sharing-private-depth-2/starintel-documents.part-016.jsonl
digs/flock/2026-07-31-new-york-locality-seed/README.md
digs/flock/2026-07-31-new-york-locality-seed/manifest.json
digs/flock/2026-07-31-new-york-locality-seed/sources.md
digs/flock/2026-07-31-new-york-locality-seed/starintel-documents.part-001.jsonl
digs/flock/2026-07-31-new-york-locality-seed/starintel-documents.part-002.jsonl
digs/flock/2026-07-31-new-york-locality-seed/starintel-documents.part-003.jsonl
digs/flock/2026-07-31-new-york-locality-seed/starintel-documents.part-004.jsonl
digs/flock/2026-07-31-new-york-locality-seed/starintel-documents.part-005.jsonl
digs/flock/2026-07-31-new-york-locality-seed/starintel-documents.part-006.jsonl
digs/flock/2026-07-31-new-york-locality-seed/starintel-documents.part-007.jsonl
digs/flock/2026-07-31-new-york-locality-seed/starintel-documents.part-008.jsonl
digs/flock/2026-07-31-organization-rosters-wef-crossmatch/README.md
digs/flock/2026-07-31-organization-rosters-wef-crossmatch/manifest.json
digs/flock/2026-07-31-organization-rosters-wef-crossmatch/sources.md
digs/flock/2026-07-31-organization-rosters-wef-crossmatch/starintel-documents.jsonl.gz.b64.part-001
digs/flock/2026-07-31-organization-rosters-wef-crossmatch/starintel-documents.jsonl.gz.b64.part-002
digs/flock/2026-07-31-organization-rosters-wef-crossmatch/starintel-documents.jsonl.gz.b64.part-003a
digs/flock/2026-07-31-organization-rosters-wef-crossmatch/starintel-documents.jsonl.gz.b64.part-003b
digs/flock/2026-07-31-organization-rosters-wef-crossmatch/starintel-documents.jsonl.gz.b64.part-004-0
digs/flock/2026-07-31-organization-rosters-wef-crossmatch/starintel-documents.jsonl.gz.b64.part-004-1
digs/flock/2026-07-31-organization-rosters-wef-crossmatch/starintel-documents.jsonl.gz.b64.part-004-2
digs/flock/2026-07-31-organization-rosters-wef-crossmatch/starintel-documents.jsonl.gz.b64.part-004-3
digs/flock/2026-07-31-organization-rosters-wef-crossmatch/starintel-documents.jsonl.gz.b64.part-005
digs/flock/2026-07-31-organization-rosters-wef-crossmatch/starintel-documents.jsonl.gz.b64.parts
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/README.md
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/manifest.json
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/sources.md
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/starintel-documents.jsonl.gz.b64.part-001
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/starintel-documents.jsonl.gz.b64.part-002
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/starintel-documents.jsonl.gz.b64.part-003
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/starintel-documents.jsonl.gz.b64.part-004a
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/starintel-documents.jsonl.gz.b64.part-004b
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/starintel-documents.jsonl.gz.b64.part-004c
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/starintel-documents.jsonl.gz.b64.part-005
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/starintel-documents.jsonl.gz.b64.part-006
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/starintel-documents.jsonl.gz.b64.part-007
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/starintel-documents.jsonl.gz.b64.part-008
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/starintel-documents.jsonl.gz.b64.part-009a
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/starintel-documents.jsonl.gz.b64.part-009b
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/starintel-documents.jsonl.gz.b64.part-009c1
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/starintel-documents.jsonl.gz.b64.part-009c2
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/starintel-documents.jsonl.gz.b64.part-009c3
digs/flock/2026-08-02-new-york-decisionmakers-contract-admin-depth-3/starintel-documents.jsonl.gz.b64.parts
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
digs/flock/2026-08-17-dunwoody-mjcca-camera-access/board-public-contact-report.md
digs/flock/2026-08-17-dunwoody-mjcca-camera-access/starintel-documents.jsonl
digs/flock/2026-08-17-vp-location-enrichment-pass-1/flock-799118-valid-sanitized.csv
digs/flock/2026-08-17-vp-location-enrichment-pass-1/starintel-documents.part-001.jsonl
digs/flock/2026-08-17-vp-location-enrichment-pass-1/starintel-documents.part-002.jsonl
digs/flock/2026-08-17-vp-location-enrichment-pass-1/starintel-documents.part-003.jsonl
digs/flock/2026-08-17-vp-location-enrichment-pass-1/starintel-documents.part-004.jsonl
digs/flock/2026-08-19-request-1895-poestenkill-flock-rejection/README.md
digs/flock/2026-08-19-request-1895-poestenkill-flock-rejection/starintel-documents.jsonl
digs/flock/2026-08-19-request-1896-petersburgh-flock-deployment/README.md
digs/flock/2026-08-19-request-1896-petersburgh-flock-deployment/starintel-documents.jsonl
digs/flock/2026-08-19-request-1897-north-greenbush-flock-vendor/README.md
digs/flock/2026-08-19-request-1897-north-greenbush-flock-vendor/starintel-documents.jsonl
digs/flock/2026-08-19-request-1898-east-greenbush-flock-vendor/README.md
digs/flock/2026-08-19-request-1898-east-greenbush-flock-vendor/starintel-documents.jsonl
digs/flock/2026-08-19-request-1899-ithaca-offboarding/README.md
digs/flock/2026-08-19-request-1899-ithaca-offboarding/starintel-documents.jsonl
digs/flock/2026-08-19-request-1900-cornell-flock-controls/README.md
digs/flock/2026-08-19-request-1900-cornell-flock-controls/starintel-documents.jsonl
digs/flock/2026-08-19-request-1901-rensselaer-sheriff-network/README.md
digs/flock/2026-08-19-request-1901-rensselaer-sheriff-network/starintel-documents.jsonl
digs/flock/2026-08-20-request-1902-stewarts-proposals/README.md
digs/flock/2026-08-20-request-1902-stewarts-proposals/starintel-documents.jsonl
digs/flock/2026-08-20-request-1903-syracuse-transition/README.md
digs/flock/2026-08-20-request-1903-syracuse-transition/starintel-documents.jsonl
digs/flock/2026-08-20-request-1905-troy-governance-audit/README.md
digs/flock/2026-08-20-request-1905-troy-governance-audit/starintel-documents.jsonl
digs/flock/2026-08-20-request-1907-onondaga-county-network/README.md
digs/flock/2026-08-20-request-1907-onondaga-county-network/starintel-documents.jsonl
digs/flock/2026-08-24-request-1901-harvest/README.md
digs/flock/2026-08-24-request-1901-harvest/starintel-documents.jsonl
digs/flock/2026-08-25-request-1904-harvest/starintel-documents.jsonl
digs/flock/2026-08-25-request-2112-harvest/starintel-documents.jsonl
digs/gop/2026-08-18-c00096412-location-overlap/starintel-documents.jsonl
digs/gop/2026-08-19-rnc-receipts-location/README.md
digs/gop/2026-08-19-rnc-receipts-location/starintel-documents.jsonl
digs/graphika/2026-08-18-headquarters-locality-hourly/starintel-documents.jsonl
digs/graphika/2026-08-18-public-offices-news-scan/starintel-documents.jsonl
digs/graphika/2026-08-19-hq-federal-address-news-scan/README.md
digs/graphika/2026-08-19-hq-federal-address-news-scan/starintel-documents.jsonl
digs/greater-israel/2026-08-18-trump-foundation-location-news-scan/starintel-documents.jsonl
digs/greater-israel/2026-08-18-trump-foundation-municipality-news-scan/starintel-documents.jsonl
digs/hanceville/2026-08-20-police-corruption-rebrand/sources.md
digs/hunter-biden/2026-08-01-bhr-partners-depth-12/README.md
digs/hunter-biden/2026-08-01-bhr-partners-depth-12/attack-results.md
digs/hunter-biden/2026-08-01-bhr-partners-depth-12/entities.jsonl
digs/hunter-biden/2026-08-01-bhr-partners-depth-12/investigation-targets.jsonl
digs/hunter-biden/2026-08-01-bhr-partners-depth-12/manifest.json
digs/hunter-biden/2026-08-01-bhr-partners-depth-12/relations.jsonl
digs/hunter-biden/2026-08-01-bhr-partners-depth-12/sources.jsonl
digs/hunter-biden/2026-08-01-bhr-partners-depth-12/sources.md
digs/hunter-biden/2026-08-18-reporting-publisher-provenance/starintel-documents.jsonl
digs/hunter-biden/2026-08-19-brownes-location-receiver-authority/README.md
digs/hunter-biden/2026-08-19-brownes-location-receiver-authority/starintel-documents.jsonl
digs/iiss/2026-08-19-arundel-house-headquarters-news/README.md
digs/iiss/2026-08-19-arundel-house-headquarters-news/starintel-documents.jsonl
digs/influence-watch-db/2026-08-19-one-america-location-semantics/README.md
digs/influence-watch-db/2026-08-19-one-america-location-semantics/starintel-documents.jsonl
digs/larry-fink/2026-08-18-blackrock-succession-hq/starintel-documents.jsonl
digs/offshore-leaks/2026-08-19-energia-global-registration-news-scan/README.md
digs/offshore-leaks/2026-08-19-energia-global-registration-news-scan/starintel-documents.jsonl
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
digs/palantir/2026-08-18-vulcan-headquarters-osc-status/starintel-documents.jsonl
digs/rockefeller-foundation/2026-08-19-global-hq-coo-transition/README.md
digs/rockefeller-foundation/2026-08-19-global-hq-coo-transition/starintel-documents.jsonl
digs/seattle/2026-08-20-request-2106-personnel-integrity/README.md
digs/seattle/2026-08-20-request-2106-personnel-integrity/starintel-documents.jsonl
digs/seattle/2026-08-20-request-2106-rtcc-narcotics-control/README.md
digs/seattle/2026-08-20-request-2106-rtcc-narcotics-control/starintel-documents.jsonl
digs/seattle/2026-08-25-request-2106-harvest/starintel-documents.jsonl
digs/tech-bro/2026-08-18-capital-syndication-location-news/starintel-documents.jsonl
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
digs/trump-netanyahu/2026-08-18-netanya-ashkelon-record-access/starintel-documents.jsonl
digs/usaid-doge-mortality-accountability/2026-08-19-usaid-former-hq-state-oig/README.md
digs/usaid-doge-mortality-accountability/2026-08-19-usaid-former-hq-state-oig/starintel-documents.jsonl
digs/violent-offenders/2026-08-08-local-news-expanded-scan/README.md
digs/violent-offenders/2026-08-08-local-news-expanded-scan/sources.md
digs/violent-offenders/2026-08-08-local-news-expanded-scan/starintel-documents-part-007.jsonl
digs/violent-offenders/2026-08-18-elijah-foster-mercedes-chico-sims/README.md
digs/violent-offenders/2026-08-18-elijah-foster-mercedes-chico-sims/sources.md
digs/violent-offenders/2026-08-18-elijah-foster-mercedes-chico-sims/starintel-documents.jsonl
digs/violent-offenders/2026-08-19-news-scan/README.md
digs/violent-offenders/2026-08-19-news-scan/sources.md
digs/violent-offenders/2026-08-19-news-scan/starintel-documents.jsonl
digs/violent-offenders/2026-08-19-siders-vinton-child-abuse/README.md
digs/violent-offenders/2026-08-19-siders-vinton-child-abuse/sources.md
digs/violent-offenders/2026-08-19-siders-vinton-child-abuse/starintel-documents-001.jsonl
digs/violent-offenders/2026-08-19-siders-vinton-child-abuse/starintel-documents-002.jsonl
digs/violent-offenders/2026-08-19-siders-vinton-child-abuse/starintel-documents-003.jsonl
digs/violent-offenders/2026-08-25-request-2286-wire-oregon/starintel-documents.jsonl
digs/wef-columbus/2026-07-31-depth-6-primary-records/manifest.json
digs/wef-columbus/2026-08-17-jobsohio-hq-fury/starintel-documents.jsonl
digs/wef-columbus/2026-08-17-ohio-development-location-demolition/starintel-documents.jsonl
digs/wef-columbus/2026-08-18-andhealth-location-incentive/starintel-documents.jsonl
digs/wef-columbus/2026-08-18-global-shapers-archive/starintel-documents.jsonl
digs/wef/2026-08-11-ecp-methodology-requisition-depth-2/README.md
digs/wef/2026-08-11-ecp-methodology-requisition-depth-2/starintel-documents.jsonl
digs/wef/2026-08-12-katherine-hsiao-data-policy-attribution-depth-7/README.md
digs/wef/2026-08-12-katherine-hsiao-data-policy-attribution-depth-7/sources.md
digs/wef/2026-08-12-katherine-hsiao-data-policy-attribution-depth-7/starintel-documents.jsonl
digs/wef/2026-08-12-katherine-hsiao-data-policy-council-depth-6/README.md
digs/wef/2026-08-12-katherine-hsiao-data-policy-council-depth-6/starintel-documents.jsonl
digs/wef/2026-08-12-katherine-hsiao-wef-artifact-recovery-depth-8/README.md
digs/wef/2026-08-12-katherine-hsiao-wef-artifact-recovery-depth-8/starintel-documents.jsonl
digs/wef/2026-08-12-palantir-amnc-session-speaker-resolution-depth-5/README.md
digs/wef/2026-08-12-palantir-amnc-session-speaker-resolution-depth-5/starintel-documents.jsonl
digs/wef/2026-08-12-palantir-wef-data-equity-output-network-root/starintel-documents.jsonl
digs/wef/2026-08-12-palantir-wef-participant-resolution-depth-4/README.md
digs/wef/2026-08-12-palantir-wef-participant-resolution-depth-4/manifest.json
digs/wef/2026-08-12-palantir-wef-participant-resolution-depth-4/starintel-documents.jsonl
digs/wef/2026-08-12-thiel-company-employee-wef-crossmatch-depth-3/README.md
digs/wef/2026-08-12-thiel-company-employee-wef-crossmatch-depth-3/manifest.json
digs/wef/2026-08-12-thiel-company-employee-wef-crossmatch-depth-3/sources.md
digs/wef/2026-08-12-thiel-company-employee-wef-crossmatch-depth-3/starintel-documents.jsonl
digs/wef/2026-08-12-wef-data-equity-2023-coauthor-institution-crossmatch-depth-1/starintel-documents.jsonl
digs/wef/2026-08-12-wef-data-equity-2023-full-author-affiliation-resolution-depth-2/starintel-documents.jsonl
digs/wef/2026-08-17-katherine-hsiao-data-equity-term-end-depth-4/README.md
digs/wef/2026-08-17-katherine-hsiao-data-equity-term-end-depth-4/starintel-documents.jsonl
digs/wef/2026-08-17-katherine-hsiao-data-equity-term-start-depth-3/README.md
digs/wef/2026-08-17-katherine-hsiao-data-equity-term-start-depth-3/starintel-documents.jsonl
digs/wef/2026-08-17-katherine-hsiao-data-frontiers-successor-roster-depth-5/README.md
digs/wef/2026-08-17-katherine-hsiao-data-frontiers-successor-roster-depth-5/starintel-documents.jsonl
digs/wef/2026-08-17-katherine-hsiao-data-policy-direct-artifact-depth-2/README.md
digs/wef/2026-08-17-katherine-hsiao-data-policy-direct-artifact-depth-2/starintel-documents.jsonl
digs/wef/2026-08-17-katherine-hsiao-data-policy-term-calibration-depth-1/README.md
digs/wef/2026-08-17-katherine-hsiao-data-policy-term-calibration-depth-1/starintel-documents.jsonl
digs/wef/2026-08-17-katherine-hsiao-wef-council-chronology-closure-depth-6/README.md
digs/wef/2026-08-17-katherine-hsiao-wef-council-chronology-closure-depth-6/starintel-documents.jsonl
digs/wef/2026-08-17-katherine-hsiao-wef-council-chronology-root/README.md
digs/wef/2026-08-17-katherine-hsiao-wef-council-chronology-root/starintel-documents.jsonl
digs/wef/2026-08-17-palantir-current-news-pass/starintel-documents.jsonl
digs/wef/2026-08-17-palantir-sec-principal-office-history/README.md
digs/wef/2026-08-17-palantir-sec-principal-office-history/starintel-documents.jsonl
digs/wef/2026-08-17-palantir-wef-data-equity-output-network-closure-depth-5/README.md
digs/wef/2026-08-17-palantir-wef-data-equity-output-network-closure-depth-5/starintel-documents.jsonl
digs/wef/2026-08-17-wef-data-equity-2023-pdf-affiliation-closure-depth-3/README.md
digs/wef/2026-08-17-wef-data-equity-2023-pdf-affiliation-closure-depth-3/starintel-documents.jsonl
digs/wef/2026-08-17-wef-data-equity-2024-roster-continuity-depth-4/README.md
digs/wef/2026-08-17-wef-data-equity-2024-roster-continuity-depth-4/starintel-documents.jsonl
digs/wef/2026-08-17-wef-data-governance-council-member-carryover-root/README.md
digs/wef/2026-08-17-wef-data-governance-council-member-carryover-root/starintel-documents.jsonl
digs/wef/2026-08-17-wef-data-policy-2020-2021-roster-expansion-depth-1/README.md
digs/wef/2026-08-17-wef-data-policy-2020-2021-roster-expansion-depth-1/starintel-documents.jsonl
digs/wef/2026-08-19-palantir-identity-hq-staleness/README.md
digs/wef/2026-08-19-palantir-identity-hq-staleness/starintel-documents.jsonl
digs/worldcoin/2026-08-20-request-2095-control-biometric-token/ORB-SMPC-DEPTH-1.md
digs/worldcoin/2026-08-20-request-2095-control-biometric-token/README.md
digs/worldcoin/2026-08-20-request-2095-control-biometric-token/WORLD-ID-CONTROL-DEPTH-1.md
digs/worldcoin/2026-08-20-request-2095-control-biometric-token/starintel-documents-orb-smpc-depth-1.jsonl
digs/worldcoin/2026-08-20-request-2095-control-biometric-token/starintel-documents-world-id-control-depth-1.jsonl
digs/worldcoin/2026-08-20-request-2095-control-biometric-token/starintel-documents.jsonl
digs/worldcoin/2026-08-25-request-2095-harvest/starintel-documents.jsonl
docs/auto-dig-requests.md
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
scripts/auto_dig_request.py
scripts/company_public_hq.py
scripts/generate_dnc_key_people_wef_accountability.py
scripts/materialize_harvest.py
scripts/scrape_fbi_procurement.py
scripts/scrape_tsc_job_postings.py
scripts/scrape_usaspending_award_transactions.py
scripts/scrape_wef_council_artifacts.py
scripts/sec_principal_office_history.py
scripts/seed_flock_dunwoody_mjcca_camera_access.py
scripts/seed_palantir_current_news_pass.py
scripts/seed_palantir_sec_principal_offices.py
scripts/sync_flock_locality_issues.py
skills/validate-starintel-changes/SKILL.md
tests/test_auto_dig_request.py
tests/test_canonical_dataset_roots.py
tests/test_company_public_hq.py
tests/test_scrape_fbi_procurement.py
tests/test_scrape_tsc_job_postings.py
tests/test_scrape_usaspending_award_transactions.py
tests/test_scrape_wef_council_artifacts.py
tests/test_sec_principal_office_history.py
tests/test_sec_principal_office_real_cover_shapes.py
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/auto-dig-failure-report-check.yml
.github/workflows/auto-dig-prolog-actor-check.yml
.github/workflows/auto-dig-prolog-actor.yml
.github/workflows/auto-dig-prolog-failure-report.yml
.github/workflows/auto-dig-request-check.yml
.github/workflows/auto-dig-request.yml
.github/workflows/dnc-key-people-wef-accountability.yml
.github/workflows/fbi-procurement-collector.yml
.github/workflows/flock-dunwoody-mjcca-one-shot.yml
.github/workflows/materialize-harvest.yml
.github/workflows/palantir-sec-principal-offices-one-shot.yml
.github/workflows/sync-flock-locality-issues.yml
.github/workflows/upgrade-prolog-rlm-298.yml
.github/workflows/validate-db.yml
scripts/auto_dig_request.py
scripts/company_public_hq.py
scripts/generate_dnc_key_people_wef_accountability.py
scripts/materialize_harvest.py
scripts/scrape_fbi_procurement.py
scripts/scrape_tsc_job_postings.py
scripts/scrape_usaspending_award_transactions.py
scripts/scrape_wef_council_artifacts.py
scripts/sec_principal_office_history.py
scripts/seed_flock_dunwoody_mjcca_camera_access.py
scripts/seed_palantir_current_news_pass.py
scripts/seed_palantir_sec_principal_offices.py
scripts/sync_flock_locality_issues.py
tests/test_auto_dig_request.py
tests/test_canonical_dataset_roots.py
tests/test_company_public_hq.py
tests/test_scrape_fbi_procurement.py
tests/test_scrape_tsc_job_postings.py
tests/test_scrape_usaspending_award_transactions.py
tests/test_scrape_wef_council_artifacts.py
tests/test_sec_principal_office_history.py
tests/test_sec_principal_office_real_cover_shapes.py
```
