---
name: adalterome-gene-report
description: Internal/advanced direct-use AD-Alterome helper for reproducible one-gene deep report generation. Normally do not select for ordinary user-facing AD-Alterome questions; adalterome invokes this helper after it detects a gene query. Use directly only when the user explicitly names adalterome-gene-report, asks for the gene report builder script, or needs to reproduce a known one-gene report output contract.
---

# AD-Alterome Gene Report

Use this skill when the user wants a research-style report for one AD-related gene, not a short API answer.

> Direct-use boundary: this is an internal/advanced helper. For ordinary
> one-gene AD-Alterome questions, start from `adalterome`; use this skill
> directly only for explicit builder-script or reproducibility tasks.

## Workflow

1. Run the report builder script with `--gene` and `--output-dir`; use `--selected-limit` to control displayed evidence from the server-side full-pool curation package. `--curation-limit` and `--top-k` are deprecated compatibility options and do not enable capped event fallback.
2. Inspect `data/curation.json`, `data/evidence.json`, and `data/overview.json`.
3. Read [references/report_contract_gene_deep.md](references/report_contract_gene_deep.md), [references/evidence_schema.md](references/evidence_schema.md), and [references/final_report_playbook.md](references/final_report_playbook.md).
4. Expand `report.md` into a researcher-level final report if the user needs more depth.
5. Keep exact original evidence sentences and PubMed links traceable.
6. Do not use or display `EvidenceScore`; calibrate claims by exact sentence content, provenance, curation reasons, sentence informativeness, `MechanismProvided`, `RelevantToAD`, and whether the original sentence supports causality.
7. If evidence is sparse or generic, use [references/boundary_responses.md](references/boundary_responses.md) instead of padding unsupported claims.
8. If the user wants the skill to act like an AD pathologist and write a paper-level scientific case study, route to `adalterome-case-study-expert`.

## Quick Start

```bash
python3 scripts/build_gene_report.py --gene MAPT --output-dir outputs/mapt_deep --selected-limit 30
```

Expected outputs:

- `report.md`
- `data/query.json`
- `data/overview.json`
- `data/evidence.json`
- `data/curation.json`
- `data/cache_manifest.json`

Optional API override:

```bash
python3 scripts/build_gene_report.py --gene APOE --base-url http://117.72.176.137/api/adalterome --output-dir outputs/apoe_deep
```

## Report Standard

The final report should follow this storyline:

1. query scope and data provenance
2. global evidence landscape
3. evidence curation layer
4. mechanism-stratified evidence map
5. representative molecular and pathological evidence
6. long-tail evidence signals
7. chronological evidence trajectory
8. original evidence traces
9. interpretation guide and follow-up priorities

## Current Boundaries

- AD-Alterome is a curated sentence-level evidence source, not a full-text causal validation system.
- PubMed links come from PMID and do not imply full article access.
- Deep reports use their own sentence informativeness score for curation; API `EvidenceQualityScore` may exist in raw JSON but is not treated as proof strength.
- `EvidenceScore` may exist in raw API JSON but is ignored by this skill.
- `--top-k` is retained only as a deprecated alias for fallback event-endpoint sampling; do not use it to mean final report length.
- Deep reports use server-side curation endpoints, which deduplicate and sample from the complete matched query pool before returning selected evidence. REST event endpoints remain capped legacy/debug samples and are not used as report fallback.
- Deep reports save task-local JSON files and `data/cache_manifest.json`; exact raw API payloads are also kept in the shared local cache for repeat requests and manual inspection.
- Genetic alteration taxonomy comes from the leading `AlterationType` value. `TriggerWord` and `RegType` are regulatory/event context, not alteration labels.
- Generic sentences may still appear when the database has limited high-information evidence.
- External enrichment such as UniProt, NCBI Gene, GWAS Catalog, or OpenTargets should be reported separately if added.
- Expert case-study interpretation lives in `adalterome-case-study-expert`; keep this gene report as the stable traceable evidence dossier.

## Resources

- Builder script: [scripts/build_gene_report.py](scripts/build_gene_report.py)
- Deep report contract: [references/report_contract_gene_deep.md](references/report_contract_gene_deep.md)
- Evidence schema: [references/evidence_schema.md](references/evidence_schema.md)
- Final report playbook: [references/final_report_playbook.md](references/final_report_playbook.md)
- Boundary responses: [references/boundary_responses.md](references/boundary_responses.md)
