# AD-Alterome Expert Case Study: Neuroinflammation Hypothesis

## Interpreted Scientific Question

Neuroinflammation Hypothesis的证据池是否能重建TREM2/APOE等炎症相关AD病理线索？

## Evidence Strategy

- Use AD-Alterome full-pool curation first; fall back to capped event samples only when the curation endpoint is unavailable.
- Fetch up to 80 candidate evidence rows, then keep up to 16 expert-included rows for the main narrative.
- Score evidence by AD specificity, mechanism depth, long-tail insight, user-question fit, traceability, and sentence informativeness.
- Apply an AD pathologist-style biological cut: keep molecular/pathological evidence in the main argument and demote generic background evidence.

## Coverage and Balance Check

| Target | Curation scope | Pool rows | Event-unique rows | Matched events | Coverage ratio | Warnings |
| --- | --- | --- | --- | --- | --- | --- |
| Neuroinflammation Hypothesis | offline_full_query_pool_prescreened | 5225 | 5225 | 34060 | 15.34% | - |

- Balance status: `not_applicable`

## AD Pathologist-Style Synthesis

For `Neuroinflammation Hypothesis`, the useful case-study argument is not that the hypothesis is proven, but that AD-Alterome organizes gene and phenotype evidence into amyloid/tau axis, neuroinflammation and microglia axis, synaptic and neuronal dysfunction axis, vascular/metabolic axis.
Long-tail evidence should be protected rather than discarded: CELF2 / structural variation:splice variant, APOE / point mutations:mutations, CLU / point mutations:mutations, MAPT / normalized variants:dna change, TGFBR2 / expression changes:underexpression, GTF3C1 / normalized variants:rsid normalized may provide mechanistic leads that a frequency-only report would under-emphasize.

## Expert-Included Evidence

