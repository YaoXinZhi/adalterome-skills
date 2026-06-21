# AD-Alterome Skills Design Notes

This repository follows the layered style of `r1seee/cucurlitbase-skills`.

## Deployment and Trigger Strategy

All skill folders remain installable so the unified entrypoint can route to
stable helper workflows and advanced users can reproduce exact builder outputs.
The user-facing trigger surface should not be flat:

- `adalterome` is the public default entrypoint for ordinary questions.
- `adalterome-knowledge-synthesis` is the public research/evaluation entrypoint
  for knowledge packets, expert review sheets, scoring tables, and
  AI-for-biomedical-knowledge-synthesis experiments.
- `adalterome-api`, `adalterome-report`, `adalterome-gene-report`,
  `adalterome-term-report`, `adalterome-hypothesis-report`,
  `adalterome-compare-report`, and `adalterome-case-study-expert` are
  internal/advanced direct-use helpers. Their descriptions should discourage
  automatic selection for ordinary user questions unless the user explicitly
  names the helper, asks for a direct builder script, or needs reproducibility.

## Skill Layers

1. `adalterome`
   - Unified entrypoint skill.
   - Routes natural-language requests to API lookup, fixed report, gene report, phenotype/process report, hypothesis report, comparison report, knowledge synthesis, or legacy expert case-study mode.
   - Ensures final answers mention report outputs and raw-data cache locations when scripts are run.

2. `adalterome-api`
   - Internal/advanced direct-use helper, normally reached through `adalterome`.
   - Lowest-level retrieval skill.
   - Calls the live AD-Alterome REST API.
   - Exposes reproducible commands for schema, event samples, single-axis curation, compound curation, and two-gene comparison.
   - Preserves exact sentence evidence, PubMed links, Event chains, and normalized Evidence blocks.
   - Caches raw API JSON payloads locally by exact request URL for repeat use and manual inspection.

3. `adalterome-report`
   - Internal/advanced direct-use helper, normally reached through `adalterome`.
   - Presentation skill.
   - Converts API outputs into a fixed report contract.
   - Keeps provenance and evidence sections stable across runs.

4. `adalterome-gene-report`
   - Internal/advanced direct-use helper, normally reached through `adalterome`.
   - Research-style report skill.
   - Builds a deep Markdown draft for one gene.
   - Supports mechanism synthesis, evidence caveats, and follow-up gap analysis.

5. `adalterome-term-report`
   - Internal/advanced direct-use helper, normally reached through `adalterome`.
   - Research-style report skill for phenotypes, ontology terms, and pathological processes.
   - Uses `/term/overview` and `/term/curation`, with `/term/events` as capped fallback.
   - Emphasizes top genes, top hypotheses, evidence traces, and broad-term caveats.

6. `adalterome-hypothesis-report`
   - Internal/advanced direct-use helper, normally reached through `adalterome`.
   - Research-style report skill for AD hypothesis support.
   - Uses `/hypothesis/overview` and `/hypothesis/curation`, with `/hypothesis/support` as capped fallback.
   - Separates curated hypothesis labels from original sentence evidence.

7. `adalterome-compare-report`
   - Internal/advanced direct-use helper, normally reached through `adalterome`.
   - Research-style report skill for two-gene comparison.
   - Uses `/compare/genes` plus per-gene overview and curation packages for both genes.
   - Keeps common patterns and gene-specific evidence separate.

8. `adalterome-knowledge-synthesis`
   - Publication-facing knowledge organization layer above report skills.
   - Uses AD-Alterome full-pool curation first, then applies coverage checks, comparison-balance checks, transparent AI organization scoring, long-tail protection, duplicate merging, and evidence grouping.
   - For compound gene / phenotype-process / hypothesis questions, calls `/compound/curation` so the server intersects curated pools by `raw_event_id` before sampling.
   - Produces an expert-evaluable output package: `knowledge_packet.md`, `evidence_map.md`, `expert_review_sheet.tsv`, `evaluation_record.json`, `provenance_manifest.json`, and raw data manifests.
   - Frames AI output as an evaluation object for `AI for Biomedical Knowledge Synthesis`, not as final biological claims or paper-ready mechanism conclusions.

