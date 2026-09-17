# Zara Plugins Android special: installable means compatible, coherent and permissioned

## FOLLOW-UP

Mobile companion to the plugin failure-handling deep dive. This is compatibility guidance, not an announcement of universal desktop-plugin parity on Android.

## Changes

Local Recall's transactional installer treats its library and wrapper as one coherent pair. If publishing either component fails, the prior pair is restored and unrelated configuration is left alone. An Android installer should preserve the same outcome distinction rather than report failure while leaving mismatched components active.

The Agent Zero repair also matters at a phone-facing error surface: a remote failure body can contain reflected credentials or hostile prompt-like text. The adapter limits the visible error information and suppresses exception causes that could put removed content back into a traceback.

Neither patch proves that a desktop plugin's Python/native dependencies exist on Android. A registry entry, downloaded archive and activated compatible plugin are three different states. The phone runtime must declare the supported API and execution environment, then enforce its permission/capability boundary.

Useful acceptance cases include an interrupted component update, a missing native dependency and an upstream error that reflects a test credential. Verify that the previous working version remains coherent and that diagnostics do not expose the test value. These are proposed mobile checks; they were not run on a physical phone for this post.

## Sources

Transactional library/wrapper update: <https://github.com/lost-rob0t/zara-plugins/commit/ef45b794685ad5c1a6d7015ae7d08b95c9326f05>
Remote-error contract: <https://github.com/lost-rob0t/zara-plugins/pull/525>
