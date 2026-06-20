# AD-Alterome Knowledge Synthesis Packet: TREM2-DAP12 neuroinflammatory axis

## Query Scope and User Intent

- User question: Organize AD-Alterome evidence for the TREM2-DAP12 neuroinflammatory axis as a hypothesis/network review object.
- Output role: AI-organized evidence structure for expert evaluation.
- Manuscript role: evaluation object for AI-for-biomedical-knowledge-synthesis, not paper-ready biological conclusion.

## Analytical Pattern

- Pattern: `hypothesis_network`
- Targets: TREM2, TYROBP, Neuroinflammation Hypothesis

## Event Schema Used

| Layer | Fields | Use in this packet |
| --- | --- | --- |
| Gene | `Gene`, `Entrez` | Anchors the alteration evidence to a genetic entity. |
| Alteration | `AlterationType`, `AlterationMention`, `AlterationID` | Keeps AD-Alterome alteration-centered rather than only gene-centered. |
| Event relation | `TriggerWord`, `RegType`, `Event` | Records the extracted relation context; not treated as genetic alteration labels. |
| Phenotype/process | `TermName`, `TermID`, `TermType`, ontology fields | Organizes downstream biological processes, clinical phenotypes, and pathology features. |
| AD interpretation | `Hypothesis`, `MechanismProvided`, `HypothesisReason`, `ExtendedExplanation` | Used as curated interpretation fields that require expert review. |
| Provenance | `PMID`, `Journal`, `Year`, `Sentence`, `PubMedURL` | Makes every organized item traceable to source sentences. |

`EvidenceScore` is intentionally not used or displayed as evidence strength.

## Evidence Landscape and Coverage

| Target | Curation scope | Pool rows | Event-unique rows | Matched events | Unique PMIDs | Coverage warnings |
| --- | --- | --- | --- | --- | --- | --- |
| TREM2 | offline_full_query_pool_prescreened | 1019 | 1019 | 6446 | 486 | - |
| TYROBP | offline_full_query_pool_prescreened | 189 | 189 | 673 | 57 | - |
| Neuroinflammation Hypothesis | offline_full_query_pool_prescreened | 5304 | 5304 | 34086 | 3063 | - |

- Balance status: `balanced`
- Targets have comparable curation scope for knowledge synthesis.

## Organized Evidence Groups

### model_or_intervention

- Organized evidence rows: `6`
- Genes represented: MAPT, NLRC3, TREM2, TYROBP
- Phenotype/process features represented: entorhinal cortex loss, Neurodegeneration, complement activation, amyloid protein, hyperphosphorylation, Alzheimer
- Mechanism strata: neuroinflammation and microglia axis (6), amyloid/tau axis (5), synaptic and neuronal dysfunction axis (3)


## Gene-Alteration-Phenotype/Hypothesis Map

| Gene | Alteration taxonomy | Phenotype/process | Hypothesis | Evidence rows | Long-tail rows |
| --- | --- | --- | --- | --- | --- |
| MAPT | normalized variants:dna change | entorhinal cortex loss | Tau Protein Hypothesis,Neuroinflammation Hypothesis | 1 | 1 |
| NLRC3 | point mutations:mutations | Neurodegeneration | Amyloid Hypothesis,Neuroinflammation Hypothesis | 1 | 1 |
| TREM2 | normalized variants:dna change | complement activation | Neuroinflammation Hypothesis | 1 | 1 |
| TREM2 | normalized variants:dna change | amyloid protein | Amyloid Hypothesis,Neuroinflammation Hypothesis | 1 | 1 |
| TYROBP | normalized variants:dna change | hyperphosphorylation | Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis | 1 | 1 |
| TYROBP | point mutations:mutations | Alzheimer | Amyloid Hypothesis,Neuroinflammation Hypothesis | 1 | 1 |

## Long-Tail Evidence Candidates

