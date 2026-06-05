# 2026-06-05 Curated Pool and Final Annotation Update

## Summary

This update aligns the AD-Alterome skills with the new API curation behavior:
report-grade curation now defaults to the offline curated evidence pool and uses
`event_expert_annotation_final` for evidence type, mechanism strata, expert
score, and annotation provenance.

## What Changed

- `gene-curation`, `term-curation`, and `hypothesis-curation` now send
  `source=curated` by default.
- The skill API script accepts `--source curated|raw`.
- Curated reports display:
  - `ExpertOverallScore`
  - `AnnotationSource`
  - `AnnotationConfidence`
  - `ExpertReason` when available
  - `SamplingBucket`
- Skill documentation now explains that curated evidence is preselected from
  complete query pools, then re-ranked using final expert annotation.
- `--source raw` remains available for compatibility and debugging, but broad
  raw queries may be slow.

## API Behavior Expected by the Skills

The public API curation response should include:

- `coverage_scope.curation_source = curated_pool`
- `coverage_scope.annotation_source = event_expert_annotation_final`
- `selected_evidence[].ExpertOverallScore`
- `selected_evidence[].AnnotationSource`
- `selected_evidence[].AnnotationConfidence`
- `final_annotation_summary`

Rows marked `llm_reviewed_invalid` are excluded from report-grade curated
evidence by default.

## Validation

Local API smoke tests against the updated backend passed for:

- `MAPT` gene curation
- `APOE` gene curation
- `mitochondrial dysfunction` term curation
- `Tau Protein Hypothesis` hypothesis curation

All four returned `curation_source=curated_pool`, used
`event_expert_annotation_final`, and returned selected evidence with
`ExpertOverallScore` plus annotation provenance.

## Notes

For alias-merged term queries, the API reports `curated_query_stats_raw_event_count`
separately because canonical term pools can overlap or broaden a natural-language
term alias. The actual curated rows used for report generation are exposed via
`curated_filtered_pool_rows` and the event-level deduplication summary.
