# lost-rob0t/zara

- generated: `2026-09-19T12:31:41Z`
- canonical branch: `master`
- changelog eligible: `yes`
- head: [`02308958a4265d8aa670f1870c3c04dfb0fb7411`](https://github.com/lost-rob0t/zara/commit/02308958a4265d8aa670f1870c3c04dfb0fb7411)
- head date: `2026-09-19T08:11:40-04:00`
- head subject: Merge pull request #1209 from lost-rob0t/fix/1046-runtime-refresh-noop-generation

## Git log, last 14 days

```text
2026-09-19 02308958a4265d8aa670f1870c3c04dfb0fb7411 Merge pull request #1209 from lost-rob0t/fix/1046-runtime-refresh-noop-generation
2026-09-19 9188f407a1978620688e3943394e30545b12b406 chore(runtime): drop unrelated Android acceptance drift
2026-09-19 0cc85e6a13be3f62047518ff4a33bb13e6c253c1 Merge master into fix/1046-runtime-refresh-noop-generation
2026-09-19 9aa86f19014833e795177c998d95305582a94d02 Merge pull request #1154 from lost-rob0t/fix/android-local-ai-close-fence-20260919
2026-09-19 5a8589de8d3165d47042f29b38f9c0eba68b50ca test(android): pin repeated local-ai close teardown fence
2026-09-19 e659be5859edb7a0d722da394db5cbe1fbf6d915 fix(local-ai): avoid actor-thread shutdown deadlock
2026-09-19 5b432ed4a1add1a86a66e62ce47cf5384fb2610e test(local-ai): reproduce actor-thread close deadlock
2026-09-19 f0cd912b99d01ecbfd065c1862513ff0dbd34bbf fix(ci): clear launcher ANR before release-note evidence
2026-09-19 42bf865705ab03126beee1677710bbcde2974151 test(android): target release-note overlay ordering precisely
2026-09-19 0e8e7836cfc2aae73be4cde62db68c4f8d0d3909 test(android): pin system-overlay recovery before release notes
2026-09-19 33a0d09e1286f082a39ccecd648e0429306ed42a docs(changelog): record local shutdown stale-callback fence
2026-09-19 0d80b8e53ffe86010ca0cbe1bbd5ec1bccb69a3b fix(android): simplify atomic local shutdown fence
2026-09-19 1ed390c3debf82be4e3f851c8b16ab4fe1f3a4f4 fix(android): atomically fence local runtime shutdown
2026-09-19 3cbe3a121dfe45f15b93d0aa5f12418197ab12e9 docs(changelog): record local AI shutdown fence
2026-09-19 2d3b788a468f789114808c76101e4d8627fcc33e test(android): fence stale local callbacks after close
2026-09-19 334990f7684cbf49d39f94a70f310fe2bbccc014 fix(android): fence local AI work when shutdown starts
2026-09-19 dc248a2d72814f599a0d038e1d978e58233e6c8d docs(runtime): define no-op discovery refresh semantics
2026-09-19 589e72d9a9597cd76be4fa1ff1ea7f5ba286a1a7 fix(runtime): preserve Android generation across identical discovery polls
2026-09-19 1157989fc73b47ae82bd4bc3185550884a742aed fix(runtime): keep generation stable across identical discovery polls
2026-09-19 cb623a140778d0c321420ac78c6a0a1a7c2153d3 test(runtime): mirror no-op discovery generation semantics on Android
2026-09-19 8d531c3ed7b1f2db20f8872788569e8c3c6c4aab test(runtime): pin no-op discovery generation semantics
2026-09-19 91d2b2d72366cad18076c1171f67e96b05b183ed Merge pull request #1055 from lost-rob0t/feat/emacs-package-symbol-registry-1054
2026-09-19 b981d0abe801ecd6c3334bb30aab6aeaa340d9e9 fix(packages): preserve symbol kind across owner reloads
2026-09-19 6ae704320d8ee7b148db5f723dfe1c5c79ceb0fe fix(ci): preserve current release-evidence race handling
2026-09-19 14c71e8098730131f080a15f073e6f5d91b29c17 fix(packages): preserve runtime cancellation fences during reconcile
2026-09-19 94783ae725d761539d5f0c74e83b6d4edda26a5f merge: restore current master tree while preserving #1055 changes
2026-09-19 ffdbfa0b2e6e1892d8cc6d9d08ee8262d712fd81 merge: reconcile #1055 package registry with current master
2026-09-19 aa24642303115f3ab574d69247cf0d644d63fdf4 docs(changelog): record portable package namespace validation
2026-09-19 f6c032da49e15f98862ead922331c74bab7ce2e9 fix(packages): enforce portable symbol namespace tokens
2026-09-19 72d60a24f78e5d53c2b966e55beee6229820c22f test(packages): reject nonportable symbol identifiers
2026-09-19 5e7614dc5b3a1f73e25ba8ce3bbc85b7763b5e70 Merge pull request #931 from lost-rob0t/feat/org-todo-canonical-926
2026-09-19 f43ced80ff1bae4a7b3a55b8af1666d2948bc8da test(packages): reject kind changes across owner reload
2026-09-19 fcc1c7c9b61a39b49d12db455ac87d4705decdd9 docs(changelog): record nested Org root discovery fix
2026-09-19 4bfc6099d291308423c673a9d8519a68f206485a fix(org): discover todos recursively within configured roots
2026-09-19 918a848063ee25179a96699759a68efc033d2fb6 test(packages): cover bounded app package profiles
2026-09-19 172614ce3c5c8236204ea61746605f59225d91d4 fix(packages): restore portable package count bound
2026-09-19 97093bced3a33b8b2d1413944ea9926f050d88c2 docs(changelog): record portable package version fencing
2026-09-19 646b99ab0dde377e7d17e976b5aebf6db5f96d11 fix(packages): fence portable version tokens
2026-09-19 b8858ff23b97ca072d39213568f6ddc0cc6d3b58 test(packages): reject nonportable version tokens
2026-09-19 c861ad900624fc991ce3214e3e49618d521517b2 Merge master into org todo canonical branch
2026-09-19 d6b2be151c28735e281ee49f1e2e8dd2209d7970 Merge pull request #1207 from lost-rob0t/feat/org-automation-run-envelope-1050
2026-09-19 d757014cd721e3afac353e180621efa255e00015 test(org): cover nested canonical todo roots
2026-09-19 a4982978ae47e63e5e72109aa70bee43ae5692fa Merge master into Org automation run envelope
2026-09-19 74687dd88f0ee2d34bf9273e96b9a36780caf429 Merge pull request #1013 from lost-rob0t/feat/android-code-editor-voice-1007
2026-09-19 770894e0158a926c49a18d3c93714be81dd1c532 merge(master): reconcile #1013 editor recovery with current Org authority
2026-09-19 39028eaa6af8d08ca64e023b4b9831c18d76fe29 chore(changelog): reconcile package entries with current master
2026-09-19 7879345f6be35b0c88da993a528d3b2ba43f7461 fix(packages): validate direct app package profiles
2026-09-19 c372b9849fee2dce50bd8b28e02ed139fb1016b8 test(packages): reject unvalidated direct package profiles
2026-09-19 595ea23c17f1aeba4be1ae651cde8a9b06ac430b docs(changelog): note Org automation run fencing
2026-09-19 e87f6ae010c99c2f2709fbe22db848ad0619d990 test(org): bind run envelope tests to planning contract
2026-09-19 766045afba12d2d6e9253a8d70ceda1314af6edc feat(org): add inert automation run envelope and stale-generation fence
2026-09-19 575db2cfa159a40822468a62d328b25ccec212c4 test(org): specify automation run envelope and generation fence
2026-09-19 49023469dd27b70b12bfddb2da0e42658a5758c2 Merge pull request #1162 from lost-rob0t/test/org-sync-workspace-authority-20260919
2026-09-19 8c7d9c11c353e063040cf512f446e3cb7095cae5 merge master into feat/android-code-editor-voice-1007
2026-09-19 8ce54736084dc024dfae92c2ff41b253ef2132fb test(org): reconcile shared workspace authority invariants onto current master
2026-09-19 f32dbbf95616a9b283ae63ffb612e529206636f0 feat(org): add symbolic Org automation recipe contract (#1160)
2026-09-19 18afb84b6420d8af8b95cf8afa89837b5a7096a7 fix(packages): enforce per-app version pins
2026-09-19 c0ef7aa266efda7789b373d5312ca8cfd61699b1 test(packages): require pinned activation version
2026-09-19 5b2fc85f7f49b078a8ae612719ed17ab8b01e937 android: recognize canonical Zara dotfiles config layout (#1182)
2026-09-19 7c9d21d1fadd6bda2bd25eadbfc3da172d1ec23d docs(changelog): record spoken code spacing fix
2026-09-19 370b493bc5ad177d8b3916dc238524bdbbc23d0c fix(android): preserve spoken code spacing
2026-09-19 092d0f08cd1e6f4b24f812121d7e0593d626ec25 test(android): cover release-notes launcher ANR recovery
2026-09-19 aad1d1b38b20d6c5e9cf2d2934beab61a0e63bd9 test(android): recover screenshot capture from launcher ANR
2026-09-19 cb2140413ddf1ae51d8382947fb0802a0e56c98d chore(packages): drop unrelated release-note test delta
2026-09-19 098b310b248cf9a128430f87a4924ea573eb9549 chore(packages): reconcile plugin manager with current master
2026-09-19 89f2a063d9d3d51f2f2f194cb2396758869aa318 chore(packages): reconcile plugin runtime API with current master
2026-09-19 110ed3320013cbceb7ef3e68f17f605c7f0ab722 chore(packages): preserve runtime registry export from master
2026-09-19 3a479e047b76a74c98f9e277cfd96286cae54bf3 chore(packages): reconcile changelog with current master
2026-09-19 623a535879d2ce1db829b0962c67b8c816232d15 Merge pull request #967 from lost-rob0t/feat/android-launcher-kb-memory-final
2026-09-19 b711358516aba630886e9f2f42edeca77237d247 fix(android): fence programmatic editor navigation
2026-09-19 aa22131b17839f6831343cbca863569a25f75276 docs(changelog): record voice selection fencing
2026-09-19 ee4c7cc4c65857e02bb9587221567c1ead5bda42 fix(android): fence selection-only voice edits
2026-09-19 e4b7117d9281a0a9bc0559246f0311d452d9b52d test(android): fence selection-only voice state changes
2026-09-18 dc27d466c2ed46f2d69a27c9361b47792122a8e3 Merge current master into feat/org-todo-canonical-926
2026-09-18 c710e494a16c54f56fc41ed5bedbd81e2918174e docs(changelog): record code-editor CI fixes
2026-09-18 79fb2706db4d68f0f30e6aaf40f53e1ec60efdce fix(android): use ColumnScope weight for code editor
2026-09-18 06a12b4c410734a48bf76454a03548a5599e77e8 test(android): align gate diagnostic with code editor slice
2026-09-18 c26a9c114e47a93a3e829129405f4f5b1decc570 fix(android): make spoken-code punctuation regex valid
2026-09-18 6a20157596e744ec248acbeea658a4012b4b9bbd ci(release): publish versioned Zara Code APK
2026-09-18 bd39fe4829890bd11d83ba1a177222b6000ebdc8 ci(release): publish rolling Zara Code APK
2026-09-18 4c1988b7cd4c298b6c36a787f891629fcf40cc6e ci(android): upload exact-head code editor APK
2026-09-18 551cfa353b38308959015a7a5cbc40fad06c81bd fix(android): sign code editor with Zara update key
2026-09-18 a3f5479883b1700563c0eb771a129f16c380cbdc test(android): require downloadable code editor APKs
2026-09-18 ed18f3206284ad2bd03c8a2eb7b8ceb524b59d78 docs(changelog): record per-app package profile isolation
2026-09-18 553c4a4e3b89f5428bc301df188aa65f3a04614b feat(packages): export app package profile ABI
2026-09-18 bb321361e8b22a7a4b9e7449be0abc7802744fdd feat(packages): add portable per-app package profiles
2026-09-18 0124ce7d66132680fbeb2b0d6f0e2a8069a6155e test(packages): pin per-app package profile isolation
2026-09-18 82509a6c3b83c10040e11ad97c7f93912451ce34 merge master into Org Home launcher foundation
2026-09-18 89e911f8862a2859712120f80c4a37893a2d7ae5 fix(android): reconcile revision-safe code editor onto current master
2026-09-18 ed01166ebd60fdb3c2a7193940d3d75e3be588c3 test(org): pin shared foundation invariants (#1159)
2026-09-18 cff27dc9b179d4c55ec15e4d6a23889a72bf77d4 test(android): pin release-notes acceptance dismissal
2026-09-18 6114576d84cdf8a10a2e24743bdc5e20e1627613 docs(changelog): record canonical Org todo storage
2026-09-18 beece81b547bcf2765be4983ec3945fb85af5e05 docs(org): document arbitrary todo workspace roots
2026-09-18 da7deac2b3d99d6a1af6db9a745f87536b745abd fix(android): keep launcher memory Kotlin deterministic
2026-09-18 cc9b3c44768ce181c94cefa795698e24d337392e fix(org): stop guessing operator todo layout
2026-09-18 af232b84890f8cf0314632ed337aab639603a6f7 feat(android): implement durable launcher Prolog memory
2026-09-18 f72914b4b6fef7c854e55a227a050933dee9bf4d test(org): reject implicit operator todo roots
2026-09-18 ae1a6736af1f813ec51b6b571ac15e97233cdcde test(android): harden emulator screenshot evidence
2026-09-18 d708c0094b2c2fdc1c1bc1bae29ef673ee7ebe25 Merge 9140b11ca3b64cdae7cca59e25f56c39460d2355 into 9cedeade0fb7b8d37209f04bcacabb988476f963
2026-09-18 9cedeade0fb7b8d37209f04bcacabb988476f963 fix(android): restore embedded Trealla local queries (#1153)
2026-09-18 2eb0bd2a2e2d46755a9272c2a0a342fba62f1ed5 fix(android): reject transcript updates after final r4 (#620)
2026-09-18 039e1d23916da9e017c3b7b85f57fea21dc926a9 feat(plugins): canonical unavailable startup result (#1127)
2026-09-18 99b4a2829df24819a2e78096ad478261cf12cf64 Merge pull request #621 from lost-rob0t/rage/core/388-tool-cancellation-r18
2026-09-18 3abe5b882a1e343877ae4aab943d63bf9b25753e Merge current master into #621 cancellation transport
2026-09-18 da9d8d1b3fe039f74939a13b771503798a163eec feat(android): add durable chat lifecycle and history controls (#1062)
2026-09-18 6a9c7e469287974035f07c990af612170c48203f Android local-first RuntimeHost + Assistant strict-local integration (#916)
2026-09-18 d417d18cce9846c63109f39ac4bc359d468f156b merge: reconcile plugin cancellation with current master
2026-09-18 77bfc9414c5a5cb6524984f47849aff3888e1071 feat(android): add portable local conversation persistence core (#966)
2026-09-18 0ad26a3405c39aa265af07f1834684e0ed621227 Merge master into rage/core/388-tool-cancellation-r18
2026-09-18 ffaa482cf621489bb67e1121dedb570095a472b0 chore(todo): add canonical ideas.org inbox (#1125)
2026-09-18 935a7734a0899c79ac41e32017c43c7b2dde556f feat(wear): add strict-local Zara Voice launcher
2026-09-18 27132ff59e366692c2ff64bb01c340823744a9f0 fix(plugins): notify capability registration waiters
2026-09-18 d3c7e4ab3551838cc42ede8fe577007cd934730f Merge master into plugin cancellation branch
2026-09-18 75b4954a895c01a6a4e2a8e7676dbac71e2e49e1 Merge pull request #1048 from lost-rob0t/rage/1046-runtime-contract-s1
2026-09-18 2a35994c7c6815cc3ae1523d4b42225810cecf0d docs(changelog): record composed plugin cancellation
2026-09-18 aa8dcd845e0e4fda4dbf1c8f7f644c4e821175f7 rebase(runtime): replay ZARA-RUNTIME/1 S1 on current master
2026-09-18 20f9c3877a9711dd0b815e11173dce86090312cc merge: reconcile plugin cancellation onto integrated master
2026-09-18 b72c3cd928a4a874bc394b150ca7675b9616bb90 Merge pull request #659 from lost-rob0t/fix/400-plugin-capability-composition
2026-09-18 ca985f4ca512c92168b323838aa2d90716a538f7 merge: refresh plugin cancellation atop capability composition
2026-09-18 e3d14b90133286a96988c50117fbb3f2a256b116 Merge master into #659 after rolling Android latest update
2026-09-18 9b0d54036a86d64aebacfd7678e7525bf49b0f0f ci(android): publish a fresh APK from every master push (#1057)
2026-09-18 b74a3325727ab511cb776872d7b9f5d73dfae191 fix(android): relaunch saved task during acceptance recreation
2026-09-18 a695ade721661ab23544bb16a72335a740be9fb4 test(android): require saved-task relaunch on recreation
2026-09-18 5986d202989097297969c97a330488c8246f3ed0 test(packages): enforce per-app registry isolation
2026-09-18 db6f337af8725ae39e2ffab41b0ab43a04d01432 merge master into #659 after release publication fix
2026-09-18 a36bcc1ad27636b12cdfcc3c39ce828d0b259202 docs(changelog): record programmable package symbols
2026-09-18 a9e66c85ea53c095f50a629d71049c44dae89738 test(plugins): prove symbol override lifecycle
2026-09-18 517dbd433f61829af93615a51269e2bcd7fd361f feat(runtime): export programmable symbol contracts
2026-09-18 9f2e95be931e0763163da21674deee0c827075bb feat(runtime): expose package symbol registry through host
2026-09-18 1467ab0df9216d40e6151a15c03317621f97c66c test(android): harden stock interop transport readiness
2026-09-18 57f129b3e476f62f0d16f125cafcb3c6dbcd1257 feat(plugins): inject programmable symbol registry
2026-09-18 635e6e738b1920cdd5ffbbb98464fd52c9951a31 feat(plugins): let packages register canonical symbols
2026-09-18 e2d2d98eda73db3c2a0cf23db5aceff03d298440 test(runtime): cover package symbol overrides and rollback
2026-09-18 62dece97b8d55d431c36cabfe840b3d9b2b17846 feat(runtime): add stacked programmable symbol registry
2026-09-18 80342717114e372e30550fe74fca1f022a29f681 ci(release): reliably publish promoted v0.2.2-alpha (#965)
2026-09-18 c9d87cf8799daf82c203f1400092b7bb00df642a fix(android): dismiss versioned release notes in acceptance
2026-09-18 c8006d9fac9c6e1fbed92fa520473c8814a9374c test(android): reproduce release-notes screenshot blocker
2026-09-18 e72783147456f777ea7e72e29ce64bb057b2b39c chore(plugins): reconcile capability composition with 0.2.2-alpha master
2026-09-18 04b5244dc6b09693d34ddceea19dde0cae5f7714 docs(changelog): record live plugin approval enforcement
2026-09-18 3fed727a444ae86e723bab53f5ae84879599237c release: promote source to 0.2.2-alpha (#1039)
2026-09-18 e4903e06e6ec60977338126520726c9e2db7ec4c feat(changelog): canonical release notes on desktop and Android (#1044)
2026-09-18 15d21eb5dbcb7342c556ccfeb01a983e07f0c4ce rebase(android): replay audio focus release retry on current master (#615)
2026-09-18 5b0e2eb0b4eb8e5147d6cbff948ded5eb5fd15e5 Merge pull request #1037 from lost-rob0t/feat/android-project-contexts
2026-09-18 bd16eb6054ac424bc8ea9ab767942a9592bdd1bb chore(plugins): sync composition branch with current master
2026-09-18 fbba35488f49ba01b47397b65b9894dfc3173c4e Merge current master into Android Projects
2026-09-18 efd2425f48cdcf9c7d05bd5bd96c67efa57cefa3 feat(android): simplify Zara to three left menus and tabbed settings (#939)
2026-09-18 05f2fdd691c97c9e53395d7a957364bf3046b6d8 fix(plugins): recheck live approval metadata before composition
2026-09-18 aac43f550242882087089c2cabc94dae5167c23a test(plugins): prove live approval metadata is rechecked
2026-09-18 de867d43bcd162b5666184dea1f36865a9ecf1f4 fix(android): compile Projects error banners on current Compose
2026-09-18 a56f8cc27a4dabecdb757d07b7872061daba0472 Merge current three-menu shell into Android Projects
2026-09-18 eebd109c755405cc79f361d6f2021bfba6771683 Merge master into feat/android-three-menu-navigation
2026-09-18 38f5a6d45f80b0203698fae07e1ba305553efeff ci(android): reconcile navigation acceptance with source provenance
2026-09-18 46392769c206e43a33680741ab3584e6e2da70e2 Merge pull request #997 from lost-rob0t/quality/dual-screenshot-deep-gate-2026-09-17
2026-09-18 9e134aaaf0cc0d461a298c92c7f6de327376af85 compose(runtime): replay #621 composed cancellation bridge
2026-09-18 edbdf8fe07ae43a4722e335c048838b934f2c4e6 compose(runtime): replay #621 t/test_plugin_capability_authorization_cancellation.py
2026-09-18 607d4be1c9267d468db8870a66661a0f1483fbaa compose(runtime): replay #621 zara/agent/tools/registry.py
2026-09-18 2c2b566586a23c665e48104dda9d7e2db8407ecd compose(runtime): replay #621 zara/plugins/__init__.py
2026-09-18 2c150387bec94d5ddb1e3c1b2ac775dfc3e16cd7 compose(runtime): replay #621 zara/agent/tool_cancellation.py
2026-09-18 5ce7267413136ed19af2b3cf3fe06a0925ef8143 compose(runtime): replay #621 t/test_plugin_tool_cancellation_r18.py
2026-09-18 279e8c03f755e81c165a0159f67df664d06572b3 compose(runtime): replay #621 rage/388-plugin-cancellation-r18.org
2026-09-18 811890371cea35eb282103da217119c434abfd66 fix(android): validate canonical SemVer correctly
2026-09-18 229d4b9a8e88a75322385a6a8f432de0b219afe2 test(android): reject over-escaped version regex
2026-09-18 886ad299c871b7df2aba6af12893e4b73ff01d37 fix(android): keep plugins block before version loader
2026-09-18 dc8e3e0cfa6d8687b353cc1f66ba43a184455ba3 test(release): require Gradle plugin ordering
2026-09-18 6a8aa5c6dc75e079c28be0d8361910b840a141fa test(release): keep version target single-source
2026-09-18 dca8e71964553c3b88eed74cc990f1f049db143b fix(release): fail closed on version promotion
2026-09-18 df4c92aa2200d085f500803e63cea11f4f551f47 fix(release): enforce canonical Zara version context
2026-09-18 4e2f7a8b4b5bd9664cacbe31bc1800e93db031d2 test(release): require canonical version context
2026-09-17 c3fd8c0795ba871133074eab86467ab049609a28 Merge current master into Android three-menu navigation
2026-09-17 43869ca0813379ca308f669e8f50982a5a89c9a3 fix(ci): install emulator libpulse host runtime
2026-09-17 74b011bc32644d87ef071207191f52fc7f006f01 test(ci): require emulator host libpulse preflight
2026-09-17 786dde0c00e1ae5ebfb6cac38c6f9c16d9582564 Merge master into fix/400-plugin-capability-composition
2026-09-17 836351067b95a094ee0749355e728579886cf44b Merge current master into release evidence gate branch
2026-09-17 c4c896d14535eca7233f601ee9e06bb54632c81e fix(ci): purge sdkmanager download intermediates
2026-09-17 ceabc94f4abccdae81fc813d0b34e5b9f46dd18b test(ci): require sdk download-intermediate cleanup
2026-09-17 2403f81435b3b85e74e5793361c7d605d37dc40e fix(android): replay Assistant qualification on current master (#898)
2026-09-17 5e027d79464a1c48da07753c1da0e82b5efc022c test(ci): align emulator retry contract with refreshed sdkmanager
2026-09-17 2ef8db50ad662d0367c195ea5f85322afddd2f39 fix(ci): refresh Android SDK manager before emulator provisioning
2026-09-17 85d285c2716f42edb64a3acc2ed4a56e785d3722 test(ci): pin current Android command-line tools contract
2026-09-17 b28257d1c3665efbee42801cf7aad9f34c1dca64 Merge master into quality/dual-screenshot-deep-gate-2026-09-17
2026-09-17 4e714c8894a2f4b9948decdfcd152ffd6d7a98aa merge: reconcile three-menu navigation with current master
2026-09-17 65efb1f4795ad12763fa25d567eff5ae0b30e633 fix(ci): purge corrupt Android emulator download cache
2026-09-17 c76e458b174372da12c8c28dbb132e03cc63e512 test(ci): require Android SDK download cache purge
2026-09-17 4dc9963dbe8de849ccccb80316401e2aeab2aa91 test(android): harden project metadata failure cases
2026-09-17 a2a8dcddac143926fe237cfe28424f5e140eb87d test(android): require visible Projects operation failures
2026-09-17 033443942d3c3990bc241283a1ba824a06cf14ec fix(android): show Projects operation errors in context
2026-09-17 eee8aa1a5b6f8bd8b402229fdabeecd52f9bc864 merge current master into #659 drain candidate
2026-09-17 7ad74adb8b3c41f9396ad6b332c52dac0f652233 fix(android): keep Projects error parameter source-compatible
2026-09-17 1bd2889797e90e2cd7cd0704a5c78eae84b47e9e fix(android): surface project operation failures
2026-09-17 b98470a28fc564cead85d6f6b28df78aef73b0fa feat(config): make project identity Prolog-driven (#914)
2026-09-17 a0e0fc672f6cf1c4ff14bea0185732962219676d docs(android): document project scope and isolation invariants
2026-09-17 53255ab99a4f5185a9c2b6445ea280a815c98a58 test(android): pin Projects UI and host wiring contracts
2026-09-17 be2983213494f4ff05aa3b6924a0deff90033527 fix(android): keep scoped project turns out of default conversation
2026-09-17 faca81cecd55731a38625fe80fc5dc2e6b9968c7 test(android): prevent project chat contaminating default conversation
2026-09-17 47380f792462bb4a7c6cbfbf6e9cc5d76186f9e4 test(ci): assert emulator retry behavior independent of YAML wrapping
2026-09-17 10dd893f774d41b50b60ea07945b1b8af696c84c feat(android): persist active project and isolate project chat turns
2026-09-17 4f8108446215d51769b37c6bd3c9856015b7f390 feat(android): wire Projects workspace and chat scope
2026-09-17 b857dc3f2e937d50ef091fad588135cd28c9eb26 feat(android): add active project chat breadcrumb
2026-09-17 00317f7869c513cf8559826e08cf9ebddd9e6d4f feat(android): add real Projects workspace surface
2026-09-17 3908ee9908d3ae800c4456190d85eeca47a7cb4b feat(android): route text turns through project conversation scope
2026-09-17 cf6b8862380d7629a66e67e2cc9916cfef79a699 test(android): cover project conversation routing
2026-09-17 221cd82df6a5de9faa3059601bd4269660224ca9 feat(android): allow explicit project conversation routing
2026-09-17 36f27625e519d12a0f2556839252335ad3c0e5e6 feat(android): persist bounded project contexts
2026-09-17 0f4424cb209b038a382e6354def4816d669e7813 test(android): pin persistent project context contract
2026-09-17 56bcd2615babb06ed3221f88c99b243ee3edb2cc test(ci): pin desktop screenshot hashes
2026-09-17 9f864bfbbcfa2fbad33adc7ad648a68332f17528 fix(ci): hash desktop screenshot fixtures
2026-09-17 fe8403846cd242507853248fd8c9ebf2de76b988 fix(ci): verify desktop screenshot content hashes
2026-09-17 aa90caf9ced365d98e12c054931ab3916294ce61 test(ci): reject tampered desktop screenshot evidence
2026-09-17 22f836f99d89220bc191a9d2e586244a4aa94e02 merge: reconcile screenshot gate with updater hardening
2026-09-17 22f8fea1fbb65eda6decf779b00db15ef79534ff merge: reconcile three-menu navigation with updater hardening
2026-09-17 786077f7919ed9f89788eb1991503b0bf96b338e fix(ci): verify idempotent host emulator bootstrap
2026-09-17 efead73cb55617de0b2896664b6047c4e0a0dc70 test(ci): require verified idempotent emulator bootstrap
2026-09-17 6f704cf2f87c5a676ca1281965f5162142b7a588 fix(ci): resolve emulator sdkmanager from host SDK root
2026-09-17 ff2ebf0844415a288c7a03eb8c30cc05c6b94f4a test(ci): pin host sdkmanager resolution for emulator gate
2026-09-17 52e4cbc853c711d947687f160174081d25465422 fix(android): harden verified self-update lifecycle (#899)
2026-09-17 90e4a11e739c3dc4ad6a67b101e2cdac3471dd1f merge: reconcile three-menu navigation with current master
2026-09-17 35b2439eb29c10e5769e0c7e6484cd10af1e0a4b Merge master into quality/dual-screenshot-deep-gate-2026-09-17
2026-09-17 6769f3a2e6e42d99e1d5fa359e85a20a621683bc Merge pull request #876 from lost-rob0t/feature/android-wireless-pairing
2026-09-17 0c54c83ecaa02ebac63e1902f1cfe8a20cbcdd82 test: lock emulator SDK retry into release gate
2026-09-17 5c9ec16b9e4143dcab5cf7be9701a2ecbf2b78ed ci: retry transient Android emulator package downloads
2026-09-17 d27d2e9764fcb3c999653c2f94c73348998dff1e test: sync Android gate diagnostics contract from master
2026-09-17 36728e3e74b3c5d3d4de180afd783b257f7474f3 chore: sync Android gate diagnostics from master
2026-09-17 0ecf924d941ba192b315dd6264c2668ef810909d chore: sync stock interop diagnostics from master
2026-09-17 49aa0a9334efb05a9cdff3432882b181c4139a99 test(ci): assert emulator acceptance behavior, not heredoc syntax
2026-09-17 eec1e1c30be8b32ea3e4a9826367e6bcf4260e2c ci: fix emulator acceptance command quoting
2026-09-17 78d8f2b07c8b12c6d8a5c8f0ac5ce41af9873d41 fix(ci): target screenshot emulator deterministically
2026-09-17 1679d5bf1ed6590cbe296096af195331759d15d6 test(ci): require explicit emulator targeting
2026-09-17 819b329cb93ce3b932f1a18ee4eb004a755afad8 merge master into #659 current-base validation
2026-09-17 d61dc253d47bdf8d5376f8297dcc305efc032561 fix(android): replay scanner-friendly QR pairing on current master
2026-09-17 8dceebb91fc3e58f5acb430388611d0ef9c6a273 Merge master into dual-screenshot gate after #1032
2026-09-17 02cdf6ebba8a15bcf1d2f583c1bb7ecb928146c0 ci: retain stock ZaraServer log for #575 recurrence (#1032)
2026-09-17 057510a2521daf49c727ca7d5d3052c6487e5635 test(ci): keep provenance fixture hermetic
2026-09-17 fc33a4cbbde7d3e05be98658a03458167f7801ff fix(ci): run emulator acceptance under bash
2026-09-17 614c277dc5723a2bef92de09eff2d476dc3cd1ad Merge current master into Android three-menu navigation
2026-09-17 98140b73cda10e7d9a8d3492c4481fa31a81bda1 feat(plugins): replay generation-fenced capability composition on current master
2026-09-17 a48f80c766d2c831dddbc38aed567ce62cb63ffa chore(ci): anchor dual-surface evidence gate to merged #947 master
2026-09-17 01a9a56307d0edbd1f6afdede364af188c2dbe86 fix(ci): replay Android/Wear artifact gates on current master (#947)
2026-09-17 7c67e67e94d74059df82c27d05b317aa9721c671 chore(ci): integrate dual-surface evidence gate with #947 candidate
2026-09-17 735310cc8eb68e94067c5de0fd5b310055aa6487 chore(ci): refresh release artifact gate onto repaired master
2026-09-17 df01a886cf3e4f800458c2269a04af84a86c496c fix(android): restore AutomationActivity Compose build
2026-09-17 ef847b25481c82c1dbba5847d84f007dea1cc9b2 test(android): cover rail accessibility and saved drafts
2026-09-17 803c26df21fe7077b16bd0fd974b2229ec37c2f0 test(android): deepen navigation lifecycle evidence
2026-09-17 9d7bb9e94fa4df45c583794c5ff965329fe204a7 test(android): validate screenshot harness semantics
2026-09-17 85a1735e5fa6b3b4c4f3d8c059c0ac76c12d41f8 test(android): exercise three-menu screenshot lifecycle matrix
2026-09-17 80a7a4d2757908b11c04ea72191f83e710ab3efe test(android): pin three-menu screenshot acceptance contract
2026-09-17 dd5c512e9aa3f1823c38b6a59283a3487983b15b fix(ci): bind evidence to exact reviewed head
2026-09-17 d5638902fbfeebfd2e54e63780032dc521cccd30 test(ci): reject mismatched screenshot source claims
2026-09-17 76e32ffea4d833eeebfbf61d259f48da314564d8 fix(ci): verify Android evidence source provenance
2026-09-17 97f30012cb2c40cdc144f7f93220613ff632e8e6 test(ci): cover tampered and escaping evidence
2026-09-17 d8d8ffd925828765fd15cd4fb4f6e3b585e655d3 docs: define dual-surface quality gate
2026-09-17 a7c4422ac08734a0f2583b6ccad8484737b0f68f docs(android): make screenshot gate repo-wide
2026-09-17 0dfd030b4f9033b56abe4ae76dfcc8a8b10660a0 docs(ci): require cross-platform evidence in PRs
2026-09-17 9d9722659173c73d2c4acd8fb7efcca0f8db9806 ci: require dual-surface screenshots and deeper regression
2026-09-17 86df0b494dba6386b66720f2c7ed342c81948204 fix(android): stamp reviewed SHA in screenshot evidence
2026-09-17 ab812a2196b7bfc8ffb23d044cfc2c894147dc12 feat(ci): validate cross-platform screenshot evidence
2026-09-17 8b4dcbc86f524ea51f8281a884d5dfb80e2b289c test(ci): define dual-surface evidence gate
2026-09-17 b8b64d09f3c29afa3feb018cac1a19804261ac52 fix(ci): replay Android/Wear artifact gates on current master
2026-09-17 6cbc73c6f894231e1216df9a5f63e51bfa75cd80 feat(android): add Prolog-driven Samsung Health plugin (#971)
2026-09-17 b47c6aa8d83fabadff76c078c006e36fa369425d Merge master 8a11e9c583a5539c187633bcf87901111e2cc827 into feat/android-three-menu-navigation
2026-09-17 ebf2d9b2acecb75aaf65cfa93c65beb6afea8301 test(android): define launcher discovery and KB feedback contract
2026-09-17 a784926d2da9f8fe5fd43c982d9c95ac2bc823f4 test(android): define durable Android KB memory contract
2026-09-17 8a11e9c583a5539c187633bcf87901111e2cc827 fix(android): restore local-first runtime and automation on-device (#941)
2026-09-17 18492c07d8500f0bb5d5ae0f313df87ffd89dd33 Merge cadbe265fdb93baf8b6d1043e7cfe932d9248c5f into ec9756e56537ee85f165291499ceb6312ee84451
2026-09-17 cadbe265fdb93baf8b6d1043e7cfe932d9248c5f docs(android): record navigation red-green evidence and remaining release gates
2026-09-17 b4aa27c8c4911bf4094466fb2781134b87fadd6c docs(android): document navigation, grouped settings and visual acceptance matrix
2026-09-17 9b033f3dadc00e6d7a497b7f653bb43bca00506a docs(android): revise canonical navigation to three menus and settings tabs
2026-09-17 5a32f9e2253146a2882dbe988d89d8f55a951ae1 feat(android): replace eleven-item drawer with three menus and tabbed settings
2026-09-17 ec9756e56537ee85f165291499ceb6312ee84451 feat(android): host embedded local AI and offline TTS service (#907)
2026-09-17 2c72350e906ab0f27b776a6b6c3a7a6dffc11d72 feat(android): add semantic navigation rail and scrollable menu tabs
2026-09-17 1b2f3fa8c687f8f66c72ea952be535b17fb1dd3c feat(android): model three menus with validated per-menu navigation state
2026-09-17 0f2174b552853df8a55db5559b4c12c91ce0507d test(android): run navigation contracts through the existing JUnit gate
2026-09-17 7b1412137e86de0d1de7da12d4e6d1dfc3838c48 test(android): require tabbed settings, state preservation and adaptive shell (RED)
2026-09-17 cb09c157028336eeb1297a8a7bf25221efd5b9da test(android): define three-menu navigation and restoration contracts (RED)
2026-09-17 9140b11ca3b64cdae7cca59e25f56c39460d2355 fix(todo): isolate Org task metadata from child headings
2026-09-17 841018e1aeb0e44c2f66e0b805a308eaed1b3eb3 test(todo): protect child Org headings during parent edits
2026-09-17 53a4da62ae2629423f94de889e6f4f7a64549034 test(todo): update resolver corpus for Org todo intents
2026-09-17 f6185850083b6e3bf363939f7bc4572e8bbfd879 docs(todo): document canonical Org and gpt-todos integration
2026-09-17 89c91157539e611b9f386956aca51e045d6f8501 fix(todo): consult canonical Prolog runtime for expert brief
2026-09-17 b79005556b2e6f6089b2de8d89af7529c0ca397e test(todo): fix canonical Org fixture syntax
2026-09-17 0d831fb1b70125058fdd5638b41ac0d0e09e0053 test(todo): cover Org editor and expert todo intents
2026-09-17 bc3c8c8298380069b55a2b9dd1fd298c2429fb44 feat(todo): load todo expert into canonical Prolog runtime
2026-09-17 151b8903bc9ecc8cbf0abfa13b0ceb8d07e92515 feat(todo): add Org editor and expert todo intents
2026-09-17 65455c06c4ee88b1196f04c9fdf54cc6d9d40fc4 feat(todo): register Org editor and expert todo skills
2026-09-17 bdb280ead0d144e03660bcdab5a9b7fdbfddb788 feat(todo): expose Org ids and expert brief to agent tools
2026-09-17 48046145d0ac9c70ff02eee575099f4717e2d47a feat(todo): make Org store the default todo backend
2026-09-17 61f61784fdf11e05bc81540cdc551d118bcdcbbd feat(todo): add deterministic todo expert rules for #926
2026-09-17 eb13f487ebf1186a189b3198220935668a2d89d0 feat(todo): add canonical Org-mode todo store for #926
2026-09-17 a332d3e74c8c2040b851cc3e77d6dfb8d16c30ad test(todo): fix upcoming expert fixture syntax
2026-09-17 f1c1c3e26a79fde2abbbfad8c92571245137fdc3 test(todo): define Prolog todo expert contract for #926
2026-09-17 f78d57386f489a5df06e61622934bdce7542b20f test(todo): define canonical Org store contract for #926
2026-09-17 e8e8382ddea3a48b1b67de9146e5e8ae6d17645f Android: Prolog automation, special access, and Git config templates (#915)
2026-09-16 5910759379ff623dad83bbd5703629445e3a063a feat(android): install Zara Wear from the phone (#903)
2026-09-16 ab1ff39f14437db63ac5f47b1ab82bf48248798f ci(android): publish reproducible releases and direct latest APKs (#902)
2026-09-16 82496e16b9081ff84c59ce52bfab02af0c4e0f5f feat(android): complete expert logic authoring studio (#894)
2026-09-16 b03cbf5c7ed3653c023588db079c87a8a1ed940a Merge pull request #891 from lost-rob0t/feature/android-local-prolog-studio
2026-09-16 130dd414b38350607f8a14644e059468934d0a42 feat(android): add local Prolog studio and verified updates
2026-09-16 43d8fa8c98771e02aff5ee1850ad5f2be7c35377 Merge pull request #890 from lost-rob0t/fix/android-connection-fix
2026-09-16 3e6c61c2f00963296a7d90b8266372e48bdfd2cf release(android): prepare v0.1.2-alpha in GitHub Actions
2026-09-16 66b976e65da06e68f2277bebc1762cde40836c85 feat(android): add Zara adaptive launcher icon
2026-09-16 d3c829f9ef04800137ec158bec8752397d1400f0 fix(android): expose connection stages and allow explicit server repin
2026-09-16 e030ca4cd3667d533fa7005514bb89ca847c7bb4 Merge pull request #886 from lost-rob0t/fix/android-remote-listener
2026-09-16 a04b5a7c2b7e7eb433396f0b08196cd68ceb7094 feat(server): serve authenticated Android TCP alongside local IPC
2026-09-15 812d202c0b061a05a081ae8c94f5b02a349954ad Merge pull request #885 from lost-rob0t/feat/chat-ui-overhaul
2026-09-15 a5bb0650e18648b57d416a89e50aeeb6843139cb feat(desktop): modernize copilot conversation UI
2026-09-15 a08db0d8be2059ef0d9c5afb18dad4f5a4175772 docs(rage): #880/#881/#882 merge closeout (PR #883, 8bb90979) (#884)
2026-09-15 8bb909798047eb3558623bd139e610ede87c44f6 fix(voice): Pulse playback sink, capture-stall watchdog, configurable STT decode (#880 #881 #882) (#883)
2026-09-15 88b8db66d04e2f97e291a84c6f5790a6f7cb4bce fix(wake): match client READY enum and await reconnect future (#879)
2026-09-14 e317c51e437cae3aaebd9432453439172ee1161b Speak Qwen3-TTS through the OpenAI-compatible streaming API (#878)
2026-09-14 6a5f98f414b437c91dc6a8fffd25a1a2bc3a262d fix(desktop): project daemon startup completion (#877)
2026-09-12 a6605f5e1dd36273834cd3c58aca89a55b07bba8 Merge pull request #874 from lost-rob0t/feat/adb-pairing-scripts
2026-09-12 96577589a2bb9bf476e1cb78a528d64f08a395af Merge master into feat/adb-pairing-scripts
2026-09-12 6ba387fb46342d51f9b21ea5ad8a0a0bff869c9e test(android): gate wireless ADB pairing helper
2026-09-12 d1f0ce0cbbcf20d6bbe2b8bf624e95d179ed1474 Merge pull request #871 from lost-rob0t/rage/866-wear-foundation
2026-09-12 7f06dc88b7ba3072a705d8bf74dc8a9885668e30 android: make adb helpers executable
2026-09-12 adcc8e730f75809dd1ea79eea2977d4f602efd9f android: keep qr pairing nix-first
2026-09-12 de9ec42627e8093dd63ae621870ad38120de080d test: cover adb qr pairing flow
2026-09-12 9b40b8f31ead13417d51f553a9da075d24d17919 android: add watch adb pairing alias
2026-09-12 ebc715cb91796905dfc44588bc818d51caeea93f android: add adb qr pairing flow
2026-09-12 3ce2f954ff041d48c3d5b9d0371d038c315ca799 android: add reusable adb pairing helper
2026-09-12 163cc7d0fbefa702bccb090f341a43ee3be6ac07 test(android): keep interop diagnostics contract task-list agnostic
2026-09-12 3ee772a88ee68d26ffb0735ba03f485acbea65eb ci(android): publish phone and Wear debug APKs
2026-09-12 b998df6b76d8972e1ccabe12a83730a0ef83db33 test(android): gate phone, shared theme, and Wear APK together
2026-09-12 a595f5891f19bf188ebb0c4360789d7962378709 test(android): wire shared theme unit tests
2026-09-12 4ae87072f7f1171c89986fea51cec42a22100468 test(android): cover canonical shared Zara themes
2026-09-12 994483b3fb610d53b0cf89ae4851b4ad97612aa8 build(wear): pin stable Wear Material3 independently
2026-09-12 fed6778d22f0b99c059769f3dca87d064271c393 test(android): validate shared theme source after Wear extraction
2026-09-12 7d4688733cde947031f45f7209231ac78f7acc76 test(android): use shared Zara theme type
2026-09-12 7da7ad1f9f6b3a959f13a176770313e87db87122 refactor(android): consume shared Zara theme type
2026-09-12 4af9424a047669a3c86d2118853f03eba92158a3 refactor(android): import shared Zara theme in preference store
2026-09-12 a445826ee14e0f00b5b850730b3296d90d097494 refactor(android): consume canonical shared Zara theme tokens
2026-09-12 da2fc3234c214b45263a78498b5e75ca772e6fa3 feat(wear): add Zara-themed round watch client shell
2026-09-12 ae6f685cd10b1bcb83a0e50983c12ff54c21853c feat(wear): declare standalone watch application
2026-09-12 319eab08fc5eb60632fb9c5ebe08af19fe3293ee feat(wear): add standalone Zara Wear application module
2026-09-12 a750a2a577303f3cff0fefa68d69ad4f6e6d38a8 build(android): consume shared Zara theme module from phone app
2026-09-12 1efc53e2aeee56c4d31dc78f5d6d6ad3b2a800b2 build(android): register shared UI and Wear app modules
2026-09-12 71f125640620e1fabfaa6b62fb7581c0fc57f4cf build(android): register library plugin for shared Wear UI
2026-09-12 6c05ccf1efba01442e6aa60f1ec25286ded0ee4a build(android): add Wear Compose and library plugin aliases
2026-09-12 e637256c71798f91ac01df2405e644e1d8e6e694 build(android): add shared UI library module
2026-09-12 e342888b5e608505b3b7ca390236d165c729d67f feat(android): add canonical shared Zara theme tokens
2026-09-12 6504b3176d269a21374ebdc062bc89c17ef40dc5 test(android): define RED Wear shared-theme contract
2026-09-12 a9c4af23036df5b9f79c6d546b9ebc88b2d7931b docs(rage): start Wear foundation iteration for #866
2026-09-12 336fddb9840a7699cc0316b107545a6990488319 Merge pull request #865 from lost-rob0t/fix/daemon-vulkan-qwen-e2e
2026-09-12 240f9b86597e406ba28c38a8bd1c7b078ea0e89e fix(kb): preserve existing project loaders
2026-09-12 3c1065c3ce273f2c85cc704d5e64a97b46e108d7 fix(stt): route daemon Vulkan through whisper.cpp
2026-09-11 12f202ba31bed0a0c641e45a57fbfb3a14a582ac fix(wake): share daemon endpoint and CURVE configuration (#864)
2026-09-11 db97e030215a49614a7fa533a83b0ecfb2066ea0 fix(wake): read audio_output_format from the client contract (#861) (#862)
2026-09-11 81a8cdcd04dd8bb3748cceda111b9296ad750d97 test(transport): guard client connection failures end-to-end (#669) (#860)
2026-09-10 8c32d458c8781063950e9d5d18dffc6a13482092 fix(transport): tolerate loaded hosts and surface silent route drops (#669) (#859)
2026-09-10 23ad58013f8590a88e3514165c39318d1a641b29 fix(prolog): actionable diagnostic for hyphenated user config atoms (#670)
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
```

## Repository paths changed, last 14 days

```text
.github/pull_request_template.md
.github/workflows/android-latest.yml
.github/workflows/ci.yml
.github/workflows/rage-575-apply-green.yml
.github/workflows/release-v0.1.0-alpha.yml
.github/workflows/release.yml
.impeccable/design.json
.prolog/kb/daemon_startup.pl
.prolog/kb/desktop_copilot_ui.pl
.prolog/kb/index.pl
.prolog/kb/voice_ingress_stt.pl
.prolog/kb/wake_connection.pl
AGENTS.md
CHANGELOG.md
DESIGN.md
MANIFEST.in
android/.gitignore
android/AGENTS.md
android/DESIGN.md
android/THIRD_PARTY_NOTICES.md
android/app/build.gradle.kts
android/app/libs/README.md
android/app/src/main/AndroidManifest.xml
android/app/src/main/cpp/zara_trealla_jni.c
android/app/src/main/java/ai/zara/app/AndroidAppSession.kt
android/app/src/main/java/ai/zara/app/MainActivity.kt
android/app/src/main/java/ai/zara/app/ZaraApplication.kt
android/app/src/main/java/ai/zara/app/accessibility/AccessibilityAutomationAdapter.kt
android/app/src/main/java/ai/zara/app/accessibility/ZaraAccessibilityService.kt
android/app/src/main/java/ai/zara/app/assistant/AndroidAssistantRolePlatform.kt
android/app/src/main/java/ai/zara/app/assistant/AssistantInvocationGate.kt
android/app/src/main/java/ai/zara/app/assistant/AssistantLifecycleFence.kt
android/app/src/main/java/ai/zara/app/assistant/AssistantRoleController.kt
android/app/src/main/java/ai/zara/app/assistant/AssistantRoleVoicePolicy.kt
android/app/src/main/java/ai/zara/app/assistant/AssistantVoiceSessionBridge.kt
android/app/src/main/java/ai/zara/app/assistant/ZaraRecognitionService.kt
android/app/src/main/java/ai/zara/app/assistant/ZaraVoiceInteractionService.kt
android/app/src/main/java/ai/zara/app/assistant/ZaraVoiceInteractionSession.kt
android/app/src/main/java/ai/zara/app/auth/EnrollmentRepository.kt
android/app/src/main/java/ai/zara/app/automation/AutomationActivity.kt
android/app/src/main/java/ai/zara/app/control/AndroidControlAccess.kt
android/app/src/main/java/ai/zara/app/conversations/ConversationStore.kt
android/app/src/main/java/ai/zara/app/device/AndroidAppAliases.kt
android/app/src/main/java/ai/zara/app/device/AndroidAppLauncher.kt
android/app/src/main/java/ai/zara/app/device/AndroidAppSearchLauncher.kt
android/app/src/main/java/ai/zara/app/device/AndroidUriLauncher.kt
android/app/src/main/java/ai/zara/app/device/AppSearchAdapter.kt
android/app/src/main/java/ai/zara/app/device/DeviceActionTypes.kt
android/app/src/main/java/ai/zara/app/device/DeviceCapabilityRegistry.kt
android/app/src/main/java/ai/zara/app/device/OpenAppAdapter.kt
android/app/src/main/java/ai/zara/app/device/OpenUriAdapter.kt
android/app/src/main/java/ai/zara/app/device/OpenUriPolicy.kt
android/app/src/main/java/ai/zara/app/device/RegistryDeviceActionHandler.kt
android/app/src/main/java/ai/zara/app/diagnostics/LocalRuntimeDiagnostics.kt
android/app/src/main/java/ai/zara/app/history/PortableConversationStore.kt
android/app/src/main/java/ai/zara/app/launcher/LauncherCatalog.kt
android/app/src/main/java/ai/zara/app/localai/AndroidOfflineTtsBackend.kt
android/app/src/main/java/ai/zara/app/localai/LiteRtLocalLlmBackend.kt
android/app/src/main/java/ai/zara/app/localai/LocalAiAbi.kt
android/app/src/main/java/ai/zara/app/localai/LocalAiContracts.kt
android/app/src/main/java/ai/zara/app/localai/LocalAiProvider.kt
android/app/src/main/java/ai/zara/app/localai/LocalAiRuntime.kt
android/app/src/main/java/ai/zara/app/localai/LocalAiService.kt
android/app/src/main/java/ai/zara/app/localai/LocalAiServiceClient.kt
android/app/src/main/java/ai/zara/app/localai/LocalModelStore.kt
android/app/src/main/java/ai/zara/app/localai/LocalTtsContracts.kt
android/app/src/main/java/ai/zara/app/projects/ProjectContextStore.kt
android/app/src/main/java/ai/zara/app/prolog/AndroidAutomation.kt
android/app/src/main/java/ai/zara/app/prolog/AndroidAutomationCatalog.kt
android/app/src/main/java/ai/zara/app/prolog/AndroidKnowledgeBase.kt
android/app/src/main/java/ai/zara/app/prolog/GitConfigTemplateImporter.kt
android/app/src/main/java/ai/zara/app/prolog/LogicLanguage.kt
android/app/src/main/java/ai/zara/app/prolog/NativeTreallaBridge.kt
android/app/src/main/java/ai/zara/app/prolog/PrologStudio.kt
android/app/src/main/java/ai/zara/app/prolog/TreallaSemanticRuntime.kt
android/app/src/main/java/ai/zara/app/runtime/AndroidTextSessionController.kt
android/app/src/main/java/ai/zara/app/runtime/ClientStateStore.kt
android/app/src/main/java/ai/zara/app/runtime/ConnectionFailureReason.kt
android/app/src/main/java/ai/zara/app/runtime/DeviceActionHandler.kt
android/app/src/main/java/ai/zara/app/runtime/LocalZaraServer.kt
android/app/src/main/java/ai/zara/app/runtime/RuntimeMode.kt
android/app/src/main/java/ai/zara/app/runtime/RuntimeRegistry.kt
android/app/src/main/java/ai/zara/app/runtime/RuntimeState.kt
android/app/src/main/java/ai/zara/app/runtime/ZaraCapabilityCodec.kt
android/app/src/main/java/ai/zara/app/runtime/ZaraDeviceActionCodec.kt
android/app/src/main/java/ai/zara/app/runtime/ZaraTextClientActor.kt
android/app/src/main/java/ai/zara/app/runtime/ZaraTextCodec.kt
android/app/src/main/java/ai/zara/app/runtime/ZaraVoiceHelloCodec.kt
android/app/src/main/java/ai/zara/app/samsunghealth/SamsungHealthAndroidPlugin.kt
android/app/src/main/java/ai/zara/app/samsunghealth/SamsungHealthPlugin.kt
android/app/src/main/java/ai/zara/app/ui/AppNavigation.kt
android/app/src/main/java/ai/zara/app/ui/AssistantSetupGuidance.kt
android/app/src/main/java/ai/zara/app/ui/LocalEmbeddingPreferenceStore.kt
android/app/src/main/java/ai/zara/app/ui/ProjectsSurface.kt
android/app/src/main/java/ai/zara/app/ui/PrologStudioSurface.kt
android/app/src/main/java/ai/zara/app/ui/RuntimeModePreferenceStore.kt
android/app/src/main/java/ai/zara/app/ui/ThemePreferenceStore.kt
android/app/src/main/java/ai/zara/app/ui/UiOperationFailure.kt
android/app/src/main/java/ai/zara/app/ui/WatchSetupSurface.kt
android/app/src/main/java/ai/zara/app/ui/ZaraApp.kt
android/app/src/main/java/ai/zara/app/ui/ZaraNavigationBars.kt
android/app/src/main/java/ai/zara/app/update/AndroidUpdateManager.kt
android/app/src/main/java/ai/zara/app/update/Changelog.kt
android/app/src/main/java/ai/zara/app/update/UpdateInstallReceiver.kt
android/app/src/main/java/ai/zara/app/update/UpdateSecurity.kt
android/app/src/main/java/ai/zara/app/voice/AndroidAudioFocusPlatform.kt
android/app/src/main/java/ai/zara/app/voice/AndroidAudioRoutePlatform.kt
android/app/src/main/java/ai/zara/app/voice/AudioFocusController.kt
android/app/src/main/java/ai/zara/app/voice/AudioRouteController.kt
android/app/src/main/java/ai/zara/app/voice/ManualVoiceCapture.kt
android/app/src/main/java/ai/zara/app/voice/ManualVoiceSessionCoordinator.kt
android/app/src/main/java/ai/zara/app/voice/PushToTalkController.kt
android/app/src/main/java/ai/zara/app/voice/VoiceDiagnosticFailure.kt
android/app/src/main/java/ai/zara/app/voice/VoicePlaybackController.kt
android/app/src/main/java/ai/zara/app/voice/VoiceRuntimeSessionPolicy.kt
android/app/src/main/java/ai/zara/app/voice/VoiceStreamReducer.kt
android/app/src/main/java/ai/zara/app/voice/VoiceStreamSinkActor.kt
android/app/src/main/java/ai/zara/app/voice/ZaraVoiceAckCodec.kt
android/app/src/main/java/ai/zara/app/voice/ZaraVoiceStreamCodec.kt
android/app/src/main/java/ai/zara/app/watch/BluetoothWatchScanner.kt
android/app/src/main/java/ai/zara/app/watch/WatchAdbConnection.kt
android/app/src/main/java/ai/zara/app/watch/WatchAdbIdentity.kt
android/app/src/main/java/ai/zara/app/watch/WatchAdbTransfer.kt
android/app/src/main/java/ai/zara/app/watch/WatchDebugDiscovery.kt
android/app/src/main/java/ai/zara/app/watch/WatchInstallPolicy.kt
android/app/src/main/java/ai/zara/app/watch/WatchSetupActivity.kt
android/app/src/main/java/ai/zara/app/watch/WatchSetupController.kt
android/app/src/main/java/ai/zara/app/watch/WatchSetupState.kt
android/app/src/main/java/ai/zara/app/watch/WearApkRepository.kt
android/app/src/main/java/ai/zara/app/watch/WearNodeScanner.kt
android/app/src/main/res/drawable/ic_zara_foreground.xml
android/app/src/main/res/mipmap-anydpi-v26/ic_launcher.xml
android/app/src/main/res/values/strings.xml
android/app/src/main/res/values/zara_icon_colors.xml
android/app/src/main/res/xml/recognition_service.xml
android/app/src/main/res/xml/voice_interaction_service.xml
android/app/src/main/res/xml/zara_accessibility_service.xml
android/app/src/samsungHealthSdk/java/ai/zara/app/samsunghealth/sdk/SamsungHealthSdkGateway.kt
android/app/src/test/java/ai/zara/app/LocalNaturalLanguageFallbackTest.kt
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
android/app/src/test/java/ai/zara/app/automation/AutomationManifestContractTest.kt
android/app/src/test/java/ai/zara/app/conversations/ConversationStoreTest.kt
android/app/src/test/java/ai/zara/app/device/AndroidUriLauncherContractTest.kt
android/app/src/test/java/ai/zara/app/device/AppSearchAdapterTest.kt
android/app/src/test/java/ai/zara/app/device/DeviceCapabilityRegistryTest.kt
android/app/src/test/java/ai/zara/app/device/OpenAppAdapterTest.kt
android/app/src/test/java/ai/zara/app/device/OpenAppWiringContractTest.kt
android/app/src/test/java/ai/zara/app/device/OpenUriAdapterTest.kt
android/app/src/test/java/ai/zara/app/device/OpenUriPolicyTest.kt
android/app/src/test/java/ai/zara/app/diagnostics/LocalRuntimeDiagnosticsTest.kt
android/app/src/test/java/ai/zara/app/history/PortableConversationHistoryTest.kt
android/app/src/test/java/ai/zara/app/launcher/LauncherCatalogTest.kt
android/app/src/test/java/ai/zara/app/localai/EmbeddedLocalAiContractTest.kt
android/app/src/test/java/ai/zara/app/localai/LocalAiProviderContractTest.kt
android/app/src/test/java/ai/zara/app/localai/LocalAiRuntimeTest.kt
android/app/src/test/java/ai/zara/app/localai/LocalHybridRoutingContractTest.kt
android/app/src/test/java/ai/zara/app/localai/LocalModelStoreTest.kt
android/app/src/test/java/ai/zara/app/projects/ProjectContextStoreTest.kt
android/app/src/test/java/ai/zara/app/prolog/AndroidAutomationPlanParserTest.kt
android/app/src/test/java/ai/zara/app/prolog/AndroidAutomationRunnerTest.kt
android/app/src/test/java/ai/zara/app/prolog/AndroidKnowledgeBaseTest.kt
android/app/src/test/java/ai/zara/app/prolog/GitConfigTemplateImporterContractTest.kt
android/app/src/test/java/ai/zara/app/prolog/NativeTreallaBridgeTest.kt
android/app/src/test/java/ai/zara/app/prolog/NativeTreallaSourceContractTest.kt
android/app/src/test/java/ai/zara/app/prolog/PrologStudioTest.kt
android/app/src/test/java/ai/zara/app/prolog/TreallaSemanticRuntimeTest.kt
android/app/src/test/java/ai/zara/app/runtime/AndroidProjectConversationRoutingTest.kt
android/app/src/test/java/ai/zara/app/runtime/AndroidReconnectSchedulerFailureTest.kt
android/app/src/test/java/ai/zara/app/runtime/AndroidTextSessionControllerTest.kt
android/app/src/test/java/ai/zara/app/runtime/AndroidTextSessionRestartTest.kt
android/app/src/test/java/ai/zara/app/runtime/ClientStateStoreTest.kt
android/app/src/test/java/ai/zara/app/runtime/ConnectionFailureReasonTest.kt
android/app/src/test/java/ai/zara/app/runtime/LocalZaraServerTest.kt
android/app/src/test/java/ai/zara/app/runtime/RuntimeRegistryV1Test.kt
android/app/src/test/java/ai/zara/app/runtime/RuntimeStateTest.kt
android/app/src/test/java/ai/zara/app/runtime/StockZaraServerInteropTest.kt
android/app/src/test/java/ai/zara/app/runtime/StrictLocalRemoteSuspensionTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraCapabilityCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraDeviceActionCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraDeviceActionCodecTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientCapabilitiesTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientDeviceActionTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraVoiceHelloCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/samsunghealth/SamsungHealthApplicationWiringContractTest.kt
android/app/src/test/java/ai/zara/app/samsunghealth/SamsungHealthPluginTest.kt
android/app/src/test/java/ai/zara/app/security/AndroidProductionLoggingContractTest.kt
android/app/src/test/java/ai/zara/app/ui/AndroidPrologStudioContractTest.kt
android/app/src/test/java/ai/zara/app/ui/AppNavigationContract.kt
android/app/src/test/java/ai/zara/app/ui/AppNavigationTest.kt
android/app/src/test/java/ai/zara/app/ui/AppNavigationWiringContract.kt
android/app/src/test/java/ai/zara/app/ui/ConversationHistoryWiringContractTest.kt
android/app/src/test/java/ai/zara/app/ui/ProjectsWiringContractTest.kt
android/app/src/test/java/ai/zara/app/ui/RuntimeModePreferenceStoreTest.kt
android/app/src/test/java/ai/zara/app/ui/ThemePreferenceStoreTest.kt
android/app/src/test/java/ai/zara/app/ui/UiOperationFailureTest.kt
android/app/src/test/java/ai/zara/app/ui/WearFoundationContractTest.kt
android/app/src/test/java/ai/zara/app/ui/WearVoiceAppContractTest.kt
android/app/src/test/java/ai/zara/app/ui/ZaraAppProjectionTest.kt
android/app/src/test/java/ai/zara/app/update/ChangelogTest.kt
android/app/src/test/java/ai/zara/app/update/UpdateManagerContractTest.kt
android/app/src/test/java/ai/zara/app/update/UpdateSecurityTest.kt
android/app/src/test/java/ai/zara/app/voice/AudioFocusControllerTest.kt
android/app/src/test/java/ai/zara/app/voice/AudioFocusReleaseFailureTest.kt
android/app/src/test/java/ai/zara/app/voice/AudioFocusSynchronousLossTest.kt
android/app/src/test/java/ai/zara/app/voice/AudioRouteControllerTest.kt
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
android/app/src/test/java/ai/zara/app/voice/VoiceStreamReducerTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamSinkActorTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamSinkFailureStateTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamSinkObserverFailureTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamSinkSelfCloseTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceAckCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceStreamCodecTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceStreamPayloadLimitTest.kt
android/app/src/test/java/ai/zara/app/watch/WatchInstallPolicyTest.kt
android/app/src/test/java/ai/zara/app/watch/WatchInstallerContractTest.kt
android/build.gradle.kts
android/code-editor/build.gradle.kts
android/code-editor/src/main/AndroidManifest.xml
android/code-editor/src/main/java/ai/zara/code/editor/AndroidSpeechInput.kt
android/code-editor/src/main/java/ai/zara/code/editor/CodeTreeRepository.kt
android/code-editor/src/main/java/ai/zara/code/editor/MainActivity.kt
android/code-editor/src/test/java/ai/zara/code/editor/EditorStateSyncTest.kt
android/design/reference-2026-09-07.svg
android/design/zara-launcher-icon.svg
android/editor-core/build.gradle.kts
android/editor-core/src/main/java/ai/zara/editor/core/EditorCore.kt
android/editor-core/src/main/java/ai/zara/editor/core/SpokenCode.kt
android/editor-core/src/test/java/ai/zara/editor/core/EditorCoreTest.kt
android/editor-core/src/test/java/ai/zara/editor/core/SpokenCodeTest.kt
android/gradle/libs.versions.toml
android/integration/device_acceptance.py
android/integration/stock_zara_server_fixture.py
android/settings.gradle.kts
android/shared-ui/build.gradle.kts
android/shared-ui/src/main/java/ai/zara/ui/theme/ZaraTheme.kt
android/shared-ui/src/test/java/ai/zara/ui/theme/ZaraThemeTest.kt
android/wear-app/build.gradle.kts
android/wear-app/src/main/AndroidManifest.xml
android/wear-app/src/main/java/ai/zara/wear/WearMainActivity.kt
android/wear-app/src/main/res/values/wear.xml
android/wear-voice/build.gradle.kts
android/wear-voice/src/main/AndroidManifest.xml
android/wear-voice/src/main/java/ai/zara/wear/voice/WearVoiceActivity.kt
contracts/zara-runtime-v1/README.md
contracts/zara-runtime-v1/descriptors.tsv
contracts/zara-runtime-v1/runtime-descriptor.schema.json
docs/development.org
ideas.org
kb/config.pl
kb/intents.pl
main.pl
modules/config_loader.pl
modules/todo_expert.pl
planning/backlog.pl
rage/160-semantic-first-runtime.org
rage/172-android-native-adapter.org
rage/174-android-device-capabilities.org
rage/174-android-open-app-aliases.org
rage/175-android-audio-focus-lifecycle.org
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
rage/196-android-assistant-role.org
rage/196-ui-closed-runtime.org
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
rage/29-streaming-tts-provider-recovery-r10.org
rage/29-streaming-tts-recovery-r7.org
rage/324-expanded-history-sidebar-r2.org
rage/324-unified-copilot-r2.org
rage/324-unified-copilot-research-r2.org
rage/326-desktop-toggle.org
rage/371-plugin-approval-contract.org
rage/388-plugin-cancellation-r16.org
rage/388-plugin-cancellation-r17.org
rage/388-plugin-cancellation-r18.org
rage/492-device-action-replay-r3.org
rage/575-gateway-send-diagnostics.org
rage/575-stock-interop-diagnostics.org
rage/575-transient-send-backpressure-r3.org
rage/587-dictation-vulkan.org
rage/668-config-loader-diagnostic.org
rage/669-turn-event-loss.org
rage/866-wear-foundation.org
rage/867-wear-voice.org
rage/880-882-voice-pipeline-design.org
rage/880-882-voice-pipeline-merge-closeout.org
rage/880-882-voice-pipeline-research.org
rage/880-882-voice-pipeline.org
rage/895-android-prolog-ide.org
rage/android-three-menu-navigation.org
rage/client-connection-guards.org
scripts/check-android-apk-signer.sh
scripts/import-backlog.py
scripts/pair-android-qr.sh
scripts/pair-android.sh
scripts/pair-watch.sh
scripts/stt-phrase-benchmark.py
scripts/test-all.sh
scripts/test-android-device.sh
scripts/test-android-release.sh
scripts/test-android-semantic-parity.sh
scripts/test-android.sh
scripts/test-pair-android-qr.sh
scripts/test-s1-mini-normalizer.sh
scripts/test-streaming-tts.sh
scripts/validate-ui-evidence.py
scripts/version-context.py
setup.py
skills/zara-android-release/SKILL.md
skills/zara-android-release/agents/openai.yaml
t/fixtures/intents.expected
t/intents.pl
t/prolog_config.pl
t/test_adaptive_copilot.py
t/test_android_acceptance_overlay_order.py
t/test_android_device_acceptance_uiautomator.py
t/test_android_emulator_sdk_retry_contract.py
t/test_android_gate_diagnostics.py
t/test_android_gate_diagnostics_contract.py
t/test_android_local_history_recovery.py
t/test_android_release_contract.py
t/test_android_release_notes_race.py
t/test_android_three_menu_device_acceptance.py
t/test_app_package_profiles.py
t/test_audio_shared_input.py
t/test_backlog_import.py
t/test_changelog.py
t/test_cli_semantic_modes.py
t/test_client_connection_resolution.py
t/test_conversation_portability_hardening.py
t/test_conversation_schema_portable.py
t/test_conversation_store.py
t/test_copilot_controller_collapse.py
t/test_copilot_screenshot_ci.py
t/test_copilot_screenshot_fixtures.py
t/test_cross_platform_evidence_gate.py
t/test_daemon_client_config.py
t/test_daemon_connection_guards.py
t/test_desktop_control.py
t/test_desktop_launch_surface.py
t/test_desktop_shell.py
t/test_desktop_theme.py
t/test_desktop_toggle_control.py
t/test_device_action_replay_contract.py
t/test_device_action_sequence_wiring.py
t/test_dictation_vulkan_backend.py
t/test_org_automation_contract.py
t/test_org_automation_run_contract.py
t/test_org_foundation_invariants.py
t/test_org_todo_recursive_roots.py
t/test_org_todo_subtrees.py
t/test_org_todos.py
t/test_plugin_backend_composition.py
t/test_plugin_capability_authorization_cancellation.py
t/test_plugin_capability_composition.py
t/test_plugin_host_cancellation.py
t/test_plugin_tool_approval.py
t/test_plugin_tool_approval_live_policy.py
t/test_plugin_tool_cancellation_r18.py
t/test_plugin_unavailable_start.py
t/test_production_secure_listener.py
t/test_programmable_symbol_registry.py
t/test_programmable_symbol_registry_reload_kind.py
t/test_pulse_output_stream.py
t/test_quick_copilot.py
t/test_qwen_openai_client.py
t/test_runtime_intent_routing.py
t/test_runtime_registry_v1.py
t/test_s1_mini_normalizer.py
t/test_s1_mini_numeric_bounds.py
t/test_semantic_first_runtime.py
t/test_service_plugin_symbols.py
t/test_stt_beam_plumbing.py
t/test_toolnode_dispatch_contract.py
t/test_transcript_normalization.py
t/test_transcript_normalization_config.py
t/test_transcript_normalization_selection.py
t/test_tts.py
t/test_tts_output_lifecycle.py
t/test_tts_provider_recovery.py
t/test_version_context.py
t/test_voice_runtime_ingress.py
t/test_wake_capture_stall.py
t/test_wake_daemon_client.py
t/test_wake_fail_closed.py
t/test_wake_import.py
t/test_wake_lifecycle.py
t/test_wake_principal_isolation.py
t/test_wake_speaker.py
t/test_wake_words.py
t/test_zmq_send_diagnostics.py
t/test_zmq_transient_backpressure.py
t/test_zmq_transport.py
t/todo_expert.pl
version.properties
wiki/android-automation.org
wiki/android-local-ai.org
wiki/android-navigation.org
wiki/android-projects.org
wiki/android-prolog-studio.org
wiki/android-samsung-health.org
wiki/android-watch-install.org
wiki/android.org
wiki/install.org
wiki/org-todos.org
wiki/plugins.org
zara/__main__.py
zara/agent/tool_cancellation.py
zara/agent/tools/registry.py
zara/agent/tools/todo_tools.py
zara/audio.py
zara/changelog.py
zara/config.py
zara/conversation_schema.py
zara/conversation_schema.sql
zara/daemon_client.py
zara/desktop/app.py
zara/desktop/chat_widgets.py
zara/desktop/control.py
zara/desktop/controller.py
zara/desktop/conversation/store.py
zara/desktop/theme.py
zara/desktop/ui_fixtures.py
zara/desktop/windows/__init__.py
zara/desktop/windows/copilot.py
zara/desktop/windows/quick.py
zara/device_action_replay.py
zara/dictate.py
zara/org_automation.py
zara/org_automation_run.py
zara/org_todos.py
zara/plugins/__init__.py
zara/plugins/api.py
zara/plugins/manager.py
zara/protocol.py
zara/python_skills.py
zara/runtime/__init__.py
zara/runtime/backend.py
zara/runtime/host.py
zara/runtime/package_profiles.py
zara/runtime/registry.py
zara/runtime/symbols.py
zara/runtime/tts_output.py
zara/runtime/turn_context.py
zara/s1_mini_normalizer.py
zara/server.py
zara/streaming_stt.py
zara/todo_skills.py
zara/transcript_normalization.py
zara/transcript_normalization_config.py
zara/transcript_normalization_selection.py
zara/tts/engine.py
zara/tts/qwen.py
zara/version_context.py
zara/voice_runtime.py
zara/wake.py
zara/wake_daemon.py
zara/wake_words.py
zara/zmq_transport.py
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/android-latest.yml
.github/workflows/ci.yml
.github/workflows/rage-575-apply-green.yml
.github/workflows/release-v0.1.0-alpha.yml
.github/workflows/release.yml
android/app/src/test/java/ai/zara/app/LocalNaturalLanguageFallbackTest.kt
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
android/app/src/test/java/ai/zara/app/automation/AutomationManifestContractTest.kt
android/app/src/test/java/ai/zara/app/conversations/ConversationStoreTest.kt
android/app/src/test/java/ai/zara/app/device/AndroidUriLauncherContractTest.kt
android/app/src/test/java/ai/zara/app/device/AppSearchAdapterTest.kt
android/app/src/test/java/ai/zara/app/device/DeviceCapabilityRegistryTest.kt
android/app/src/test/java/ai/zara/app/device/OpenAppAdapterTest.kt
android/app/src/test/java/ai/zara/app/device/OpenAppWiringContractTest.kt
android/app/src/test/java/ai/zara/app/device/OpenUriAdapterTest.kt
android/app/src/test/java/ai/zara/app/device/OpenUriPolicyTest.kt
android/app/src/test/java/ai/zara/app/diagnostics/LocalRuntimeDiagnosticsTest.kt
android/app/src/test/java/ai/zara/app/history/PortableConversationHistoryTest.kt
android/app/src/test/java/ai/zara/app/launcher/LauncherCatalogTest.kt
android/app/src/test/java/ai/zara/app/localai/EmbeddedLocalAiContractTest.kt
android/app/src/test/java/ai/zara/app/localai/LocalAiProviderContractTest.kt
android/app/src/test/java/ai/zara/app/localai/LocalAiRuntimeTest.kt
android/app/src/test/java/ai/zara/app/localai/LocalHybridRoutingContractTest.kt
android/app/src/test/java/ai/zara/app/localai/LocalModelStoreTest.kt
android/app/src/test/java/ai/zara/app/projects/ProjectContextStoreTest.kt
android/app/src/test/java/ai/zara/app/prolog/AndroidAutomationPlanParserTest.kt
android/app/src/test/java/ai/zara/app/prolog/AndroidAutomationRunnerTest.kt
android/app/src/test/java/ai/zara/app/prolog/AndroidKnowledgeBaseTest.kt
android/app/src/test/java/ai/zara/app/prolog/GitConfigTemplateImporterContractTest.kt
android/app/src/test/java/ai/zara/app/prolog/NativeTreallaBridgeTest.kt
android/app/src/test/java/ai/zara/app/prolog/NativeTreallaSourceContractTest.kt
android/app/src/test/java/ai/zara/app/prolog/PrologStudioTest.kt
android/app/src/test/java/ai/zara/app/prolog/TreallaSemanticRuntimeTest.kt
android/app/src/test/java/ai/zara/app/runtime/AndroidProjectConversationRoutingTest.kt
android/app/src/test/java/ai/zara/app/runtime/AndroidReconnectSchedulerFailureTest.kt
android/app/src/test/java/ai/zara/app/runtime/AndroidTextSessionControllerTest.kt
android/app/src/test/java/ai/zara/app/runtime/AndroidTextSessionRestartTest.kt
android/app/src/test/java/ai/zara/app/runtime/ClientStateStoreTest.kt
android/app/src/test/java/ai/zara/app/runtime/ConnectionFailureReasonTest.kt
android/app/src/test/java/ai/zara/app/runtime/LocalZaraServerTest.kt
android/app/src/test/java/ai/zara/app/runtime/RuntimeRegistryV1Test.kt
android/app/src/test/java/ai/zara/app/runtime/RuntimeStateTest.kt
android/app/src/test/java/ai/zara/app/runtime/StockZaraServerInteropTest.kt
android/app/src/test/java/ai/zara/app/runtime/StrictLocalRemoteSuspensionTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraCapabilityCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraDeviceActionCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraDeviceActionCodecTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientCapabilitiesTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextClientDeviceActionTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraTextCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/runtime/ZaraVoiceHelloCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/samsunghealth/SamsungHealthApplicationWiringContractTest.kt
android/app/src/test/java/ai/zara/app/samsunghealth/SamsungHealthPluginTest.kt
android/app/src/test/java/ai/zara/app/security/AndroidProductionLoggingContractTest.kt
android/app/src/test/java/ai/zara/app/ui/AndroidPrologStudioContractTest.kt
android/app/src/test/java/ai/zara/app/ui/AppNavigationContract.kt
android/app/src/test/java/ai/zara/app/ui/AppNavigationTest.kt
android/app/src/test/java/ai/zara/app/ui/AppNavigationWiringContract.kt
android/app/src/test/java/ai/zara/app/ui/ConversationHistoryWiringContractTest.kt
android/app/src/test/java/ai/zara/app/ui/ProjectsWiringContractTest.kt
android/app/src/test/java/ai/zara/app/ui/RuntimeModePreferenceStoreTest.kt
android/app/src/test/java/ai/zara/app/ui/ThemePreferenceStoreTest.kt
android/app/src/test/java/ai/zara/app/ui/UiOperationFailureTest.kt
android/app/src/test/java/ai/zara/app/ui/WearFoundationContractTest.kt
android/app/src/test/java/ai/zara/app/ui/WearVoiceAppContractTest.kt
android/app/src/test/java/ai/zara/app/ui/ZaraAppProjectionTest.kt
android/app/src/test/java/ai/zara/app/update/ChangelogTest.kt
android/app/src/test/java/ai/zara/app/update/UpdateManagerContractTest.kt
android/app/src/test/java/ai/zara/app/update/UpdateSecurityTest.kt
android/app/src/test/java/ai/zara/app/voice/AudioFocusControllerTest.kt
android/app/src/test/java/ai/zara/app/voice/AudioFocusReleaseFailureTest.kt
android/app/src/test/java/ai/zara/app/voice/AudioFocusSynchronousLossTest.kt
android/app/src/test/java/ai/zara/app/voice/AudioRouteControllerTest.kt
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
android/app/src/test/java/ai/zara/app/voice/VoiceStreamReducerTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamSinkActorTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamSinkFailureStateTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamSinkObserverFailureTest.kt
android/app/src/test/java/ai/zara/app/voice/VoiceStreamSinkSelfCloseTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceAckCodecDepthTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceStreamCodecTest.kt
android/app/src/test/java/ai/zara/app/voice/ZaraVoiceStreamPayloadLimitTest.kt
android/app/src/test/java/ai/zara/app/watch/WatchInstallPolicyTest.kt
android/app/src/test/java/ai/zara/app/watch/WatchInstallerContractTest.kt
android/code-editor/src/test/java/ai/zara/code/editor/EditorStateSyncTest.kt
android/editor-core/src/test/java/ai/zara/editor/core/EditorCoreTest.kt
android/editor-core/src/test/java/ai/zara/editor/core/SpokenCodeTest.kt
android/shared-ui/src/test/java/ai/zara/ui/theme/ZaraThemeTest.kt
scripts/check-android-apk-signer.sh
scripts/import-backlog.py
scripts/pair-android-qr.sh
scripts/pair-android.sh
scripts/pair-watch.sh
scripts/stt-phrase-benchmark.py
scripts/test-all.sh
scripts/test-android-device.sh
scripts/test-android-release.sh
scripts/test-android-semantic-parity.sh
scripts/test-android.sh
scripts/test-pair-android-qr.sh
scripts/test-s1-mini-normalizer.sh
scripts/test-streaming-tts.sh
scripts/validate-ui-evidence.py
scripts/version-context.py
t/fixtures/intents.expected
t/intents.pl
t/prolog_config.pl
t/test_adaptive_copilot.py
t/test_android_acceptance_overlay_order.py
t/test_android_device_acceptance_uiautomator.py
t/test_android_emulator_sdk_retry_contract.py
t/test_android_gate_diagnostics.py
t/test_android_gate_diagnostics_contract.py
t/test_android_local_history_recovery.py
t/test_android_release_contract.py
t/test_android_release_notes_race.py
t/test_android_three_menu_device_acceptance.py
t/test_app_package_profiles.py
t/test_audio_shared_input.py
t/test_backlog_import.py
t/test_changelog.py
t/test_cli_semantic_modes.py
t/test_client_connection_resolution.py
t/test_conversation_portability_hardening.py
t/test_conversation_schema_portable.py
t/test_conversation_store.py
t/test_copilot_controller_collapse.py
t/test_copilot_screenshot_ci.py
t/test_copilot_screenshot_fixtures.py
t/test_cross_platform_evidence_gate.py
t/test_daemon_client_config.py
t/test_daemon_connection_guards.py
t/test_desktop_control.py
t/test_desktop_launch_surface.py
t/test_desktop_shell.py
t/test_desktop_theme.py
t/test_desktop_toggle_control.py
t/test_device_action_replay_contract.py
t/test_device_action_sequence_wiring.py
t/test_dictation_vulkan_backend.py
t/test_org_automation_contract.py
t/test_org_automation_run_contract.py
t/test_org_foundation_invariants.py
t/test_org_todo_recursive_roots.py
t/test_org_todo_subtrees.py
t/test_org_todos.py
t/test_plugin_backend_composition.py
t/test_plugin_capability_authorization_cancellation.py
t/test_plugin_capability_composition.py
t/test_plugin_host_cancellation.py
t/test_plugin_tool_approval.py
t/test_plugin_tool_approval_live_policy.py
t/test_plugin_tool_cancellation_r18.py
t/test_plugin_unavailable_start.py
t/test_production_secure_listener.py
t/test_programmable_symbol_registry.py
t/test_programmable_symbol_registry_reload_kind.py
t/test_pulse_output_stream.py
t/test_quick_copilot.py
t/test_qwen_openai_client.py
t/test_runtime_intent_routing.py
t/test_runtime_registry_v1.py
t/test_s1_mini_normalizer.py
t/test_s1_mini_numeric_bounds.py
t/test_semantic_first_runtime.py
t/test_service_plugin_symbols.py
t/test_stt_beam_plumbing.py
t/test_toolnode_dispatch_contract.py
t/test_transcript_normalization.py
t/test_transcript_normalization_config.py
t/test_transcript_normalization_selection.py
t/test_tts.py
t/test_tts_output_lifecycle.py
t/test_tts_provider_recovery.py
t/test_version_context.py
t/test_voice_runtime_ingress.py
t/test_wake_capture_stall.py
t/test_wake_daemon_client.py
t/test_wake_fail_closed.py
t/test_wake_import.py
t/test_wake_lifecycle.py
t/test_wake_principal_isolation.py
t/test_wake_speaker.py
t/test_wake_words.py
t/test_zmq_send_diagnostics.py
t/test_zmq_transient_backpressure.py
t/test_zmq_transport.py
t/todo_expert.pl
```
