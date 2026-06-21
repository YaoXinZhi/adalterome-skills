# AD-Alterome Skills

AD-Alterome Skills provides a set of Codex skills for querying AD-Alterome and turning Alzheimer disease literature evidence into structured, source-traceable reports and expert-evaluable knowledge synthesis packets.

These skills are designed for users who want to explore AD-related genes, phenotypes, ontology terms, hypotheses, and sentence-level evidence without manually assembling API calls or reformatting PubMed-linked evidence tables. The publication-facing framing is **AI for Biomedical Knowledge Synthesis**: AI organizes complex alteration evidence for expert evaluation; it does not replace expert review or directly establish disease mechanisms.

## Recommended Invocation Model

Install all skill folders, but treat the user-facing surface as two public
entrypoints:

- `adalterome`: default entrypoint for ordinary AD-Alterome questions.
- `adalterome-knowledge-synthesis`: direct research/evaluation entrypoint for
  knowledge packets, evidence maps, expert review sheets, scoring tables, and
  AI-for-biomedical-knowledge-synthesis experiments.

All other `adalterome-*` skills remain available as internal/advanced
direct-use helpers for routing, debugging, reproducibility, and fixed builder
scripts. Ordinary users should not need to choose among gene, phenotype/process,
hypothesis, comparison, report, API, or legacy case-study skills.

## Skill Index

| Skill | Status | Purpose | Trigger keywords |
| --- | --- | --- | --- |
| `adalterome` | Public default | Unified entrypoint that routes natural-language AD-Alterome questions to API lookup, fixed report, deep report, knowledge synthesis, comparison, or legacy case-study helper workflows. | "AD-Alterome", "query AD-Alterome", "write AD-Alterome report", "organize AD evidence" |
| `adalterome-knowledge-synthesis` | Public research/evaluation | Generate researcher-facing knowledge packets, evidence maps, expert review sheets, evaluation records, and provenance manifests for AI-for-biomedical-knowledge-synthesis experiments. | "knowledge synthesis", "evidence organization", "expert review sheet", "scoring table", "long-tail evidence", "AI evaluation" |
| `adalterome-api` | Internal/advanced direct-use | Raw REST API, schema, cache, and payload helper used by the unified entrypoint and report builders. | "explicit adalterome-api", "raw API debug", "schema inspection", "reproduce API payload" |
| `adalterome-report` | Internal/advanced direct-use | Fixed-format evidence report formatter for reproducible report contracts. | "explicit adalterome-report", "fixed report contract", "reproduce fixed report" |
| `adalterome-gene-report` | Internal/advanced direct-use | One-gene deep report builder used after routing detects a gene query. | "explicit adalterome-gene-report", "gene report builder", "reproduce one-gene report" |
| `adalterome-term-report` | Internal/advanced direct-use | Phenotype/process deep report builder used after routing detects a phenotype, ontology, or pathological-process query. | "explicit adalterome-term-report", "term report builder", "reproduce phenotype/process report" |
| `adalterome-hypothesis-report` | Internal/advanced direct-use | AD hypothesis support report builder used after routing detects a hypothesis-centered query. | "explicit adalterome-hypothesis-report", "hypothesis report builder", "reproduce hypothesis report" |
| `adalterome-compare-report` | Internal/advanced direct-use | Two-gene comparison report builder used after routing detects a comparison query. | "explicit adalterome-compare-report", "compare report builder", "reproduce comparison report" |
| `adalterome-case-study-expert` | Legacy/internal direct-use | Older narrative case-study helper kept for compatibility. Prefer `adalterome-knowledge-synthesis` for publication-facing evaluation work. | "explicit adalterome-case-study-expert", "legacy case study", "older narrative case-study style" |

## Report vs Knowledge Synthesis

Use the report skills when the user wants a pure, stable, source-traceable evidence packet for later human expert interpretation. Report mode optimizes provenance, reproducibility, fixed sections, original sentences, PubMed links, curation scope, long-tail visibility, and conservative caveats.

Use `adalterome-knowledge-synthesis` when the user wants AI to organize AD-Alterome evidence into an expert-evaluable knowledge packet. This mode produces an evidence map, organized evidence groups, a review worksheet, an evaluation record, and a provenance manifest. Its output is a review object, not a final biological conclusion.

Use `adalterome-case-study-expert` only for compatibility with earlier narrative-style workflows. Publication-facing experiments should prefer knowledge synthesis plus human expert scoring.