9. `adalterome-case-study-expert`
   - Legacy/internal direct-use helper, normally not selected unless explicitly requested.
   - Legacy compatibility layer for older narrative-style case-study outputs.
   - Uses AD-Alterome full-pool curation first, then applies coverage checks, comparison-balance checks, transparent expert evidence scoring, long-tail protection, and AD pathology-oriented biological trimming.
   - Produces a two-layer output: a case-study narrative plus an audit appendix with scored evidence and exact sentence traces.
   - Does not implement TF-IDF recommendation, external database overlap, manual gold relevance grading, or AD-LitPathoNet network parsing.

## Writing Style

- Keep `SKILL.md` short and procedural.
- Put endpoint details, report contracts, and caveats in `references/`.
- Use deterministic scripts for repeated API retrieval and report scaffolding.
- Preserve original evidence sentences exactly.
- Treat AD-Alterome interpretation fields as curated interpretation, not causal proof.
- Use PubMed links from PMID for traceability.

## Evidence Quality Strategy

Report skills compute their own `SentenceQuality` and curation reasons from the original sentence, biological context, AD interpretation fields, traceability, and query-relative diversity. They do not use or display raw `EvidenceScore`.

Knowledge synthesis mode adds a separate transparent AI organization score for review usefulness. This score is not a human gold label. It prioritizes AD specificity, molecular or pathological mechanism depth, long-tail insight, fit to the user's scientific question, PMID traceability, and common-sense filtering of generic evidence. The generated `expert_review_sheet.tsv` is where human experts evaluate traceability, accuracy, breadth, depth, hallucination or overclaim risk, inspiration, efficiency, and overall usefulness.

Legacy case-study mode keeps the earlier narrative workflow for compatibility, but publication-facing experiments should prefer knowledge synthesis packets plus expert review sheets.

Large genes and broad hypotheses can expose curation risk. When full-pool curation is unavailable and a report falls back to `api_sentence_sample`, the expert layer must label conclusions as exploratory and avoid absence-of-evidence claims. In two-gene comparisons, unequal curation scope or strongly different coverage ratios must downgrade strong contrastive conclusions.

## Retrieval and Curation Flow

The repository is designed for remote use through the public API. Installed
skills do not require a local AD-Alterome SQLite database.

```text
User question
  -> public entrypoint selection
  -> deterministic builder script
  -> public REST API request
  -> server-side curated pool / event hydration
  -> local JSON cache and task data files
  -> report, knowledge packet, or expert review sheet
```

Single-axis report-grade retrieval uses `/gene/curation`, `/term/curation`, or
`/hypothesis/curation`. Compound retrieval uses `/compound/curation` when at
least two of gene, phenotype/process, and hypothesis are present. The compound
endpoint must be treated as the primary retrieval path for those questions:
strict event intersection happens on the server before diversity sampling,
long-tail protection, representative selection, and knowledge organization.
The `axis_merge` fallback is exploratory context only and must remain visibly
marked when used.

## Repository Layout

```text
adalterome-skills/
├── README.md
├── DESIGN.md
└── skills/
    ├── adalterome-api/
    ├── adalterome/
    ├── adalterome-report/
    ├── adalterome-gene-report/
    ├── adalterome-term-report/
    ├── adalterome-hypothesis-report/
    ├── adalterome-compare-report/
    ├── adalterome-knowledge-synthesis/
    └── adalterome-case-study-expert/
```

## Versioning Strategy

The unified `adalterome` entrypoint is the recommended user-facing route. The specialized report skills remain stable direct-entry versions optimized for reproducible evidence packages that human experts can interpret later.

The publication-facing synthesis version lives in `adalterome-knowledge-synthesis`. It should be selected when the user asks for evidence organization, AI-for-biomedical-knowledge-synthesis, expert review sheets, scoring tables, long-tail candidate review, or evaluation materials. This keeps stable report behavior and expert-evaluable synthesis behavior side by side.

The legacy expert narrative version lives in `adalterome-case-study-expert`. It remains available for older case-study workflows, but the default manuscript-oriented path should be `adalterome-knowledge-synthesis` because it treats AI output as an expert-scored object instead of a final mechanism narrative.
