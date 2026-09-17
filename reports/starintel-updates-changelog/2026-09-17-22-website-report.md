# StarIntel Website: exact schema conformance instead of a familiar version label

September 17, 2026. The website's schema-consumer update pins and checks the canonical artifacts it actually uses. This is a compatibility change, not a new visual redesign announcement.

## Changes

### The consumer has an explicit selected release

The landed website update aligns its vendored schema and manifest with the canonical 0.9.1 release/profile while retaining the immutable 0.9.0 wire envelope. Its required document-type checks include research-node and operation.

That distinction remains important now that other additive profiles exist. This post describes the website's verified consumer update. It does not claim that 0.9.1 is the newest profile everywhere or that the website has automatically adopted later extensions.

### A local checkout must match the lock

The sync/check path records the canonical source selection and validates the artifact hash, release/revision metadata and required types. When a canonical checkout is used, its Git identity must match the lock; an arbitrary checkout with a plausible filename is not silently accepted as the pinned source.

Exact artifact equality makes drift visible. It also gives maintainers a concrete reason for a failed compatibility check instead of treating every disagreement as an interchangeable schema-version string.

### Validation includes the surrounding site pipeline

The implementation record reports build, tests, type checking, Org export, generated facts and schema verification against the selected artifacts. Those are recorded source/build checks. They do not independently establish that every hosted instance is running the new build.

For readers, the practical outcome is a more explicit contract between the site and StarIntel documents. A future schema upgrade should be a deliberate consumer change, with the supported types and artifacts checked together.

## Sources

This public summary is based on the verified private implementation and its recorded validation. Private repository identifiers and deployment details are omitted.

## Private Source Attestation

Verified on the configured private canonical branch.