## Requirements

These skills use the public AD-Alterome REST API by default. They do not require a local AD-Alterome database.

Default public base URL:

```text
http://117.72.176.137/api/adalterome
```

You can override it per command:

```bash
python skills/adalterome-api/scripts/query_adalterome.py gene-events --gene MAPT --base-url http://117.72.176.137/api/adalterome
```

or by environment variable:

```bash
export ADALTEROME_API_BASE_URL=http://117.72.176.137/api/adalterome
```

The scripts use only Python standard library modules.

## Update Reports

- [2026-06-21 entrypoint routing and skill hierarchy update](UPDATE_REPORT_2026-06-21_ENTRYPOINT_ROUTING.md)
- [2026-06-21 curation limit stability test](UPDATE_REPORT_2026-06-21_CURATION_LIMIT_STABILITY.md)
- [2026-06-20 knowledge synthesis revision update](UPDATE_REPORT_2026-06-20_KNOWLEDGE_SYNTHESIS.md)
- [2026-06-20 knowledge synthesis revision plan](KNOWLEDGE_SYNTHESIS_REVISION_PLAN_2026-06-20.md)
- [2026-06-15 field normalization and deployment update](UPDATE_REPORT_2026-06-15_FIELD_NORMALIZATION_AND_DEPLOYMENT.md)
- [2026-06-07 skill implementation audit and consistency fixes](UPDATE_REPORT_2026-06-07_SKILL_AUDIT.md)
- [2026-06-05 unified entrypoint and local raw-data cache update](UPDATE_REPORT_2026-06-05_UNIFIED_ENTRYPOINT_AND_CACHE.md)
- [2026-06-05 curated pool and final annotation update](UPDATE_REPORT_2026-06-05_CURATED_POOL_FINAL_ANNOTATION.md)
- [2026-06-05 curated global statistics update](UPDATE_REPORT_2026-06-05_CURATED_GLOBAL_STATISTICS.md)
- [2026-06-04 expert case-study skill update](UPDATE_REPORT_2026-06-04_EXPERT_CASE_STUDY.md)
- [2026-06-03 full-pool curation update](UPDATE_REPORT_2026-06-03_FULL_POOL_CURATION.md)

## Installation

Clone this repository:

```bash
git clone https://github.com/YaoXinZhi/adalterome-skills.git
cd adalterome-skills
```

Copy the skill folders into your local Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/adalterome-api "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/adalterome "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/adalterome-report "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/adalterome-gene-report "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/adalterome-term-report "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/adalterome-hypothesis-report "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/adalterome-compare-report "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/adalterome-knowledge-synthesis "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/adalterome-case-study-expert "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart Codex after installation so the skills can be discovered.

Most users should invoke only `adalterome` and ask in natural language. The
unified skill routes the request to the correct specialized helper. Users doing
publication-facing AI-for-biomedical-knowledge-synthesis experiments may invoke
`adalterome-knowledge-synthesis` directly. Advanced users can still call the
lower-level skills directly for reproducibility, debugging, or fixed script
contracts.

## Local Data Cache

The scripts save raw API payloads automatically so users can inspect returned
data and exact repeat requests do not need to hit the remote API again.

- Task-local report outputs keep query JSON under the requested output directory.
- Each deep report writes `data/cache_manifest.json`, which lists the raw API payload files used for that report.
- The shared local cache defaults to `~/.adalterome-skills/cache`.
- Set `ADALTEROME_CACHE_DIR` to choose another cache location.
- Set `ADALTEROME_REFRESH_CACHE=1` to force a fresh API request.
- Set `ADALTEROME_DISABLE_CACHE=1` to bypass caching.

For follow-up analysis, inspect the previous report directory's `data/*.json`
and `data/cache_manifest.json` first. If those files already cover the target,
the skill can continue from local data and avoid another remote request.

## Quick API Examples

### Inspect API Schema

```text
Use $adalterome-api to inspect the AD-Alterome API schema.
```

Equivalent script:

```bash
python skills/adalterome-api/scripts/query_adalterome.py schema --output json
```

### Retrieve Gene Evidence

```text
Use $adalterome-api to retrieve AD-Alterome evidence for MAPT with PubMed links.
```

Equivalent script:

```bash
python skills/adalterome-api/scripts/query_adalterome.py gene-events --gene MAPT --top-k 5 --output report
```

