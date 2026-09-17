# A0 Symbolics: upstream upgrades become a replayable distribution workflow

## FOLLOW-UP

This adds the detailed replay proof, resume handling and fork-surface maintenance evidence behind the distribution-update summary.

September 17, 2026. A0 Symbolics has landed an explicit maintenance model for staying compatible with upstream without accidentally replacing the Symbolics distribution with plain upstream software.

## Changes

### The upstream base is immutable and distribution identity is explicit

The maintenance metadata pins an exact upstream base and identifies the Symbolics distribution remotes. Release identity distinguishes the upstream version from the distribution's own series. That makes the question which software am I updating to answerable before the update runs.

Self-update and the durable update manager accept the Symbolics distribution sources and reject raw upstream or marker-less targets. A bare upstream release tag is no longer treated as an equivalent substitute for a distribution release. The goal is to preserve the product's symbolic additions through an update, not merely to obtain a newer checkout with a familiar name.

### Upstream changes can be replayed in an isolated worktree

The new upstream-sync tool exposes status, planning, preparation, resume, verification and fork-surface reporting. It uses isolated worktree replay, recorded conflict handling and range-diff/machine-readable reports so a maintainer can inspect what was carried forward.

The follow-up includes guards for an already in-progress pick, skipping empty picks and using worktree-log evidence when resuming. Those details matter for a partially completed replay: resuming should continue the known operation, not quietly start a conflicting second one.

The repository records a 68-of-68 replay proof against upstream v2.12 and a green verification gate. That is a recorded maintenance exercise. It is not a claim that every future upstream release will replay without conflicts or that every deployed instance has already been upgraded.

### Product overlays reduce edits to upstream-owned files

Prompt debloat and persona overrides move into the Symbolics prompt-overlay plugin rather than remaining direct edits to upstream prompt files. A classified fork-surface budget makes the remaining divergence inspectable.

Reducing that patch surface has a concrete maintenance benefit: fewer upstream-owned files need manual reconciliation on the next replay. It does not mean product-specific behavior disappears; its ownership becomes more explicit.

A separate boot fix re-enables symbolic plugins on every boot. That addresses runtime activation independently of whether the underlying distribution checkout was updated correctly.

## Android relationship

This change governs the host-side distribution and update path. It does not publish a new A0 Symbolics Android APK. A phone-facing client still connects to the selected host; updating that client and updating the host distribution are separate operations.

When diagnosing a mobile session, record the host's distribution identity as well as the phone app version. A successful phone connection cannot establish that the host retained its symbolic overlays through an upstream update.

## Sources

Upstream-replayable model merge: <https://github.com/lost-rob0t/a0-symbolics/commit/80eee4650558480358faa68e7851de859677388e>
Pinned base, update policy and sync implementation: <https://github.com/lost-rob0t/a0-symbolics/commit/790687b96cad3dc542c3a6f49b58dab67933839b>
Replay proof, resume hardening and fork-surface budget: <https://github.com/lost-rob0t/a0-symbolics/commit/e922df43043bb83ad50b6837f042f490bc3991db>
Symbolic-plugin boot activation: <https://github.com/lost-rob0t/a0-symbolics/commit/ec0ef188e89ed77e53ec1e94d1ad800bb69b6c35>
