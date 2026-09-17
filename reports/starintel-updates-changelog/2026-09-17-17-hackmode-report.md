# Hackmode: replay checkpoints now identify the bytes they consumed

September 17, 2026. The meaningful new Hackmode change is an integrity repair in IPX replay. It closes a gap between remembering a byte offset and proving that the file at that offset is still the same evidence stream.

## Changes

### An offset alone was not enough

Replay previously resumed from the stored byte offset associated with a capture/session source. If the spool file had been replaced, restored or re-exported while retaining that identity, the offset could point into unrelated bytes. The replay path could then decode those bytes into canonical evidence without recognizing the substitution.

The checkpoint now records a SHA-256 fingerprint of the consumed spool prefix, plus its size. Before resuming, replay checks that the required prefix is present and matches. A missing or shortened spool, or a changed consumed prefix, raises the typed ipx-spool-fingerprint-mismatch condition rather than proceeding with a misleading reconstruction.

### The check is about the consumed prefix

The protected range is the data before the checkpoint offset. That ties the checkpoint to the content it actually consumed, rather than treating a filename or session label as sufficient identity.

This distinction is useful when a spool legitimately grows. A checkpoint should be anchored to the processed prefix, not automatically invalidated merely because more data exists after it. Conversely, preserving the same label must not authorize replay from a changed prefix.

The checkpoint constructor accepts validated fingerprint and size fields. Legacy checkpoints without a fingerprint retain the size-only path. That compatibility behavior should be kept visible: an old checkpoint does not gain cryptographic content verification just because it is opened by newer code.

### The tests reproduce the bad cases

The regression fixtures replace and shorten a spool after a checkpoint, then require the typed mismatch error. The implementation record reports all ten core Hackmode suites passing and the canonical merge cites green core, hygiene and boundary checks.

The follow-up cleanup of an accidental empty placeholder is not being promoted into a user feature. The shipped behavior worth testing is that replay refuses a mismatched source rather than decoding it as if nothing changed.

## Android and evidence-transfer scope

No native Android capture/replay package is established by this merge. The relevant mobile integration lesson is narrower: transferring or restoring an evidence file must preserve its checkpoint/content relationship, not only its display name.

Treat a mismatch as a reconciliation problem. It is not a reason to overwrite the stored fingerprint with whatever bytes are currently present. Doing so would erase the very distinction the new check was added to preserve.

## Sources

Canonical replay-integrity merge: <https://github.com/lost-rob0t/hackmode/commit/420b788df3bb6432fcb16de69be3fbc044f64640>
Failure scenario, legacy behavior and regression details: <https://github.com/lost-rob0t/hackmode/commit/26dd29fd4979467c598c9893ae03da6dd1ba4166>
