# AD-Alterome Skills Revision Plan: AI for Biomedical Knowledge Synthesis

Date: 2026-06-20

## 1. Revised Positioning

AD-Alterome skills should no longer be framed as tools that directly generate
expert mechanism conclusions or paper-ready biological case claims. The revised
positioning is:

> AI for Biomedical Knowledge Synthesis: a provenance-preserving system that
> organizes complex Alzheimer disease alteration evidence into auditable
> knowledge packets for expert evaluation.

The AI output is therefore an evaluation object, not the final biological
conclusion. The manuscript emphasis shifts from "AI guesses mechanisms" to
"AI reliably organizes complex disease evidence under expert review".

## 2. Reviewer-Risk Mapping

| Reviewer concern | Risk | Skill and manuscript response |
| --- | --- | --- |
| AD experts may ask whether the work advances AD mechanisms. | Overclaiming mechanism discovery would be fragile. | State that AD-Alterome organizes sentence-level evidence and helps experts review mechanism candidates; it does not prove mechanisms. |
| AI or digital medicine experts may ask how this differs from generic LLM/RAG. | A generic narrative generator would look incremental. | Emphasize alteration-centered schema, full-pool curation, long-tail rescue, PMID traceability, structured outputs, and expert evaluation rubrics. |
| Genomics experts may ask whether the alterome resource is systematic and reusable. | The resource could look like a sentence collection. | Surface event schema, API contract, curation source, data versioning, field normalization, cache/provenance manifests, and reusable JSON/TSV outputs. |
| Systems biology experts may ask whether system-level patterns are revealed. | Claims of causal networks would be overreach. | Present evidence topology, gene-alteration-process-hypothesis organization, hypothesis overlap, and long-tail bridges as literature-evidence organization patterns, not causal networks. |
| Reviewers may question LLM reliability. | Hallucination and attribution errors are expected concerns. | Add expert review sheets, rubric-based scoring, baseline comparison plans, and explicit non-claims in every synthesis packet. |

## 3. Manuscript-Aligned Result Structure

### 3.1 Event Schema

Provide the schema used by AD-Alterome evidence organization:

- gene and Entrez ID
- genetic alteration taxonomy and mention
- trigger word and regulation type
- phenotype/process term and ontology context
- AD hypothesis label and explanation fields
- PMID, journal, year, and exact sentence provenance

### 3.2 Full-Database Evidence Landscape

Use the API and curated pool to expose:

- event count, event-unique count, PMID count, gene count
- gene, phenotype/process, alteration, hypothesis, and year distributions
- publication concentration and broad-term dominance
- long-tail definitions and retained candidate evidence

### 3.3 Callable Analytical Patterns

The skills should support multiple entry patterns over the same AD-Alterome
resource:

- single-gene entry: `PSEN1`
- multi-gene entry: `APOE vs APP`
- gene-set entry: AD-specific enrichment or selected AD gene panels
- recommendation entry: `MAPT` phenotype landscape
- hypothesis/network entry: `TREM2-DAP12 neuroinflammatory axis`

### 3.4 Researcher-Facing Knowledge Synthesis

The agent skill should convert structured results into a researcher-facing
knowledge packet. It should not output a final paper section. The packet should
include source-backed organization, evidence maps, candidate groupings, original
sentences, and expert review materials.

## 4. Skill Architecture Changes

### 4.1 Add `adalterome-knowledge-synthesis`

Create a new skill above report mode and beside the legacy case-study skill.
Its job is to build auditable knowledge packets for expert review.

Expected outputs:

- `knowledge_packet.md`
- `evidence_map.md`
- `expert_review_sheet.tsv`
- `evaluation_record.json`
- `provenance_manifest.json`
- `data/cache_manifest.json`
- raw target JSON files under `data/`

### 4.2 Update `adalterome` Unified Entrypoint

The unified entrypoint should route:

- raw lookup tasks to `adalterome-api`
- fixed evidence packets to `adalterome-report`
- deep traceable reports to gene/term/hypothesis/compare report skills
- evidence organization, evaluation, literature-review support, and
  knowledge-synthesis tasks to `adalterome-knowledge-synthesis`
