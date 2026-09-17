# StarIntel Auto-Research Android special: discover a capability without inventing another registry

## FOLLOW-UP

Android design companion to the corrected registry/routing ownership record. This is architecture guidance, not a newly deployed discovery UI.

## Changes

The corrected design makes StarIntel Server the deployment-facing actor/service registry. StarLang supplies typed actor/domain semantics, and cross-authority route selection has its own routing boundary.

A phone actor browser should consume the deployment's safe discovery projection rather than maintaining a second independent authority for which actors exist. It also needs to distinguish a declared capability from a currently available runtime instance.

Discovery must not grant invocation rights. Showing a button for a registered actor is a UI choice; authorizing its operation against a tenant or dataset is a separate server-side decision. A stale phone view must not widen that authority.

Useful design/acceptance cases are a registered but unavailable actor, a changed runtime generation, a capability the caller cannot invoke and an unresolved remote destination. The interface should preserve those differences instead of labeling every failure offline.

These cases follow from the research ownership model. They are not claims that all required endpoints or native Android screens have been implemented. Implementation must still be checked against the actual server and client revisions.

## Sources

Corrected registry, domain and cross-authority ownership: <https://github.com/lost-rob0t/starintel-auto-research/commit/825689da3ad669a29a9a7af585e7cdc8db2693b1>
