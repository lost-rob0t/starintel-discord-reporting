# StarIntel document profile Android special: a capture document is not a credential bundle

## FOLLOW-UP

Mobile integration companion to the 0.9.2 network-capture manifest deep dive.

## Changes

The profile adds http-transaction and web-capture types over the immutable 0.9.0 envelope. An Android producer must distinguish the envelope version, selected capture profile and the receiving server's supported types. A new profile upstream is not proof of support in an installed APK.

The manifest represents request/response bodies, screenshots and DOM content through artifact references. Session and network context use opaque references. It also names sensitive authorization, cookie and API-key header classes for redaction.

For a mobile capture integration, do not replace those references with inline credentials or live browser context just because it makes debugging easier. Keep the normalized document, protected source context and any separately stored artifacts in their intended roles.

Suggested acceptance checks include sensitive-header fixtures, unsupported-profile rejection and preservation of artifact references through transfer. These are proposed conformance checks, not proof that every producer already applies the policy.

This is a document-contract release. It does not install a capture plugin, enable an accessibility service or restart collection jobs on a phone.

## Sources

Exact profile manifest and reference/redaction requirements: <https://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/c8d44f4bb1121093ea437175bf35cc7d5be3799d>
