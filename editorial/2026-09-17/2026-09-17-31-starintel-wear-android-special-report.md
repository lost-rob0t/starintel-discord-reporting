# StarIntel Wear Android special: bootstrap once, verify the pair, then install from Companion

September 17, 2026.

## FOLLOW-UP

This expands the release announcement with the landed pairing/launcher repair, installation prerequisites and a device-test sequence. Discovery, transfer and installation are separate checkpoints.

## Changes

### Install a matching phone/watch pair

Companion and the Wear receiver need the matching application identity and signing certificate for Data Layer communication. The pairing repair adds a shared debug signing identity and parity gates, avoiding mismatched debug builds produced on different build hosts.

The companion tries the advertised capability, then falls back to directly connected Wear nodes when capability propagation is stale. Direct sending probes the receiver instead of leaving setup permanently disabled. Transport failure diagnostics now call out the signing requirement.

Do not treat repeated retries as a signer migration strategy. The install tooling supports an explicit clean migration for legacy mismatches; removing an existing app can remove its local configuration, so preserve the configuration needed to re-enroll it.

### The receiver must exist before it can receive updates

Install the receiver-bearing Wear application once through the documented bootstrap path. After that, Companion's Watch Apps and Update Manager can deliver matching client/face packages through Data Layer. The watch verifies the package and invokes the system installer. Installation consent remains an operating-system step.

The package order is faces first, Wear self-update last. Updating the receiver before its remaining transfers finish would disrupt the batch. MASTER, latest release and an exact version are distinct choices; use an exact release to reproduce a failure.

### A scheduler failure should not stop the launcher

Background JobScheduler setup is now best-effort. Rejection of a persisted periodic job can fall back to a non-persisted job. Refresh, notifications, saved-search runs and Tile requests are isolated so one subsystem failure does not escape into the activity lifecycle.

That is a failure-containment change, not a guarantee that every refresh succeeded. A usable launcher and a successful background update need separate checks.

### Physical test sequence

Confirm watch discovery, send configuration, check acknowledgement, select the intended package version, transfer, verify, approve the system install prompt and inspect the installed version. Record the first failing stage, phone/watch versions and signer/migration history. These instructions do not claim a fresh physical-device test was performed for this post.

## Downloads and sources

Companion phone APK: <https://github.com/lost-rob0t/starintel-wearos/releases/download/v0.3.0-alpha/starintel-phone-v0.3.0-alpha.apk>
Wear client/receiver: <https://github.com/lost-rob0t/starintel-wearos/releases/download/v0.3.0-alpha/starintel-wear-v0.3.0-alpha.apk>
Matching bundle including faces: <https://github.com/lost-rob0t/starintel-wearos/releases/download/v0.3.0-alpha/starintel-wearos-v0.3.0-alpha-apks.zip>
Checksums: <https://github.com/lost-rob0t/starintel-wearos/releases/download/v0.3.0-alpha/SHA256SUMS>
Pairing and launcher implementation: <https://github.com/lost-rob0t/starintel-wearos/commit/5b4a9d9fcc38c429b70b3df7f00dac57968f4126>
Repair details: <https://github.com/lost-rob0t/starintel-wearos/pull/63>
Companion installation contract: <https://github.com/lost-rob0t/starintel-wearos/pull/89>
Bootstrap guide: <https://github.com/lost-rob0t/starintel-wearos/blob/main/README.md>
