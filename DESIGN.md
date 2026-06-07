# AD-Alterome Skills Design Notes

This repository follows the layered style of `r1seee/cucurlitbase-skills`.

## Skill Layers

1. `adalterome`
   - Unified entrypoint skill.
   - Routes natural-language requests to API lookup, fixed report, gene report, phenotype/process report, hypothesis report, comparison report, or expert case-study mode.
   - Ensures final answers mention report outputs and raw-data cache locations when scripts are run.

2. `adalterome-api`
   - Lowest-level retrieval skill.
   - Calls the live AD-Alterome REST API.
   - Preserves exact sentence evidence, PubMed links, Event chains, and normalized Evidence blocks.
   - Caches raw API JSON payloads locally by exact request URL for repeat use and manual inspection.

3. `adalterome-report`
   - Presentation skill.
   - Converts API outputs into a fixed report contract.
   - Keeps provenance and evidence sections stable across runs.

4. `adalterome-gene-report`
   - Research-style report skill.
   - Builds a deep Markdown draft for one gene.
   - Supports mechanism synthesis, evidence caveats, and follow-up gap analysis.

5. `adalterome-term-report`
   - Research-style report skill for phenotypes, ontology terms, and pathological processes.
   - Uses `/term/overview` and `/term/curation`, with `/term/events` as capped fallback.
   - Emphasizes top genes, top hypotheses, evidence traces, and broad-term caveats.

6. `adalterome-hypothesis-report`
   - Research-style report skill for AD hypothesis support.
   - Uses `/hypothesis/overview` and `/hypothesis/curation`, with `/hypothesis/support` as capped fallback.
   - Separates curated hypothesis labels from original sentence evidence.

7. `adalterome-compare-report`
   - Research-style report skill for two-gene comparison.
   - Uses `/compare/genes` plus per-gene overview and curation packages for both genes.
   - Keeps common patterns and gene-specific evidence separate.

8. `adalterome-case-study-expert`
   - Expert interpretation layer above the report skills.
   - Uses AD-Alterome full-pool curation first, then applies coverage checks, comparison-balance checks, transparent expert evidence scoring, long-tail protection, and AD pathology-oriented biological trimming.
   - Produces a two-layer output: a paper-style case-study narrative plus an audit appendix with scored evidence and exact sentence traces.
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

Expert case-study mode adds a separate transparent expert score for case-study usefulness. This score is not a human gold label. It prioritizes AD specificity, molecular or pathological mechanism depth, long-tail insight, fit to the user's scientific question, PMID traceability, and common-sense filtering of generic evidence.

Large genes and broad hypotheses can expose curation risk. When full-pool curation is unavailable and a report falls back to `api_sentence_sample`, the expert layer must label conclusions as exploratory and avoid absence-of-evidence claims. In two-gene comparisons, unequal curation scope or strongly different coverage ratios must downgrade strong contrastive conclusions.

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
    └── adalterome-case-study-expert/
```

## Versioning Strategy

The unified `adalterome` entrypoint is the recommended user-facing route. The specialized report skills remain stable direct-entry versions optimized for reproducible evidence packages that human experts can interpret later.

The expert version lives in `adalterome-case-study-expert`. It should be selected when the user asks for case studies, AD pathology insight, biological interpretation, long-tail candidate judgment, or paper-level argumentation. This keeps report and expert behavior available side by side instead of overwriting the stable report contract.
