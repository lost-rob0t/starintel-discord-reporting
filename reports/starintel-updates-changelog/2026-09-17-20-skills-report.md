# StarIntel Skills: resolve the consumer's actual spec before generating contracts

September 17, 2026. The maintained skills now make spec resolution an explicit prerequisite rather than asking a worker to guess which release a schema filename represents.

## Changes

### Resolve first, generate second

Actor creation now requires the spec-version skill whenever the actor consumes or emits StarIntel documents or manifests. Before defining a document, a derived message field or an actor manifest, the workflow resolves the consumer lock's active release_version and verifies the pinned canonical manifest.

The same prerequisite was added to ingest, corpus search and OSINT-output guidance. These are places where a plausible-looking object can still be incompatible with its consumer. Looking at a familiar dtype name is not enough to establish which complete contract applies.

### Release and envelope versions remain different dimensions

The guidance explicitly rejects deriving the release from a v0.9.0 schema filename. The immutable base schema_version can remain unchanged while an additive release/profile evolves. The lock and canonical manifest establish the consumer's selected release, not a guess based on a path.

This is particularly relevant during mixed-version rollout. A newer profile existing upstream does not mean that every repository has adopted it. The correct starting point is the consumer's declared lock, followed by a deliberate compatibility update when required.

### Runtime ownership still matters

Spec resolution does not replace actor implementation work. The actor-creation workflow retains explicit state ownership, bounded mailboxes, restart/generation behavior, effect adapters and tests at the real runtime boundary. A manifest or registered reference is not, by itself, an executing actor.

This is landed workflow guidance. It is not proof that every agent has loaded the new skill, that every generated object passes validation, or that a new runtime enforcement engine has shipped. Maintainers still need to run the owning repository's validators and tests.

## Sources

Actor-contract prerequisite and version distinction: <https://github.com/lost-rob0t/skills/commit/17fd4bebf64ccddee45a9fe8a514a0c63aab5031>
Ingest prerequisite: <https://github.com/lost-rob0t/skills/commit/825d570f4d7800d0b54bc68e99588fdb2d68df83>
Corpus-search prerequisite: <https://github.com/lost-rob0t/skills/commit/4ea9f5e504476b65821610d9044bf21b02e98124>
Output prerequisite: <https://github.com/lost-rob0t/skills/commit/4b355075057a6f1438ce01dbd0d98c638bc6ffad>
