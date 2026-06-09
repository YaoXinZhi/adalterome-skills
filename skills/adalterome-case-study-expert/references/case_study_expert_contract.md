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
- `data/ad_expert_pruning.json`: full reusable AD expert pruning payload, including policy, duplicate groups, and hypothesis-count handling.
- `data/merged_evidence.json`: duplicate-collapsed candidate evidence used for narrative selection.
- `data/excluded_or_deprioritized_evidence.json`: evidence kept out of the main narrative after expert pruning.
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
   - duplicate-merge summary
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
- `event_expert_annotation_final` score, source, confidence, and reason when available
- common-sense penalty for generic or weakly supported evidence

## AD Expert Pruning Rules

The case-study skill uses a reusable second-layer pruning module after API curation:

- Default case-study candidate pool target is 200 curated rows; use 300-500 only when the API can support it.
- The final narrative normally uses 15-30 expert-included rows after duplicate merging and biological trimming.
- Merge repeated or overlapping evidence by target, PMID, normalized sentence, and EventDedupKey before narrative selection.
- `Not applicable to any AD hypothesis` is not counted in hypothesis statistics. It can remain mechanism evidence when the user asks for biological insight rather than a named hypothesis.
- If the user asks for a named hypothesis, Not applicable rows may appear as context but should not be treated as support for that hypothesis.
- Low-frequency, mechanism-rich long-tail evidence can be rescued when it is biologically specific and traceable.

## Coverage Rules

`offline_full_query_pool_prescreened` or `server_full_query_pool` supports stronger coverage claims. `curation_endpoint_unavailable` means the report is partial and selected evidence should stay empty rather than being filled with capped event samples. If an old cached payload has `api_sentence_sample`, label it as exploratory legacy evidence and do not infer absence of evidence from the capped sample.

For two-gene comparisons, mark the comparison as imbalanced when one side has full-pool curation and the other has unavailable curation or legacy capped sampling, or when coverage ratios differ strongly. In imbalanced mode, discuss visible evidence contrasts but avoid strong ranking claims.

## AD-Alterome First

The report should privilege AD-Alterome records. Outside knowledge may be used only as a concise interpretive bridge and must not replace AD-Alterome evidence traces.
