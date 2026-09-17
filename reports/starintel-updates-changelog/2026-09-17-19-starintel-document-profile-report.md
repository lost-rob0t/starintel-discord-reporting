# StarIntel document tooling: the 0.9.2 network-capture profile is additive, not an envelope rewrite

## FOLLOW-UP

This adds the release manifest's exact envelope/profile distinction, artifact-reference policy and sensitive-header classes to the earlier profile summary.

September 17, 2026. The document/spec work hosted in the Auto-Dig repository has landed a network-capture profile and release manifest. This is a schema/tooling announcement, not an investigation report or an instruction to restart collection workers.

## Changes

### Two capture types have a named profile

The published profile declares http-transaction and web-capture document types. Its release/profile version is 0.9.2, while its base envelope remains the immutable 0.9.0 schema. The manifest explicitly says the extension is additive within v0.9 and existing 0.9.1 document types remain unchanged.

Those version fields are not interchangeable. A consumer seeing profile version 0.9.2 should not rewrite every existing envelope's schema_version or assume all other components already support the new types. The profile is applied through its declared schema module and network-capture validator.

### Large or sensitive capture material stays behind references

The manifest makes request bodies, response bodies, screenshots and DOM material artifact-reference-only. Browser-session and network-context fields use opaque references rather than embedding the corresponding live context directly into the document.

It also declares redaction classes for authorization, proxy authorization, cookies, set-cookie values and common API-key/auth-token headers. The point is to represent a capture without turning the normalized document into a portable credential dump.

A schema policy does not independently prove that every producer has applied it. Producers and consumers need the matching validation/materialization path; merely placing a profile label on arbitrary captured data is not conformance.

### Capability metadata is part of the contract

The manifest names the captcha.solve capability for challenged captures, and the accompanying work checks the opaque source-context requirement. This announces the typed contract, not universal challenge-solving availability or a bypass of authorization at a source site.

## Android and interoperability scope

A phone-side capture integration would need to produce the declared types, retain artifact references and preserve the redaction/opaque-context rules. This merge does not itself publish an Android capture APK or establish that existing phone clients have adopted the profile.

Keep envelope version, profile version and deployed consumer support visible during rollout. That avoids diagnosing a deliberate unsupported-type rejection as a generic networking failure, and avoids claiming ecosystem-wide migration from a single schema release.

## Sources

Landed profile: <https://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/0114f25f8fbab59fa31d70877bf988a28f4a40c5>
Release manifest and exact version/reference policy: <https://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/c8d44f4bb1121093ea437175bf35cc7d5be3799d>
Manifest: <https://github.com/lost-rob0t/starintel-gpt-auto-dig/blob/main/schemas/starintel-network-capture-v0.9.2.manifest.json>
