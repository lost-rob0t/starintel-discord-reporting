# StarIntel Server Android special: preserve operation identity when the phone disconnects

## FOLLOW-UP

Android integration companion to the server reliability deep dive. These are backend effects and client acceptance guidance, not a StarIntel Server APK release.

## Changes

The terminal-job retention repair preserves the original total and status counters after releasing the large request payload. A mobile status screen can continue to show that receipt without requiring the server to retain the entire submitted document list.

The quarantine concurrency repair adds a different guarantee: workers no longer race an unsynchronized identifier generator, and failed settlement leaves the broker delivery unacknowledged instead of calling it completed. Neither fix makes a disconnected client's POST automatically safe to repeat.

For a phone client, preserve the submission's operation/job identity and distinguish accepted, running and terminal states. Losing Wi-Fi or recreating an activity is not evidence that the server rejected the original request. Reconcile the authorized status before repeating a consequential write.

A useful mobile acceptance test is to submit a bounded operation, interrupt connectivity, reconnect and retrieve the same authorized job receipt. Separately test denied access and a terminal failure. This is a recommended test sequence derived from the contracts, not a claim that all current Android clients already implement it.

The server revision is part of the result. Updating only the APK cannot install a server-side memory-retention or settlement fix.

## Sources

Terminal-job contract: <https://github.com/lost-rob0t/starintel-server/pull/190>
Newly covered quarantine-settlement implementation: <https://github.com/lost-rob0t/starintel-server/commit/d48fa939402abf701fa1cc4079dfb8bedfad8d4a>
