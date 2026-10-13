# lost-rob0t/starintel-gpt-auto-dig

- generated: `2026-10-13T16:03:16Z`
- canonical branch: `main`
- changelog eligible: `yes`
- head: [`a4309f2d1f0e4bceb9f51d56309a36e28892bf95`](https://github.com/lost-rob0t/starintel-gpt-auto-dig/commit/a4309f2d1f0e4bceb9f51d56309a36e28892bf95)
- head date: `2026-10-11T11:33:35-04:00`
- head subject: Merge pull request #2747 from lost-rob0t/fix/event-ingest-contract-regression

## Git log, last 14 days

```text
2026-10-11 a4309f2d1f0e4bceb9f51d56309a36e28892bf95 Merge pull request #2747 from lost-rob0t/fix/event-ingest-contract-regression
2026-10-11 96e7a80a642d216edbb329d50a9e8aef2c64f91a test: preserve canonical event payload on legacy ingest rejection
2026-10-11 370f532a0c7257b49cf32e68eb887c415f77d65a Merge pull request #2746 from lost-rob0t/dig/columbus-public-events-2026-10-11
2026-10-11 d138b29d52f6ceff0d495c6a7fb8eeee9cd3a59a Merge pull request #2744 from lost-rob0t/dig/columbus-election-institutions-2026-10-10
2026-10-11 dfa082a380552a5024ef30e9b79c4fa737008685 Merge pull request #2740 from lost-rob0t/codex/starintel-0101-generated-consumer
2026-10-11 6afabf0eb3c8c5f0322e6bf3740b268a3daf3992 Create one mission per event and support canonical ingestion readback
2026-10-11 40da35691c6f9aba7765fe27de867c0e0de57411 Add canonical public event targets and draft mission for Columbus
2026-10-11 7152363fb72f591251fbd6ff4d82a135ec31fd0a Correct institutional packet archive link
2026-10-10 0304e62b53dad56b7fa9a7ec62b91981e350be43 fix(site): preserve explicit public non-sensitive source annotations
2026-10-10 e7075e7c4fe3e7d9f1dcd73bff5844daae0c219e research(election26): add sourced Columbus institutions and non-destructive institutional manifest
2026-10-10 8122f715fc8b256573ac5aab7efe358125fecdb3 fix(site): preserve canonical 0.10.1 records and support exact-ID topic overlays
2026-10-11 a6c5aa93494992f6f24df700131ab9b4dcae3d26 Select legacy storage profile for historical producer imports
2026-10-11 83731efcc3a2e0b839c5654ee2fa7933dad4ea35 Validate and roll back canonical import batches as a unit
2026-10-03 fea86e4f08e37a6fcadbe28cfc173675caed71ee Install schema runtimes in the Python and native environments used by CI
2026-10-03 94b8620f6d4919f16c4c5d614d559269e56f13fc Provision pinned validators without loading optional web dependencies
2026-10-03 54e63c9bcff1c61353a3df17575d60e2d4282a94 Consume StarLang 0.10.1 and separate historical research storage
```

## Repository paths changed, last 14 days

```text
.github/workflows/auto-dig-request-check.yml
.github/workflows/dnc-key-people-wef-accountability.yml
.github/workflows/flock-dunwoody-mjcca-one-shot.yml
.github/workflows/gop-autodig-100k.yml
.github/workflows/import-starintel-documents.yml
.github/workflows/palantir-sec-principal-offices-one-shot.yml
.github/workflows/schema-release.yml
.github/workflows/sync-schema.yml
.github/workflows/temp-backlog-import.yml
.github/workflows/validate-db.yml
.github/workflows/validate-site-ui.yml
.gitignore
AGENTS.md
README.md
backend/__init__.py
backend/app.py
backend/tests/test_app.py
backend/validation.py
conformance/__init__.py
conformance/adapter.py
conformance/implementations.json
conformance/legacy_adapter.py
conformance/runner.py
digs/anarchist-violence/2026-10-10-columbus-election-institutions/README.md
digs/anarchist-violence/2026-10-10-columbus-election-institutions/adaptation-receipt.json
digs/anarchist-violence/2026-10-10-columbus-election-institutions/generate-packet.py
digs/anarchist-violence/2026-10-10-columbus-election-institutions/starintel-documents.jsonl
digs/anarchist-violence/2026-10-10-columbus-election-official-listings/README.md
digs/anarchist-violence/2026-10-10-columbus-election-official-listings/generate-packet.py
digs/anarchist-violence/2026-10-10-columbus-election-official-listings/generation-receipt.json
digs/anarchist-violence/2026-10-10-columbus-election-official-listings/observations.json
digs/anarchist-violence/2026-10-10-columbus-election-official-listings/starintel-documents.jsonl
digs/columbus/2026-10-11-public-event-announcements/README.md
digs/columbus/2026-10-11-public-event-announcements/duplicate-search.json
digs/columbus/2026-10-11-public-event-announcements/starintel-documents.jsonl
docs/election26-inventory.org
docs/election26-public-institutional-listings.org
manifests/topic-datasets.json
pyproject.toml
reports/archives/2026-10-10-columbus-election-institutions/README.md
reports/archives/2026-10-10-columbus-election-institutions/original-unpublished-packet.jsonl.txt
schema/starintel-runtime.lock.json
schema/starintel-schema.lock.json
schemas/starintel-0.10.1/compatibility-fixtures.json
schemas/starintel-0.10.1/compatibility.json
schemas/starintel-0.10.1/core.star
schemas/starintel-0.10.1/generated/portable-manifest.json
schemas/starintel-0.10.1/generated/schema.json
schemas/starintel-0.10.1/generated/starintel.lisp
schemas/starintel-0.10.1/generated/starintel_types.nim
schemas/starintel-0.10.1/generated/starintel_types.py
schemas/starintel-0.10.1/generated/starintel_types.ts
schemas/starintel-0.10.1/release-lock.json
schemas/starintel-0.10.1/schema-lock-manifest.json
scripts/build_columbus_public_events_packet.py
scripts/build_election26_manifest.py
scripts/create-db-document-legacy.py
scripts/create-db-document.py
scripts/dark_academia_memberships_core.py
scripts/dark_academia_memberships_impl.py
scripts/export_starintel_documents.py
scripts/import-starintel-documents.py
scripts/import_aleph_public.py
scripts/import_icij_offshore_leaks.py
scripts/import_wef_annual_meeting_partners.py
scripts/influencewatch/cli.py
scripts/prepare_pages_data.py
scripts/schema-release-legacy.py
scripts/schema-release.py
scripts/seed_flock_dunwoody_mjcca_camera_access.py
scripts/seed_palantir_current_news_pass.py
scripts/seed_palantir_sec_principal_offices.py
scripts/starintel_ingest_core.nim
scripts/starintel_site.nim
scripts/starintel_site/topic_datasets.py
scripts/starintel_site_entry.nim
scripts/starintel_site_projection.nim
scripts/starintel_validate.nim
scripts/sync-starintel-schema.py
scripts/validate-for-merge.py
scripts/validate_for_merge.nim
starintel-runtime.toml
starintel_auto_dig.nimble
starintel_doc/__init__.py
starintel_doc/canonical.py
starintel_doc/cli.py
starintel_doc/cli_legacy.py
starintel_doc/legacy.py
starintel_doc/storage_validation.py
starintel_doc/store.py
starintel_doc/writer.py
tests/test_aleph_import.py
tests/test_canonical_batch_import.py
tests/test_columbus_institution_packet.py
tests/test_columbus_official_listings_packet.py
tests/test_columbus_public_events_packet.py
tests/test_conformance.py
tests/test_counterevidence_packet_identity.py
tests/test_export_starintel_documents.py
tests/test_import_starintel_documents.py
tests/test_nim_site_contract.py
tests/test_operation_document.py
tests/test_schema_release.py
tests/test_scrape_wef_council_artifacts.py
tests/test_starintel_ingest_core.py
tests/test_starlang_consumer.py
tests/test_topic_datasets.py
```

## Test and CI paths touched, last 14 days

```text
.github/workflows/auto-dig-request-check.yml
.github/workflows/dnc-key-people-wef-accountability.yml
.github/workflows/flock-dunwoody-mjcca-one-shot.yml
.github/workflows/gop-autodig-100k.yml
.github/workflows/import-starintel-documents.yml
.github/workflows/palantir-sec-principal-offices-one-shot.yml
.github/workflows/schema-release.yml
.github/workflows/sync-schema.yml
.github/workflows/temp-backlog-import.yml
.github/workflows/validate-db.yml
.github/workflows/validate-site-ui.yml
backend/tests/test_app.py
scripts/build_columbus_public_events_packet.py
scripts/build_election26_manifest.py
scripts/create-db-document-legacy.py
scripts/create-db-document.py
scripts/dark_academia_memberships_core.py
scripts/dark_academia_memberships_impl.py
scripts/export_starintel_documents.py
scripts/import-starintel-documents.py
scripts/import_aleph_public.py
scripts/import_icij_offshore_leaks.py
scripts/import_wef_annual_meeting_partners.py
scripts/influencewatch/cli.py
scripts/prepare_pages_data.py
scripts/schema-release-legacy.py
scripts/schema-release.py
scripts/seed_flock_dunwoody_mjcca_camera_access.py
scripts/seed_palantir_current_news_pass.py
scripts/seed_palantir_sec_principal_offices.py
scripts/starintel_ingest_core.nim
scripts/starintel_site.nim
scripts/starintel_site/topic_datasets.py
scripts/starintel_site_entry.nim
scripts/starintel_site_projection.nim
scripts/starintel_validate.nim
scripts/sync-starintel-schema.py
scripts/validate-for-merge.py
scripts/validate_for_merge.nim
tests/test_aleph_import.py
tests/test_canonical_batch_import.py
tests/test_columbus_institution_packet.py
tests/test_columbus_official_listings_packet.py
tests/test_columbus_public_events_packet.py
tests/test_conformance.py
tests/test_counterevidence_packet_identity.py
tests/test_export_starintel_documents.py
tests/test_import_starintel_documents.py
tests/test_nim_site_contract.py
tests/test_operation_document.py
tests/test_schema_release.py
tests/test_scrape_wef_council_artifacts.py
tests/test_starintel_ingest_core.py
tests/test_starlang_consumer.py
tests/test_topic_datasets.py
```
