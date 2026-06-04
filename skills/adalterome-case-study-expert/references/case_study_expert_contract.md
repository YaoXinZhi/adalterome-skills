# AD-Alterome Expert Case-Study Contract

This contract defines the expert layer for AD-Alterome case-study reports.

## Scope

The expert case-study skill does not implement TF-IDF recommendation, external database overlap, manual gold relevance grading, or AD-LitPathoNet network parsing. It focuses on weaknesses exposed by traceable evidence reports:

- fallback from full-pool curation to capped sentence samples
- incomplete coverage reporting
- imbalanced two-gene comparisons
- under-interpreted long-tail candidates
- evidence lists that need AD pathology-oriented biological trimming

## Required Outputs

Each run must write:

- `case_study_report.md`: user-facing paper-style case-study draft.
- `data/query.json`: exact CLI parameters.
- `data/coverage.json`: per-target curation scope, coverage, warnings, and comparison balance status.
- `data/expert_evidence.json`: scored evidence with included, additional high-scoring, secondary, and deprioritized tiers.
- `data/case_study.json`: compact machine-readable summary for follow-up writing.

## Report Structure

The Markdown report should keep two layers:

1. Expert narrative layer
   - interpreted scientific question
   - evidence strategy
   - coverage and balance check
   - AD pathologist-style synthesis
   - main mechanistic claims
   - long-tail candidates worth expert attention
   - limitations

2. Audit layer
   - scored evidence table
   - additional high-scoring evidence not used in the main narrative
   - deprioritized evidence summary
   - original sentence traces with PMID/PubMed links

## Expert Evidence Scores

Scores are transparent first-pass expert triage, not human gold labels. They help choose evidence for the case-study narrative. The assistant should still inspect the original sentences before making final claims.

Score dimensions:

- AD specificity
- molecular/pathological mechanism depth
- long-tail insight
- direct fit to the user question
- source traceability
- sentence informativeness
- common-sense penalty for generic or weakly supported evidence

## Coverage Rules

`server_full_query_pool` supports stronger coverage claims. `api_sentence_sample` is acceptable for exploratory reports but must be labeled as a fallback. Do not infer absence of evidence from a capped sample.

For two-gene comparisons, mark the comparison as imbalanced when one side uses full-pool curation and the other uses capped sampling, or when coverage ratios differ strongly. In imbalanced mode, discuss visible evidence contrasts but avoid strong ranking claims.

## AD-Alterome First

The report should privilege AD-Alterome records. Outside knowledge may be used only as a concise interpretive bridge and must not replace AD-Alterome evidence traces.
