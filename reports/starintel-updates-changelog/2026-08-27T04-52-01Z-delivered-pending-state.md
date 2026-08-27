## PROLOG-RLM NOW HAS A RENDERER-NEUTRAL RUNTIME STATUS VIEW

## Changes

Prolog-RLM now exposes canonical runtime status data for model identity, cumulative input/output tokens, and current context occupancy without binding that state to a specific UI.

Context usage stays separate from cumulative token usage. Unknown context capacity stays unknown instead of being guessed from historical token counters, and frontends can render the same normalized status contract themselves.

Landed: <https://github.com/lost-rob0t/prolog-rlm/commit/ad52a1dd79caf1f65e1910961fd93d6798723b35>

Delivery recovery note: Discord accepted this report as message 1542396790853210122 in channel 1539717118218469416. The publisher's state commit then conflicted during rebase, so this artifact is temporarily outside the `*-report.md` publisher glob to prevent duplicate delivery until the receipt-state race is repaired.