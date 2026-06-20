# AD-Alterome Knowledge Synthesis Packet: PSEN1

## Query Scope and User Intent

- User question: Organize AD-Alterome evidence for PSEN1 into a knowledge synthesis packet.
- Output role: AI-organized evidence structure for expert evaluation.
- Manuscript role: evaluation object for AI-for-biomedical-knowledge-synthesis, not paper-ready biological conclusion.

## Analytical Pattern

- Pattern: `single_gene`
- Targets: PSEN1

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
| PSEN1 | offline_full_query_pool_prescreened | 2398 | 2398 | 21835 | 1481 | - |

- Balance status: `not_applicable`

## Organized Evidence Groups

### model_or_intervention

- Organized evidence rows: `6`
- Genes represented: PSEN1
- Phenotype/process features represented: pilus, attenuated neuroinflammation, cell population proliferation, Prolonged, reactive gliosis, AD hallmarks
- Mechanism strata: amyloid/tau axis (6), neuroinflammation and microglia axis (4), synaptic and neuronal dysfunction axis (2)


## Gene-Alteration-Phenotype/Hypothesis Map

| Gene | Alteration taxonomy | Phenotype/process | Hypothesis | Evidence rows | Long-tail rows |
| --- | --- | --- | --- | --- | --- |
| PSEN1 | normalized variants:dna change | pilus | Tau Protein Hypothesis,Neuroinflammation Hypothesis | 1 | 1 |
| PSEN1 | normalized variants:dna change | attenuated neuroinflammation | Amyloid Hypothesis,Neuroinflammation Hypothesis | 1 | 1 |
| PSEN1 | point mutations:mutations | cell population proliferation | Amyloid Hypothesis | 1 | 1 |
| PSEN1 | normalized variants:dna change | Prolonged | Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis | 1 | 1 |
| PSEN1 | point mutations:mutations | reactive gliosis | Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis | 1 | 1 |
| PSEN1 | normalized variants:dna change | AD hallmarks | Amyloid Hypothesis,Tau Protein Hypothesis | 1 | 1 |

## Long-Tail Evidence Candidates

