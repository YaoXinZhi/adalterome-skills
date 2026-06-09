---
name: adalterome-case-study-expert
description: Build AD pathologist-style AD-Alterome case-study reports. Use when the user asks for a paper-level case study, expert interpretation, biological insight, AD pathology framing, disease-mechanism comparison, evidence prioritization, long-tail candidate interpretation, coverage/balance-aware synthesis, or a report that should argue a scientific question using AD-Alterome evidence rather than only listing traceable records.
---

# AD-Alterome Case Study Expert

Use this skill when the user wants AD-Alterome evidence interpreted as a scientific case study, not only a stable evidence report.

This skill is the expert layer above the report skills. It keeps AD-Alterome first, preserves traceability, and calls the reusable AD expert pruning layer over curated candidate evidence before writing the case-study narrative.

## When To Use

Use this expert skill for:

- paper-level case studies
- AD pathology expert interpretation
- gene, term, hypothesis, or two-gene questions that need a scientific argument
- questions asking for mechanism differences, biological insight, or disease-pathology interpretation
- long-tail candidate triage
- molecular pathological mechanism screening
- coverage-aware and balance-aware comparison reports

Use the existing `adalterome-*-report` skills instead when the user asks for a pure evidence packet, fixed report, API trace, PMID table, or raw source-backed dossier for human experts to interpret later.

## Quick Start

Gene-centered case study:

```bash
python3 scripts/build_case_study_expert.py --gene MAPT --question "What does MAPT evidence reveal about tau-centered AD pathology?" --output-dir outputs/mapt_case_study --candidate-limit 200 --expert-limit 18
```

Two-gene case study:

```bash
python3 scripts/build_case_study_expert.py --gene-a APOE --gene-b APP --question "How do APOE and APP differ in AD pathological mechanisms?" --output-dir outputs/apoe_app_case_study --candidate-limit 200 --expert-limit 20
```

Term or hypothesis case study:

```bash
python3 scripts/build_case_study_expert.py --term "mitochondrial dysfunction" --output-dir outputs/mitochondrial_case_study
python3 scripts/build_case_study_expert.py --hypothesis "Neuroinflammation Hypothesis" --output-dir outputs/neuroinflammation_case_study
```

Expected outputs:

- `case_study_report.md`
- `data/query.json`
- `data/case_study.json`
- `data/expert_evidence.json`
- `data/ad_expert_pruning.json`
- `data/merged_evidence.json`
- `data/excluded_or_deprioritized_evidence.json`
- `data/coverage.json`
- `data/cache_manifest.json`
- source payload JSON files for each target

## Workflow

1. Identify the user's scientific question before fetching evidence.
2. Choose the case-study frame:
   - `--gene` for one gene
   - `--term` for a phenotype, ontology term, or pathological process
   - `--hypothesis` for one AD hypothesis
   - `--gene-a` and `--gene-b` for a balanced two-gene comparison
3. Run `scripts/build_case_study_expert.py` with a larger `--candidate-limit` than the final `--expert-limit`. Default `--candidate-limit` is 200 for expert mode; use 300-500 only when the API can support a broader case-study candidate pool.
4. Inspect `data/coverage.json` first. If any target has `curation_scope=curation_endpoint_unavailable`, treat the case study as partial and avoid strong negative claims.
5. Inspect `data/ad_expert_pruning.json` or `data/expert_evidence.json`:
   - `included_evidence` is the main case-study evidence.
   - `secondary_evidence` can support caveats or context.
   - `deprioritized_evidence` should normally stay out of the main argument.
   - `merged_evidence` contains duplicate-collapsed evidence used for selection.
   - `duplicate_groups` explains which repeated or overlapping evidence rows were merged.
6. Use the exact sentences and PubMed links when writing final claims.
7. Keep the two-layer report structure:
   - expert narrative case study
   - audit appendix with scored evidence and original sentence traces
8. Tell the user that task-local source payloads and `data/cache_manifest.json` preserve the raw data used for the case study.

## Expert Scoring Policy

The script provides transparent first-pass expert scores. The assistant should refine the narrative as an AD pathology expert using common sense and the original sentences.

Prioritize evidence that has:

- AD-specific pathology or phenotype content
- molecular mechanism, alteration, model, or pathway detail
- explicit connection to amyloid, tau, neuroinflammation, mitochondrial/oxidative stress, synaptic dysfunction, proteostasis/autophagy, vascular/metabolic pathology, or neuronal death
- long-tail status with plausible mechanistic value
- direct relevance to the user's scientific question
- PMID traceability and an informative original sentence
- high-confidence `event_expert_annotation_final` annotation fields when present
- low-frequency but mechanism-rich long-tail evidence that would be missed by frequency-only summaries

Deprioritize evidence that is:

- broad disease background only
- too generic to support a mechanism
- only a weak association without AD-pathological context
- missing full-pool curation when stronger conclusions would require selected evidence from the curated pool
- repeated or overlapping evidence after PMID/sentence/EventDedupKey merge

## AD Expert Pruning Rules

The reusable pruning layer runs before the main narrative is selected.

- Request a broad curated candidate pool first; default expert mode requests 200 rows and retries lower limits only for legacy API compatibility.
- Merge duplicate or overlapping evidence by target, PMID, normalized sentence, and EventDedupKey before selecting narrative evidence.
- Treat `Not applicable to any AD hypothesis` as not countable for hypothesis statistics. Do not discard that evidence solely for this label when the user asks for mechanism or biological insight rather than a named hypothesis.
- If the user asks for a named AD hypothesis, Not applicable rows may remain as context but should not be used as main support for that hypothesis.
- Use DeepSeek/LLM curation annotations as priors, not final truth; inspect self-contained sentences and biological fit before making strong claims.
- Label APP/PS1, 5xFAD, and similar model evidence as model-level evidence unless the sentence directly supports the queried gene mechanism.

## Guardrails

- Do not introduce TF-IDF recommendation, external database overlap, manual gold relevance grading, or AD-LitPathoNet network parsing inside this skill.
- Do not display or interpret `EvidenceScore`.
- Do not claim a mechanism is proven by sentence-level evidence alone.
- Do not count Not applicable rows in named-hypothesis support statistics.
- When curation scope is `curation_endpoint_unavailable`, explicitly report the boundary instead of filling the gap with capped event samples.
- If an old cached payload has `api_sentence_sample`, treat it as exploratory legacy evidence only.
- In two-gene reports, do not make strong comparative conclusions if the two sides have unequal curation scope or very different coverage ratios.
- If using outside knowledge, keep it as a small interpretive bridge and label it separately from AD-Alterome evidence.
- Exact raw API payloads are cached in the shared local cache for repeat requests and manual inspection.

## Resources

- Builder script: [scripts/build_case_study_expert.py](scripts/build_case_study_expert.py)
- Reusable pruning module: [../adalterome-api/scripts/ad_expert_pruning.py](../adalterome-api/scripts/ad_expert_pruning.py)
- Case-study contract: [references/case_study_expert_contract.md](references/case_study_expert_contract.md)
