---
name: adalterome-case-study-expert
description: Build AD pathologist-style AD-Alterome case-study reports. Use when the user asks for a paper-level case study, expert interpretation, biological insight, AD pathology framing, evidence prioritization, long-tail candidate interpretation, coverage/balance-aware synthesis, or a report that should argue a scientific question using AD-Alterome evidence rather than only listing traceable records.
---

# AD-Alterome Case Study Expert

Use this skill when the user wants AD-Alterome evidence interpreted as a scientific case study, not only a stable evidence report.

This skill is the expert layer above the report skills. It keeps AD-Alterome first, preserves traceability, and adds an AD pathologist-style biological cut over selected evidence.

## When To Use

Use this expert skill for:

- paper-level case studies
- AD pathology expert interpretation
- gene, term, hypothesis, or two-gene questions that need a scientific argument
- long-tail candidate triage
- molecular pathological mechanism screening
- coverage-aware and balance-aware comparison reports

Use the existing `adalterome-*-report` skills instead when the user asks for a pure evidence packet, fixed report, API trace, PMID table, or raw source-backed dossier for human experts to interpret later.

## Quick Start

Gene-centered case study:

```bash
python3 scripts/build_case_study_expert.py --gene MAPT --question "What does MAPT evidence reveal about tau-centered AD pathology?" --output-dir outputs/mapt_case_study --candidate-limit 80 --expert-limit 18
```

Two-gene case study:

```bash
python3 scripts/build_case_study_expert.py --gene-a APOE --gene-b APP --question "How do APOE and APP differ in AD pathological mechanisms?" --output-dir outputs/apoe_app_case_study --candidate-limit 80 --expert-limit 20
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
- `data/coverage.json`
- source payload JSON files for each target

## Workflow

1. Identify the user's scientific question before fetching evidence.
2. Choose the case-study frame:
   - `--gene` for one gene
   - `--term` for a phenotype, ontology term, or pathological process
   - `--hypothesis` for one AD hypothesis
   - `--gene-a` and `--gene-b` for a balanced two-gene comparison
3. Run `scripts/build_case_study_expert.py` with a larger `--candidate-limit` than the final `--expert-limit`.
4. Inspect `data/coverage.json` first. If the report fell back to `api_sentence_sample`, mark conclusions as exploratory and avoid strong negative claims.
5. Inspect `data/expert_evidence.json`:
   - `included_evidence` is the main case-study evidence.
   - `secondary_evidence` can support caveats or context.
   - `deprioritized_evidence` should normally stay out of the main argument.
6. Use the exact sentences and PubMed links when writing final claims.
7. Keep the two-layer report structure:
   - expert narrative case study
   - audit appendix with scored evidence and original sentence traces

## Expert Scoring Policy

The script provides transparent first-pass expert scores. The assistant should refine the narrative as an AD pathology expert using common sense and the original sentences.

Prioritize evidence that has:

- AD-specific pathology or phenotype content
- molecular mechanism, alteration, model, or pathway detail
- explicit connection to amyloid, tau, neuroinflammation, mitochondrial/oxidative stress, synaptic dysfunction, proteostasis/autophagy, vascular/metabolic pathology, or neuronal death
- long-tail status with plausible mechanistic value
- direct relevance to the user's scientific question
- PMID traceability and an informative original sentence

Deprioritize evidence that is:

- broad disease background only
- too generic to support a mechanism
- only a weak association without AD-pathological context
- sampled from a low-coverage fallback when stronger conclusions would require full-pool curation

## Guardrails

- Do not introduce TF-IDF recommendation, external database overlap, manual gold relevance grading, or AD-LitPathoNet network parsing inside this skill.
- Do not display or interpret `EvidenceScore`.
- Do not claim a mechanism is proven by sentence-level evidence alone.
- When curation scope is `api_sentence_sample`, explicitly report the coverage limitation.
- In two-gene reports, do not make strong comparative conclusions if the two sides have unequal curation scope or very different coverage ratios.
- If using outside knowledge, keep it as a small interpretive bridge and label it separately from AD-Alterome evidence.

## Resources

- Builder script: [scripts/build_case_study_expert.py](scripts/build_case_study_expert.py)
- Case-study contract: [references/case_study_expert_contract.md](references/case_study_expert_contract.md)