### Retrieve Phenotype / Process Evidence

```text
Use $adalterome-api to find genes and hypotheses associated with mitochondrial dysfunction.
```

Equivalent script:

```bash
python skills/adalterome-api/scripts/query_adalterome.py term-events --term "mitochondrial dysfunction" --top-k 5 --output report
```

### Retrieve Full-Pool Curation for a Deep Report

```text
Use $adalterome-api to curate mitochondrial dysfunction evidence from the full API query pool.
```

Equivalent script:

```bash
python skills/adalterome-api/scripts/query_adalterome.py term-curation --term "mitochondrial dysfunction" --selected-limit 30 --output report
```

### Retrieve Hypothesis Support

```text
Use $adalterome-report to summarize evidence supporting the Tau Protein Hypothesis.
```

Equivalent script:

```bash
python skills/adalterome-api/scripts/query_adalterome.py hypothesis-support --hypothesis "Tau Protein Hypothesis" --top-k 5 --output report
```

### Compare Two Genes

```text
Use $adalterome-report to compare APOE and APP in AD-Alterome.
```

Equivalent script:

```bash
python skills/adalterome-api/scripts/query_adalterome.py compare --gene-a APOE --gene-b APP --output report
```

## Deep Gene Report

Use `adalterome-gene-report` for a researcher-facing gene evidence dossier:

```text
Use $adalterome-gene-report to create a deep report for MAPT with evidence traces and mechanism synthesis.
```

Equivalent script:

```bash
python skills/adalterome-gene-report/scripts/build_gene_report.py --gene MAPT --output-dir outputs/mapt_deep --curation-limit 50 --selected-limit 12
```

Expected outputs:

- `outputs/mapt_deep/report.md`
- `outputs/mapt_deep/data/query.json`
- `outputs/mapt_deep/data/overview.json`
- `outputs/mapt_deep/data/evidence.json`
- `outputs/mapt_deep/data/curation.json`
- `outputs/mapt_deep/data/cache_manifest.json`

## Deep Phenotype / Process Report

Use `adalterome-term-report` for a phenotype, ontology term, or pathological process:

```text
Use $adalterome-term-report to create a deep AD-Alterome report for mitochondrial dysfunction.
```

Equivalent script:

```bash
python skills/adalterome-term-report/scripts/build_term_report.py --term "mitochondrial dysfunction" --output-dir outputs/mitochondrial_dysfunction --curation-limit 50 --selected-limit 12
```

Expected outputs:

- `outputs/mitochondrial_dysfunction/report.md`
- `outputs/mitochondrial_dysfunction/data/query.json`
- `outputs/mitochondrial_dysfunction/data/overview.json`
- `outputs/mitochondrial_dysfunction/data/evidence.json`
- `outputs/mitochondrial_dysfunction/data/curation.json`
- `outputs/mitochondrial_dysfunction/data/cache_manifest.json`

## Deep Hypothesis Report

Use `adalterome-hypothesis-report` for an AD hypothesis support dossier:

```text
Use $adalterome-hypothesis-report to summarize evidence for the Amyloid Hypothesis.
```

Equivalent script:

```bash
python skills/adalterome-hypothesis-report/scripts/build_hypothesis_report.py --hypothesis "Amyloid Hypothesis" --output-dir outputs/amyloid_hypothesis --curation-limit 50 --selected-limit 12
```

Expected outputs:

- `outputs/amyloid_hypothesis/report.md`
- `outputs/amyloid_hypothesis/data/query.json`
- `outputs/amyloid_hypothesis/data/overview.json`
- `outputs/amyloid_hypothesis/data/evidence.json`
- `outputs/amyloid_hypothesis/data/curation.json`
- `outputs/amyloid_hypothesis/data/cache_manifest.json`

## Two-Gene Compare Report

Use `adalterome-compare-report` for shared and distinct AD-Alterome patterns between two genes:

```text
Use $adalterome-compare-report to compare APOE and APP with evidence traces.
```

Equivalent script:

```bash
python skills/adalterome-compare-report/scripts/build_compare_report.py --gene-a APOE --gene-b APP --output-dir outputs/apoe_vs_app --curation-limit 50 --selected-limit 8
```

Expected outputs:

- `outputs/apoe_vs_app/report.md`
- `outputs/apoe_vs_app/data/query.json`
- `outputs/apoe_vs_app/data/compare.json`
- `outputs/apoe_vs_app/data/gene_a_evidence.json`
- `outputs/apoe_vs_app/data/gene_b_evidence.json`
- `outputs/apoe_vs_app/data/gene_a_curation.json`
- `outputs/apoe_vs_app/data/gene_b_curation.json`
- `outputs/apoe_vs_app/data/cache_manifest.json`

## Knowledge Synthesis Packet

Use `adalterome-knowledge-synthesis` when the goal is to organize AD-Alterome
evidence for expert evaluation rather than generate final manuscript claims:

```text
Use $adalterome-knowledge-synthesis to create a PSEN1 knowledge packet with an expert review sheet.
```

Equivalent script:

```bash
python skills/adalterome-knowledge-synthesis/scripts/build_knowledge_synthesis.py --gene PSEN1 --output-dir outputs/psen1_knowledge --organized-limit 18
```

Supported analytical patterns:

```bash
# Single-gene entry
python skills/adalterome-knowledge-synthesis/scripts/build_knowledge_synthesis.py --gene PSEN1 --pattern single_gene --output-dir outputs/psen1_knowledge

# Multi-gene entry
python skills/adalterome-knowledge-synthesis/scripts/build_knowledge_synthesis.py --gene-a APOE --gene-b APP --pattern multi_gene --output-dir outputs/apoe_app_knowledge

# Recommendation entry
python skills/adalterome-knowledge-synthesis/scripts/build_knowledge_synthesis.py --gene MAPT --pattern recommendation --question "Organize the MAPT phenotype landscape for expert review." --output-dir outputs/mapt_phenotype_landscape

# Hypothesis/network entry
python skills/adalterome-knowledge-synthesis/scripts/build_knowledge_synthesis.py --gene-set TREM2 TYROBP --hypothesis "Neuroinflammation Hypothesis" --axis "TREM2-DAP12 neuroinflammatory axis" --pattern hypothesis_network --output-dir outputs/trem2_dap12_axis
```

Expected outputs:

- `outputs/*/knowledge_packet.md`
- `outputs/*/evidence_map.md`
- `outputs/*/expert_review_sheet.tsv`
- `outputs/*/evaluation_record.json`
- `outputs/*/provenance_manifest.json`
- `outputs/*/data/query.json`
- `outputs/*/data/coverage.json`
- `outputs/*/data/knowledge_synthesis.json`
- `outputs/*/data/ad_expert_pruning.json`
- `outputs/*/data/cache_manifest.json`

Knowledge synthesis packets are designed as evaluation objects for
`AI for Biomedical Knowledge Synthesis`. They explicitly include non-claims:
the packet does not prove an AD mechanism, does not replace expert review, and
does not treat AI-organized groups as final biological conclusions.

By default, knowledge synthesis requests the current API maximum candidate pool
of 500 rows per target, then narrows it with `--organized-limit`. For quick
smoke tests, use at least `--candidate-limit 20`; lower values are raised to 20
automatically. Reduce `--candidate-limit` only when latency or payload size
matters more than coverage.

## Expert Case-Study Report

Use `adalterome-case-study-expert` only for compatibility with the older
narrative-style workflow. For publication-facing work and expert evaluation,
prefer `adalterome-knowledge-synthesis`.

```text
Use $adalterome-case-study-expert to compare APOE and APP as AD pathological mechanisms with coverage and balance checks.
```

Equivalent script:

```bash
python skills/adalterome-case-study-expert/scripts/build_case_study_expert.py --gene-a APOE --gene-b APP --question "How do APOE and APP differ in AD pathological mechanisms?" --output-dir outputs/apoe_app_case_study --candidate-limit 80 --expert-limit 20
```

Expected outputs:

- `outputs/apoe_app_case_study/case_study_report.md`
- `outputs/apoe_app_case_study/data/query.json`
- `outputs/apoe_app_case_study/data/coverage.json`
- `outputs/apoe_app_case_study/data/expert_evidence.json`
- `outputs/apoe_app_case_study/data/case_study.json`
- `outputs/apoe_app_case_study/data/cache_manifest.json`

## Report Modules

Deep report builders return Markdown reports with stable modules plus JSON data files for audit.

