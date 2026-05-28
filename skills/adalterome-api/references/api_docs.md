# AD-Alterome API Reference

## Base URL

Default local service:

```text
http://127.0.0.1:8010
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
| Term events | `GET /term/events` | `term`, `top_k` |
| Term overview | `GET /term/overview` | `term` |
| Hypothesis support | `GET /hypothesis/support` | `hypothesis`, `top_k` |
| Hypothesis overview | `GET /hypothesis/overview` | `hypothesis` |
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
- `Evidence.ad_interpretation`: hypothesis, mechanism, relevance, explanation.

## Evidence Ranking

The API retrieves a small candidate pool and re-ranks by deterministic sentence quality before returning `top_k`.
Ranking favors records whose sentences contain the target, gene, term, alteration, trigger, Event chain, AD interpretation, PMID, and suitable sentence length.

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
