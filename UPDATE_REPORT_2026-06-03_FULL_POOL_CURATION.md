# AD-Alterome Skills Full-Pool Curation Update Report

Date: 2026-06-03

Repository: `YaoXinZhi/adalterome-skills`

Public API base: `http://117.72.176.137/api/adalterome`

## Executive Summary

This update changes AD-Alterome skills from top-k evidence summarization to report-grade full-pool curation.

The original problem was that API event rows were capped and sorted, so reports could over-represent a few high-frequency publications, broad phenotypes, or repetitive mutation records. The new workflow asks the public API for server-side curation packages computed over the complete matched query pool, then returns compact distributions, event-level deduplication summaries, long-tail signals, mechanism strata, chronological summaries, and diverse representative evidence.

## What Changed

### 1. Public API Curation Endpoints

The skills now prefer dedicated curation endpoints:

| Query type | Endpoint | Required parameter | Report role |
| --- | --- | --- | --- |
| Gene | `/gene/curation` | `gene` | Full-pool gene evidence curation |
| Term/phenotype | `/term/curation` | `term` | Full-pool term evidence curation |
| Hypothesis | `/hypothesis/curation` | `hypothesis` | Full-pool hypothesis support curation |

These endpoints are designed for reports. They do not return every raw row. Instead, they compute distributions and sampling decisions on the server side, then return a bounded curation package suitable for the skill runtime.

The legacy event endpoints remain useful for lightweight evidence inspection:

- `/gene/events`
- `/term/events`
- `/hypothesis/support`

Those event endpoints still cap `top_k` and should not be treated as the full report evidence universe.

### 2. Skill Runtime Logic

Current deep report flow:

```text
user query
  -> API overview endpoint for global aggregate statistics
  -> API curation endpoint for full-pool curation
  -> report builder renders Markdown and JSON audit files
```

If a curation endpoint is unavailable, the report builders fall back to capped event endpoints and clearly mark the source scope as fallback mode.

### 3. Evidence Deduplication

Deduplication is query-relative:

| Search type | Primary event key |
| --- | --- |
| Gene report | alteration taxonomy + phenotype/term + hypothesis |
| Term report | gene + alteration taxonomy + hypothesis |
| Hypothesis report | gene + alteration taxonomy + phenotype/term |

PMID and sentence text are fallback identity fields, but the report-level curation is not just sentence deduplication. The goal is to avoid counting the same biological event pattern repeatedly when a user asks from different entry points.

### 4. Alteration Taxonomy

Dominant alteration signatures now use only the leading genetic alteration taxonomy from `AlterationType`.

Human-readable examples:

- `point mutations:mutations`
- `normalized variants:dna change`
- `improper regulation linked to disease:inherited variation`

`TriggerWord` and `RegType` are treated as event relation or regulation context, not genetic alteration labels. They are not included in dominant alteration signatures.

### 5. EvidenceScore Handling

`EvidenceScore` may remain in raw API JSON for compatibility, but skills intentionally ignore it.

Skill-facing reports do not display it, rank by it, or describe it as evidence strength. The curation layer instead exposes interpretable fields such as evidence type, mechanism strata, sentence informativeness, curation reasons, PMID, year, term, gene, and alteration taxonomy.

### 6. Long-Tail and Top Pattern Reporting

Top and long-tail patterns are computed from the full curation pool, not from displayed representative rows.

The curation package includes query-relative distributions for:

- genes
- gene-alteration pairs
- phenotypes/terms
- hypotheses, when relevant to the query type

Long-tail signals are frequency-based: patterns below a low-frequency threshold or percentile can be surfaced even when they would not appear in top-ranked event rows.

### 7. Mechanism Strata

Mechanism strata are not final biological labels. They are an intermediate organization layer for expert-style summaries and LLM-assisted interpretation.

Stable strata include categories such as:

- genetic alteration
- molecular pathology
- pathway or cellular process
- model or experimental system
- clinical or biomarker association
- broad background

The final report can use these strata to avoid letting broad background evidence crowd out more specific molecular or model-based records.

## Report Modules

Deep reports now expose these stable modules:

| Module | Purpose | Example |
| --- | --- | --- |
| Query scope and data provenance | Shows query, API base, curation source, and whether full-pool curation was used. | `scope=server_full_query_pool` |
| Global evidence landscape | Uses overview counts for total events, PMIDs, genes, terms, and hypotheses. | `matched_events=925` |
| Evidence curation layer | Shows deduped event rows, selected evidence count, top/long-tail distributions, and curation scope. | `event_unique_rows=440` |
| Dominant signatures | Lists human-readable top gene, phenotype, and gene-alteration patterns. | `MAPT / point mutations:mutations` |
| Mechanism map | Groups evidence into mechanism strata for expert interpretation. | `molecular pathology`, `model evidence` |
| Representative evidence | Displays selected source-traceable evidence with PMID/PubMed, year, sentence, and curation reasons. | selected evidence rows |
| Long-tail evidence signals | Highlights low-frequency but potentially useful patterns from the full query pool. | rare gene-alteration/term pairs |
| Chronological trajectory | Summarizes how evidence types and mechanisms develop by year. | early genetic association to later pathway studies |
| Original evidence traces | Keeps exact sentences and PubMed links available for audit. | `PMID`, `pubmed_url`, `sentence` |

