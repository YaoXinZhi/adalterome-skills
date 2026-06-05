# AD-Alterome Skills

AD-Alterome Skills provides a set of Codex skills for querying AD-Alterome and turning Alzheimer disease literature evidence into structured, source-traceable reports.

These skills are designed for users who want to explore AD-related genes, phenotypes, ontology terms, hypotheses, and sentence-level evidence without manually assembling API calls or reformatting PubMed-linked evidence tables.

## Skill Index

| Skill | Status | Purpose | Trigger keywords |
| --- | --- | --- | --- |
| `adalterome` | Recommended | Unified entrypoint that routes natural-language AD-Alterome questions to API lookup, gene report, phenotype/process report, hypothesis report, comparison report, or expert case-study mode. | "AD-Alterome", "query AD-Alterome", "write AD-Alterome report", "compare AD mechanisms" |
| `adalterome-api` | Stable | Query AD-Alterome REST API for schema, hypotheses, gene events, term events, hypothesis support, full-pool curation packages, overviews, two-gene comparison, original evidence sentences, and PubMed links. | "query AD-Alterome", "gene events", "term events", "hypothesis support", "PubMed evidence", "PMID evidence" |
| `adalterome-report` | Stable | Convert AD-Alterome API results into fixed-format evidence reports with stable sections, source links, original sentences, and caveats. | "fixed report", "standard report", "evidence summary", "AD-Alterome report" |
| `adalterome-gene-report` | Advanced | Generate deep researcher-facing gene reports with API overview statistics, server-side full-pool curation, PubMed links, phenotype/process and hypothesis interpretation, mechanism synthesis, top and long-tail patterns, and research priorities. | "deep gene report", "MAPT report", "APOE evidence dossier", "mechanism synthesis" |
| `adalterome-term-report` | Advanced | Generate deep phenotype, ontology term, or pathological-process reports with API top genes, hypotheses, server-side full-pool curation, PubMed links, top and long-tail gene/gene-alteration/phenotype patterns, and mechanism-oriented interpretation. | "phenotype report", "process report", "mitochondrial dysfunction", "neuroinflammation" |
| `adalterome-hypothesis-report` | Advanced | Generate deep AD hypothesis support reports with top genes, top phenotype/process features, server-side full-pool curation, source-traceable evidence, and support pattern synthesis. | "hypothesis report", "Amyloid Hypothesis", "Tau Protein Hypothesis", "support evidence" |
| `adalterome-compare-report` | Advanced | Generate two-gene comparison reports with shared/distinct phenotype/process features, shared/distinct hypotheses, and full-pool curation traces for each gene. | "compare genes", "APOE vs APP", "gene comparison", "shared mechanisms" |
| `adalterome-case-study-expert` | Expert | Generate paper-level AD pathology case-study reports that interpret a user scientific question, check coverage and balance, score selected evidence for biological insight, protect long-tail candidates, and return both an expert narrative and an audit appendix. | "case study", "expert interpretation", "AD pathology insight", "paper-level report", "biological cut" |

## Report vs Expert Mode

Use the report skills when the user wants a pure, stable, source-traceable evidence packet for later human expert interpretation. Report mode optimizes provenance, reproducibility, fixed sections, original sentences, PubMed links, curation scope, long-tail visibility, and conservative caveats.

Use `adalterome-case-study-expert` when the user wants the skill to behave more like an AD pathologist: infer the scientific question, define an evidence strategy, check coverage and comparison balance, score selected evidence for biological insight, demote generic evidence, protect low-frequency but mechanistically plausible long-tail candidates, and write a case-study argument supported by AD-Alterome traces.

## Requirements

These skills use the public AD-Alterome REST API by default. They do not require a local AD-Alterome database.

Default public base URL:

```text
http://117.72.176.137/api/adalterome
```

You can override it per command:

```bash
python scripts/query_adalterome.py gene-events --gene MAPT --base-url http://117.72.176.137/api/adalterome
```

or by environment variable:

```bash
export ADALTEROME_API_BASE_URL=http://117.72.176.137/api/adalterome
```

The scripts use only Python standard library modules.

## Update Reports

- [2026-06-05 curated pool and final annotation update](UPDATE_REPORT_2026-06-05_CURATED_POOL_FINAL_ANNOTATION.md)
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
cp -R skills/adalterome-case-study-expert "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart Codex after installation so the skills can be discovered.

Most users can invoke `adalterome` and ask in natural language. The unified
skill routes the request to the correct specialized skill. Advanced users can
still call the lower-level skills directly.

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

## Expert Case-Study Report

Use `adalterome-case-study-expert` for a paper-level case study that should argue a scientific question using AD-Alterome evidence:

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
| Gene report | Query scope and data provenance; global evidence landscape; evidence curation layer; mechanism-stratified evidence map; representative evidence; long-tail evidence signals; chronological trajectory; original evidence traces; interpretation guide; follow-up priorities. | For `MAPT`, the evidence curation layer lists server-side full-pool rows, event-unique rows, top phenotypes, top gene-alteration pairs such as `MAPT / point mutations:mutations`, and long-tail phenotype/gene-alteration patterns. |
| Phenotype/process report | Query scope and data provenance; global evidence landscape; top genes and hypotheses; evidence curation layer; mechanism map; representative evidence; long-tail evidence signals; chronological trajectory; original evidence traces; interpretation guide; follow-up priorities. | For `mitochondrial dysfunction`, global evidence landscape shows API aggregate event, PMID, gene, and hypothesis counts; curation shows top genes, top gene-alteration pairs, and phenotype mappings from the server-side full-pool curation package. |
| Hypothesis report | Query scope and hypothesis frame; global evidence landscape; top genes and phenotypes; evidence curation layer; mechanism map; representative support evidence; long-tail evidence signals; chronology; original evidence traces; interpretation guide; follow-up priorities. | For `Amyloid Hypothesis`, top patterns show genes, gene-alteration pairs, and phenotypes associated with the hypothesis in the server-side curation package. |
| Compare report | Query scope and comparison frame; side-by-side overview; shared phenotype/process features and hypotheses; gene-specific patterns; curation layer for each gene; mechanism maps; representative and long-tail evidence for each gene; comparative interpretation guide; follow-up priorities. | For `APOE` vs `APP`, each gene has its own top phenotypes, top gene-alteration pairs, long-tail evidence signals, and original PubMed-linked evidence traces. |
| Expert case-study report | Interpreted scientific question; evidence strategy; coverage and balance check; AD pathologist-style synthesis; expert-included evidence; long-tail candidates; limitations; audit appendix with scored evidence and original sentence traces. | For `APOE` vs `APP`, the expert layer marks whether the comparison is balanced, scores evidence for biological insight, protects mechanistically plausible long-tail candidates, and avoids strong comparative claims when one side falls back to capped sampling. |

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
- In expert mode, prefer biologically insightful evidence rows, but keep the expert score transparent and separate from the original AD-Alterome record.

## Repository Design

See [DESIGN.md](DESIGN.md) for design notes and how the unified entrypoint plus specialized skills map to the CucurLitBase skill pattern.
