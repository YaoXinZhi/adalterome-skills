# AD-Alterome API Reference

## Base URL

Default public service:

```text
http://117.72.176.137/api/adalterome
```

Override with `--base-url` or `ADALTEROME_API_BASE_URL`.

## Local Request Cache

Skill scripts cache raw API JSON payloads locally by exact request URL.

- Default cache directory: `~/.adalterome-skills/cache`
- Override cache directory: `ADALTEROME_CACHE_DIR=/path/to/cache`
- Force a fresh remote request: `ADALTEROME_REFRESH_CACHE=1`
- Bypass caching: `ADALTEROME_DISABLE_CACHE=1`
- Default maximum cache age: 30 days; override with `ADALTEROME_CACHE_MAX_AGE_DAYS`

When caching is enabled, returned payloads include `meta._local_cache` with the
cache file path, cache hit status, index file, and saved time. Report builders
also write `data/cache_manifest.json` into the task output directory.

## Endpoints

| Purpose | Method and Path | Parameters |
| --- | --- | --- |
| Service index | `GET /` | none |
| Health | `GET /health` | none |
| Schema | `GET /schema` | none |
| Hypothesis catalog | `GET /hypotheses` | none |
| Gene events (legacy/debug sample) | `GET /gene/events` | `gene`, `top_k` |
| Gene overview | `GET /gene/overview` | `gene` |
| Gene curation | `GET /gene/curation` | `gene`, `selected_limit`, `source` |
| Term events | `GET /term/events` | `term`, `top_k` |
| Term overview | `GET /term/overview` | `term` |
| Term curation | `GET /term/curation` | `term`, `selected_limit`, `source` |
| Hypothesis support | `GET /hypothesis/support` | `hypothesis`, `top_k` |
| Hypothesis overview | `GET /hypothesis/overview` | `hypothesis` |
| Hypothesis curation | `GET /hypothesis/curation` | `hypothesis`, `selected_limit`, `source` |
| Gene comparison | `GET /compare/genes` | `gene_a`, `gene_b` |

## General Response Shape

```json
{
  "tool": "query_gene_events",
  "status": "ok",
  "query": {"gene": "MAPT", "top_k": 10},
  "count": 10,
  "data": {},
  "meta": {}
}
```

## Event Evidence Shape

Event endpoints return flat legacy fields plus a normalized `Evidence` block.

Important fields:

- `Sentence`: exact original sentence.
- `RichSentence`: highlighted HTML sentence.
- `PMID`: PubMed ID.
- `EvidenceQualityScore`: deterministic quality score for sentence usefulness.
- `Evidence.sentence`: exact original sentence.
- `Evidence.rich_sentence_html`: highlighted HTML sentence.
- `Evidence.pubmed_url`: direct PubMed link.
- `Evidence.article`: journal, year, MeSH, PubTypes, substances.
- `Evidence.biological_context`: gene, alteration, trigger, term, ontology context.
- `AlterationType`: genetic alteration taxonomy. When a value contains pipe-separated context, use the leading taxonomy segment only.
- `AlterationMention` and `AlterationID`: sentence mention and identifier/context for the alteration.
- `TriggerWord` and `RegType`: event relation/regulation context, not genetic alteration labels.
- `Evidence.ad_interpretation`: hypothesis, mechanism, relevance, explanation.

## Evidence Ranking

The REST API event endpoints retrieve a limited candidate pool and re-rank by deterministic sentence quality before returning `top_k`. Public event endpoints currently cap `top_k` at 50 and are intended for legacy/debug sentence inspection, not report-grade evidence selection or large-gene case studies.
Ranking favors records whose sentences contain the target, gene, term, alteration, trigger, Event chain, AD interpretation, PMID, and suitable sentence length.

## Full-Pool Curation Endpoints

Deep report builders should use `/gene/curation`, `/term/curation`, and `/hypothesis/curation`. These endpoints default to `source=curated`: the API reads the offline curated evidence pool built from complete query pools, then hydrates selected raw event IDs for exact sentences and PubMed links. If curation is unavailable, report builders should emit a partial report with the curation failure reason rather than falling back to capped event endpoints. Use `source=raw` only for compatibility or debugging; broad raw queries can be slow.

For example, `GET /term/curation?term=mitochondrial+dysfunction&selected_limit=30&source=curated` uses the curated term pool, filters alias-expanded rows back to the requested term fields, and returns:

- `coverage_scope`: query type, curation source/scope, curated pool size, annotation source, and matched event count when exact raw count is available. For alias-merged term queries, `curated_query_stats_raw_event_count` is reported separately because canonical term pools can overlap or broaden the natural-language alias.
- `global_statistics`: complete curated-query statistics from `curated_query_stats`, including raw/event-unique counts, complete-pool top genes, phenotypes, gene-alteration pairs, alteration taxonomies, hypotheses, evidence types, mechanism strata, coverage summaries, alteration interpretation, and sampling policy.
- `deduplication_summary`: event-unique row count, query-specific deduplication key, unique PMIDs, genes, phenotypes, alteration taxonomies, gene-alteration pairs, and hypotheses.
- `dominant_clusters`: top PMIDs, genes, phenotypes, gene-alteration pairs, alteration taxonomies, evidence types, and mechanism strata.
- `query_relative_patterns`: top and long-tail genes, gene-alteration pairs, phenotypes, and/or hypotheses according to the query type.
- `long_tail_definition`: frequency threshold rule, currently query-specific frequency `<= min(Q25, 10)` after event-level deduplication.
- `selected_evidence`: diverse representative evidence rows with PubMed links, original sentence, evidence type, candidate mechanism strata, expert 1-5 score, annotation source/confidence, long-tail signals, and curation reasons.
- `final_annotation_summary`: selected row counts by `AnnotationSource` and `AnnotationConfidence`.

Use `global_statistics` for complete query-pool distributions. Use
`dominant_clusters`, `query_relative_patterns`, and `selected_evidence` for the
bounded representative evidence package returned to a report.

Hypothesis fields in the source SQLite table can contain comma-separated multiple
hypotheses. The API and skill curation layer split those values before catalog
listing, unique counts, top-hypothesis aggregation, long-tail hypothesis detection,
and representative-evidence diversity quotas.

The curation endpoint deliberately returns a bounded interpreted package rather than all raw rows. Raw `EvidenceScore` may still exist in compatibility event endpoints, but it is not used in curation decisions or skill-facing summaries.

## Error Boundary

Missing entities usually return HTTP 200 with:

```json
{
  "status": "error",
  "count": 0,
  "data": {},
  "meta": {"message": "gene not found"}
}
```
