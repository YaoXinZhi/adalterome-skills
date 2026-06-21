# 2026-06-20 Knowledge Synthesis Revision Update

## Summary

This update reframes AD-Alterome skills around **AI for Biomedical Knowledge
Synthesis**. The new publication-facing workflow no longer treats AI output as
an expert biological conclusion or paper-ready case narrative. Instead, the
skills organize AD-Alterome evidence into auditable knowledge packets that can
be evaluated by human experts.

## What Changed

### New skill

Added `adalterome-knowledge-synthesis`.

The skill builds:

- `knowledge_packet.md`
- `evidence_map.md`
- `expert_review_sheet.tsv`
- `evaluation_record.json`
- `provenance_manifest.json`
- `data/query.json`
- `data/coverage.json`
- `data/knowledge_synthesis.json`
- `data/ad_expert_pruning.json`
- `data/cache_manifest.json`
- target-specific raw overview, evidence, and curation JSON files

### New framing

Updated repository and skill docs to state:

- AI organizes evidence for expert evaluation.
- AI-organized groups are review candidates, not final biological conclusions.
- AD-Alterome sentence-level evidence supports traceability, not causal proof.
- `EvidenceScore` is not used or displayed as evidence strength.

### New analytical patterns

The knowledge synthesis builder supports:

- `single_gene`
- `multi_gene`
- `gene_set`
- `recommendation`
- `phenotype_process`
- `hypothesis`
- `hypothesis_network`

### Expert review sheet

The generated TSV includes one row per organized evidence item and blank human
scoring columns:

- traceability
- accuracy
- breadth
- depth
- organization usefulness
- long-tail usefulness
- hallucination or overclaim risk
- inspiration
- review efficiency
- overall usefulness
- cannot judge
- reviewer notes

### Evaluation record

`evaluation_record.json` stores:

- reviewer types
- scoring dimensions
- recommended baselines
- fairness controls
- non-claims
- candidate counts
- coverage summary

### Documentation

Updated:

- `README.md`
- `DESIGN.md`
- `skills/adalterome/SKILL.md`
- `skills/adalterome-api/SKILL.md`
- `skills/adalterome-case-study-expert/SKILL.md`

Added:

- `KNOWLEDGE_SYNTHESIS_REVISION_PLAN_2026-06-20.md`
- `skills/adalterome-knowledge-synthesis/SKILL.md`
- `skills/adalterome-knowledge-synthesis/references/knowledge_synthesis_contract.md`
- `skills/adalterome-knowledge-synthesis/scripts/build_knowledge_synthesis.py`
- `experimental-records/2026-06-20-knowledge-synthesis-evaluation/zh_evaluation_report.md`
- `experimental-records/2026-06-20-knowledge-synthesis-evaluation/zh_expert_case_comparison_report.md`

## Validation Cases

Smoke/evaluation outputs were generated under:

`experimental-records/2026-06-20-knowledge-synthesis-evaluation/`

Cases:

1. Single-gene entry: `PSEN1`
2. Multi-gene entry: `APOE vs APP`
3. Recommendation entry: `MAPT phenotype landscape`
4. Hypothesis/network entry: `TREM2-DAP12 neuroinflammatory axis`

All four cases generated:

- `knowledge_packet.md`
- `evidence_map.md`
- `expert_review_sheet.tsv`
- `evaluation_record.json`
- `provenance_manifest.json`
- `data/cache_manifest.json`

The hypothesis/network case was adjusted to enforce target representation
across `TREM2`, `TYROBP`, and `Neuroinflammation Hypothesis` instead of letting
the large hypothesis pool dominate the organized evidence.

A Chinese expert-case comparison report was also added to make the evaluation
framing explicit: AI packets are assessed against human expert case judgment,
not treated as a replacement for that judgment.

## Verification

Completed checks:

- Python `py_compile` for all skill scripts.
- Four knowledge-synthesis smoke/evaluation runs.
- Output file presence check for every required file.
- Expert review sheet column check.
- Non-claim language check in generated packets and evaluation records.
- Search confirmed the new knowledge-synthesis outputs no longer contain the
  old `case-study synthesis` wording.

## Remaining Boundaries

- Human expert scores are not filled automatically; the TSV is designed for
  expert review.
- The generated organization scores are triage signals, not gold labels.
- The current smoke cases use bounded `candidate_limit` values for validation;
  manuscript-scale experiments should rerun selected cases with larger limits
  such as 200-500 where API latency allows.
