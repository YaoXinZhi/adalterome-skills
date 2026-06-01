---
name: adalterome-api
description: Query the live AD-Alterome REST API for Alzheimer disease literature evidence. Use when Codex needs current data from an AD-Alterome API service to inspect schema, list AD hypotheses, retrieve gene-centered events, term/phenotype-centered events, hypothesis support evidence, gene/term/hypothesis overviews, compare two genes, return PubMed links, or expose exact original evidence sentences through the normalized Evidence payload.
---

# AD-Alterome API

Use this skill to query AD-Alterome through the REST API instead of guessing database contents from memory.

## Quick Start

Run the bundled script:

```bash
python scripts/query_adalterome.py schema
python scripts/query_adalterome.py hypotheses --output summary
python scripts/query_adalterome.py gene-events --gene MAPT --top-k 5 --output report
python scripts/query_adalterome.py term-events --term "mitochondrial dysfunction" --top-k 5 --output report
python scripts/query_adalterome.py hypothesis-support --hypothesis "Amyloid Hypothesis" --top-k 5 --output evidence-md
python scripts/query_adalterome.py compare --gene-a APOE --gene-b APP --output report
```

The default API base URL is `http://117.72.176.137/api/adalterome`. Override it with:

```bash
python scripts/query_adalterome.py gene-events --gene MAPT --base-url http://117.72.176.137/api/adalterome
```

Read [references/api_docs.md](references/api_docs.md) when you need endpoint details or response fields.
Read [references/output_layers.md](references/output_layers.md) when choosing `json`, `summary`, `report`, or `evidence-md`.
Read [references/boundary_responses.md](references/boundary_responses.md) when the API is unreachable, a target is absent, or evidence is too weak.

## Workflow

1. Decide whether the user needs discovery, retrieval, aggregation, or comparison.
2. Use `schema` to verify fields if the API shape is uncertain.
3. Use `hypotheses` before hypothesis search when the exact hypothesis name is unclear.
4. Use `gene-events`, `term-events`, or `hypothesis-support` for sentence-level evidence.
5. Use `gene-overview`, `term-overview`, or `hypothesis-overview` for aggregate statistics.
6. Use `compare` for two-gene shared/distinct term and hypothesis summaries.
7. Preserve `Evidence.sentence`, `Evidence.pubmed_url`, `Evidence.event`, and `EvidenceQualityScore` in user-facing answers.
8. Do not invent PubMed links; only use `PMID` or `Evidence.pubmed_url` returned by the API.

## Supported Tasks

### Browse and inspect

- `schema`
- `hypotheses`

### Retrieve evidence

- `gene-events --gene GENE`
- `term-events --term TERM`
- `hypothesis-support --hypothesis HYPOTHESIS`

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
- Use higher `--top-k` sparingly; the API already re-ranks a small candidate pool by evidence quality.

## Evidence Contract

Event-style endpoints return a normalized evidence block:

- `Evidence.sentence`: exact original sentence.
- `Evidence.rich_sentence_html`: highlighted sentence with AD-Alterome spans.
- `Evidence.pubmed_url`: direct PubMed link from PMID.
- `Evidence.article`: journal, year, MeSH, publication types, and substances when available.
- `Evidence.biological_context`: gene, alteration, trigger, term, and ontology fields.
- `Evidence.ad_interpretation`: AD hypothesis, mechanism, relevance, and explanation fields.
- `EvidenceQualityScore`: deterministic sentence-quality score used to push generic low-information sentences down.

## Fixed Report Format

When using `--output report`, preserve this section order:

1. `## Query`
2. `## API Links`
3. `## Summary`
4. `## Results`
5. `## Evidence`
6. `## Notes`

The `## API Links` section must include `api_page` and `request_url`.

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
