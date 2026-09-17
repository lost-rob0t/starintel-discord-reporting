# A0 Symbolics Android special: identify the host distribution as well as the phone app

## FOLLOW-UP

Mobile integration companion to the upstream-replay maintenance deep dive.

## Changes

The upstream-sync work pins an upstream base, keeps Symbolics distribution identity explicit and provides isolated replay/verification machinery. The detailed replay record is host-side maintenance evidence. It does not publish a new Android A0 Symbolics runtime.

For a phone-facing session, record two versions: the client application and the host distribution. Updating an APK does not prove the server kept its symbolic overlays, and a successful connection does not prove that the host was updated from the intended distribution source.

The update policy rejects raw upstream and marker-less targets rather than silently replacing Symbolics with plain upstream software. A mobile update screen should not flatten those identities into one newer-version label.

When validating a reconnect after maintenance, check host identity, expected symbolic plugin activation and an ordinary supported operation. A replay report is evidence about the source-maintenance process, not automatically a session-continuity or physical-phone test.

This post describes the integration boundary and a suggested verification sequence. No new native Android package or complete client/host version-negotiation feature was established by the inspected changes.

## Sources

Replay proof and maintenance hardening: <https://github.com/lost-rob0t/a0-symbolics/commit/e922df43043bb83ad50b6837f042f490bc3991db>
Distribution update model: <https://github.com/lost-rob0t/a0-symbolics/commit/790687b96cad3dc542c3a6f49b58dab67933839b>
