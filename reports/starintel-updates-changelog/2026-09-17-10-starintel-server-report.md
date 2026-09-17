# StarIntel Server: bounded bulk-job retention, safer quarantine settlement and opt-in telemetry

## FOLLOW-UP

The additional coverage includes the quarantine concurrency failure and its settlement regression, alongside the previously announced retention and telemetry work.

September 17, 2026. Recent master changes address three different failure boundaries: retaining completed requests, settling failed ingest work and exporting operational telemetry. They should not be flattened into a generic stability update.

## Changes

### Completed bulk jobs stop retaining the original request

Asynchronous bulk jobs remain in the process-local job table after completion so callers can inspect their status. Previously, that also kept the original document lists and request service contexts reachable. Status polling calculated the total from those retained documents, tying a small status record to the lifetime of a potentially large request.

The repair records the original total at submission and releases both request-only fields when the job becomes terminal. Completed, completed-with-errors and failed jobs retain their identity, submitter, status, counts and error code. The status API therefore keeps the useful receipt without needing the original payload in memory.

This is a targeted retention repair. It does not make the job table durable, change queue admission or make an ambiguous POST safe to repeat. A client that lost its response still needs to reconcile the original operation rather than infer that a timeout means nothing happened.

### Concurrent quarantine IDs no longer share an unsynchronized generator

The pinned ULID generator maintains mutable process-wide state. Concurrent server workers could obtain the same quarantine ID, causing a CouchDB conflict during settlement. The unhandled settlement failure could then kill the listener.

All server calls to that generator now pass through a shared lock. The consumer failure path logs and exits the affected worker, closes its Rabbit stream and leaves the delivery unacknowledged for redelivery. Quarantine persistence still occurs before publish and acknowledgement.

There are two useful invariants here: a failed record must not overwrite another record's quarantine identity, and a failed settlement must not be presented to the broker as completed work. The regression suite tests distinct IDs under concurrency and failed-settlement behavior rather than only a sequential happy path.

### Search auditing and export activation are explicit

The newest observability work audits authorized search-query entry points and wires the hosted telemetry add-on through an explicit activation gate. Export defaults off; merely loading the add-on is not enough to enable external telemetry. Hosted opt-in can arrange the add-on automatically, while transport installation is kept idempotent.

For operators, the distinction is between creating audit events and deciding where telemetry may be exported. A deployment should make that decision explicitly. This update does not establish that every installation has enabled export, nor does a source merge prove the current production process has been restarted or reloaded onto it.

## Android and client impact

These are server-side changes, not a new server APK. Native Quasar and Wear clients benefit only when their configured server runs the relevant revision. Status totals should remain usable after terminal bulk requests release their payloads, and mobile clients must still treat submission, acceptance and completion as separate states.

A phone losing connectivity is not evidence that a write was rejected. Preserve the operation identity and inspect the authorized status path before retrying a consequential submission. Nothing in these fixes grants a client broader tenant or dataset access.

## Verification

The bulk-retention PR records a RED boundary test followed by unit, integration, documentation-coverage, flake and stack checks. The quarantine PR records a concurrency regression that failed on the old code, then passing unit/integration/image checks. These are linked implementation records, not test runs performed for this post.

## Sources

Terminal request retention: <https://github.com/lost-rob0t/starintel-server/commit/1ac298b797bd4bc0e71cfde083c6a59af55ccc6f>
Cause, preserved API behavior and test evidence: <https://github.com/lost-rob0t/starintel-server/pull/190>
Quarantine concurrency and settlement: <https://github.com/lost-rob0t/starintel-server/commit/d48fa939402abf701fa1cc4079dfb8bedfad8d4a>
Concurrency regression record: <https://github.com/lost-rob0t/starintel-server/pull/188>
Search auditing and hosted activation: <https://github.com/lost-rob0t/starintel-server/commit/e49c67d88d60dbcc0fcba1b4ba76c1a0a6d6655c>
Default-off export contract: <https://github.com/lost-rob0t/starintel-server/commit/414bfba309e2c7de8a40e2625458a7c806ebbf08>
