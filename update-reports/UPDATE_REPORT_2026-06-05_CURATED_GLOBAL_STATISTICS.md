# 2026-06-05 Curated Global Statistics Update

## Summary

This update makes report-grade curation responses expose complete offline query-pool statistics through `data.curation.global_statistics`.

The previous curated response already selected evidence from the offline curated pool and used `event_expert_annotation_final`, but skill reports could still over-emphasize the bounded representative evidence rows because `global_statistics` was empty in curated mode. The API now surfaces `curated_query_stats` directly, and the skill report renderer displays complete-pool distributions separately from selected evidence distributions.

## What Changed

- API curation endpoints now populate `global_statistics` from `curated_query_stats`.
- `global_statistics.summary` reports:
  - raw matched event records
  - event-unique records
  - candidate event records
  - curated pool records
  - high-quality, long-tail, and broad-background counts
- `global_statistics` also exposes complete-pool top:
  - genes
  - phenotypes
  - gene-alteration pairs
  - alteration taxonomies
  - hypotheses
  - evidence types
  - mechanism strata
- Skill reports now render a `Complete query-pool statistics` section before representative evidence tables.
- API reference docs now clarify that `global_statistics` is the complete query-pool distribution, while `dominant_clusters` and `selected_evidence` describe the bounded hydrated representative package.

## Validation

Local HTTP smoke tests against API version `0.4.1` passed:

```text
MAPT gene curation:
  curation_source=curated_pool
  raw_event_count=27921
  curated_pool_count=2687
  top_gene_alteration=MAPT / point mutations:mutations

mitochondrial dysfunction term curation:
  curation_source=curated_pool
  raw_event_count=4159
  curated_pool_count=858
  curated_filtered_pool_rows=244
  top_gene=MAPT [Entrez:4137]

Tau Protein Hypothesis curation:
  curation_source=curated_pool
  raw_event_count=38095
  curated_pool_count=4921
```

The local skill report preview now includes:

```text
### Complete query-pool statistics
- Statistics source: curated_query_stats.
- Raw matched event records: 27921.
- Event-unique records before final representative sampling: 8014.
- Curated pool records available to the API: 2687.
- Selected evidence below is a representative expert-reviewed subset, not the full query distribution.
```

## Boundary

This update does not rebuild the curated SQLite pool and does not change event selection logic. It only exposes and renders the full curated-query statistics already stored in the offline database.
