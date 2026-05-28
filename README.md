# AD-Alterome Skills

AD-Alterome Skills provides a set of Codex skills for querying AD-Alterome and turning Alzheimer disease literature evidence into structured, source-traceable reports.

These skills are designed for users who want to explore AD-related genes, phenotypes, ontology terms, hypotheses, and sentence-level evidence without manually assembling API calls or reformatting PubMed-linked evidence tables.

## Skill Index

| Skill | Status | Purpose | Trigger keywords |
| --- | --- | --- | --- |
| `adalterome-api` | Stable | Query AD-Alterome REST API for schema, hypotheses, gene events, term events, hypothesis support, overviews, two-gene comparison, original evidence sentences, and PubMed links. | "query AD-Alterome", "gene events", "term events", "hypothesis support", "PubMed evidence", "PMID evidence" |
| `adalterome-report` | Stable | Convert AD-Alterome API results into fixed-format evidence reports with stable sections, source links, original sentences, and caveats. | "fixed report", "standard report", "evidence summary", "AD-Alterome report" |
| `adalterome-gene-report` | Advanced | Generate deep researcher-facing gene reports with overview statistics, high-quality evidence rows, PubMed links, term/hypothesis interpretation, mechanism synthesis, and research gaps. | "deep gene report", "MAPT report", "APOE evidence dossier", "mechanism synthesis" |
| `adalterome-term-report` | Advanced | Generate deep phenotype, ontology term, or pathological-process reports with top genes, hypotheses, original sentences, PubMed links, and broad-term caveats. | "phenotype report", "term report", "mitochondrial dysfunction", "neuroinflammation" |
| `adalterome-hypothesis-report` | Advanced | Generate deep AD hypothesis support reports with top genes, top terms, source-traceable evidence, and support pattern synthesis. | "hypothesis report", "Amyloid Hypothesis", "Tau Protein Hypothesis", "support evidence" |
| `adalterome-compare-report` | Advanced | Generate two-gene comparison reports with shared/distinct terms, shared/distinct hypotheses, and evidence traces for each gene. | "compare genes", "APOE vs APP", "gene comparison", "shared mechanisms" |

## Requirements

These skills assume an AD-Alterome REST API service is available.

Default local base URL:

```text
http://127.0.0.1:8010
```

You can override it per command:

```bash
python scripts/query_adalterome.py gene-events --gene MAPT --base-url http://127.0.0.1:8010
```

or by environment variable:

```bash
export ADALTEROME_API_BASE_URL=http://127.0.0.1:8010
```

The scripts use only Python standard library modules.

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
cp -R skills/adalterome-report "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/adalterome-gene-report "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/adalterome-term-report "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/adalterome-hypothesis-report "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/adalterome-compare-report "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart Codex after installation so the skills can be discovered.

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

### Retrieve Phenotype / Term Evidence

```text
Use $adalterome-api to find genes and hypotheses associated with mitochondrial dysfunction.
```

Equivalent script:

```bash
python skills/adalterome-api/scripts/query_adalterome.py term-events --term "mitochondrial dysfunction" --top-k 5 --output report
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
python skills/adalterome-gene-report/scripts/build_gene_report.py --gene MAPT --output-dir outputs/mapt_deep --top-k 12
```

Expected outputs:

- `outputs/mapt_deep/report.md`
- `outputs/mapt_deep/data/query.json`
- `outputs/mapt_deep/data/overview.json`
- `outputs/mapt_deep/data/evidence.json`

## Deep Term / Phenotype Report

Use `adalterome-term-report` for a phenotype, ontology term, or pathological process:

```text
Use $adalterome-term-report to create a deep AD-Alterome report for mitochondrial dysfunction.
```

Equivalent script:

```bash
python skills/adalterome-term-report/scripts/build_term_report.py --term "mitochondrial dysfunction" --output-dir outputs/mitochondrial_dysfunction --top-k 12
```

Expected outputs:

- `outputs/mitochondrial_dysfunction/report.md`
- `outputs/mitochondrial_dysfunction/data/query.json`
- `outputs/mitochondrial_dysfunction/data/overview.json`
- `outputs/mitochondrial_dysfunction/data/evidence.json`

## Deep Hypothesis Report

Use `adalterome-hypothesis-report` for an AD hypothesis support dossier:

```text
Use $adalterome-hypothesis-report to summarize evidence for the Amyloid Hypothesis.
```

Equivalent script:

```bash
python skills/adalterome-hypothesis-report/scripts/build_hypothesis_report.py --hypothesis "Amyloid Hypothesis" --output-dir outputs/amyloid_hypothesis --top-k 12
```

Expected outputs:

- `outputs/amyloid_hypothesis/report.md`
- `outputs/amyloid_hypothesis/data/query.json`
- `outputs/amyloid_hypothesis/data/overview.json`
- `outputs/amyloid_hypothesis/data/evidence.json`

## Two-Gene Compare Report

Use `adalterome-compare-report` for shared and distinct AD-Alterome patterns between two genes:

```text
Use $adalterome-compare-report to compare APOE and APP with evidence traces.
```

Equivalent script:

```bash
python skills/adalterome-compare-report/scripts/build_compare_report.py --gene-a APOE --gene-b APP --output-dir outputs/apoe_vs_app --top-k 8
```

Expected outputs:

- `outputs/apoe_vs_app/report.md`
- `outputs/apoe_vs_app/data/query.json`
- `outputs/apoe_vs_app/data/compare.json`
- `outputs/apoe_vs_app/data/gene_a_evidence.json`
- `outputs/apoe_vs_app/data/gene_b_evidence.json`

## Evidence Payload

AD-Alterome event endpoints are expected to return original sentence evidence plus a normalized `Evidence` block:

- `Evidence.sentence`: exact original sentence.
- `Evidence.rich_sentence_html`: highlighted sentence HTML.
- `Evidence.pubmed_url`: direct PubMed link generated from PMID.
- `Evidence.article`: journal, year, MeSH, publication type, and substance metadata when available.
- `Evidence.biological_context`: gene, alteration, trigger, term, and ontology context.
- `Evidence.ad_interpretation`: AD hypothesis, mechanism, relevance, and explanation fields.
- `EvidenceQualityScore`: deterministic score used by the API to prioritize more informative sentences.

## Report Philosophy

These skills preserve source traceability first:

- Keep original evidence sentences intact.
- Keep PMID and PubMed links visible.
- Separate original sentence content from AD-Alterome interpretation fields.
- Avoid turning sentence-level associations into causal claims without direct support.
- Prefer high-quality evidence rows, but still expose enough provenance for manual audit.

## Repository Design

See [DESIGN.md](DESIGN.md) for design notes and how the three-skill structure maps to the CucurLitBase skill pattern.
