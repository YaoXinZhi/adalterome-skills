# AD-Alterome API Reference

## Base URL

Default public service:

```text
http://117.72.176.137/api/adalterome
```

Override with `--base-url` or `ADALTEROME_API_BASE_URL`.

## Endpoints

| Purpose | Method and Path | Parameters |
| --- | --- | --- |
| Service index | `GET /` | none |
| Health | `GET /health` | none |
| Schema | `GET /schema` | none |
| Hypothesis catalog | `GET /hypotheses` | none |
| Gene events | `GET /gene/events` | `gene`, `top_k` |
| Gene overview | `GET /gene/overview` | `gene` |
| Gene full-pool curation | `GET /gene/curation` | `gene`, `selected_limit` |
| Term events | `GET /term/events` | `term`, `top_k` |
| Term overview | `GET /term/overview` | `term` |
| Term full-pool curation | `GET /term/curation` | `term`, `selected_limit` |
| Hypothesis support | `GET /hypothesis/support` | `hypothesis`, `top_k` |
| Hypothesis overview | `GET /hypothesis/overview` | `hypothesis` |
| Hypothesis full-pool curation | `GET /hypothesis/curation` | `hypothesis`, `selected_limit` |
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

The REST API event endpoints retrieve a limited candidate pool and re-rank by deterministic sentence quality before returning `top_k`. Public event endpoints currently cap `top_k` at 50 and are intended for lightweight sentence inspection.
Ranking favors records whose sentences contain the target, gene, term, alteration, trigger, Event chain, AD interpretation, PMID, and suitable sentence length.

## Full-Pool Curation Endpoints

Deep report builders should use `/gene/curation`, `/term/curation`, and `/hypothesis/curation` when available. These endpoints run on the API server against the complete matched query pool before returning a compact curation package.

For example, `GET /term/curation?term=mitochondrial+dysfunction&selected_limit=30` uses all records matched by the term query, then returns:

- `coverage_scope`: query type, matched event count, curation pool size, and source scope.
- `deduplication_summary`: event-unique row count, query-specific deduplication key, unique PMIDs, genes, phenotypes, alteration taxonomies, gene-alteration pairs, and hypotheses.
- `dominant_clusters`: top PMIDs, genes, phenotypes, gene-alteration pairs, alteration taxonomies, evidence types, and mechanism strata.
- `query_relative_patterns`: top and long-tail genes, gene-alteration pairs, phenotypes, and/or hypotheses according to the query type.
- `long_tail_definition`: frequency threshold rule, currently query-specific frequency `<= min(Q25, 10)` after event-level deduplication.
- `selected_evidence`: diverse representative evidence rows with PubMed links, original sentence, evidence type, candidate mechanism strata, long-tail signals, and curation reasons.

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
