---
name: adalterome-report
description: Turn AD-Alterome API results into fixed-format user-facing evidence reports. Use when the user wants a stable gene report, phenotype or term report, AD hypothesis support report, two-gene comparison report, evidence summary with PubMed links, or any AD-Alterome output whose section order, query provenance, original sentence evidence, and caveats should remain consistent across turns.
---

# AD-Alterome Report

Use this skill for stable presentation and reporting. Fetch data through the sibling `adalterome-api` skill and keep the output format fixed.

## Quick Start

Use the installed API script with `--output report`:

```bash
python3 ../adalterome-api/scripts/query_adalterome.py gene-events --gene MAPT --top-k 5 --output report
python3 ../adalterome-api/scripts/query_adalterome.py term-events --term "mitochondrial dysfunction" --top-k 5 --output report
python3 ../adalterome-api/scripts/query_adalterome.py hypothesis-support --hypothesis "Tau Protein Hypothesis" --top-k 5 --output report
python3 ../adalterome-api/scripts/query_adalterome.py compare --gene-a APOE --gene-b APP --output report
```

Read [references/output_contract.md](references/output_contract.md) before changing the report section order.
Read [../adalterome-api/references/api_docs.md](../adalterome-api/references/api_docs.md) when exact endpoint or evidence field behavior matters.

## Workflow

1. Identify whether the user wants a gene, term, hypothesis, or comparison report.
2. Use `adalterome-api` with `--output report`.
3. Preserve the fixed section order from the script output.
4. Keep PubMed links and exact original sentences in `## Evidence`.
5. If adding interpretation, append it after the fixed report or under `## Notes`; do not rewrite the evidence.
6. If the user wants a multi-section researcher-facing gene analysis with mechanisms, evidence strength, and gaps, route to `adalterome-gene-report`.

## Use Cases

- gene-centered evidence reports
- phenotype or ontology term evidence reports
- AD hypothesis support summaries
- two-gene comparison summaries
- standardized evidence excerpts for manuscript planning or database QA

## Required Sections

When delivering a report, keep these sections:

1. `## Query`
2. `## API Links`
3. `## Summary`
4. `## Results`
5. `## Evidence`
6. `## Notes`

## Guardrails

- Do not invent records absent from the API response.
- Do not drop `request_url`; it is the reproducibility link.
- Do not silently remove PMID or PubMed links.
- Do not display or interpret `EvidenceScore`; it is a raw API compatibility field.
- Do not turn weak sentence-level associations into strong causality.
- Do not use this brief report skill for a deep researcher-facing gene dossier; use `adalterome-gene-report`.

## Resources

- Output contract: [references/output_contract.md](references/output_contract.md)
- Data fetcher: `../adalterome-api/scripts/query_adalterome.py`
