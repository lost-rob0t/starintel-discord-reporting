# Quasar Android special: native login and package verification, not a server inside an APK

September 17, 2026.

## FOLLOW-UP

This is the Android companion to the expanded runtime-packaging post. It explains the phone/host boundary and the installation path, rather than reannouncing the APK as a new second release.

## Changes

### The native app is a separate product artifact

The Quasar APK is published with the StarIntel Wear package set. It is separate from both the static web bundle and the executable Common Lisp server. The newly examined hosted-runtime packaging makes that separation concrete: serving frontend files and starting the control-plane runtime are different deployment outputs.

Installing the phone app does not start that SBCL server on Android. Mobile feature parity must be established operation by operation against the configured server, not inferred from the shared name.

### Validate credentials before replacing the stored account

The native client supports username/password login and direct API-key authentication. It checks the bearer credential against the server's authentication-context endpoint before replacing the stored credential. Passwords are not persisted; the resulting credential uses Keystore-backed storage and is excluded from update manifests and logs.

A server-address error, failed login and rejected API operation are different failures. When reporting a problem, identify which step failed without posting passwords or API keys.

### Installation has its own checks

Companion's Phone apps catalog downloads Quasar over HTTPS and verifies expected length, SHA-256, package identity, downgrade policy and installed signing continuity. Android still asks for final installation approval. A completed download is not proof that the installation prompt was approved or that the expected version is now installed.

The published release remains v0.3.0-alpha. Use its matching manifest and checksums for reproducible testing; do not equate a successful artifact publication with a completed physical-phone test.

## Sources

Native Quasar APK: <https://github.com/lost-rob0t/starintel-wearos/releases/download/v0.3.0-alpha/quasar-android-v0.3.0-alpha.apk>
Companion APK: <https://github.com/lost-rob0t/starintel-wearos/releases/download/v0.3.0-alpha/starintel-phone-v0.3.0-alpha.apk>
Release and manifest: <https://github.com/lost-rob0t/starintel-wearos/releases/tag/v0.3.0-alpha>
Checksums: <https://github.com/lost-rob0t/starintel-wearos/releases/download/v0.3.0-alpha/SHA256SUMS>
Native authentication and installer contract: <https://github.com/lost-rob0t/starintel-wearos/pull/91>
Host runtime packaging boundary: <https://github.com/lost-rob0t/quasar/commit/cb55fdf24505c1edfd226db6c3cbcfbb0af1d22b>
