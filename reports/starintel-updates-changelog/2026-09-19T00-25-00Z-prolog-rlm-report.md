# Prolog-RLM can now plug into Zara as a bounded local runtime

## Changes

- Prolog-RLM now ships an optional loopback-only `ZARA-RUNTIME/1` sidecar around its public runtime APIs. Zara can discover it, inspect health, run bounded `direct` or `rlm` generation, and cancel work without giving the host a second planner/provider stack.
- Provider and model authority stay inside Prolog-RLM. Request budgets may narrow runtime defaults but cannot widen them, and literal API keys are rejected instead of being accepted over the bridge.
- Discovery tells the truth about the current implementation: buffered HTTP, cancellation supported, no streaming, no Zara context handles, and no host-tool round trips yet. The packaged Nix output now includes the `prolog-rlm-zara` entrypoint.
- A follow-up merge aligned the bridge provenance with Zara's canonical bounded descriptor format, so the live descriptor is accepted as `prolog-rlm:local` instead of being rejected for schema mismatch.

Bridge: <https://github.com/lost-rob0t/prolog-rlm/commit/fa03bb5b48c858b16ec6061d5b49804ee6f29070>
Descriptor compatibility fix: <https://github.com/lost-rob0t/prolog-rlm/commit/9c475fe44c24ca58795c6b5cb5e002f2e2decc5e>
