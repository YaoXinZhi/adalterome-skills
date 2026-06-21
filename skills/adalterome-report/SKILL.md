---
name: adalterome-report
description: Internal/advanced direct-use AD-Alterome fixed-report formatter for reproducible evidence packets. Normally do not select for ordinary user-facing AD-Alterome questions; adalterome invokes this helper after routing. Use directly only when the user explicitly names adalterome-report, asks for the fixed report output contract, or needs to reproduce a known fixed-format report from API results.
---

# AD-Alterome Report

Use this skill for stable presentation and reporting. Fetch data through the sibling `adalterome-api` skill and keep the output format fixed.

> Direct-use boundary: this is an internal/advanced report formatter. For
> ordinary user-facing AD-Alterome questions, start from `adalterome`; use this
> skill directly only for explicit fixed-report or reproducibility tasks.

## Quick Start

Use the installed API script with `--output report`:

```bash
python3 ../adalterome-api/scripts/query_adalterome.py gene-curation --gene MAPT --selected-limit 30 --output report
python3 ../adalterome-api/scripts/query_adalterome.py term-curation --term "mitochondrial dysfunction" --selected-limit 30 --output report
python3 ../adalterome-api/scripts/query_adalterome.py hypothesis-curation --hypothesis "Tau Protein Hypothesis" --selected-limit 30 --output report
python3 ../adalterome-api/scripts/query_adalterome.py compare --gene-a APOE --gene-b APP --output report
```

Read [references/output_contract.md](references/output_contract.md) before changing the report section order.
Read [../adalterome-api/references/api_docs.md](../adalterome-api/references/api_docs.md) when exact endpoint or evidence field behavior matters.

## Workflow

1. Identify whether the user wants a gene, phenotype/process, hypothesis, or comparison report.
2. Use `adalterome-api` curation endpoints with `--output report`; reserve event-style endpoints for explicit legacy/debug sentence samples.
3. Preserve the fixed section order from the script output.
4. Keep PubMed links and exact original sentences in `## Evidence`.
5. If adding interpretation, append it after the fixed report or under `## Notes`; do not rewrite the evidence.
6. If the user wants a multi-section researcher-facing gene analysis with mechanisms, evidence strength, and gaps, route to `adalterome-gene-report`.
7. If the user asks for a paper-level case study, AD pathology expert interpretation, biological insight, or a scientific argument, route to `adalterome-case-study-expert` instead of this fixed report skill.

## Use Cases

- gene-centered evidence reports
- phenotype, biological process, or ontology term evidence reports
- AD hypothesis support summaries
- two-gene comparison summaries
- standardized evidence excerpts for manuscript planning or database QA

## Required Sections

When delivering a report, keep these sections:

1. `## Query`
2. `## API Links`
3. `## Local Data Cache`
4. `## Summary`
5. `## Results`
6. `## Evidence`
7. `## Notes`

## Guardrails

- Do not invent records absent from the API response.
- Do not drop `request_url`; it is the reproducibility link.
- Do not drop `## Local Data Cache`; it tells users where the raw API payload was saved or reused.
- Do not silently remove PMID or PubMed links.
- Do not display or interpret `EvidenceScore`; it is a raw API compatibility field.
- Do not turn weak sentence-level associations into strong causality.
- Do not use capped event endpoints as report fallback when curation is unavailable; report the curation failure boundary instead.
- Do not use this brief report skill for a deep researcher-facing gene dossier; use `adalterome-gene-report`.

## Resources

- Output contract: [references/output_contract.md](references/output_contract.md)
- Data fetcher: `../adalterome-api/scripts/query_adalterome.py`