Experimental reports should not include a separate `Bias, Coverage, and Limitations` section. Publication skew can still be discussed briefly inside interpretation when grounded in the actual returned distribution.

## Files Updated

Major changed areas:

- `README.md`
- `skills/adalterome-api/SKILL.md`
- `skills/adalterome-api/references/api_docs.md`
- `skills/adalterome-api/scripts/query_adalterome.py`
- `skills/adalterome-api/scripts/evidence_fetch.py`
- `skills/adalterome-api/scripts/evidence_curation.py`
- `skills/adalterome-gene-report/*`
- `skills/adalterome-term-report/*`
- `skills/adalterome-hypothesis-report/*`
- `skills/adalterome-compare-report/*`

## User Installation

Fresh installation:

```bash
git clone https://github.com/YaoXinZhi/adalterome-skills.git
cd adalterome-skills
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/adalterome-* "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Update an existing local skill copy:

```bash
cd adalterome-skills
git pull
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
rsync -a --delete skills/adalterome-api/ "${CODEX_HOME:-$HOME/.codex}/skills/adalterome-api/"
rsync -a --delete skills/adalterome-report/ "${CODEX_HOME:-$HOME/.codex}/skills/adalterome-report/"
rsync -a --delete skills/adalterome-gene-report/ "${CODEX_HOME:-$HOME/.codex}/skills/adalterome-gene-report/"
rsync -a --delete skills/adalterome-term-report/ "${CODEX_HOME:-$HOME/.codex}/skills/adalterome-term-report/"
rsync -a --delete skills/adalterome-hypothesis-report/ "${CODEX_HOME:-$HOME/.codex}/skills/adalterome-hypothesis-report/"
rsync -a --delete skills/adalterome-compare-report/ "${CODEX_HOME:-$HOME/.codex}/skills/adalterome-compare-report/"
```

## Manual Test Questions

After installing the skills, users can test with natural-language prompts:

1. `Use adalterome-term-report to write a mitochondrial dysfunction report with full-pool curation.`
2. `Use adalterome-gene-report to generate a MAPT gene report.`
3. `Use adalterome-hypothesis-report to summarize Tau Protein Hypothesis support evidence.`
4. `Use adalterome-compare-report to compare APOE and APP with long-tail evidence signals.`
5. `Use adalterome-api to query mitochondrial dysfunction curation and show representative evidence.`

Equivalent direct script tests:

```bash
python skills/adalterome-api/scripts/query_adalterome.py term-curation --term "mitochondrial dysfunction" --selected-limit 5 --output summary
python skills/adalterome-api/scripts/query_adalterome.py gene-curation --gene MAPT --selected-limit 5 --output summary
python skills/adalterome-api/scripts/query_adalterome.py hypothesis-curation --hypothesis "Tau Protein Hypothesis" --selected-limit 5 --output summary
python skills/adalterome-term-report/scripts/build_term_report.py --term "mitochondrial dysfunction" --selected-limit 5 --output-dir outputs/mitochondrial_dysfunction
```

## Verification

Public API verification on 2026-06-03:

| Test | Result |
| --- | --- |
| Public API index | Version `0.3.0`; curation endpoints listed |
| `/term/curation?term=mitochondrial+dysfunction&selected_limit=5` | `matched_events=925`, `curation_pool_rows=925`, `event_unique_rows=440`, `selected_evidence=5`, `source_scope=server_full_query_pool` |
| `/gene/curation?gene=MAPT&selected_limit=3` | `matched_events=27822`, `curation_pool_rows=27822`, `event_unique_rows=8010`, dominant gene-alteration includes `MAPT / point mutations:mutations` |
| `/hypothesis/curation?hypothesis=Tau+Protein+Hypothesis&selected_limit=3` | `matched_events=38103`, `curation_pool_rows=38103`, `event_unique_rows=17537`, top gene includes `MAPT` |
| `query_adalterome.py term-curation` | PASS |
| `build_term_report.py --term "mitochondrial dysfunction"` | PASS; generated Markdown and `data/curation.json` |
| Python compile checks for skill scripts | PASS |

## Current Boundaries

- The curation endpoints return compact curation packages, not all raw rows.
- `selected_limit` controls displayed representative evidence, not the statistics pool.
- If the server curation endpoint is unavailable, fallback mode uses capped event rows and should be interpreted as limited.
- AD-Alterome evidence is sentence-level literature evidence; it is not automatic causal proof.
- Long-tail frequency is a discovery aid. It identifies underrepresented patterns for expert inspection, not guaranteed biological importance.
