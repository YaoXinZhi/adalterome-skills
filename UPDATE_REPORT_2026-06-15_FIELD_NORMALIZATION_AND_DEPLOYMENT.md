# 2026-06-15 Field Normalization and Deployment Update

## Summary

The AD-Alterome backing SQLite files were refreshed after a conservative field
normalization pass. The update fixes format drift in hypothesis-related fields
without changing sentence evidence, event metadata, or biological assertions.

## What Changed

- Normalized `Hypothesis` and `LinkedHypothesis` labels to the active AD
  hypothesis catalog.
- Sorted and deduplicated canonical multi-hypothesis combinations.
- Regenerated malformed `LinkedHypothesis` values from already-canonical
  `Hypothesis` values where this was format repair rather than biological
  reinterpretation.
- Normalized clear `DiseaseRelated` aliases and non-AD placeholder disease
  labels.
- Widened raw SQLite varchar declarations where stored content already exceeded
  historical limits; no content was truncated.
- Rebuilt and redeployed the curated evidence database used by report-grade
  curation endpoints.

## Data Integrity

Final raw database checks:

- Rows: `451307`
- Unique events: `446289`
- Distinct `Hypothesis`: `163`
- Distinct `LinkedHypothesis`: `163`
- Non-catalog `Hypothesis` rows: `0`
- Non-catalog `LinkedHypothesis` rows: `0`
- Raw DB SHA256:
  `eaaff5b2ef1e0c6dd19624a15bc6d660e39b2ae0c5d118cc939976360af22896`

Final curated database checks:

- `event_llm_annotation`: `451307`
- `event_expert_annotation_final`: `451307`
- Curated DB SHA256:
  `df5c4af818aaec3f1ef8fe8a20366cd8250fd1e83b92c15a976fc971a0457f86`

Both SQLite files passed `PRAGMA integrity_check`.

## Deployment Validation

The public API was restarted with the refreshed raw and curated databases.

PSEN1 curated evidence smoke test:

- Endpoint: `/gene/curation?gene=PSEN1&selected_limit=10&source=curated`
- Status: `ok`
- Returned selected evidence: `10`
- Raw event count: `21835`
- Curated pool count: `2398`
- Query value: `PRESENILIN 1 [Entrez:5663]`

This confirms that large-gene report paths continue to use the curated pool
rather than slow capped event endpoints.

## Notes

- Non-standard year values such as `-`, `null`, or `Unknown` were retained
  because inferring missing publication years would alter metadata provenance.
- This update affects data consistency and deployment state. The skill code
  contracts remain compatible with the 2026-06-07 skill implementation audit.
