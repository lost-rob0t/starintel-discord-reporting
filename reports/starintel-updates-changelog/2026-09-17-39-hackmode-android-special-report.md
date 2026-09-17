# Hackmode Android special: preserve checkpoint identity when evidence moves

## FOLLOW-UP

Mobile/evidence-transfer companion to the replay-integrity deep dive. This merge does not establish a native Android capture application.

## Changes

A new replay checkpoint includes the size and SHA-256 fingerprint of the consumed spool prefix. The detailed implementation and regression record show why a byte offset alone was insufficient: a replaced or shortened file could retain its label while no longer containing the same evidence.

For a phone-assisted transfer or restore workflow, preserve the checkpoint together with its associated content identity. A familiar filename, capture label or successful transfer notification is not proof that the consumed prefix matches.

Do not repair a mismatch by replacing the old fingerprint with the new file's fingerprint. That would erase the evidence that the checkpoint referred to different bytes. Reconcile which file and checkpoint belong together instead.

A useful acceptance test transfers the correct pair and verifies resumability, then substitutes or truncates the spool and requires the typed mismatch result. Legacy checkpoints without a fingerprint retain weaker size-only checking and should remain distinguishable.

These are integration checks derived from the host replay contract. They do not claim that such a phone transfer UI or a physical-device test has shipped.

## Sources

Checkpoint format, failure cases and regression evidence: <https://github.com/lost-rob0t/hackmode/commit/26dd29fd4979467c598c9893ae03da6dd1ba4166>