| Rank | Target | Score | PMID | Gene | Phenotype | Mechanism strata | Expert reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Neuroinflammation Hypothesis | 107.0 | [37799732](https://pubmed.ncbi.nlm.nih.gov/37799732/) | CELF2 | Blood Platelet Disorders | amyloid/tau axis; neuroinflammation and microglia axis; proteostasis/autophagy axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 2 | Neuroinflammation Hypothesis | 105.0 | [37108421](https://pubmed.ncbi.nlm.nih.gov/37108421/) | APOE | lipid binding | neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 3 | Neuroinflammation Hypothesis | 104.0 | [37927337](https://pubmed.ncbi.nlm.nih.gov/37927337/) | CLU | low-density lipoprotein | amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 4 | Neuroinflammation Hypothesis | 103.0 | [36966157](https://pubmed.ncbi.nlm.nih.gov/36966157/) | MAPT | Auditory Diseases, Central | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 5 | Neuroinflammation Hypothesis | 102.0 | [37600517](https://pubmed.ncbi.nlm.nih.gov/37600517/) | TGFBR2 | Neurodegeneration | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 6 | Neuroinflammation Hypothesis | 102.0 | [37305557](https://pubmed.ncbi.nlm.nih.gov/37305557/) | GTF3C1 | Peripheral | amyloid/tau axis; neuroinflammation and microglia axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 7 | Neuroinflammation Hypothesis | 101.0 | [32709045](https://pubmed.ncbi.nlm.nih.gov/32709045/) | TYROBP | Alzheimer&#39;s disease without Neurofibrillary tangles | amyloid/tau axis; neuroinflammation and microglia axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 8 | Neuroinflammation Hypothesis | 101.0 | [37947642](https://pubmed.ncbi.nlm.nih.gov/37947642/) | GBA1 | movement and dementia disorders | amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 9 | Neuroinflammation Hypothesis | 101.0 | [37019383](https://pubmed.ncbi.nlm.nih.gov/37019383/) | APOE | cAMP-dependent protein kinase complex | amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 10 | Neuroinflammation Hypothesis | 101.0 | [36648426](https://pubmed.ncbi.nlm.nih.gov/36648426/) | PPP1R37 | binding | amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 11 | Neuroinflammation Hypothesis | 100.0 | [36829747](https://pubmed.ncbi.nlm.nih.gov/36829747/) | PSEN1 | Attenuated familial adenomatous polyposis | amyloid/tau axis; neuroinflammation and microglia axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 12 | Neuroinflammation Hypothesis | 100.0 | [35173266](https://pubmed.ncbi.nlm.nih.gov/35173266/) | NLRC3 | Neurodegeneration | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 13 | Neuroinflammation Hypothesis | 100.0 | [35273086](https://pubmed.ncbi.nlm.nih.gov/35273086/) | MAPT | sleep | amyloid/tau axis; neuroinflammation and microglia axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 14 | Neuroinflammation Hypothesis | 100.0 | [37081555](https://pubmed.ncbi.nlm.nih.gov/37081555/) | CCR7 | Cerebrovascular Trauma | amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 15 | Neuroinflammation Hypothesis | 100.0 | [36453246](https://pubmed.ncbi.nlm.nih.gov/36453246/) | PDS5B | Neuroinflammation | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 16 | Neuroinflammation Hypothesis | 100.0 | [37192007](https://pubmed.ncbi.nlm.nih.gov/37192007/) | DLG3 | Memory Disorders | amyloid/tau axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |

## Additional High-Scoring Evidence Not Used in the Main Narrative

| Rank | Target | Score | PMID | Gene | Phenotype | Mechanism strata | Expert reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Neuroinflammation Hypothesis | 100.0 | [37735992](https://pubmed.ncbi.nlm.nih.gov/37735992/) | SOX21 | Wnt signaling pathway | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 2 | Neuroinflammation Hypothesis | 100.0 | [34425108](https://pubmed.ncbi.nlm.nih.gov/34425108/) | APOE | T cell activation | neuroinflammation and microglia axis; vascular/metabolic axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 3 | Neuroinflammation Hypothesis | 100.0 | [34468933](https://pubmed.ncbi.nlm.nih.gov/34468933/) | FPR1 | memory | amyloid/tau axis; neuroinflammation and microglia axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 4 | Neuroinflammation Hypothesis | 100.0 | [30249283](https://pubmed.ncbi.nlm.nih.gov/30249283/) | TYROBP | kinase binding | amyloid/tau axis; neuroinflammation and microglia axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 5 | Neuroinflammation Hypothesis | 100.0 | [35443157](https://pubmed.ncbi.nlm.nih.gov/35443157/) | GAD2 | Frequency | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 6 | Neuroinflammation Hypothesis | 99.0 | [32709045](https://pubmed.ncbi.nlm.nih.gov/32709045/) | DNMT1 | Memory Disorders | amyloid/tau axis; neuroinflammation and microglia axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 7 | Neuroinflammation Hypothesis | 98.0 | [35216123](https://pubmed.ncbi.nlm.nih.gov/35216123/) | H3P10 | senescence | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 8 | Neuroinflammation Hypothesis | 98.0 | [35237315](https://pubmed.ncbi.nlm.nih.gov/35237315/) | PSEN1 | double-strand break repair | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 9 | Neuroinflammation Hypothesis | 98.0 | [34764472](https://pubmed.ncbi.nlm.nih.gov/34764472/) | PSEN1 | fibrinogen | neuroinflammation and microglia axis; amyloid/tau axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 10 | Neuroinflammation Hypothesis | 98.0 | [36364766](https://pubmed.ncbi.nlm.nih.gov/36364766/) | H19 | BCL2 expression | amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; vascular/metabolic axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 11 | Neuroinflammation Hypothesis | 98.0 | [35379280](https://pubmed.ncbi.nlm.nih.gov/35379280/) | SAA2 | Inflammation | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 12 | Neuroinflammation Hypothesis | 98.0 | [35167942](https://pubmed.ncbi.nlm.nih.gov/35167942/) | MIR328 | neuron projection development | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |

## Long-Tail Candidates Worth Expert Attention

| Rank | Target | Score | PMID | Gene | Phenotype | Mechanism strata | Expert reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Neuroinflammation Hypothesis | 107.0 | [37799732](https://pubmed.ncbi.nlm.nih.gov/37799732/) | CELF2 | Blood Platelet Disorders | amyloid/tau axis; neuroinflammation and microglia axis; proteostasis/autophagy axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 2 | Neuroinflammation Hypothesis | 105.0 | [37108421](https://pubmed.ncbi.nlm.nih.gov/37108421/) | APOE | lipid binding | neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 3 | Neuroinflammation Hypothesis | 104.0 | [37927337](https://pubmed.ncbi.nlm.nih.gov/37927337/) | CLU | low-density lipoprotein | amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 4 | Neuroinflammation Hypothesis | 103.0 | [36966157](https://pubmed.ncbi.nlm.nih.gov/36966157/) | MAPT | Auditory Diseases, Central | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 5 | Neuroinflammation Hypothesis | 102.0 | [37600517](https://pubmed.ncbi.nlm.nih.gov/37600517/) | TGFBR2 | Neurodegeneration | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 6 | Neuroinflammation Hypothesis | 102.0 | [37305557](https://pubmed.ncbi.nlm.nih.gov/37305557/) | GTF3C1 | Peripheral | amyloid/tau axis; neuroinflammation and microglia axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 7 | Neuroinflammation Hypothesis | 101.0 | [32709045](https://pubmed.ncbi.nlm.nih.gov/32709045/) | TYROBP | Alzheimer&#39;s disease without Neurofibrillary tangles | amyloid/tau axis; neuroinflammation and microglia axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 8 | Neuroinflammation Hypothesis | 101.0 | [37947642](https://pubmed.ncbi.nlm.nih.gov/37947642/) | GBA1 | movement and dementia disorders | amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 9 | Neuroinflammation Hypothesis | 101.0 | [37019383](https://pubmed.ncbi.nlm.nih.gov/37019383/) | APOE | cAMP-dependent protein kinase complex | amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 10 | Neuroinflammation Hypothesis | 101.0 | [36648426](https://pubmed.ncbi.nlm.nih.gov/36648426/) | PPP1R37 | binding | amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 11 | Neuroinflammation Hypothesis | 100.0 | [36829747](https://pubmed.ncbi.nlm.nih.gov/36829747/) | PSEN1 | Attenuated familial adenomatous polyposis | amyloid/tau axis; neuroinflammation and microglia axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 12 | Neuroinflammation Hypothesis | 100.0 | [35173266](https://pubmed.ncbi.nlm.nih.gov/35173266/) | NLRC3 | Neurodegeneration | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 13 | Neuroinflammation Hypothesis | 100.0 | [35273086](https://pubmed.ncbi.nlm.nih.gov/35273086/) | MAPT | sleep | amyloid/tau axis; neuroinflammation and microglia axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 14 | Neuroinflammation Hypothesis | 100.0 | [37081555](https://pubmed.ncbi.nlm.nih.gov/37081555/) | CCR7 | Cerebrovascular Trauma | amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 15 | Neuroinflammation Hypothesis | 100.0 | [36453246](https://pubmed.ncbi.nlm.nih.gov/36453246/) | PDS5B | Neuroinflammation | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 16 | Neuroinflammation Hypothesis | 100.0 | [37192007](https://pubmed.ncbi.nlm.nih.gov/37192007/) | DLG3 | Memory Disorders | amyloid/tau axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |

## Limitations and Common-Sense Boundaries

- This expert layer scores evidence for case-study usefulness; it is not a human gold relevance label.
- Additional high-scoring evidence was not rejected; it was held back to keep the main argument concise and auditable.
- AD-Alterome sentence evidence supports traceable arguments, not final causal proof.
- When coverage warnings are present, use the report to generate hypotheses and prioritize manual review.
- Raw API scoring fields such as EvidenceScore are not used for expert conclusions.

## Audit Appendix: Original Sentence Traces

## Included Evidence Traces

### 1. Neuroinflammation Hypothesis / PMID [37799732](https://pubmed.ncbi.nlm.nih.gov/37799732/)

- Expert score: `107.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `CELF2` / `Blood Platelet Disorders` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; proteostasis/autophagy axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Prior research has demonstrated that the alternative splicing of exon three in TREM2, a genetic risk factor for AD, is regulated by two paralogous RNA-binding proteins, CELF1 and CELF2, with CELF2 being implicated in the reduction of full-length TREM2 protein expression through exon three skipping and nonsense-mediated mRNA decay, which effects on microglial responses to the Abeta aggregation.

### 2. Neuroinflammation Hypothesis / PMID [37108421](https://pubmed.ncbi.nlm.nih.gov/37108421/)

- Expert score: `105.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `lipid binding` / `Neuroinflammation hypothesis,Vascular hypothesis`
- Mechanism strata: neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: These polymorphisms cause differences in the lipid binding properties of the APOE isoforms and receptor affinities; APOE4 is hypolipidated compared to APOE3 and APOE2 (Figure 3).

### 3. Neuroinflammation Hypothesis / PMID [37927337](https://pubmed.ncbi.nlm.nih.gov/37927337/)

- Expert score: `104.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `CLU` / `low-density lipoprotein` / `Neuroinflammation hypothesis,Amyloid hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: These variants affect the stability of TREM2, impair its phagocytic ability, and alter its affinity for APOE4, clusterin (ApoJ), low-density lipoprotein, and Abeta.

### 4. Neuroinflammation Hypothesis / PMID [36966157](https://pubmed.ncbi.nlm.nih.gov/36966157/)

- Expert score: `103.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `Auditory Diseases, Central` / `Tau protein hypothesis,Neuroinflammation hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Reinforcing earlier discussion on hp-tau aggregates and neuronal phagoptosis, APOE knockdown in P301S mice significantly reduced hippocampal and entorhinal cortex loss; APOE preservation increased Iba1 + (suggesting microglia and macrophage populations) cells that were positive with CD68 + phagocytic inclusions.

### 5. Neuroinflammation Hypothesis / PMID [37600517](https://pubmed.ncbi.nlm.nih.gov/37600517/)

- Expert score: `102.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `TGFBR2` / `Neurodegeneration` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: The activation of the PI3K/Akt pathway has been shown to have beneficial effects on neurons and neural stem cells, while dysfunction of the TGF-beta/TbetaRII signaling axis in the AD brain may accelerate Abeta deposition and neurodegeneration.

### 6. Neuroinflammation Hypothesis / PMID [37305557](https://pubmed.ncbi.nlm.nih.gov/37305557/)

- Expert score: `102.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `GTF3C1` / `Peripheral` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: rs12932325 is an eQTL for IL21R (Table S29) that impacts Alzheimer disease pathology by enhancing brain and peripheral immune and inflammatory responses and leads to increased deposition of Abeta plaques.

### 7. Neuroinflammation Hypothesis / PMID [32709045](https://pubmed.ncbi.nlm.nih.gov/32709045/)

- Expert score: `101.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `TYROBP` / `Alzheimer&#39;s disease without Neurofibrillary tangles` / `Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Further, TREM2 or DAP12 haplodeficient AD-like mice or AD patients with R47H mutations exhibited less compact toxic plaques thus leading to severe neuritic tau hyperphosphorylation and increased plaque-associated neuritic dystrophies.

### 8. Neuroinflammation Hypothesis / PMID [37947642](https://pubmed.ncbi.nlm.nih.gov/37947642/)

- Expert score: `101.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `GBA1` / `movement and dementia disorders` / `Amyloid hypothesis,Neuroinflammation hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: The experiments demonstrated glycolipid stress caused by GBA1 inhibition in WT mice induced ApoE expression in several brain regions associated with movement and dementia disorders.

### 9. Neuroinflammation Hypothesis / PMID [37019383](https://pubmed.ncbi.nlm.nih.gov/37019383/)

- Expert score: `101.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `cAMP-dependent protein kinase complex` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: For instance, hVASP interactions with microfilament motor activity proteins Myo1b, Myo1c, and Myo5a were increased following PKA inhibition in apoE4 Neuro-2a cells.

### 10. Neuroinflammation Hypothesis / PMID [36648426](https://pubmed.ncbi.nlm.nih.gov/36648426/)

- Expert score: `101.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `PPP1R37` / `binding` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Harmful AD SNP rs754366 (has a positive PFC eQTL link to APOC2 expression) may increase SPI1 binding to an APOC2 DLPFC enhancer where it activates APOC2 (Supplementary Material, Fig.

### 11. Neuroinflammation Hypothesis / PMID [36829747](https://pubmed.ncbi.nlm.nih.gov/36829747/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `PSEN1` / `Attenuated familial adenomatous polyposis` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: In addition to alleviation of Abeta-induced cognitive impairment, other groups found that MSC-derived exosomes promoted neurogenesis in the subventricular zone and attenuated neuroinflammation in drug (streptozotocin)-induced AD mice, double transgenic (APP/PS1) AD, and triple (APP Swedish, MAPT P301L, and PSEN1 M146V) transgenic AD mouse models.

### 12. Neuroinflammation Hypothesis / PMID [35173266](https://pubmed.ncbi.nlm.nih.gov/35173266/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `NLRC3` / `Neurodegeneration` / `Neuroinflammation Hypothesis,Amyloid Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Considering that wild type NLRC3 is involved in lowering inflammation, and overexpression has been shown to inhibit the deposition of A-beta, and reverse the degeneration of neurons in APP/PS1 mice, we speculate that rare variants in NLRC3 elevate inflammation, resulting in increased neurodegeneration and dementia symptoms.

### 13. Neuroinflammation Hypothesis / PMID [35273086](https://pubmed.ncbi.nlm.nih.gov/35273086/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `sleep` / `Tau protein hypothesis,Neuroinflammation hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: We therefore conducted a comprehensive assessment of the effects of chronic trazodone treatment on microglial activation, the NLRP3 inflammasome, the UPR, EEG sleep, and memory in rTg4510 mice, a model expressing the human P301L tau mutation linked to hereditary frontotemporal dementia.

### 14. Neuroinflammation Hypothesis / PMID [37081555](https://pubmed.ncbi.nlm.nih.gov/37081555/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `CCR7` / `Cerebrovascular Trauma` / `Amyloid Hypothesis,Neuroinflammation Hypothesis,Vascular Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Moreover, CCR7 knockout (which regulates the meningeal lymphatic immune function) leads to increased AD-related pathology (increased Abeta deposition, brain vascular damage, and microglial activation) and worse cognitive profile in a familial animal model of AD.

### 15. Neuroinflammation Hypothesis / PMID [36453246](https://pubmed.ncbi.nlm.nih.gov/36453246/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `PDS5B` / `Neuroinflammation` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Its overexpression enhances the effects of Abeta25-35 on neuronal viability and neuroinflammation, and its knockdown reduces neurotoxicity and neuroinflammation, highlighting the potential role of MAGI2-AS3 in AD progression and treatment.

### 16. Neuroinflammation Hypothesis / PMID [37192007](https://pubmed.ncbi.nlm.nih.gov/37192007/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `DLG3` / `Memory Disorders` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; synaptic and neuronal dysfunction axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Smad4 was identified as a target of miR-431, and Smad4 knockdown modulated the expression of synaptic proteins including SAP102, and protected against synaptic plasticity and memory dysfunctions in APP/PS1 mice.


## Additional High-Scoring Evidence Traces

### 1. Neuroinflammation Hypothesis / PMID [37735992](https://pubmed.ncbi.nlm.nih.gov/37735992/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `SOX21` / `Wnt signaling pathway` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Silencing of SOX21-AS1 could act to alleviate neuronal apoptosis in AD mice through the upregulation of FZD3/5 and subsequent activation of the Wnt signaling pathway.

### 2. Neuroinflammation Hypothesis / PMID [34425108](https://pubmed.ncbi.nlm.nih.gov/34425108/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `T cell activation` / `Neuroinflammation Hypothesis`
- Mechanism strata: neuroinflammation and microglia axis; vascular/metabolic axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: In particular, apoE deficiency or apoE4 expression in myeloid cells, particularly in dendritic cells, has been shown to enhance major histocompatibility complex II-dependent antigen presentation and CD4+ T cell activation, whereas apoE2 impairs lipid antigen presentation via the CD1d-mediated pathway.

### 3. Neuroinflammation Hypothesis / PMID [34468933](https://pubmed.ncbi.nlm.nih.gov/34468933/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `FPR1` / `memory` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: reported that blockade of FPR1 and FPR2 by the antagonist Boc2 in amyloid precursor protein/presenilin 1 (APP/PS1) transgenic mice ameliorates neuropathological deficits with a reduction in Abeta plaques in the hippocampus and an improvement in spatial memory performance.

### 4. Neuroinflammation Hypothesis / PMID [30249283](https://pubmed.ncbi.nlm.nih.gov/30249283/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `TYROBP` / `kinase binding` / `Amyloid hypothesis,Tau protein hypothesis,Neuroinflammation hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Moreover, deletion of progranulin, which has been extensively associated with frontotemporal dementia, results in increased TYRO protein tyrosine kinase binding protein (TYROBP) signaling activation and microglial Abeta phagocytosis in the APP/PS1 mouse model, whereas it increases tau pathology in human P301L tau-expressing mice.

### 5. Neuroinflammation Hypothesis / PMID [35443157](https://pubmed.ncbi.nlm.nih.gov/35443157/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `GAD2` / `Frequency` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: To gauge the relevance of this axis in pathogenic pre-synaptic loss during beta-amyloidosis, we employed an antibody against Stat1 phosphorylated at Tyr701 (pStat1) and detected enhanced frequency of pStat1+ pre-synaptic boutons in 5XFAD brain (Figures S5F and S5G), suggesting a potential functional involvement.

### 6. Neuroinflammation Hypothesis / PMID [32709045](https://pubmed.ncbi.nlm.nih.gov/32709045/)

- Expert score: `99.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `DNMT1` / `Memory Disorders` / `Tau Protein Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: The study also demonstrated that deacetylated DNMT1 is active and can repress IL-1beta expression and that deficiency of SIRT1 leads to aging- or tau-mediated memory deficits in hTau-P301S mice via inhibition of DNMT1 and IL-1beta upregulation.

### 7. Neuroinflammation Hypothesis / PMID [35216123](https://pubmed.ncbi.nlm.nih.gov/35216123/)

- Expert score: `98.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `H3P10` / `senescence` / `Amyloid hypothesis,Neuroinflammation hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: showed that the expression of cell senescence marker p16 is significantly increased in neurons, although not in astrocytes or microglia, in 5XFAD transgenic mice, which overexpress human amyloid beta (A4) precursor protein 695 (APP) with three mutations detected in familial Alzheimer's disease (FAD) and human presenilin 1 (PS1) harboring two FAD mutations.

### 8. Neuroinflammation Hypothesis / PMID [35237315](https://pubmed.ncbi.nlm.nih.gov/35237315/)

- Expert score: `98.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `PSEN1` / `double-strand break repair` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Preferential Involvement of BRCA1/BARD1, Not Tip60/Fe65, in DNA Double-Strand Break Repair in Presenilin-1 P117L Alzheimer Models Recently, we showed that DNA double-strand breaks (DSBs) are increased by the Abeta42-amyloid peptide and decreased by all-trans retinoic acid (RA) in SH-SY5Y cells and C57BL/6J mice.


## Secondary Evidence Traces

No evidence rows available.

## Deprioritized Evidence Summary

| Rank | Target | Score | PMID | Gene | Phenotype | Mechanism strata | Expert reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| - | - | - | - | - | - | - | No evidence rows were deprioritized by the expert screen. |

## Source Payloads

- `Neuroinflammation Hypothesis` overview: http://117.72.176.137/api/adalterome/hypothesis/overview?hypothesis=Neuroinflammation+Hypothesis
- `Neuroinflammation Hypothesis` curation/evidence: http://117.72.176.137/api/adalterome/hypothesis/curation?hypothesis=Neuroinflammation+Hypothesis&selected_limit=80