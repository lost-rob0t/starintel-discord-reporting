# StarIntel Auto-Research: registry discovery and domain routing have different owners

September 17, 2026. The architecture research corrects an important ownership mistake. This is a design-record update, not an announcement that the entire runtime-plan system is deployed.

## Changes

### StarIntel Server owns deployment discovery

The corrected document places the actor/service registry and discovery plane in StarIntel Server. It consumes actor-emitted manifests and combines their static contracts with deployment and runtime availability. The registry answers what is available to a deployment and which declared capabilities it advertises.

Registration is not authorization. Seeing an actor in a discovery result does not grant a caller permission to invoke it or access its datasets.

### StarLang owns typed actor and domain semantics

StarLang owns the contracts and semantics of actor/domain definitions: accepted and produced types, logical domain destinations, typed dispatch, mailbox constraints and lifecycle behavior. A stable logical domain address is not the same thing as a currently running process incarnation.

The correction avoids turning these language/runtime responsibilities into a claim that StarLang owns the global StarIntel registry. Discovery and routing can cooperate without becoming the same subsystem.

### Cross-authority transport has another boundary

StarRouter handles cross-authority route resolution and transport-profile selection. Actor packages define actors and emit manifests; merely running an actor in a particular runtime does not make that package the global routing or registry authority.

These boundaries matter for extensions. A new actor package should not need to invent another registry, change the meaning of a typed domain command or make its own transport identifier the canonical application identity.

### Runtime planning composes policy before effects

The design describes a deterministic server RuntimePlan composed from deployment/dataset configuration and registered semantic contracts. Compilation is intended to finish before starting long-lived actors, threads, listeners, timers or database/broker connections.

That is the recorded design direction. It is not evidence that all those constraints are already enforced in deployed code. Implementation slices still require their own code and end-to-end verification. The corrected record supersedes the earlier statement that StarLang should own the entire registry.

## Sources

Corrected ownership record and rationale: <https://github.com/lost-rob0t/starintel-auto-research/commit/825689da3ad669a29a9a7af585e7cdc8db2693b1>
