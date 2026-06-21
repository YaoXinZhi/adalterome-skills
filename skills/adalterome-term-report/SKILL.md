---
name: adalterome-term-report
description: Internal/advanced direct-use AD-Alterome helper for reproducible phenotype/process deep report generation. Normally do not select for ordinary user-facing AD-Alterome questions; adalterome invokes this helper after it detects a phenotype, downstream biological process, ontology term, or pathological-process query. Use directly only when the user explicitly names adalterome-term-report, asks for the term report builder script, or needs to reproduce a known phenotype/process report output contract.
---

# AD-Alterome Phenotype / Process Report

Use this skill when the user wants a deep report for one phenotype, ontology term, or pathological process rather than a short API answer.

> Direct-use boundary: this is an internal/advanced helper. For ordinary
> phenotype/process AD-Alterome questions, start from `adalterome`; use this
> skill directly only for explicit builder-script or reproducibility tasks.

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
- `data/cache_manifest.json`

## Workflow

1. Run the report builder with `--term` and `--output-dir`; `--term` is retained as the API-compatible argument for phenotype/process queries. Use `--selected-limit` to control displayed evidence from the server-side full-pool curation package. `--curation-limit` and `--top-k` are deprecated compatibility options and do not enable capped event fallback.
2. Inspect `data/curation.json` for selected evidence, query-relative top/long-tail patterns, evidence type groups, mechanism strata, and chronology.
3. Inspect `data/evidence.json` for returned `Evidence.sentence`, `Evidence.pubmed_url`, and original event fields.
4. Read [references/report_contract_term_deep.md](references/report_contract_term_deep.md) before expanding or revising the report.
5. Use top genes and hypotheses from `/term/overview` as aggregate context.
6. Use curated `/term/curation` rows as the source-traceable sentence layer when available; `/term/events` is a capped fallback.
7. Keep original evidence sentences and PubMed links intact.
8. Do not use or display `EvidenceScore`.
9. If selected evidence is sparse or generic, use [references/boundary_responses.md](references/boundary_responses.md) instead of overstating mechanisms.
10. If the user wants AD pathologist-style interpretation, long-tail candidate judgment, or a paper-level case study, route to `adalterome-case-study-expert`.

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

- Do not imply every gene in a phenotype/process report causally drives the queried phenotype.
- Separate sentence-level evidence from AD-Alterome interpretation fields.
- Use PubMed links returned by the API or generated from PMID.
- Use `curation.json` to filter broad background evidence away from molecular or model-based evidence when needed.
- Phenotype/process reports deduplicate by gene + alteration taxonomy + hypothesis because the searched phenotype/process feature is fixed by the query.
- Deep reports use server-side curation endpoints, which deduplicate and sample from the complete matched query pool before returning selected evidence. REST event endpoints remain capped legacy/debug samples and are not used as report fallback.
- Genetic alteration taxonomy comes from the leading `AlterationType` value. `TriggerWord` and `RegType` are regulatory/event context, not alteration labels.
- Deep reports save task-local JSON files and `data/cache_manifest.json`; exact raw API payloads are also kept in the shared local cache for repeat requests and manual inspection.
- If the phenotype/process feature is broad, explicitly say the report is an evidence map rather than a narrow mechanistic conclusion.
- Expert case-study interpretation lives in `adalterome-case-study-expert`; keep this phenotype/process report as the stable traceable evidence dossier.

## Resources

- Builder script: [scripts/build_term_report.py](scripts/build_term_report.py)
- Report contract: [references/report_contract_term_deep.md](references/report_contract_term_deep.md)
- Boundary responses: [references/boundary_responses.md](references/boundary_responses.md)
