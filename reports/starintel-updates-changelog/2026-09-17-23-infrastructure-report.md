# StarIntel Infrastructure: operator access is a configuration invariant

September 17, 2026. Recent infrastructure changes tighten the distinction between public-facing services and operator-only web surfaces. This summary intentionally omits private deployment details.

## Changes

### Operator-only surfaces require explicit access gates

The maintained configuration now applies authorization gates to operator-only surfaces, including their staged counterparts. The important change is that an alternate deployment name or stage must not quietly turn a restricted surface into an unrestricted one.

This is a configuration/control-plane outcome. It is not a claim that a single login screen proves every downstream operation is authorized correctly. Application-level authorization and the access boundary around an operator surface remain separate responsibilities.

### Validation rejects a missing gate

The accompanying validation work rejects operator-only routes that lack the required gate. That moves a class of configuration mistakes into a checkable failure rather than relying exclusively on a reviewer to notice a missing restriction in a large configuration change.

A validator only establishes the properties it checks. This update should not be read as an independent penetration-test result or a guarantee about every deployment outside the maintained configuration.

### Query-audit views become an operator concern

The recent changes also add operator-facing query-audit/dashboard work. Operational visibility is useful, but it does not make the underlying records public. The same separation between public application use and restricted operational inspection must be preserved when exposing a dashboard.

The source changes have landed. A repository change and a verified production rollout are separate checkpoints; no fresh live-deployment test was performed for this post.

## Sources

Verified private configuration and validation changes. Public reporting omits source identifiers, addresses, service topology and access details.

## Private Source Attestation

Verified on the configured private canonical branch.
