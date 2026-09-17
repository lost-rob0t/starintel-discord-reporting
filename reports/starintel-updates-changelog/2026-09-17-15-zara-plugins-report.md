# Zara Plugins: remote failures stop reflecting secrets, and Local Recall updates roll back coherently

September 17, 2026. Two landed plugin repairs strengthen failure handling without changing the Plugin API or widening capabilities. Both are about what happens when the happy path breaks.

## Changes

### Agent Zero errors are data from an untrusted remote

The Agent Zero adapter no longer reflects arbitrary response bodies or exception details into Zara-facing errors. HTTP failures expose the status code. Native JSON errors become a fixed generic category. Transport errors avoid stringifying potentially untrusted details, and exception causes are suppressed so a traceback does not reintroduce the material removed from the top-level message.

That last point matters. Sanitizing the visible error string is incomplete if exception chaining prints the original remote text below it. The regression tests use responses containing both an API-key value and hostile prompt-like text, including traceback-reflection cases.

The change reduces a concrete reflection path. It is not a claim that every remote response is safe or that the whole integration is immune to prompt injection. Successful responses, request headers, endpoint defaults, timeout/response bounds, principals, capabilities and lifecycle behavior are intentionally unchanged.

### Local Recall publishes a matched library and wrapper

The Local Recall installer previously needed a stronger guarantee when an update failed while publishing one component. The repair stages the wrapper, backs up an existing coherent library/wrapper pair and restores both components if publication fails.

The unit of recovery is the pair, not whichever file happened to be written last. Tests require the previous working pair to survive either library-publication or wrapper-publication failure. Unrelated configuration state stays untouched, and staging/backup scratch is cleaned after rollback or success.

This is more useful than reporting update failed while leaving a new wrapper pointing at an old library. The installation outcome should describe the environment that remains usable after failure, not only whether the attempted new version was copied.

## What remains unchanged

These patches do not introduce a new registry, alter Plugin API v1 or change principal/secret behavior. They repair error reporting and transactional update behavior inside existing plugins. Compatibility should be checked against the runtime that actually loads them.

## Android scope

A plugin repository update is not proof that its desktop Python/native dependencies run inside Zara Android. The same principles matter on the phone: do not display raw upstream error bodies, and do not call a plugin installed until its required components form a coherent version.

The commits cited here establish the repository-side repairs. They do not establish a separately released Android plugin APK or universal phone/desktop plugin parity. For Android package support, use the phone runtime's declared plugin capabilities rather than inferring support from a registry entry alone.

## Sources

Agent Zero sanitization: <https://github.com/lost-rob0t/zara-plugins/commit/c6d96a01a2c16dd8f41083e281b8d2ef145c18f3>
Reflection regressions and unchanged contracts: <https://github.com/lost-rob0t/zara-plugins/pull/525>
Transactional Local Recall update: <https://github.com/lost-rob0t/zara-plugins/commit/ef45b794685ad5c1a6d7015ae7d08b95c9326f05>
Rollback scope and tests: <https://github.com/lost-rob0t/zara-plugins/pull/521>
