---
name: adalterome-compare-report
description: Build two-gene AD-Alterome comparison reports. Use when the user asks to compare two genes such as APOE vs APP, MAPT vs APP, or PSEN1 vs PSEN2 using AD-Alterome overviews, shared and distinct terms, shared and distinct AD hypotheses, high-quality evidence sentences for each gene, PubMed links, mechanism differences, common patterns, and evidence limitations.
---

# AD-Alterome Compare Report

Use this skill when the user wants a structured comparison of two genes in AD-Alterome.

## Quick Start

```bash
python scripts/build_compare_report.py --gene-a APOE --gene-b APP --output-dir outputs/apoe_vs_app --top-k 8
```

Expected outputs:

- `report.md`
- `data/query.json`
- `data/compare.json`
- `data/gene_a_evidence.json`
- `data/gene_b_evidence.json`

## Workflow

1. Run the report builder with `--gene-a`, `--gene-b`, `--output-dir`, and `--top-k`.
2. Inspect `data/compare.json` for shared/distinct terms and hypotheses.
3. Inspect each gene evidence JSON for representative sentence-level records.
4. Read [references/report_contract_compare.md](references/report_contract_compare.md) before expanding the report.
5. Keep common patterns and gene-specific mechanisms separate.
6. Preserve PubMed links and original sentences for each gene.
7. Use [references/boundary_responses.md](references/boundary_responses.md) when one gene has sparse evidence or the comparison is imbalanced.

## Report Standard

The report should follow this storyline:

1. query scope and comparison frame
2. side-by-side overview
3. shared terms and shared hypotheses
4. gene-A-specific terms and hypotheses
5. gene-B-specific terms and hypotheses
6. high-quality evidence traces for each gene
7. comparative mechanism synthesis
8. limitations and follow-up priorities

## Guardrails

- Do not conclude one gene is more important solely because it has more records.
- Report literature-density bias explicitly.
- Keep evidence traces separated by gene.
- Use sentence-level evidence to support contrastive claims.

## Resources

- Builder script: [scripts/build_compare_report.py](scripts/build_compare_report.py)
- Report contract: [references/report_contract_compare.md](references/report_contract_compare.md)
- Boundary responses: [references/boundary_responses.md](references/boundary_responses.md)
