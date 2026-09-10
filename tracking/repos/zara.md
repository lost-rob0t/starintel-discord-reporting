# lost-rob0t/zara

- generated: `2026-09-10T11:25:21Z`
- canonical branch: `master`
- changelog eligible: `yes`
- head: [`f8394af0ba8cfd222d94a5c2bff1555d60161694`](https://github.com/lost-rob0t/zara/commit/f8394af0ba8cfd222d94a5c2bff1555d60161694)
- head date: `2026-09-08T22:31:27Z`
- head subject: release: Zara v0.1.1-alpha (#665)

## Git log, last 14 days

```text
2026-09-08 f8394af0ba8cfd222d94a5c2bff1555d60161694 release: Zara v0.1.1-alpha (#665)
2026-09-08 291f5e3474c33911dfd1ead833230fa8c4c71e4b fix(client): use the configured Zara daemon by default (#664)
2026-09-08 c6a557964f11f892aaa984ad52a2e5b1b2e829f2 Merge pull request #661 from lost-rob0t/ui/650-outrun-shell
2026-09-08 de1543adefa5b6c009dc7a4e80a848bd1a2d171d test(android): drop stray blank line at eof
2026-09-08 e4ff21def40cde100d5fb6f39a178a7c5e04d793 fix(android): match system bar icon contrast to the resolved theme
2026-09-08 501456994a3221f8a982a5d99ef0aa96f9f964cb fix(android): keep shell below system bars and make drawer routes scrollable
2026-09-08 c336f7260ba76ea6221bd6cf7e7c71c141c36d35 feat(android): wire themes surface with persisted immediate token switching
2026-09-08 2429cba429fc42f72d994b981ee5ee66f9a37da4 feat(android): resolve all frozen themes through one semantic hierarchy
2026-09-08 d160c600860c7904fb26315a30a25d26b74d04ec fix(android): isolate interop fixture lease from the running user server
2026-09-08 2581875a8c3cd37b5789c320ede0c2f49a446d22 test(android): make device navigation scroll in both directions and record geometry
2026-09-08 01fd38f4191602f801c1c9eef6481249b259cfce test(android): add installed-device drawer and theme screenshot acceptance
2026-09-08 c843b944e534aff943c997cbb53f6015ebce87b6 test(android): specify frozen theme palette and reduced glow behavior
2026-09-08 5814288fbe8997937e6407714997e98c324b2a1e fix(android): remove inaccessible Compose weight import
2026-09-07 d85362851cc5f18e91b38506478b59eceb20fb6d fix(android): remove platform light action bar
2026-09-07 d4e0e5dc3f816bc733fd88d692e74fe15590161d feat(android): replace generic shell with Outrun drawer UI
2026-09-07 4e75e362355c544deb0153fdfb9a348f719f0e80 test(android): freeze Outrun drawer shell expectations
2026-09-07 fe6e8eee30d6beb153c2a399a79d325e017f2b02 fix(tts): stop idle zara-server CPU busy-spin (#660)
2026-09-07 80307569fd13cd047d4cc6fbe834c8bb507f6624 docs(android): freeze canonical symbolic workspace design (#649)
2026-09-06 207e3b689399464de413d3faba7c2ed763168ca3 release(android): prepare v0.1.0-alpha APK (#618)
2026-09-06 b09b6e6fcc2225118fe80f0a038bedad6f5df80e Merge pull request #617 from lost-rob0t/rage/core/324-expanded-history-sidebar-r2
2026-09-06 12bf147480cc6b088524eee793248dee7e2701e0 fix: place expanded history beside canonical chat
2026-09-06 a34929130fd5770b8bd16e7bbdbf2b5500dc46c1 rage: record #324 deterministic RED evidence
2026-09-06 07a0c5eb04f27f8f8ed8657d5f6c6d6cba6db313 test: recover #324 expanded history sidebar RED
2026-09-06 95bf75613782b2710b1a978645f6145d438b5e0d rage: recover #324 sidebar slice on current master
2026-09-06 89e67acae248960e80314de02fcd368c84d1b298 Merge pull request #613 from lost-rob0t/rage/android/175-route-stop-retry-r3
2026-09-06 c97d5fd6eedd3aee591411f6aeb858e0d0eccf42 test(android): recover route teardown retry acceptance on current master
2026-09-06 146db040fcd6bed8d0c4402777f48059e6f1386c fix(android): recover retryable audio-route teardown on current master
2026-09-06 c549491b24a116985f095641cc800bececf03478 Merge pull request #610 from lost-rob0t/rage/575-transient-send-backpressure-r3
2026-09-06 607f338f75f2a8f10740196915a50f90b81e0b5a rage: record #575 GREEN and payload coverage
2026-09-06 9ebb31c96c5ff3fc0fdfefee3bcecc330016590a test(zmq): cover payload-safe FIFO backpressure recovery
2026-09-06 c939aa8cd1fbbce49215fddd6d3af01ea32f4836 fix(zmq): preserve live routes across transient backpressure
2026-09-06 1e636b68b8f186826fff17a68513643c7be7d91f rage: record #575 transient backpressure r3 design
2026-09-06 9756f083e2ef553d295e7e0c7060b7330ada6422 test(zmq): split transient and permanent send failures
2026-09-06 2574d0251d15c8fd6485eafa2b7e163d881a18ec test(zmq): recover transient ROUTER backpressure RED
2026-09-06 461eed70d1fd0efc26d90091b5171c973cba3c69 Merge pull request #606 from lost-rob0t/rage/android/175-sink-self-close-r2
2026-09-06 2c19843d9d50f6ebf5d112ca72b001ee9b632bee fix(android): prevent voice sink observer self-close deadlock
2026-09-06 8e86ec81c1341c6544ac27b1949dea6069b946ed test(android): require sink observer self-close to return
2026-09-06 0771d0161c5607d3bbf57c56a02afb6491e6b275 Merge pull request #603 from lost-rob0t/rage/android/175-audio-focus-sync-loss-r2
2026-09-06 c348e2db6b0325ef9b7f3ded06f8c51e69302922 fix(android): recover synchronous audio-focus loss hardening
2026-09-06 fc6875aa95115ef4b098486cbd2c0bfa591a5272 Merge pull request #599 from lost-rob0t/rage/android/175-recover-stack-current-4
2026-09-06 ed2cca33fee2091d7b96e3b412afcc75e7790737 rage(android): recover verified voice hardening on current master
2026-09-06 61ab916cf6546b7cc917c3d22e9c4a7c7dbe149c Merge PR #596: recover verified Vulkan dictation backend
2026-09-06 e53010f21a78cfc2255121db060b8efdc403f76d fix: recover verified Vulkan dictation backend on current master
2026-09-06 b1c5218d823304b950e95b3bcea94482162ad264 Merge PR #589: characterize ToolCall forwarding
2026-09-06 16d0f88d24f875604c5e7b71bd061b00d7ae1f00 test: recover #388 r17 on canonical #575 diagnostic master
2026-09-06 6d8fa68a63218bc14934bac75b23fb3a996963ba Merge PR #585: expose bounded gateway send-failure diagnostics
2026-09-06 2e59e1cdd0c03f34bc583ffa703717df5c111d05 test: recover #388 r17 ToolCall forwarding characterization
2026-09-06 1c3d87b89078f85a2fd7dcd472a28eef9182d409 fix: expose bounded gateway send failure [rage-575-green]
2026-09-06 38ea9c7bab6945b16b725686d565e974aa6cae3f chore: apply #575 green on exact-current recovery
2026-09-06 a9816e1dbceadd895f12c257f891f94e75e4a45c docs: recover #575 RAGE evidence on current master
2026-09-06 c32adb10455f3a4f58ef64eef138b913d6136f8d test: recover bounded gateway send RED on current master
2026-09-06 e6c90b274d285444520bd8372efe396c5f4cf24f Merge PR #578: preserve stock interop diagnostics
2026-09-06 8beddd4ba8c4fdeb9e8e82f22647ed37e908b48a RAGE #388: pin r17 forwarding characterization
2026-09-06 028b3451dc437e828c54f15111e0df43d5a89916 test(#388): characterize whole ToolCall forwarding wrapper
2026-09-06 a9f0e7a056f90655a062ebe976f553dd91a3e2f5 RAGE #575: recover green diagnostics evidence on current master
2026-09-06 c3290b6f96fb0c17b815c4441e35fd0a4ed888cf test(#575): require stock-server diagnostics on Gradle failure
2026-09-06 9c4e9d488b90ce36cbab08a81cb9e7ddf3dfb384 fix(#575): preserve stock interop diagnostics on gate failure
2026-09-06 bea53760a6c1e91bb0671a509985498d760a49d5 Merge PR #569: characterize ToolNode dispatch boundary
2026-09-06 ea00e250489493ff4e717ca97af905d89a461a5d test(#388): exercise ToolNode through compiled graph runtime
2026-09-06 dd439a30946c9776e80e671f71bce251c544da31 RAGE #388 r16: characterize ToolNode public dispatch boundary
2026-09-06 d0d6fa8562fa1b4df9d677e392420605ca1d903c RAGE #388 r16: record exact dispatch isolation start
2026-09-06 2da13cb08d15f268e355171ba56f0decde238126 Merge pull request #564 from lost-rob0t/rage/324-independent-geometry-r2
2026-09-06 84003e34772b0df01fd57c54c2338cb3f3423296 test(copilot): prove independent compact and expanded geometry
2026-09-06 838bf374b1bd0328834a1997f7e3c20c5d8eb567 fix(copilot): restore independent presentation geometry
2026-09-06 47381e446e42e1332c96833ab0b958430ea42962 Merge pull request #558 from lost-rob0t/rage/324-screenshot-provenance-r1
2026-09-06 0152aa9a2ab2c8b41f66cfc1fba56ec41c1fb948 RAGE #324: recover screenshot provenance onto current master
2026-09-06 dcfff6cc75ef5b672e2ce4abc93bc7b57ae7633a Merge pull request #552 from lost-rob0t/rage/324-history-parity-r1
2026-09-06 68c8967ab21d17dad4d8ea3f9f72936c0a76a568 RAGE #324: stamp screenshots with reviewed source head
2026-09-06 624fd0fd95bcb625bf329ba9d4f80277f01b1645 RAGE #324: require exact PR-head screenshot provenance
2026-09-06 e770c8c9c4bc99e7e560cea6d10e88f0da5078dc RAGE #324: record screenshot provenance correction
2026-09-06 be36e90b466fb20d9c79a8b291f0dcb61cf85d2d RAGE #324: add expanded conversation history projection
2026-09-06 99794ef7198028b8d95ecbd517c0b7fee37ee3a1 Merge pull request #551 from lost-rob0t/rage/324-screenshot-ci-r1
2026-09-06 b1ca89d52e0ffc84f8ad6eb18987f3f77fc841e5 Merge pull request #550 from lost-rob0t/rage/324-unified-copilot-r4
2026-09-06 af5d617e892b514a7ad6cd77a021511e1647e63a RAGE #324: add RED expanded history parity
2026-09-06 466427ff740c44397387102ffe15ccd15313a717 RAGE #324: design expanded history parity slice
2026-09-06 01e45f6ec7b1eb24a283917f0820431f8d4e3ed5 RAGE #324: record screenshot CI RED/GREEN slice
2026-09-06 ba1c796ccef9ef38ac01107b5ca393d173a78238 RAGE #324: render deterministic Copilot screenshots in CI
2026-09-06 e26d36a62dbc458d601a5a94b4b882108da16922 RAGE #324: add RED screenshot CI invocation contract
2026-09-06 60acf0c7a666837e66477c4c8edadd2c92d6bd15 RAGE #324 r4: recover adaptive Copilot onto current Android master
2026-09-06 3533308b391079171cd9dd5ffe4ad6e0231da06f Merge pull request #542 from lost-rob0t/rage/178-voice-stream-json-depth-r5
2026-09-06 96fc32fba5790eea6a767d2080a82ad5dd061cc8 RAGE #324 r3: recover adaptive Copilot onto current master
2026-09-06 ea41dad2f0000dc95ca5a2148014d58a530261e5 fix(android): recover voice stream JSON depth bound on current master
2026-09-06 f4b17bde742cca416728d6edc3f5dc1d19784bc6 RAGE #160: semantic-first runtime and timer CLI regression (#541)
2026-09-06 2a4cb38a820832e08ed3de200b0d53a3a5b6614b Merge pull request #536 from lost-rob0t/rage/178-voice-ack-json-depth-r3
2026-09-06 d1c95f0cd2d5ee295b97b7df46a1debbad57f825 RAGE #324: retire dual-renderer handoff assumptions
2026-09-06 9491a460f4fe2d031119d2273fb32e279f5a19d3 RAGE #324 GREEN: project complete canonical conversation
2026-09-06 ad85b9eada47e1c6c1d4ea18b31eecdf6db0817e RAGE #324: expose projection policy seam
2026-09-06 0b785f868493f9e12a1ee17a341862b08bbbd1c2 RAGE #324: restore desktop diagnostics signal
2026-09-06 175ae929e890b2720ad68bb6c5a390ff53988a5b RAGE #324: restore canonical desktop restart signal
2026-09-06 a4167b4226c48c3d4ace7d8b0018a012258d9c7c RAGE #324 RED: require full conversation projection
2026-09-06 1baa5ff059685539ab6c9b897e46e2abc6be38bd RAGE #324: design canonical full-conversation projection
2026-09-06 32cc8d2718476145c17efb97359500cca54301ff feat(#324): collapse desktop ownership to one Copilot renderer
2026-09-06 ddb41dea063be497b8bc0e05d81a69d1a857734b test(#324): require one process-owned Copilot renderer
2026-09-06 56e93635766a6e3514f34bccfac313d8a05d662f docs(#324): record screenshot fixture GREEN
2026-09-06 8ff01894a15b2f032b1975b6ec01fd8f11eae445 feat(#324): render deterministic Copilot screenshot fixtures
2026-09-06 009daf9b092f78ed3de29e74b9f149ddf69bcb1c fix(android): bound voice acknowledgement JSON nesting
2026-09-06 b6e03355b9938a6444caa9587d49519f261e8283 test(android): preserve voice acknowledgement JSON depth bound
2026-09-06 a8641c410407a79cdb8d8dff35f4d041b3c0eb94 test(#324): fix adaptive fixture request identity
2026-09-06 56fdffa5eee7361ec16501d1c0c447134d80507a test(#324): define deterministic Copilot screenshot RED
2026-09-06 5dab4f2a01285b34db7f32da5a71fc3b4cecbec1 rage(#324): record adaptive Copilot RED and GREEN slice
2026-09-06 3ace55d7b9957b7a932e4201e371c28e2d697405 feat(#324): export adaptive Copilot surface
2026-09-06 d4d75d46e74bab5fbcf178ea463bc720b81f5282 feat(#324): add single-renderer adaptive Copilot seam
2026-09-06 38e550dfafd8e1a9a2f4533de2335825ec082606 test(#324): define adaptive Copilot presentation RED
2026-09-06 b5794db14ad41137c06d20c0e67645175643cb95 rage(#324): reconcile exact-current adaptive Copilot design
2026-09-06 fa0374289e22e9f6ab5d95dae103a2af900c3c18 rage(#324): record exact-current r2 transaction
2026-09-06 c2d903fd5cf08e2d28e006cec021309142bf6834 Merge pull request #529 from lost-rob0t/rage/492-device-action-replay-r6
2026-09-06 c956d238c4d6d338d88eb1415e6d79e1fc8bb82d rage(#492): recover exact green replay contract onto current master
2026-09-06 23260e1598c85641effae3ec573ff66930cdc2f0 Merge pull request #530 from lost-rob0t/rage/178-voice-hello-json-depth
2026-09-06 aec46b3ef543ee2a6858c7faee705fa0f984c1c0 RAGE #178 GREEN: bound voice hello JSON container depth
2026-09-06 32b9727baeda389c233a92aaaf1dfcd734c6404b RAGE #178 RED: prove voice hello JSON nesting is unbounded
2026-09-06 e13a67df2bd3bb8b84b4e64f6e632dcb10e9063a RAGE #178: record Android voice hello JSON depth slice
2026-09-06 f8ba7eb9f891eddb54de71390dd942567a8866fd Merge pull request #527 from lost-rob0t/rage/178-capability-json-depth-bound
2026-09-06 ca6dd5bf775c742b38177c0d6509949e284e9485 fix(android): bound capability JSON nesting
2026-09-06 6b71e056f5003b5b1297525d47fd3e0f63de5220 test(android): expose unbounded capability JSON nesting
2026-09-06 52109e8a3a43461278e689cfe8964bace48cce2f rage: start Android capability JSON depth slice
2026-09-06 20e7ce159009accad9a1aeded424f566835df355 Merge pull request #525 from lost-rob0t/rage/178-android-daemon-restart-stale-turn-r2
2026-09-06 9b2508bd09feb1656d97bbce081c13e95abd1815 test(android): expect stale text turn to fail closed
2026-09-06 b2071ba7e90dd3fcd6d3e8031771aac8ada72106 docs(rage): record stale text-session recovery evidence
2026-09-06 47888f36e7434309588e08592c2df60674c2415a fix(android): fence stale text turn completions
2026-09-06 ef0b4eada009a80c4470c1729d3c7c8f7520bded test(android): prove stale text turn fails after daemon restart
2026-09-06 7a6b3cf6a9f524e29dcd6da624ec76fd6c89e749 Merge pull request #522 from lost-rob0t/rage/178-android-json-depth-bound-r2
2026-09-06 31c4eed35bf10bfaa3b690fe3b09fd4132b05e25 RAGE #178: record JSON depth RED and GREEN
2026-09-06 365b25a4358fd304e8f1af8a70b2b043a9074215 RAGE #178: pin JSON nesting boundary
2026-09-06 71a6e07887f11d2a1dd41b0ea4e5701eceb2d5dd RAGE #178 GREEN: bound strict JSON container depth
2026-09-06 115a5eea76dfe6de5f2cbf53dfd0925c3d19a4d8 RAGE #178 RED r2: prove bounded JSON nesting
2026-09-06 3634d19a72d943804e5400c2d87dad5d397c2523 RAGE #178 r2: recover JSON depth-bound evidence
2026-09-06 b4f6297d70543be674fd2c6ef0769499eb77955d Merge pull request #520 from lost-rob0t/rage/203-android-playback-session-invalidation-r3
2026-09-06 f613455f183b3c0577525e314838e381db2b9d22 RAGE #203 r3: recover stale playback invalidation
2026-09-06 98360054f80dda5b93669c7a44ba268ae52c0927 Merge pull request #518 from lost-rob0t/rage/178-android-audio-payload-bound-r4
2026-09-06 9c4b31adb76eedc68620f33e05d54a94d6df9511 RAGE #178: restore inbound audio payload regression
2026-09-06 6154c964054f06e68bca1bbe23f5e8402160b5c4 RAGE #178: recover bounded inbound audio payload
2026-09-06 a5eb7dc55af207bd4936d15475c70b7742a692bb Merge pull request #514 from lost-rob0t/rage/203-android-ui-close-runtime-ownership-r3
2026-09-06 3d23655c0420a1e82fd7909ac225c920e99407e9 rage(android): recover UI-close runtime ownership evidence
2026-09-06 0f3a7a95b004614f788dcf8b59ba158cb8e6980d test(android): preserve app-scoped assistant runtime ownership
2026-09-06 457c8cc6e489e4a38bdf0bc4acd0b822a3f43b3a Merge pull request #510 from lost-rob0t/rage/178-android-uri-intent-abuse-r4
2026-09-06 3b71c2195425f09afdbdec61aca2dfddf4c3382a docs(rage): recover URI proof after Android merge
2026-09-06 6424e9f8098e998c33bf541be90018e8deb69621 test(android): recover URI launcher intent contract
2026-09-06 5f17f167850c87fe04ca30a525819b2d2a11ae98 Merge pull request #505 from lost-rob0t/rage/178-android-no-raw-logging-r5
2026-09-06 f9021ffa943d8799164d37e1d58db1d83dd9cdfc docs(rage): recover Android logging proof on current master
2026-09-06 17b3b3169086d1158026bf3b946dc4807430b725 test(android): forbid raw production logging sinks
2026-09-06 93e6bc371c866eed9cc52b3169bf35a8d8dbb74c Merge pull request #504 from lost-rob0t/rage/218-normalizer-config-r4
2026-09-06 bcd35a0067060fd6346d19153621f2341ac1f4a5 docs(rage): record #218 selection RED and implementation
2026-09-06 af4e54449f7d34efb9c17083f1351f490f61d193 feat(config): add canonical normalizer selection diagnostics
2026-09-06 4e8ad347c1fdedc0a16f67c4e8e3d31f2741485f test(config): bind selection to existing ZaraConfig authority
2026-09-06 31e665b7edb865a8cc45698af6b1ec616dabeaf1 test(config): require canonical normalizer selection diagnostics
2026-09-06 de59f3b06d4893aaaf40c2880a10e29df4301ca8 docs(rage): record #218 r4 recovery
2026-09-06 aec29fb20439b280293a83a46315e0ded4e44926 feat(config): recover transcript normalizer descriptor
2026-09-06 91d6ad7b3ce8dfceaf65028e41066edbcb8b27c4 test(config): recover transcript normalizer acceptance
2026-09-06 4cd2f44eb76bb3f1f648cbbefddf57b4a6fb0b09 Merge pull request #498 from lost-rob0t/rage/178-android-prolog-lifecycle-r3
2026-09-06 4ac1d4c68f4c65ad708773ee098ad8be475cec6f docs(rage): record Trealla lifecycle r3 recovery
2026-09-06 b7f32d04c9fcd3b5fc53217ed439d602a5be212a test(android): stress Trealla lifecycle ownership
2026-09-06 fd91a74e05e28371d903d44256d10c8a29ba5134 Merge pull request #495 from lost-rob0t/rage/178-android-principal-target-abuse-r2
2026-09-06 553d65166d7de58c4ad2c7ad625b5f73051fac6a docs(rage): record #178 target injection recovery r2
2026-09-06 e78d59a4d7b3e0b2edce38708b12940fa95dd084 test(android): reject payload supplied principal and device targets
2026-09-06 ceae9662a2462991c8b964eac33bb31e32d0ab39 Merge pull request #490 from lost-rob0t/rage/178-android-device-action-replay-r4
2026-09-06 f555f7d1b5a0984b0bb1e10528b699c66cd4bc36 docs(rage): record #178 device-action replay recovery r4
2026-09-06 5972f534155f2b67025526f0c23798f037c699d0 test(android): prove stale and replayed device actions fail closed
2026-09-06 77c1c1ac12b159e4e2b8ccc2a87fee53dfb6ec9e Merge pull request #488 from lost-rob0t/rage/178-android-capability-revocation-r3
2026-09-06 2c9c488a228dd3943401417f08c99eefedfa14f6 docs(rage): recover #178 capability revocation proof
2026-09-06 72030d9b232c090143feac54ed44122424a13f8d test(android): prove revoked capability cannot execute
2026-09-06 9de82e4f3b6691cdcdcbc57c302cdef17d864852 Merge pull request #485 from lost-rob0t/rage/178-android-auth-revocation-r2
2026-09-06 c63e1b3a106c7845665ffe0218a6313a0ff6bea2 docs(rage): recover auth revocation proof on canonical head
2026-09-06 42bf7cbf377f82c802b3c4d7fc318fcd1ebe5ca4 test(android): prove credential and pin revocation fails closed
2026-09-06 2fca33b9caa288df8a0cc61bf582379333de1ede Merge pull request #481 from lost-rob0t/rage/178-android-reconnect-storm-r3
2026-09-06 aef74ca03e040ddc2256c9b9ab1e638593c9e102 docs(rage): record reconnect-storm exact-master recovery
2026-09-06 37f49b45dcdcfe6fe30431c6a6952ba5f718cbd5 chore(android): keep reconnect regression diff reviewable
2026-09-06 c7477d13e810b1a4ffa4178f71e0ccb29d9b29ca test(android): prove reconnect-loss callbacks are idempotent
2026-09-06 ccbcebff816f1d6e7dc6f5b68e7329484ebc3f0a fix(android): make duplicate reconnect loss idempotent
2026-09-06 e1b86f17debe88f6d7190379b0ae3f1522d70b29 Merge pull request #477 from lost-rob0t/rage/217-s1-mini-normalizer-r4
2026-09-06 8ce9dec768546af648e72c5144ed73c09e192fb0 docs(rage): record #217 exact-master recovery r4
2026-09-06 2368b0a3735e209e750f4c9cc6441c7c68b28b41 test: compose #217 into repository gate
2026-09-06 f3bb290c64faef686c73332a9cc3f3a357804f36 test(normalization): restore focused #217 gate
2026-09-06 51611d0357bf1fdfaf030a9156149fbe5081ae67 test(normalization): recover #217 provider acceptance
2026-09-06 ac21941cfcaf0eb2b0ab2a9cb8a5c25102d57130 test(normalization): recover #217 numeric bounds
2026-09-06 192699962428ca0d19dd6a3f15b5f6d63baea7fa feat(normalization): recover S1-mini provider for #217
2026-09-06 9ac0e0c0b94f571d6cab69ec252bb69ac2db3420 Merge pull request #473 from lost-rob0t/rage/178-android-release-matrix-r1
2026-09-05 2f3d01d9734db910fdd2beda61ef9bac8f559f7d android: add exact-head release gate manifest
2026-09-05 d9b1f660c978db9061b0c88418e2b9fe07df8ce9 rage: start #178 Android release matrix
2026-09-05 a88ad71d5b81e83cf32e20bf26c6d592f947a4d2 Merge pull request #471 from lost-rob0t/rage/203-android-recorder-failure-diagnostics-r3
2026-09-05 c3dce0e031e3c420d817ffb2ca4a900e7ba46423 android: recover recorder failure diagnostics onto canonical role-loss head
2026-09-05 c4a3afba72a63f4b1e3a39058a3dc1172cfcb64a Merge pull request #470 from lost-rob0t/rage/203-android-assistant-role-loss-wiring-r3
2026-09-05 bc26d04e470ec7403d0d9d79b94a40449fc0d4ad android: recover Assistant role-loss ownership onto current master
2026-09-05 f34084ecacec9ef39f3b421ec1a1e772b46ca652 Merge pull request #468 from lost-rob0t/rage/216-transcript-normalization-contract-r2
2026-09-05 1c2d6d7fd5a91255ef031cad140ba2258dd911d8 docs: record #216 exact-master recovery
2026-09-05 4c9ed3ead595e5b12d4c4d8805c897b196a925af test: recover transcript normalization acceptance
2026-09-05 574ba4c41be74402b7ca478b4dcf9f987093c538 feat: add transcript normalization contract
2026-09-05 61f0f7977bc5ce8bd7bd9c4dd795ffb37600bf58 Merge pull request #464 from lost-rob0t/rage/203-android-reconnect-scheduler-failure-r2
2026-09-05 e0f742b33ce62501f62b8aadcdd37726143f2ddf fix(android): preserve focused reconnect reducer diff
2026-09-05 09b59fe839d8c42de8d419654a015812853874f2 docs(rage): record reconnect recovery transaction
2026-09-05 11e2ab67f23e7266589c89600c55d716db926781 test(android): cover reconnect scheduler rejection
2026-09-05 fa6326b479105405ba5c34132c1ed9d0841eb2e1 fix(android): handle reconnect scheduler rejection
2026-09-05 4ad6849c95bfde99fab4c0743a3743c35cd236c1 feat(android): fail closed on reconnect scheduling failure
2026-09-05 2f4bd28a9428a117f986f06b025d1a35abf5124a Merge pull request #461 from lost-rob0t/rage/203-android-voice-session-invalidation-r4
2026-09-05 92e39dcfa9ae4866a455b8089e6b840ca626727f docs(rage): record #203 capture invalidation r4
2026-09-05 6832375c79ad89098edb5c619f721af4b17030c1 test(android): enforce capture invalidation publication order
2026-09-05 df3a5cc0569d5a791c26033faa3312724b195fc0 test(android): reject stale authenticated capture
2026-09-05 a22c10316fc07f98d219171089e8fcc1c964ffed android: invalidate capture before publishing runtime state
2026-09-05 b672841ae924fa958bcc6e3e10609c6e6535168b android: bind manual capture to authenticated session
2026-09-05 83890b69962364c11a281680febe8b1659f95fd6 Merge pull request #459 from lost-rob0t/rage/203-android-ui-error-redaction-r3
2026-09-05 e71638ec5f74a3d96ba800ef0a1efcc09d3e339f RAGE #203 r3: replay Android UI error redaction on current master
2026-09-05 9bdf9b8d4bcab37da80bbfb31f701e3021b0ef3e Merge pull request #455 from lost-rob0t/rage/203-android-audio-route-rollback-failure-r2
2026-09-05 c0577a2864f6ab12e3859773e074e49ac28aed89 docs(rage): record Android route rollback recovery
2026-09-05 1ca9a647b8b789aeeae94b28f5d0aab6fabc97e3 test(android): cover route rollback failure ordering
2026-09-05 7d69df7c33736c28a968e35c7f86882d1ade1688 fix(android): preserve audio route startup failure
2026-09-05 a3032be8e60220d2e34dc138db1f79a953355f92 Merge pull request #453 from lost-rob0t/rage/203-android-state-store-temp-isolation-r2
2026-09-05 7818594bf53dda9c2947e905450c5c6fa90d7975 docs(rage): record #203 state-store temp recovery
2026-09-05 62f26669005e28154bbfafde715340ac262e0dd8 fix(android): isolate client-state temp files per save
2026-09-05 5ecd8ddeaded04d9626a10297164b906701a61bb test(android): reproduce cross-process state temp collision
2026-09-05 28f8afea91f8e3f389d9a28df6fe8089f56f86f4 Merge pull request #433 from lost-rob0t/rage/203-android-voice-runtime-invalidation-r2
2026-09-05 86bbc9908064bc3f723f50bf7aa98cccdf715895 docs(rage): record fallible playback close ownership hardening
2026-09-05 8b51533264f7c42c19cbcb7896484d06d2de1953 fix(android): detach stale playback before fallible close
2026-09-05 393891dfdb77c82152b244178efe7bb3218c3410 test(android): prove failed playback close cannot poison ownership
2026-09-05 fe00e2da56e12e083a8f4dc48fc5ad316c2f0def Merge pull request #443 from lost-rob0t/master
2026-09-05 15499557e5994a05d57cc1c0a3ec97857939efda Merge pull request #438 from lost-rob0t/rage/203-android-connection-error-redaction
2026-09-05 3022b1a72301501429424e256e1d20189489a213 Merge pull request #440 from lost-rob0t/master
2026-09-05 31b91b8c0ef3360e9472eef91d7d5dff7b00d491 rage: record Android connection failure redaction
2026-09-05 64c694e9928d3058bcd16f80fca3274110f537e9 android: redact connection exceptions before reducer state
2026-09-05 4f3b15623da3bf62bbc174b07e11cff14666736e android: add bounded connection failure reason classifier
2026-09-05 d3e8a47462cb5491e64e81067eb0b115696ace30 test(android): require redacted connection failure reasons
2026-09-05 6dc76c474f26e51602a68af86df1812c1696ef65 rage: re-gate voice runtime invalidation on canonical #432 base
2026-09-05 0a370079f2bf293b320ea72865239e6ee4c08a73 Merge pull request #432 from lost-rob0t/rage/203-android-assistant-role-loss-r3
2026-09-05 fd50e9ba8e4fbeb76ac2e0d56bc5581b340959b6 rage: record #203 runtime invalidation recovery r2
2026-09-05 06cf0ee75dc81a07d11ecf9bc20c6e82497d7148 test(android): recover serialized voice sink reset coverage
2026-09-05 10ab5a76041c13f458526be56f061627190d4d34 test(android): recover stale voice session policy matrix
2026-09-05 8b467c88331a59093e8a92b4b6da9a7ebef63394 android: recover voice runtime session invalidation policy
2026-09-05 74fdcaf6540aca4b18e0958fc8ee923032d216c3 android: recover serialized voice playback reset
2026-09-05 c09a61bb772b406905ed267e5c227d4a84edb7c7 rage: record #203 Assistant role-loss recovery r3
2026-09-05 18332e3a169a1c122cda12b46dbeb3364f38c21e test(android): recover Assistant role-loss policy matrix
2026-09-05 715f7fe21c0262c45e3158b9e74174dc02d6404b test(android): recover Assistant role-loss guard coverage
2026-09-05 8021bc80e2043c4bf4bb013a6b9df65acc96b109 android: recover Assistant role-loss voice guard
2026-09-05 13cee05f2076c3c50dfe19937194fe3cdd5f63da Merge pull request #428 from lost-rob0t/rage/203-android-voice-diagnostic-redaction-r2
2026-09-05 ffd338b95f4829dd61f83e574bb51ea8fe69aca9 RAGE #203: record clean diagnostic redaction recovery
2026-09-05 cde0f7db8a99b617fd23b0393475973f05d680bc RAGE #203: lock redacted AppSession diagnostic wiring
2026-09-05 9c04a334a56041193df9c1749e2d243e94482560 RAGE #203: redact AppSession voice diagnostics
2026-09-05 ab8f7b4e999810088c4abc31bccc482a47abc25b RAGE #203: test redacted voice diagnostic failures
2026-09-05 c9c87cc44f68307f5b292fa700d957ed6f1e6d34 RAGE #203: add redacted voice diagnostic categories
2026-09-05 9cd82222375d1a4968babfa7f543fa7d9447d98e Merge pull request #408 from lost-rob0t/rage/174-android-open-app-aliases
2026-09-05 05b6b669422495799f9014098a3cf6a4ed7cbc4d Merge pull request #421 from lost-rob0t/master
2026-09-05 27cb2d85a51c735213d807bacfe38a4880994da6 Merge pull request #407 from lost-rob0t/rage/203-android-assistant-shutdown-fence
2026-09-05 a5a3c814c941e34c7da01ddc66fd3a13c680873e Merge pull request #416 from lost-rob0t/master
2026-09-05 8c343601b2c6ec5255bef04003d9d7a67af828b0 Merge pull request #415 from lost-rob0t/master
2026-09-05 dad880789e4bac67a7233ca67947511487dc588a RAGE #203: record exact green and ready-gate refresh
2026-09-05 bff04e48423fb4a9a935a8b69d980df33c701878 Merge pull request #410 from lost-rob0t/rage/29-streaming-tts-provider-recovery-r10
2026-09-05 2a1ab13ab22fe4e898873057a793f5b94141f1f2 RAGE #174: record open_app wiring GREEN
2026-09-05 299f204e5cc0a2097c89cd620d7f39e2feedc2aa RAGE #174: GREEN wire executable open_app capability
2026-09-05 14a291dcadbd52ff7297636e011f29c291099d53 RAGE #174: GREEN contain app visibility probe failures
2026-09-05 93e14ba1198478537d1111f27594a1e11f88ad6d RAGE #174: RED fail closed on app visibility probe errors
2026-09-05 aa7db5f7275ca15c02ac4f30f370c5586bef77fa RAGE #174: RED require open_app AppSession wiring
2026-09-05 e717afa63a4a494df047b6e5dd5a43494d494b73 fix: isolate transient TTS bootstrap failure by turn
2026-09-05 fcd0f7a8b24e0c8e5b1ebc55f2909b712dabf890 RAGE #174: cover typed open_app failure semantics
2026-09-05 57f2f9f87723afe40fe1b419c10c259e1430c926 test: prove transient TTS provider recovery on next streamed turn
2026-09-05 17f35a33ccb6a43639f4e040fafcdbc132c262c8 rage: consume #29 provider recovery on current master
2026-09-05 2f3b91cb405695bc0c3244b94a0bec2df14d9605 Merge pull request #409 from lost-rob0t/master
2026-09-05 b09de84dd8f6b2d7ae6ee284b9e95c4b97a3d6be RAGE #174: record open_app research and implementation
2026-09-05 7b6c205f2dcf0f93df862473f84de7b6e4462844 RAGE #174: declare closed app visibility queries
2026-09-05 998974b3c61232a109233aea0876d34796600d1b RAGE #174: add reviewed Android app launcher
2026-09-05 69ec9b2ba20f6a9375f6c2c438f174642403331c RAGE #174: implement closed open_app adapter
2026-09-05 6d3deec725072555741e23a9450bd29da1d0adb2 RAGE #203: keep VoiceInteraction service bound explicitly to shared AppSession
2026-09-05 5865920d1e2ec25ab3f150e3a1a625f5bdcd8160 RAGE #203: preserve explicit shared AppSession contract proof
2026-09-05 12c8945ec5b6aa2aa728c1598aa2bf95585018eb RAGE #174: consume closed open_app alias slice
2026-09-05 e4849fd17e8abf5ed63dc91286c66f50af70070d RED #174: open_app must use closed semantic aliases
2026-09-05 ada24b73ab599d417dfbda6c864854c19b3426e3 Merge pull request #393 from lost-rob0t/rage/203-android-mic-permission-lifecycle
2026-09-05 0d19f9d7f89febad4fc0721c73e1bea107ca676c Merge pull request #384 from lost-rob0t/rage/203-android-audio-route-lifecycle
2026-09-05 834fd28d94fb8f5a3827b3454b815421b91724f3 Merge pull request #381 from lost-rob0t/rage/175-android-audio-focus-lifecycle
2026-09-05 998211c7fe849d4de3e6f9d0b96d588966e1888c Merge pull request #375 from lost-rob0t/rage/174-android-device-capabilities
2026-09-05 614b9c2e04f0b1435d3b9e1f07efc9fc37431354 RAGE #203: record shutdown-fence RED and implementation
2026-09-05 4a740213be72736c37bd69ba5538cfc1dfe72925 RAGE #203: preserve stale-start cancellation failure evidence
2026-09-05 90891d5f5573ea58e21ecd1fe653edfd0b242a16 RAGE #203: invalidate assistant starts before service shutdown cleanup
2026-09-05 0369cb9fd15c72e77ea69e5c251a50346cce2c4b RAGE #203: bind assistant session starts to lifecycle generation
2026-09-05 1293278a216115eec09fa8af2d11f5efd3ac12b2 RAGE #203: fence async assistant voice start across shutdown
2026-09-05 e625cfe21d884d68b40a0a72bcf6a45918587337 RAGE #203: share assistant lifecycle fence across service and session
2026-09-05 83b16bec6d99c7e28fb3c559369278f9ddbf6f13 GREEN #203: add monotonic assistant lifecycle fence
2026-09-05 a4bcf97fb3ae424bba7c834b097ade30aab992e6 RED #203: stale assistant start must fail after shutdown
2026-09-05 96c02ceeaae0012ce13d36fa44ecd4a0ea7e07f9 RAGE #203: consume assistant shutdown fence slice
2026-09-05 c827a71d394a5c574bf6e85e8a14400d294b6d07 Merge pull request #406 from lost-rob0t/rage/203-android-audio-route-lifecycle
2026-09-05 41f42843cd9ef1c3643d055f33bccff1f5d40344 Merge pull request #405 from lost-rob0t/rage/175-android-audio-focus-lifecycle
2026-09-05 19039d590cb627b8eadfd03c4ea9a97be4686bb0 Merge pull request #404 from lost-rob0t/rage/174-android-device-capabilities
2026-09-05 7fdbf379272b2ffa8506f3bd65d7c663b8d0bf94 Merge pull request #403 from lost-rob0t/master
2026-09-05 efe112f74b130ec39e81f2fc538818895e790ea5 Merge pull request #390 from lost-rob0t/rage/326-desktop-toggle
2026-09-05 d2cdaf3bb3e3f42fc2d571b243fd6a741fc6d83f fix(#326): keep desktop control owner alive after liveness probes
2026-09-05 4d5f7cdd98db376e17c48a9c5a3a32be53fda175 docs(rage): record foreground-loss capture cleanup
2026-09-05 2b0c536e48f5aefcd1609d3aaf09560f86eb09d9 RAGE #326: record local owner contract and exact CI long-path recovery
2026-09-05 89ad28328298d3c818f8c96b3954a66bcd034952 feat(android): cancel manual PTT when activity stops
2026-09-05 5e5324d915707c632a82b82be29291b7ddd0deb0 feat(android): serialize foreground-loss voice cleanup
2026-09-05 ea1bd49bb6a70e4a2928e78ff20db80240b426d1 feat(android): cancel manual capture when host stops
2026-09-05 bfb3aaaa3c294464062d43c71056b8d8d4867220 test(android): red foreground loss cancels manual capture
2026-09-05 f812bd0739050c7fc22c7fee8a8d2d9ebe5606b1 docs(rage): record mic lifecycle production wiring
2026-09-05 c7510c075ed0b6564c4df088e095f18d25448449 RAGE #326: cover long-path fallback and stale endpoint parent
2026-09-05 15395fc4d677edab42ac8fc029cb0b29fe48c7d9 feat(android): reconcile mic permission on activity lifecycle
2026-09-05 e77924242ded113eb1d8570922a4a8c6bd5ba866 RAGE #326: bound AF_UNIX endpoint length with private hashed fallback
2026-09-05 599b9a7ce65f7268ecf4861d8de2979ffde37c93 feat(android): expose serialized mic permission lifecycle
2026-09-05 d16bfdca97cc408ebd0478d56215650607d0e3fa Merge pull request #398 from lost-rob0t/rage/174-android-device-capabilities
2026-09-05 fde5f05d48c9c50e854cba08a6b1e626c8194b42 fix(android): keep route shutdown failure-safe
2026-09-05 b583a4f92db3bbc807e8611e4d972fddf98156ed feat(android): wire route changes into canonical playback owner
2026-09-05 8d915c150d96bfe515ff5cd56670e6994cb5c655 Merge pull request #396 from lost-rob0t/rage/175-android-audio-focus-lifecycle
2026-09-05 5355a9001c0dce45a684f9b63776cea07e2de1c0 feat(android): wire audio focus into canonical playback owner
2026-09-05 73977ab47e75552037670addbcbf5709e340f63f Merge pull request #395 from lost-rob0t/rage/174-android-device-capabilities
2026-09-05 140fb65588be4facf1faf2c757f65a258f948109 Merge pull request #394 from lost-rob0t/master
2026-09-05 82f5e8d4c6042282707994810260be8ebd432985 test(android): prove revoke cleanup survives recorder stop failure
2026-09-05 946726a397688f32d3fae53284f137cea02ec0cc docs(rage): record mic owner correction
2026-09-05 5d3c9d03fc41bb73351ad5b5cfa783ded45e19d7 test(android): move permission lifecycle assertion to mic owner
2026-09-05 1dcf5d5e687464ce66a70b3270ec6386f674922a refactor(android): keep permission lifecycle at recorder owner
2026-09-05 f0ee6d33c71e07ba708d6a1bf5d7225c6cf0fc56 feat(android): route permission lifecycle through voice coordinator
2026-09-05 5f8fd492b026cc669f7d5833c774e481e5d478db test(android): red coordinator permission revocation path
2026-09-05 3dbd368f1000909d204132a9442e692ac2276a75 fix(android): make mic permission loss stop recorder owner
2026-09-05 ddd0038196a6a20b79548876a4eac76bcd8f7632 test(android): red permission loss stops recorder owner
2026-09-05 75bba4088e9aba98a6e0a7f0c7fbb4a59438d34b RAGE #326: add bounded toggle/show/hide desktop CLI
2026-09-05 2c455acc75b43bb8ece1e7f387af6fef1ec7649e RAGE #326: reserve one desktop owner before client startup
2026-09-05 ff3b833e196f50356c1b4effc0e975bebb75f342 RAGE #326: preserve desktop cleanup while adding local control signal
2026-09-05 1671c2e5b5a6f87f0e71ed1d46d62cf08255c360 RAGE #326: route local desktop controls onto Qt owner
2026-09-05 6b1bbc2497989e674d1047779c095e20f7712258 docs(rage): record Android mic permission lifecycle slice
2026-09-05 56278458c73380cb70eec0a55173cc10ac6e6b39 feat(android): cancel capture on mic permission loss
2026-09-05 a0bfbd2911edf30399c237174981aa441afdad30 RAGE #326: RED for CLI and duplicate-owner desktop control lifecycle
2026-09-05 4475031d3918b5294e6aa7551fe01407aa5e1538 test(android): red mic permission revocation lifecycle
2026-09-05 d9e88fb01833c9b55e34630f0d88697028de84c8 Merge pull request #392 from lost-rob0t/master
2026-09-05 6bbb8d62128ebe470f3c98cef1095e4fcdb6bf88 RAGE #326: prove failed duplicate cannot unlink live owner
2026-09-05 25bbd0bbfa1a3f80e4b471bf5563ce75a74199aa test(android): keep capability hello fixture canonical
2026-09-05 6ae5cb4c6e9f15ad50afc5280999e1e75bfdfa1c RAGE #326: make desktop socket ownership race-safe
2026-09-05 9c7372a452569dbed83a246ac3caa5b65ac3779b RAGE #326: implement bounded local desktop control socket
2026-09-05 596ab286d2179ec75060ec6b1288c7f5f6392dd9 test: require bounded owner-private desktop control IPC
2026-09-05 12aa5a88e01f5ca549f7533a1262190cfaa8f6f9 desktop: make tray primary activation a true toggle
2026-09-05 ca274ed7925d0c149cd87cc1ffc70d100253f951 rage: record #326 tray-toggle RED and repair
2026-09-05 d6e78031fbfc0bf7c9b1f9a78998681c0b2cbd2f test: require true tray toggle for Quick Copilot
2026-09-05 8299bba79fab04a787ffa4e7c74667c360adc6dc rage: consume #326 desktop toggle control
2026-09-05 3676fc7e452eab409305f62a826b9f0b1f9841d4 Merge pull request #383 from lost-rob0t/rage/29-streaming-tts-current-r7
2026-09-05 3237cc975be2bac08c0a337b0ad2a6f78f12cb49 Merge pull request #387 from lost-rob0t/master
2026-09-05 e5401970f8cded29db39b6e742c17454ec48a36e Merge pull request #386 from lost-rob0t/master
2026-09-05 f9b462d35d3fc8aafc7fff7b8dcbf50e380c4774 Merge pull request #385 from lost-rob0t/master
2026-09-05 3d5757ca54e6bc14ef3d93e1b360b1fe21060b8b RAGE #203: roll back failed audio route startup
2026-09-05 0b81b7f66ebc9c3be5d18665e47b107edb178d17 RAGE #203 RED: require failed route start rollback
2026-09-05 06e14764cf43bb804e734e8c92cf84a802905d55 RAGE #203: record audio route lifecycle slice
2026-09-05 38328c179051c60909e15cd6991b5f84723db94f RAGE #203: monitor Android output route changes
2026-09-05 46753ddc60d661e3e8887c0801f0ba9e62e98e45 RAGE #29: recover bounded streaming TTS lifecycle on current master
2026-09-05 2e64bb86f791b8709448ad035d97cafb05ea89a8 RAGE #203: add deterministic audio route controller
2026-09-05 bb5dfbcbbdaf42cfbdd0ecc5101c0cbfd171f5c5 RAGE #203 RED: specify Android audio route lifecycle
2026-09-05 b839268b4cd63b30da455734ba1346b0bee02f05 Merge pull request #380 from lost-rob0t/rage/371-plugin-approval-current
2026-09-05 aba41f81461d9ae22e06eb2034aadc7d07eecb65 RAGE #174: exercise capability negotiation with executable handler
2026-09-05 7db95db6108df0aa601a18bbaece661a9118667e RAGE #175: record audio-focus RED GREEN and deferred AppSession wiring
2026-09-05 8a9a969d611e156dc238938df4b721bffcc074a1 RAGE #175: abandon framework focus on loss to prevent stale auto-resume
2026-09-05 5c03e46d3205468ee74ee0eee6227324ee46d406 RAGE #174 GREEN: preserve raw URI escapes during normalization
2026-09-05 a633d9cec0f9cf3c5674a4d0d18c372f9d6bccb4 RAGE #174 RED: preserve valid URI percent encoding
2026-09-05 445c45f6076afb6416130b5adebe31099c764f39 RAGE #175 GREEN: make playback acquire and release Android audio focus
2026-09-05 8932eca947138a88f11f53bd2483a7a956b3d597 RAGE #175 RED: bind playback lifecycle to explicit audio focus
2026-09-05 45b23661f2b3109e8a415aafd878bc4ef31c2164 RAGE #175: add public Android AudioManager focus adapter
2026-09-05 96589e8cb9998647b1451dab7deaf5bed731ad83 RAGE #175 GREEN: add explicit audio-focus owner state machine
2026-09-05 05005e6b5dec1ac62f81969cf0e84730d0036dd3 RAGE #175 RED: require explicit Android audio-focus ownership state
2026-09-05 e481be426612afaf0f274b2acdd76973819df4b8 RAGE #175: audit residual Android audio-focus lifecycle gap
2026-09-05 8ab5a47bca3c426a0b0ca99d253def27df7c5178 RAGE #174: record registry and canonical actor implementation evidence
2026-09-05 0a343c43c852fb9a1d4bf479c25ecceb74d858c0 RAGE #174: advertise and execute real open_uri capability from app session
2026-09-05 036b599dfa2349a97db2935c004ffcf026cfe57e RAGE #174: bind registry to canonical device-action actor boundary
2026-09-05 52c7e3d95a2d9a193d7dd514045703f8d18406bb RAGE #174 GREEN: execute interleaved device actions on canonical actor
2026-09-05 4767d64847263ca3c734603b4f96621d51426a7d RAGE #174 GREEN: define canonical actor device-action handler boundary
2026-09-05 816ef34694480778a84a3d6ef6f98d494e68681d RAGE #174 RED: require interleaved action execution on canonical actor
2026-09-05 c814eecf64323b55a1913f81361d729657da879c core: recover #371 plugin approval contract on exact master
2026-09-05 d5c283997cc6995fbc8747241ef423c728e39209 RAGE #174 RED: derive handshake snapshot from executable adapters
2026-09-05 7e7eeac6a18af969621332aee93c784600af3219 RAGE #174 GREEN: implement strict device action wire codec
2026-09-05 ae6d34b195347582b739d69fe9bb409428fb1e55 RAGE #174 RED: require strict device action wire codec
2026-09-05 237771ba7438cae5acc2e2ecdb291ba88c4af8e5 Merge pull request #377 from lost-rob0t/master
2026-09-05 8b0bb2d011b74c2a1dc09bddd9a59fbc59e7efa2 RAGE #174: add constrained Android ACTION_VIEW launcher
2026-09-05 03143a3cd4990734e3f9afaf63462c8b03108337 Merge pull request #373 from lost-rob0t/rage/196-ui-closed-runtime
2026-09-05 288201a12a634f3a7cc6a985cf5b354145dd545d RAGE #174: keep registry test adapter executable
2026-09-05 3608cb36e78ec9779ef357f544dd73914eb55a53 RAGE #174 GREEN: make registry execute typed adapters
2026-09-05 5e7a39d88e6b6ec95fe1225e13e61c82395ef8c9 RAGE #174 GREEN: implement typed open_uri adapter
2026-09-05 a5b680c0a947d9fb05dd04e87a7802411370ea18 RAGE #174 GREEN: define closed typed device action outcomes
2026-09-05 ef0e5082f0c4664e019a97f92845c70196061616 RAGE #174 RED: require typed open_uri adapter results
2026-09-05 53f5bd73845ea14228b0094ba5751ab6c0a37784 RAGE #174 GREEN: add strict bounded open_uri policy
2026-09-05 a900a8b354f9b5da59115e072292c01b6ca85bfc RAGE #174 GREEN: add closed Android capability registry
2026-09-05 97de0a48759c8e2b5d0aea50784d57c0feaf14d2 RAGE #174 RED: require bounded open_uri policy
2026-09-05 8ebc039baa526faafa714d74e66796e967a29c78 RAGE #174 RED: require closed Android capability registry
2026-09-05 ca1cf26a537bf5cdd365bbeb2cdcfefabd3e26bd RAGE #174: record Android device capability research and design
2026-09-05 d5f9a57e437cee72e2dfeae97ed5124727608085 Merge pull request #369 from lost-rob0t/rage/196-android-assistant-role
2026-09-05 c9c432f692641df723fc341ca2d1cfdb64fea49c docs(rage): record rendered Assistant guidance slice
2026-09-05 0858604bc4c422b7baa920dc326c5ac066a07457 feat(android): render bounded Samsung Assistant setup guidance
2026-09-05 43897bdc79ffe236acea55524adafe26579691ee test(android): require Samsung Assistant guidance in Settings
2026-09-05 1abbfbe40cbafee50b99c66a626cb302c1351138 docs(rage): record UI-closed assistant runtime design and rejected auto-mic path
2026-09-05 30597abd6739f8963c50a6421a68cf42958538c5 feat(android): add explicit system-assistant overlay push-to-talk
2026-09-05 34b479da73a398b58d36f8c8cfa92fb526444ea7 test(android): require explicit VoiceInteraction overlay PTT UI
2026-09-05 f33d547a5e3f2ec1895615ffe2d16c47d098bb69 feat(android): model explicit assistant overlay PTT lifecycle
2026-09-05 ed1f7e89021424899a00b9ce2388f6d52eaa9c50 test(android): require explicit assistant overlay PTT lifecycle
2026-09-05 5b1f32e4a17fd8ad0e9ec9d8d6f1dbb8754d45aa feat(android): bind assistant service lifecycle to shared runtime
2026-09-05 7c8c59ee6e8b37fd27c725a279b7fff7e466a31b test(android): require shared service role and shutdown lifecycle
2026-09-05 0193a713bd8220f7bdcdbeeaa522fe825756b5fb fix(android): avoid duplicate assistant capture cancellation
2026-09-05 b6256bc828122a835270f11d3ccff05f36fea750 feat(android): single-claim assistant capture cancellation
2026-09-05 07bb81a8908d3740c4850d39e093c06853fdf125 test(android): require single-claim assistant capture cancellation
2026-09-05 4f74bff6c0b6684f20f4490e0f110281496e6dc7 feat(android): drive UI-closed voice through shared Zara session
2026-09-05 baf06e025069f41d47a184a28a7e3c39f918a31d feat(android): fence assistant invocation show-hide races
2026-09-05 a0bad7c6f578843428b66a9c732a9f8132428c7d test(android): fence duplicate and late assistant capture lifecycle
2026-09-05 bdaa690b66381610df664953ecaa6bd122d583ad feat(android): plan UI-closed assistant voice on canonical runtime state
2026-09-05 3d6a00ecc2863ed7103df3a192b9e40f1587a625 test(android): require fail-closed UI-closed assistant start plan
2026-09-05 7f75100265e5bca8a8948178be12e047721e3fc6 feat(android): detach Compose lifecycle from shared runtime lifetime
2026-09-05 885657805fdc440211ee38f3b59db6c544e69c53 feat(android): co-locate UI and assistant services in runtime process
2026-09-05 33f8bd9133d5c63dea11ff9a110772ca33ceb12d feat(android): own Zara session at application process scope
2026-09-05 bdff5bcd543dbf52e55b0bc1598c941fed954042 test(android): require one UI-closed assistant runtime owner
2026-09-05 d85fa83f47c9b372a9d7dd44363c6d33c1ed760f docs(rage): record Samsung guidance slice
2026-09-05 11f3d808486b2f26c2ac676bc23a41fc3b4760e3 feat(android): encode bounded Samsung assistant setup guidance
2026-09-05 9cc6ad40c90e54a0ce463a6e80622d6b75abece0 test(android): require bounded Samsung assistant guidance
2026-09-05 b7b144ac256be4a5ff7a9d48427a6740c16009c4 docs(rage): record role lifecycle hardening evidence
2026-09-05 d7893258c4ccfe124833848152773943334797af feat(android): recheck assistant role on activity resume
2026-09-05 0c6bddbd22c3bf506f24e0ddd9777e227608bd90 test(android): require assistant role recheck on resume
2026-09-05 95f4dbf158e15a000d323416a470f1261f6ba4fd docs(rage): record Android #196 assistant-role evidence
2026-09-05 fdaf8a4dd87d6ac3baaa8a4e10de982b43674e5b feat(android): wire explicit system assistant role request
2026-09-05 cd63eee181ed830151eaf2cec447c55f047a07d1 feat(android): bind assistant role to canonical app session
2026-09-05 6eac03ef965a311671ce68ba69870c4fabc58970 test(android): assert assistant result from observed role only
2026-09-05 63f6bfaa1984623209d8bad1d85820b76ee745fe refactor(android): make assistant role result a platform recheck
2026-09-05 c8778fe5ba1a055ab2fc786ddcd77e272711816d test(android): require explicit assistant role onboarding flow
2026-09-05 ec836e07ca8ea30f9406ef04336a7e69a039658b feat(android): render honest assistant role onboarding state
2026-09-05 4a9124a371f5c911117fdbd6b9c955b4a9421112 test(android): require honest assistant role UI projection
2026-09-05 bb983d62af63ea31928204e35ab3fa5720fcc541 feat(android): publish assistant role through runtime reducer
2026-09-05 262b15b93dd2eb08234b29063d414d1d0a45e5bd test(android): require canonical assistant role publication
2026-09-05 caa3ffd425ff28206c436ab2b82043ab1413acb9 feat(android): verify assistant role ownership after user result
2026-09-05 ea795271a1fa4159e86a8bc934962946af6e70c8 test(android): require fail-closed assistant role request result
2026-09-05 6c20074158902f839f4984b0bf55cc1887da1871 Merge pull request #372 from lost-rob0t/master
2026-09-05 b6d46352b30d26aa85fc5fe897c28204a345df4d Merge pull request #366 from lost-rob0t/rage/175-android-barge-in
2026-09-05 dab37719bf3388e020ffad8b892ea736fa08fe68 Merge pull request #355 from lost-rob0t/rage/175-android-streamed-voice
2026-09-05 e0170a59c2118148f05227329ee5e074b6d627ec feat(android): bind assistant role checks to RoleManager
2026-09-05 4a14b485301318f91e5e8087dbfc47a95c311eaa feat(android): register assistant voice services
2026-09-05 4e7b3d3a28342a734fa1a5b040154b7a79d5a7de feat(android): declare assistant voice interaction metadata
2026-09-05 0b64df678df90c1c6764dd01c01618bb8675f214 feat(android): add lightweight assistant session
2026-09-05 9f2ca554879808e224af793d1ab595b61cd365db feat(android): add voice interaction session service
2026-09-05 d149764ab996c77fc909c25fcd7161bf606c708b feat(android): add public voice interaction service surface
2026-09-05 9092fc2ea60fe0fb300f089cb9f06dda8f1d71f3 test(android): define assistant service manifest contract
2026-09-05 6f84765ef51c6a3a93d876a6f73d999aae46245b feat(android): add typed assistant role assessment controller
2026-09-05 86cfe5608e121432251215c1c4045952615a1787 test(android): define assistant role assessment contract
2026-09-05 558fdd6a0831a721ab85a2fe5702b17edb8a282d Merge pull request #368 from lost-rob0t/rage/175-android-streamed-voice
2026-09-05 4ffdb54be76cc91d82125059ca3c1ede2a695439 Merge pull request #367 from lost-rob0t/master
2026-09-05 5779e44c567147c1d344e69985761e74a863ebd7 Merge pull request #347 from lost-rob0t/rage/175-android-manual-voice
2026-09-05 6ec4826a051ec925f9e145ef5b3999898ea0075d RAGE #175 B3: stop local speaker before opening barge-in microphone
2026-09-05 2dfc273bb2b66fffd41f663bc37214d9be360a30 RAGE #175 B3: serialize local barge-in through playback actor
2026-09-05 848c835d2934cddc2856dd45f112798fe6007a41 RAGE #175 B3 RED: serialize barge-in through playback actor
2026-09-05 2235c0a41490ff1b5253972661cbaafbefc700b5 RAGE #175 B3: stop local playback immediately on barge-in
2026-09-05 f0a94ff8114c49578b83098d0e112cc42f7a5589 RAGE #175 B3 RED: local barge-in stops output before network cancel
2026-09-05 8482388d9f62e28c669dccb03b2b443b8b5aebd5 RAGE #175 B3: define Android barge-in ownership boundary
2026-09-05 cf937c8ac514b7b4facd1ca2d0d8bc0741ce1165 RAGE #175 B2: record streamed voice recovery and acceptance evidence
2026-09-05 74d083af331b9f0c403b31e3b7d98b53a19e2a58 RAGE #175 B2: surface bounded playback actor failures in app diagnostics
2026-09-05 945040a79474665387e291edaa1512fa40d38251 RAGE #175 B2: expose asynchronous playback failures from sink actor
2026-09-05 7f90a2368a0b6348bbe12f2da5244200444a1d70 RAGE #175 B2 RED: surface asynchronous playback failure
2026-09-05 0a23c7df94a570f093b31f762889ca21cf7bc9c0 RAGE #175 B2: use runtime voice negotiation types
2026-09-05 0e4576c95341622b7f4957d95e8d67b9d5557c26 RAGE #175 B2: fix runtime audio negotiation import
2026-09-05 9c322bfa877085fc38c24917d1a3f8549cb7faf4 RAGE #175 B2: use runtime voice hello negotiation type
2026-09-05 a194c686202bea3927931d3d584673ba0034c192 Merge pull request #365 from lost-rob0t/rage/175-android-manual-voice
2026-09-05 c080f25ab06c424e2cc8961759d5a01e53059741 Merge pull request #364 from lost-rob0t/master
2026-09-05 44a84f47518e1a712f72146ae10512dc5ae51a63 RAGE #175 B2: enable canonical 24 kHz mono output negotiation in app session
2026-09-05 2a8039168f77f16f4cf6353c2278702fb1fbe530 RAGE #175 B2: negotiate canonical PCM output on the live Android actor
2026-09-05 46a5b082903c28e80cc78a663b73795b0f0298cb RAGE #175 B2 RED: require live actor audio output negotiation
2026-09-05 230a53b3a3f961ad2010bc66fc7c989fbf0da0c1 RAGE #175 B2: bound event interleaving before typed voice acknowledgements
2026-09-05 e57ab143055b57e3b0c02b895f1b5edbacc3d2f4 RAGE #175 B2 RED: bound stream events that may precede a command ack
2026-09-05 82c8a62880faf6f613e204b1c73c632463b33a75 RAGE #175 B2: render real transcript playback and stream errors
2026-09-05 14f4a3f086a8b2d08268a47bf969f875b1cb1278 RAGE #175 B2: observe canonical transcript and playback state in Compose
2026-09-05 dcdac058ac94262d44a5e728eb6d0a3753afee1a RAGE #175 B2: wire canonical stream events into bounded Android playback actor
2026-09-05 a0fb8c69a2273df4020b55814f7eb49c49b0c829 RAGE #175 B2: pump post-commit voice events on the socket actor
2026-09-05 126b392b775e6324317428ec1d30f7581efff31e RAGE #175 B2 RED: drain final transcript and audio after voice commit
2026-09-05 65669d17dec74a174cc2e458f76cb9b170ee708d RAGE #175 B2: add bounded single-owner playback event actor
2026-09-05 fa12f1864198019387aae6f5af570ed7384a6a0b RAGE #175 B2 RED: require serialized bounded voice stream sink ownership
2026-09-05 67f51700318aae4480dbb762f0118f70ea429e01 RAGE #175 B2: dispatch interleaved voice events while awaiting command replies
2026-09-05 7bebe54e2add0d5a96f235d250494e360ace29c3 RAGE #175 B2 RED: route interleaved stream events while awaiting ack
2026-09-05 a959d19c5222148316cb7ef57d39f2b5749334ba RAGE #175 B2: clear playback ownership before replacement start
2026-09-05 aa240bcba18f38b284b6eae433377324f836acbf RAGE #175 B2 RED: keep playback ownership honest after replacement failure
2026-09-05 681918ca5a0bef5b4e31fd789f4d64bcad43aaa5 RAGE #175 B2: reset transcript sequence at terminal stream boundary
2026-09-05 c7a338ace71acc1b3736d727683cd3aae4ccd8ce RAGE #175 B2 RED: permit sequence reset after terminal transcript
2026-09-05 8c5783daf4bd773a24be76e8e3f7b7289e5de25f RAGE #175 B2: classify streamed voice events beside command replies
2026-09-05 ef8d5d964269147881d8e6096b2f74832719e00e RAGE #175 B2 RED: require voice event and ack multiplexing
2026-09-05 82f8f8cb17ece2c4731747b421300a16c00f4a71 Merge pull request #359 from lost-rob0t/rage/327-bounded-target-edit-distance-recovery-r2
2026-09-05 0605498bcf2134ff48b73d4d0dc1330d5e91167b Merge pull request #362 from lost-rob0t/rage/175-android-manual-voice
2026-09-05 e2ec5efc85a0cbd04dcd99f60112a7c8edb5f259 Merge pull request #361 from lost-rob0t/master
2026-09-05 1c8eaea28fa1df190d4711bc87e94a42eaa516ed RAGE #327: correct preserved RED head identity
2026-09-05 e993e2a424bcff35202cbeb8786fe7a4cc805b30 RAGE #327: record post-security-fix exact-base recovery
2026-09-05 d68e470103c6a8ec0755e4cb3b06fcbf28f80a7b RAGE #327: advance recovery onto merged security fix
2026-09-05 a1429625ec43880310d6c53d8343e58749003b6f Merge pull request #356 from lost-rob0t/rage/348-dash-prefixed-z85-cli-r2
2026-09-05 4e34cd9992107550b0c9bac13c176e7e14f1b215 RAGE #327: record current-master recovery iteration
2026-09-05 0cab11f49db73bbf0900fe61cada6ab726f36596 RAGE #327: replay bounded target recovery on current master
2026-09-05 c3d25fee8225819f752c9f14f44a903cc9caab78 RAGE #348: record current-master recovery iteration
2026-09-05 d858a9b4230d3edbcb23c5077143f6b0833b62d3 RAGE #348: replay dash-prefixed Z85 fix on current master
2026-09-05 4099e811b03a394fb35025359750187ce88f77cf chore(android): keep PCM output imports strict
2026-09-05 25256c2dc069e8c800c24e0a00a4b7d1422435ec feat(android): add single-owner AudioTrack PCM output
2026-09-05 685c92def1a1685c345f43d9fa48b9f3fc703ae0 feat(android): enforce one-owner voice playback lifecycle
2026-09-05 e5a0573516c7f17efec51a8a8f01815b44088911 test(android): specify one-owner streamed voice playback
2026-09-05 613fb9cce40c4520fcdb83fce25fa826abc655b0 docs(rage): record Android manual voice evidence
2026-09-05 863561e5ebb4d12f050651e6621f15562af8ff1b feat(android): reject stale streamed voice state
2026-09-05 a5aa8ae4721849c5996bb17b83569f70f5b1b8b3 test(android): specify stale-safe streamed voice reducer
2026-09-05 d288b6b01ffa807497ac62b052e2739c3ad9030d feat(android): negotiate canonical voice output format
2026-09-05 83e55e00a23c6e9d1252a06bd3ef1fe701f92357 test(android): isolate voice hello negotiation codec
2026-09-05 f02b8d93529dd2cfff01eca7c476d87fd01e559b feat(android): decode canonical streamed transcript and audio events
2026-09-05 44a032432fec75dc9d9a2729cf86937f854c71f0 test(android): specify streamed transcript and audio decoding
2026-09-05 e2944efe29bcc1e833c0fb1b736217518581b8cf test(android): specify canonical voice output negotiation
2026-09-05 6096ca9188d27420e9e39b0bc388002a57dfdaf0 Merge pull request #354 from lost-rob0t/master
2026-09-05 f590e50fdccd6b25453c09ba697ab70c770c9692 Merge pull request #345 from lost-rob0t/rage/197-compose-first-usable
2026-09-05 07cc092e4810dfef495c99b9283a650ffce6d8e9 feat(android): request mic permission and drive manual voice UI
2026-09-05 357101e720e7d2b3193649a6a9422360bc2d272a feat(android): add honest manual voice surface
2026-09-05 090549d921cdb13a137491de98ff42780d4c980c test(android): require honest manual voice availability
2026-09-05 7ca62614813e5659debcfa80cccd4e4b156917e3 feat(android): expose canonical PTT session operations
2026-09-05 a9278a7314f92a81f5f3e5d9b23e06904f9e823a feat(android): bind PTT to canonical runtime session state
2026-09-05 c12589b5f8978bca996ee9f8173504e6422b32d1 test(android): bind manual voice to canonical runtime session
2026-09-05 2191c2e46674e5b20d43274fa716db90d60adfe0 test(android): prove voice shares authenticated dealer session
2026-09-05 46d823ef514f5468221e413f7ac4b14f66df6ea2 feat(android): serialize voice commands on authenticated dealer owner
2026-09-05 561b0c6de0833f5443414f191dc4606956e04fed feat(android): decode voice acknowledgements fail closed
2026-09-05 fb021ae0114415b117d0148c2a85e580b7640b57 test(android): specify strict voice acknowledgement decoding
2026-09-05 fe9faeaf0b349eb95cd04116d174a459d4c0a806 feat(android): gate manual voice on authenticated command acks
2026-09-05 1b22cf35f8041014d29c443814fe77387fbc9f98 test(android): require authenticated voice command acknowledgements
2026-09-05 f6f77e22c12f12bc14e165a000db6511fef43637 Merge pull request #353 from lost-rob0t/rage/197-compose-first-usable
2026-09-05 e3ebbb126beac5a946cb126fcf1e704458e21492 Merge pull request #352 from lost-rob0t/master
2026-09-05 345d318360737598bb7a0407d6961d0d76e02e8d Merge pull request #338 from lost-rob0t/rage/173-android-client-continuity
2026-09-05 97ed4b773a33d5d11dbb14b2d0f137160002b6fd feat(android): encode canonical ZARA/1 voice ingress frames
2026-09-05 5b6facb54bf9486ad23b500c791f5ccd1e1cf6bf test(android): define canonical ZARA/1 voice wire encoding
2026-09-05 f53025a3e42c3235050d42375d5a8f57a1b38197 feat(android): declare runtime microphone permission for manual voice
2026-09-05 497376b84c9d6bfc88e577790aec918b6aa04e86 feat(android): add single-owner AudioRecord PCM recorder
2026-09-05 268c5c2468877a2f7f273b03349aab6ad371c932 feat(android): fail closed on asynchronous recorder errors
2026-09-05 2fcb2500b138e401103afdcdb2d01badd9943c78 feat(android): add atomic voice cancellation for recorder failures
2026-09-05 15a8de277b44db97f74a25d3c3e1faf9b23254d6 test(android): require async recorder failure to cancel voice stream
2026-09-05 9f05b3301a4f44d6bbf3b5ec25efe60fb3ecf127 rage(#348): record bounded parser design and implementation
2026-09-05 3c38f150940cda8fa7dd21552ce78184de92a8c1 test(#348): keep malformed dash values fail-closed
2026-09-05 ecbe34f353c7fd4000a916329ba59ea4d997f8c1 Merge pull request #351 from lost-rob0t/rage/197-compose-first-usable
2026-09-05 2ffe9711b52963044c82caf644babd8d241b6841 Merge pull request #350 from lost-rob0t/rage/173-android-client-continuity
2026-09-05 5dc158133c681b1b6975d82bcd5933c3ac6a8f19 fix(android): route capability ack through its canonical codec in stock interop
2026-09-05 1490c4068e287d999bd8a79e3ef3549c0164fa06 fix(#348): accept dash-prefixed Z85 enrollment keys
2026-09-05 32d5bd7b603868fa7bdb4a01643fef0e90f42eb8 test(#348): pin dash-prefixed Z85 parser regression
2026-09-05 5486f67c5b0fe4ec000ca96abae1a9408c7da0d0 rage(#348): record dash-prefixed Z85 CLI regression
2026-09-05 e3f08b6d3316c6a4dd816fd59e619a6957f62a68 fix(android): serialize manual voice capture transitions
2026-09-05 39ca3050c4f920103e140c77d40377371911db30 feat(android): enforce single-owner push-to-talk recorder lifecycle
2026-09-05 d60c58ca3a9504dd389039ca566d611c48f5720f test(android): define push-to-talk recorder ownership ordering
2026-09-05 85612bdac953559869b63b9515b2a63b3a97ca5d fix(#327): keep target recovery inside closed latency schema
2026-09-05 66c159dcb7bd4f5998477d79faacc87f1824bc2a feat(android): add manual voice capture ownership boundary
2026-09-05 1442ddcba34e4fcb92041f68d50d6eed6591db24 test(android): define strict manual voice capture lifecycle
2026-09-05 1febdd31cd309ab45813a7b8d1f6c69a5eaff440 Merge pull request #346 from lost-rob0t/rage/173-android-client-continuity
2026-09-05 3465d9e05e4eaf92512ae6ecd90a71fa19c3e3ff fix(android): bootstrap stock server fixture from repo package
2026-09-05 4c1d16aca25ec68e027bff1eca3dbb8ea2ca25b1 RAGE #173: signal stock runtime after actual JeroMQ turn acceptance
2026-09-05 edd409ed17583acd5bb1de557c6eb37251d69a73 RAGE #173: gate runtime events on observed turn acceptance
2026-09-05 ff5a146460bbb6c08ddbcccc08a84e235b23700f RAGE #197: record live first-usable wiring and UI invariants
2026-09-05 41edb3eecada2161b88410d4e3d7d83c115b84b2 RAGE #197: prevent parallel connects and clarify enrollment
2026-09-05 f755d2b711fd5fc9aa72ccc6fce6ee9f6532e2f2 RAGE #197: RED parallel connect control
2026-09-05 dc8bc136e499073da4d8ef09ebc53a447513f42a RAGE #173: bound cold Nix stock-server fixture startup
2026-09-05 ef356d75cba664c6375513c2710a2a72b208bfbf RAGE #197: test live reducer state observation
2026-09-05 2d40d17c33ae171e9cbda7764b1529616ae667de RAGE #197: drive Compose from reducer state observer
2026-09-05 4a65252cd6500452f9384e086dfd3e65ddf90fb8 RAGE #197: expose canonical runtime state observation
2026-09-05 562ee6dcdbf248c1899bbe7f3f594c1fda6367f6 RAGE #197: publish canonical reducer state to UI observers
2026-09-05 42e202d50a93642a10af0c0d86224a38fc69c11d RAGE #173: require stock secure ZaraServer interop in Android gate
2026-09-05 c6d921b8cd8ecf26ee78f0f4a3a85ba752fc1bba RAGE #173: prove JeroMQ actor against stock secure ZaraServer
2026-09-05 bcbfa54693ce609b0953e4e2b9dbfa0b3aca1327 RAGE #173: add stock ZaraServer Android interop fixture
2026-09-05 11e6db290073bd269a70760610c58b8e8ad1a0c5 RAGE #197: connect Compose controls to canonical Zara session
2026-09-05 0ee493350485cac0efe9404776fdcc027b688e0f RAGE #197: wire enrollment connection and real chat controls
2026-09-05 84f097ab17e7c02f80a17788d989723726a2d043 RAGE #197: own canonical Android app session lifecycle
2026-09-05 6d4595ba9a887e74dd115854946fe9285888f86a RAGE #197: record first-usable Compose shell evidence
2026-09-05 47b0d1d186130342ab522f96a3838ca978faea4a RAGE #197: test canonical UI state projections
2026-09-05 71db459594950e4da4745f01fc45f32b2d6f2d69 RAGE #197: launch Compose shell from restored runtime state
2026-09-05 d0f79b0c85110de39f0f8b186cb72fc90f2a45de RAGE #197: add honest first-usable Compose surfaces
2026-09-05 62e3af73b571f5a15b1927e747d44fe33c5f9bb4 RAGE #197: enable pinned Compose Material 3 shell
2026-09-05 37f19709974402927d77943c5d0e2984ff6b126a Merge current master into Android #173 recovery
2026-09-05 a0d218de65e2dc294dbf4b9b3fab6a7309e8783a RAGE #173: disambiguate synchronized request predicate
2026-09-05 f2406d1e7282cfaab78df59c0fddaab0fd373530 feat: recover registered app targets in Prolog router
2026-09-05 28ea0c2638f0e267871b318aa9b2472efeda9e3b test: require bounded registered target recovery
2026-09-05 1e358175f57d2a8eedaceefa20ee51b51a05a6df docs(rage): recover issue 327 on current master
2026-09-05 925f5fc9506abe4f5b9e5a942fe3a1f87525166f feat: add bounded registered target matcher
2026-09-05 7cb047a390644c7da96cfb4620bfb8d569450fff Merge pull request #331 from lost-rob0t/rage/329-production-secure-listener
2026-09-05 b20c0c18cbe391000829334e4dec370bbab0054d RAGE #173: emit compact canonical text JSON
2026-09-05 c123ba40a46937f8ba87dd395f2885fce66c0533 RAGE #173: invalidate timed-out text transport before reuse
2026-09-05 142e9777c00119978e3f81f09500a81e607e7647 RAGE #173 RED: reconnect after text request timeout
2026-09-05 af972b7154021f983ba89bbc433b21bd8427101f RAGE #173: disconnect transport when enrollment authority is lost
2026-09-05 8bb17a50582676f2663d515db1ce7ec7b06d802a RAGE #173: invalidate active runtime when enrollment is lost
2026-09-05 3480312fbe2d0fe7e475c59f8562caed9239520a RAGE #173 RED: disconnect when enrollment authority is lost
2026-09-05 d3d87e983c96fbed470c7fe8ef0530fbeabaaccd RAGE #173 RED: invalidate active session when enrollment is lost
2026-09-05 51689ecb15db92bb53111ff718c56469a7f5a18b RAGE #173: record text lifecycle and reconnect hardening
2026-09-05 81e7aafc6fc4b36c1c3aec5535a5fdada6b39ca9 RAGE #173: ignore stale connect completions before retry effects
2026-09-05 0af3860c5784572b4697d1c9a990e59d3dfef797 RAGE #173 RED: reject stale connect failure retry scheduling
2026-09-05 9330314a8a201f6adc3b61d266c90ef1f36d7904 RAGE #173: negotiate capabilities in ordering fixture
2026-09-05 fb53318443f56de52cc3533729876a90518f1647 RAGE #173: cover capability negotiation across text sessions
2026-09-05 0e552e13e2ccb351c19af3ac7273e895b50f5353 RAGE #173: negotiate empty capability snapshot before connected
2026-09-05 d74b978f14124ee516d58250dde49d6d0f60d455 RAGE #173 RED: require capability snapshot negotiation after hello
2026-09-05 d591e395878962cc10517d8bde71eedc031cd27b RAGE #173: align text actor fixture with terminal turn event
2026-09-05 9a8d7df580e8ef155cd961f01e1fd8ee74986320 RAGE #173: drain canonical text turn lifecycle
2026-09-05 5c97b44ce7f52490e048a867416a12bc9e1f4457 RAGE #173: record reconnect and merged capability contract
2026-09-05 af5a27979d66cbea75062f829dc565e17955d72e Android #173: harden capability JSON integer parser
2026-09-05 fabea77133914976bd0da2373ad9392d42a46a1e RAGE #329: prove typed device actions survive secure gateway hardening
2026-09-05 04ef8a261570f5a45639314b74fae404c9f354ce Android #173 GREEN: add closed ZARA1 capability codec
2026-09-05 b5a32e6136ff52fda4794562df95e99c8cb90f11 Android #173: isolate capability negotiation codec
2026-09-05 056c6eb4c4a6f4e100b201ebed3d358bc986554a RAGE #329: preserve #336 device-action authorization on hardened gateway
2026-09-05 acefb7b80abe4b7c59a492b5033245aa8a0c7587 Android #173 RED: require typed capability snapshot codec
2026-09-05 3479c7507f00ae6526828a5c412905352738f07a Merge canonical master after #336 into RAGE #329
2026-09-05 c28f43701b5b7196dc64f2050966a2cea0116af2 Android #173 GREEN: execute bounded reconnect schedule
2026-09-05 6f6dabd20578abad4218b4173883ed141dc44e7b Android #173 RED: require bounded reconnect orchestration
2026-09-05 a4173f79ec5bb51ea54c1711663ae2872afa0228 Android #173 GREEN: retain configured server across restore
2026-09-05 bb55b494bbbdb8c93e73b5facb0646e6102b9d9e Android #173 RED: restored state retains configured server
2026-09-05 7ad60ae16aea72ba614e3b2b80334ab904efd742 Recovery: refresh Android #173 on merged #159 master
2026-09-05 759222b879825cf34bff226f247ef1a93eccae0e Android #173: bind text actor to session-client contract
2026-09-05 4353214b9a3e96a0e2d70986722117d09d5f71a7 Android #173: implement reducer-owned text session controller
2026-09-05 19e2b27befebc9c8911ce969cac6e060e26e35d1 RAGE #173: record text client and source-SHA gate repair
2026-09-05 eb6e9bac0a9fc13ca90b3779fe1d7271107d431e Merge PR #336: typed ZARA/1 device capability/action lifecycle
2026-09-05 08c16b05e37eded8aac9e76fd6404e75891e8a4d RAGE #329: point depth threat to exact gateway oracle
2026-09-05 d41d6bafaa24205b822f211d716adb3cec95e2e3 RAGE #329: enforce compound threat oracle references
2026-09-05 c2a1547f88d59af29da58ffd6dbbc6ac30077f7c Android: derive diagnostics SHA from PR event head
2026-09-05 63c72640aa3518b6455e56042e3aaae399ce0993 RAGE #329: catalog research-derived cross-boundary threats
2026-09-05 a487b908b6175a3813c8a616cec27ad3081efa92 RAGE #329: assert exact duplicate-device failure class
2026-09-05 a07c412aaead1d51f2e4f8c8fe87d24aca247e8e RAGE #329: cover adversarial enrollment lifecycle sequences
2026-09-05 ac9c041ef245fe00f44b05a6e512ec22ce360ff5 RAGE #329: prove control-plane rate quota stays bounded
2026-09-05 b89a124c002435a0dafaa17aa42afcc3af144225 RAGE #329: keep reconnect hello outside runtime concurrency quota
2026-09-05 678c1a69ff3e040390caba00b6eadecdaec68457 RAGE #329: separate request-rate quota from runtime concurrency
2026-09-05 4a8d68543c334c6ea8caf4d478dd168cc8a54caf RAGE #329: pin untrusted JSON nesting boundary
2026-09-05 e6e0e2fc04ab583b36e393004c495ae0e2e76006 RAGE #329: keep structured persistence fuzz JSON-native
2026-09-05 84431b4c3b97ecb1e4cf9dfb72ce6423e6c5aec9 RAGE #329: bound persistent security JSON nesting before parse
2026-09-05 fe1740a91d44059795bf1bdea4c2221ac3b33470 RAGE #329: bound security admin JSON nesting before parse
2026-09-05 8109e34bd5c7c2afab0ac574d40be82486c57e4d RAGE #329: add deterministic untrusted JSON nesting bound
2026-09-05 d8787394a62fcca108bebc7c364937b011a972b1 test(android): define reducer-owned text session controller contract
2026-09-05 a50a30920cec53a39afd20e4ae88ae5ca3d33e0e Merge pull request #340 from lost-rob0t/master
2026-09-05 87ecf536c2347e6407155846a6c47bf8b7890e6e Merge master docs refresh into RAGE #159
2026-09-05 a6e06877aae1f70bc77a999f95f7e12f80a53b37 RAGE #329: include parser and reconnect threat cases in soak
2026-09-05 172e92e459c583a4509479c07b018dbf3240711a RAGE #173 GREEN: decode canonical text-turn progress and terminal events
2026-09-05 6def13fa033e72613b3f527633bf4c3c1bbd1947 RAGE #329: verify route replacement and vanished-route quota release
2026-09-05 52eb5fb38ecfd36d386ed1b229f8f162a78ed0ec RAGE #329: prove recursive ZARA/1 JSON cannot kill secure gateway
2026-09-05 352362fb865f47b1f949baf74a8ddd3666784d2d RAGE #329: scope recursive JSON unit tests to local boundaries
2026-09-05 eb72da2ad230c207bd9c060484f166f7dfe92735 RAGE #329: normalize recursive persisted JSON failures
2026-09-05 b76c1f94620aae6d04ef0383e9d7e302ff7d5568 RAGE #173 RED: require canonical turn progress and terminal drain
2026-09-05 f4887e937ea2cc8439ae533d9ec8545df5bc3d81 RAGE #329: normalize recursive admin JSON failures
2026-09-05 588ea73734429989904b5c03adba47fb953e7ac4 RAGE #329: close authenticated route and quota lifecycle leaks
2026-09-05 108f3a6d307b7211de8d2a493ed7521e820b4d76 RAGE #173: bind text actor to authenticated JeroMQ DEALER
2026-09-05 5f874e1f51ac30b5c705c0479d831b2fba77accc RAGE #173: keep actor assertions at wire boundary
2026-09-05 f12c358d8069beaacf3ad189231f5d64c2b322a2 RAGE #329 RED: model authenticated reconnect quota abuse
2026-09-05 752a8d208531e86436573d6e752f6fd15f008b13 RAGE #173 GREEN: add single-owner ZARA1 text client actor
2026-09-05 77728fe1d7a03721c85f7211348f5f51d98f9f94 RAGE #329 RED: cover recursive JSON parser exhaustion
2026-09-05 04eb6774eb37c0dbeadcc7ed618725d42b1acb8a RAGE #173 RED: define single-owner authenticated text client actor
2026-09-05 7b35dd2b581091143d0392b268eab48990b7e3ba RAGE #173 GREEN: add strict ZARA1 text codec
2026-09-05 400744e5bd00e8a302318c91db0678c7d8314af7 docs: extensive Zara documentation refresh (#337)
2026-09-05 3ead5986506a738d1235daabad85d81fa4ce258d RAGE #329: include dependency threat gate in security soak
2026-09-05 6f10852686738cf8459583f9df6dbd7843cedef3 RAGE #329: require actual libzmq CURVE capability
2026-09-05 df332b4b2376b27bff108c667401d94732a4fed8 RAGE #173 RED: define strict dependency-free ZARA1 text codec
2026-09-05 de639188f0453d5a4cd626fe4cfc54b7872cf051 RAGE #329 RED: require actual libzmq CURVE capability
2026-09-05 1b86b1e71737f67d0a0be3c2574f0c7d7a30165b RAGE #173: record client-state campaign slices
2026-09-05 d354638d035ddddeaaa5bd967046005ffda2acde RAGE #173: render real enrollment and restorable state on launch
2026-09-05 4a6bf32109ec41f63b33ede307e0697062b60f47 RAGE #329: run full threat-model security soak
2026-09-05 1a275917e20f0548b630c55a14f228b5cd74f70b RAGE #173 GREEN: project enrollment readiness into canonical reducer
2026-09-05 da440bd3f9e737f53cce99b1d51fa97aedc66e30 RAGE #329: record complete authenticated-daemon threat model
2026-09-05 b5c54cfb8242488ffac0ab459efab80e10383c1c RAGE #173 GREEN: expose key-free enrollment readiness projection
2026-09-05 a57c02a7ca5b072fc5fa87c40df90ebf3ec75715 RAGE #173 RED: project enrollment authority into key-free runtime state
2026-09-05 8cf1d470cbac81bb5197c412573a54fe11eac560 RAGE #173: regress exact Android diagnostic source SHA
2026-09-05 d90b4d7cbe50feb7a16921650a1e2741228f7059 RAGE #329: enforce threat-model traceability in CI
2026-09-05 f297cebd5ba630e97be851c3387261d8e2d0fd57 RAGE #329: verify owner-private admin permission contract
2026-09-05 8987efe19f07725efeeffab9e6c69cb1bedbd2e9 RAGE #329: add executable STRIDE threat catalog
2026-09-05 ef7c7b832962679efdf0296fd802cba16575f9ee RAGE #173 GREEN: bound request correlation to generation and session
2026-09-05 605993c0f533bc7907588b2b8b90c04d61253c7f RAGE #173 RED: require bounded generation-bound request correlation
2026-09-05 09dfc355444b579d0120abb9a21544ba96b2aa17 RAGE #173: record actual PR head SHA in Android diagnostics
2026-09-05 5c487853915e1a0334ade61319b149da9bfb8ed7 RAGE #159: record surfaced accepted-before-error RED
2026-09-05 ad0f22667bc88ce7fc2efc5c76cb4e4f55f4dbd7 RAGE #329: add security-management disclosure and state-limit tests
2026-09-05 06c9a62e77935f3eee28ad65bfb5ea8b0aa28ce4 RAGE #159: align remote-error test with accepted-terminal lifecycle
2026-09-05 a7847072cf1597c6465cf312aad762d0dce1cb49 RAGE #329: add remote gateway threat-model tests
2026-09-05 69c76809abc8d6f128e012fcde8d8d1ee7c3b2f9 RAGE #173 GREEN: restore durable selection without fabricating a session
2026-09-05 81adb076b2d32650f0b8430a2a0722fbebefbb17 RAGE #173 GREEN: persist only restorable public client state
2026-09-05 696d832cdcafe9cd2bca9a95083cee97128369ca RAGE #173 RED: process restore must never persist live session state
2026-09-05 22a54533c3215f446064d7df0dbcb4a4f02c5645 RAGE #329: make ZAP user ids opaque bounded ASCII
2026-09-05 f78f54c92a1a293824441a7fa32dadad4dcb3002 RAGE #173: expose exact Android source SHA in diagnostics
2026-09-05 985e56d365c92eeaccf79550cbf8ba36ccc39d32 RAGE #173: embed exact source SHA in Android BuildConfig
2026-09-05 9edcc1c97a504f19752484d19de9f485b71112de RAGE #173: render evolved canonical connection states
2026-09-05 5d5dc5978abcf818cdd55a13f8791275d2ed9e44 RAGE #329: harden CURVE/ZAP transport invariants
2026-09-05 0c9a971dfead6170af221ea94b35539268e3cc06 RAGE #173 GREEN: generation-bind hello sessions and bounded reconnect
2026-09-05 9d13265325f85ada47cb7852063f782121dbfda1 RAGE #173 RED: require generation-bound session and reconnect reducer
2026-09-05 c2c568f5a219f22e35509615d12e4240575c0179 RAGE #329 RED: codify transport and local-admin threat cases
2026-09-05 9abadedaac91557e344135c233a593f8898d31fa RAGE #173 GREEN: validate public TCP server profiles
2026-09-05 f17105cb1daaa33d6c9757aa9d636602696979ac RAGE #173 RED: define safe Android server endpoint contract
2026-09-05 4b48bbd5ba0881e5f0633ed9e0e06a98250e2f87 RAGE #173: consume Android client continuity slice
2026-09-05 752a46bc754e8c96bba4e98e59bee220e5735c62 RAGE #159: record failure-surfacing recovery
2026-09-05 31e1110576828ac4b5b778ce7898e68bc7fd3db5 RAGE #159: make device-action ZMQ teardown failure-safe
2026-09-05 05b25f1edfce97ea5045b9f6b1956a35b3f7ebb6 RAGE #159: make adversarial ZMQ teardown failure-safe
2026-09-05 330402ef67f6c92b7c19ac63d10f65734b49cdd9 Merge pull request #335 from lost-rob0t/rage/159-zara1-device-actions-recovery
2026-09-05 cc4826bb8ea2f05b04238612f0ba4ce184c201b0 RAGE #329: add process-chaos tier to security soak
2026-09-05 98b0bcd30ff0a973d12bb06c138e0a1a5da389cd RAGE #329: add multi-process crash-point security chaos
2026-09-05 9928b70d96686ece187e225d9a2f28bafda34427 RAGE #329: make structured fuzz mutations unambiguously invalid
2026-09-05 85d8f7b6f82124fc6b69241840db0701a385cd75 RAGE #329: widen deterministic security fuzz corpus
2026-09-05 1fb7d255795626de6ac4090a4e4ac07697bd1069 RAGE #329: include adversarial suite in security soak
2026-09-05 0440f2dcac15e2d07eb5bc6c059d7181e2fc8b70 RAGE #329: add adversarial security state and admin tests
2026-09-05 dc850892edd5ab12555fad3e4bdb8c32dac438e7 RAGE #329: exercise chaos through bounded admin socket path
2026-09-05 d6f031e54f5a71d4f1db9382476809f0ce1b0ed3 RAGE #329: serialize persistent security state mutations
2026-09-05 479634cb71384e728ae501db7594999c0fb58cb1 RAGE #329: harden security identity validation
2026-09-05 49fbe4c45c31bcccf78e463dd8f1cb6337b02278 test: make security fuzz inputs byte-for-byte reproducible
2026-09-05 3c00b9c5fabe436b297b8308389da1837a05669b Merge master into RAGE #159 device actions recovery
2026-09-05 2bf5f6e688bfbe80ad6d734b4ea2e8e0aebe09c8 test: add reproducible security fuzz chaos soak runner
2026-09-05 beb733afb4d3cf0b0f2d8048d808236307d12eb7 test: make security fuzz seed corpus scalable
2026-09-05 ceb2e13951af518cbc29df2dafabdea022baad89 Merge pull request #322 from lost-rob0t/rage/173-android-auth
2026-09-05 b6e8e62d9489123a6b39397536a5a0dd76b0cea8 docs: record security fuzz and chaos hardening
2026-09-05 617f9cf11a649959f6855970e54a4b0ab8d43735 test: add live security chaos and fault-injection coverage
2026-09-05 c5d1f17834f87f4001d0b542384adba5d890f4c3 test: add deterministic security mutation fuzzing
2026-09-05 d25096f0110c1484cd9e012008bc432f299f42d5 fix: fail closed when live security control disappears
2026-09-05 aef972cc5e4ab4529a9faf81277d2d92173a0ae7 test: lock long-path live security socket regression
2026-09-05 4e0d5906104b8859b5091ad20cf3ad3e6994b7b4 fix: keep long-path admin socket inside security directory
2026-09-05 36a30958ebab6b96df82b414b7d54631cdbc4747 Merge master into RAGE #329 security recovery
2026-09-05 17b1fda2aae0835efdc21b23fa0ef424f875b556 fix: route owner security management through live daemon
2026-09-05 6f1f040a6a4dde8bf5309edf40e1c09b1ee57d5f feat: add owner-local live security control socket
2026-09-05 7d4fca38628a6fc4e5e6e568b667c41e72a4167d fix: make security persistence live-registry aware
2026-09-05 97a010110d7defede9135851db21a365369050cf docs: record live security RED and no-reload design
2026-09-05 7c62117ecc55c488771b5496be84bd0b75bcb74b test: prove live security mutations require no reload
2026-09-05 01dd7da417ae19848bf8a4e21031819edcaf04e8 Merge pull request #334 from lost-rob0t/master
2026-09-05 45975f7baa0f81a91198861185993bb31a12597d RAGE #159: record protocol-state repair iteration
2026-09-05 6e974fcdc11a10616a0dfa573cfb174eba44818a RAGE #159: enforce device action lifecycle
2026-09-05 a86170c3009d56271c595305443a004d26fd02eb Merge current master into RAGE #159 recovery
2026-09-05 8e247fd4cb6ffe1f3258bfb4f115a3339208e8c1 Merge pull request #328 from lost-rob0t/research/unified-copilot-20260905
2026-09-05 7ed53bdbc2b19c3de4d1f33e85f4a2810814da4a RAGE #173: record Android auth implementation and green gate
2026-09-05 b9822bcf5b078f2bb13eefb5a8ad96c14d4dfd05 Merge pull request #333 from lost-rob0t/master
2026-09-05 83e4f4828a3c2928ae95aede3943f5d4439bb44d RAGE #329: wire secure CURVE/ZAP listener into zara-server
2026-09-05 f9c249280fb6fc22b9a3afd99f20143dd0d78de8 RAGE #329: split server lifecycle core for secure facade
2026-09-05 e6fef87a214ea96552107a621213b0c94a2316f4 RAGE #329: add durable CURVE security state
2026-09-05 60f103e79470d2938e6d28905cfd117811c8c1ad RAGE #329 RED: specify production secure listener and durable state
2026-09-05 6cdc8a392639946232bd220a1627ff52c9bcfcfa research: fix whitespace in unified Copilot notes
2026-09-05 892b1549ba7f2717260f81cfc12aa4f5460e3168 RAGE #329: record secure production listener recovery
2026-09-05 8fe8c3ddca0e5cc2ef5624f551d75b4e3c29d9a0 research: unify desktop copilot, voice chats and visual CI
2026-09-05 50dd567f0a976ce7dd97f5f3374cba75eff6f7c8 RAGE #173: fail closed on server pin replacement
2026-09-05 62cbfddb74777c5a0be8964856dbfafe557d22bf RAGE #173 RED: reject silent server repinning
2026-09-05 d0fd3d99de0a9c21fb97baca65c02cfd6d537375 RAGE #173: permit authenticated ZARA/1 network transport
2026-09-05 16b1eda8dd4a0b1e4a3dba7742787e8a75192347 Merge pull request #319 from lost-rob0t/rage/133-desktop-daemon-default-regression
2026-09-05 5035be7964f801cd8a4726178eb8124eb440b4a2 RAGE #173: cover enrollment state and Z85 exchange
2026-09-05 e93396a0d7ccfb59926f798188428397f774bfa2 RAGE #173: expose Z85 enrollment exchange
2026-09-05 66dd0e58d7bd8764ad5390de5a1e54e480295553 RAGE #173: add CURVE Z85 enrollment exchange and dealer factory
2026-09-05 52b51d8cc3b85c1f663c3db2943757288a5c0cef RAGE #173: clear loaded CURVE secrets after enrollment operations
2026-09-05 d59043957811b1e734b99ae1deeacdc91ceedab2 RAGE #173: bound plaintext CURVE secret lifetime
2026-09-05 197d45c87984ede4f6caa968224e08b908da644f RAGE #173: wire pinned JeroMQ into Android client
2026-09-05 5b1c7eee8c8feeb80bd266a4237d02ebbae032d4 RAGE #173: pin JeroMQ CURVE dependency
2026-09-05 0e9f3fccee9d6435e024dce8dd0a9542dcc7248f RAGE #173: add typed Android enrollment repository
2026-09-05 29f8d6d8412299e774d03610e266afc3769f4fb1 RAGE #173: bind auth material to JeroMQ CURVE
2026-09-05 f01a9cdfd8fa0528fed51f97421184b99ddcaafa RAGE #173: harden atomic credential write
2026-09-05 bd895648d134b7bc7eccb425901d6a3964b3d2ce RAGE #173: add Android Keystore credential wrapping
2026-09-05 86d6ed7ce3f8869b98843622e131a2770c5fb611 RAGE #173: implement wrapped CURVE credential core
2026-09-05 01cbc085a05755f8705bae07789c5a90a86ae4e5 RAGE #173 RED: specify Android authentication contract
2026-09-05 1ceaef551690dfdbf02799bb70521267d3bc07f2 RAGE #173: record Android auth start and design
2026-09-05 f90bf1d47af2a7830c8f9e54c2852482cacbf5c4 RAGE #159: record current-master recovery
2026-09-05 20a63186bb9433016682ee48d64fb7fcdeed5710 Merge current master into #159 recovery branch
2026-09-05 d2b59eaf387104fa7bc2a325f6bf0f9fef1fae8d RAGE #133: record desktop RED and implementation
2026-09-05 f6102b5d6cde02ae623f07fd4dc9e278e01bcc0c RAGE #133: default desktop to daemon client
2026-09-05 dfca78b44fc0e7ccced4800476d2be52b0a67e9f test: require desktop daemon client by default
2026-09-05 4dc71e0c5543f27016baefc7b9b22dbff9786cd4 rage: record #133 desktop daemon-default iteration
2026-09-04 da515c80a2ba18e889f62dc8f1816c8c95249f43 Merge pull request #318 from lost-rob0t/rage/133-daemon-default-regression
2026-09-04 10ff76e5c53d5c189572a06d58f4ab430ba0a4bd RAGE #133: keep daemon-default CLI diff minimal
2026-09-04 a20a343b9632afe59474d5f4870a0ebe4e7d24aa RAGE #133: record RED and daemon-default implementation
2026-09-04 2f5effd17e388637974ce2d6c7917bbece1db614 RAGE #133: default one-shot commands to daemon client
2026-09-04 1de5c5ad041a54868aaeaf6c4163bd9fbeab1b8b test: prove default timer command uses daemon client
2026-09-04 d34f1365bad6653d61e4d38dfd3b4e0e0a22e5e5 rage: start #133 daemon-default regression recovery
2026-09-04 59e9654176fa02eb4aab4cbed4e1532d02f71d2f Merge pull request #317 from lost-rob0t/rage/13-open-app-allowlist-regression
2026-09-04 1c9f7fe5c7af64f83b3be29f3a7958fbe5a34fdc fix: fail closed on unconfigured app launches
2026-09-04 118bf44a3891a3d257d88c0b54babe6c9847ecba RAGE #13: record exact-head RED evidence
2026-09-04 f7e4698f3afddcec7d5a46a4f96e660a24037cc9 test: require unknown app names to fail closed
2026-09-04 08c134f150f1936508731fa1d5032ae35a7b2ac4 test: expose unknown executable fallback regression
2026-09-04 8f4baf46344fcf730e08e71d800438329cc31204 rage: consume reopened #13 app allowlist regression
2026-09-04 7340ca414fff8b543a3a279acd93c2bb613b1eab Merge pull request #314 from lost-rob0t/rage/165-user-command-runtime
2026-09-04 446bffa9b3a8db130f037ebd6cea95b699e618f4 docs(rage): record strict #165 gate recovery
2026-09-04 69ff37f8b5d43d07bbf5e691abb57f146cdc6d7c Merge 23fcd224a2742b76eb5b4c6d21d4776fc8c414e5 into a1b38d9b80a2f4dabe06d53d1185ff23acbbb84d
2026-09-04 23fcd224a2742b76eb5b4c6d21d4776fc8c414e5 rage: record #315 recovery before #165 re-gate
2026-09-04 996440122611c978a0b2d56558fafcbc67bb425e test: sync route-backpressure contract from #315
2026-09-04 a1b38d9b80a2f4dabe06d53d1185ff23acbbb84d Merge pull request #316 from lost-rob0t/rage/315-route-backpressure-test-contract
2026-09-04 fbc22c09e4e4e40d5c8523b960f2c4efdeb81851 test: assert route-local ordering under backpressure
2026-09-04 e3ee03164a09bd8b067fe7cc4cc5b661dba9db45 rage: consume #315 route backpressure test regression
2026-09-04 8268443861524a27191d5529281585c827166e12 rage: record #165 schema placeholder RED
2026-09-04 57734bfa6ca70fb96c3715584d80c318722505e8 fix: resolve schema-legal command placeholders
2026-09-04 9fd706b6dd123663bf6292d9da5fea37a5291f1a fix: align command placeholders with slot schema
2026-09-04 96dde9843aa57e5e968bf4d470d4dfcc5505eee3 test: cover schema-legal hyphenated slot placeholders
2026-09-04 f5146cb2ad3a5a5011b2ab95d8e3811a4ad78f71 feat: validate user command trigger placeholders
2026-09-04 68a323fa9b58b2db50d38b45a7ec24a2c50e1985 feat: resolve compiled user commands at runtime
2026-09-04 e395daf082b870c9f8808238014fb85419839ac1 test: use overlapping distinct command templates
2026-09-04 1fd1ce78d3d111b172afd295ec42b196f3b6134a rage: record #165 deterministic red
2026-09-04 d992fd9c9b9f21309be8290bc705a8dc244b675f test: define parameterized user command runtime contract
2026-09-04 15e942bb16e85346733fa6c2c7963015579a0ed7 rage: consume #165 user command runtime
2026-09-04 dd03e3309f5c09ddbc76c22ba936ce366508ac2a Merge pull request #313 from lost-rob0t/rage/164-user-command-authoring
2026-09-04 8ba768b17da7a40773d3141fa2289b4abebf7ebe rage: record authoring cancellation acceptance fix
2026-09-04 986d4252cc6818921f9dedaa755d4e7bfafef5de fix: route authoring cancellation through clarification control
2026-09-04 3f6c38eea08bae8036e7040659ba81876e23b70a test: prove remaining command authoring acceptance invariants
2026-09-04 a12ddb0f63660743fd714aa903f19382c85db050 rage: record command management RED and implementation
2026-09-04 cccad6ca72ed29312ab2195470dc9034f29bbce9 feat: complete user command authoring dialogue
2026-09-04 9d93b4ab9580a43fdfad3648207caa9c10378985 test: cover full user command authoring dialogue
2026-09-04 106d4414019fb6d1273b3d4d99abdfdee5ef616e test: preserve canonical clarification tombstone lifecycle
2026-09-04 97c76e5c9c3de78eb01f3fbeea56cc8b0bfc54ca RAGE #164: record dialogue RED and contract correction
2026-09-04 70bd5040e027aac8aa947c8aa986e3b8c8fb0fba feat: add typed create-command dialogue
2026-09-04 408466e45f4d50976cbc40a1774bd7b3ef46f6fe test: define conversational authoring red contract
2026-09-04 de47813751ff32bc142a22a55e0c72232233a99b test: align authoring preview with compiled action contract
2026-09-04 a413f27031e26adb2cc5584af84b2934a8f989b6 RAGE #164: record RED and implementation evidence
2026-09-04 c1ee7bf865971a1781ddb9bdb1c3239fce451900 RAGE #164: implement semantic user command authoring service
2026-09-04 53ebf3a08071cef4f821271428cbc5a248f9fb27 test: add user command authoring gate
2026-09-04 af7323778df878ed9480d99007c5ab93629a129c test: define red contract for user command authoring
2026-09-04 4ff167db5a519624dc787c6a1af675a0ad1dd5b4 rage: research and design user command authoring
2026-09-04 014e8f7e472011b6319f03026cd37f29d4748a18 rage: consume issue 164
2026-09-04 c4945cf3e848eb4e55355ed767ce780348beb414 Merge pull request #312 from lost-rob0t/rage/163-user-command-compiler
2026-09-03 7f908015761c0367d1a739fb535140422d588a7d docs: record #163 RED and compiler implementation
2026-09-03 65ab9123088999473e7e9edf4df7e65085672492 feat: compile persisted user commands into semantic frames
2026-09-03 cf03f6376d9be0799812d2c740e3ded559f45c21 test: add user command compiler gate
2026-09-03 6b27dad03ac4e25171ef35908576622d348660d3 test: define user command compiler contract
2026-09-03 bc1c2d8a977e38311c7d8d1b7ff8ddcd057eacc2 rage: consume issue 163
2026-09-03 7ae6739f44f11aaef2786fa9410e26f5b7aecab3 Merge pull request #311 from lost-rob0t/rage/162-user-command-persistence
2026-09-03 ae0d49d89dd5b910b43134fc3ffc2cbf56af5bdc RAGE #162: complete typed command definition persistence
2026-09-03 9693cf1082491a0247dece1695224bbc3729379d docs: record #162 acceptance-gap iteration
2026-09-03 c189c26dcda56eb363fcfee3586c97a5361da2a3 test: cover full user command persistence contract
2026-09-03 4cd886cecb2e71e5e054dc08daa0202f13b17d34 test: add user command persistence gate
2026-09-03 a573ddcb7c10c17165a0c38d696a77e29f205668 feat: persist principal-scoped semantic commands
2026-09-03 3184fff6e25ae055773a9b77341e3e19580582e1 docs: record #162 RED evidence
2026-09-03 5c757371475cd823c6f59bc251c03e0c7c9ea1f7 test: cover user command persistence invariants
2026-09-03 7110b3a693ba566e1259fd8d3ba8a09bc38dadad test: define first user command persistence contract
2026-09-03 6e85c351f0c197c032983f538e17669e76cd4564 rage: consume issue 162
2026-09-03 f25aea5f9e5bceb747cb282b6a28c43f07e5b727 Merge pull request #310 from lost-rob0t/rage/309-prolog-config-recovery
2026-09-03 3c91e35849e38927285a495b3147a2804b6054a6 rage #309: record Nix contract cleanup
2026-09-03 fdffbe5184d11ddd232e7ca83dd409dcbf02fe17 fix #309: drop Prolog-RLM lock input
2026-09-03 704b937f04f01e5f8149e5fc61fb067afe3b04e8 fix #309: remove Prolog-RLM Nix wiring
2026-09-03 6be2a50bd646591f6ac6e99b58bfaa9f37669add test: compare recovery base config by bytes
2026-09-03 de529830ad7f70c4b695189562d054da6909989c rage: record CI 906 config assertion diagnosis
2026-09-03 b736091731658aa4b7d441883100c062d7c9f69b test: compare provisioned config content by character codes
2026-09-03 411c83ad3504d252937cec976518579262df0049 docs(rage): record 904 stale RLM gate
2026-09-03 f658a0d5fad90ce35b605a5739d730218218e0ba test: retire stale Prolog-RLM gate
2026-09-03 6c5135dd7e5bb9c3f67ea3441ff3f5929140fda3 test: point routing gate at daemon router
2026-09-03 440399b60b95d1d7cbea327fc1090297c1646c28 docs(rage): record CI 902 routing gate failure
2026-09-03 1c5d4f589f2dfea0d99c45fbc8e56f9760100a94 docs(rage): record api-service test restoration
2026-09-03 fd51cee576a31dbedeb0727d5104fdc57cefbcc6 test(search): restore full api-service suite with Brave expectation
2026-09-03 1c87f3949b0018d1bde9240e017c574fc4eb5907 docs(rage): record phase-6 Brave contract reconciliation
2026-09-03 3748d88f2bb1f059c90088b4ee62d3e80bbd3b45 test(search): expect Brave from server search provider
2026-09-03 b3a065356fa70a389f9d99511f65b1acd786683c test(command-loop): remove coverage for retired RLM routing knob
2026-09-03 5e47384947ea8ab0b85718d16944ffea95ac36cc docs(rage): record config recovery GREEN implementation
2026-09-03 8d49d942e6fc54fa94a333ebd2591496ed541697 docs(config): document durable Prolog overlay and remove RLM setup
2026-09-03 713d8cc99e7d343d5762aaefb2ad30610b10e8c6 docs(config): align API service config ownership with recovery
2026-09-03 628edb8d07787bd994b62a88d566013b93d8b120 fix(command-loop): remove dead Prolog-RLM fallback branch
2026-09-03 a3ad2cb75b57e0e6f879390ec7f9ce33f2b5eb1d test(config): retire obsolete RLM configuration contract
2026-09-03 8f61822ce5f244aed20bf108d4f19b92fa238b1c fix(config): reject removed RLM knobs and document local overlay
2026-09-03 0412cae73595f75a85e54b9ef058daca8dc34022 docs(rage): record first genuine RED for #309
2026-09-03 b6220dea467660ed6cdf9aded0eaeeb1222abf09 fix(config): make Brave the supported built-in search default
2026-09-03 329e3db39ff13516b8aceb86e869de363be79229 test: make phase failures unswallowable
2026-09-03 da62139a68ef9dcd2e3f08b9488ab97852995fcf docs(rage): record third false-green and hard RED gate
2026-09-03 8c60d925d9e29f177c1d4d09ecd0bdec08d00b49 test: make Prolog recovery RED fail closed
2026-09-03 504b38246f19fcc7eedd506786a1f92e6865d68c rage: record second false-green and fail-closed RED harness
2026-09-03 d05d7dc401b9463e284104ab079d5f6b9058bbbb test: make Prolog config RED gate fail closed
2026-09-03 b1e49d9cdf4a79059f3f216324683c2a2edda1bd rage: record false-green harness and corrected RED candidate
2026-09-03 e0974ff2b23fc757c2a7b44bdfa02af4a710dee6 test: run recovery PlUnit separately so RED cannot false-green
2026-09-03 28f4c7d7658cd8780a447f20612d7382fe4920ed rage: record issue 309 research design and RED candidate
2026-09-03 291975c0dc2c3fe611a11c52f7f1957918ca1dee test: include issue 309 recovery unit in Prolog config gate
2026-09-03 17dec76d5d4229cee4e13d351202e0e486258ba9 test: define RED config recovery contract for issue 309
2026-09-03 696a3883a460a3b05e2ebbef16186378df01767a rage: design issue 309 config recovery contract
2026-09-03 1d89c457b12881129cb6a8926997a1057a440e65 rage: research issue 309 config authority regression
2026-09-03 6da4aa595d16cb3f1b7dd0ed81a86595407a850c rage: consume issue 309 from exact master
2026-09-03 e6d9409e49246a187d5ea015da681bfc4e4fdc63 Merge pull request #308 from lost-rob0t/docs/260-customization-wiki
2026-09-03 5a2999390ffe29ad10d8c4208c59d2a0e7bd6399 docs: document hooks advice and agent backends
2026-09-03 ea787f5807d54ef1801e083e9f250d1bf386e762 docs(rage): record #260 customization wiki slice
2026-09-03 e15fe203c69ef8196430aa5479158ccfde2e2322 Merge pull request #306 from lost-rob0t/rage/260-customization-diagnostics
2026-09-03 ad1fe996c6c221c30004e7012fbc9dbfc2b88a74 test: complete diagnostics manager fixture
2026-09-03 f014ff791568d5001eec7b3838c8218b18a3fb72 RAGE #159 RED: include adversarial device-action tests
2026-09-03 6dcc6c0ecafb908d13181053f62cb1f64b2976e0 RAGE #159 RED: harden action lifecycle contract
2026-09-03 4fe812d6a0097144a2cfc5ffae5a418b9ae67ccd RAGE #159: remove one-shot apply harness
2026-09-03 aa963063bdabc8e6dbd69c88fb16c0354911cb5d RAGE #159: remove one-shot apply workflow
2026-09-03 c64c408b051e618904b0b25f7eca9728af032eb9 docs(rage): record diagnostics red and implementation
2026-09-03 f57abe38d6f002694805215bf64e2709e5c41e56 test(rage): use canonical runtime host shutdown
2026-09-03 c37c0a6539e963ed2784abdf9d5cd7213ab02af0 feat(rage): expose customization diagnostics from runtime host
2026-09-03 8180f79b6c0bf598fbe8023c61fb595784baee04 [rage159-applied] RAGE #159: implement typed device actions
2026-09-03 f08caa98e76fafc2209bed0ea3fdde1112e08df9 RAGE #159: tighten gateway patch anchor
2026-09-03 f3274ad75adc78f58599ae6d1b4b399ca9fc3731 feat(rage): expose runtime customization diagnostics
2026-09-03 50d522dbbcecbcd294f8282a358ceb8ab8847e93 RAGE #159: run one-shot implementation harness
2026-09-03 6cd63f28f03a6b9e6679cf4fbc21b8fe5307f0f6 feat(rage): expose bounded customization diagnostics
2026-09-03 1ed47f4dfd365646b429adc4258e693c0505200a RAGE #159: add one-shot implementation harness
2026-09-03 1b3008aabd0919a64f127ede4b3c666313316497 feat(rage): add safe backend diagnostics projection
2026-09-03 b410fe531bdd4e620b2835b0db556b3805c705c4 feat(rage): add safe advice diagnostics projection
2026-09-03 fa1e5e74bc89f56a84c40a69ce35109320683d2a test(rage): require runtime customization diagnostics seam
2026-09-03 0387f8adf2e3627fac291ae48b3682338f698e9f RAGE #159: freeze device-action design
2026-09-03 832c2ec4fa2cac125f03df9651c0bab586e5de5c RAGE #159: record protocol research
2026-09-03 8f602872227903c8a6c1110068e84e47c3e1f83a RAGE #159 RED: add focused device-action gate
2026-09-03 b8f2413a149230f247f99b904ab494c489c1bf7d RAGE #159 RED: require typed device-action protocol
2026-09-03 b6d2754ef6b2c25e3bfeb2ba80b8840d2c674021 RAGE #159: consume typed device-action protocol
2026-09-03 94aeeae839da4f4d71241100d018f4b4b83c1bdb test: define #260 customization diagnostic contract
2026-09-03 d04e2a38a07f94c2c4b322c7f912d7a597324184 rage: design #260 customization diagnostics
2026-09-03 7c70219cb393302145582d31c28b00f214f112d6 rage: research #260 customization diagnostics
2026-09-03 41c323131f9a0df73f934d72e3388c3183eb3539 rage: start #260 customization diagnostics
2026-09-03 6141ac7d28c5eb32f0a8e78b31643792aa2c0fd7 Merge pull request #305 from lost-rob0t/rage/260-agent-loop-backend-registry
2026-09-03 fc573aa8898478187fe9500c69ae81eedae44c76 rage: record override policy for loop backend selection
2026-09-03 acf10a9f2e1167dc22b47ef451e5b71aecec9db2 test: enforce override gate for custom loop backend
2026-09-03 44f81d910a73a606eb53c97faac1e035f57a01e5 fix: enforce hook override gate for custom loop backends
2026-09-03 27994cd898af42dce339b222f3eafed782349c9b feat: gate custom loop backends behind override policy
2026-09-03 fa6a6699045fe759188c0d8c60df0a1847435056 test: cover implicit langgraph backend default
2026-09-03 b17cbe3e34f724e023992bc8f75fefa85684d33d feat: resolve configured agent loop through registry
2026-09-03 dc78c7c970c564584649ccf3b85fee387ffa11c1 feat: add owner-safe agent loop backend registry
2026-09-03 2c6f9707220828d4318b4c5c9f7cd9ac5559c18c test: define RED contract for named agent loop backends
2026-09-03 4953cf0cb3fc3c932e7ca73e13d2c2d6f93d394a rage: record #260 agent backend registry design
2026-09-02 7a89d6d0efeac92ba2ff47203882c2a89b663ede Merge pull request #304 from lost-rob0t/rage/260-service-plugin-advice
2026-09-02 70413aabc66c077d4757c1bc9663253d3478230a RAGE #260: wire service-plugin advice through RuntimeHost
2026-09-02 08c2bef5e317065820da49f927ebcee0e16c9fd0 Merge pull request #299 from lost-rob0t/rage/android-172-cross-runtime-parity
2026-09-02 27aa25c12258f76c7018aeb8f765150ad34dd25c chore(android): reconcile #172 parity with current master
2026-09-02 c07914416b5995f5b708e51790544151714e82bd Merge pull request #303 from lost-rob0t/rage/zara-004-config-durability
2026-09-02 b8ec2eae62ffef834be03cd6e8c84f88b519306a fix(android): make ambiguity matching Trealla-portable
2026-09-02 096c6606dc6f790f40c99f86ea85d19a0c2ece9a RAGE #5: record config layering implementation
2026-09-02 96ca65eb033d4d90f06310cd13696f31c378655f RAGE #5: layer mutable Prolog config over provisioned base
2026-09-02 7b891ffee6b91ba4fa31b9d33b1ffc44d36f757e RAGE #5: enforce explicit PLUnit result accounting
2026-09-02 c5444b6354767965ecf70c74046122a42c7f8105 RAGE #5: make Prolog test failure set process status
2026-09-02 2ece25e99c98bbbc8a753d95f792f2beeb9b52af RAGE #5: make PLUnit config gate target the loaded unit
2026-09-02 e80a24d4c99737420cae9f14aa2ad18b816976a9 fix(android): treat whitespace-only utterances as empty
2026-09-02 f6dd1da9df1b2a9cd5a932104ef76a2af13f3841 RAGE #5: record false-green harness finding
2026-09-02 b33dd78fe728d4badd40753e880eac254a305ee7 RAGE #5: make Prolog config test launcher fail closed
2026-09-02 9df18df47c5afb0657c8b6662a30c440a3a8d3e6 RAGE #5 RED: require durable local Prolog config overlay
2026-09-02 0902076daea66474b7ba4ea322f6d939ed8fb32e RAGE #5: record config durability transaction and design
2026-09-02 7e72d98e0cfc262294f01ed177416a3b2c3bf275 Merge pull request #298 from lost-rob0t/rage/260-prolog-command-advice
2026-09-02 d74f89ca0173db2cac2ccecbca4aef318de97b56 fix(android): compare portable parity attestations
2026-09-02 94416a0bcee155440d78966549c8c6b7ddb00d62 fix(android): handle empty utterances portably
2026-09-02 6a30b3d254478237b4f2557d28ed534e4e8845a1 rage: record Trealla string_to_atom recovery
2026-09-02 3853fea309de9040e5042f95315ba3766569ee3c fix(android): remove Trealla string_to_atom dependency
2026-09-02 3e6e4352c62055f621d2b73ac63fcba19a29c19e RAGE #260: implement gated Prolog command-loop advice
2026-09-02 bd50e6b235daeb0af347274d12ac68031fb57e39 fix(android): preserve state-control frame semantics
2026-09-02 5416af7be1b814af70a980bdf05e32fa56fcac94 fix(android): remove atom_string from portable intent entrypoint
2026-09-02 b8cdbbdab66792dede09971d5826bb3494d1f6ff Merge pull request #264 from lost-rob0t/feature/long-horizon-tasks
2026-09-02 9a62ab423b5ed80c023d0de9b11c356ef6855b93 docs(rage): record Trealla normalizer portability failure
2026-09-02 5bcba65649accc0b7757fb1b59a85c330e624084 fix(android): make shared normalizer portable to Trealla
2026-09-02 b7cc0a85a6d84352c668d8e892e01b2b5f5e0e79 RAGE #264: expose principal identity through runtime backend
2026-09-02 7d363fe7a3f6c532a9fb9cf41d87c0175246e311 rage: record Android parity diagnostic recovery
2026-09-02 cfa53c3358fd1cdd83145024d8f417db4832b48d ci(android): upload semantic parity diagnostics
2026-09-02 783a5d1a3c7ad1a23989aa00fa03c804be64e270 test(android): preserve parity failure diagnostics
2026-09-02 fdff7ef91a13a57199c1f6637b77006a8fc73907 RAGE #264: apply narrow long-horizon task config delta
2026-09-02 bbcc59fe880c114e7761cdde9407f27a81d8f5c3 RAGE #264: isolate historical task config delta
2026-09-02 3c8d07a9336884e4789abc01a936a304bb4c6968 RAGE #264: drop unrelated config rewrite churn
2026-09-02 442d0571ff6af830e5c1cf3375ff35bb61ae874b RAGE #264: port long-horizon tasks onto current RuntimeHost
2026-09-02 b60b826c146ec36f367573665d31360efc4bc87f RAGE #264: port bounded long-horizon task configuration
2026-09-02 9b999de0f5aee37fdeccc5ab4516e00debfb79ba build(android): declare fail-closed Trealla patch tooling
2026-09-02 8c624c5b4196e1760e25a26e5f7700c66a00c32c test(android): bind parity to native Trealla compatibility patch
2026-09-02 ca791c8161a61e9a184639cee868c8f823e2e2e8 test(android): keep staging contract source-faithful
2026-09-02 38804a6894e4b7fee85483a2e6eaf0c47a1c8b24 test(android): parity uses patched Trealla runtime
2026-09-02 27a9774ab034c93d10f424a5bbb9709b2f38b320 fix(android): patch Trealla module source paths
2026-09-02 6728c3499c7c47ccc102f549514b08cfb2cebe14 fix(android): preserve Trealla module source paths
2026-09-02 85425ad4813537641119adaf1dac10dfec305b4d test(android): require cwd-independent semantic loader
2026-09-02 2b6b3f49cbfee70b1026c517dcf8a4d6005cf80c RAGE #264: isolate long-horizon task turns at runtime backend
2026-09-02 dc698488011ace1c90575aa501bd64e42f1cc793 RAGE #264: port task turn context through current agent advice loop
2026-09-02 a4cfa984999f549682370c838a39c723e944c49c RAGE #172: record headless Trealla build recovery
2026-09-02 866c22ee932ef3148231ad21ab81c347f05ed061 RAGE #172: build headless pinned Trealla for parity
2026-09-02 0f10ea918eacbca6edc443c02c7b3b289c79b0a9 RAGE #172: correct parity target to canonical corpus
2026-09-02 3c72bfc97eab77173ba273220c784034247ce4b6 RAGE #172: keep parity toolchain minimal
2026-09-02 7112e1025af4341f97544b0db23e858d2db18aea RAGE #172: execute full canonical semantic corpus
2026-09-02 ba916142d4d3f87dd9a675f61052c0659649e40f RAGE #172: require canonical corpus in parity gate
2026-09-02 4854917a80731636c9f896b8db7dce50c1199042 RAGE #172: record RED and parity implementation
2026-09-02 137842cd801e0904a5da9aff164be40779d14d94 RAGE #172: wire executable semantic parity into Android gate
2026-09-02 94a66f2f190fd702ff0683d27efbf5679fdcac94 RAGE #172: add executable SWI Trealla parity gate
2026-09-02 249e51b4246b6f54523fcf51ecfeb8a48db81e22 RAGE #172: add parity runtimes to Android dev shell
2026-09-02 52e16d5d02cb2d8ba2b4a0074a84bcad4bd04133 RAGE #172: add RED cross-runtime parity gate contract
2026-09-02 90896a3821d3448fa7b7d0c8c460075256affd79 RAGE #172: record cross-runtime parity design
2026-09-02 9a05d0021e84b978dee009ceac288cfb07faa398 RAGE #264: port task runtime events onto current event model
2026-09-02 7c78907d42a067c457fff920e54aeaf3da342002 RAGE #264: rebase long-horizon task core onto current master
2026-09-02 9f3b779b876df360001b12d0100698f334beb8b8 Merge pull request #296 from lost-rob0t/rage/android-172-resolver-parity
2026-09-02 575e841503628f28c1cca3cfc638c7202b7e0d81 merge current master into Android #172 resolver parity
2026-09-02 4746ef00f973513d56112687553db32a3c13e3ba Merge pull request #297 from lost-rob0t/rage/260-python-user-hooks
2026-09-02 0e6f4ed0c6c8c76447acb29f18f7d4cdf659a104 merge master into Android #172 resolver parity
2026-09-02 2007e16928017b68956d8284bcf4ddbcc69b6668 docs(rage): record user hooks red and implementation
2026-09-02 deda2f310bf5fe71d997d61d7f315dd692462f8b feat(hooks): autoload mutable user hooks in agent runtime
2026-09-02 a628b8c093451a739da23ff8117337a6b11432b6 feat(hooks): load mutable user Python hooks
2026-09-02 416a88584a3b1c6aaefe9f9cd3d52c510fb978e0 docs(rage): record Android unit contract recovery
2026-09-02 8e4281b6244613bcbcfc8dbafa21a25602cf8f7f test(android): update portable resource contract for shared resolver
2026-09-02 5c1809c501f2a038d9a2f0b86f8ab0881e51de72 test #260: define Python user hook loader contract RED
2026-09-02 229bc423a9a435844e0de3e7669feb9e37935320 rage #260: record Python user hooks design
2026-09-02 b2ec0ee9c46ba94cedff7ec784f540b0bd9a6a00 rage #260: record Python user hooks research
2026-09-02 d281d2bacca4166105d861ecab0ed73b74bd03dc rage #260: start Python user hooks slice
2026-09-02 e66f43e0f5d3f22f79668ccc71a7098a3417883f docs(rage): record Android gate failure and output recovery
2026-09-02 39af84ecdc9262cfd761c5b8dbba7e32cee00b99 fix(android): configure portable semantic asset output
2026-09-02 f078a2d3f1bd10b60914153de486130bce787380 Merge pull request #293 from lost-rob0t/rage/260-agent-loop-integration
2026-09-02 09a27707d16246cc91e74d62b36efe8a15ab887f docs(rage): record Android gate failure recovery
2026-09-02 8824f042a482cb1019d89f70dd9b9db91d90ebe1 test(android): require bounded generated asset inputs
2026-09-02 2440469422b73ac101879317b26b82b7b5ceb832 fix(android): bound portable asset task inputs
2026-09-02 b8ba54f81cbbfd0a750b880466b183eb4a76b7c4 Merge master into rage/260-agent-loop-integration
2026-09-02 1f19fc2946ae2565f5f890089a391be17c61dce0 RAGE #172: record resolver packaging RED/GREEN and exact-head gate
2026-09-02 452814fa450cf5a66899e9bc3ed2dcf9afe8efd2 RAGE #172: make staged resource digest byte-stable
2026-09-02 6a0ce2db3646cd01d69dbe218d62492a57cdc824 RAGE #172: verify canonical resolver source packaging contract
2026-09-02 93b859b276de374179300dca2f879a0117a902ed RAGE #172: generate Android resolver assets from canonical Prolog sources
2026-09-02 5b50aebe2e4ed947370c87801f7363560d679ad8 RAGE #172: expose canonical resolver through portable core
2026-09-02 b59a205efd6b27ceb34e213f5ed89cdc94d01327 RAGE #172: initialize Trealla from complete staged semantic set
2026-09-02 afd0e0dffb097e56fddf33e5e5df7233ad1af9ac RAGE #172: stage complete portable resolver resource sets
2026-09-02 fd8827d4ef528a88a0bdc24dbe1a0f0082673de9 RAGE #172: declare canonical resolver assets
2026-09-02 63da392b2808658d598ca791f53025f7ccc47f14 RAGE #172 RED: require canonical resolver packaging and staging
2026-09-02 d55821e64efede075ca975e5f7ac30ff2f7e91ec RAGE #172: record Android resolver parity iteration
2026-09-02 753f79326f1be7dc77030c9950a08e2901827d8d Merge pull request #292 from lost-rob0t/rage/android-172-asset-staging
2026-09-02 f4b3189170ef4c7fd094f6b63937876634f71608 fix(agent): fail closed for partially constructed managers
2026-09-02 eadda3766a80060b4472a92ddf4164a96e2f1a39 RAGE #172: record asset-staging RED/GREEN evidence
2026-09-02 507962af225c269925df1d53bdfc845036e2d2ce RAGE #172: initialize Trealla from staged Android assets
2026-09-02 7b3b3ed69074ebd2af2a896a3510a319ccdaf41e RAGE #172: stage portable Prolog core into app-private storage
2026-09-02 1780e4142ce2f7e4e18a92258336a1284ffd5418 RAGE #172: name canonical portable semantic asset paths
2026-09-02 f4c2409b860a80ac93b3fe19e0a09703ddb9b0dc RAGE #172 RED: require deterministic Android Prolog asset staging
2026-09-02 43cf88b7a45168508459597819386364d457ee47 RAGE #172: record Android asset-staging iteration start
2026-09-02 accf1d7057d288cb11b62026c6507789324513e6 docs(rage): record #260 green-attempt regression and recovery
2026-09-02 dc90edfbcccfb99d61ea815aa30826bc35b406de Merge current master into #260 advice integration
2026-09-02 70efc7a71763cc006a4b2af3ed916e533719607f chore(#260): remove whitespace from advice integration fix
2026-09-02 858879bb28baa3c7f7a11d137bda28d333ed9fc7 fix(#260): fail closed for config adapters without hooks API
2026-09-02 0b2dc899bba6303f5ae4abeadbc909a44cf24b1e Merge pull request #290 from lost-rob0t/rage/android-172-native-adapter
2026-09-02 ed247cfe4c55c6b22f249a2bea0728eab3b1b920 rage: record #260 RED evidence and implementation boundary
2026-09-02 559f761a2ece818572c1f67de6d58fa89ae5a2be feat: route canonical agent loop through advice registry
2026-09-02 1a154ff72a513d06a806bf9ce3aa80b4bd25ade7 test: fix RAGE artifact whitespace before RED
2026-09-02 f1a08a84ad22f537f9fa67c3b6b565b36e97a318 test: define RED agent-loop advice integration contract
2026-09-02 656e9504f751a95a42ca36f600eeea741b0b5445 rage: design #260 agent-loop advice integration
2026-09-02 8b77a759b9cf4c37f26a4430f488c24e537e30bf rage: research #260 agent-loop advice integration
2026-09-02 16a8a526e92a78b02f21fdc11e8acdf9a18d37a5 rage: consume #260 agent-loop integration slice
2026-09-01 f956574916dff85e8ca92ebdcf4f5d7725245daf docs(rage): record #172 packaging green and master recovery
2026-09-01 e080c59dade0652aad806be679dd0548b8d0d13f chore(android): recover #172 native adapter onto current master
2026-09-01 a96b48d12d6fe0eb7bfb88d0a0e0559775974a9d Merge pull request #288 from lost-rob0t/rage/260-python-hooks-advice
2026-09-01 f2715253c4e7f885a1521409486e2a539653d8e2 docs(rage): record Android Trealla packaging RED and recovery
2026-09-01 7b5ef168956234506ad33730d33cf30e29cc5f3f fix(android): point at versioned NDK root
2026-09-01 3f33f44625cc4a11a91e0b2bcb76a480d4dfb09e build(android): pin exact Trealla source hash
2026-09-01 5ab3b1b3ba3c15dd0150dd70b00ece980aec16c3 ci(android): use Android-owned NDK toolchain
2026-09-01 025478efc3878999db6335ab6764d99d65d84106 build(android): require the pinned NDK version
2026-09-01 d7743d458ac3c63c798474b22482aed0738314df test(android): bind packaging proof to Android-owned toolchain
2026-09-01 5a2ebe0639cafd708edc00fc9ad91213d2b9e637 build(android): lock Android toolchain nixpkgs
2026-09-01 5494c8932b2708345b808d9cde69a712ed4244e4 feat(android): define pinned NDK and Trealla toolchain
2026-09-01 5044792caadc6ab7756ffa28c729d70b328f35a8 test(android): build native Trealla before APK gate
2026-09-01 d534c0674641f1003b118f1bb6e8c642bffeabf3 feat(android): build pinned Trealla for supported ABIs
2026-09-01 037346380650e230396a0d5e025e94db7c743435 feat(android): resolve pinned Trealla library per ABI
2026-09-01 2627c28dd6fb28b93ee5a54974e5482ebb80b338 feat(android): wire Trealla native build into APK
2026-09-01 e7a40b552c2ba1ae4a6235480336078fc3d18e25 test(android): require reproducible Trealla NDK packaging
2026-09-01 abeb9c39583ea11331662d5c62b80d59dc78b110 RAGE #172: record native adapter RED/GREEN evidence
2026-09-01 b65c54c4ce0aada001ffff96af7744050fb908e6 RAGE #172: define pinned Trealla native build contract
2026-09-01 80a072a3277209a77de86a39fca5d6ea4147fb5b RAGE #172 GREEN: add fail-closed Trealla JNI adapter source
2026-09-01 5e313630513b8df92bbe5615225d79526736d7fe RAGE #172 RED: require native Trealla JNI source contract
2026-09-01 7101099e41c407be2f31509e0ac154a836cac865 RAGE #172: start Android native Trealla adapter iteration
2026-09-01 6dee4a02abc3fba3f6750df35f5825c54c9535cc Merge master into RAGE #260 Python hooks slice
2026-09-01 518fef14a710b04c99f4509235ef244bdf4f9f34 docs(rage): record Python hooks RED and implementation
2026-09-01 e1c61a38b68fb0601f49152ca4d2205e4a5c41f7 Merge pull request #286 from lost-rob0t/rage/android-172-jni-bridge
2026-09-01 9e7895bd7087b947613093b6bb55ff3b045e5c27 feat(agent): implement bounded advice registry
2026-09-01 f2a9c09da861890e161bc30a7f01e8b3c13c350a test: RED Python hook/advice registry contract
2026-09-01 4012ddb16586da0bde8168026294484f60cce8bd rage: design #260 Python hook/advice registry
2026-09-01 579c9a5548bd8812050d52cc398ac9ee5a5aeeb7 rage: research #260 Python hook/advice seam
2026-09-01 7ea61cf90c37dd3ab467f4d302bb86431577f063 rage: start #260 Python hooks/advice iteration
2026-09-01 bb82778cca98de8eb2c4d1220a64900b80bd7f77 docs(rage): record #172 JNI bridge design and TDD evidence
2026-09-01 b26fc07dc3b06c50c08fb14efce988092e938c48 feat(android): add fail-closed Trealla JNI bridge boundary
2026-09-01 44427e416ce1613e8774ee42a059389f3191511d test(android): define Trealla JNI bridge fail-closed contract
2026-09-01 0988bbe5249ce5530144110ebabdb8d2986af080 rage(android): start #172 JNI bridge iteration
2026-09-01 89e6fbc6f17df0a86083b5e66dd1496c89555daf Merge pull request #283 from lost-rob0t/rage/android-172-trealla-runtime
2026-09-01 be75c73c0b32ca4cabd4837ca41e685d967e1ae3 docs(rage): record #172 stale-base recovery
2026-09-01 934aa4e6049b3b82202820f559b38a740e6518a8 merge(master): refresh Android #172 candidate
2026-09-01 800a740a36b57969cb5cf6bafbbf9dd52d68e4fe Merge pull request #281 from lost-rob0t/rage/260-hooks-prolog-config
2026-09-01 eadbd238f83abb8283332961e785e3d3e0af0ff1 Merge master into rage/260-hooks-prolog-config
2026-09-01 59de1e9a468672353f83ca6064bcc9070f658246 docs(rage): record Android semantic contract compile fix
2026-09-01 2c708f71f1fbe4cd1e1ad4c65233b2bcc233d3b2 fix(android): match semantic result terms contract
2026-09-01 1e2b9501fefa9fc1cb5e42fc6ee56991710c5889 docs: record hook policy RED and implementation
2026-09-01 632c7ec9edc935a2ca98a711e69fc9cc6490e615 test: create config directory in hook fixture
2026-09-01 78c2b2bc69be6802837785e80dd672d02536befa docs: define fail-closed hook policy projection
2026-09-01 6fa447ba2ae5672fa2dcb35cbd2eb6c7f4a76c8b feat: project hook policy from canonical TOML
2026-09-01 49c658bbde0c109826bf2f93d3073dca50e7740b test: keep daemon wiring scope unchanged
2026-09-01 496be51db4e8efbafc01a12f5d4eaab9bb367eaf test: drive hook policy from canonical TOML
2026-09-01 54525963735b792cd3d8945bb512ed939bcb6103 test: preserve existing runtime wiring coverage
2026-09-01 7e53146bd29278b6f15ebe3984cf22501cd0f01a test: apply hook policy at daemon Prolog boundary
2026-09-01 2344f338c3a8d63cdd9a1921b7ba1d1b6a92dcc5 feat: enforce explicit Prolog hook policy
2026-09-01 67c4367329bcacc8455780b846d8985b6313b222 test: gate user hooks behind explicit policy
2026-09-01 e3d5c4d8ed75aa580dadb3d97befc0901464dce1 RAGE #172 GREEN: add Trealla semantic runtime lifecycle
2026-09-01 ecec0caabf42efd5fc1d0040e559775872a148a0 RAGE #172 RED: specify Trealla semantic runtime lifecycle
2026-09-01 501923450ebed99670049ba6e0b45b4d92f909b1 RAGE #172: record Trealla runtime lifecycle iteration
2026-09-01 82eddb0a1c81dd1ae92c5e575e90e7d485a17bc8 Merge pull request #280 from lost-rob0t/rage/android-172-fixture-runner
2026-09-01 ae40572020ae59536ebe3c6834bc65919560753e Merge master into RAGE #260 recovery
2026-09-01 c82aea0a041411709b510c38ca6394dd8cce6e36 rage: record #172 cross-runtime runner iteration
2026-09-01 93dcd05ab5ce903a43f4d5b70fea8cff57a8eb9e RAGE #172 GREEN: add fail-closed semantic parity runner
2026-09-01 1a48be8515637f14494f34ed768e319f70d26081 RAGE #172 RED: require cross-runtime semantic fixture runner
2026-09-01 54c0e96fa75a6f2c5ba44b55d1f7a5f6e088fcf3 RAGE #172: normalize Android semantic parity results (#278)
2026-09-01 30d6b52609de219cb58b144cb85c2b7aad1a10d2 RAGE #260: recover hooks policy onto current master
2026-09-01 2833e8b2d4bd50a14b0674c34f688749b3b01f54 RAGE #172: package Android portable semantic assets (gate recovery) (#275)
2026-09-01 a77e4e866d38019f24af7ec3518f419e86f91e35 fix: rebase built-in todo surface toggle on current master (#272)
2026-09-01 928aee7105842cc50b9eff73c7b56980c414ef3b RAGE #172: portable Android Prolog semantic contract (#269)
2026-09-01 ed683b454bc15d14ca4fdec329640a1bf1d431d1 Merge pull request #259 from lost-rob0t/feature/agent-mode-core
2026-09-01 f17175e65f91bb00c100613d8a987da8bf3e9d82 rage: record PR 259 current-master recovery
2026-09-01 204ffe5f149df984af8ef04433133f11ac762bdd recover: rebase agent hooks and barge-in on current master
2026-09-01 4e539b5a74d95ccecf67976c132ccf68ed10485a Merge pull request #267 from lost-rob0t/rage/244-wake-daemon-voice
2026-09-01 8687662306224516feaaf13c9f7bbc2e0208f5a1 Merge pull request #265 from lost-rob0t/docs/244-merge-evidence
2026-09-01 d1f2cf666ec5e7e8c7314e2f6ed1e58d04eeed89 fix(wake): restore ack player wiring broken by the daemon migration
2026-09-01 ce3271bde9df5215754c91f97ea1d8986af00022 Merge pull request #263 from lost-rob0t/rage/244-wake-daemon-voice
2026-09-01 e0b29ec0b482b90efbc354a67979136be725e8e4 docs(rage): record issue 244 merge evidence
2026-09-01 ddfad5f8453691ccaba05e4d30d8a7d9070c06f3 chore(rage): fix wake research whitespace gate
2026-09-01 867c7ce219489b525889d6aa827a962e27d17583 test: extend agent-mode backend double for the latency_trace contract
2026-09-01 8ef404126afa149b9b7d9b54eb494f6fb574c482 Merge remote-tracking branch 'origin/master' into rage/244-wake-daemon-voice
2026-09-01 45bc17c60c0b74b51872c72a172600d46b2b1991 docs(rage): record issue 244 implementation evidence and gate results
2026-09-01 eeeadc4180275186f5974226267e98de91f7c82b Merge pull request #261 from lost-rob0t/docs/250-merge-evidence
2026-09-01 76b4f8ad7aec19956af600243913b85c130a8f07 feat(config): add [daemon] section for wake client endpoint, audio output rate, and auth keys
2026-09-01 70edb119647d97a8d3c1a93b06e4ac5319a0221f test(wake): prove two-principal isolation and end-to-end trace continuity
2026-09-01 57ee4ae060c932d996344134aa85f0ebe00a453b docs(rage): record 250 merge evidence
2026-08-31 7a9c25cf31c4088568e2b50e49f47ce05a0a0172 feat(stt): route AMD device tokens to the whisper.cpp Vulkan backend (#258)
2026-08-31 cc256c130cccc2914a4d900c62e6ccf3979d1e85 feat(wake): migrate wake listener onto the daemon ZARA/1 voice client
2026-08-31 ddac73abe02a2b90732262b3bc0d90dff57a922b Merge pull request #257 from lost-rob0t/feature/agent-mode-core
2026-08-31 a1623daabacc08b2ffb252647074a9ebe10572fe Test agent-mode routing prompt precedence
2026-08-31 5ee36fe99b1ea2dd9dbdd7d3f829056d8803a27f Route autonomous and speech requests to service tools
2026-08-31 a2300848bf155d463db5dfe2e11ffdd388be2199 Document first-party core plugin exception
2026-08-31 b8d4f82da3af8207abd159fc27fb9798fa19763c Cover agent mode TTS without microphone ownership
2026-08-31 8848efdeefbeb26d0fcf70488027512a2574b002 Document core autonomous agent mode
2026-08-31 dc1ed103ed1fb9dd8b63278c9ed92d332d9c1a61 Test core agent mode plugin
2026-08-31 e4162c8a991c7d9cea042d2ce1109846fe443bc3 Discover toggleable first-party core plugins
2026-08-31 b251060e3feed01924bb1fc6c6836094a738c67e Add toggleable core agent mode plugin
2026-08-31 317722b475b28c0edae126a3221f30ae04eb4dea Add builtin plugin package
2026-08-31 58887a7dfd6bbd969bd07e9f3a3af71e78beca40 Merge pull request #253 from lost-rob0t/rage/158-api-service-providers
2026-08-31 8eead19b462c2131c73b124e96f97bc25ecafef6 Merge branch 'master' into rage/158-api-service-providers
2026-08-31 9554387ad83c8a70008fa7dd4a9b4e6ba1bfba92 Merge pull request #254 from lost-rob0t/docs/249-merge-evidence
2026-08-31 64eff4e69a25f9f70df07d6d6a55ce9fb4a02844 Merge branch 'master' into rage/158-api-service-providers
2026-08-31 5f8e0fd1e3f1e60e5b1e71b415375753ccf98496 Merge pull request #252 from lost-rob0t/rage/249-latency-trace-checkpoint
2026-08-31 8456119a2cedafebc0af3ec16b3635f114611dac docs(rage): record 249 merge evidence
2026-08-31 9b14af1cf5bd7b59bc1e83e169220f4f1f85d499 docs(rage): record 249 red/green evidence and exact-head gates
2026-08-31 10f1258ab00b2409d8c1ddee8e6bd196697a4ac9 fix(runtime): server boot drops kb_config module collision; engine singleton
2026-08-31 d823a0300b909a7639b78924f3e732e32024f9fa fix(agent): keep latency traces out of checkpointed graph state
2026-08-31 1a43d1ca2f51f7f647fa61eed6ce572797b333b2 docs(wiki): api-service provider registry and config split; capability-plans scope note
2026-08-31 34fb840480fff1456414e3bb1f42b4d9fe7bbdc8 feat(runtime): versioned api_service registry, plan execution service, host wiring
2026-08-31 142e295f03cc8b56b721adeaec8f3be8d7269754 feat(kb): split device provider configuration from shared semantic config
2026-08-31 7201e9b8e69028eb166c55226497587797c46ea5 feat(wake): add thin daemon voice client adapter for the wake listener
2026-08-31 29162a90e5e6c9d6343b571ef74804c84aedd698 test: extend gateway double for negotiated audio output format capture
2026-08-31 899a52b2bb3e6acf95e6f2e3d930bfb53f6272dc feat(runtime): add daemon TTS output bridge producing ZARA/1 audio.output streams
2026-08-31 cc5ade3023cee40b702cb4e05ad716b7094e22fa docs(planning): regenerate backlog for 158 consumption
2026-08-31 ec0c74a39a9cd99aabee2795a0f4abfd92966949 Merge pull request #241 from lost-rob0t/codex/zara-discord-plugin-guidance
2026-08-31 c18323b4b4891fada06efb000d9f50daedee21e0 docs(rage): record 157 merge evidence; regenerate backlog post-merge
2026-08-31 65313760cfa4102468b77cf045a2680505f37a6f Merge branch 'master' into codex/zara-discord-plugin-guidance
2026-08-31 2054ac1d368b175a85518c258f6a9cf6647f69a4 Merge pull request #247 from lost-rob0t/rage/157-execution-plans
2026-08-31 5fcd5a54d3267696640bbc1debb1ef8a2800c26d feat(runtime): stream assistant phrase events and persist turns to principal memory
2026-08-31 ccb2807723888e01560f9526d7b971acc5dbe56d docs(rage): record 157 tdd evidence and gate results
2026-08-31 2c1907e0ab3fc48e544ad1a0fcd038f1aea3940e feat(runtime): add daemon-side Prolog-first intent router with per-turn latency traces
2026-08-31 a3646137a51bfb71a723edd4905072a47e33ebc5 test(gate): capability plan phase; docs(wiki): capability plans page
2026-08-31 205da6eb983c1ba468ae8d86f946b85475566021 feat(runtime): typed ExecutionPlan mirror, PrologEngine plan boundary, PlanExecutor
2026-08-31 3da07e5168ace5aa768b1283906eed0fa2e1c05b feat(prolog): pure capability reasoning with typed ExecutionPlans
2026-08-31 f0ddfef3250d834ce6d3b11872035dc14b691f31 docs(rage): record issue 244 research and design artifacts
2026-08-31 930088c6b6b2f488243b84c025f62039125ca3f5 docs(rage): record 157 adversarial review
2026-08-31 4d08f7f152c45a778ab53af464c8329dd9f8b880 docs(rage): record 157 research, design, adversarial-review decisions
2026-08-31 13b7b1d863dde90966d5ee12524891b5b2c0bb75 docs(rage): record 157 run identity and queue state at consumption
2026-08-31 f58b551df7ce411d17277d4073a8121b47824145 docs(rage): record #156 merge evidence; regenerate backlog post-merge
2026-08-31 7ae4b7f7a716f302f3ad9299df3f3b1d9322e3a5 Merge pull request #245 from lost-rob0t/chore/backlog-244
2026-08-31 18659368cd00d57f3ea8c6da5534cb141e05f8c0 docs: define external plugin configuration contract
2026-08-31 37410f988055939579e5bbbfb8e4a789e3d299fb chore(backlog): import issue 244 and refresh closed-issue mirror
2026-08-31 4f77de3c7dec0cebf711a5ffdad04fd136354693 Merge pull request #243 from lost-rob0t/rage/156-prolog-frames
2026-08-31 7d5e17693463d2f9f9479df564474d3eea3fc958 Merge branch 'master' into rage/156-prolog-frames
2026-08-31 8f2581cefd79890788ca83d46dedb2c4f0fd4d7b feat(prolog): adapt resolution to IntentFrame with canonical semantic corpus
2026-08-31 de7c91c80a1380781ef41d0b6a85d0f1725d812a Merge pull request #242 from lost-rob0t/fix/agent-openrouter-server-entrypoint
2026-08-31 8e212f8ccba35ea1a31e2faae2b058455e8951b0 fix(server): keep one PrincipalContext under the -m entrypoint
2026-08-31 34a0638ec83a9c9fc0b44be72be390454f7be714 fix(agent): add OpenRouter provider to the agent ChatModel factory
2026-08-31 5fef90c22c64508ca7595018b4e02281182e7936 docs: define external plugin configuration contract
2026-08-31 170d33bc71221c1eacb069609274425e8b893c50 Merge pull request #239 from lost-rob0t/rage/28-post-merge-evidence
2026-08-31 1ff26122e32baba1446f6a07461a668412db6afc Merge pull request #237 from lost-rob0t/perf/zara-027-streaming-llm-impl
2026-08-31 da4e70eb619ac131143b94ba38e28bb50bfc2667 docs(rage): record issue 28 merge closeout
2026-08-31 14a6fdfdf0b5a1d165ffdb1986f71e89b4d84d00 Merge remote-tracking branch 'origin/master' into perf/zara-027-streaming-llm-impl
2026-08-31 c72a930da2127870f01513f0d6fde90c3f57252a docs: record ZARA-027 exact-head gate results
2026-08-31 aa5c396a75a336fae86fcbd13c35aca2161a7092 docs: record ZARA-027 RAGE implementation evidence and update wiki
2026-08-31 24643d71de59acd75c498af9e5c9832de6cb2dae feat(agent,llm): stream LLM/agent output with cancellation-safe text events
2026-08-31 a4ccec2c7947038fcd30e546c421ac55a3073897 feat(agent): add typed stream events and pure sentence chunker
2026-08-31 64ee53c1ee107fc93c46ed92568bd538e33f9de1 docs(rage): record #156 run identity, research, design, adversarial review
2026-08-31 55b3bb84c649afb620a139d9e4c28eadbc26d48f docs(rage): record #155 merge evidence; regenerate backlog post-merge
2026-08-31 f053f41f2997a8c4054baef5238a84554d0826d8 Merge pull request #236 from lost-rob0t/rage/155-typed-slots
2026-08-31 7c31c456add5ae637cbe161932b3421073aaf03b Merge branch 'master' into rage/155-typed-slots
2026-08-31 0f5734b64d71a02f1a9aa9d42e5d54cb131a0ee3 docs(rage): record #155 TDD and gate evidence; regenerate backlog mirror
2026-08-31 1911487a925f7808a08ee643a1b93356cf9fc4e7 feat(runtime): typed slots and principal/conversation-scoped clarification dialogue
2026-08-31 ec89bd448e9812fbf6cfc722cdc8616e0eaab8ec Merge pull request #235 from lost-rob0t/test/live-smoke-reasoning-budgets
2026-08-31 29107ad04a3ef0d3214611ca717584ba342af39e test: raise live smoke token budget for reasoning models
2026-08-31 95b10090095cd096ff63da5ed5b494a516fa474d Merge pull request #234 from lost-rob0t/feature/openrouter-rlm-directmode
2026-08-31 04734f220b5345e94ad7ff5ffe6ae3869b2ff85c docs(rage): record #155 run identity, research, design, adversarial review
2026-08-31 e60b5bd69ddf24c3b5580668a393c9452a45fef6 test: add OpenRouter live smoke scripts for client and RLM direct mode
2026-08-30 7ad29b117ab8aa8b6f708b6341793eaedeb6a723 Merge pull request #233 from lost-rob0t/feature/openrouter-rlm-directmode
2026-08-30 708bb515c365e1cfc62dd7a37d214cbb9bb1c5d9 merge: resolve kb/config and prolog_config conflicts with master wake_word
2026-08-30 be17d2dbbc4a8cd4c0b70cafc87929a8638dd91b feat: add OpenRouter provider and Prolog-RLM direct-mode rewrites
2026-08-30 0aed7d6c89f4be5c1733a3ced4b1fd423cb5b23e Merge pull request #232 from lost-rob0t/rage/154-intentframe-contract
2026-08-30 f42f0cad1126dbcf23df282e02f880bf6ffb62b9 docs(rage): freeze IntentFrame v1 contract with 154 research and migration design
2026-08-30 0661a2d56d2f8ebcc02fcecdc7f2be8334e90983 Merge pull request #231 from lost-rob0t/chore/backlog-import
2026-08-30 88b6b53ebdf301c4efee5947efe84af769ccad1a feat(planning): import backlog state from GitHub issues with Prolog-verifiable mirror
2026-08-29 90b0c821f944d6b5edc2e381b0318ea44a116224 Merge pull request #230 from lost-rob0t/rage/195-samsung-assistant-research
2026-08-29 b53a469ec08e71f4b075e69d85814b51709df416 docs(rage): record 195 Samsung assistant research gate and decision record
2026-08-29 38e98a4c6e683d590d8682af98803ba9987f3418 Merge pull request #229 from lost-rob0t/feat/android-app
2026-08-29 2d3f9c57eccb58f611a2d294f170bdf7a1b19655 Merge branch 'master' into feat/android-app
2026-08-29 b09d9e44c4693aa8bb9518f3911cbefec749b5b3 feat(android): Android skeleton with reproducible Nix/Gradle gate (#170, #171)
2026-08-29 ad2f43d2cfe914f1ac1c2b06f9048d477a2d4c9b Merge pull request #228 from lost-rob0t/feature/wake-words-edit-distance
2026-08-29 5fce64fa43e994efa934077e7d8f0ca67f2506be feat(wake): Zarathushtra wake word with edit-distance matching
2026-08-29 e5a4f26e37f65289b225aaeffc7d692512765ff1 Merge pull request #227 from lost-rob0t/perf/zara-027-streaming-llm
2026-08-29 3d12c6df67c1b716f337820bfac017db0b9870a7 docs(rage): record 28 streaming LLM research and design artifacts
2026-08-29 dc51f12ac17a9b771b63345a2539285319bf7939 Merge pull request #226 from lost-rob0t/docs/134-reentry-assessment
2026-08-29 bb171a8d251f6e3865afccd9010ee3f04978879b docs(rage): record 134 re-entry assessment and queue correction
2026-08-29 6811cdf56ba232f8cc1ec1610cbe60b662e0cbd4 Merge pull request #190 from lost-rob0t/rage/134-daemon-release-gate
2026-08-29 fcc4af3080d6258b5aec484424194df6f44bd4df Merge branch 'master' into rage/134-daemon-release-gate
2026-08-29 429f99614b30497ca012cd1e9106a89e1deee98c Merge pull request #184 from lost-rob0t/rage/131-merge-closeout
2026-08-29 823aab5bada50f2b30b6bf56a2f417455d147160 Merge branch 'master' into rage/131-merge-closeout
2026-08-29 ff8f4b47a50e12882b569105ea7c61ee7d00c728 Merge pull request #146 from lost-rob0t/docs/rage-130-merge-outcome
2026-08-29 85e6dfa4c7b5cd3c264e27bc435129ab2c1442ec Merge branch 'master' into rage/131-merge-closeout
2026-08-29 44ee97f35f3a2a96a324fdf98afe0e1ffc6f39cd Merge branch 'master' into docs/rage-130-merge-outcome
2026-08-29 cea85d3c523e5690170f7a40bce0da5303bce9f0 Merge pull request #225 from lost-rob0t/docs/rage-17-merge-outcome
2026-08-29 634b105b67b989b7e68c7893f976adb6c7d1e7de Merge pull request #224 from lost-rob0t/fix/zara-016-llm-provider-contracts
2026-08-29 a503012ba0cfda67c57640a17243d15035787264 docs(rage): record issue 17 merge outcome
2026-08-29 fe43c9e8cf1966ef3d08051f15f5e99dead882b6 docs(rage): record ZARA-016 gate evidence
2026-08-29 7985353d048e46e9120276256f335eaa73a28ab4 fix(llm): classify arity-2 socket_error as connection failure
2026-08-29 4acbda423f605f2f5edb5d34aa3e8871ea480b54 docs(rage): open ZARA-016 iteration log for issue 17
2026-08-28 a04435d2b73b44dffd52e00aff3bf478d5a48d6b Merge pull request #221 from lost-rob0t/build/flake-update-2026-08
2026-08-28 6567bce87d6a60cc9891a22bb9699484a5f24a6b build(flake): update nixpkgs, pin python313, adopt nixpkgs sherpa-onnx
```

## Repository paths changed, last 14 days

```text
.github/workflows/ci.yml
.github/workflows/rage-159-apply.yml
.github/workflows/rage-575-apply-green.yml
.github/workflows/release-v0.1.0-alpha.yml
.github/workflows/release.yml
AGENTS.md
PRODUCT.md
README.org
android/.gitignore
android/AGENTS.md
android/DESIGN.md
android/app/build.gradle.kts
android/app/src/main/AndroidManifest.xml
android/app/src/main/assets/prolog/.gitkeep
android/app/src/main/assets/prolog/portable/semantic_core.pl
android/app/src/main/assets/prolog/portable/semantic_fixtures.json
android/app/src/main/cpp/CMakeLists.txt
android/app/src/main/cpp/zara_trealla_jni.c
android/app/src/main/java/ai/zara/app/AndroidAppSession.kt
android/app/src/main/java/ai/zara/app/MainActivity.kt
android/app/src/main/java/ai/zara/app/ZaraApplication.kt
android/app/src/main/java/ai/zara/app/assistant/AndroidAssistantRolePlatform.kt
android/app/src/main/java/ai/zara/app/assistant/AssistantInvocationGate.kt
android/app/src/main/java/ai/zara/app/assistant/AssistantLifecycleFence.kt
android/app/src/main/java/ai/zara/app/assistant/AssistantRoleController.kt
android/app/src/main/java/ai/zara/app/assistant/AssistantRoleVoicePolicy.kt
android/app/src/main/java/ai/zara/app/assistant/AssistantVoiceSessionBridge.kt
android/app/src/main/java/ai/zara/app/assistant/ZaraVoiceInteractionService.kt
android/app/src/main/java/ai/zara/app/assistant/ZaraVoiceInteractionSession.kt
android/app/src/main/java/ai/zara/app/assistant/ZaraVoiceInteractionSessionService.kt
android/app/src/main/java/ai/zara/app/auth/AndroidCredentialCipher.kt
android/app/src/main/java/ai/zara/app/auth/AuthCore.kt
android/app/src/main/java/ai/zara/app/auth/EnrollmentRepository.kt
android/app/src/main/java/ai/zara/app/auth/JeroMqAuth.kt
android/app/src/main/java/ai/zara/app/device/AndroidAppLauncher.kt
android/app/src/main/java/ai/zara/app/device/AndroidUriLauncher.kt
android/app/src/main/java/ai/zara/app/device/DeviceActionTypes.kt
android/app/src/main/java/ai/zara/app/device/DeviceCapabilityRegistry.kt
android/app/src/main/java/ai/zara/app/device/OpenAppAdapter.kt
android/app/src/main/java/ai/zara/app/device/OpenUriAdapter.kt
android/app/src/main/java/ai/zara/app/device/OpenUriPolicy.kt
android/app/src/main/java/ai/zara/app/device/RegistryDeviceActionHandler.kt
android/app/src/main/java/ai/zara/app/prolog/NativeTreallaBridge.kt
android/app/src/main/java/ai/zara/app/prolog/PortableSemanticAssetStager.kt
android/app/src/main/java/ai/zara/app/prolog/PortableSemanticCore.kt
android/app/src/main/java/ai/zara/app/prolog/SemanticFixtureRunner.kt
android/app/src/main/java/ai/zara/app/prolog/SemanticResultComparator.kt
android/app/src/main/java/ai/zara/app/prolog/TreallaSemanticRuntime.kt
android/app/src/main/java/ai/zara/app/runtime/AndroidTextSessionController.kt
android/app/src/main/java/ai/zara/app/runtime/ClientStateStore.kt
android/app/src/main/java/ai/zara/app/runtime/ConnectionFailureReason.kt
android/app/src/main/java/ai/zara/app/runtime/DeviceActionHandler.kt
android/app/src/main/java/ai/zara/app/runtime/EnrollmentProjection.kt
android/app/src/main/java/ai/zara/app/runtime/JeroMqTextDealer.kt
android/app/src/main/java/ai/zara/app/runtime/RequestCorrelations.kt
android/app/src/main/java/ai/zara/app/runtime/RuntimeState.kt
android/app/src/main/java/ai/zara/app/runtime/ServerProfile.kt
android/app/src/main/java/ai/zara/app/runtime/ZaraCapabilityCodec.kt
android/app/src/main/java/ai/zara/app/runtime/ZaraDeviceActionCodec.kt
android/app/src/main/java/ai/zara/app/runtime/ZaraTextClientActor.kt
android/app/src/main/java/ai/zara/app/runtime/ZaraTextCodec.kt
android/app/src/main/java/ai/zara/app/runtime/ZaraVoiceHelloCodec.kt
android/app/src/main/java/ai/zara/app/ui/AssistantSetupGuidance.kt
android/app/src/main/java/ai/zara/app/ui/ThemePreferenceStore.kt
android/app/src/main/java/ai/zara/app/ui/UiOperationFailure.kt
android/app/src/main/java/ai/zara/app/ui/ZaraApp.kt
android/app/src/main/java/ai/zara/app/voice/AndroidAudioFocusPlatform.kt
android/app/src/main/java/ai/zara/app/voice/AndroidAudioRoutePlatform.kt
android/app/src/main/java/ai/zara/app/voice/AndroidPcmOutput.kt
android/app/src/main/java/ai/zara/app/voice/AndroidPcmRecorder.kt
android/app/src/main/java/ai/zara/app/voice/AudioFocusController.kt
android/app/src/main/java/ai/zara/app/voice/AudioRouteController.kt
android/app/src/main/java/ai/zara/app/voice/AuthenticatedVoiceIngress.kt
android/app/src/main/java/ai/zara/app/voice/ManualVoiceCapture.kt
android/app/src/main/java/ai/zara/app/voice/ManualVoiceSessionCoordinator.kt
android/app/src/main/java/ai/zara/app/voice/PushToTalkController.kt
android/app/src/main/java/ai/zara/app/voice/VoiceDiagnosticFailure.kt
android/app/src/main/java/ai/zara/app/voice/VoicePlaybackController.kt
android/app/src/main/java/ai/zara/app/voice/VoiceRuntimeSessionPolicy.kt
android/app/src/main/java/ai/zara/app/voice/VoiceStreamReducer.kt
android/app/src/main/java/ai/zara/app/voice/VoiceStreamSinkActor.kt
android/app/src/main/java/ai/zara/app/voice/ZaraVoiceAckCodec.kt
android/app/src/main/java/ai/zara/app/voice/ZaraVoiceCodec.kt
android/app/src/main/java/ai/zara/app/voice/ZaraVoiceInboundCodec.kt
android/app/src/main/java/ai/zara/app/voice/ZaraVoiceStreamCodec.kt
android/app/src/main/res/xml/voice_interaction_service.xml
android/app/src/test/java/ai/zara/app/BuildMetadataTest.kt
android/app/src/test/java/ai/zara/app/assistant/AppScopedAssistantRuntimeContractTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantInvocationGateTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantLifecycleFenceTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantRoleControllerTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantRoleVoiceGuardTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantRoleVoicePolicyTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantRoleVoiceWiringContractTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantServiceManifestContractTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantUiErrorRedactionContractTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantVoiceSessionBridgeTest.kt
android/app/src/test/java/ai/zara/app/assistant/PlaybackSessionInvalidationContractTest.kt
android/app/src/test/java/ai/zara/app/auth/AuthenticationRevocationAdversarialTest.kt
android/app/src/test/java/ai/zara/app/auth/AuthenticationTest.kt
android/app/src/test/java/ai/zara/app/device/AndroidUriLauncherContractTest.kt
android/app/src/test/java/ai/zara/app/device/DeviceCapabilityRegistryTest.kt
android/app/src/test/java/ai/zara/app/device/OpenAppAdapterTest.kt
android/app/src/test/java/ai/zara/app/device/OpenAppWiringContractTest.kt
android/app/src/test/java/ai/zara/app/device/OpenUriAdapterTest.kt
android/app/src/test/java/ai/zara/app/device/OpenUriPolicyTest.kt
android/app/src/test/java/ai/zara/app/prolog/CrossRuntimeParityGateContractTest.kt
android/app/src/test/java/ai/zara/app/prolog/NativeTreallaBridgeTest.kt
android/app/src/test/java/ai/zara/app/prolog/NativeTreallaPackagingContractTest.kt
android/app/src/test/java/ai/zara/app/prolog/NativeTreallaSourceContractTest.kt
android/app/src/test/java/ai/zara/app/prolog/PortableResolverPackagingContractTest.kt
android/app/src/test/java/ai/zara/app/prolog/PortableSemanticAssetStagerTest.kt
android/app/src/test/java/ai/zara/app/prolog/PortableSemanticAssetsTest.kt
android/app/src/test/java/ai/zara/app/prolog/PortableSemanticCoreTest.kt
android/app/src/test/java/ai/zara/app/prolog/SemanticFixtureRunnerTest.kt
android/app/src/test/java/ai/zara/app/prolog/SemanticResultComparatorTest.kt
android/app/src/test/java/ai/zara/app/prolog/TreallaSemanticRuntimeTest.kt
android/app/src/test/java/ai/zara/app/runtime/AndroidReconnectSchedulerFailureTest.kt
android/app/src/test/java/ai/zara/app/runtime/AndroidTextSessionControllerTest.kt
android/app/src/test/java/ai/zara/app/runtime/AndroidTextSessionObserverTest.kt
android/app/src/test/java/ai/zara/app/runtime/AndroidTextSessionRestartTest.kt
android/app/src/test/java/ai/zara/app/runtime/ClientStateStoreTest.kt
android/app/src/test/java/ai/zara/app/runtime/ConnectionFailureReasonTest.kt
android/app/src/test/java/ai/zara/app/runtime/EnrollmentProjectionTest.kt
android/app/src/test/java/ai/zara/app/runtime/RequestCorrelationTest.kt
android/app/src/test/java/ai/zara/app/runtime/RuntimeStateTest.kt
android/app/src/test/java/ai/zara/app/runtime/ServerProfileTest.kt
android/app/src/test/java/ai/zara/app/runtime/StockZaraServerInteropTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraCapabilityCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraDeviceActionCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraDeviceActionCodecTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientActorTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientCapabilitiesTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientDeviceActionTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientVoiceFloodTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientVoiceNegotiationTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientVoicePumpTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientVoiceTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextCodecTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextTurnOrderingTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraVoiceHelloCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraVoiceNegotiationTest.kt
android/app/src/test/java/ai/zara/app/security/AndroidProductionLoggingContractTest.kt
android/app/src/test/java/ai/zara/app/ui/ThemePreferenceStoreTest.kt
android/app/src/test/java/ai/zara/app/ui/UiOperationFailureTest.kt
android/app/src/test/java/ai/zara/app/ui/ZaraAppProjectionTest.kt
android/app/src/test/java/ai/zara/app/voice/AudioFocusControllerTest.kt
android/app/src/test/java/ai/zara/app/voice/AudioFocusSynchronousLossTest.kt
android/app/src/test/java/ai/zara/app/voice/AudioRouteControllerTest.kt
android/app/src/test/java/ai/zara/app/voice/AuthenticatedVoiceIngressTest.kt
android/app/src/test/java/ai/zara/app/voice/ManualVoiceCaptureTest.kt
android/app/src/test/java/ai/zara/app/voice/ManualVoiceSessionCoordinatorTest.kt
android/app/src/test/java/ai/zara/app/voice/PushToTalkCloseFailureTest.kt
android/app/src/test/java/ai/zara/app/voice/PushToTalkControllerTest.kt
android/app/src/test/java/ai/zara/app/voice/PushToTalkFailurePrecedenceTest.kt
android/app/src/test/java/ai/zara/app/voice/RecorderFailureDiagnosticWiringContractTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceDiagnosticFailureTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceDiagnosticWiringContractTest.kt
android/app/src/test/java/ai/zara/app/voice/VoicePlaybackAudioFocusTest.kt
android/app/src/test/java/ai/zara/app/voice/VoicePlaybackCloseFailureTest.kt
android/app/src/test/java/ai/zara/app/voice/VoicePlaybackControllerTest.kt
android/app/src/test/java/ai/zara/app/voice/VoicePlaybackStartFailurePrecedenceTest.kt
android/app/src/test/java/ai/zara/app/voice/VoicePlaybackTerminalStopFailureTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceRuntimeSessionPolicyTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceSessionInvalidationWiringContractTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamBargeInTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamReducerTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamSinkActorTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamSinkFailureStateTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamSinkObserverFailureTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamSinkSelfCloseTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceAckCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceAckCodecTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceCodecTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceInboundCodecTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceStreamCodecTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceStreamPayloadLimitTest.kt
android/build-trealla.sh
android/build.gradle.kts
android/design/reference-2026-09-07.svg
android/flake.lock
android/flake.nix
android/gradle.properties
android/gradle/libs.versions.toml
android/integration/device_acceptance.py
android/integration/stock_zara_server_fixture.py
android/patch-trealla-module-path.sh
android/settings.gradle.kts
docs/README.org
docs/STT.md
docs/architecture.org
docs/development.org
docs/intentframe-contract.md
docs/research/002-unified-copilot-voice-visual-ci.md
docs/server.org
flake.lock
flake.nix
kb/capabilities.pl
kb/config.pl
kb/device_providers.pl
kb/intents.pl
kb/semantic_corpus.pl
kb/server_providers.pl
main.pl
modules/capability_plans.pl
modules/command_loop.pl
modules/commands.pl
modules/config_loader.pl
modules/dictate.pl
modules/hooks_loader.pl
modules/intent_frames.pl
modules/intent_resolver.pl
modules/llm_client.pl
modules/normalizer.pl
modules/rlm_rewrite.pl
modules/sound.pl
modules/zara_hooks.pl
planning/backlog.pl
rage/13-open-app-allowlist-regression.org
rage/133-daemon-default-regression.org
rage/133-desktop-daemon-default-regression.org
rage/134-daemon-release-gate.org
rage/154-intentframe-design.org
rage/154-intentframe-research.org
rage/154-intentframe.org
rage/155-clarification-dialogue.org
rage/156-prolog-frames.org
rage/157-execution-plans.org
rage/158-api-service-providers.org
rage/159-zara1-device-actions-design.org
rage/159-zara1-device-actions-research.org
rage/159-zara1-device-actions.org
rage/160-semantic-first-runtime.org
rage/162-user-command-persistence.org
rage/163-user-command-compiler.org
rage/164-user-command-authoring.org
rage/165-user-command-runtime.org
rage/17-zara016-provider-contracts.org
rage/170-android-bakeoff.org
rage/171-android-skeleton.org
rage/172-android-asset-staging.org
rage/172-android-fixture-runner.org
rage/172-android-jni-bridge.org
rage/172-android-native-adapter.org
rage/172-android-portable-prolog.org
rage/172-android-resolver-parity.org
rage/172-android-trealla-runtime.org
rage/172-cross-runtime-parity.org
rage/173-android-auth.org
rage/173-android-client-continuity.org
rage/174-android-device-capabilities.org
rage/174-android-open-app-aliases.org
rage/175-android-audio-focus-lifecycle.org
rage/175-android-barge-in.org
rage/175-android-manual-voice.org
rage/175-android-streamed-voice.org
rage/178-android-auth-revocation-r2.org
rage/178-android-capability-revocation-r3.org
rage/178-android-daemon-restart-stale-turn-r2.org
rage/178-android-device-action-replay-r4.org
rage/178-android-json-depth-bound-r2.org
rage/178-android-no-raw-logging-r5.org
rage/178-android-principal-target-abuse-r2.org
rage/178-android-prolog-lifecycle-r3.org
rage/178-android-reconnect-storm-r3.org
rage/178-android-release-matrix.org
rage/178-android-uri-intent-abuse-r4.org
rage/178-android-voice-hello-json-depth-r1.org
rage/178-capability-json-depth-bound.org
rage/195-samsung-assistant-research.org
rage/196-android-assistant-role.org
rage/196-ui-closed-runtime.org
rage/197-compose-first-usable.org
rage/203-android-assistant-role-loss-r3.org
rage/203-android-assistant-role-loss-wiring-r2.org
rage/203-android-assistant-shutdown-fence.org
rage/203-android-audio-route-lifecycle.org
rage/203-android-audio-route-rollback-failure-r2.org
rage/203-android-connection-error-redaction.org
rage/203-android-mic-permission-lifecycle.org
rage/203-android-playback-session-invalidation-r2.org
rage/203-android-reconnect-scheduler-failure-r2.org
rage/203-android-recorder-failure-diagnostics-r2.org
rage/203-android-state-store-temp-isolation-r2.org
rage/203-android-ui-close-runtime-ownership-r3.org
rage/203-android-ui-error-redaction-r2.org
rage/203-android-voice-diagnostic-redaction-r2.org
rage/203-android-voice-runtime-invalidation-primitives-r2.org
rage/203-android-voice-session-invalidation-r4.org
rage/216-transcript-normalization-contract-r2.org
rage/217-s1-mini-normalizer-r4.org
rage/218-normalizer-config-r4.org
rage/244-wake-daemon-voice-design.org
rage/244-wake-daemon-voice-research.org
rage/244-wake-daemon-voice.org
rage/246-todo-toggle-recovery.org
rage/249-latency-trace-checkpoint-design.org
rage/249-latency-trace-checkpoint-research.org
rage/249-latency-trace-checkpoint.org
rage/250-amd-stt-device-routing-design.org
rage/250-amd-stt-device-routing-research.org
rage/250-amd-stt-device-routing.org
rage/259-agent-hooks-recovery.org
rage/260-agent-loop-backend-registry.org
rage/260-agent-loop-integration-design.org
rage/260-agent-loop-integration-research.org
rage/260-agent-loop-integration.org
rage/260-customization-diagnostics-design.org
rage/260-customization-diagnostics-research.org
rage/260-customization-diagnostics.org
rage/260-customization-wiki.org
rage/260-hooks-prolog-config-design.org
rage/260-hooks-prolog-config-research.org
rage/260-hooks-prolog-config.org
rage/260-prolog-command-advice-design.org
rage/260-prolog-command-advice-research.org
rage/260-prolog-command-advice.org
rage/260-python-hooks-advice-design.org
rage/260-python-hooks-advice-research.org
rage/260-python-user-hooks-design.org
rage/260-python-user-hooks-research.org
rage/260-python-user-hooks.org
rage/260-service-plugin-advice.org
rage/28-streaming-llm-design.org
rage/28-streaming-llm.org
rage/29-streaming-tts-provider-recovery-r10.org
rage/29-streaming-tts-recovery-r7.org
rage/309-prolog-config-recovery-design.org
rage/309-prolog-config-recovery-research.org
rage/309-prolog-config-recovery.org
rage/315-route-backpressure-test-contract.org
rage/324-expanded-history-sidebar-r2.org
rage/324-unified-copilot-r2.org
rage/324-unified-copilot-research-r2.org
rage/326-desktop-toggle.org
rage/327-bounded-target-edit-distance-recovery.org
rage/329-production-secure-listener.org
rage/329-threat-model.org
rage/348-dash-prefixed-z85-cli.org
rage/371-plugin-approval-contract.org
rage/388-plugin-cancellation-r16.org
rage/388-plugin-cancellation-r17.org
rage/492-device-action-replay-r3.org
rage/5-config-durability.org
rage/575-gateway-send-diagnostics.org
rage/575-stock-interop-diagnostics.org
rage/575-transient-send-backpressure-r3.org
rage/587-dictation-vulkan.org
rage/long-horizon-tasks.org
scripts/benchmark-voice.py
scripts/import-backlog.py
scripts/rage-159-apply.py
scripts/security-fuzz-soak.sh
scripts/test-all.sh
scripts/test-android-device.sh
scripts/test-android-release.sh
scripts/test-android-semantic-parity.sh
scripts/test-android.sh
scripts/test-api-service.sh
scripts/test-capability-plans.sh
scripts/test-command-routing.sh
scripts/test-hooks.sh
scripts/test-openrouter-live.sh
scripts/test-process-safety.sh
scripts/test-prolog-command-advice.sh
scripts/test-prolog-config.sh
scripts/test-prolog-rlm-live.sh
scripts/test-replies.sh
scripts/test-rlm-rewrite.sh
scripts/test-s1-mini-normalizer.sh
scripts/test-streaming-llm.sh
scripts/test-streaming-tts.sh
scripts/test-user-command-authoring.sh
scripts/test-user-command-compiler.sh
scripts/test-user-command-persistence.sh
scripts/test-zara1-device-actions.sh
server_main.pl
t/api_service.pl
t/capability_plans.pl
t/dictation_lifecycle.pl
t/llm_clients.pl
t/process_safety.pl
t/prolog_config.pl
t/prolog_config_recovery.pl
t/rlm_rewrite.pl
t/security_threat_catalog.py
t/security_threat_extensions.py
t/sounds.pl
t/test_adaptive_copilot.py
t/test_agent_hooks.py
t/test_agent_loop_advice_integration.py
t/test_agent_loop_backend_registry.py
t/test_agent_mode_core_plugin.py
t/test_agent_mode_voice_barge_in.py
t/test_android_gate_diagnostics.py
t/test_api_service.py
t/test_backend_turn_services.py
t/test_backlog_import.py
t/test_capability_plans.py
t/test_clarification_session.py
t/test_cli_client_migration.py
t/test_cli_semantic_modes.py
t/test_client.py
t/test_command_routing.py
t/test_config.py
t/test_conversation_flow.py
t/test_conversation_service.py
t/test_copilot_controller_collapse.py
t/test_copilot_screenshot_ci.py
t/test_copilot_screenshot_fixtures.py
t/test_customization_diagnostics.py
t/test_daemon_client_config.py
t/test_daemon_intent_router.py
t/test_daemon_tts_output.py
t/test_database_fetch_locking.py
t/test_desktop_control.py
t/test_desktop_launch_surface.py
t/test_desktop_preferences.py
t/test_desktop_toggle_control.py
t/test_device_action_replay_contract.py
t/test_device_action_sequence_wiring.py
t/test_dialogue_script.py
t/test_dictation_vulkan_backend.py
t/test_hooks_config.py
t/test_host_api_service.py
t/test_json_limits.py
t/test_latency_metrics.py
t/test_llm.py
t/test_llm_streaming.py
t/test_plan_executor.py
t/test_plans.py
t/test_plugin_tool_approval.py
t/test_principal_runtime_wiring.py
t/test_production_secure_listener.py
t/test_prolog_frame_adapter.py
t/test_qt_runtime_bridge.py
t/test_quick_copilot.py
t/test_registered_target_recovery.py
t/test_runtime_backend_publisher.py
t/test_runtime_host.py
t/test_runtime_host_clarification.py
t/test_runtime_intent_routing.py
t/test_s1_mini_normalizer.py
t/test_s1_mini_numeric_bounds.py
t/test_security_admin_permissions_placeholder.py
t/test_security_adversarial.py
t/test_security_chaos.py
t/test_security_device_action_integration.py
t/test_security_fuzz.py
t/test_security_process_chaos.py
t/test_security_quota_control_plane.py
t/test_security_threat_dependency.py
t/test_security_threat_extensions.py
t/test_security_threat_gateway.py
t/test_security_threat_json_depth.py
t/test_security_threat_lifecycle_sequences.py
t/test_security_threat_management.py
t/test_security_threat_model.py
t/test_security_threat_protocol_depth.py
t/test_security_threat_reconnect.py
t/test_security_threat_transport.py
t/test_semantic_corpus.py
t/test_semantic_first_runtime.py
t/test_sentence_chunker.py
t/test_server.py
t/test_service_plugin_advice.py
t/test_task_approval_flow.py
t/test_task_host_wiring.py
t/test_task_observability.py
t/test_task_runner.py
t/test_task_store.py
t/test_task_tools.py
t/test_task_turn_context.py
t/test_tasks_config.py
t/test_todo_surface_toggle.py
t/test_toolnode_dispatch_contract.py
t/test_transcript_normalization.py
t/test_transcript_normalization_config.py
t/test_transcript_normalization_selection.py
t/test_tts.py
t/test_tts_output_lifecycle.py
t/test_tts_provider_recovery.py
t/test_user_command_authoring.py
t/test_user_command_authoring_acceptance.py
t/test_user_command_compiler.py
t/test_user_command_persistence.py
t/test_user_command_runtime.py
t/test_user_python_hooks.py
t/test_voice_runtime_ingress.py
t/test_wake_clarification.py
t/test_wake_daemon_client.py
t/test_wake_fail_closed.py
t/test_wake_import.py
t/test_wake_latency_continuity.py
t/test_wake_lifecycle.py
t/test_wake_model_debug.py
t/test_wake_principal_isolation.py
t/test_wake_speaker.py
t/test_wake_words.py
t/test_whisper_cpp.py
t/test_zara1_device_actions.py
t/test_zara1_device_actions_adversarial.py
t/test_zara_hooks_registry.py
t/test_zmq_send_diagnostics.py
t/test_zmq_transient_backpressure.py
t/test_zmq_transport_route_backpressure.py
t/zara_hooks_registry.pl
wiki/agent-mode.org
wiki/android.org
wiki/api-service.org
wiki/capability-plans.org
wiki/customization.org
wiki/install.org
wiki/long-horizon-tasks.org
wiki/plugins.org
zara/__main__.py
zara/agent/__init__.py
zara/agent/graph.py
zara/agent/hooks.py
zara/agent/loops.py
zara/agent/prompting.py
zara/agent/sentence_chunker.py
zara/agent/stream_events.py
zara/agent/tools/builtin_tools.py
zara/agent/tools/registry.py
zara/agent/user_hooks.py
zara/command_gate.py
zara/config.py
zara/console.py
zara/daemon_client.py
zara/database.py
zara/desktop/app.py
zara/desktop/control.py
zara/desktop/controller.py
zara/desktop/preferences.py
zara/desktop/ui_fixtures.py
zara/desktop/windows/__init__.py
zara/desktop/windows/copilot.py
zara/desktop/windows/quick.py
zara/desktop/windows/settings.py
zara/device_action_replay.py
zara/dictate.py
zara/json_limits.py
zara/latency.py
zara/llm.py
zara/plugins/api.py
zara/plugins/builtin/__init__.py
zara/plugins/builtin/agent_mode.py
zara/plugins/builtin/agent_mode_hooks.py
zara/plugins/manager.py
zara/principals.py
zara/prolog_engine.py
zara/protocol.py
zara/protocol_runtime.py
zara/python_skills.py
zara/runtime/api_service.py
zara/runtime/backend.py
zara/runtime/clarification.py
zara/runtime/events.py
zara/runtime/frames.py
zara/runtime/host.py
zara/runtime/intent_router.py
zara/runtime/plans.py
zara/runtime/tts_output.py
zara/s1_mini_normalizer.py
zara/security.py
zara/security_admin.py
zara/security_gateway.py
zara/security_state.py
zara/security_transport.py
zara/server.py
zara/server_core.py
zara/speech_activity.py
zara/tasks/__init__.py
zara/tasks/runner.py
zara/tasks/store.py
zara/transcript_normalization.py
zara/transcript_normalization_config.py
zara/transcript_normalization_selection.py
zara/user_command_authoring.py
zara/user_command_compiler.py
zara/user_command_runtime.py
zara/user_commands.py
zara/voice_runtime.py
zara/wake.py
zara/wake_daemon.py
zara/wake_words.py
zara/zmq_transport.py
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/ci.yml
.github/workflows/rage-159-apply.yml
.github/workflows/rage-575-apply-green.yml
.github/workflows/release-v0.1.0-alpha.yml
.github/workflows/release.yml
android/app/src/test/java/ai/zara/app/BuildMetadataTest.kt
android/app/src/test/java/ai/zara/app/assistant/AppScopedAssistantRuntimeContractTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantInvocationGateTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantLifecycleFenceTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantRoleControllerTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantRoleVoiceGuardTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantRoleVoicePolicyTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantRoleVoiceWiringContractTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantServiceManifestContractTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantUiErrorRedactionContractTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantVoiceSessionBridgeTest.kt
android/app/src/test/java/ai/zara/app/assistant/PlaybackSessionInvalidationContractTest.kt
android/app/src/test/java/ai/zara/app/auth/AuthenticationRevocationAdversarialTest.kt
android/app/src/test/java/ai/zara/app/auth/AuthenticationTest.kt
android/app/src/test/java/ai/zara/app/device/AndroidUriLauncherContractTest.kt
android/app/src/test/java/ai/zara/app/device/DeviceCapabilityRegistryTest.kt
android/app/src/test/java/ai/zara/app/device/OpenAppAdapterTest.kt
android/app/src/test/java/ai/zara/app/device/OpenAppWiringContractTest.kt
android/app/src/test/java/ai/zara/app/device/OpenUriAdapterTest.kt
android/app/src/test/java/ai/zara/app/device/OpenUriPolicyTest.kt
android/app/src/test/java/ai/zara/app/prolog/CrossRuntimeParityGateContractTest.kt
android/app/src/test/java/ai/zara/app/prolog/NativeTreallaBridgeTest.kt
android/app/src/test/java/ai/zara/app/prolog/NativeTreallaPackagingContractTest.kt
android/app/src/test/java/ai/zara/app/prolog/NativeTreallaSourceContractTest.kt
android/app/src/test/java/ai/zara/app/prolog/PortableResolverPackagingContractTest.kt
android/app/src/test/java/ai/zara/app/prolog/PortableSemanticAssetStagerTest.kt
android/app/src/test/java/ai/zara/app/prolog/PortableSemanticAssetsTest.kt
android/app/src/test/java/ai/zara/app/prolog/PortableSemanticCoreTest.kt
android/app/src/test/java/ai/zara/app/prolog/SemanticFixtureRunnerTest.kt
android/app/src/test/java/ai/zara/app/prolog/SemanticResultComparatorTest.kt
android/app/src/test/java/ai/zara/app/prolog/TreallaSemanticRuntimeTest.kt
android/app/src/test/java/ai/zara/app/runtime/AndroidReconnectSchedulerFailureTest.kt
android/app/src/test/java/ai/zara/app/runtime/AndroidTextSessionControllerTest.kt
android/app/src/test/java/ai/zara/app/runtime/AndroidTextSessionObserverTest.kt
android/app/src/test/java/ai/zara/app/runtime/AndroidTextSessionRestartTest.kt
android/app/src/test/java/ai/zara/app/runtime/ClientStateStoreTest.kt
android/app/src/test/java/ai/zara/app/runtime/ConnectionFailureReasonTest.kt
android/app/src/test/java/ai/zara/app/runtime/EnrollmentProjectionTest.kt
android/app/src/test/java/ai/zara/app/runtime/RequestCorrelationTest.kt
android/app/src/test/java/ai/zara/app/runtime/RuntimeStateTest.kt
android/app/src/test/java/ai/zara/app/runtime/ServerProfileTest.kt
android/app/src/test/java/ai/zara/app/runtime/StockZaraServerInteropTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraCapabilityCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraDeviceActionCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraDeviceActionCodecTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientActorTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientCapabilitiesTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientDeviceActionTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientVoiceFloodTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientVoiceNegotiationTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientVoicePumpTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientVoiceTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextCodecTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextTurnOrderingTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraVoiceHelloCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraVoiceNegotiationTest.kt
android/app/src/test/java/ai/zara/app/security/AndroidProductionLoggingContractTest.kt
android/app/src/test/java/ai/zara/app/ui/ThemePreferenceStoreTest.kt
android/app/src/test/java/ai/zara/app/ui/UiOperationFailureTest.kt
android/app/src/test/java/ai/zara/app/ui/ZaraAppProjectionTest.kt
android/app/src/test/java/ai/zara/app/voice/AudioFocusControllerTest.kt
android/app/src/test/java/ai/zara/app/voice/AudioFocusSynchronousLossTest.kt
android/app/src/test/java/ai/zara/app/voice/AudioRouteControllerTest.kt
android/app/src/test/java/ai/zara/app/voice/AuthenticatedVoiceIngressTest.kt
android/app/src/test/java/ai/zara/app/voice/ManualVoiceCaptureTest.kt
android/app/src/test/java/ai/zara/app/voice/ManualVoiceSessionCoordinatorTest.kt
android/app/src/test/java/ai/zara/app/voice/PushToTalkCloseFailureTest.kt
android/app/src/test/java/ai/zara/app/voice/PushToTalkControllerTest.kt
android/app/src/test/java/ai/zara/app/voice/PushToTalkFailurePrecedenceTest.kt
android/app/src/test/java/ai/zara/app/voice/RecorderFailureDiagnosticWiringContractTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceDiagnosticFailureTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceDiagnosticWiringContractTest.kt
android/app/src/test/java/ai/zara/app/voice/VoicePlaybackAudioFocusTest.kt
android/app/src/test/java/ai/zara/app/voice/VoicePlaybackCloseFailureTest.kt
android/app/src/test/java/ai/zara/app/voice/VoicePlaybackControllerTest.kt
android/app/src/test/java/ai/zara/app/voice/VoicePlaybackStartFailurePrecedenceTest.kt
android/app/src/test/java/ai/zara/app/voice/VoicePlaybackTerminalStopFailureTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceRuntimeSessionPolicyTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceSessionInvalidationWiringContractTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamBargeInTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamReducerTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamSinkActorTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamSinkFailureStateTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamSinkObserverFailureTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamSinkSelfCloseTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceAckCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceAckCodecTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceCodecTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceInboundCodecTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceStreamCodecTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceStreamPayloadLimitTest.kt
android/flake.nix
flake.nix
scripts/benchmark-voice.py
scripts/import-backlog.py
scripts/rage-159-apply.py
scripts/security-fuzz-soak.sh
scripts/test-all.sh
scripts/test-android-device.sh
scripts/test-android-release.sh
scripts/test-android-semantic-parity.sh
scripts/test-android.sh
scripts/test-api-service.sh
scripts/test-capability-plans.sh
scripts/test-command-routing.sh
scripts/test-hooks.sh
scripts/test-openrouter-live.sh
scripts/test-process-safety.sh
scripts/test-prolog-command-advice.sh
scripts/test-prolog-config.sh
scripts/test-prolog-rlm-live.sh
scripts/test-replies.sh
scripts/test-rlm-rewrite.sh
scripts/test-s1-mini-normalizer.sh
scripts/test-streaming-llm.sh
scripts/test-streaming-tts.sh
scripts/test-user-command-authoring.sh
scripts/test-user-command-compiler.sh
scripts/test-user-command-persistence.sh
scripts/test-zara1-device-actions.sh
t/api_service.pl
t/capability_plans.pl
t/dictation_lifecycle.pl
t/llm_clients.pl
t/process_safety.pl
t/prolog_config.pl
t/prolog_config_recovery.pl
t/rlm_rewrite.pl
t/security_threat_catalog.py
t/security_threat_extensions.py
t/sounds.pl
t/test_adaptive_copilot.py
t/test_agent_hooks.py
t/test_agent_loop_advice_integration.py
t/test_agent_loop_backend_registry.py
t/test_agent_mode_core_plugin.py
t/test_agent_mode_voice_barge_in.py
t/test_android_gate_diagnostics.py
t/test_api_service.py
t/test_backend_turn_services.py
t/test_backlog_import.py
t/test_capability_plans.py
t/test_clarification_session.py
t/test_cli_client_migration.py
t/test_cli_semantic_modes.py
t/test_client.py
t/test_command_routing.py
t/test_config.py
t/test_conversation_flow.py
t/test_conversation_service.py
t/test_copilot_controller_collapse.py
t/test_copilot_screenshot_ci.py
t/test_copilot_screenshot_fixtures.py
t/test_customization_diagnostics.py
t/test_daemon_client_config.py
t/test_daemon_intent_router.py
t/test_daemon_tts_output.py
t/test_database_fetch_locking.py
t/test_desktop_control.py
t/test_desktop_launch_surface.py
t/test_desktop_preferences.py
t/test_desktop_toggle_control.py
t/test_device_action_replay_contract.py
t/test_device_action_sequence_wiring.py
t/test_dialogue_script.py
t/test_dictation_vulkan_backend.py
t/test_hooks_config.py
t/test_host_api_service.py
t/test_json_limits.py
t/test_latency_metrics.py
t/test_llm.py
t/test_llm_streaming.py
t/test_plan_executor.py
t/test_plans.py
t/test_plugin_tool_approval.py
t/test_principal_runtime_wiring.py
t/test_production_secure_listener.py
t/test_prolog_frame_adapter.py
t/test_qt_runtime_bridge.py
t/test_quick_copilot.py
t/test_registered_target_recovery.py
t/test_runtime_backend_publisher.py
t/test_runtime_host.py
t/test_runtime_host_clarification.py
t/test_runtime_intent_routing.py
t/test_s1_mini_normalizer.py
t/test_s1_mini_numeric_bounds.py
t/test_security_admin_permissions_placeholder.py
t/test_security_adversarial.py
t/test_security_chaos.py
t/test_security_device_action_integration.py
t/test_security_fuzz.py
t/test_security_process_chaos.py
t/test_security_quota_control_plane.py
t/test_security_threat_dependency.py
t/test_security_threat_extensions.py
t/test_security_threat_gateway.py
t/test_security_threat_json_depth.py
t/test_security_threat_lifecycle_sequences.py
t/test_security_threat_management.py
t/test_security_threat_model.py
t/test_security_threat_protocol_depth.py
t/test_security_threat_reconnect.py
t/test_security_threat_transport.py
t/test_semantic_corpus.py
t/test_semantic_first_runtime.py
t/test_sentence_chunker.py
t/test_server.py
t/test_service_plugin_advice.py
t/test_task_approval_flow.py
t/test_task_host_wiring.py
t/test_task_observability.py
t/test_task_runner.py
t/test_task_store.py
t/test_task_tools.py
t/test_task_turn_context.py
t/test_tasks_config.py
t/test_todo_surface_toggle.py
t/test_toolnode_dispatch_contract.py
t/test_transcript_normalization.py
t/test_transcript_normalization_config.py
t/test_transcript_normalization_selection.py
t/test_tts.py
t/test_tts_output_lifecycle.py
t/test_tts_provider_recovery.py
t/test_user_command_authoring.py
t/test_user_command_authoring_acceptance.py
t/test_user_command_compiler.py
t/test_user_command_persistence.py
t/test_user_command_runtime.py
t/test_user_python_hooks.py
t/test_voice_runtime_ingress.py
t/test_wake_clarification.py
t/test_wake_daemon_client.py
t/test_wake_fail_closed.py
t/test_wake_import.py
t/test_wake_latency_continuity.py
t/test_wake_lifecycle.py
t/test_wake_model_debug.py
t/test_wake_principal_isolation.py
t/test_wake_speaker.py
t/test_wake_words.py
t/test_whisper_cpp.py
t/test_zara1_device_actions.py
t/test_zara1_device_actions_adversarial.py
t/test_zara_hooks_registry.py
t/test_zmq_send_diagnostics.py
t/test_zmq_transient_backpressure.py
t/test_zmq_transport_route_backpressure.py
t/zara_hooks_registry.pl
```
