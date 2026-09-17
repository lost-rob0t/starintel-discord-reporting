# StarLang: real mailbox-to-Nim execution and deterministic binary64 JSON

September 17, 2026. StarLang has landed a concrete external-actor transport path and a carefully bounded canonical-number foundation. The former demonstrates an actual runtime round trip; the latter improves byte-level interoperability without announcing unfinished language features.

## Changes

### A compiled actor reaches a real external process

The ZMQ runtime adapter consumes normal compiled external-actor IR and materializes a mailbox-backed runtime proxy. A request can now traverse the Star mailbox, proxy handler, ROUTER/DEALER transport and persistent Nim process, then return as a correlated lifecycle reply.

The underlying Common Lisp binding uses libzmq's C ABI with a managed context, owner-thread sockets, bounded multipart messages, finite timeouts and high-water marks. Polling preserves the caller's monotonic deadline across interruptions or spurious wakeups. Cleanup includes draining and reaping the managed peer rather than merely dropping a reference to its process.

This remains a local IPC/literal-loopback transport slice. A routing identity or a ready message is not authentication, and this merge does not turn on an authenticated public federation listener.

### Mailbox and generation authority stay where they belong

The adapter does not bypass admission to make an external actor look fast. The mailbox remains responsible for admission, FIFO behavior and backpressure. The runtime remains responsible for generations, restarts and handlers. When the runtime generation changes, the old external session is invalidated and replaced before a new command.

Readiness belongs to the transport control layer, not to each application's manifest. The first compiled-actor end-to-end test exposed that layering mistake, and the implementation now separates transport readiness from application messages.

Failed or unknown-outcome commands are not automatically replayed. Queuing bytes inside libzmq is not represented as durable admission, journal commitment or application completion. Unsupported deadlines fail before the external effect instead of silently changing the caller's request semantics.

### The end-to-end test exercises the actual boundaries

The recorded native verification compiles a real external actor and checks the full mailbox-to-Nim path. It also checks rejection without an adapter, capacity-one mailbox backpressure, rejection before an unsupported-deadline effect and generation replacement after restart. Those cases matter more than an isolated socket echo because they exercise the runtime contract around the transport.

### Binary64 canonicalization is a foundation, not the whole float feature

The canonical JSON system now has a pure Common Lisp shortest-roundtrip serializer for finite IEEE-754 binary64 values. It normalizes positive and negative zero to JSON 0 and rejects NaN and infinities with a typed error before number serialization.

Exact-output coverage includes applicable RFC 8785/ECMAScript vectors and notation boundaries. The implementation is deliberately not delegated to the implementation's generic float printer, Python, Node, FFI or an external process. Stable canonical bytes matter when two producers need to agree on the same manifest or digest.

The scope is narrow: this does not add compiler/type-system float support, generated language mappings, geo migration or document-schema changes. Existing canonical manifest and wire bytes are preserved by the surrounding fixtures.

## Android and integration scope

No Android runtime package is established by these two merges. A native phone client can consume a compatible service contract without hosting this Lisp/Nim process arrangement. Embedding the transport on Android would still require a supported packaging, lifecycle and authentication design; desktop local-loopback acceptance is not mobile acceptance.

For cross-language consumers, compare exact serialized fixtures rather than assuming every platform's default number printer produces the required bytes. That is integration guidance, not an announcement of a new Android binding.

## Sources

Managed transport and compiled runtime integration: <https://github.com/lost-rob0t/star-lang/commit/878cd2a99cc99b31f502242ba6adca19cf4815e3>
End-to-end cases, authority boundaries and recorded runs: <https://github.com/lost-rob0t/star-lang/pull/112>
Canonical binary64 foundation: <https://github.com/lost-rob0t/star-lang/commit/c9d56a38e04ef5cc1cfe90924da1551c7125bf3e>
Exact scope and serialization verification: <https://github.com/lost-rob0t/star-lang/pull/104>
Actor-option contract rejection: <https://github.com/lost-rob0t/star-lang/commit/d320172e42ddc4448da0334fc67c8b7bd6a001e5>
