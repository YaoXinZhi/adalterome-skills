# AD-Alterome Skill Test Report

Date: 2026-06-01 23:37:37 CEST

## Summary

Result: PASS

The AD-Alterome skills were tested against the public jingdong API endpoint:

```text
http://117.72.176.137/api/adalterome
```

The test run covered static script validation, default URL configuration, the public API query commands, fixed report formatting, evidence markdown output, empty-result boundary behavior, deep report generation scripts, and the installed local Codex skill copy under `~/.codex/skills`.

Final count: 20 passed, 0 failed.

## Environment

- Source repository: `/Users/yao/Nutstore Files/Mac2PC/BioNLP_Django/adalterome-skills`
- Installed skill path tested: `/Users/yao/.codex/skills/adalterome-api`
- Public API base URL: `http://117.72.176.137/api/adalterome`
- Temporary test artifacts: `/tmp/adalterome-skill-test-20260601-233343`
- Test summary JSON: `/tmp/adalterome-skill-test-20260601-233343/summary.json`

## Scope

The run verified:

- All bundled Python scripts compile with `py_compile`.
- The skills no longer default to `127.0.0.1:8010`.
- The public API URL appears in README and skill/script defaults.
- API schema and content endpoints are reachable through the public nginx proxy.
- Fixed report output includes the required sections and API link fields.
- Evidence markdown output includes PubMed/PMID traceability.
- An absent gene query returns a clean empty-result response.
- Deep gene, term, hypothesis, and two-gene comparison report scripts generate Markdown plus JSON data artifacts.
- The installed local `adalterome-api` skill script can query MAPT evidence from the public endpoint.

## API Evidence

The schema endpoint returned:

- Table: `ADAlteromeModel`
- Rows: `451322`
- Columns: `32`

The hypothesis listing returned `253` hypothesis strings. Representative positive query targets used in this run were `APOE`, `MAPT`, `APP`, `neuroinflammation`, `Amyloid Hypothesis`, and `Tau Protein Hypothesis`.

## Test Matrix

| Test | Result | Evidence |
| --- | --- | --- |
| `static_py_compile` | PASS | compiled 5 scripts |
| `static_no_local_default` | PASS | no local default found |
| `static_public_default_present` | PASS | public URL mentions=12 |
| `api_schema_json` | PASS | table=ADAlteromeModel, rows=451322, columns=32 |
| `api_hypotheses_json` | PASS | status=ok, hypotheses=253 |
| `api_gene_events_apoe_json` | PASS | status=ok, count=2 |
| `api_gene_overview_apoe_json` | PASS | status=ok, count=1, top_terms=10 |
| `api_term_events_neuroinflammation_json` | PASS | status=ok, count=2 |
| `api_term_overview_neuroinflammation_json` | PASS | status=ok, count=1, top_hypotheses=10 |
| `api_hypothesis_support_amyloid_json` | PASS | status=ok, count=2 |
| `api_hypothesis_overview_amyloid_json` | PASS | status=ok, count=1, top_terms=10 |
| `api_compare_apoe_app_json` | PASS | status=ok, count=1, compare payload includes shared/distinct fields |
| `api_report_output_sections` | PASS | fixed report sections and API links present |
| `api_evidence_md_pubmed` | PASS | evidence markdown includes PMID/PubMed |
| `api_empty_gene_boundary_json` | PASS | status=ok, count=0 boundary handled |
| `deep_gene_report_apoe` | PASS | generated 4 files, report=3591 bytes |
| `deep_term_report_neuroinflammation` | PASS | generated 4 files, report=3874 bytes |
| `deep_hypothesis_report_amyloid` | PASS | generated 4 files, report=3328 bytes |
| `deep_compare_report_apoe_app` | PASS | generated 5 files, report=4280 bytes |
| `installed_skill_gene_events_mapt_summary` | PASS | installed summary ok, PMID=33246331 |

## Generated Artifacts

The deep report scripts generated temporary reports under:

```text
/tmp/adalterome-skill-test-20260601-233343/reports
```

Generated report sets:

- `reports/apoe/report.md`
- `reports/neuroinflammation/report.md`
- `reports/amyloid/report.md`
- `reports/apoe_vs_app/report.md`

Each report set also generated its expected JSON data files under its local `data/` directory.

## Observations

- The public API path works for normal `GET` requests through nginx.
- The `hypotheses` JSON payload stores the list under `data.hypotheses`.
- The `--output summary` mode for the tested installed script returns a compact JSON-style summary with `top_evidence`, including PMID.
- Query outputs preserve source traceability through PMID/PubMed information.
- No server database files were modified during this test.

## Not Tested

- Natural-language skill activation in a fresh restarted Codex session was not tested; this run tested the installed scripts directly.
- Browser rendering of generated Markdown reports was not tested.
- Authentication, write operations, and server deployment paths were not tested because the AD-Alterome skill API is read-only for these workflows.
