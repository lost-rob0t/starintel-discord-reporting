# lost-rob0t/zara

- generated: `2026-09-05T15:17:37Z`
- canonical branch: `master`
- changelog eligible: `yes`
- head: [`efe112f74b130ec39e81f2fc538818895e790ea5`](https://github.com/lost-rob0t/zara/commit/efe112f74b130ec39e81f2fc538818895e790ea5)
- head date: `2026-09-05T11:16:03-04:00`
- head subject: Merge pull request #390 from lost-rob0t/rage/326-desktop-toggle

## Git log, last 14 days

```text
2026-09-05 efe112f74b130ec39e81f2fc538818895e790ea5 Merge pull request #390 from lost-rob0t/rage/326-desktop-toggle
2026-09-05 d2cdaf3bb3e3f42fc2d571b243fd6a741fc6d83f fix(#326): keep desktop control owner alive after liveness probes
2026-09-05 2b0c536e48f5aefcd1609d3aaf09560f86eb09d9 RAGE #326: record local owner contract and exact CI long-path recovery
2026-09-05 c7510c075ed0b6564c4df088e095f18d25448449 RAGE #326: cover long-path fallback and stale endpoint parent
2026-09-05 e77924242ded113eb1d8570922a4a8c6bd5ba866 RAGE #326: bound AF_UNIX endpoint length with private hashed fallback
2026-09-05 75bba4088e9aba98a6e0a7f0c7fbb4a59438d34b RAGE #326: add bounded toggle/show/hide desktop CLI
2026-09-05 2c455acc75b43bb8ece1e7f387af6fef1ec7649e RAGE #326: reserve one desktop owner before client startup
2026-09-05 ff3b833e196f50356c1b4effc0e975bebb75f342 RAGE #326: preserve desktop cleanup while adding local control signal
2026-09-05 1671c2e5b5a6f87f0e71ed1d46d62cf08255c360 RAGE #326: route local desktop controls onto Qt owner
2026-09-05 a0bfbd2911edf30399c237174981aa441afdad30 RAGE #326: RED for CLI and duplicate-owner desktop control lifecycle
2026-09-05 6bbb8d62128ebe470f3c98cef1095e4fcdb6bf88 RAGE #326: prove failed duplicate cannot unlink live owner
2026-09-05 6ae5cb4c6e9f15ad50afc5280999e1e75bfdfa1c RAGE #326: make desktop socket ownership race-safe
2026-09-05 9c7372a452569dbed83a246ac3caa5b65ac3779b RAGE #326: implement bounded local desktop control socket
2026-09-05 596ab286d2179ec75060ec6b1288c7f5f6392dd9 test: require bounded owner-private desktop control IPC
2026-09-05 12aa5a88e01f5ca549f7533a1262190cfaa8f6f9 desktop: make tray primary activation a true toggle
2026-09-05 ca274ed7925d0c149cd87cc1ffc70d100253f951 rage: record #326 tray-toggle RED and repair
2026-09-05 d6e78031fbfc0bf7c9b1f9a78998681c0b2cbd2f test: require true tray toggle for Quick Copilot
2026-09-05 8299bba79fab04a787ffa4e7c74667c360adc6dc rage: consume #326 desktop toggle control
2026-09-05 3676fc7e452eab409305f62a826b9f0b1f9841d4 Merge pull request #383 from lost-rob0t/rage/29-streaming-tts-current-r7
2026-09-05 46753ddc60d661e3e8887c0801f0ba9e62e98e45 RAGE #29: recover bounded streaming TTS lifecycle on current master
2026-09-05 b839268b4cd63b30da455734ba1346b0bee02f05 Merge pull request #380 from lost-rob0t/rage/371-plugin-approval-current
2026-09-05 c814eecf64323b55a1913f81361d729657da879c core: recover #371 plugin approval contract on exact master
2026-09-05 03143a3cd4990734e3f9afaf63462c8b03108337 Merge pull request #373 from lost-rob0t/rage/196-ui-closed-runtime
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
2026-08-24 8dc7448e3d130e1ad4600e27621e72d5cd772b53 Merge pull request #214 from lost-rob0t/rage/191-post-merge-evidence-2
2026-08-24 51356e3cee216c3fb7f51aae308463b7e8f15c55 Merge pull request #213 from lost-rob0t/rage/191-zara1-tool-approvals-2
2026-08-24 ab34d02cdc958d95e9964489a291f3b19434c4b9 docs(rage): record issue 191 merge outcome
2026-08-24 c6c4e3080e7d3fb126824eae9dffaaa3dfa15e00 feat(protocol): carry authenticated tool approvals over ZARA/1
2026-08-24 55f4f76b2906a05f289f3720e339702d5139aa6d RAGE #209: record merge outcome (#212)
2026-08-24 ddc30c737ee7eff030dd424949a490f5c6cf52dd Merge pull request #211 from lost-rob0t/rage/209-runtime-tool-approvals
2026-08-24 ac0917228a912923de0807fe93fe71afee2e7dba docs(rage): record issue 209 merge outcome
2026-08-24 394a0ede032b0528b9eb727512666db9a822e09f docs(rage): record issue 209 local gates
2026-08-24 77d403c54c0c170ebb63fddc42ca5321e4c188af test(runtime): close approval coverage gaps
2026-08-24 39addc5ae729617c8bb3d9417a5fbf43aa60e927 fix(runtime): harden approval metadata
2026-08-24 630cf2ffdf5b9229314fe25a32a52db146e6312f feat(runtime): add resumable tool approvals
2026-08-24 72c8fae70df57beee3689854b9a8c2d10f2f2d31 test(runtime): prove missing tool approval gate
2026-08-24 3d2b40045354fbc93881c3f01469ca63055d77e0 docs(rage): design runtime tool approvals
2026-08-24 2c608e7d4d79dc76ebfcc16bf8f064174a38df3b RAGE #191: expose missing runtime approval prerequisite
2026-08-24 935bd914c1c66f261b8ebeee4b6a1b1847cb5a0a docs(rage): start issue 209 runtime approvals
2026-08-24 b739619a09287c8633391a68147ee67b63b41990 docs(rage): record and fix issue 191 whitespace gate
2026-08-24 2d827c5413fd5da534bfc55ee4e25095ce1debc2 Merge remote-tracking branch 'origin/master' into rage/191-zara1-tool-approvals
2026-08-24 47a6dcb566111ba9794fd5b23687a56eb2b047bb Merge pull request #208 from lost-rob0t/codex/theme-settings
2026-08-24 abded68049a6b86a7a5e3a2252a72185ac92d406 docs(rage): record issue 191 decision gates
2026-08-24 56a75f433d99cef7d4998b60ca524462cc188fff docs(rage): reject premature tool approval wire
2026-08-24 71b72994db30cfc04d5d7b4c5dc66a61eff0f330 feat(desktop): add themes settings and Prolog editor
2026-08-24 3b6d1ef1ac91a721c162442e5a133c3b89f00466 feat(desktop): redesign Copilot with Signal Cabin UI
2026-08-24 9d6fa5ec4aa8014bce6e347f2a8c4223e24d73a3 docs(rage): start issue 191 tool approvals
2026-08-24 a41877367f7e0af8d936e91982e88e03912dd5c2 RAGE #132: record visible STT merge evidence
2026-08-24 30b165e4b3d08aeac2ea5be0934d63cd296ebdb5 RAGE #132: restore client-visible streaming STT events
2026-08-24 99c0913e4bb0d502903416343ca7d7ea65c6180d docs(rage): close visible STT regression evidence
2026-08-24 d63bdf350e99ca5c8fc06c4e1239b8a94e7ae51e docs(rage): record visible STT pre-publication gates
2026-08-24 103de087aa74b64d7f05f4be45647d2f816bc702 docs: record local gates and coverage audit
2026-08-24 c9dd9989b34104dc8fe4e8e0c631af66c1c1a665 refactor: use canonical voice event publisher
2026-08-24 0e675a7a1b6335487657558e11b3ea69eaa38d69 test: close visible STT integration coverage
2026-08-24 3e4f796fe7f505fc2b986f6b0f2353a68a7c7e1e docs: record full-gate environment failure
2026-08-24 a50c156965854378dc1f86d067df63eddc98ce1e docs: record cancellation race evidence
2026-08-24 810da2405d0db02db472ff94331167b36b7137a6 fix: serialize visible STT cancellation
2026-08-24 c90b5383b67b76628fc16b303da4dc3f7d9fff40 docs: record visible STT red-green evidence
2026-08-24 919096d2b0a74f81d29f1098cc971a5da90fd180 fix: carry visible STT events across ZARA/1
2026-08-24 903217e07d7dc06dcb78e9757e5e936610832469 test: close visible STT protocol and principal boundaries
2026-08-24 0cb03e78d0e1a7dfc31a327a5ba29391e5e4801a docs(rage): record corrected #132 TDD red gate
2026-08-24 dd081f9ada718d6b485e36675f7bb26189378ca1 test: align client STT events with canonical runtime vocabulary
2026-08-24 26cc031e79902cc29e2c6c96caafad1a618f25f6 test: align visible STT wire spec with canonical runtime events
2026-08-24 457c127ac7d84c9be3d6ad585ee2efb1220d3f4d test: require visible STT events through ZaraClient boundary
2026-08-24 ebd803081219733e6792720c555ff82ced9ac04e test: specify visible STT ZARA/1 event codec
2026-08-24 17e89f0cc77802730770a02dca6aa39e0ff2150a test: fence in-flight STT publication against cancel
2026-08-24 bc4e411238d9392e3d647385389ae689397ecfad docs(rage): reconcile #132 regression transaction state
2026-08-24 b7328da9e937a0fbbeff44b46f7b0ec9382d89c6 fix: preserve final voice submission without observer seam
2026-08-24 f2059d0dbb91bf76a0c479d7cc40dde4f4dd4e35 feat: publish visible STT events through principal runtime bus
2026-08-24 335ed17d71b7d1b2525e1747881d3c837af6a7b7 feat: add correlated runtime STT events
2026-08-24 3160346b774ff749b3dbd66d8cb68067e3222d6c test: specify reopened #132 runtime STT visibility
2026-08-24 79b0ce18dfbbaab152905ea955632c08ada82d56 rage: design reopened #132 STT visibility repair
2026-08-24 f3dea12058fb027a4b57798bd270a9e88815ceda rage: research reopened #132 STT visibility regression
2026-08-24 db6243b5261608af143d1cb532948a4e0dd35fc3 chore: persist Zara Auto-RAGE control plane
2026-08-24 ae23557201425090c2c325a285f1486d0427bb96 rage: initialize reopened #132 STT visibility iteration
2026-08-24 0df76da7511994f097af05ab2fccb4dd98439917 docs(rage): record #134 Auto-RAGE decision gate
2026-08-24 1356c43680a3ea6313476ec89f67ad8a4e36af10 docs(rage): design blocker-aware #134 release gate
2026-08-24 05b339b9f27b620a69e3b67d53e6e3ba45a851ca docs(rage): record #134 adversarial release research
2026-08-24 8797c0f7da7fe4295979f6107d0de2e3b24ed828 docs: release #134 under Auto-RAGE
2026-08-24 c8fc5a94caf5091537d8109731cb4527b4de8fb3 docs: select Auto-RAGE control plane for #134
2026-08-23 62c2cd8029819cd5ee0fa9100a0b4de23a8ce62c docs(rage): initialize issue 134 control-plane gate
2026-08-23 b9463faf4f69bcc92c0db16941ea27ae0c252327 Merge pull request #189 from lost-rob0t/rage/133-post-merge-evidence
2026-08-23 e1912324e92e042867a608a093b5df05d062328d docs(rage): record issue 133 merge closeout
2026-08-23 487996d56467f5227c5c6b1178333fbf1ee6d8a0 Merge pull request #188 from lost-rob0t/rage/133-client-migration
2026-08-23 3e626b47de7830b5c9ffbd6d516259c0be7b66af Merge master into rage/133-client-migration
2026-08-23 517e4993a67cbfbc788e4d8cee10818b4e4766e9 docs(rage): record #133 exact-head gate protection race
2026-08-23 c9c6bc7f318f2c8abd8190919e693188e7a2472e rage: record #133 final exact-head gate
2026-08-23 3a34e642d9fd87ea51ce29d149da6553fca417b2 fix: coalesce concurrent reconnect generations
2026-08-23 cfa83fe3dbb4e8fe84eb4649dac49b6ba046c015 test: require one active reconnect generation
2026-08-23 8a7b3cef6d2b99768048866232a1651e36f9444f feat: add bounded ZaraClient reconnect controller
2026-08-23 42c1f1fce1125a08b3416a4a1a512bd2b4e2a232 docs(rage): record reconnect backoff red evidence
2026-08-23 097c42c3e5cbc14ad2149c56abc7f03ef1b03744 test: specify bounded reconnect backoff behavior
2026-08-23 d3ac8171f26fc17df3c30a25d739ec26b4a9a886 fix: replace stale ROUTER state on client reconnect
2026-08-23 c6406566ad583942a31602fe4d66aad7414ac6b0 fix: fence stale client events across reconnect generations
2026-08-23 8272d9499104581bf5eae642b252c38f284865bb test: reject stale queued events after reconnect
2026-08-23 c1d3bb0ee2f7e65e466d954df8927f1448bf84b2 fix(#133): restore selected conversation after reconnect
2026-08-23 6edc6dbb15c181ed2bd86bc813ea6eb72496da8b test(#133): require conversation continuity across reconnect
2026-08-23 c86a89735b5bb1a857f1c9e909d19f9605c4b849 RAGE #133: record CLI completion red and implementation
2026-08-23 5aca6e36fc739b52811dee40029ebfb88a92149f RAGE #133: wait for completed daemon CLI turns
2026-08-23 0312d0fcd6760ad867556401b1291a9920664fad RAGE #133: align daemon CLI boundary fixture with completion contract
2026-08-23 6554b1f19d65b1c3e44d286328b0c1b5cc83e7ef RAGE #133: record CLI selection green and completion red candidate
2026-08-23 4fe074c04ac7075754eaf6b25ef65d68ce7b8702 RAGE #133: specify completed daemon CLI turn behavior
2026-08-23 fd5ee35a023163e7cb048d8c3502315a7110b60b RAGE #133: record CLI slice red and implementation evidence
2026-08-23 972c5ec333c38f9d314ee721fd43ac8f35970215 RAGE #133: route explicit daemon text turns through ZaraClient
2026-08-23 85223a3417915cfce1ed5fbc34048ac5671ef254 docs: record #133 slice 2 green and CLI red candidate
2026-08-23 a1b4e0192c1973fd0d80c9a373bad52cdc71f7e2 test: define CLI daemon and standalone client policy
2026-08-23 8315ca127b10260aba6742da6f35c18335021faf docs: preserve RAGE #133 failed-green evidence
2026-08-23 7d6b23c91b888689ead3fe8ebd098feb2d1c3520 fix: preserve legacy desktop start call shape
2026-08-23 bca489f04a79fc18df85faf8dd43ffdef2780d5c docs: record RAGE #133 desktop red and implementation
2026-08-23 655a0e13a12d86ef3186d1dd0f45dc0b3f87e698 feat: make desktop lifecycle ZaraClient-owned
2026-08-23 d3eba985abf97aafed3ccdd4bf070fd0a5c0af92 feat: construct desktop through ZaraClient boundary
2026-08-23 d78ea92de5d7da68aa1b5074ba9672c5a948591a test: define ZaraClient-owned desktop lifecycle
2026-08-23 4c8cadad861fb091a9a5e9850fb6117772b4385b Merge PR #187: record RAGE #132 final evidence
2026-08-23 3a3af88fc601b0f6e4af1fd5e1b78f1b133398ce fix: bind Qt runtime events to supplied client subscription
2026-08-23 25fb5ad18b655f2320dddf1aa5bc8797273d970f rage: record issue 133 research design and first authoritative red
2026-08-23 6101479fc803304864af9fff4af93290a596f23d rage: record missing secure client wiring in issue 133 research
2026-08-23 e45fc3d3fd75ee0497a21db296ab1957bc05a9ca test: require Qt bridge to use supplied ZaraClient subscription
2026-08-23 e65b84890cd2910624e7b52414d74cafedd948f1 rage: derive issue 133 client migration design
2026-08-23 1e3c63761db9e64920737752b8b82b91a7e1b11d rage: research issue 133 client migration boundaries
2026-08-23 6068c2e2f0c59a47adcbf34992243ace74d5191f rage: consume issue 133 at immutable master head
2026-08-23 9b39e04122f311b4f586eea65de3b74f88571d08 docs(rage): record #132 final gate and merge evidence
2026-08-23 4c6018b30ff4be2e168551f0cf256f8333bc58af Merge PR #185: RAGE #132 live voice over ZARA/1
2026-08-23 06f23ede1120d482dfa6b28c1168adf7c335951f fix: bind voice streams to authenticated principal
2026-08-23 7e0f1e183e932627ca282d2b7a6cfcc1d95f34b5 test: prove secure voice cleanup stays principal-bound
2026-08-23 881e1d253fd5a0747e9575785b2a8859ac71b476 fix: enforce negotiated voice output format
2026-08-23 4be02d1ddb2982aa18cdde1fdff738d906400767 test: make negotiated output mismatch assertion precise
2026-08-23 f765c496ad1712c9543861a2754fb756be277278 test: include negotiated playback enforcement gate
2026-08-23 7e5ee328044eb8d14a3e140d94dea76bc7b2913c test: enforce negotiated voice output format at playback
2026-08-23 f68bf9e7551bf5dd7214728503af2aa218979aaa feat: authorize secure live voice ingress
2026-08-23 cd500b7cf8a9e855517e9495e4400639b2e5a6ec test: include secure voice authorization gate
2026-08-23 479b1eb8a9dfde53e2dc6e47fc8675b0b3066a35 test: specify secure ZARA/1 voice authorization
2026-08-23 ee787df4f00f323c306b0d9aca3a2c61b5127ca5 test(#132): negotiate output format in playback fixtures
2026-08-23 b398795ec56603e0406abe4505fa708643607d64 test(#132): negotiate output format in barge-in fixture
2026-08-23 87518639b39831da641d9c4b06873ba27dc02d53 docs(#132): record negotiation red and acceptance audit blockers
2026-08-23 d98bdc7c52b2cdd98298edff450bb70ac0c7975a docs(#132): close negotiation and secure voice design gaps
2026-08-23 8f7375d05dd552e15d7c65072ac40f8089cce05d test(#132): include output negotiation in focused voice gate
2026-08-23 d4830639ac6040fe616688225347731d17294644 feat(#132): negotiate output PCM format during handshake
2026-08-23 9121980894f078443adb54d5f48c3b8517c92efc test(#132): require output PCM handshake negotiation
2026-08-23 16f4900ba4f10580dd4b5a9d7e36f1b8c150c12e test(#132): compose live voice gate into ZARA/1 regression gate
2026-08-23 c007acbd282619f3aacf99f9fa7502fabebd50ec test(#132): add focused live voice transport gate
2026-08-23 d7b948a9ffb69529023708eea0f786c716b48f9b feat: barge in before opening new voice input
2026-08-23 f38340f340ff62dd534f80220fa7d8717e659c1f test: drain barge-in audio start after local-stop assertion
2026-08-23 b0e5de5379c395d7f162caa8becc7a9293be476d test: require proactive cross-process voice barge-in
2026-08-23 401a862a68a1c5ddadddca2e779d3b649ecbbe69 feat: serialize voice commit behind accepted PCM
2026-08-23 f6cf44231f66cfa0542df780b3df977a2279cbe0 feat: finalize streaming STT on explicit voice commit
2026-08-23 24914a445c0359053ab77cfd51230d4f81ef1a14 test: define streaming STT commit semantics
2026-08-23 d7809d839fa048af1e704c977d263f4abe206023 test: prove committed voice flushes final transcript
2026-08-23 7c13943d9bee332761aa376a00d85bdc23a749c8 feat: wire daemon voice ingress into zara-server
2026-08-23 2678606100e15770c0e9fcaa89823d7130d5a722 feat: connect daemon voice ingress to canonical runtime
2026-08-23 6201d4de619cc8f21b91c023c92fa0c7140b75d8 test: prove daemon voice ingress reaches canonical runtime
2026-08-23 6ee6ed4bb2f026b153d2ffb15f9032d01b0b4f2c fix: stop cancelled turn playback and drop stale audio
2026-08-23 acfea1af39ed49508822c6ed653c2c4dce652902 test: prove cancelled turns stop playback and drop stale audio
2026-08-23 9442b8804ddb6f046e661db62aefb71d9f0414a3 feat: hand binary voice output to client playback boundary
2026-08-23 5bbc37e8615f6305489d18af84a0f25666c9d4d6 docs: record voice output RAGE evidence
2026-08-23 bdd9cb210a7e6db063f28fa276b3e3f1507a81c5 test: define client-owned voice output handoff
2026-08-23 c88e72642c9122fed73ece6057a64a307ee65871 feat: validate ZARA/1 audio output framing
2026-08-23 000347da1f02b5af1afc8392602412e628a5da4d test: define ZARA/1 audio output framing contract
2026-08-23 8e6176306168f3874320e7833fa3fd20f2c55638 rage: record #132 client audio green gate
2026-08-23 959c4c45eaffe02a8496831d606454ab31e3ed8b feat: add ZaraClient binary audio input transport
2026-08-23 8e0e3f6cb2763fb145a39a3b6411f055f06afe59 rage: record #132 ZaraClient audio red evidence
2026-08-23 bf6f12d9efa84e6b9715e26b44081d92068051ae test: define ZaraClient voice input framing contract
2026-08-23 236335dfaf3390bd5b91dcaef04bd63f3fd1528c fix: contain terminal voice ingress failures
2026-08-23 6212e914c3fa882059ccedbffbad0350a72e6ad1 test: prove voice terminal ingress failures are contained
2026-08-23 7f8bc0a956c0b0c9210593a41173d0d81a8d1b8e docs: record degraded voice ingress RAGE evidence
2026-08-23 4ad166bb5476aa8071b1d6689fe93488568b1c77 fix: contain voice ingress adapter failures
2026-08-23 1f5b662162a08c6276c304273cf3bfe7baf24cdb test: prove voice ingress failures stay route-local
2026-08-23 9f00a48ccc5128c92758f6db8798161e14480f48 fix: return explicit voice ingress backpressure
2026-08-23 83f64a6f3d8a510e1c80b3c4e0b9706067dabca3 test: define bounded voice ingress backpressure
2026-08-23 cd5919ee1073ea2692bf396dd9e46939b9501833 fix: preserve secure route quota across hello reset
2026-08-23 49f203f62d4d55c8253eb999704a7855aa810607 fix: bind and clean up voice stream context
2026-08-23 59e5e01804d0cdcc9cef4a23e279fc436fda43d7 test: define voice stream cleanup and correlation contract
2026-08-23 1d44d47f2d80d90e8b5a03202904ab928a229854 docs: record cancellation failed-green regression
2026-08-23 53827ddc81166c8a1340e3e20a9e391843eda6ee fix: preserve strict ZARA token validation
2026-08-23 63bcd26dea378d4013e301a11aa50c0aaf1a9209 docs: record cancellation red and implementation
2026-08-23 2139d527420f7a85d90c2aaf5caff7d6cd0f5900 feat: cancel live audio input streams
2026-08-23 366699391b18ce6d7a82e1945d126112d4bcb5f1 feat: acknowledge cancelled audio input streams
2026-08-23 7c18bcbbb47984500baa38e214db20cbf489bc19 docs: record slice 3 green and slice 4 red candidate
2026-08-23 850e969c1ad22872cbfe852f322131a48cf3d7bf test: define audio input cancellation lifecycle
2026-08-23 b789d6261a9cf7665d7475a675b45991b3736a7f docs: record slice 3 red proof and ingress implementation
2026-08-23 063c5e3ace9fd33524bb99363f0fba73e1846eab feat: hand validated voice frames to injected ingress
2026-08-23 77c4cce00bf6c60e4d2ef73eb32a2ed1b65615d9 docs: record slice 2 green and slice 3 red candidate
2026-08-23 19b0278ae1a7ed3bd4497708cf12c75983218687 test: define bounded voice ingress handoff contract
2026-08-22 7420e66aa6417b7e0ccda63e69c18b3fd7d487e4 docs: record #132 slice 2 failed green evidence
2026-08-22 efb5e771c1ca9efde7cb6ddde1b0fd0c4be6ad00 fix: register audio input lifecycle acknowledgements
2026-08-22 7a116a0151fca26bfc0d49d05b7e9b779bf3b824 RAGE #132: record gateway lifecycle red evidence
2026-08-22 b11fafb128f34de277525eee9e127f52bb2d84a2 RAGE #132: implement route-scoped audio input lifecycle
2026-08-22 275c63de47b1e0b590fe79c65b2900514335af3c docs: record voice gateway TDD boundary
2026-08-22 6734794d04a024b1c0881c8b228411104c78a5f1 test: define voice stream lifecycle at gateway
2026-08-22 003484c74e0491d2a314d43c7981d37a01427fe3 docs: reconcile #132 with daemon voice research baseline
2026-08-22 fb27b3496ae5edb021f87e65b8a049da6f3dfff8 feat: enforce ZARA/1 baseline input audio contract
2026-08-22 1fe1c16b1e33586bb3f113095efd2dd8b8e7d36c test: align reserved audio fixtures with #132 contract
2026-08-22 614c9844ecda3fc55005893670c59bb5c302447e RAGE #132: record research design and first red candidate
2026-08-22 df1f8762dc2b7d9962fcbf12e832753d85b5c6a7 RAGE #132: add failing audio protocol contract tests
2026-08-22 c530780c6a90d54efcb5eb0b8c0b5721ada87ae9 RAGE #132: derive live voice transport design
2026-08-22 2651db04e11466362d36d3e23f36b2b17fb38a64 RAGE #132: record adversarial voice transport research
2026-08-22 d82763e124614f45fb7122dbb7e917cb1e0d8c8f RAGE #132: record immutable start
2026-08-22 d645973a299c92b7126f9a8f70191294af80e145 docs(rage): record #131 merge outcome
2026-08-22 1a076e9921228d9d0eb18ea63225a1862f81023d Merge PR #148: RAGE #131 principal isolation
2026-08-22 bf9e35d677a159e193389371ffc57af6323a9b57 docs: record final principal-context TDD evidence
2026-08-22 4880f2adb2b66265b70d860c64378c4f7d804d6e fix: thread principal into live conversation context
2026-08-22 981ae77113c09f3712a565acbd13dd2f4b8e1f31 fix: bind live conversation context to principal
2026-08-22 46a8330f453def30f060af9dc4fb9bfa283dc684 test: prove daemon conversation context is principal-bound
2026-08-22 0420d98da746d6efbdd848b13c6907843fae95c5 fix(#131): enforce canonical transient memory ownership
2026-08-22 ca4568c702f9ce13dc6d029eec179979ed842941 test(#131): reject shaped principal objects at memory boundary
2026-08-22 6d4a3ebacc062496ff5ff871d02eddc4c4dd4861 test(#131): stop barrier harness from masking serialized migration
2026-08-22 d7dd6225b29e6b407ef268215c33d499cea5c7f9 test(#131): require ephemeral principals to remain non-durable
2026-08-22 e1a5937aff8cc79bf26f27973efbb42e2658c200 fix(#131): serialize principal schema upgrades
2026-08-22 0203c5296017bd0a2ad9835865cb0b58401867f2 fix(#131): allow immediate SQLite transactions for schema serialization
2026-08-22 4958a307e52942c15c381688d64d10887393da90 test(#131): use RuntimeEventSubscription timeout contract
2026-08-22 7c6262c866b45f6be6aa086830e29016a730479f test: include daemon principal wiring in isolation gate
2026-08-22 a182b7163f769fdbe27229f55f5cf91b622e2fa2 test: reproduce concurrent principal schema migration race
2026-08-22 a59481a43b6a7eab1216595f2f64cc2bbf96db4e docs(rage): record runtime wiring red-green evidence
2026-08-22 fa098b2e52c48e69edf95ef8ebc24ef31c0da20d test: unwrap runtime event envelopes in principal isolation gate
2026-08-22 3a7b307f72016e01ca8869a40e6ed79c9edccc59 fix: thread principal into daemon runtime backend
2026-08-22 b414076c675f283054348f78db5f1aec84793ab9 fix: bind agent memory to principal
2026-08-22 50e26ab780b7395c7b453927acfd1a59b5a726fb test: require principal on default daemon private state path
2026-08-22 9a8342212a11d39a69c4a52823f97ecfdec1c572 test: preserve runtime event boundary in isolation fake
2026-08-22 9e665fd9a9907d4cf455cc54b7565ff244ba6db2 docs(rage): append issue 131 review evidence
2026-08-22 82cfccbeeb5caa55e5ef375351ce5ae05f09203c test: add principal isolation focused gate
2026-08-22 c94024e77750fb6466a462979dacbd7aec4b1bcd test: add red runtime principal isolation matrix
2026-08-22 7a07d78d091583f681869004acead96f0dc1d078 feat(memory): bind memory state to principal
2026-08-22 0e68d2636dca17c66e2d01848e9868a7d787510c feat: bind conversation compatibility store to principal
2026-08-22 f40b803071e0a898f3cee903071541e0ed245382 feat: scope conversations to authenticated principal
2026-08-22 6fbd268b068a15d7c77ce2502322f84b33e0f699 docs(rage): record issue 131 red evidence
2026-08-22 1cbfe6b53833e70e4a418a0854080fb1cfa6a188 test: define principal-scoped memory isolation
2026-08-22 28ce6a0ae47eca4812429fbbd4867c15c3225321 test: define principal-scoped conversation persistence
2026-08-22 3dd4ba2ac44c517c943d21384c45912be94d9741 docs(rage): design issue 131 principal isolation
2026-08-22 47244f37b3777624fbb79abd91214698b53110e4 docs(rage): research issue 131 principal isolation
2026-08-22 6d37e2be29859542bfaacdcd174892ddf7519290 docs(rage): start issue 131 isolation iteration
2026-08-22 f3a2430962feab29505d3639ced5c45e26639fe5 docs(rage): record issue 130 final gate and merge
2026-08-22 71615bcd4cdece940db433cb79ea46fe9ad085e3 feat: secure Zara daemon with CURVE/ZAP and abuse controls (#145)
2026-08-22 fdf6f9a1d4e51a03ab4f46b1f291cf262e416020 fix: fail closed on unmapped daemon capabilities
2026-08-22 d14980f57cab66b674591e5271202cdbb9c49cd4 test: require fail-closed daemon capability mapping
2026-08-22 02dcea04ff55fe0742f0d52a97dea1cf6fc6aa26 fix(security): rate-limit malformed authenticated requests
2026-08-22 8bdcc6781c46d5ff6c6e9235b6c7337ee0f43c96 test(security): cover malformed abuse and server pinning
2026-08-22 efe9afa55e7a1be57d3f24ec242bd59d3853f065 docs(rage): record CI 323 synchronization failure
2026-08-22 76dd48f2e2cd75f8e391f63b548b6a20a1c0833d test(security): synchronize concurrent quota dispatch
2026-08-22 dc72c3d96535b2184496cfe441487ff735deebd9 docs(rage): record slice C integration red gate
2026-08-22 57b590002a9cef5302dfec3ad790f9650ee08392 fix(security): enforce gateway request quotas and audit
2026-08-22 8f32effdd1f8f20157b8f2d10addcf9c0c5fc155 test(security): define hostile multi-client quota and audit matrix
2026-08-22 754af1716807ad3f94c072650ceaf99627ecd19b fix(security): accept PyZMQ Z85 callback credentials
2026-08-22 e51e4b21927e995bd38bc443d4e425464062adc6 feat(security): add CURVE ZAP authenticated gateway
2026-08-22 d9fe1954791834580bfd67b52d038cbe191f9a6b fix(security): run registry ZAP authenticator in owned thread
2026-08-22 987a0da375b3ffa2a2343af3eaee9e6d13532e4c docs(rage): record refined slice C red gate
2026-08-22 64891356d73b9e8bb2d9347ee4bda2302c5c232a test(security): target explicit secure gateway boundary
2026-08-22 af0629edd879f6039650631eb6192630482cffbd docs(rage): record slice C red and secure gateway boundary
2026-08-22 2096ba40c744da7e1143ed84d9b1cc2c90157ce4 test(security): establish authenticated gateway red gate
2026-08-22 c59900784f16bf3c8894ac39fa04cfe957ee1c46 docs(rage): record slice B green checkpoint
2026-08-22 0277c380451964b377b45d270114d8524cb5b032 test(security): assert supported CURVE socket contract
2026-08-22 b20060cf2b82394f5cd94b1a2970eb95e22017f3 fix(security): use supported PyZMQ CURVE socket properties
2026-08-22 e8363828c416418f7c6278fae32bb18a3c2f65c4 feat(security): add registry-backed CURVE transport primitives
2026-08-22 32e5d3d3098351337c0dd767c9f13f7fa1a4cbcf docs(rage): record slice B transport security red gate
2026-08-22 b22461a05699dc9563d267575f5480fa54211bbd test(security): define CURVE/ZAP transport plumbing red gate
```

## Repository paths changed, last 14 days

```text
.github/workflows/ci.yml
.github/workflows/rage-159-apply.yml
.impeccable/design.json
.impeccable/surfaces/zara-desktop-windows-quick-py.md
.rage.toml
AGENTS.md
DESIGN.md
PRODUCT.md
README.org
android/.gitignore
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
android/app/src/main/java/ai/zara/app/assistant/AssistantRoleController.kt
android/app/src/main/java/ai/zara/app/assistant/AssistantVoiceSessionBridge.kt
android/app/src/main/java/ai/zara/app/assistant/ZaraVoiceInteractionService.kt
android/app/src/main/java/ai/zara/app/assistant/ZaraVoiceInteractionSession.kt
android/app/src/main/java/ai/zara/app/assistant/ZaraVoiceInteractionSessionService.kt
android/app/src/main/java/ai/zara/app/auth/AndroidCredentialCipher.kt
android/app/src/main/java/ai/zara/app/auth/AuthCore.kt
android/app/src/main/java/ai/zara/app/auth/EnrollmentRepository.kt
android/app/src/main/java/ai/zara/app/auth/JeroMqAuth.kt
android/app/src/main/java/ai/zara/app/prolog/NativeTreallaBridge.kt
android/app/src/main/java/ai/zara/app/prolog/PortableSemanticAssetStager.kt
android/app/src/main/java/ai/zara/app/prolog/PortableSemanticCore.kt
android/app/src/main/java/ai/zara/app/prolog/SemanticFixtureRunner.kt
android/app/src/main/java/ai/zara/app/prolog/SemanticResultComparator.kt
android/app/src/main/java/ai/zara/app/prolog/TreallaSemanticRuntime.kt
android/app/src/main/java/ai/zara/app/runtime/AndroidTextSessionController.kt
android/app/src/main/java/ai/zara/app/runtime/ClientStateStore.kt
android/app/src/main/java/ai/zara/app/runtime/EnrollmentProjection.kt
android/app/src/main/java/ai/zara/app/runtime/JeroMqTextDealer.kt
android/app/src/main/java/ai/zara/app/runtime/RequestCorrelations.kt
android/app/src/main/java/ai/zara/app/runtime/RuntimeState.kt
android/app/src/main/java/ai/zara/app/runtime/ServerProfile.kt
android/app/src/main/java/ai/zara/app/runtime/ZaraCapabilityCodec.kt
android/app/src/main/java/ai/zara/app/runtime/ZaraTextClientActor.kt
android/app/src/main/java/ai/zara/app/runtime/ZaraTextCodec.kt
android/app/src/main/java/ai/zara/app/runtime/ZaraVoiceHelloCodec.kt
android/app/src/main/java/ai/zara/app/ui/AssistantSetupGuidance.kt
android/app/src/main/java/ai/zara/app/ui/ZaraApp.kt
android/app/src/main/java/ai/zara/app/voice/AndroidPcmOutput.kt
android/app/src/main/java/ai/zara/app/voice/AndroidPcmRecorder.kt
android/app/src/main/java/ai/zara/app/voice/AuthenticatedVoiceIngress.kt
android/app/src/main/java/ai/zara/app/voice/ManualVoiceCapture.kt
android/app/src/main/java/ai/zara/app/voice/ManualVoiceSessionCoordinator.kt
android/app/src/main/java/ai/zara/app/voice/PushToTalkController.kt
android/app/src/main/java/ai/zara/app/voice/VoicePlaybackController.kt
android/app/src/main/java/ai/zara/app/voice/VoiceStreamReducer.kt
android/app/src/main/java/ai/zara/app/voice/VoiceStreamSinkActor.kt
android/app/src/main/java/ai/zara/app/voice/ZaraVoiceAckCodec.kt
android/app/src/main/java/ai/zara/app/voice/ZaraVoiceCodec.kt
android/app/src/main/java/ai/zara/app/voice/ZaraVoiceInboundCodec.kt
android/app/src/main/java/ai/zara/app/voice/ZaraVoiceStreamCodec.kt
android/app/src/main/res/xml/voice_interaction_service.xml
android/app/src/test/java/ai/zara/app/BuildMetadataTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantInvocationGateTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantRoleControllerTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantServiceManifestContractTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantVoiceSessionBridgeTest.kt
android/app/src/test/java/ai/zara/app/auth/AuthenticationTest.kt
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
android/app/src/test/java/ai/zara/app/runtime/AndroidTextSessionControllerTest.kt
android/app/src/test/java/ai/zara/app/runtime/AndroidTextSessionObserverTest.kt
android/app/src/test/java/ai/zara/app/runtime/ClientStateStoreTest.kt
android/app/src/test/java/ai/zara/app/runtime/EnrollmentProjectionTest.kt
android/app/src/test/java/ai/zara/app/runtime/RequestCorrelationTest.kt
android/app/src/test/java/ai/zara/app/runtime/RuntimeStateTest.kt
android/app/src/test/java/ai/zara/app/runtime/ServerProfileTest.kt
android/app/src/test/java/ai/zara/app/runtime/StockZaraServerInteropTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientActorTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientVoiceFloodTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientVoiceNegotiationTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientVoicePumpTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientVoiceTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextCodecTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextTurnOrderingTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraVoiceNegotiationTest.kt
android/app/src/test/java/ai/zara/app/ui/ZaraAppProjectionTest.kt
android/app/src/test/java/ai/zara/app/voice/AuthenticatedVoiceIngressTest.kt
android/app/src/test/java/ai/zara/app/voice/ManualVoiceCaptureTest.kt
android/app/src/test/java/ai/zara/app/voice/ManualVoiceSessionCoordinatorTest.kt
android/app/src/test/java/ai/zara/app/voice/PushToTalkControllerTest.kt
android/app/src/test/java/ai/zara/app/voice/VoicePlaybackControllerTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamBargeInTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamReducerTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamSinkActorTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceAckCodecTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceCodecTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceInboundCodecTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceStreamCodecTest.kt
android/build-trealla.sh
android/build.gradle.kts
android/flake.lock
android/flake.nix
android/gradle.properties
android/gradle/libs.versions.toml
android/integration/stock_zara_server_fixture.py
android/patch-trealla-module-path.sh
android/settings.gradle.kts
docs/README.org
docs/STT.md
docs/architecture.org
docs/desktop-copilot-design.md
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
rage/131-principal-isolation-design.org
rage/131-principal-isolation-merge-closeout.org
rage/131-principal-isolation-research.org
rage/131-principal-isolation.org
rage/132-live-voice-design.org
rage/132-live-voice-research.org
rage/132-live-voice.org
rage/132-post-merge-evidence.org
rage/132-visible-stt-regression-design.org
rage/132-visible-stt-regression-research.org
rage/132-visible-stt-regression.org
rage/133-client-migration-design.org
rage/133-client-migration-final-gate.org
rage/133-client-migration-research.org
rage/133-client-migration.org
rage/133-daemon-default-regression.org
rage/133-desktop-daemon-default-regression.org
rage/133-post-merge-evidence.org
rage/134-daemon-release-design.org
rage/134-daemon-release-gate.org
rage/134-daemon-release-research.org
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
rage/175-android-barge-in.org
rage/175-android-manual-voice.org
rage/175-android-streamed-voice.org
rage/191-zara1-tool-approvals-2-design.org
rage/191-zara1-tool-approvals-2-research.org
rage/191-zara1-tool-approvals-2.org
rage/191-zara1-tool-approvals-design.org
rage/191-zara1-tool-approvals-research.org
rage/191-zara1-tool-approvals.org
rage/195-samsung-assistant-research.org
rage/196-android-assistant-role.org
rage/196-ui-closed-runtime.org
rage/197-compose-first-usable.org
rage/209-runtime-tool-approvals-design.org
rage/209-runtime-tool-approvals-research.org
rage/209-runtime-tool-approvals.org
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
rage/29-streaming-tts-recovery-r7.org
rage/309-prolog-config-recovery-design.org
rage/309-prolog-config-recovery-research.org
rage/309-prolog-config-recovery.org
rage/315-route-backpressure-test-contract.org
rage/326-desktop-toggle.org
rage/327-bounded-target-edit-distance-recovery.org
rage/329-production-secure-listener.org
rage/329-threat-model.org
rage/348-dash-prefixed-z85-cli.org
rage/371-plugin-approval-contract.org
rage/5-config-durability.org
rage/daemon-130-security.org
rage/long-horizon-tasks.org
scripts/benchmark-voice.py
scripts/import-backlog.py
scripts/rage-159-apply.py
scripts/security-fuzz-soak.sh
scripts/test-all.sh
scripts/test-android-semantic-parity.sh
scripts/test-android.sh
scripts/test-api-service.sh
scripts/test-capability-plans.sh
scripts/test-command-routing.sh
scripts/test-hooks.sh
scripts/test-openrouter-live.sh
scripts/test-principal-isolation.sh
scripts/test-process-safety.sh
scripts/test-prolog-command-advice.sh
scripts/test-prolog-config.sh
scripts/test-prolog-rlm-live.sh
scripts/test-replies.sh
scripts/test-rlm-rewrite.sh
scripts/test-runtime-tool-approvals.sh
scripts/test-streaming-llm.sh
scripts/test-streaming-tts.sh
scripts/test-user-command-authoring.sh
scripts/test-user-command-compiler.sh
scripts/test-user-command-persistence.sh
scripts/test-zara1-device-actions.sh
scripts/test-zara1-protocol.sh
scripts/test-zara1-tool-approvals.sh
scripts/test-zara1-voice.sh
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
t/test_agent_hooks.py
t/test_agent_loop_advice_integration.py
t/test_agent_loop_backend_registry.py
t/test_agent_mode_core_plugin.py
t/test_agent_mode_voice_barge_in.py
t/test_api_service.py
t/test_backend_turn_services.py
t/test_backlog_import.py
t/test_capability_plans.py
t/test_clarification_session.py
t/test_cli_client_migration.py
t/test_client.py
t/test_command_routing.py
t/test_config.py
t/test_conversation_flow.py
t/test_conversation_service.py
t/test_customization_diagnostics.py
t/test_daemon_intent_router.py
t/test_daemon_security_abuse.py
t/test_daemon_security_gateway.py
t/test_daemon_security_policy.py
t/test_daemon_security_transport.py
t/test_daemon_tts_output.py
t/test_database_fetch_locking.py
t/test_desktop_control.py
t/test_desktop_launch_surface.py
t/test_desktop_preferences.py
t/test_desktop_settings_window.py
t/test_desktop_shell.py
t/test_desktop_theme.py
t/test_desktop_toggle_control.py
t/test_dialogue_script.py
t/test_full_chat.py
t/test_hooks_config.py
t/test_host_api_service.py
t/test_json_limits.py
t/test_latency_metrics.py
t/test_llm.py
t/test_llm_streaming.py
t/test_memory.py
t/test_plan_executor.py
t/test_plans.py
t/test_plugin_tool_approval.py
t/test_principal_conversation_isolation.py
t/test_principal_memory_isolation.py
t/test_principal_runtime_isolation.py
t/test_principal_runtime_wiring.py
t/test_production_secure_listener.py
t/test_prolog_frame_adapter.py
t/test_prolog_studio.py
t/test_protocol.py
t/test_protocol_runtime.py
t/test_qt_runtime_bridge.py
t/test_quick_copilot.py
t/test_quick_handoff_edges.py
t/test_registered_target_recovery.py
t/test_runtime_backend_publisher.py
t/test_runtime_host.py
t/test_runtime_host_clarification.py
t/test_runtime_intent_routing.py
t/test_runtime_tool_approval.py
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
t/test_sentence_chunker.py
t/test_server.py
t/test_service_plugin_advice.py
t/test_streaming_stt_commit.py
t/test_task_approval_flow.py
t/test_task_host_wiring.py
t/test_task_observability.py
t/test_task_runner.py
t/test_task_store.py
t/test_task_tools.py
t/test_task_turn_context.py
t/test_tasks_config.py
t/test_todo_surface_toggle.py
t/test_tts.py
t/test_tts_output_lifecycle.py
t/test_user_command_authoring.py
t/test_user_command_authoring_acceptance.py
t/test_user_command_compiler.py
t/test_user_command_persistence.py
t/test_user_command_runtime.py
t/test_user_python_hooks.py
t/test_visible_stt_runtime.py
t/test_voice_output_protocol.py
t/test_voice_protocol.py
t/test_voice_runtime_commit.py
t/test_voice_runtime_ingress.py
t/test_voice_secure_gateway.py
t/test_voice_zmq_backpressure.py
t/test_voice_zmq_barge_in.py
t/test_voice_zmq_cancel.py
t/test_voice_zmq_cleanup.py
t/test_voice_zmq_client.py
t/test_voice_zmq_negotiation.py
t/test_voice_zmq_output_client.py
t/test_voice_zmq_output_negotiation.py
t/test_voice_zmq_transport.py
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
t/test_zara1_tool_approvals.py
t/test_zara_hooks_registry.py
t/test_zmq_transport.py
t/test_zmq_transport_reconnect_backoff.py
t/test_zmq_transport_reconnect_idempotency.py
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
wiki/tool-approvals.org
zara/__main__.py
zara/agent/__init__.py
zara/agent/approval.py
zara/agent/conversation.py
zara/agent/graph.py
zara/agent/hooks.py
zara/agent/loops.py
zara/agent/prompting.py
zara/agent/sentence_chunker.py
zara/agent/stream_events.py
zara/agent/tools/builtin_tools.py
zara/agent/tools/registry.py
zara/agent/user_hooks.py
zara/client.py
zara/command_gate.py
zara/config.py
zara/console.py
zara/database.py
zara/desktop/app.py
zara/desktop/chat_widgets.py
zara/desktop/control.py
zara/desktop/controller.py
zara/desktop/conversation/__init__.py
zara/desktop/conversation/store.py
zara/desktop/preferences.py
zara/desktop/prolog_studio.py
zara/desktop/qt_bridge.py
zara/desktop/theme.py
zara/desktop/tray/tray.py
zara/desktop/windows/__init__.py
zara/desktop/windows/chat.py
zara/desktop/windows/quick.py
zara/desktop/windows/settings.py
zara/desktop/windows/status.py
zara/json_limits.py
zara/latency.py
zara/llm.py
zara/memory.py
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
zara/security.py
zara/security_admin.py
zara/security_gateway.py
zara/security_state.py
zara/security_transport.py
zara/server.py
zara/server_core.py
zara/speech_activity.py
zara/streaming_stt.py
zara/tasks/__init__.py
zara/tasks/runner.py
zara/tasks/store.py
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
android/app/src/test/java/ai/zara/app/BuildMetadataTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantInvocationGateTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantRoleControllerTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantServiceManifestContractTest.kt
android/app/src/test/java/ai/zara/app/assistant/AssistantVoiceSessionBridgeTest.kt
android/app/src/test/java/ai/zara/app/auth/AuthenticationTest.kt
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
android/app/src/test/java/ai/zara/app/runtime/AndroidTextSessionControllerTest.kt
android/app/src/test/java/ai/zara/app/runtime/AndroidTextSessionObserverTest.kt
android/app/src/test/java/ai/zara/app/runtime/ClientStateStoreTest.kt
android/app/src/test/java/ai/zara/app/runtime/EnrollmentProjectionTest.kt
android/app/src/test/java/ai/zara/app/runtime/RequestCorrelationTest.kt
android/app/src/test/java/ai/zara/app/runtime/RuntimeStateTest.kt
android/app/src/test/java/ai/zara/app/runtime/ServerProfileTest.kt
android/app/src/test/java/ai/zara/app/runtime/StockZaraServerInteropTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientActorTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientVoiceFloodTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientVoiceNegotiationTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientVoicePumpTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientVoiceTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextCodecTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextTurnOrderingTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraVoiceNegotiationTest.kt
android/app/src/test/java/ai/zara/app/ui/ZaraAppProjectionTest.kt
android/app/src/test/java/ai/zara/app/voice/AuthenticatedVoiceIngressTest.kt
android/app/src/test/java/ai/zara/app/voice/ManualVoiceCaptureTest.kt
android/app/src/test/java/ai/zara/app/voice/ManualVoiceSessionCoordinatorTest.kt
android/app/src/test/java/ai/zara/app/voice/PushToTalkControllerTest.kt
android/app/src/test/java/ai/zara/app/voice/VoicePlaybackControllerTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamBargeInTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamReducerTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamSinkActorTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceAckCodecTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceCodecTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceInboundCodecTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceStreamCodecTest.kt
android/flake.nix
flake.nix
scripts/benchmark-voice.py
scripts/import-backlog.py
scripts/rage-159-apply.py
scripts/security-fuzz-soak.sh
scripts/test-all.sh
scripts/test-android-semantic-parity.sh
scripts/test-android.sh
scripts/test-api-service.sh
scripts/test-capability-plans.sh
scripts/test-command-routing.sh
scripts/test-hooks.sh
scripts/test-openrouter-live.sh
scripts/test-principal-isolation.sh
scripts/test-process-safety.sh
scripts/test-prolog-command-advice.sh
scripts/test-prolog-config.sh
scripts/test-prolog-rlm-live.sh
scripts/test-replies.sh
scripts/test-rlm-rewrite.sh
scripts/test-runtime-tool-approvals.sh
scripts/test-streaming-llm.sh
scripts/test-streaming-tts.sh
scripts/test-user-command-authoring.sh
scripts/test-user-command-compiler.sh
scripts/test-user-command-persistence.sh
scripts/test-zara1-device-actions.sh
scripts/test-zara1-protocol.sh
scripts/test-zara1-tool-approvals.sh
scripts/test-zara1-voice.sh
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
t/test_agent_hooks.py
t/test_agent_loop_advice_integration.py
t/test_agent_loop_backend_registry.py
t/test_agent_mode_core_plugin.py
t/test_agent_mode_voice_barge_in.py
t/test_api_service.py
t/test_backend_turn_services.py
t/test_backlog_import.py
t/test_capability_plans.py
t/test_clarification_session.py
t/test_cli_client_migration.py
t/test_client.py
t/test_command_routing.py
t/test_config.py
t/test_conversation_flow.py
t/test_conversation_service.py
t/test_customization_diagnostics.py
t/test_daemon_intent_router.py
t/test_daemon_security_abuse.py
t/test_daemon_security_gateway.py
t/test_daemon_security_policy.py
t/test_daemon_security_transport.py
t/test_daemon_tts_output.py
t/test_database_fetch_locking.py
t/test_desktop_control.py
t/test_desktop_launch_surface.py
t/test_desktop_preferences.py
t/test_desktop_settings_window.py
t/test_desktop_shell.py
t/test_desktop_theme.py
t/test_desktop_toggle_control.py
t/test_dialogue_script.py
t/test_full_chat.py
t/test_hooks_config.py
t/test_host_api_service.py
t/test_json_limits.py
t/test_latency_metrics.py
t/test_llm.py
t/test_llm_streaming.py
t/test_memory.py
t/test_plan_executor.py
t/test_plans.py
t/test_plugin_tool_approval.py
t/test_principal_conversation_isolation.py
t/test_principal_memory_isolation.py
t/test_principal_runtime_isolation.py
t/test_principal_runtime_wiring.py
t/test_production_secure_listener.py
t/test_prolog_frame_adapter.py
t/test_prolog_studio.py
t/test_protocol.py
t/test_protocol_runtime.py
t/test_qt_runtime_bridge.py
t/test_quick_copilot.py
t/test_quick_handoff_edges.py
t/test_registered_target_recovery.py
t/test_runtime_backend_publisher.py
t/test_runtime_host.py
t/test_runtime_host_clarification.py
t/test_runtime_intent_routing.py
t/test_runtime_tool_approval.py
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
t/test_sentence_chunker.py
t/test_server.py
t/test_service_plugin_advice.py
t/test_streaming_stt_commit.py
t/test_task_approval_flow.py
t/test_task_host_wiring.py
t/test_task_observability.py
t/test_task_runner.py
t/test_task_store.py
t/test_task_tools.py
t/test_task_turn_context.py
t/test_tasks_config.py
t/test_todo_surface_toggle.py
t/test_tts.py
t/test_tts_output_lifecycle.py
t/test_user_command_authoring.py
t/test_user_command_authoring_acceptance.py
t/test_user_command_compiler.py
t/test_user_command_persistence.py
t/test_user_command_runtime.py
t/test_user_python_hooks.py
t/test_visible_stt_runtime.py
t/test_voice_output_protocol.py
t/test_voice_protocol.py
t/test_voice_runtime_commit.py
t/test_voice_runtime_ingress.py
t/test_voice_secure_gateway.py
t/test_voice_zmq_backpressure.py
t/test_voice_zmq_barge_in.py
t/test_voice_zmq_cancel.py
t/test_voice_zmq_cleanup.py
t/test_voice_zmq_client.py
t/test_voice_zmq_negotiation.py
t/test_voice_zmq_output_client.py
t/test_voice_zmq_output_negotiation.py
t/test_voice_zmq_transport.py
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
t/test_zara1_tool_approvals.py
t/test_zara_hooks_registry.py
t/test_zmq_transport.py
t/test_zmq_transport_reconnect_backoff.py
t/test_zmq_transport_reconnect_idempotency.py
t/test_zmq_transport_route_backpressure.py
t/zara_hooks_registry.pl
```
