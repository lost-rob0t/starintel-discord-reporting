# lost-rob0t/zara

- generated: `2026-10-10T18:40:05Z`
- canonical branch: `master`
- changelog eligible: `yes`
- head: [`69f16070ecba35c12a7d4df6503c3a3f30bf9e1e`](https://github.com/lost-rob0t/zara/commit/69f16070ecba35c12a7d4df6503c3a3f30bf9e1e)
- head date: `2026-10-04T01:25:00-04:00`
- head subject: Merge pull request #1500 from lost-rob0t/feat/desktop-prolog-ide

## Git log, last 14 days

```text
2026-10-04 69f16070ecba35c12a7d4df6503c3a3f30bf9e1e Merge pull request #1500 from lost-rob0t/feat/desktop-prolog-ide
2026-10-04 aa6ea0a634fd41d8c88795018e4f14b34bc954bb feat(desktop): add full Prolog IDE workspace
2026-10-03 b14b1ebef8867dcf1f97482377cdd35d80ef5714 Merge pull request #1499 from lost-rob0t/rage/1333-desktop-android-ui-parity
2026-10-03 2d34d93f1c86211f34412f9e5d786e34f03898a4 Refresh desktop UI from Android design
2026-10-03 a0b661ffacb885607d972ac8eeddcdcfa4777866 Merge pull request #1498 from lost-rob0t/codex/zara-health-phone-watch
2026-10-03 cc5be4aee9caa246a9cda5662748b3b5ddd353bd feat: add Zara Health goal complications
2026-10-03 3db0c101beaa2e847b4fe970eea654f701bb5bcb chore: promote Zara 0.4.0-alpha
2026-10-03 a2487b33c43c53543ea9c4b57a2ce544e4358b09 feat: add secure Zara Health phone and Wear surfaces
2026-09-27 74728fa899e937fb43a9f618c8223137832b09b5 Merge pull request #1463 from lost-rob0t/agentic15/1396-session-demux-hardening
```

## Repository paths changed, last 14 days

```text
.github/workflows/android-latest.yml
.github/workflows/ci.yml
.github/workflows/release.yml
.prolog/kb/desktop_copilot_ui.pl
.prolog/kb/desktop_prolog_ide.pl
.prolog/kb/index.pl
CHANGELOG.md
android/.gitignore
android/app/build.gradle.kts
android/app/src/main/AndroidManifest.xml
android/app/src/main/java/ai/zara/app/MainActivity.kt
android/app/src/main/java/ai/zara/app/samsunghealth/HealthGoalStore.kt
android/app/src/main/java/ai/zara/app/samsunghealth/HealthOpenPgpRecipientStore.kt
android/app/src/main/java/ai/zara/app/samsunghealth/HealthPrologExport.kt
android/app/src/main/java/ai/zara/app/samsunghealth/OpenPgpHealthExporter.kt
android/app/src/main/java/ai/zara/app/samsunghealth/SamsungHealthAndroidPlugin.kt
android/app/src/main/java/ai/zara/app/samsunghealth/SamsungHealthPlugin.kt
android/app/src/main/java/ai/zara/app/samsunghealth/SamsungHealthUiState.kt
android/app/src/main/java/ai/zara/app/ui/AppNavigation.kt
android/app/src/main/java/ai/zara/app/ui/PairingZaraApp.kt
android/app/src/main/java/ai/zara/app/ui/ZaraApp.kt
android/app/src/main/java/ai/zara/app/ui/ZaraHealthSurface.kt
android/app/src/main/java/ai/zara/app/watch/WearCompanionLinkService.kt
android/app/src/main/java/ai/zara/app/watch/WearCompanionProvisionSource.kt
android/app/src/main/res/xml/zara_file_paths.xml
android/app/src/samsungHealthSdk/java/ai/zara/app/samsunghealth/sdk/SamsungHealthSdkGateway.kt
android/app/src/test/java/ai/zara/app/samsunghealth/HealthGoalStoreTest.kt
android/app/src/test/java/ai/zara/app/samsunghealth/HealthOpenPgpRecipientStoreTest.kt
android/app/src/test/java/ai/zara/app/samsunghealth/HealthPrologExportTest.kt
android/app/src/test/java/ai/zara/app/samsunghealth/OpenPgpHealthExporterTest.kt
android/app/src/test/java/ai/zara/app/samsunghealth/SamsungHealthApplicationWiringContractTest.kt
android/app/src/test/java/ai/zara/app/samsunghealth/SamsungHealthPluginTest.kt
android/app/src/test/java/ai/zara/app/ui/AppNavigationContract.kt
android/app/src/test/java/ai/zara/app/ui/AppNavigationTest.kt
android/gradle/libs.versions.toml
android/shared-ui/src/main/java/ai/zara/ui/continuity/WearCompanionContract.kt
android/shared-ui/src/main/java/ai/zara/ui/health/ZaraHealthCatalog.kt
android/shared-ui/src/test/java/ai/zara/ui/continuity/WearCompanionContractTest.kt
android/shared-ui/src/test/java/ai/zara/ui/health/ZaraHealthCatalogTest.kt
android/wear-app/build.gradle.kts
android/wear-app/libs/README.md
android/wear-app/src/main/AndroidManifest.xml
android/wear-app/src/main/java/ai/zara/wear/WearCompanionClient.kt
android/wear-app/src/main/java/ai/zara/wear/WearCompanionLinkService.kt
android/wear-app/src/main/java/ai/zara/wear/WearMainActivity.kt
android/wear-app/src/main/java/ai/zara/wear/health/WearHealth.kt
android/wear-app/src/main/java/ai/zara/wear/health/ZaraHealthGoalComplicationService.kt
android/wear-app/src/main/java/ai/zara/wear/health/ZaraWearHealthSurface.kt
android/wear-app/src/samsungHealthSensorSdk/java/ai/zara/wear/health/sdk/SamsungHealthSensorGateway.kt
android/wear-app/src/test/java/ai/zara/wear/WearCompanionWiringContractTest.kt
android/wear-app/src/test/java/ai/zara/wear/WearHealthControllerTest.kt
android/wear-app/src/test/java/ai/zara/wear/ZaraHealthGoalComplicationTest.kt
main.pl
modules/health_reasoning.pl
rage/1333-desktop-android-ui-parity-design.org
rage/1333-desktop-android-ui-parity-research.org
rage/1333-desktop-android-ui-parity.org
server_main.pl
setup.py
t/health_reasoning.pl
t/test_android_release_contract.py
t/test_config.py
t/test_copilot_screenshot_fixtures.py
t/test_daemon_security_policy.py
t/test_desktop_mobile_parity.py
t/test_desktop_preferences.py
t/test_desktop_settings_window.py
t/test_desktop_theme.py
t/test_health_cli.py
t/test_health_store.py
t/test_org_desktop_screenshot_fixtures.py
t/test_packaging.py
t/test_protocol_runtime.py
t/test_runtime_host.py
t/test_runtime_intent_routing.py
t/test_zmq_transport.py
version.properties
wiki/android-samsung-health.org
wiki/desktop-design.org
zara/__main__.py
zara/config.py
zara/desktop/app.py
zara/desktop/controller.py
zara/desktop/org_fixtures.py
zara/desktop/prolog_studio.py
zara/desktop/theme.py
zara/desktop/ui_fixtures.py
zara/desktop/windows/copilot.py
zara/desktop/windows/quick.py
zara/desktop/windows/settings.py
zara/health_cli.py
zara/health_store.py
zara/protocol.py
zara/protocol_runtime.py
zara/runtime/backend.py
zara/runtime/commands.py
zara/runtime/host.py
zara/security_gateway.py
zara/zmq_transport.py
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/android-latest.yml
.github/workflows/ci.yml
.github/workflows/release.yml
android/app/src/test/java/ai/zara/app/samsunghealth/HealthGoalStoreTest.kt
android/app/src/test/java/ai/zara/app/samsunghealth/HealthOpenPgpRecipientStoreTest.kt
android/app/src/test/java/ai/zara/app/samsunghealth/HealthPrologExportTest.kt
android/app/src/test/java/ai/zara/app/samsunghealth/OpenPgpHealthExporterTest.kt
android/app/src/test/java/ai/zara/app/samsunghealth/SamsungHealthApplicationWiringContractTest.kt
android/app/src/test/java/ai/zara/app/samsunghealth/SamsungHealthPluginTest.kt
android/app/src/test/java/ai/zara/app/ui/AppNavigationContract.kt
android/app/src/test/java/ai/zara/app/ui/AppNavigationTest.kt
android/shared-ui/src/test/java/ai/zara/ui/continuity/WearCompanionContractTest.kt
android/shared-ui/src/test/java/ai/zara/ui/health/ZaraHealthCatalogTest.kt
android/wear-app/src/test/java/ai/zara/wear/WearCompanionWiringContractTest.kt
android/wear-app/src/test/java/ai/zara/wear/WearHealthControllerTest.kt
android/wear-app/src/test/java/ai/zara/wear/ZaraHealthGoalComplicationTest.kt
t/health_reasoning.pl
t/test_android_release_contract.py
t/test_config.py
t/test_copilot_screenshot_fixtures.py
t/test_daemon_security_policy.py
t/test_desktop_mobile_parity.py
t/test_desktop_preferences.py
t/test_desktop_settings_window.py
t/test_desktop_theme.py
t/test_health_cli.py
t/test_health_store.py
t/test_org_desktop_screenshot_fixtures.py
t/test_packaging.py
t/test_protocol_runtime.py
t/test_runtime_host.py
t/test_runtime_intent_routing.py
t/test_zmq_transport.py
```
