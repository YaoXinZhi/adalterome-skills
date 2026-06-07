---
name: adalterome-hypothesis-report
description: Build deep AD hypothesis support reports from AD-Alterome. Use when the user asks for a researcher-facing report about Amyloid Hypothesis, Tau Protein Hypothesis, Neuroinflammation Hypothesis, oxidative stress, mitochondrial autophagy, vascular hypothesis, or any AD hypothesis-centered evidence summary with top genes, top phenotype/process features, curated representative sentences, top and long-tail gene/gene-alteration/phenotype/process patterns, PubMed links, and support patterns.
---

# AD-Alterome Hypothesis Report

Use this skill when the user wants a deep report for one AD hypothesis rather than a short list of supporting records.

## Quick Start

```bash
python3 scripts/build_hypothesis_report.py --hypothesis "Amyloid Hypothesis" --output-dir outputs/amyloid_hypothesis --selected-limit 30
```

Expected outputs:

- `report.md`
- `data/query.json`
- `data/overview.json`
- `data/evidence.json`
- `data/curation.json`
- `data/cache_manifest.json`

## Workflow

1. Run the report builder with `--hypothesis` and `--output-dir`; use `--selected-limit` to control displayed evidence from the server-side full-pool curation package. `--curation-limit` only controls capped event-endpoint fallback mode.
2. Inspect `data/overview.json` for top genes and phenotype/process features.
3. Inspect `data/curation.json` for selected evidence, query-relative top/long-tail patterns, evidence type groups, mechanism strata, and chronology.
4. Inspect `data/evidence.json` for exact sentence evidence and PubMed links.
5. Read [references/report_contract_hypothesis_deep.md](references/report_contract_hypothesis_deep.md) before expanding or revising the report.
6. Distinguish direct sentence support from AD-Alterome's curated hypothesis labels.
7. Do not use or display `EvidenceScore`.
8. Use [references/boundary_responses.md](references/boundary_responses.md) if evidence is sparse, generic, or ambiguous.
9. If the user wants AD pathologist-style interpretation, long-tail candidate judgment, or a paper-level case study, route to `adalterome-case-study-expert`.

## Report Standard

The report should follow this storyline:

1. query scope and hypothesis definition
2. global evidence landscape
3. evidence curation layer
4. mechanism-stratified evidence map
5. representative support evidence
6. long-tail evidence signals
7. chronological evidence trajectory
8. original evidence traces
9. interpretation guide and follow-up priorities

## Guardrails

- Do not claim the hypothesis is proven by sentence-level database evidence.
- Report conflicting or broad evidence conservatively.
- Preserve PMID and original sentences.
- Treat `HypothesisReason` and `ExtendedExplanation` as curated interpretation, not primary experimental text.
- Use `curation.json` to separate broad background support from molecular, alteration, pathway, model, or clinical evidence.
- Hypothesis reports deduplicate by gene + alteration taxonomy + phenotype/term because the hypothesis is fixed by the query.
- Deep reports prefer server-side curation endpoints, which deduplicate and sample from the complete matched query pool before returning selected evidence. REST event endpoints remain capped and are used only for lightweight retrieval or fallback.
- Deep reports save task-local JSON files and `data/cache_manifest.json`; exact raw API payloads are also kept in the shared local cache for repeat requests and manual inspection.
- Genetic alteration taxonomy comes from the leading `AlterationType` value. `TriggerWord` and `RegType` are regulatory/event context, not alteration labels.
- Expert case-study interpretation lives in `adalterome-case-study-expert`; keep this hypothesis report as the stable traceable evidence dossier.

## Resources

- Builder script: [scripts/build_hypothesis_report.py](scripts/build_hypothesis_report.py)
- Report contract: [references/report_contract_hypothesis_deep.md](references/report_contract_hypothesis_deep.md)
- Boundary responses: [references/boundary_responses.md](references/boundary_responses.md)