| Rank | Target | PMID | Gene | Phenotype/process | Why review it |
| --- | --- | --- | --- | --- | --- |
| 1 | PSEN1 | [33171143](https://pubmed.ncbi.nlm.nih.gov/33171143/) | PSEN1 | pilus | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 2 | PSEN1 | [36829747](https://pubmed.ncbi.nlm.nih.gov/36829747/) | PSEN1 | attenuated neuroinflammation | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 3 | PSEN1 | [37655317](https://pubmed.ncbi.nlm.nih.gov/37655317/) | PSEN1 | cell population proliferation | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 4 | PSEN1 | [37998336](https://pubmed.ncbi.nlm.nih.gov/37998336/) | PSEN1 | Prolonged | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 5 | PSEN1 | [37095621](https://pubmed.ncbi.nlm.nih.gov/37095621/) | PSEN1 | reactive gliosis | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 6 | PSEN1 | [36968493](https://pubmed.ncbi.nlm.nih.gov/36968493/) | PSEN1 | AD hallmarks | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 7 | PSEN1 | [37513800](https://pubmed.ncbi.nlm.nih.gov/37513800/) | presenilin-1 | roseolovirus infection | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 8 | PSEN1 | [38063257](https://pubmed.ncbi.nlm.nih.gov/38063257/) | PSEN1 | glycolytic process | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 9 | PSEN1 | [37394008](https://pubmed.ncbi.nlm.nih.gov/37394008/) | PSEN1 | Stable | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 10 | PSEN1 | [36959497](https://pubmed.ncbi.nlm.nih.gov/36959497/) | PSEN1 | amyloid aggregation | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 11 | PSEN1 | [35847683](https://pubmed.ncbi.nlm.nih.gov/35847683/) | FAD | lysosomal deficiencies | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 12 | PSEN1 | [37298443](https://pubmed.ncbi.nlm.nih.gov/37298443/) | PSEN1 | voluntary alcohol consumption | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 13 | PSEN1 | [37553376](https://pubmed.ncbi.nlm.nih.gov/37553376/) | PSEN1 | Melanoma | molecular_mechanism evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 14 | PSEN1 | [36901549](https://pubmed.ncbi.nlm.nih.gov/36901549/) | PSEN1 | cognitive impairments | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 15 | PSEN1 | [37394008](https://pubmed.ncbi.nlm.nih.gov/37394008/) | PSEN1 | Transient | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 16 | PSEN1 | [35391749](https://pubmed.ncbi.nlm.nih.gov/35391749/) | PSEN1 | - | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |

## AI-Organized Synthesis for Expert Review

For `PSEN1`, the skill organized evidence for the question: `Organize AD-Alterome evidence for PSEN1 into a knowledge synthesis packet.`.

This section is a review object. It proposes a structure for expert inspection and should not be copied as a final manuscript conclusion.

- Analytical pattern: `single_gene`
- Dominant mechanism strata among organized evidence: amyloid/tau axis (6), neuroinflammation and microglia axis (4), synaptic and neuronal dysfunction axis (2)
- Frequently represented genes: PSEN1
- Frequently represented phenotype/process features: pilus, attenuated neuroinflammation, cell population proliferation, Prolonged, reactive gliosis, AD hallmarks
- Frequently represented hypotheses: Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis, Tau Protein Hypothesis,Neuroinflammation Hypothesis, Amyloid Hypothesis,Neuroinflammation Hypothesis, Amyloid Hypothesis, Amyloid Hypothesis,Tau Protein Hypothesis
- Long-tail rows retained for review: `6`

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

### 1. PSEN1 / PMID [33171143](https://pubmed.ncbi.nlm.nih.gov/33171143/)

- AI organization score: `138.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `PSEN1` / `normalized variants:dna change` / `pilus` / `Tau Protein Hypothesis,Neuroinflammation Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: Evidence has shown that CCI causes an injury-severity-dependent increase in P-tau (notably at Ser199, Thr205, Thr231, Ser396, Ser422) in the ipsilateral fimbria/amygdala and contralateral CA1 regions of 3xTg AD mice (carrying SweAPP, MAPT P301L and PSEN1 M146V transgenes) compared with sham 3xTg AD mice, which can be attenuated by a treatment of D-JNKil, a peptide inhibitor of JNK.

### 2. PSEN1 / PMID [36829747](https://pubmed.ncbi.nlm.nih.gov/36829747/)

- AI organization score: `136.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `PSEN1` / `normalized variants:dna change` / `attenuated neuroinflammation` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: In addition to alleviation of Abeta-induced cognitive impairment, other groups found that MSC-derived exosomes promoted neurogenesis in the subventricular zone and attenuated neuroinflammation in drug (streptozotocin)-induced AD mice, double transgenic (APP/PS1) AD, and triple (APP Swedish, MAPT P301L, and PSEN1 M146V) transgenic AD mouse models.

### 3. PSEN1 / PMID [37655317](https://pubmed.ncbi.nlm.nih.gov/37655317/)

- AI organization score: `136.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `PSEN1` / `point mutations:mutations` / `cell population proliferation` / `Amyloid Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: amyloid/tau axis; synaptic and neuronal dysfunction axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: In double transgenic mice expressing human mutant amyloid-beta precursor protein (APP) and presenilin-1 (PS1) (TgAPP/PS1 model), EGb 761 significantly increased cell proliferation in the hippocampus, which may be mediated by activation of cellular transcription factor cAMP response element-binding protein (CREB).

### 4. PSEN1 / PMID [37998336](https://pubmed.ncbi.nlm.nih.gov/37998336/)

- AI organization score: `134.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `PSEN1` / `normalized variants:dna change` / `Prolonged` / `Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: In line with this, prolonged hyperbaric oxygen treatment can reduce hypoxia, neuroinflammation, the accumulation of Abeta and phosphorylated tau, leading to a significant improvement of cognitive performances in a 3xTg AD mouse model carrying three mutations associated with familial AD (APP Swedish, MAPT P301L, and PSEN1 M146V) when tested in hippocampal-dependent behavioral tasks and, possibly, in affected patients.

### 5. PSEN1 / PMID [37095621](https://pubmed.ncbi.nlm.nih.gov/37095621/)

- AI organization score: `134.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `PSEN1` / `point mutations:mutations` / `reactive gliosis` / `Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: To this end, we employed the TgF344-AD transgenic rat model which expresses both mutant human amyloid precursor protein (APP  SW ) and presenilin 1 (PS1DeltaE9), resulting in the recapitulation of age-dependent AD pathology including elevated soluble amyloid-beta, hyperphosphorylated tau, neuronal loss, and gliosis as early as 6 months of age.

### 6. PSEN1 / PMID [36968493](https://pubmed.ncbi.nlm.nih.gov/36968493/)

- AI organization score: `134.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `PSEN1` / `normalized variants:dna change` / `AD hallmarks` / `Amyloid Hypothesis,Tau Protein Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: amyloid/tau axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: We aimed to investigate whether the triple-transgenic AD (3xTg-AD) mice harboring PS1 M146V , APP Swe , and Tau P301L show sex differences in beta-amyloid (Abeta) and hyperphosphorylated tau (p-Tau), the two primary AD hallmarks, and how local 17beta-estradiol (E2) may regulate the expression of EGR1 and AChE.


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
- `PSEN1` overview: http://117.72.176.137/api/adalterome/gene/overview?gene=PSEN1
- `PSEN1` curation/evidence: http://117.72.176.137/api/adalterome/gene/curation?gene=PSEN1&selected_limit=20