| Rank | Target | PMID | Gene | Phenotype/process | Why review it |
| --- | --- | --- | --- | --- | --- |
| 1 | Neuroinflammation Hypothesis | [36966157](https://pubmed.ncbi.nlm.nih.gov/36966157/) | MAPT | entorhinal cortex loss | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 2 | Neuroinflammation Hypothesis | [35173266](https://pubmed.ncbi.nlm.nih.gov/35173266/) | NLRC3 | Neurodegeneration | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 3 | TREM2 | [37969043](https://pubmed.ncbi.nlm.nih.gov/37969043/) | TREM2 | complement activation | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 4 | TREM2 | [37090086](https://pubmed.ncbi.nlm.nih.gov/37090086/) | TREM2 | amyloid protein | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 5 | TYROBP | [32709045](https://pubmed.ncbi.nlm.nih.gov/32709045/) | TYROBP | hyperphosphorylation | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 6 | TYROBP | [28612290](https://pubmed.ncbi.nlm.nih.gov/28612290/) | TYROBP | Alzheimer | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 7 | Neuroinflammation Hypothesis | [35273086](https://pubmed.ncbi.nlm.nih.gov/35273086/) | MAPT | sleep | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 8 | TREM2 | [33446504](https://pubmed.ncbi.nlm.nih.gov/33446504/) | TREM2 | Microglia activation | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 9 | Neuroinflammation Hypothesis | [37587513](https://pubmed.ncbi.nlm.nih.gov/37587513/) | PTGS2 | cognitive decline via reducing neurotoxic Abeta | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 10 | Neuroinflammation Hypothesis | [37090086](https://pubmed.ncbi.nlm.nih.gov/37090086/) | TREM2 | amyloid protein | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 11 | TREM2 | [37274187](https://pubmed.ncbi.nlm.nih.gov/37274187/) | TREM2 | senile dementia | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 12 | TREM2 | [36658241](https://pubmed.ncbi.nlm.nih.gov/36658241/) | TREM2 | neurotoxicity of Abeta plaques | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 13 | TREM2 | [36721205](https://pubmed.ncbi.nlm.nih.gov/36721205/) | TREM2 | reactive gliosis | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 14 | TREM2 | [32709045](https://pubmed.ncbi.nlm.nih.gov/32709045/) | TREM2 | neuritic tau hyperphosphorylation | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 15 | Neuroinflammation Hypothesis | [37165437](https://pubmed.ncbi.nlm.nih.gov/37165437/) | APP | neuronal cell loss or NFTs | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 16 | Neuroinflammation Hypothesis | [36658241](https://pubmed.ncbi.nlm.nih.gov/36658241/) | TREM2 | neurotoxicity of Abeta plaques | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |

## AI-Organized Synthesis for Expert Review

For `TREM2-DAP12 neuroinflammatory axis`, the skill organized evidence for the question: `Organize AD-Alterome evidence for the TREM2-DAP12 neuroinflammatory axis as a hypothesis/network review object.`.

This section is a review object. It proposes a structure for expert inspection and should not be copied as a final manuscript conclusion.

- Analytical pattern: `hypothesis_network`
- Dominant mechanism strata among organized evidence: neuroinflammation and microglia axis (6), amyloid/tau axis (5), synaptic and neuronal dysfunction axis (3)
- Frequently represented genes: TREM2, TYROBP, MAPT, NLRC3
- Frequently represented phenotype/process features: entorhinal cortex loss, Neurodegeneration, complement activation, amyloid protein, hyperphosphorylation, Alzheimer
- Frequently represented hypotheses: Amyloid Hypothesis,Neuroinflammation Hypothesis, Tau Protein Hypothesis,Neuroinflammation Hypothesis, Neuroinflammation Hypothesis, Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis
- Long-tail rows retained for review: `6`
- Secondary evidence is retained in `data/ad_expert_pruning.json` and can support caveats, but should not drive strong claims without manual review.

## Expert Review Worksheet

Reviewer-facing worksheet: `expert_review_sheet.tsv`.

Suggested reviewer groups:

- clinical or translational AD experts
- AD or neurodegeneration researchers
- biomedical graduate students or postdocs

Recommended scoring dimensions use 1-5 scores, with `cannot_judge` allowed:

| Dimension | Reviewer question |
| --- | --- |
| Traceability | Are important statements backed by PMID and original sentence evidence? |
| Accuracy | Are gene, alteration, phenotype/process, and hypothesis attributions correct? |
| Breadth | Does the packet cover the relevant evidence space rather than only dominant high-frequency records? |
| Depth | Does the organized evidence include molecular, cellular, pathological, or model-level detail? |
| Organization usefulness | Do the evidence groups make the complex AD evidence easier to review? |
| Long-tail usefulness | Are low-frequency but potentially informative records surfaced for review? |
| Hallucination or overclaim risk | Score high when hallucination or unsupported overclaim risk is low. |
| Inspiration | Does the packet help generate useful review, mechanism, or experiment questions? |
| Review efficiency | Does the packet reduce the time needed to inspect the evidence? |
| Overall usefulness | Does the packet meet the user need better than unstructured search or generic LLM output? |

## Original Evidence Traces

### 1. Neuroinflammation Hypothesis / PMID [36966157](https://pubmed.ncbi.nlm.nih.gov/36966157/)

- AI organization score: `142.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `MAPT` / `normalized variants:dna change` / `entorhinal cortex loss` / `Tau Protein Hypothesis,Neuroinflammation Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: Reinforcing earlier discussion on hp-tau aggregates and neuronal phagoptosis, APOE knockdown in P301S mice significantly reduced hippocampal and entorhinal cortex loss; APOE preservation increased Iba1 + (suggesting microglia and macrophage populations) cells that were positive with CD68 + phagocytic inclusions.

### 2. Neuroinflammation Hypothesis / PMID [35173266](https://pubmed.ncbi.nlm.nih.gov/35173266/)

- AI organization score: `142.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `NLRC3` / `point mutations:mutations` / `Neurodegeneration` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: Considering that wild type NLRC3 is involved in lowering inflammation, and overexpression has been shown to inhibit the deposition of A-beta, and reverse the degeneration of neurons in APP/PS1 mice, we speculate that rare variants in NLRC3 elevate inflammation, resulting in increased neurodegeneration and dementia symptoms.

### 3. TREM2 / PMID [37969043](https://pubmed.ncbi.nlm.nih.gov/37969043/)

- AI organization score: `141.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `TREM2` / `normalized variants:dna change` / `complement activation` / `Neuroinflammation Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: Furthermore, mouse brains transplanted with TREM2 R47H/+ microglia exhibited reduced synaptic density, with upregulation of multiple complement cascade components in TREM2 R47H/+ microglia suggesting inappropriate synaptic pruning as one potential mechanism.

### 4. TREM2 / PMID [37090086](https://pubmed.ncbi.nlm.nih.gov/37090086/)

- AI organization score: `141.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `TREM2` / `normalized variants:dna change` / `amyloid protein` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: In addition, inhibiting the expression of TREM2 can promote the abnormal accumulation of amyloid protein and aggravate the impairment of spatial learning ability in P301S transgenic mice.

### 5. TYROBP / PMID [32709045](https://pubmed.ncbi.nlm.nih.gov/32709045/)

- AI organization score: `140.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `TYROBP` / `normalized variants:dna change` / `hyperphosphorylation` / `Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: Further, TREM2 or DAP12 haplodeficient AD-like mice or AD patients with R47H mutations exhibited less compact toxic plaques thus leading to severe neuritic tau hyperphosphorylation and increased plaque-associated neuritic dystrophies.

### 6. TYROBP / PMID [28612290](https://pubmed.ncbi.nlm.nih.gov/28612290/)

- AI organization score: `138.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `TYROBP` / `point mutations:mutations` / `Alzheimer` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: Some modulatory effects of TYROBP on Alzheimer's-related genes were only apparent on a background of mice with cerebral amyloidosis due to overexpression of mutant APP/PSEN1.


## Limitations and Non-Claims

- This packet organizes AD-Alterome sentence-level evidence; it does not prove an AD mechanism.
- This packet does not replace expert review.
- AI-organized evidence groups are review candidates, not manuscript conclusions.
- Human experts should score traceability, accuracy, depth, breadth, hallucination or overclaim risk, and usefulness before using the packet in a manuscript.
- `EvidenceScore` is not used or displayed as evidence strength.
- `EvidenceQualityScore`, when present in raw payloads, is a sentence-usefulness signal rather than proof strength.
- PubMed-linked sentences support provenance, not direct causal validation.
- Curation scope and coverage warnings should be reported when comparing targets.

## Source Payloads

- Raw API cache manifest: `data/cache_manifest.json`
- Provenance manifest: `provenance_manifest.json`
- `TREM2` overview: http://117.72.176.137/api/adalterome/gene/overview?gene=TREM2
- `TREM2` curation/evidence: http://117.72.176.137/api/adalterome/gene/curation?gene=TREM2&selected_limit=12
- `TYROBP` overview: http://117.72.176.137/api/adalterome/gene/overview?gene=TYROBP
- `TYROBP` curation/evidence: http://117.72.176.137/api/adalterome/gene/curation?gene=TYROBP&selected_limit=12
- `Neuroinflammation Hypothesis` overview: http://117.72.176.137/api/adalterome/hypothesis/overview?hypothesis=Neuroinflammation+Hypothesis
- `Neuroinflammation Hypothesis` curation/evidence: http://117.72.176.137/api/adalterome/hypothesis/curation?hypothesis=Neuroinflammation+Hypothesis&selected_limit=12