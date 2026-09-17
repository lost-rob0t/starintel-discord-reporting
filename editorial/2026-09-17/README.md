# September 17, 2026: project changelogs and Android companions

Seventeen project updates paired with seventeen separately authored Android companion articles. The existing in-depth Zara and StarIntel Wear articles are retained; the expanded follow-ups add implementation and verification detail beyond the brief announcements.

Android articles distinguish native packages from backend integration guidance. Research and maintenance-status posts are labeled as such rather than presented as shipped runtime features.

| Project | Main article | Android companion |
|---|---|---|
| Zara | [Desktop and shared runtime](../../reports/starintel-updates-changelog/2026-09-17T05-57-14Z-report.md) | [Local/remote setup and APKs](../../reports/starintel-updates-changelog/2026-09-17-30-zara-android-special-report.md) |
| StarIntel Wear | [Watch experience and release](../../reports/starintel-updates-changelog/2026-09-17T05-57-15Z-report.md) | [Companion, signing and bootstrap](../../reports/starintel-updates-changelog/2026-09-17-31-starintel-wear-android-special-report.md) |
| Quasar | [Static web and hosted runtime](../../reports/starintel-updates-changelog/2026-09-17-14-quasar-runtime-report.md) | [Native phone client and installer](../../reports/starintel-updates-changelog/2026-09-17-32-quasar-android-special-report.md) |
| StarIntel Server | [Retention, settlement and telemetry](../../reports/starintel-updates-changelog/2026-09-17-10-starintel-server-report.md) | [Mobile operation identity](../../reports/starintel-updates-changelog/2026-09-17-33-starintel-server-android-special-report.md) |
| StarLang | [Actor transport and canonical numbers](../../reports/starintel-updates-changelog/2026-09-17-11-star-lang-report.md) | [Portable contracts versus runtime packaging](../../reports/starintel-updates-changelog/2026-09-17-34-star-lang-android-special-report.md) |
| Tek9 / star-git | [Snapshots, packs and custody](../../reports/starintel-updates-changelog/2026-09-17-12-tek9-star-git-report.md) | [Cache and archive-custody boundaries](../../reports/starintel-updates-changelog/2026-09-17-35-tek9-android-special-report.md) |
| Prolog-RLM | [Durable semantic project knowledge](../../reports/starintel-updates-changelog/2026-09-17-13-prolog-rlm-report.md) | [Provenance and partial coverage](../../reports/starintel-updates-changelog/2026-09-17-36-prolog-rlm-android-special-report.md) |
| Zara Plugins | [Error sanitization and transactional updates](../../reports/starintel-updates-changelog/2026-09-17-15-zara-plugins-report.md) | [Compatibility and coherent installation](../../reports/starintel-updates-changelog/2026-09-17-37-zara-plugins-android-special-report.md) |
| A0 Symbolics | [Distribution updates and upstream replay](../../reports/starintel-updates-changelog/2026-09-17-16-a0-symbolics-report.md) | [Client and host distribution identity](../../reports/starintel-updates-changelog/2026-09-17-38-a0-symbolics-android-special-report.md) |
| Hackmode | [Replay-checkpoint integrity](../../reports/starintel-updates-changelog/2026-09-17-17-hackmode-report.md) | [Evidence transfer and checkpoint identity](../../reports/starintel-updates-changelog/2026-09-17-39-hackmode-android-special-report.md) |
| LLM-Log | [Backfill, provenance and quota coverage](../../reports/starintel-updates-changelog/2026-09-17-18-llm-log-report.md) | [Missing usage versus zero usage](../../reports/starintel-updates-changelog/2026-09-17-40-llm-log-android-special-report.md) |
| StarIntel document profile | [Network-capture contract and manifest](../../reports/starintel-updates-changelog/2026-09-17-19-starintel-document-profile-report.md) | [References, redaction and mobile conformance](../../reports/starintel-updates-changelog/2026-09-17-41-document-profile-android-special-report.md) |
| StarIntel Skills | [Resolve the consumer's selected spec](../../reports/starintel-updates-changelog/2026-09-17-20-skills-report.md) | [Phone-consumer compatibility](../../reports/starintel-updates-changelog/2026-09-17-42-skills-android-special-report.md) |
| StarIntel Auto-Research | [Registry and routing ownership clarification](../../reports/starintel-updates-changelog/2026-09-17-21-auto-research-report.md) | [Discovery and authorization design](../../reports/starintel-updates-changelog/2026-09-17-43-auto-research-android-special-report.md) |
| StarIntel Website | [Pinned schema conformance](../../reports/starintel-updates-changelog/2026-09-17-22-website-report.md) | [Browser access versus native parity](../../reports/starintel-updates-changelog/2026-09-17-44-website-android-special-report.md) |
| StarIntel Infrastructure | [Operator gates and validation](../../reports/starintel-updates-changelog/2026-09-17-23-infrastructure-report.md) | [Mobile operator-access boundary](../../reports/starintel-updates-changelog/2026-09-17-45-infrastructure-android-special-report.md) |
| Task Steward | [Evidence-reconciliation status](../../reports/starintel-updates-changelog/2026-09-17-24-task-steward-report.md) | [Synchronized state versus execution evidence](../../reports/starintel-updates-changelog/2026-09-17-46-task-steward-android-special-report.md) |

## Downloads

Zara rolling prerelease: [phone APK](https://github.com/lost-rob0t/zara/releases/download/android-latest/zara-latest.apk), [Wear APK](https://github.com/lost-rob0t/zara/releases/download/android-latest/zara-wear-latest.apk), [manifest](https://github.com/lost-rob0t/zara/releases/download/android-latest/zara-latest.manifest.txt), [release](https://github.com/lost-rob0t/zara/releases/tag/android-latest).

StarIntel v0.3.0-alpha: [Companion phone APK](https://github.com/lost-rob0t/starintel-wearos/releases/download/v0.3.0-alpha/starintel-phone-v0.3.0-alpha.apk), [Wear APK](https://github.com/lost-rob0t/starintel-wearos/releases/download/v0.3.0-alpha/starintel-wear-v0.3.0-alpha.apk), [Quasar Android APK](https://github.com/lost-rob0t/starintel-wearos/releases/download/v0.3.0-alpha/quasar-android-v0.3.0-alpha.apk), [matching bundle and faces](https://github.com/lost-rob0t/starintel-wearos/releases/download/v0.3.0-alpha/starintel-wearos-v0.3.0-alpha-apks.zip), [checksums](https://github.com/lost-rob0t/starintel-wearos/releases/download/v0.3.0-alpha/SHA256SUMS).

## Delivery evidence

Article files are not delivery receipts. The authoritative verified message IDs and destination are recorded in [published state](../../state/published.json). The one-shot batch retains a separate delivery ledger after publication.
