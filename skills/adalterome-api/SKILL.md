---
name: adalterome-api
description: Query the live AD-Alterome REST API for Alzheimer disease literature evidence. Use when Codex needs current data from an AD-Alterome API service to inspect schema, list AD hypotheses, retrieve gene-centered events, phenotype/process-centered events, hypothesis support evidence, gene/phenotype/hypothesis overviews, compare two genes, return PubMed links, or expose exact original evidence sentences through the normalized Evidence payload.
---

# AD-Alterome API

Use this skill to query AD-Alterome through the REST API instead of guessing database contents from memory.

## Quick Start

Run the bundled script with `python3`:

```bash
python3 scripts/query_adalterome.py schema
python3 scripts/query_adalterome.py hypotheses --output summary
python3 scripts/query_adalterome.py gene-curation --gene MAPT --selected-limit 30 --source curated --output report
python3 scripts/query_adalterome.py term-curation --term "mitochondrial dysfunction" --selected-limit 30 --output report
python3 scripts/query_adalterome.py hypothesis-curation --hypothesis "Amyloid Hypothesis" --selected-limit 30 --output evidence-md
python3 scripts/query_adalterome.py compare --gene-a APOE --gene-b APP --output report
```

Legacy/debug event samples remain available for small targeted inspections:

```bash
python3 scripts/query_adalterome.py gene-events --gene MAPT --top-k 5 --output evidence-md
```

The default API base URL is `http://117.72.176.137/api/adalterome`. Override it with:

```bash
python3 scripts/query_adalterome.py gene-curation --gene MAPT --base-url http://117.72.176.137/api/adalterome
```

Read [references/api_docs.md](references/api_docs.md) when you need endpoint details or response fields.
Read [references/output_layers.md](references/output_layers.md) when choosing `json`, `summary`, `report`, or `evidence-md`.
Read [references/boundary_responses.md](references/boundary_responses.md) when the API is unreachable, a target is absent, or evidence is too weak.

Raw API payloads are cached locally by default. Exact repeat requests reuse the
cache; set `ADALTEROME_REFRESH_CACHE=1` for a fresh request, `ADALTEROME_DISABLE_CACHE=1`
to bypass caching, or `ADALTEROME_CACHE_DIR` to choose a cache directory.

## Workflow

1. Decide whether the user needs discovery, retrieval, aggregation, or comparison.
2. Use `schema` to verify fields if the API shape is uncertain.
3. Use `hypotheses` before hypothesis search when the exact hypothesis name is unclear.
4. Use `gene-curation`, `term-curation`, or `hypothesis-curation` for report-grade full-pool event deduplication, long-tail sampling, mechanism-stratified curation, and complete curated-query statistics.
5. Use `gene-overview`, `term-overview`, or `hypothesis-overview` only as auxiliary aggregate summaries when needed.
6. Use `gene-events`, `term-events`, or `hypothesis-support` only for legacy/debug small sentence samples, not for reports or large genes.
7. Use `compare` for two-gene shared/distinct phenotype/process and hypothesis summaries.
8. Preserve `Evidence.sentence`, `Evidence.pubmed_url`, and `Evidence.event` in user-facing answers.
9. Do not invent PubMed links; only use `PMID` or `Evidence.pubmed_url` returned by the API.
10. Do not display or interpret `EvidenceScore` in skill-facing reports; it may remain in raw API JSON for compatibility.
11. Tell the user where raw payloads were saved when a script output includes `## Local Data Cache` or `data/cache_manifest.json`.

## Supported Tasks

### Browse and inspect

- `schema`
- `hypotheses`

### Retrieve legacy/debug evidence samples

- `gene-events --gene GENE`
- `term-events --term TERM`
- `hypothesis-support --hypothesis HYPOTHESIS`

### Curate full-pool evidence for reports

- `gene-curation --gene GENE --selected-limit 30 --source curated`
- `term-curation --term TERM --selected-limit 30 --source curated`
- `hypothesis-curation --hypothesis HYPOTHESIS --selected-limit 30 --source curated`

### Retrieve overviews

- `gene-overview --gene GENE`
- `term-overview --term TERM`
- `hypothesis-overview --hypothesis HYPOTHESIS`

### Compare genes

- `compare --gene-a GENE --gene-b GENE`

## Output Handling

