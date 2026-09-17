# StarLang Android special: portable contracts do not imply a portable process runtime

## FOLLOW-UP

Android integration companion to the runtime and canonical-JSON deep dive.

## Changes

The compiled external-actor work proves a real Common Lisp mailbox-to-ZMQ-to-Nim path. Its local IPC/loopback policy and managed-process lifecycle are part of that proof. They are not evidence of an Android service package, public federation authentication or a native phone binding.

The actor contract also has to reject unsupported options rather than silently accepting a declaration the runtime cannot honor. A phone-side consumer should preserve that distinction: unsupported, unavailable and completed are not interchangeable states.

For a mobile integration, begin with the exact typed contract and a supported transport. Keep command identity and deadline visible, and do not replay an unknown-outcome command solely because a phone activity restarted. The runtime deliberately does not turn transport queueing into durable application completion.

Canonical binary64 JSON is relevant at the interchange boundary. Test exact fixture bytes rather than trusting the phone platform's default number printer. The finite-number serializer does not establish that compiler floats or every generated binding have shipped.

These are integration requirements derived from the landed runtime constraints. A complete native Android StarLang host remains unverified in this edition.

## Sources

Actor-option contract rejection: <https://github.com/lost-rob0t/star-lang/commit/d320172e42ddc4448da0334fc67c8b7bd6a001e5>
Runtime end-to-end scope: <https://github.com/lost-rob0t/star-lang/pull/112>
Canonical-number scope: <https://github.com/lost-rob0t/star-lang/pull/104>
