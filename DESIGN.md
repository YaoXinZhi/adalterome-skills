# AD-Alterome Skills Design Notes

This repository follows the layered style of `r1seee/cucurlitbase-skills`.

## Skill Layers

1. `adalterome-api`
   - Lowest-level retrieval skill.
   - Calls the live AD-Alterome REST API.
   - Preserves exact sentence evidence, PubMed links, Event chains, and normalized Evidence blocks.

2. `adalterome-report`
   - Presentation skill.
   - Converts API outputs into a fixed report contract.
   - Keeps provenance and evidence sections stable across runs.

3. `adalterome-gene-report`
   - Research-style report skill.
   - Builds a deep Markdown draft for one gene.
   - Supports mechanism synthesis, evidence caveats, and follow-up gap analysis.

4. `adalterome-term-report`
   - Research-style report skill for phenotypes, ontology terms, and pathological processes.
   - Uses `/term/overview` and `/term/events`.
   - Emphasizes top genes, top hypotheses, evidence traces, and broad-term caveats.

5. `adalterome-hypothesis-report`
   - Research-style report skill for AD hypothesis support.
   - Uses `/hypothesis/overview` and `/hypothesis/support`.
   - Separates curated hypothesis labels from original sentence evidence.

6. `adalterome-compare-report`
   - Research-style report skill for two-gene comparison.
   - Uses `/compare/genes` plus sentence-level evidence for both genes.
   - Keeps common patterns and gene-specific evidence separate.

## Writing Style

- Keep `SKILL.md` short and procedural.
- Put endpoint details, report contracts, and caveats in `references/`.
- Use deterministic scripts for repeated API retrieval and report scaffolding.
- Preserve original evidence sentences exactly.
- Treat AD-Alterome interpretation fields as curated interpretation, not causal proof.
- Use PubMed links from PMID for traceability.

## Evidence Quality Strategy

The AD-Alterome API is expected to return `EvidenceQualityScore`.
Skills should prefer high-quality rows and still show the exact original sentence so users can audit whether the sentence is informative.

## Repository Layout

```text
adalterome-skills/
├── README.md
├── DESIGN.md
└── skills/
    ├── adalterome-api/
    ├── adalterome-report/
    ├── adalterome-gene-report/
    ├── adalterome-term-report/
    ├── adalterome-hypothesis-report/
    └── adalterome-compare-report/
```
