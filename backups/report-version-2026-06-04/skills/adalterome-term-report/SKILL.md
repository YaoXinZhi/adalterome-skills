---
name: adalterome-term-report
description: Build deep phenotype, ontology term, or pathological-process reports from AD-Alterome. Use when the user asks for a researcher-facing report about a phenotype such as mitochondrial dysfunction, neuroinflammation, amyloid processing, synaptic dysfunction, an HPO/GO/MeSH term, or any AD-Alterome term-centered evidence summary with API top genes, AD hypotheses, curated representative evidence, top and long-tail gene/gene-alteration/phenotype patterns, original evidence sentences, PubMed links, and follow-up interpretation.
---

# AD-Alterome Term Report

Use this skill when the user wants a deep report for one phenotype, ontology term, or pathological process rather than a short API answer.

## Quick Start

```bash
python3 scripts/build_term_report.py --term "mitochondrial dysfunction" --output-dir outputs/mitochondrial_dysfunction --selected-limit 30
```

Expected outputs:

- `report.md`
- `data/query.json`
- `data/overview.json`
- `data/evidence.json`
- `data/curation.json`

## Workflow

1. Run the report builder with `--term` and `--output-dir`; use `--selected-limit` to control displayed evidence from the server-side full-pool curation package. `--curation-limit` only controls capped event-endpoint fallback mode.
2. Inspect `data/curation.json` for selected evidence, query-relative top/long-tail patterns, evidence type groups, mechanism strata, and chronology.
3. Inspect `data/evidence.json` for returned `Evidence.sentence`, `Evidence.pubmed_url`, and original event fields.
4. Read [references/report_contract_term_deep.md](references/report_contract_term_deep.md) before expanding or revising the report.
5. Use top genes and hypotheses from `/term/overview` as aggregate context.
6. Use curated `/term/curation` rows as the source-traceable sentence layer when available; `/term/events` is a capped fallback.
7. Keep original evidence sentences and PubMed links intact.
8. Do not use or display `EvidenceScore`.
9. If selected evidence is sparse or generic, use [references/boundary_responses.md](references/boundary_responses.md) instead of overstating mechanisms.

## Report Standard

The report should follow this storyline:

1. query scope and provenance
2. global evidence landscape
3. evidence curation layer
4. mechanism-stratified evidence map
5. representative molecular and pathological evidence
6. long-tail evidence signals
7. chronological evidence trajectory
8. original evidence traces
9. interpretation guide and follow-up priorities

## Guardrails

- Do not imply every gene in a term report causally drives the phenotype.
- Separate sentence-level evidence from AD-Alterome interpretation fields.
- Use PubMed links returned by the API or generated from PMID.
- Use `curation.json` to filter broad background evidence away from molecular or model-based evidence when needed.
- Term reports deduplicate by gene + alteration taxonomy + hypothesis because the searched phenotype/term is fixed by the query.
- Deep reports prefer server-side curation endpoints, which deduplicate and sample from the complete matched query pool before returning selected evidence. REST event endpoints remain capped and are used only for lightweight retrieval or fallback.
- Genetic alteration taxonomy comes from the leading `AlterationType` value. `TriggerWord` and `RegType` are regulatory/event context, not alteration labels.
- If the term is broad, explicitly say the report is an evidence map rather than a narrow mechanistic conclusion.

## Resources

- Builder script: [scripts/build_term_report.py](scripts/build_term_report.py)
- Report contract: [references/report_contract_term_deep.md](references/report_contract_term_deep.md)
- Boundary responses: [references/boundary_responses.md](references/boundary_responses.md)
