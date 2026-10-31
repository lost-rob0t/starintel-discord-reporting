# lost-rob0t/zara

- generated: `2026-10-31T23:25:58Z`
- canonical branch: `master`
- changelog eligible: `yes`
- head: [`034d6b23077b543cb5d2ed8b177411bd5179ac4a`](https://github.com/lost-rob0t/zara/commit/034d6b23077b543cb5d2ed8b177411bd5179ac4a)
- head date: `2026-10-18T21:05:36-04:00`
- head subject: Merge PR #1524: retain copyable Android chat error details

## Git log, last 14 days

```text
2026-10-18 034d6b23077b543cb5d2ed8b177411bd5179ac4a Merge PR #1524: retain copyable Android chat error details
2026-10-18 1a83ec47988a625eee89a5ca6912c0af49b66efd test(android): reveal remote reply after retained error history #1523
2026-10-18 9618ca6ef3148ce5307f251c3c877f9acdd51f5d test(android): reveal completed recovery reply before asserting #1523
2026-10-18 9efd3767871bc8d1132b51167e468d7ceb5d3fa0 fix(test): install Android instrumentation APK with test-only flag
2026-10-18 60d3fd67f29d9b1ea018f5628a8ef3644849a78e test(android): require diagnostic payload in failed-turn persistence wiring
2026-10-18 d012851d863cb775f395c7b1a83608f56c39b0e9 fix(android): forward error copy through pairing-enabled chat shell
2026-10-18 5b87bd18e18c6a7cc8593276f5d9390a841ca434 fix(test): preserve executable Android acceptance runner
2026-10-18 c3bcd1b395559221c869dbb2d89bf0f7a7513174 test(android): prove restored error details reach the real clipboard
2026-10-18 7ed1457bfd930dde87ffebc3d8adce7649c1ee5c fix(android): retain copyable diagnostics beneath failed chat messages (#1523)
```

## Repository paths changed, last 14 days

```text
CHANGELOG.md
android/app/src/androidTest/java/ai/zara/app/ui/ChatErrorClipboardInstrumentedTest.kt
android/app/src/main/java/ai/zara/app/AndroidAppSession.kt
android/app/src/main/java/ai/zara/app/MainActivity.kt
android/app/src/main/java/ai/zara/app/conversations/ConversationStore.kt
android/app/src/main/java/ai/zara/app/diagnostics/ChatErrorDetails.kt
android/app/src/main/java/ai/zara/app/runtime/ZaraTextClientActor.kt
android/app/src/main/java/ai/zara/app/telemetry/ClientEventJournal.kt
android/app/src/main/java/ai/zara/app/telemetry/SessionTelemetry.kt
android/app/src/main/java/ai/zara/app/ui/PairingZaraApp.kt
android/app/src/main/java/ai/zara/app/ui/ZaraApp.kt
android/app/src/test/java/ai/zara/app/conversations/ConversationErrorDetailsTest.kt
android/app/src/test/java/ai/zara/app/diagnostics/ChatErrorDetailsTest.kt
android/app/src/test/java/ai/zara/app/diagnostics/ChatErrorWiringTest.kt
android/app/src/test/java/ai/zara/app/telemetry/SessionTelemetryTest.kt
android/app/src/test/java/ai/zara/app/ui/ConversationHistoryWiringContractTest.kt
android/integration/chat_error_acceptance.py
android/integration/device_acceptance.py
android/integration/device_remote_acceptance.py
rage/1523-chat-error-details-20261018.org
scripts/test-android-emulator-install.sh
t/test_android_chat_error_acceptance.py
t/test_android_device_acceptance_uiautomator.py
t/test_android_remote_acceptance_packaging.py
wiki/android.org
```

## Test and CI paths touched, last 14 days

```text
android/app/src/test/java/ai/zara/app/conversations/ConversationErrorDetailsTest.kt
android/app/src/test/java/ai/zara/app/diagnostics/ChatErrorDetailsTest.kt
android/app/src/test/java/ai/zara/app/diagnostics/ChatErrorWiringTest.kt
android/app/src/test/java/ai/zara/app/telemetry/SessionTelemetryTest.kt
android/app/src/test/java/ai/zara/app/ui/ConversationHistoryWiringContractTest.kt
scripts/test-android-emulator-install.sh
t/test_android_chat_error_acceptance.py
t/test_android_device_acceptance_uiautomator.py
t/test_android_remote_acceptance_packaging.py
```
