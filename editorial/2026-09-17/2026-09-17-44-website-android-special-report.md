# StarIntel Website Android special: browser access is not native-app parity

## Changes

The website's recent work pins and verifies its selected canonical document schema. That compatibility change applies to the built website; it does not create a native Android application or prove a new mobile layout.

When accessing the site from an Android browser, distinguish a successfully loaded page from a successful backend operation. A schema mismatch or unsupported type should not be interpreted as a generic phone-network failure.

The consumer update retains the immutable 0.9.0 envelope while selecting the 0.9.1 release/profile. Do not relabel that specific update as automatic adoption of every later profile. The supported contract is a property of the deployed build.

A useful mobile acceptance pass checks the intended site build, representative supported documents and a deliberately unsupported input, alongside ordinary viewport and navigation behavior. Those are proposed tests; no fresh Android-browser or accessibility audit was performed for this post.

This companion covers the mobile implications and the limits of the verified schema change. It does not announce a new APK, offline cache or website-to-native feature bridge.

## Sources

Verified private website schema-consumer update and recorded build checks; private identifiers are omitted.

## Private Source Attestation

Verified on the configured private canonical branch.
