---
name: adalterome
description: Unified AD-Alterome entrypoint. Use when the user asks any AD-Alterome question and should not need to choose between API, gene, phenotype/process, hypothesis, comparison, or expert case-study skills. Route the request to the most appropriate AD-Alterome skill, preserve original evidence and PubMed links, and report where raw query data were saved.
---

# AD-Alterome Unified Skill

Use this as the default entrypoint for AD-Alterome work. The user should be able to invoke one skill and ask in natural language; decide the best downstream workflow from the question.

## Routing

Choose the smallest workflow that answers the user:

- Use `adalterome-api` for schema checks, short lookups, PubMed-linked evidence tables, lightweight summaries, and raw JSON inspection.
- Use `adalterome-report` for a fixed-format evidence packet from an already chosen API query.
- Use `adalterome-gene-report` when the target is one gene, such as `MAPT`, `APOE`, `APP`, `PSEN1`, or a gene-like symbol.
- Use `adalterome-term-report` when the target is a phenotype, downstream biological process, ontology term, pathological process, or phrase such as mitochondrial dysfunction, neuroinflammation, synaptic dysfunction, or amyloid processing. The CLI argument remains `--term` for API compatibility, but describe this to users as a phenotype/process query.
- Use `adalterome-hypothesis-report` when the target is one AD hypothesis, such as Amyloid Hypothesis, Tau Protein Hypothesis, Neuroinflammation Hypothesis, Oxidative Stress Hypothesis, Vascular Hypothesis, or Mitochondrial Cascade Hypothesis.
- Use `adalterome-compare-report` when the user asks to compare two genes and wants a structured evidence dossier.
- Use `adalterome-case-study-expert` when the user asks for expert interpretation, a paper-level case study, biological insight, long-tail candidate judgment, or an AD pathologist-style argument rather than only a traceable evidence packet.

If the request is ambiguous, start with `adalterome-api` to inspect the target and available hypotheses, then route to the report builder that matches the discovered target.

## Data Retention

Every workflow should tell the user where data were saved:

- Report builders save task-local files under the requested output directory, usually `data/query.json`, `data/overview.json`, `data/evidence.json`, `data/curation.json`, and `data/cache_manifest.json`.
- API payloads are also saved to the local shared cache at `${ADALTEROME_CACHE_DIR:-~/.adalterome-skills/cache}`.
- Exact repeat requests reuse the local shared cache automatically unless `ADALTEROME_REFRESH_CACHE=1` is set.
- Set `ADALTEROME_DISABLE_CACHE=1` to bypass caching.

For final answers, mention both the report path and the raw-data/cache path when a script was run.

For follow-up questions in the same investigation, inspect the previous report
directory's `data/*.json` and `data/cache_manifest.json` first. If those files
already cover the target, use them directly instead of making another API
request. Re-query only when the target, source, selected limit, or freshness
requirement changes.

## Evidence Rules

- Preserve original evidence sentences and PubMed links.
- Do not display or interpret `EvidenceScore`; it can remain inside raw API JSON for compatibility.
- Treat `AlterationType` as the genetic alteration taxonomy. `TriggerWord` and `RegType` are event relation context, not alteration labels.
- Split comma-delimited hypothesis fields before counting or summarizing hypotheses.
- Separate statistics and recommendations: report aggregate distributions, then explain which genes, phenotype/process features, alterations, or long-tail evidence look most biologically informative.
- Keep claims conservative: AD-Alterome provides sentence-level literature evidence, not direct causal proof.

## Examples

Natural-language requests and expected routing:

- "查 MAPT 的 AD-Alterome 证据并写报告" -> `adalterome-gene-report`
- "线粒体功能紊乱有哪些基因和突变证据？" -> `adalterome-term-report`
- "总结 Tau Protein Hypothesis 的支持证据" -> `adalterome-hypothesis-report`
- "比较 APP 和 APOE 的病理机制" -> `adalterome-compare-report`, or `adalterome-case-study-expert` if the user asks for expert interpretation
- "给我几个 PMID 证据句子" -> `adalterome-api`

## Resources

- API skill: ../adalterome-api/SKILL.md
- Gene report skill: ../adalterome-gene-report/SKILL.md
- Phenotype/process report skill: ../adalterome-term-report/SKILL.md
- Hypothesis report skill: ../adalterome-hypothesis-report/SKILL.md
- Compare report skill: ../adalterome-compare-report/SKILL.md
- Expert case-study skill: ../adalterome-case-study-expert/SKILL.md
