---
name: adalterome-hypothesis-report
description: Build deep AD hypothesis support reports from AD-Alterome. Use when the user asks for a researcher-facing report about Amyloid Hypothesis, Tau Protein Hypothesis, Neuroinflammation Hypothesis, oxidative stress, mitochondrial autophagy, vascular hypothesis, or any AD hypothesis-centered evidence summary with top genes, top terms, high-quality original sentences, PubMed links, evidence limitations, and support patterns.
---

# AD-Alterome Hypothesis Report

Use this skill when the user wants a deep report for one AD hypothesis rather than a short list of supporting records.

## Quick Start

```bash
python scripts/build_hypothesis_report.py --hypothesis "Amyloid Hypothesis" --output-dir outputs/amyloid_hypothesis --top-k 12
```

Expected outputs:

- `report.md`
- `data/query.json`
- `data/overview.json`
- `data/evidence.json`

## Workflow

1. Run the report builder with `--hypothesis`, `--output-dir`, and `--top-k`.
2. Inspect `data/overview.json` for top genes and terms.
3. Inspect `data/evidence.json` for exact sentence evidence and PubMed links.
4. Read [references/report_contract_hypothesis_deep.md](references/report_contract_hypothesis_deep.md) before expanding or revising the report.
5. Distinguish direct sentence support from AD-Alterome's curated hypothesis labels.
6. Use [references/boundary_responses.md](references/boundary_responses.md) if evidence is sparse, generic, or ambiguous.

## Report Standard

The report should follow this storyline:

1. query scope and hypothesis definition
2. executive support claim
3. top supporting genes and terms
4. evidence/source map
5. original evidence traces
6. support pattern synthesis
7. evidence strength and limitations
8. follow-up analysis priorities

## Guardrails

- Do not claim the hypothesis is proven by sentence-level database evidence.
- Report conflicting or broad evidence conservatively.
- Preserve PMID and original sentences.
- Treat `HypothesisReason` and `ExtendedExplanation` as curated interpretation, not primary experimental text.

## Resources

- Builder script: [scripts/build_hypothesis_report.py](scripts/build_hypothesis_report.py)
- Report contract: [references/report_contract_hypothesis_deep.md](references/report_contract_hypothesis_deep.md)
- Boundary responses: [references/boundary_responses.md](references/boundary_responses.md)