- Use `--output summary` for exploration.
- Use `--output report` for stable user-facing answers.
- Use `--output evidence-md` when the user specifically wants traceable evidence sentences and PubMed links.
- Use `--output json` when exact fields are needed or another script will consume the result.
- For deep reports, prefer the dedicated builder scripts. They use server-side curation endpoints backed by the curated SQLite pool for full-pool event deduplication, long-tail sampling, complete curated-query statistics, and source-traceable representative evidence. If a curation endpoint is unavailable, report builders return a partial report with the failure reason instead of falling back to capped event endpoints.

## Evidence Contract

Event-style endpoints return a normalized evidence block:

- `Evidence.sentence`: exact original sentence.
- `Evidence.rich_sentence_html`: highlighted sentence with AD-Alterome spans.
- `Evidence.pubmed_url`: direct PubMed link from PMID.
- `Evidence.article`: journal, year, MeSH, publication types, and substances when available.
- `Evidence.biological_context`: gene, alteration, trigger, term, and ontology fields. Treat `AlterationType` as the genetic alteration taxonomy; `TriggerWord` and `RegType` are event relation/regulation context, not alteration labels.
- `Evidence.ad_interpretation`: AD hypothesis, mechanism, relevance, and explanation fields.
- `EvidenceQualityScore`: API-side sentence-quality field; deep report curation computes its own sentence informativeness and does not rely on raw scoring fields.
- `EvidenceScore`: raw API compatibility field. Skills intentionally hide and ignore it.

## Evidence Curation Layer

Deep report skills use `scripts/evidence_fetch.py` plus `scripts/evidence_curation.py` as an intermediate layer between API retrieval and final summaries. When the API server exposes `/gene/curation`, `/term/curation`, and `/hypothesis/curation`, the builders retrieve a server-side curation package from the offline curated pool by default (`source=curated`). The curated pool is built from the complete matched query pool, applies coverage-first sampling and high-frequency downsampling, preserves long-tail evidence, and re-ranks rows with `event_expert_annotation_final`. The curation layer performs query-specific event deduplication, computes query-relative top and long-tail patterns for genes, gene-alteration pairs, phenotypes, and hypotheses where relevant, groups evidence into a small stable set of evidence types, and creates candidate mechanism strata for expert interpretation.

Curated evidence rows may include:

- `ExpertOverallScore`: 1-5 final expert score from `event_expert_annotation_final`.
- `AnnotationSource`: `llm_reviewed`, `heuristic_only`, or future human-reviewed sources.
- `AnnotationConfidence`: LLM or heuristic confidence label.
- `ExpertReason`: short rationale for LLM-reviewed rows.
- `SamplingBucket`: why the row entered the curated pool, such as phenotype coverage, gene coverage, long-tail, or recent high-quality evidence.

Use `--source raw` only when the user explicitly needs the older raw full-query curation behavior; large genes, broad terms, and broad hypotheses may be slow in raw mode. Keep `source=curated` as the default for skills and reports.

## Fixed Report Format

When using `--output report`, preserve this section order:

1. `## Query`
2. `## API Links`
3. `## Local Data Cache`
4. `## Summary`
5. `## Results`
6. `## Evidence`
7. `## Notes`

The `## API Links` section must include `api_page` and `request_url`.
The `## Local Data Cache` section must include the raw payload cache file when caching is enabled.

## Guardrails

- Treat the API as live data. Re-query instead of relying on stale memory.
- Do not treat AD-Alterome evidence as causal proof unless the sentence and interpretation fields support that claim.
- Keep weak, generic, or indirect evidence explicitly caveated.
- If the API is unreachable, report that boundary clearly and do not fabricate records.
- If a target has no records, suggest checking spelling, synonyms, or available hypotheses rather than inventing support.

## Resources

- Script entrypoint: [scripts/query_adalterome.py](scripts/query_adalterome.py)
- API reference: [references/api_docs.md](references/api_docs.md)
- Output guide: [references/output_layers.md](references/output_layers.md)
- Boundary responses: [references/boundary_responses.md](references/boundary_responses.md)
- Evidence curation helpers: [scripts/evidence_curation.py](scripts/evidence_curation.py)
- Evidence fetch helpers: [scripts/evidence_fetch.py](scripts/evidence_fetch.py)
- Local cache helpers: [scripts/query_cache.py](scripts/query_cache.py)
