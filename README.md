# AD-Alterome Skills

AD-Alterome Skills provides a set of Codex skills for querying AD-Alterome and turning Alzheimer disease literature evidence into structured, source-traceable reports.

These skills are designed for users who want to explore AD-related genes, phenotypes, ontology terms, hypotheses, and sentence-level evidence without manually assembling API calls or reformatting PubMed-linked evidence tables.

## Skill Index

| Skill | Status | Purpose | Trigger keywords |
| --- | --- | --- | --- |
| `adalterome-api` | Stable | Query AD-Alterome REST API for schema, hypotheses, gene events, term events, hypothesis support, overviews, two-gene comparison, original evidence sentences, and PubMed links. | "query AD-Alterome", "gene events", "term events", "hypothesis support", "PubMed evidence", "PMID evidence" |
| `adalterome-report` | Stable | Convert AD-Alterome API results into fixed-format evidence reports with stable sections, source links, original sentences, and caveats. | "fixed report", "standard report", "evidence summary", "AD-Alterome report" |
| `adalterome-gene-report` | Advanced | Generate deep researcher-facing gene reports with overview statistics, high-quality evidence rows, PubMed links, term/hypothesis interpretation, mechanism synthesis, and research gaps. | "deep gene report", "MAPT report", "APOE evidence dossier", "mechanism synthesis" |

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
