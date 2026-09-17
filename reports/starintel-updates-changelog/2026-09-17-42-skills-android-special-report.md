# StarIntel Skills Android special: resolve the phone consumer's lock, not the desktop's assumptions

## FOLLOW-UP

Android companion to the spec-resolution workflow update.

## Changes

The revised skills require resolving the active consumer release and verifying its canonical manifest before defining StarIntel document-derived fields or actor contracts. The same rule applies when the consumer is a phone app or mobile plugin.

Do not infer compatibility from a v0.9.0 filename, and do not assume that a desktop repository's selected profile is automatically the phone's selected profile. The immutable envelope and the consumer's release/profile lock are separate dimensions.

When generating mobile integration code, inspect the Android repository's actual contract and supported runtime first. A desktop skill describing a Python or Lisp adapter does not establish that the dependency can execute in the APK.

A useful acceptance record names the consumer lock, validates representative documents and checks explicit rejection of unsupported types. That is workflow guidance. It is not evidence that every installed assistant has loaded the revised skills or that a new Android validation service has shipped.

The practical change is an earlier compatibility decision: resolve and verify before generating code that embeds an outdated assumption.

## Sources

Consumer-lock resolution before actor contracts: <https://github.com/lost-rob0t/skills/commit/17fd4bebf64ccddee45a9fe8a514a0c63aab5031>
