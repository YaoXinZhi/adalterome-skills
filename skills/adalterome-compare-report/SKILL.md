---
name: adalterome-compare-report
description: Build two-gene AD-Alterome comparison reports. Use when the user asks to compare two genes such as APOE vs APP, MAPT vs APP, or PSEN1 vs PSEN2 using AD-Alterome API overviews, shared and distinct phenotype/process features, shared and distinct AD hypotheses, curated representative evidence for each gene, top and long-tail gene-alteration/phenotype patterns, PubMed links, mechanism differences, and common patterns.
---

# AD-Alterome Compare Report

Use this skill when the user wants a structured comparison of two genes in AD-Alterome.

## Quick Start

```bash
python3 scripts/build_compare_report.py --gene-a APOE --gene-b APP --output-dir outputs/apoe_vs_app --selected-limit 24
```

Expected outputs:

- `report.md`
- `data/query.json`
- `data/compare.json`
- `data/gene_a_evidence.json`
- `data/gene_b_evidence.json`
- `data/gene_a_curation.json`
- `data/gene_b_curation.json`
- `data/cache_manifest.json`

## Workflow

1. Run the report builder with `--gene-a`, `--gene-b`, and `--output-dir`; use `--selected-limit` to control displayed evidence from each server-side full-pool gene curation package. `--curation-limit` only controls capped event-endpoint fallback mode.
2. Inspect `data/compare.json` for shared/distinct phenotype/process features and hypotheses.
3. Inspect each gene curation JSON for selected evidence, query-relative top/long-tail patterns, evidence type groups, mechanism strata, and chronology.
4. Inspect each gene evidence JSON for raw sentence-level records.
5. Read [references/report_contract_compare.md](references/report_contract_compare.md) before expanding the report.
6. Keep common patterns and gene-specific mechanisms separate.
7. Preserve PubMed links and original sentences for each gene.
8. Do not use or display `EvidenceScore`.
9. Use [references/boundary_responses.md](references/boundary_responses.md) when one gene has sparse evidence or the comparison is imbalanced.
10. If the user wants an AD pathologist-style, coverage-aware paper-level comparison case study, route to `adalterome-case-study-expert`.

## Report Standard

The report should follow this storyline:

1. query scope and comparison frame
2. side-by-side overview
3. shared phenotype/process features and shared hypotheses
4. gene-A-specific phenotype/process features and hypotheses
5. gene-B-specific phenotype/process features and hypotheses
6. evidence curation layer for each gene
7. mechanism-stratified evidence map for each gene
8. representative and long-tail evidence for each gene
9. comparative interpretation guide and follow-up priorities

## Guardrails

- Do not conclude one gene is more important solely because it has more records.
- Keep evidence traces separated by gene.
- Use sentence-level evidence to support contrastive claims.
- Use each gene's `curation.json` to avoid comparing one gene's broad high-frequency records against another gene's molecular long-tail records.
- Each gene is curated with the gene-fixed event key: alteration taxonomy + phenotype/term + hypothesis.
- Deep reports prefer server-side curation endpoints, which deduplicate and sample from the complete matched query pool before returning selected evidence for each gene. REST event endpoints remain capped and are used only for lightweight retrieval or fallback.
- Deep reports save task-local JSON files and `data/cache_manifest.json`; exact raw API payloads are also kept in the shared local cache for repeat requests and manual inspection.
- Genetic alteration taxonomy comes from the leading `AlterationType` value. `TriggerWord` and `RegType` are regulatory/event context, not alteration labels.
- Expert case-study interpretation lives in `adalterome-case-study-expert`; keep this compare report as the stable traceable evidence dossier.

## Resources

- Builder script: [scripts/build_compare_report.py](scripts/build_compare_report.py)
- Report contract: [references/report_contract_compare.md](references/report_contract_compare.md)
- Boundary responses: [references/boundary_responses.md](references/boundary_responses.md)