- legacy expert narrative requests to `adalterome-case-study-expert`, with a
  preference for knowledge synthesis when the output will be used for a paper
  or expert scoring

### 4.3 Reframe `adalterome-case-study-expert`

Keep the existing skill for compatibility, but make it clear that the preferred
publication-facing workflow is the knowledge-synthesis packet plus expert
evaluation worksheet.

## 5. Knowledge Packet Contract

`knowledge_packet.md` should include:

1. query scope and user intent
2. active analytical pattern
3. event schema used in the analysis
4. evidence landscape and coverage profile
5. organized evidence groups
6. gene-alteration-phenotype/hypothesis map
7. long-tail evidence candidates
8. AI-organized synthesis for expert review
9. expert review worksheet instructions
10. original evidence traces and PubMed links
11. limitations and non-claims

Required non-claims:

- The packet does not prove an AD mechanism.
- The packet does not replace expert review.
- AI-organized groups are hypotheses for review, not manuscript conclusions.
- `EvidenceScore` is not used or displayed as evidence strength.

## 6. Expert Review Sheet

The expert review sheet should be generated as TSV with one row per organized
evidence item and blank scoring columns for human review.

Recommended 1-5 scoring dimensions:

- traceability
- accuracy
- breadth
- depth
- organization usefulness
- long-tail usefulness
- hallucination or overclaim risk
- inspiration
- review efficiency
- overall usefulness

Suggested reviewer types:

- clinical or translational AD experts
- AD/neurodegeneration researchers
- biomedical graduate students or postdocs

The sheet should also include reviewer-facing fields:

- evidence ID
- target
- PMID and PubMed URL
- gene
- alteration taxonomy
- phenotype/process
- hypothesis
- evidence type
- mechanism strata
- long-tail flag
- AI organization score or decision
- original sentence
- reviewer notes

## 7. Evaluation Design

Core evaluation cases:

- 3.4.1 single-gene entry: `PSEN1`
- 3.4.2 hypothesis/network entry: `TREM2-DAP12 neuroinflammatory axis`

Additional smoke/evaluation cases:

- multi-gene entry: `APOE vs APP`
- recommendation entry: `MAPT phenotype landscape`

Comparison baselines for the manuscript:

- generic LLM without AD-Alterome
- generic LLM plus ordinary RAG
- frequency top-k AD-Alterome evidence
- AD-Alterome without long-tail rescue
- AD-Alterome knowledge-synthesis skill

Fairness controls:

- same natural-language question
- same model when comparing LLM conditions
- same output length budget
- same time budget
- same scoring rubric
- blinded method labels when feasible

## 8. Implementation Plan

1. Add this revision plan as the implementation anchor.
2. Add `adalterome-knowledge-synthesis` with a builder script.
3. Reuse existing API, curation, cache, and AD expert pruning helpers.
4. Generate knowledge packet, evidence map, expert review sheet, evaluation
   record, provenance manifest, and raw data files.
5. Update `adalterome` routing instructions and repository README/DESIGN.
6. Reframe `adalterome-case-study-expert` as compatibility/legacy narrative
   mode.
7. Run smoke cases for `PSEN1`, `APOE vs APP`, `MAPT phenotype landscape`, and
   `TREM2-DAP12 neuroinflammatory axis`.
8. Write a Chinese evaluation report summarizing whether the revised skills
   meet the knowledge-synthesis goal.

## 9. Acceptance Criteria

- Users can invoke a single knowledge-synthesis skill for gene, comparison,
  gene-set, phenotype/process, hypothesis, and hypothesis/network patterns.
- The generated output clearly says it is for expert evaluation, not final
  biological truth.
- Every key evidence item preserves PMID, PubMed URL when available, and exact
  original sentence.
- Expert review TSV is created and includes all rubric columns.
- Evaluation record documents reviewer groups, scoring dimensions, baselines,
  fairness controls, and non-claims.
- Smoke cases run successfully and produce the expected files.
- Repository documentation and skill metadata are aligned with the revised
  "AI for Biomedical Knowledge Synthesis" framing.