| Report | Modules returned | Example module content |
| --- | --- | --- |
| Gene report | Query scope and data provenance; global evidence landscape; evidence curation layer; mechanism-stratified evidence map; representative evidence; long-tail evidence signals; chronological trajectory; original evidence traces; interpretation guide; follow-up priorities. | For `MAPT`, the evidence curation layer lists server-side full-pool rows, event-unique rows, top phenotype/process features, top gene-alteration pairs such as `MAPT / point mutations:mutations`, and long-tail phenotype/process or gene-alteration patterns. |
| Phenotype/process report | Query scope and data provenance; global evidence landscape; top genes and hypotheses; evidence curation layer; mechanism map; representative evidence; long-tail evidence signals; chronological trajectory; original evidence traces; interpretation guide; follow-up priorities. | For `mitochondrial dysfunction`, global evidence landscape shows API aggregate event, PMID, gene, and hypothesis counts; curation shows top genes, top gene-alteration pairs, and phenotype/process mappings from the server-side full-pool curation package. |
| Hypothesis report | Query scope and hypothesis frame; global evidence landscape; top genes and phenotype/process features; evidence curation layer; mechanism map; representative support evidence; long-tail evidence signals; chronology; original evidence traces; interpretation guide; follow-up priorities. | For `Amyloid Hypothesis`, top patterns show genes, gene-alteration pairs, and phenotype/process features associated with the hypothesis in the server-side curation package. |
| Compare report | Query scope and comparison frame; side-by-side overview; shared phenotype/process features and hypotheses; gene-specific patterns; curation layer for each gene; mechanism maps; representative and long-tail evidence for each gene; comparative interpretation guide; follow-up priorities. | For `APOE` vs `APP`, each gene has its own top phenotype/process features, top gene-alteration pairs, long-tail evidence signals, and original PubMed-linked evidence traces. |
| Knowledge synthesis packet | Query scope and user intent; analytical pattern; event schema; evidence landscape and coverage; organized evidence groups; gene-alteration-phenotype/hypothesis map; long-tail candidates; AI-organized synthesis for expert review; expert review worksheet; original evidence traces; limitations and non-claims. | For `PSEN1`, the packet organizes evidence into a reviewable map and writes `expert_review_sheet.tsv` so human experts can score traceability, accuracy, breadth, depth, hallucination risk, and usefulness. |
| Legacy expert case-study report | Interpreted scientific question; evidence strategy; coverage and balance check; AD pathologist-style synthesis; expert-included evidence; long-tail candidates; limitations; audit appendix with scored evidence and original sentence traces. | For `APOE` vs `APP`, the legacy expert layer marks whether the comparison is balanced and writes a narrative-style interpretation; use knowledge synthesis instead when the AI output must be treated as an expert-scored review object. |

Note: API overview endpoints provide aggregate counts and top overview lists. Full-pool curation endpoints provide report-grade deduplication, query-relative distributions, long-tail signals, mechanism strata, and representative evidence. API event endpoints provide lightweight source-traceable sentence rows and currently cap `top_k` at 50.

## Evidence Payload

AD-Alterome event endpoints are expected to return original sentence evidence plus a normalized `Evidence` block:

- `Evidence.sentence`: exact original sentence.
- `Evidence.rich_sentence_html`: highlighted sentence HTML.
- `Evidence.pubmed_url`: direct PubMed link generated from PMID.
- `Evidence.article`: journal, year, MeSH, publication type, and substance metadata when available.
- `Evidence.biological_context`: gene, alteration, trigger, term, and ontology context.
- `Evidence.ad_interpretation`: AD hypothesis, mechanism, relevance, and explanation fields.
- `EvidenceQualityScore`: API-side sentence quality field in raw JSON; deep reports compute their own `SentenceQuality` and do not treat this as proof strength.

## Report Philosophy

These skills preserve source traceability first:

- Keep original evidence sentences intact.
- Keep PMID and PubMed links visible.
- Separate original sentence content from AD-Alterome interpretation fields.
- Treat `AlterationType` as the genetic alteration taxonomy. `TriggerWord` and `RegType` describe event relation/regulation context and are not counted as genetic alteration labels.
- Avoid turning sentence-level associations into causal claims without direct support.
- Prefer high-quality evidence rows, but still expose enough provenance for manual audit.
- In knowledge synthesis mode, AI organization scores are triage signals for expert review, not gold labels or final biological truth.
- Legacy expert mode remains available, but publication-facing workflows should prefer knowledge packets plus expert review sheets.

## Repository Design

See [DESIGN.md](DESIGN.md) for design notes and how the unified entrypoint plus specialized skills map to the CucurLitBase skill pattern.
