# StarIntel Infrastructure Android special: a mobile browser does not change operator authorization

## Changes

The recent infrastructure changes require access gates around operator-only surfaces and reject configurations missing those gates. The same restriction applies when the browser happens to be on a phone.

Do not equate knowing a dashboard address with being authorized to inspect it. An authenticated phone session, a public application session and an operator session can have different authority. The mobile interface should preserve that distinction rather than encouraging users to bypass a denied route through an alternate address.

Operational query views can contain information that is not part of the public application response. Keep those records within the intended access boundary and avoid exposing sensitive diagnostics in screenshots or support messages.

A useful acceptance pass checks denied access before authentication, the authorized operator path and the same controls on a staged surface. This is proposed rollout verification, not a claim that a fresh physical-phone or production security test was performed.

These are infrastructure-side controls. No new Android permissions, APK or native operator console is announced by the inspected changes.

## Sources

Verified private access-gate and configuration-validation changes. Source identifiers and deployment details are omitted.

## Private Source Attestation

Verified on the configured private canonical branch.
