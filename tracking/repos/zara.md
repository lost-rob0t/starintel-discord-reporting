# lost-rob0t/zara

- generated: `2026-11-14T06:31:19Z`
- canonical branch: `master`
- changelog eligible: `yes`
- head: [`26ec30cd4a6356fe515ece94a90f657df2e50972`](https://github.com/lost-rob0t/zara/commit/26ec30cd4a6356fe515ece94a90f657df2e50972)
- head date: `2026-11-13T05:45:50-05:00`
- head subject: Merge pull request #1529 from lost-rob0t/fix/wear-voice-release-signing

## Git log, last 14 days

```text
2026-11-13 26ec30cd4a6356fe515ece94a90f657df2e50972 Merge pull request #1529 from lost-rob0t/fix/wear-voice-release-signing
2026-11-13 b28f0ca5acb7acdbd9f20467ff3b216dd27d585a fix(android): sign Wear Voice with the configured update key
2026-11-13 c14ba070b36dc14f7302cfa36260af329810cfbb Merge Android local setup and selectable update channels for 0.4.0-alpha (#1526)
2026-11-13 f9c8ea4e9d2c340d0b335a2e6a5e6f71cad246fe fix(ci): validate nested Android screenshot capture metadata
2026-11-13 5dc5c764f239099571d5e1495cdf4a101f59a12b test(android): find restored error actions in both vertical scroll directions
2026-11-13 da61d6fdb3f80662ebc215b913e191ce92d2952e test(android): reveal scrolled settings controls in installed acceptance
2026-11-13 27872dba8a600ef86622cbf6f92e0da107ca63e9 test(android): align recovery assertions with explicit menu-root navigation
2026-11-13 de36ad6f4e7fdfe29e777577da7176e448296a81 test(android): navigate remembered menu children before remote acceptance
2026-11-13 b03dd5fc108bf8b552cdb915ba4b36b1b48be987 feat(android): persist update channel and version selection for 0.4 release
2026-11-13 b0e55e7ad73e26f8ca005416e05c99c91740bc29 fix(android): reopen offline voice engines and repair local acceptance
```

## Repository paths changed, last 14 days

```text
CHANGELOG.md
android/app/src/androidTest/java/ai/zara/app/ui/ChatErrorClipboardInstrumentedTest.kt
android/app/src/androidTest/java/ai/zara/app/update/UpdateSelectionInstrumentedTest.kt
android/app/src/main/java/ai/zara/app/MainActivity.kt
android/app/src/main/java/ai/zara/app/localai/AndroidOfflineTtsBackend.kt
android/app/src/main/java/ai/zara/app/localai/IsolatedSpeechBackend.kt
android/app/src/main/java/ai/zara/app/localai/LocalAiService.kt
android/app/src/main/java/ai/zara/app/localai/LocalTtsContracts.kt
android/app/src/main/java/ai/zara/app/localai/OfflineSpeechSession.kt
android/app/src/main/java/ai/zara/app/ui/PairingZaraApp.kt
android/app/src/main/java/ai/zara/app/ui/ZaraApp.kt
android/app/src/main/java/ai/zara/app/update/AndroidUpdateManager.kt
android/app/src/main/java/ai/zara/app/update/UpdateCatalog.kt
android/app/src/main/java/ai/zara/app/update/UpdateSecurity.kt
android/app/src/test/java/ai/zara/app/localai/IsolatedSpeechBackendTest.kt
android/app/src/test/java/ai/zara/app/localai/OfflineSpeechSessionTest.kt
android/app/src/test/java/ai/zara/app/update/UpdateCatalogTest.kt
android/app/src/test/java/ai/zara/app/update/UpdateManagerContractTest.kt
android/integration/chat_error_acceptance.py
android/integration/device_acceptance.py
android/integration/device_remote_acceptance.py
android/integration/device_remote_recovery_acceptance.py
android/wear-voice/build.gradle.kts
scripts/test-android-emulator-install.sh
scripts/validate-ui-evidence.py
t/test_android_chat_error_acceptance.py
t/test_android_device_acceptance_uiautomator.py
t/test_android_release_contract.py
t/test_android_remote_recovery_settings_navigation.py
t/test_ui_evidence_org_gate.py
wiki/android-local-ai.org
```

## Test and CI paths touched, last 14 days

```text
android/app/src/test/java/ai/zara/app/localai/IsolatedSpeechBackendTest.kt
android/app/src/test/java/ai/zara/app/localai/OfflineSpeechSessionTest.kt
android/app/src/test/java/ai/zara/app/update/UpdateCatalogTest.kt
android/app/src/test/java/ai/zara/app/update/UpdateManagerContractTest.kt
scripts/test-android-emulator-install.sh
scripts/validate-ui-evidence.py
t/test_android_chat_error_acceptance.py
t/test_android_device_acceptance_uiautomator.py
t/test_android_release_contract.py
t/test_android_remote_recovery_settings_navigation.py
t/test_ui_evidence_org_gate.py
```
