---
name: adalterome-knowledge-synthesis
description: Public research/evaluation AD-Alterome entrypoint for AI-for-biomedical-knowledge-synthesis. Use directly when the user explicitly asks to organize Alzheimer disease alteration evidence, prepare an evidence map, generate an expert review sheet, evaluate AI-for-biomedical-knowledge-synthesis, compare AD-Alterome against generic LLM/RAG outputs, inspect long-tail evidence, or create publication-facing but non-conclusive knowledge packets from gene, phenotype/process, hypothesis, multi-gene, gene-set, recommendation, or hypothesis/network queries. Ordinary AD-Alterome questions can start from adalterome.
---

# AD-Alterome Knowledge Synthesis

Use this skill when the user wants AD-Alterome evidence organized for human
expert review rather than turned into final biological conclusions.

> Public research entry: users may call this skill directly for knowledge
> synthesis and expert-evaluation workflows. For ordinary AD-Alterome lookup or
> report requests, start from `adalterome`.

This is the preferred publication-facing synthesis layer for the revised
`AI for Biomedical Knowledge Synthesis` framing. It keeps AD-Alterome
provenance first, uses full-pool curation endpoints, protects long-tail
evidence, and outputs an expert review worksheet so AI-organized content can be
evaluated rather than treated as manuscript truth.

## When To Use

Use this skill for:

- researcher-facing knowledge packets
- evidence organization for literature review
- evidence maps and evidence topology
- expert review sheets or scoring tables
- hallucination/accuracy/usefulness evaluation materials
- single-gene, multi-gene, gene-set, phenotype/process, hypothesis, and
  hypothesis/network analytical patterns
- long-tail evidence screening
- fair comparison with generic LLM or RAG baselines

Use the stable report skills when the user only wants traceable evidence
dossiers. Use the legacy `adalterome-case-study-expert` only when the user
explicitly asks for an older case-study narrative style.

## Quick Start

Single-gene entry:

```bash
python3 scripts/build_knowledge_synthesis.py --gene PSEN1 --output-dir outputs/psen1_knowledge --organized-limit 18
```

Multi-gene entry:

```bash
python3 scripts/build_knowledge_synthesis.py --gene-a APOE --gene-b APP --pattern multi_gene --output-dir outputs/apoe_app_knowledge
```

Recommendation entry:

```bash
python3 scripts/build_knowledge_synthesis.py --gene MAPT --pattern recommendation --question "Organize the MAPT phenotype landscape for expert review." --output-dir outputs/mapt_phenotype_landscape
```

Hypothesis/network entry:

```bash
python3 scripts/build_knowledge_synthesis.py --gene-set TREM2 TYROBP --hypothesis "Neuroinflammation Hypothesis" --axis "TREM2-DAP12 neuroinflammatory axis" --pattern hypothesis_network --output-dir outputs/trem2_dap12_axis
```

## Expected Outputs

- `knowledge_packet.md`
- `evidence_map.md`
- `expert_review_sheet.tsv`
- `evaluation_record.json`
- `provenance_manifest.json`
- `data/query.json`
- `data/coverage.json`
- `data/knowledge_synthesis.json`
- `data/ad_expert_pruning.json`
- `data/cache_manifest.json`
- target-specific raw overview, evidence, and curation JSON files

## Workflow

1. Identify the user intent and analytical pattern.
2. Use server-side curation endpoints; do not fall back to capped event
   endpoints for publication-facing synthesis.
3. Request a broad candidate pool with `--candidate-limit`, then keep a
   bounded organized subset with `--organized-limit`.
   By default, `--candidate-limit` uses the current API maximum of 500. For
   quick smoke tests, use at least `--candidate-limit 20`; lower values are
   raised to 20 automatically. Reduce the candidate limit only when latency or
   payload size matters more than coverage.
4. Inspect `data/coverage.json` before making claims.
5. Use `knowledge_packet.md` as an AI-organized review object, not paper text.
6. Give `expert_review_sheet.tsv` to human reviewers for rubric scoring.
7. Preserve `data/cache_manifest.json` and source payloads for reproducibility.

## Analytical Patterns

- `single_gene`: one gene, such as `PSEN1`.
- `multi_gene`: two-gene comparison, such as `APOE` vs `APP`.
- `gene_set`: several genes reviewed together.
- `recommendation`: landscape/recommendation-oriented evidence organization,
  such as `MAPT` phenotype landscape.
- `phenotype_process`: one phenotype, ontology term, or biological process.
- `hypothesis`: one AD hypothesis.
- `hypothesis_network`: hypothesis or axis-centered synthesis, such as
  `TREM2-DAP12 neuroinflammatory axis`.

## Non-Claims

- The packet does not prove an AD mechanism.
- The packet does not replace human expert review.
- AI-organized groups are review candidates, not manuscript conclusions.
- `EvidenceScore` is not displayed or interpreted as evidence strength.
- PubMed-linked sentence evidence supports traceability, not causal proof.

## Resources

- Builder script: [scripts/build_knowledge_synthesis.py](scripts/build_knowledge_synthesis.py)
- Output contract: [references/knowledge_synthesis_contract.md](references/knowledge_synthesis_contract.md)
