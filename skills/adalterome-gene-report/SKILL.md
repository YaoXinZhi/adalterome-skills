---
name: adalterome-gene-report
description: Build deep researcher-facing AD-Alterome gene reports from one Alzheimer disease gene query. Use when the user wants a multi-section Markdown/DOCX-ready literature evidence report with AD-Alterome gene overview, high-quality sentence evidence, PubMed links, term and hypothesis interpretation, mechanism synthesis, evidence-strength caveats, original sentence traces, comparison-ready context, and follow-up research gaps.
---

# AD-Alterome Gene Report

Use this skill when the user wants a research-style report for one AD-related gene, not a short API answer.

## Workflow

1. Run the report builder script with `--gene`, `--output-dir`, and an evidence `--top-k`.
2. Inspect `data/evidence.json` and `data/overview.json`.
3. Read [references/report_contract_gene_deep.md](references/report_contract_gene_deep.md), [references/evidence_schema.md](references/evidence_schema.md), and [references/final_report_playbook.md](references/final_report_playbook.md).
4. Expand `report.md` into a researcher-level final report if the user needs more depth.
5. Keep exact original evidence sentences and PubMed links traceable.
6. Calibrate claims by `EvidenceScore`, `EvidenceQualityScore`, `MechanismProvided`, `RelevantToAD`, and whether the original sentence supports causality.
7. If evidence is sparse or generic, use [references/boundary_responses.md](references/boundary_responses.md) instead of padding unsupported claims.

## Quick Start

```bash
python scripts/build_gene_report.py --gene MAPT --output-dir outputs/mapt_deep --top-k 12
```

Expected outputs:

- `report.md`
- `data/query.json`
- `data/overview.json`
- `data/evidence.json`

Optional API override:

```bash
python scripts/build_gene_report.py --gene APOE --base-url http://127.0.0.1:8010 --output-dir outputs/apoe_deep
```

## Report Standard

The final report should follow this storyline:

1. query scope and data provenance
2. executive claim
3. evidence/source map
4. high-quality evidence table
5. phenotype and ontology-term interpretation
6. AD hypothesis interpretation
7. mechanism synthesis
8. evidence strength and limitations
9. research gaps and follow-up priorities

## Current Boundaries

- AD-Alterome is a curated sentence-level evidence source, not a full-text causal validation system.
- PubMed links come from PMID and do not imply full article access.
- `EvidenceQualityScore` improves sentence selection but cannot replace expert curation.
- Generic sentences may still appear when the database has limited high-information evidence.
- External enrichment such as UniProt, NCBI Gene, GWAS Catalog, or OpenTargets should be reported separately if added.

## Resources

- Builder script: [scripts/build_gene_report.py](scripts/build_gene_report.py)
- Deep report contract: [references/report_contract_gene_deep.md](references/report_contract_gene_deep.md)
- Evidence schema: [references/evidence_schema.md](references/evidence_schema.md)
- Final report playbook: [references/final_report_playbook.md](references/final_report_playbook.md)
- Boundary responses: [references/boundary_responses.md](references/boundary_responses.md)
