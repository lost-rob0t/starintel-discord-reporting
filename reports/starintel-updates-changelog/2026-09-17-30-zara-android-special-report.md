# Zara Android special: local operation, authenticated remote access and the right APK

September 17, 2026.

## FOLLOW-UP

The earlier feature post covered local Prolog, embedded AI and automation. This companion goes deeper on the separately landed authenticated listener, the enrollment boundary and practical installation checks.

## Changes

### Local and remote are different runtime choices

Local mode does not need a desktop server to answer a supported symbolic request. An embedded model is an optional fallback, and its weights are not bundled in the base APK. The built-in embedded backend executes LiteRT-LM models; a format-neutral descriptor is not proof that GGUF or ONNX inference is implemented. Offline speech requires an installed voice that declares no network dependency.

Remote operation instead requires a reachable, authenticated server. The server can now keep its owner-private desktop IPC listener while also serving an explicitly configured TCP endpoint. Desktop and phone access no longer require treating one listener as a replacement for the other.

### Enrollment ready is not connected

The remote endpoint requires explicit security state. The phone pins the server's public key, and the server enrolls the phone's client public key. A locally prepared identity and a server pin do not prove that the server has authorized the phone or that a session handshake succeeded.

Troubleshoot those stages separately: select the intended runtime, confirm the configured endpoint, verify the server identity, confirm client enrollment, then establish the authenticated session. Do not solve a changed-server-key warning by silently accepting an unknown key.

The server regression covers local IPC and authenticated TCP at the same time. It also covers startup cleanup when the remote bind fails, so a failed remote listener does not leave the local runtime lease stranded.

### Watch discovery is not watch installation

Zara can discover a paired watch through Bluetooth and Wear Data Layer, but its APK installer uses wireless ADB pairing and transport. Nearby-device permission and watch debugging setup remain relevant. This is different from StarIntel Companion's receiver-based Data Layer installer.

### Check the artifact, not only the source branch

At this check, the rolling android-latest tag still pointed to ec9756e, the embedded-AI merge. The later local-first repair at 8a11e9c was on master but not the rolling tag. Do not assume downloading the rolling APK already includes that later fix. This is a point-in-time observation; the rolling channel can move.

## Sources

Phone APK: <https://github.com/lost-rob0t/zara/releases/download/android-latest/zara-latest.apk>
Wear APK: <https://github.com/lost-rob0t/zara/releases/download/android-latest/zara-wear-latest.apk>
Build manifest: <https://github.com/lost-rob0t/zara/releases/download/android-latest/zara-latest.manifest.txt>
Phone checksum: <https://github.com/lost-rob0t/zara/releases/download/android-latest/zara-latest.apk.sha256>
Release channel: <https://github.com/lost-rob0t/zara/releases/tag/android-latest>
Authenticated dual-listener implementation and regression: <https://github.com/lost-rob0t/zara/commit/e030ca4cd3667d533fa7005514bb89ca847c7bb4>
Local AI contract: <https://github.com/lost-rob0t/zara/blob/master/wiki/android-local-ai.org>
Phone-driven watch installation: <https://github.com/lost-rob0t/zara/pull/903>
