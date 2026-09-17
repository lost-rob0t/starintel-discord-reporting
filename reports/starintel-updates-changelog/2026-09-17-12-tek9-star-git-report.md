# Tek9 / star-git: immutable snapshots, compressed packs and custody-gated eviction

## FOLLOW-UP

This adds the archive runtime-packaging and round-trip evidence, with a closer account of custody validation and restore boundaries.

September 17, 2026. The new star-git work turns archival into a set of explicit storage contracts: what was snapshotted, how it was packed, which original revision it represents and what evidence is required before discarding a hot copy.

## Changes

### Snapshots and restore are separate operations

Immutable tree snapshots and an explicit ref-restore API have landed, with tests for deterministic snapshot trees. This is useful because recording a historical state and choosing to make that state current are different actions. The history object can remain immutable while a ref is deliberately restored.

The update should not be read as a claim of complete compatibility with Git's object format or command-line behavior. star-git is the project's revision/archive layer; its actual API and tests define what it supports.

### LZMA packs have their own verified format

The archive layer now includes a deterministic liblzma codec and immutable compressed pack format. The tests exercise deterministic pack output and corruption handling. A separate Nix packaging change includes the liblzma runtime closure and an archive round-trip gate.

The distinction is between compressing arbitrary bytes and producing an archive whose framing and content can be checked on readback. Compression alone says nothing about whether the pack contains the intended revisions or whether it can be restored correctly. The new pack layer gives those checks a defined home.

### Commit provenance can point back to Couch revisions

The commit-v2 extension adds provenance and a Couch revision index. That provides an explicit lookup relationship instead of asking downstream consumers to infer which source revision a packed object represents.

For reconciliation, retain that provenance rather than reducing an archived item to only its current document identifier. Two observations can refer to the same logical document while representing different revisions. The implementation includes tests for provenance requirements and revision lookup, with semantically distinct fixtures.

### A hot object cannot be evicted just because an upload was attempted

The custody layer distinguishes uploaded, stored-unverified, verifying, verified and failed-integrity states. A verified receipt requires a verification timestamp and a declared method; its byte length must match the known pack. Receipt identity is immutable: reusing an ID with different contents is rejected.

Hot eviction is gated on verified custody policy. This separates an attempt to store an archive from the evidence that permits removing its hot representation. Failure-path tests require verified custody before eviction.

There is an important boundary in the implementation: receipt registration is a trusted embedded storage port. It does not contact a cloud provider or independently prove a remote upload. The archive/provider adapter must obtain the verification evidence honestly before registering it. Exposing this registration path as an unauthenticated public API would defeat the model.

## What this does not announce

These commits do not establish deployed bucket auto-sharding, complete server lifecycle integration, a particular production corpus size or a fully tested Android database port. They establish the snapshot, pack, provenance and custody building blocks in Tek9.

For mobile-facing systems, keep archive custody on the trusted storage side. A phone cache being evicted is not the same event as the archival system proving it retains the authoritative revision. An Android interface should expose those states distinctly rather than turning every storage action into one synced badge.

## Sources

Immutable snapshots and explicit restore: <https://github.com/lost-rob0t/tek9/commit/429ad72cef9e52c510391fdaf0311715eb5dd496>
Deterministic LZMA packs: <https://github.com/lost-rob0t/tek9/commit/c9364c229464e2334f93006267638ffa70e316ba>
Commit-v2 provenance and Couch revision index: <https://github.com/lost-rob0t/tek9/commit/79bf85fefa249a554f70c258cf5ea4e4cf0510bb>
Custody and eviction: <https://github.com/lost-rob0t/tek9/commit/8178cf0af2fcad48b509b439423c030008d62620>
Trusted receipt-port contract: <https://github.com/lost-rob0t/tek9/blob/master/src/star-git/custody.lisp>
Packaged liblzma closure and round-trip gate: <https://github.com/lost-rob0t/tek9/commit/b19f4dc7178a2ca07141cdb3ad700aef699f3178>
