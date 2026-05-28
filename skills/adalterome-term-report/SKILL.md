---
name: adalterome-term-report
description: Build deep phenotype, ontology term, or pathological-process reports from AD-Alterome. Use when the user asks for a researcher-facing report about a phenotype such as mitochondrial dysfunction, neuroinflammation, amyloid processing, synaptic dysfunction, an HPO/GO/MeSH term, or any AD-Alterome term-centered evidence summary with top genes, AD hypotheses, original evidence sentences, PubMed links, evidence-quality caveats, and follow-up interpretation.
---

# AD-Alterome Term Report

Use this skill when the user wants a deep report for one phenotype, ontology term, or pathological process rather than a short API answer.

## Quick Start

```bash
python scripts/build_term_report.py --term "mitochondrial dysfunction" --output-dir outputs/mitochondrial_dysfunction --top-k 12
```

Expected outputs:

- `report.md`
- `data/query.json`
- `data/overview.json`
- `data/evidence.json`

## Workflow

1. Run the report builder with `--term`, `--output-dir`, and `--top-k`.
2. Inspect `data/evidence.json` for returned `Evidence.sentence`, `Evidence.pubmed_url`, and `EvidenceQualityScore`.
3. Read [references/report_contract_term_deep.md](references/report_contract_term_deep.md) before expanding or revising the report.
4. Use top genes and hypotheses from `/term/overview` as aggregate context.
5. Use `/term/events` evidence rows as the source-traceable sentence layer.
6. Keep original evidence sentences and PubMed links intact.
7. If selected evidence is sparse or generic, use [references/boundary_responses.md](references/boundary_responses.md) instead of overstating mechanisms.

## Report Standard

The report should follow this storyline:

1. query scope and provenance
2. term-centered executive claim
3. top genes and hypotheses
4. high-quality evidence table
5. original evidence traces
6. mechanism and pathway interpretation
7. evidence limitations
8. follow-up research priorities

## Guardrails

- Do not imply every gene in a term report causally drives the phenotype.
- Separate sentence-level evidence from AD-Alterome interpretation fields.
- Use PubMed links returned by the API or generated from PMID.
- If the term is broad, explicitly say the report is an evidence map rather than a narrow mechanistic conclusion.

## Resources

- Builder script: [scripts/build_term_report.py](scripts/build_term_report.py)
- Report contract: [references/report_contract_term_deep.md](references/report_contract_term_deep.md)
- Boundary responses: [references/boundary_responses.md](references/boundary_responses.md)
