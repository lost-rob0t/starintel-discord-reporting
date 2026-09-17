# Tek9 / star-git Android special: a cache badge is not archive-custody proof

## FOLLOW-UP

Mobile integration companion to the archive-layer deep dive. No native Android Tek9 database package is announced here.

## Changes

The archive layer distinguishes hot content, compressed packs and verified custody evidence. The packaging follow-up includes the liblzma runtime closure and an archive round-trip gate. That is meaningful build evidence for the maintained archive package, not a blanket statement that the same native dependencies are packaged on Android.

A phone interface should distinguish locally cached, available from a local pack, available from verified remote custody and unavailable. Collapsing those into one synced indicator would hide whether the authoritative revision can actually be restored.

Custody receipt registration is a trusted storage-side operation. It does not upload or read back a remote object itself. A phone should not be able to declare an archive verified merely because it finished sending bytes or displayed a success animation.

A useful integration test removes only the phone cache, then requests the same immutable revision and checks its identity after restoration. Test missing and failed-integrity cases independently. That sequence is proposed acceptance guidance, not a new shipped Android restore feature.

Keep source revision provenance with the displayed document. The same logical document can have multiple archived revisions; retrieving the current identifier alone does not prove that the requested historical version was restored.

## Sources

Archive runtime packaging and round-trip gate: <https://github.com/lost-rob0t/tek9/commit/b19f4dc7178a2ca07141cdb3ad700aef699f3178>
Custody API contract: <https://github.com/lost-rob0t/tek9/blob/master/src/star-git/custody.lisp>
