## 案例一：单基因查询 MAPT

### 自然语言输入

MAPT evidence如何支持tau相关AD病理机制，以及新版curated pool是否能给出比人工筛选更透明的证据包？

### 完整输出

# AD-Alterome Expert Case Study: MAPT

## Interpreted Scientific Question

MAPT evidence如何支持tau相关AD病理机制，以及新版curated pool是否能给出比人工筛选更透明的证据包？

## Evidence Strategy

- Use AD-Alterome full-pool curation first; fall back to capped event samples only when the curation endpoint is unavailable.
- Fetch up to 80 candidate evidence rows, then keep up to 16 expert-included rows for the main narrative.
- Score evidence by AD specificity, mechanism depth, long-tail insight, user-question fit, traceability, and sentence informativeness.
- Apply an AD pathologist-style biological cut: keep molecular/pathological evidence in the main argument and demote generic background evidence.

## Coverage and Balance Check

| Target | Curation scope | Pool rows | Event-unique rows | Matched events | Coverage ratio | Warnings |
| --- | --- | --- | --- | --- | --- | --- |
| MAPT | offline_full_query_pool_prescreened | 2687 | 2687 | 27921 | 9.62% | low_fraction_of_matched_events_in_curation_pool |

- Balance status: `not_applicable`

## AD Pathologist-Style Synthesis

For `MAPT`, the report should argue the scientific question through amyloid/tau axis, synaptic and neuronal dysfunction axis, proteostasis/autophagy axis, neuroinflammation and microglia axis. The highest-value evidence is the original sentence-level molecular and pathological mechanism support; extracted phenotype labels should be treated as audit fields rather than the main biological conclusion.
Long-tail evidence should be protected rather than discarded: MAPT / expression changes:dysregulation, MAPT / expression changes:overexpression, MAPT / normalized variants:dna change, MAPT / genetic manipulation:knockout may provide mechanistic leads that a frequency-only report would under-emphasize.

## Expert-Included Evidence

| Rank | Target | Score | PMID | Gene | Phenotype | Mechanism strata | Expert reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | MAPT | 105.0 | [26696824](https://pubmed.ncbi.nlm.nih.gov/26696824/) | MAPT | Myopathies, Structural, Congenital | amyloid/tau axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 2 | MAPT | 105.0 | [33804962](https://pubmed.ncbi.nlm.nih.gov/33804962/) | MAPT | Skin Diseases, Vesiculobullous | amyloid/tau axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 3 | MAPT | 103.0 | [36966157](https://pubmed.ncbi.nlm.nih.gov/36966157/) | MAPT | Auditory Diseases, Central | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 4 | MAPT | 103.0 | [37337279](https://pubmed.ncbi.nlm.nih.gov/37337279/) | MAPT | Nervous System Diseases | amyloid/tau axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 5 | MAPT | 103.0 | [37452321](https://pubmed.ncbi.nlm.nih.gov/37452321/) | MAPT | import across plasma membrane | proteostasis/autophagy axis; amyloid/tau axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 6 | MAPT | 103.0 | [35794091](https://pubmed.ncbi.nlm.nih.gov/35794091/) | MAPT | peptide secretion | amyloid/tau axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 7 | MAPT | 103.0 | [37759656](https://pubmed.ncbi.nlm.nih.gov/37759656/) | MAPT | vacuole | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 8 | MAPT | 102.0 | [34658846](https://pubmed.ncbi.nlm.nih.gov/34658846/) | MAPT | - | amyloid/tau axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 9 | MAPT | 101.0 | [38010524](https://pubmed.ncbi.nlm.nih.gov/38010524/) | MAPT | translation | amyloid/tau axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 10 | MAPT | 101.0 | [37998336](https://pubmed.ncbi.nlm.nih.gov/37998336/) | MAPT | Affected | amyloid/tau axis; neuroinflammation and microglia axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 11 | MAPT | 101.0 | [37873467](https://pubmed.ncbi.nlm.nih.gov/37873467/) | MAPT | hypersensitivity | amyloid/tau axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 12 | MAPT | 101.0 | [37111315](https://pubmed.ncbi.nlm.nih.gov/37111315/) | MAPT | Gliosis | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 13 | MAPT | 101.0 | [37927337](https://pubmed.ncbi.nlm.nih.gov/37927337/) | MAPT | Bundle-Branch Block | amyloid/tau axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 14 | MAPT | 101.0 | [37445940](https://pubmed.ncbi.nlm.nih.gov/37445940/) | MAPT | Hyperkinesis | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 15 | MAPT | 101.0 | [28612290](https://pubmed.ncbi.nlm.nih.gov/28612290/) | MAPT | neuron projection terminus | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 16 | MAPT | 101.0 | [37335158](https://pubmed.ncbi.nlm.nih.gov/37335158/) | MAPT | mitochondrion dysfunction | amyloid/tau axis; mitochondrial and oxidative stress axis; proteostasis/autophagy axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |

## Additional High-Scoring Evidence Not Used in the Main Narrative

| Rank | Target | Score | PMID | Gene | Phenotype | Mechanism strata | Expert reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | MAPT | 101.0 | [34269204](https://pubmed.ncbi.nlm.nih.gov/34269204/) | MAPT | Hemorrhagic Disorders | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 2 | MAPT | 101.0 | [33852912](https://pubmed.ncbi.nlm.nih.gov/33852912/) | MAPT | Neurobehavioral Manifestations | amyloid/tau axis; mitochondrial and oxidative stress axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 3 | MAPT | 101.0 | [34177463](https://pubmed.ncbi.nlm.nih.gov/34177463/) | MAPT | Neurogenic Inflammation | amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 4 | MAPT | 101.0 | [36361799](https://pubmed.ncbi.nlm.nih.gov/36361799/) | MAPT | extracellular space | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 5 | MAPT | 100.0 | [33418848](https://pubmed.ncbi.nlm.nih.gov/33418848/) | MAPT | immunoglobulin complex, circulating | amyloid/tau axis; synaptic and neuronal dysfunction axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 6 | MAPT | 100.0 | [33494262](https://pubmed.ncbi.nlm.nih.gov/33494262/) | MAPT | Occasional | amyloid/tau axis; proteostasis/autophagy axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 7 | MAPT | 99.0 | [31572381](https://pubmed.ncbi.nlm.nih.gov/31572381/) | MAPT | T cell extravasation | amyloid/tau axis; neuroinflammation and microglia axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 8 | MAPT | 99.0 | [23029602](https://pubmed.ncbi.nlm.nih.gov/23029602/) | MAPT | - | amyloid/tau axis; mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 9 | MAPT | 98.0 | [37452321](https://pubmed.ncbi.nlm.nih.gov/37452321/) | MAPT | motor behavior | amyloid/tau axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 10 | MAPT | 98.0 | [35418705](https://pubmed.ncbi.nlm.nih.gov/35418705/) | MAPT | DNA repair | amyloid/tau axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 11 | MAPT | 98.0 | [36982371](https://pubmed.ncbi.nlm.nih.gov/36982371/) | MAPT | mitophagy | amyloid/tau axis; mitochondrial and oxidative stress axis; proteostasis/autophagy axis | cellular_or_pathway_process evidence; informative original sentence; AD-pathology vocabulary present |
| 12 | MAPT | 98.0 | [17118156](https://pubmed.ncbi.nlm.nih.gov/17118156/) | MAPT | Cyclin D1 expression | amyloid/tau axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |

## Long-Tail Candidates Worth Expert Attention

| Rank | Target | Score | PMID | Gene | Phenotype | Mechanism strata | Expert reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | MAPT | 105.0 | [26696824](https://pubmed.ncbi.nlm.nih.gov/26696824/) | MAPT | Myopathies, Structural, Congenital | amyloid/tau axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 2 | MAPT | 105.0 | [33804962](https://pubmed.ncbi.nlm.nih.gov/33804962/) | MAPT | Skin Diseases, Vesiculobullous | amyloid/tau axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 3 | MAPT | 103.0 | [36966157](https://pubmed.ncbi.nlm.nih.gov/36966157/) | MAPT | Auditory Diseases, Central | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 4 | MAPT | 103.0 | [37337279](https://pubmed.ncbi.nlm.nih.gov/37337279/) | MAPT | Nervous System Diseases | amyloid/tau axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 5 | MAPT | 103.0 | [37452321](https://pubmed.ncbi.nlm.nih.gov/37452321/) | MAPT | import across plasma membrane | proteostasis/autophagy axis; amyloid/tau axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 6 | MAPT | 103.0 | [35794091](https://pubmed.ncbi.nlm.nih.gov/35794091/) | MAPT | peptide secretion | amyloid/tau axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 7 | MAPT | 103.0 | [37759656](https://pubmed.ncbi.nlm.nih.gov/37759656/) | MAPT | vacuole | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 8 | MAPT | 102.0 | [34658846](https://pubmed.ncbi.nlm.nih.gov/34658846/) | MAPT | - | amyloid/tau axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 9 | MAPT | 101.0 | [38010524](https://pubmed.ncbi.nlm.nih.gov/38010524/) | MAPT | translation | amyloid/tau axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 10 | MAPT | 101.0 | [37998336](https://pubmed.ncbi.nlm.nih.gov/37998336/) | MAPT | Affected | amyloid/tau axis; neuroinflammation and microglia axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 11 | MAPT | 101.0 | [37873467](https://pubmed.ncbi.nlm.nih.gov/37873467/) | MAPT | hypersensitivity | amyloid/tau axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 12 | MAPT | 101.0 | [37111315](https://pubmed.ncbi.nlm.nih.gov/37111315/) | MAPT | Gliosis | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 13 | MAPT | 101.0 | [37927337](https://pubmed.ncbi.nlm.nih.gov/37927337/) | MAPT | Bundle-Branch Block | amyloid/tau axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 14 | MAPT | 101.0 | [37445940](https://pubmed.ncbi.nlm.nih.gov/37445940/) | MAPT | Hyperkinesis | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 15 | MAPT | 101.0 | [28612290](https://pubmed.ncbi.nlm.nih.gov/28612290/) | MAPT | neuron projection terminus | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 16 | MAPT | 101.0 | [37335158](https://pubmed.ncbi.nlm.nih.gov/37335158/) | MAPT | mitochondrion dysfunction | amyloid/tau axis; mitochondrial and oxidative stress axis; proteostasis/autophagy axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |

## Limitations and Common-Sense Boundaries

- This expert layer scores evidence for case-study usefulness; it is not a human gold relevance label.
- Additional high-scoring evidence was not rejected; it was held back to keep the main argument concise and auditable.
- AD-Alterome sentence evidence supports traceable arguments, not final causal proof.
- When coverage warnings are present, use the report to generate hypotheses and prioritize manual review.
- Raw API scoring fields such as EvidenceScore are not used for expert conclusions.

## Audit Appendix: Original Sentence Traces

## Included Evidence Traces

### 1. MAPT / PMID [26696824](https://pubmed.ncbi.nlm.nih.gov/26696824/)

- Expert score: `105.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `Myopathies, Structural, Congenital` / `Amyloid hypothesis,Tau protein hypothesis`
- Mechanism strata: amyloid/tau axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Using the Tg2576 mouse model, we found that removal of tau oligomers by immunotherapy shifted the Abeta aggregation pathway to amyloid plaques, while improving cognition in mice.

### 2. MAPT / PMID [33804962](https://pubmed.ncbi.nlm.nih.gov/33804962/)

- Expert score: `105.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `Skin Diseases, Vesiculobullous` / `Tau Protein Hypothesis,Glutamatergic Excitotoxicity Hypothesis`
- Mechanism strata: amyloid/tau axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Of note, axonal transport is disrupted upon tau overexpression, leading to vesicular aggregation, a process reversed by GSK-3 inhibition.

### 3. MAPT / PMID [36966157](https://pubmed.ncbi.nlm.nih.gov/36966157/)

- Expert score: `103.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `Auditory Diseases, Central` / `Tau protein hypothesis,Neuroinflammation hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Reinforcing earlier discussion on hp-tau aggregates and neuronal phagoptosis, APOE knockdown in P301S mice significantly reduced hippocampal and entorhinal cortex loss; APOE preservation increased Iba1 + (suggesting microglia and macrophage populations) cells that were positive with CD68 + phagocytic inclusions.

### 4. MAPT / PMID [37337279](https://pubmed.ncbi.nlm.nih.gov/37337279/)

- Expert score: `103.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `Nervous System Diseases` / `Amyloid Hypothesis,Vascular Hypothesis`
- Mechanism strata: amyloid/tau axis; vascular/metabolic axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Humanized APOE genotypes influence lifespan independently of tau aggregation in the P301S mouse model of tauopathy Apolipoprotein (APOE) E4 isoform is a major risk factor of Alzheimer's disease and contributes to metabolic and neuropathological abnormalities during brain aging.

### 5. MAPT / PMID [37452321](https://pubmed.ncbi.nlm.nih.gov/37452321/)

- Expert score: `103.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `import across plasma membrane` / `Tau Protein Hypothesis,Abnormal Autophagy Hypothesis`
- Mechanism strata: proteostasis/autophagy axis; amyloid/tau axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Overexpression of transcription factor EB (TFEB, a regulator of lysosomal biogenesis) in astrocytes promotes tau fibril species uptake and lysosomal activity as well as attenuates tau spreading and pathology in the hippocampus of P301S tauopathy mice (Fig.

### 6. MAPT / PMID [35794091](https://pubmed.ncbi.nlm.nih.gov/35794091/)

- Expert score: `103.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `peptide secretion` / `Amyloid Hypothesis,Tau Protein Hypothesis`
- Mechanism strata: amyloid/tau axis; synaptic and neuronal dysfunction axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Bmi1 knockout in human post-mitotic neurons induced amyloid-beta peptide secretion and deposition, p-Tau accumulation, and neurodegeneration.

### 7. MAPT / PMID [37759656](https://pubmed.ncbi.nlm.nih.gov/37759656/)

- Expert score: `103.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `vacuole` / `Tau Protein Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: PRMT8 overexpression may result in tau hyperphosphorylation, neuroinflammation and vacuole degeneration in neurons.

### 8. MAPT / PMID [34658846](https://pubmed.ncbi.nlm.nih.gov/34658846/)

- Expert score: `102.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `-` / `Tau Protein Hypothesis,Abnormal Autophagy Hypothesis`
- Mechanism strata: amyloid/tau axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Since acetylation inhibits the binding of Tau to microtubules, enhances Tau accumulation by suppressing Tau degradation, and affects the structure and function of neurons in Tau overexpression models such as C. elegans single-copy transgenic model, the activation of SIRT1 can promote the deacetylation of Tau protein, suggesting that targeting SIRT1 activation can serve as an effective strategy for the prevention and mitigation of AD.

### 9. MAPT / PMID [38010524](https://pubmed.ncbi.nlm.nih.gov/38010524/)

- Expert score: `101.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `translation` / `Amyloid Hypothesis,Tau Protein Hypothesis,Abnormal Autophagy Hypothesis`
- Mechanism strata: amyloid/tau axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: To experimentally challenge the role of protein homeostasis in the accumulation of Alzheimer's associated protein Abeta and levels of associated Tau phosphorylation, we disturbed proteostasis in single APP knock-in mouse models of AD building upon Rps9 D95N, a recently identified mammalian ram mutation which confers heightened levels of error-prone translation together with an increased propensity for random protein aggregation and which is associated with accelerated aging.

### 10. MAPT / PMID [37998336](https://pubmed.ncbi.nlm.nih.gov/37998336/)

- Expert score: `101.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `Affected` / `Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: In line with this, prolonged hyperbaric oxygen treatment can reduce hypoxia, neuroinflammation, the accumulation of Abeta and phosphorylated tau, leading to a significant improvement of cognitive performances in a 3xTg AD mouse model carrying three mutations associated with familial AD (APP Swedish, MAPT P301L, and PSEN1 M146V) when tested in hippocampal-dependent behavioral tasks and, possibly, in affected patients.

### 11. MAPT / PMID [37873467](https://pubmed.ncbi.nlm.nih.gov/37873467/)

- Expert score: `101.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `hypersensitivity` / `Amyloid Hypothesis,Tau Protein Hypothesis,Glutamatergic Excitotoxicity Hypothesis`
- Mechanism strata: amyloid/tau axis; synaptic and neuronal dysfunction axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Interestingly, all three transgenic mutants exhibited a significantly higher level of sensitivity (hypersensitivity) to 5-HT compared to the wild-type, indicating the neurotoxicity caused by Abeta and/or tau expression in neuronal plasticity and function is at least partially mediated by 5-HT (Figure 1C).

### 12. MAPT / PMID [37111315](https://pubmed.ncbi.nlm.nih.gov/37111315/)

- Expert score: `101.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `Gliosis` / `Tau Protein Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: The PS19 mice express the P301S mutant human tau, resulting in hyperphosphorylated tau and NFT-like inclusions with age, microgliosis and astrocytosis, and age-dependent brain atrophy and neuronal loss in the hippocampus, neocortex, and entorhinal cortex in the absence of Abeta pathology.

### 13. MAPT / PMID [37927337](https://pubmed.ncbi.nlm.nih.gov/37927337/)

- Expert score: `101.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `Bundle-Branch Block` / `Tau Protein Hypothesis`
- Mechanism strata: amyloid/tau axis; synaptic and neuronal dysfunction axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: While no changes in MAP 1B expression levels have been found, another study showed that crossing tau mutants with MAP 1B knockout mice exacerbates axonal bundle dysplasia, neuronal layering disorders, and impaired primary neuron maturation observed in MAP 1B knockout mice.

### 14. MAPT / PMID [37445940](https://pubmed.ncbi.nlm.nih.gov/37445940/)

- Expert score: `101.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `Hyperkinesis` / `Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Abnormalities in tau protein, synaptic dysfunction, disturbance in the balance of excitatory and inhibitory neuronal circuits, and the presence of amyloid-beta plaques contribute to enhanced neuronal hyperactivity observed in AD organoids compared to wild type.

### 15. MAPT / PMID [28612290](https://pubmed.ncbi.nlm.nih.gov/28612290/)

- Expert score: `101.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `neuron projection terminus` / `Tau Protein Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: When those AD model mice were also deficient in TYROBP, beneficial effects in gene expression, phosphorylation of tau, nerve terminal integrity, behavior, and electrophysiology were observed.

### 16. MAPT / PMID [37335158](https://pubmed.ncbi.nlm.nih.gov/37335158/)

- Expert score: `101.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `mitochondrion dysfunction` / `Tau protein hypothesis,Mitochondrial autophagy hypothesis`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; proteostasis/autophagy axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Phosphorylated tau at Ser396/404 is highly related to the aging brain and mitochondrion dysfunction.


## Additional High-Scoring Evidence Traces

### 1. MAPT / PMID [34269204](https://pubmed.ncbi.nlm.nih.gov/34269204/)

- Expert score: `101.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `Hemorrhagic Disorders` / `Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Despite the large number of theories that attempt to explain AD-related pathomorphological changes in the brain, evidences coming from in vitro and in vivo AD models have highlighted a cytotoxic effect of amyloid beta (Abeta) fragments and hyperphosphorylated TAU on neurotransmission, axonal transport, signaling cascades and immune response, leading to synaptic loss and dysfunction (Rajmohan and Reddy, 2017).

### 2. MAPT / PMID [33852912](https://pubmed.ncbi.nlm.nih.gov/33852912/)

- Expert score: `101.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `Neurobehavioral Manifestations` / `Tau Protein Hypothesis,Oxidative Stress Hypothesis`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Blocking GAPDH S-nitrosylation, inhibiting p300/CBP, or stimulating Sirtuin1 all protect mice from neurodegeneration, neurobehavioral impairment, and blood and brain accumulation of ac-tau after TBI.

### 3. MAPT / PMID [34177463](https://pubmed.ncbi.nlm.nih.gov/34177463/)

- Expert score: `101.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `Neurogenic Inflammation` / `Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis,Glutamatergic Excitotoxicity Hypothesis,Mitochondrial Autophagy Hypothesis`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: The misfolding and aggregation of amyloid-beta (Abeta) and tau in AD and superoxide dismutase type-1 (SOD1) in ALS results in a progressive loss of specific populations of neurons that is strongly associated with mitochondrial dysfunction, neuroinflammation and excitotoxicity.

### 4. MAPT / PMID [36361799](https://pubmed.ncbi.nlm.nih.gov/36361799/)

- Expert score: `101.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `extracellular space` / `Cholinergic hypothesis,Amyloid hypothesis,Tau protein hypothesis,Neuroinflammation hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: This selective alteration leads to the reduction of cholinergic markers such as acetylcholinesterase Second, amyloidogenic theory, which suggests that an abnormal clearance of amyloid-beta protein induces the accumulation of amyloid beta in the cerebral neurons, leading to a neuronal impairment and to increased neuronal apoptosis; Third, tauogenic theory, which proposes that tau protein aggregation and, consequently, NFT development, directly cause neuronal abnormalities, activating a neuroinflammatory condition in the extracellular space and inducing neuronal apoptosis.

### 5. MAPT / PMID [33418848](https://pubmed.ncbi.nlm.nih.gov/33418848/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `immunoglobulin complex, circulating` / `Tau Protein Hypothesis`
- Mechanism strata: amyloid/tau axis; synaptic and neuronal dysfunction axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: proved that the p53 protein and TauOs (recognized by the T22 antibody) interact in the neurons of AD patients and a mouse model associated with AD (Tg2576/Tau P301L).

### 6. MAPT / PMID [33494262](https://pubmed.ncbi.nlm.nih.gov/33494262/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `Occasional` / `Tau protein hypothesis`
- Mechanism strata: amyloid/tau axis; proteostasis/autophagy axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: One LRRK2 p.G2019S case, which also involved the MAPT variant p.Q124E, was described with occasional TDP-43 inclusions, nigral degeneration without Lewy bodies, and Alzheimer-type tau pathology.

### 7. MAPT / PMID [31572381](https://pubmed.ncbi.nlm.nih.gov/31572381/)

- Expert score: `99.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `T cell extravasation` / `Amyloid hypothesis,Tau protein hypothesis,Neuroinflammation hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Misfolded amyloid and tau can independently lead to T cell extravasation, but what drives this T cell infiltration is unclear as T cells were not reported to be interacting with the plaques or tangles present in transgenic mouse models of AD.

### 8. MAPT / PMID [23029602](https://pubmed.ncbi.nlm.nih.gov/23029602/)

- Expert score: `99.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `-` / `Tau Protein Hypothesis,Mitochondrial Autophagy Hypothesis`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Mitochondrial distribution in the brains of rTg4510 mice was significantly altered in cells containing aggregates of tau at an early age and in neurites regardless of whether aggregates of tau are present.


## Secondary Evidence Traces

No evidence rows available.

## Deprioritized Evidence Summary

| Rank | Target | Score | PMID | Gene | Phenotype | Mechanism strata | Expert reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| - | - | - | - | - | - | - | No evidence rows were deprioritized by the expert screen. |

## Source Payloads

- `MAPT` overview: http://117.72.176.137/api/adalterome/gene/overview?gene=MAPT
- `MAPT` curation/evidence: http://117.72.176.137/api/adalterome/gene/curation?gene=MAPT&selected_limit=80

## 案例二：单表型/病理过程查询 mitochondrial dysfunction

### 自然语言输入

mitochondrial dysfunction作为表型/病理过程时，AD-Alterome如何推荐和解释相关基因及长尾机制证据？

### 完整输出

# AD-Alterome Expert Case Study: mitochondrial dysfunction

## Interpreted Scientific Question

mitochondrial dysfunction作为表型/病理过程时，AD-Alterome如何推荐和解释相关基因及长尾机制证据？

## Evidence Strategy

- Use AD-Alterome full-pool curation first; fall back to capped event samples only when the curation endpoint is unavailable.
- Fetch up to 80 candidate evidence rows, then keep up to 16 expert-included rows for the main narrative.
- Score evidence by AD specificity, mechanism depth, long-tail insight, user-question fit, traceability, and sentence informativeness.
- Apply an AD pathologist-style biological cut: keep molecular/pathological evidence in the main argument and demote generic background evidence.

## Coverage and Balance Check

| Target | Curation scope | Pool rows | Event-unique rows | Matched events | Coverage ratio | Warnings |
| --- | --- | --- | --- | --- | --- | --- |
| mitochondrial dysfunction | offline_full_query_pool_prescreened | 244 | 228 |  | - | - |

- Balance status: `not_applicable`

## AD Pathologist-Style Synthesis

For `mitochondrial dysfunction`, AD-Alterome supports a process-centered case study anchored in genes such as MAPT, HSPD1, NANOS2, ESR1, FRMD6, INSR. The expert screen favors evidence that turns the term from a broad disease label into mechanisms across mitochondrial and oxidative stress axis, proteostasis/autophagy axis, amyloid/tau axis, vascular/metabolic axis.
Long-tail evidence should be protected rather than discarded: NANOS2 / genetic manipulation:knockout, ESR1 / normalized variants:dna change, FRMD6 / genetic manipulation:knockout, MAPT / normalized variants:dna change, INSR / genetic manipulation:knockout may provide mechanistic leads that a frequency-only report would under-emphasize.

## Expert-Included Evidence

| Rank | Target | Score | PMID | Gene | Phenotype | Mechanism strata | Expert reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mitochondrial dysfunction | 102.0 | [35453528](https://pubmed.ncbi.nlm.nih.gov/35453528/) | NANOS2 | Mitochondrial inheritance | mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 2 | mitochondrial dysfunction | 100.0 | [32690944](https://pubmed.ncbi.nlm.nih.gov/32690944/) | ESR1 | Mitochondrial Diseases | amyloid/tau axis; mitochondrial and oxidative stress axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 3 | mitochondrial dysfunction | 100.0 | [36231104](https://pubmed.ncbi.nlm.nih.gov/36231104/) | FRMD6 | Mitochondrial Diseases | mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 4 | mitochondrial dysfunction | 100.0 | [33679375](https://pubmed.ncbi.nlm.nih.gov/33679375/) | MAPT | - | amyloid/tau axis; mitochondrial and oxidative stress axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 5 | mitochondrial dysfunction | 98.0 | [36639689](https://pubmed.ncbi.nlm.nih.gov/36639689/) | MAPT | Mitochondrial Diseases | amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 6 | mitochondrial dysfunction | 98.0 | [37186836](https://pubmed.ncbi.nlm.nih.gov/37186836/) | INSR | Abnormality of mitochondrial metabolism | mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 7 | mitochondrial dysfunction | 98.0 | [38056504](https://pubmed.ncbi.nlm.nih.gov/38056504/) | LDLR | Mitochondrial Diseases | mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 8 | mitochondrial dysfunction | 98.0 | [33676568](https://pubmed.ncbi.nlm.nih.gov/33676568/) | HSPA9 | Mitochondrial inheritance | mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 9 | mitochondrial dysfunction | 98.0 | [33845179](https://pubmed.ncbi.nlm.nih.gov/33845179/) | HSPD1 | Mitochondrial inheritance | mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 10 | mitochondrial dysfunction | 96.0 | [36835494](https://pubmed.ncbi.nlm.nih.gov/36835494/) | TOMM40 | Mitochondrial Diseases | mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 11 | mitochondrial dysfunction | 96.0 | [22753410](https://pubmed.ncbi.nlm.nih.gov/22753410/) | HSPD1 | Mitochondrial Diseases | amyloid/tau axis; mitochondrial and oxidative stress axis; proteostasis/autophagy axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 12 | mitochondrial dysfunction | 96.0 | [39084875](https://pubmed.ncbi.nlm.nih.gov/39084875/) | NPCA1 | Abnormality of mitochondrial metabolism | mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 13 | mitochondrial dysfunction | 94.0 | [36927428](https://pubmed.ncbi.nlm.nih.gov/36927428/) | ASS1 | Mitochondrial inheritance | amyloid/tau axis; mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 14 | mitochondrial dysfunction | 93.0 | [35252966](https://pubmed.ncbi.nlm.nih.gov/35252966/) | NEIL1 | Mitochondrial inheritance | mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 15 | mitochondrial dysfunction | 93.0 | [33062068](https://pubmed.ncbi.nlm.nih.gov/33062068/) | CCL5 | Mitochondrial Diseases | mitochondrial and oxidative stress axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 16 | mitochondrial dysfunction | 92.0 | [27099072](https://pubmed.ncbi.nlm.nih.gov/27099072/) | DNM1L | - | amyloid/tau axis; mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |

## Additional High-Scoring Evidence Not Used in the Main Narrative

| Rank | Target | Score | PMID | Gene | Phenotype | Mechanism strata | Expert reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mitochondrial dysfunction | 91.0 | [26441662](https://pubmed.ncbi.nlm.nih.gov/26441662/) | TIMM23 | Mitochondrial inheritance | amyloid/tau axis; mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | cellular_or_pathway_process evidence; informative original sentence; AD-pathology vocabulary present |
| 2 | mitochondrial dysfunction | 91.0 | [37863658](https://pubmed.ncbi.nlm.nih.gov/37863658/) | MED12 | mitochondrial dysfunctions | mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | cellular_or_pathway_process evidence; informative original sentence; AD-pathology vocabulary present |
| 3 | mitochondrial dysfunction | 90.0 | [36727091](https://pubmed.ncbi.nlm.nih.gov/36727091/) | FXN | Abnormality of mitochondrial metabolism | mitochondrial and oxidative stress axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 4 | mitochondrial dysfunction | 90.0 | [33810506](https://pubmed.ncbi.nlm.nih.gov/33810506/) | MFN1 | Mitochondrial inheritance | mitochondrial and oxidative stress axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 5 | mitochondrial dysfunction | 90.0 | [37181110](https://pubmed.ncbi.nlm.nih.gov/37181110/) | WFS1 | Mitochondrial Diseases | mitochondrial and oxidative stress axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |

## Long-Tail Candidates Worth Expert Attention

| Rank | Target | Score | PMID | Gene | Phenotype | Mechanism strata | Expert reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mitochondrial dysfunction | 102.0 | [35453528](https://pubmed.ncbi.nlm.nih.gov/35453528/) | NANOS2 | Mitochondrial inheritance | mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 2 | mitochondrial dysfunction | 100.0 | [32690944](https://pubmed.ncbi.nlm.nih.gov/32690944/) | ESR1 | Mitochondrial Diseases | amyloid/tau axis; mitochondrial and oxidative stress axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 3 | mitochondrial dysfunction | 100.0 | [36231104](https://pubmed.ncbi.nlm.nih.gov/36231104/) | FRMD6 | Mitochondrial Diseases | mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 4 | mitochondrial dysfunction | 100.0 | [33679375](https://pubmed.ncbi.nlm.nih.gov/33679375/) | MAPT | - | amyloid/tau axis; mitochondrial and oxidative stress axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 5 | mitochondrial dysfunction | 98.0 | [36639689](https://pubmed.ncbi.nlm.nih.gov/36639689/) | MAPT | Mitochondrial Diseases | amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 6 | mitochondrial dysfunction | 98.0 | [37186836](https://pubmed.ncbi.nlm.nih.gov/37186836/) | INSR | Abnormality of mitochondrial metabolism | mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 7 | mitochondrial dysfunction | 98.0 | [38056504](https://pubmed.ncbi.nlm.nih.gov/38056504/) | LDLR | Mitochondrial Diseases | mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 8 | mitochondrial dysfunction | 98.0 | [33676568](https://pubmed.ncbi.nlm.nih.gov/33676568/) | HSPA9 | Mitochondrial inheritance | mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 9 | mitochondrial dysfunction | 98.0 | [33845179](https://pubmed.ncbi.nlm.nih.gov/33845179/) | HSPD1 | Mitochondrial inheritance | mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 10 | mitochondrial dysfunction | 96.0 | [36835494](https://pubmed.ncbi.nlm.nih.gov/36835494/) | TOMM40 | Mitochondrial Diseases | mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 11 | mitochondrial dysfunction | 96.0 | [22753410](https://pubmed.ncbi.nlm.nih.gov/22753410/) | HSPD1 | Mitochondrial Diseases | amyloid/tau axis; mitochondrial and oxidative stress axis; proteostasis/autophagy axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 12 | mitochondrial dysfunction | 96.0 | [39084875](https://pubmed.ncbi.nlm.nih.gov/39084875/) | NPCA1 | Abnormality of mitochondrial metabolism | mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 13 | mitochondrial dysfunction | 94.0 | [36927428](https://pubmed.ncbi.nlm.nih.gov/36927428/) | ASS1 | Mitochondrial inheritance | amyloid/tau axis; mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 14 | mitochondrial dysfunction | 93.0 | [35252966](https://pubmed.ncbi.nlm.nih.gov/35252966/) | NEIL1 | Mitochondrial inheritance | mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 15 | mitochondrial dysfunction | 93.0 | [33062068](https://pubmed.ncbi.nlm.nih.gov/33062068/) | CCL5 | Mitochondrial Diseases | mitochondrial and oxidative stress axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 16 | mitochondrial dysfunction | 92.0 | [27099072](https://pubmed.ncbi.nlm.nih.gov/27099072/) | DNM1L | - | amyloid/tau axis; mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |

## Limitations and Common-Sense Boundaries

- This expert layer scores evidence for case-study usefulness; it is not a human gold relevance label.
- Additional high-scoring evidence was not rejected; it was held back to keep the main argument concise and auditable.
- AD-Alterome sentence evidence supports traceable arguments, not final causal proof.
- When coverage warnings are present, use the report to generate hypotheses and prioritize manual review.
- Raw API scoring fields such as EvidenceScore are not used for expert conclusions.

## Audit Appendix: Original Sentence Traces

## Included Evidence Traces

### 1. mitochondrial dysfunction / PMID [35453528](https://pubmed.ncbi.nlm.nih.gov/35453528/)

- Expert score: `102.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `NANOS2` / `Mitochondrial inheritance` / `Neuroinflammation Hypothesis,Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis`
- Mechanism strata: mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: The knockdown of CISD2 enhanced the secretion of inflammatory mediators (NOS2 and the chemokine regulated on activation, normal T cell expressed and secreted) and led to mitochondrial dysfunction, including decreased mitochondrial membrane potential (Deltapsim), enhanced ROS release, and ultimate cellular apoptosis in SH-SY5Y cells.

### 2. mitochondrial dysfunction / PMID [32690944](https://pubmed.ncbi.nlm.nih.gov/32690944/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `ESR1` / `Mitochondrial Diseases` / `Amyloid Hypothesis,Mitochondrial Autophagy Hypothesis`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Previous results show that overexpression of wild-type (APPWT) or Swedish APP (APPSW) double mutant (K595N/M596L) induces mitochondrial dysfunction in SHSY5Y cells through the production of toxic APP cleavage products that localize to mitochondria and mitochondria-associated ER membranes (MAMs).

### 3. mitochondrial dysfunction / PMID [36231104](https://pubmed.ncbi.nlm.nih.gov/36231104/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `FRMD6` / `Mitochondrial Diseases` / `Oxidative stress hypothesis,Mitochondrial autophagy hypothesis`
- Mechanism strata: mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Furthermore, we demonstrate that Willin/FRMD6 knockdown leads to mitochondrial dysfunction and fragmentation, as well as upregulation of ERK1/2 signaling, both of which are reported to be key early features of AD pathogenesis.

### 4. mitochondrial dysfunction / PMID [33679375](https://pubmed.ncbi.nlm.nih.gov/33679375/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `-` / `Tau Protein Hypothesis,Mitochondrial Autophagy Hypothesis`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Mitochondrial dysfunction is detected in P301L tau transgenic mice.

### 5. mitochondrial dysfunction / PMID [36639689](https://pubmed.ncbi.nlm.nih.gov/36639689/)

- Expert score: `98.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MAPT` / `Mitochondrial Diseases` / `Tau Protein Hypothesis,Neuroinflammation Hypothesis,Mitochondrial Autophagy Hypothesis`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: For example, Tg4510-P301L and 3xTg mice exhibit altered inflammatory responses, blood vessel abnormalities and mitochondrial dysfunctions caused by aggregates of hyperphosphorylated tau.

### 6. mitochondrial dysfunction / PMID [37186836](https://pubmed.ncbi.nlm.nih.gov/37186836/)

- Expert score: `98.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `INSR` / `Abnormality of mitochondrial metabolism` / `Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis`
- Mechanism strata: mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Brain-wide knockout of insulin receptor in mice (NIRKO) leads to mitochondrial dysfunction characterized by a decrease in mitochondrial mass and size and increased levels of reactive oxygen species (ROS) in the brain.

### 7. mitochondrial dysfunction / PMID [38056504](https://pubmed.ncbi.nlm.nih.gov/38056504/)

- Expert score: `98.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `LDLR` / `Mitochondrial Diseases` / `Neuroinflammation hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis,Vascular hypothesis`
- Mechanism strata: mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Cognitive and emotional behavioral impairments in LDL receptor knockout (LDLr-/-) mice are associated with neuroinflammation, blood-brain barrier dysfunction, impaired neurogenesis, brain oxidative stress, and mitochondrial dysfunction.

### 8. mitochondrial dysfunction / PMID [33676568](https://pubmed.ncbi.nlm.nih.gov/33676568/)

- Expert score: `98.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `HSPA9` / `Mitochondrial inheritance` / `Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis`
- Mechanism strata: mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Furthermore, apoE4 (Delta272-299) expression promoted GRP75 expression, mitochondrial dysfunction and calcium transport into the mitochondria in neuron, which were significantly mitigated by treatment with PBA (an inhibitor of ER stress), MKT077 (a specific GRP75 inhibitor) or GRP75 silencing.

### 9. mitochondrial dysfunction / PMID [33845179](https://pubmed.ncbi.nlm.nih.gov/33845179/)

- Expert score: `98.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `HSPD1` / `Mitochondrial inheritance` / `Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis`
- Mechanism strata: mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Further, disrupting mitochondrial homeostasis in the hypothalamus through knockdown of the mitochondrial chaperone Hsp60 is sufficient to induce insulin resistance, mitochondrial dysfunction, and ROS production.

### 10. mitochondrial dysfunction / PMID [36835494](https://pubmed.ncbi.nlm.nih.gov/36835494/)

- Expert score: `96.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `TOMM40` / `Mitochondrial Diseases` / `Neuroinflammation Hypothesis,Mitochondrial Autophagy Hypothesis`
- Mechanism strata: mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: We further utilized cell models to examine the role of TOMM40 variation in mitochondrial dysfunction that causes microglial activation and neuroinflammation.

### 11. mitochondrial dysfunction / PMID [22753410](https://pubmed.ncbi.nlm.nih.gov/22753410/)

- Expert score: `96.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `HSPD1` / `Mitochondrial Diseases` / `Amyloid hypothesis,Mitochondrial autophagy hypothesis`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; proteostasis/autophagy axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Swedish Alzheimer mutation induces mitochondrial dysfunction mediated by HSP60 mislocalization of amyloid precursor protein (APP) and beta-amyloid.

### 12. mitochondrial dysfunction / PMID [39084875](https://pubmed.ncbi.nlm.nih.gov/39084875/)

- Expert score: `96.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `NPCA1` / `Abnormality of mitochondrial metabolism` / `Mitochondrial Autophagy Hypothesis`
- Mechanism strata: mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: For example, depletion of NPC1 in HEK293T- and iPSC-derived neurons results in abnormal cholesterol accumulation within lysosomes, leading to hyperactivation of mTORC1 kinase and mitochondrial dysfunction.

### 13. mitochondrial dysfunction / PMID [36927428](https://pubmed.ncbi.nlm.nih.gov/36927428/)

- Expert score: `94.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `ASS1` / `Mitochondrial inheritance` / `Amyloid hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Recent research in cellular, biochemical and animal models have shown that AD mutants affecting the presenilins, Ass, APP, and ApoE4 are associated with mitochondria and cause mitochondrial dysfunction and oxidative damage in AD (Fig.

### 14. mitochondrial dysfunction / PMID [35252966](https://pubmed.ncbi.nlm.nih.gov/35252966/)

- Expert score: `93.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `NEIL1` / `Mitochondrial inheritance` / `Oxidative stress hypothesis,Mitochondrial autophagy hypothesis`
- Mechanism strata: mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Knockout of mitochondrial OGG1 and NEIL1, which remove 8-oxo-dG and formamidopyrimidine lesions, respectively, in mice results in mitochondrial dysfunction and a metabolic syndrome phenotype.

### 15. mitochondrial dysfunction / PMID [33062068](https://pubmed.ncbi.nlm.nih.gov/33062068/)

- Expert score: `93.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `CCL5` / `Mitochondrial Diseases` / `Oxidative stress hypothesis,Mitochondrial autophagy hypothesis`
- Mechanism strata: mitochondrial and oxidative stress axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: CISD2 deficiency enhances the expression of iNOS and RANTES, which contributes to mitochondrial dysfunctions, such as low DeltaPsi(m) levels, high ROS levels, and augmented apoptosis, which are mitigated upon curcumin treatment.

### 16. mitochondrial dysfunction / PMID [27099072](https://pubmed.ncbi.nlm.nih.gov/27099072/)

- Expert score: `92.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `DNM1L` / `-` / `Mitochondrial autophagy hypothesis`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Mitochondrial dysfunction is also detected in P301L tau transgenic mice.


## Additional High-Scoring Evidence Traces

### 1. mitochondrial dysfunction / PMID [26441662](https://pubmed.ncbi.nlm.nih.gov/26441662/)

- Expert score: `91.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `TIMM23` / `Mitochondrial inheritance` / `Amyloid Hypothesis,Mitochondrial Autophagy Hypothesis`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis
- Reasons: cellular_or_pathway_process evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Due to the accumulation of Abeta peptides in the mitochondrial import channels (TIM23 and TOM40) and mutant APP in AD brain causes mitochondrial dysfunction.

### 2. mitochondrial dysfunction / PMID [37863658](https://pubmed.ncbi.nlm.nih.gov/37863658/)

- Expert score: `91.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MED12` / `mitochondrial dysfunctions` / `Oxidative stress hypothesis,Mitochondrial autophagy hypothesis`
- Mechanism strata: mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis
- Reasons: cellular_or_pathway_process evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: In brain extracts, OPA1 haploinsufficiency is known to be associated to mitochondrial dysfunctions that build up with age, starting at 10 months of age mainly as a pro-oxidative stress, sensitizing neurons to further challenges or insults.

### 3. mitochondrial dysfunction / PMID [36727091](https://pubmed.ncbi.nlm.nih.gov/36727091/)

- Expert score: `90.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `FXN` / `Abnormality of mitochondrial metabolism` / `Mitochondrial Autophagy Hypothesis`
- Mechanism strata: mitochondrial and oxidative stress axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: The authors observed that the silencing of FXN gene caused mitochondrial dysfunction leading to cellular senescence and an increase in autophagy.

### 4. mitochondrial dysfunction / PMID [33810506](https://pubmed.ncbi.nlm.nih.gov/33810506/)

- Expert score: `90.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `MFN1` / `Mitochondrial inheritance` / `Mitochondrial autophagy hypothesis`
- Mechanism strata: mitochondrial and oxidative stress axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: The importance of mitochondrial dynamics is highlighted by the fact that mouse knockout models of essential genes that are required for fusion (MFN1, MFN2 and OPA1) or fission (DNM1L) result in mitochondrial dysfunction and embryonic lethality.

### 5. mitochondrial dysfunction / PMID [37181110](https://pubmed.ncbi.nlm.nih.gov/37181110/)

- Expert score: `90.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `WFS1` / `Mitochondrial Diseases` / `Mitochondrial autophagy hypothesis`
- Mechanism strata: mitochondrial and oxidative stress axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Silencing of the WFS1 gene in HEK cells with small interfering RNA (siRNA) upregulated genes related to mitochondrial dysfunction and degeneration, suggesting that loss of wolframin precipitates degeneration via mitochondrial dysfunction.


## Secondary Evidence Traces

No evidence rows available.

## Deprioritized Evidence Summary

| Rank | Target | Score | PMID | Gene | Phenotype | Mechanism strata | Expert reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| - | - | - | - | - | - | - | No evidence rows were deprioritized by the expert screen. |

## Source Payloads

- `mitochondrial dysfunction` overview: http://117.72.176.137/api/adalterome/term/overview?term=mitochondrial+dysfunction
- `mitochondrial dysfunction` curation/evidence: http://117.72.176.137/api/adalterome/term/curation?term=mitochondrial+dysfunction&selected_limit=80

## 案例三：假说查询 Neuroinflammation Hypothesis

### 自然语言输入

Neuroinflammation Hypothesis的证据池是否能重建TREM2/APOE等炎症相关AD病理线索？

### 完整输出

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

## 案例四：基因比较 APOE vs APP

### 自然语言输入

APOE和APP在AD病理机制中有哪些共享和特异的遗传改变-表型-假说模式？

### 完整输出

# AD-Alterome Expert Case Study: APOE vs APP

## Interpreted Scientific Question

APOE和APP在AD病理机制中有哪些共享和特异的遗传改变-表型-假说模式？

## Evidence Strategy

- Use AD-Alterome full-pool curation first; fall back to capped event samples only when the curation endpoint is unavailable.
- Fetch up to 80 candidate evidence rows, then keep up to 18 expert-included rows for the main narrative.
- Score evidence by AD specificity, mechanism depth, long-tail insight, user-question fit, traceability, and sentence informativeness.
- Apply an AD pathologist-style biological cut: keep molecular/pathological evidence in the main argument and demote generic background evidence.
- Enforce target balance before writing contrastive claims; imbalanced coverage downgrades the report to exploratory comparison.

## Coverage and Balance Check

| Target | Curation scope | Pool rows | Event-unique rows | Matched events | Coverage ratio | Warnings |
| --- | --- | --- | --- | --- | --- | --- |
| APOE | offline_full_query_pool_prescreened | 1839 | 1839 | 13322 | 13.80% | - |
| APP | offline_full_query_pool_prescreened | 2300 | 2300 | 18639 | 12.34% | - |

- Balance status: `balanced`
- Targets have comparable curation scope for case-study synthesis.

## AD Pathologist-Style Synthesis

For the question `APOE和APP在AD病理机制中有哪些共享和特异的遗传改变-表型-假说模式？`, the strongest AD-Alterome case-study frame is a coverage-aware contrast across APP, APOE. The visible high-insight evidence clusters around amyloid/tau axis, synaptic and neuronal dysfunction axis, vascular/metabolic axis, proteostasis/autophagy axis.
- `APP`: prioritize amyloid/tau axis, synaptic and neuronal dysfunction axis, proteostasis/autophagy axis and verify extracted phenotype labels against the original sentences before writing fine-grained biological claims.
- `APOE`: prioritize vascular/metabolic axis, amyloid/tau axis, neuroinflammation and microglia axis and verify extracted phenotype labels against the original sentences before writing fine-grained biological claims.
Long-tail evidence should be protected rather than discarded: APP / normalized variants:dna change, APP / normalized variants:protein change, APP / expression changes:inactivation, APP / expression changes:underexpression may provide mechanistic leads that a frequency-only report would under-emphasize.

## Expert-Included Evidence

| Rank | Target | Score | PMID | Gene | Phenotype | Mechanism strata | Expert reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | APP | 102.0 | [36170028](https://pubmed.ncbi.nlm.nih.gov/36170028/) | APP | chemical synaptic transmission | amyloid/tau axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 2 | APP | 102.0 | [35457077](https://pubmed.ncbi.nlm.nih.gov/35457077/) | APP | Glioma | amyloid/tau axis; neuroinflammation and microglia axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 3 | APP | 102.0 | [32486013](https://pubmed.ncbi.nlm.nih.gov/32486013/) | APP | positive regulation of mitochondrial membrane permeability | amyloid/tau axis; mitochondrial and oxidative stress axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 4 | APP | 102.0 | [31209071](https://pubmed.ncbi.nlm.nih.gov/31209071/) | APP | Complement Component 3 Deficiency, Autosomal Recessive | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 5 | APP | 100.0 | [37887303](https://pubmed.ncbi.nlm.nih.gov/37887303/) | APP | Hemorrhage | amyloid/tau axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 6 | APP | 100.0 | [36430913](https://pubmed.ncbi.nlm.nih.gov/36430913/) | APP | - | amyloid/tau axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 7 | APP | 100.0 | [29238218](https://pubmed.ncbi.nlm.nih.gov/29238218/) | APP | cholesterol esterification | amyloid/tau axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 8 | APP | 100.0 | [37642583](https://pubmed.ncbi.nlm.nih.gov/37642583/) | amyloid beta precursor protein | - | amyloid/tau axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 9 | APP | 98.0 | [37873467](https://pubmed.ncbi.nlm.nih.gov/37873467/) | APP | hypersensitivity | amyloid/tau axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 10 | APOE | 102.0 | [37108421](https://pubmed.ncbi.nlm.nih.gov/37108421/) | APOE | lipid binding | neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 11 | APOE | 102.0 | [23867607](https://pubmed.ncbi.nlm.nih.gov/23867607/) | APOE | Neurotoxicity Syndromes | amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis; proteostasis/autophagy axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 12 | APOE | 102.0 | [21283692](https://pubmed.ncbi.nlm.nih.gov/21283692/) | APOE | regulation of DNA-templated transcription | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 13 | APOE | 101.0 | [37887303](https://pubmed.ncbi.nlm.nih.gov/37887303/) | APOE | Vascular System Injuries | amyloid/tau axis; mitochondrial and oxidative stress axis; vascular/metabolic axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 14 | APOE | 100.0 | [37455931](https://pubmed.ncbi.nlm.nih.gov/37455931/) | APOE | lysosome | amyloid/tau axis; mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 15 | APOE | 100.0 | [36646419](https://pubmed.ncbi.nlm.nih.gov/36646419/) | APOE | inflammatory | amyloid/tau axis; neuroinflammation and microglia axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 16 | APOE | 100.0 | [34876200](https://pubmed.ncbi.nlm.nih.gov/34876200/) | APOE | collagen | amyloid/tau axis; vascular/metabolic axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 17 | APOE | 100.0 | [35298921](https://pubmed.ncbi.nlm.nih.gov/35298921/) | APOE | metabolic process | amyloid/tau axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis; proteostasis/autophagy axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 18 | APOE | 100.0 | [35847516](https://pubmed.ncbi.nlm.nih.gov/35847516/) | APOE | early endosome | amyloid/tau axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |

## Additional High-Scoring Evidence Not Used in the Main Narrative

| Rank | Target | Score | PMID | Gene | Phenotype | Mechanism strata | Expert reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | APOE | 100.0 | [32417770](https://pubmed.ncbi.nlm.nih.gov/32417770/) | APOE | Cerebral hemorrhage | amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis; proteostasis/autophagy axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 2 | APOE | 99.0 | [27025652](https://pubmed.ncbi.nlm.nih.gov/27025652/) | APOE | - | amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 3 | APP | 98.0 | [35216123](https://pubmed.ncbi.nlm.nih.gov/35216123/) | APP | senescence | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 4 | APOE | 98.0 | [37019383](https://pubmed.ncbi.nlm.nih.gov/37019383/) | APOE | cAMP-dependent protein kinase complex | amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 5 | APOE | 98.0 | [24644280](https://pubmed.ncbi.nlm.nih.gov/24644280/) | APOE | reactive oxygen species biosynthetic process | amyloid/tau axis; mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 6 | APOE | 98.0 | [38203341](https://pubmed.ncbi.nlm.nih.gov/38203341/) | APOE | brain microstructure damage | amyloid/tau axis; mitochondrial and oxidative stress axis; vascular/metabolic axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 7 | APOE | 98.0 | [36597122](https://pubmed.ncbi.nlm.nih.gov/36597122/) | APOE | Blood Platelet Disorders | amyloid/tau axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 8 | APOE | 98.0 | [37927337](https://pubmed.ncbi.nlm.nih.gov/37927337/) | APOE | low-density lipoprotein | amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 9 | APP | 98.0 | [21978883](https://pubmed.ncbi.nlm.nih.gov/21978883/) | APP | mitochondrial depolarization | amyloid/tau axis; mitochondrial and oxidative stress axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 10 | APOE | 98.0 | [36966157](https://pubmed.ncbi.nlm.nih.gov/36966157/) | APOE | Auditory Diseases, Central | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 11 | APOE | 98.0 | [37708025](https://pubmed.ncbi.nlm.nih.gov/37708025/) | APOE | lipid homeostasis | amyloid/tau axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 12 | APOE | 98.0 | [33676568](https://pubmed.ncbi.nlm.nih.gov/33676568/) | APOE | calcium ion transport | mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |

## Long-Tail Candidates Worth Expert Attention

| Rank | Target | Score | PMID | Gene | Phenotype | Mechanism strata | Expert reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | APP | 102.0 | [36170028](https://pubmed.ncbi.nlm.nih.gov/36170028/) | APP | chemical synaptic transmission | amyloid/tau axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 2 | APP | 102.0 | [35457077](https://pubmed.ncbi.nlm.nih.gov/35457077/) | APP | Glioma | amyloid/tau axis; neuroinflammation and microglia axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 3 | APP | 102.0 | [32486013](https://pubmed.ncbi.nlm.nih.gov/32486013/) | APP | positive regulation of mitochondrial membrane permeability | amyloid/tau axis; mitochondrial and oxidative stress axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 4 | APP | 102.0 | [31209071](https://pubmed.ncbi.nlm.nih.gov/31209071/) | APP | Complement Component 3 Deficiency, Autosomal Recessive | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 5 | APP | 100.0 | [37887303](https://pubmed.ncbi.nlm.nih.gov/37887303/) | APP | Hemorrhage | amyloid/tau axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 6 | APP | 100.0 | [36430913](https://pubmed.ncbi.nlm.nih.gov/36430913/) | APP | - | amyloid/tau axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 7 | APP | 100.0 | [29238218](https://pubmed.ncbi.nlm.nih.gov/29238218/) | APP | cholesterol esterification | amyloid/tau axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 8 | APP | 100.0 | [37642583](https://pubmed.ncbi.nlm.nih.gov/37642583/) | amyloid beta precursor protein | - | amyloid/tau axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 9 | APP | 98.0 | [37873467](https://pubmed.ncbi.nlm.nih.gov/37873467/) | APP | hypersensitivity | amyloid/tau axis; synaptic and neuronal dysfunction axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 10 | APOE | 102.0 | [37108421](https://pubmed.ncbi.nlm.nih.gov/37108421/) | APOE | lipid binding | neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 11 | APOE | 102.0 | [23867607](https://pubmed.ncbi.nlm.nih.gov/23867607/) | APOE | Neurotoxicity Syndromes | amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis; proteostasis/autophagy axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 12 | APOE | 102.0 | [21283692](https://pubmed.ncbi.nlm.nih.gov/21283692/) | APOE | regulation of DNA-templated transcription | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 13 | APOE | 101.0 | [37887303](https://pubmed.ncbi.nlm.nih.gov/37887303/) | APOE | Vascular System Injuries | amyloid/tau axis; mitochondrial and oxidative stress axis; vascular/metabolic axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 14 | APOE | 100.0 | [37455931](https://pubmed.ncbi.nlm.nih.gov/37455931/) | APOE | lysosome | amyloid/tau axis; mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 15 | APOE | 100.0 | [36646419](https://pubmed.ncbi.nlm.nih.gov/36646419/) | APOE | inflammatory | amyloid/tau axis; neuroinflammation and microglia axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 16 | APOE | 100.0 | [34876200](https://pubmed.ncbi.nlm.nih.gov/34876200/) | APOE | collagen | amyloid/tau axis; vascular/metabolic axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |
| 17 | APOE | 100.0 | [35298921](https://pubmed.ncbi.nlm.nih.gov/35298921/) | APOE | metabolic process | amyloid/tau axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis; proteostasis/autophagy axis | molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present |
| 18 | APOE | 100.0 | [35847516](https://pubmed.ncbi.nlm.nih.gov/35847516/) | APOE | early endosome | amyloid/tau axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present |

## Limitations and Common-Sense Boundaries

- This expert layer scores evidence for case-study usefulness; it is not a human gold relevance label.
- Additional high-scoring evidence was not rejected; it was held back to keep the main argument concise and auditable.
- AD-Alterome sentence evidence supports traceable arguments, not final causal proof.
- When coverage warnings are present, use the report to generate hypotheses and prioritize manual review.
- Raw API scoring fields such as EvidenceScore are not used for expert conclusions.

## Audit Appendix: Original Sentence Traces

## Included Evidence Traces

### 1. APP / PMID [36170028](https://pubmed.ncbi.nlm.nih.gov/36170028/)

- Expert score: `102.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APP` / `chemical synaptic transmission` / `Cholinergic hypothesis,Amyloid hypothesis`
- Mechanism strata: amyloid/tau axis; synaptic and neuronal dysfunction axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: In addition to targeting TRKB, neurotrophic receptor tyrosine kinase 1 (TRKA) agonist D3 have been shown to provide beneficial effects to activate TRKA-related signaling cascades and enhance cholinergic neurotransmission in transgenic mice overexpressing human APP with KM670/671NL and V717F mutations.

### 2. APP / PMID [35457077](https://pubmed.ncbi.nlm.nih.gov/35457077/)

- Expert score: `102.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APP` / `Glioma` / `Amyloid Hypothesis,Abnormal Autophagy Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: It has been shown that pharmacological activation of PPARalpha receptors by their agonists gemfibrozil and 2-[4-chloro-6-(2,3-dimethylanilino)pyrimidin-2-yl]sulfanylacetic acid (Wy14643) induces autophagy in HM microglial and U251 human glioma cells expressing a mutant form of human APP (APP-p.M671L).

### 3. APP / PMID [32486013](https://pubmed.ncbi.nlm.nih.gov/32486013/)

- Expert score: `102.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APP` / `positive regulation of mitochondrial membrane permeability` / `Oxidative stress hypothesis,Mitochondrial autophagy hypothesis`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Blocking cyclophilin D, a component of mitochondrial permeability transition pore, enhances cognitive functions as well as diminishes oxidative stress in amyloid precursor protein (APP) transgenic mice.

### 4. APP / PMID [31209071](https://pubmed.ncbi.nlm.nih.gov/31209071/)

- Expert score: `102.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APP` / `Complement Component 3 Deficiency, Autosomal Recessive` / `Amyloid hypothesis,Neuroinflammation hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: In the DBA/2J mouse model of glaucoma, genetic and pharmacological inhibition of C3 increased retinal ganglion cell degeneration, while in the amyloid precursor protein transgenic Alzheimer's disease mouse model, C3 ablation and inhibition worsened total Abeta and fibrillar amyloid plaque burden in the brain, altered microglial activation, and increased hippocampal neuronal degeneration.

### 5. APP / PMID [37887303](https://pubmed.ncbi.nlm.nih.gov/37887303/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APP` / `Hemorrhage` / `Amyloid Hypothesis,Vascular Hypothesis`
- Mechanism strata: amyloid/tau axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Harboring a common familial APP mutation (London V717I) this 1999 model also utilized a neuronal Thy1 promoter to drive hAPP overexpression which lead to spatial memory deficits by 6 months, Abeta plaque formations by 10 months, CAA by 15 months, and micro hemorrhages by 25-30 months.

### 6. APP / PMID [36430913](https://pubmed.ncbi.nlm.nih.gov/36430913/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APP` / `-` / `Amyloid Hypothesis,Abnormal Autophagy Hypothesis`
- Mechanism strata: amyloid/tau axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: When NAGLU was overexpressed in human U251-APP cells, which expresses a mutant form of the Abeta-precursor protein (APP), APP-p.M671L, these cells exhibited stronger lysosomal activity and and enhanced expression of lysosomal pathway genes.

### 7. APP / PMID [29238218](https://pubmed.ncbi.nlm.nih.gov/29238218/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APP` / `cholesterol esterification` / `Amyloid hypothesis,Vascular hypothesis`
- Mechanism strata: amyloid/tau axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: In cultured neurons, the cholesterol ester cycle regulated Abeta-induced synapse damage; inhibition of cholesterol ester hydrolases protected neurons, whereas inhibition of cholesterol esterification increased the Abeta-induced synapse damage.

### 8. APP / PMID [37642583](https://pubmed.ncbi.nlm.nih.gov/37642583/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `amyloid beta precursor protein` / `-` / `Amyloid Hypothesis,Abnormal Autophagy Hypothesis`
- Mechanism strata: amyloid/tau axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Further reports also indicated that endocytosed Abeta disrupts endo-lysosomal compartments thereby contributing to neuronal death.Abeta variants of various length have been identified that result from alternative processing of APP (amyloid beta precursor protein) and/or further cleavages of Abeta by several peptidases.

### 9. APP / PMID [37873467](https://pubmed.ncbi.nlm.nih.gov/37873467/)

- Expert score: `98.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APP` / `hypersensitivity` / `Amyloid Hypothesis,Tau Protein Hypothesis,Glutamatergic Excitotoxicity Hypothesis`
- Mechanism strata: amyloid/tau axis; synaptic and neuronal dysfunction axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Interestingly, all three transgenic mutants exhibited a significantly higher level of sensitivity (hypersensitivity) to 5-HT compared to the wild-type, indicating the neurotoxicity caused by Abeta and/or tau expression in neuronal plasticity and function is at least partially mediated by 5-HT (Figure 1C).

### 10. APOE / PMID [37108421](https://pubmed.ncbi.nlm.nih.gov/37108421/)

- Expert score: `102.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `lipid binding` / `Neuroinflammation hypothesis,Vascular hypothesis`
- Mechanism strata: neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: These polymorphisms cause differences in the lipid binding properties of the APOE isoforms and receptor affinities; APOE4 is hypolipidated compared to APOE3 and APOE2 (Figure 3).

### 11. APOE / PMID [23867607](https://pubmed.ncbi.nlm.nih.gov/23867607/)

- Expert score: `102.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `Neurotoxicity Syndromes` / `Amyloid Hypothesis,Neuroinflammation Hypothesis.`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis; proteostasis/autophagy axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: For example, cleavage of apoE4 produces N- and C-terminal fragments that are neurotoxic in nature.

### 12. APOE / PMID [21283692](https://pubmed.ncbi.nlm.nih.gov/21283692/)

- Expert score: `102.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `regulation of DNA-templated transcription` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Indeed, previous observations of alternative splicing in AD brains for glutamate transporter, PIN1 , estrogen receptor alpha and the APOE receptor genes strongly suggest that alteration of transcriptional control for genes involved in neuronal physiology is a landmark of ongoing neurodegeneration.

### 13. APOE / PMID [37887303](https://pubmed.ncbi.nlm.nih.gov/37887303/)

- Expert score: `101.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `Vascular System Injuries` / `Oxidative Stress Hypothesis,Vascular Hypothesis`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; vascular/metabolic axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Interestingly, when the APP23 APOE allele was silenced, vascular damage and oxidative stress occurred; conversely, APOE4 overexpression in Tg2576 mice induced oxidative stress and vascular injury.

### 14. APOE / PMID [37455931](https://pubmed.ncbi.nlm.nih.gov/37455931/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `lysosome` / `Abnormal Autophagy Hypothesis,Mitochondrial Autophagy Hypothesis,Oxidative Stress Hypothesis`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Methods: Fibroblasts from Alzheimer's patients with APOE 3/4 + G206D-PSEN1 mutation and homozygous APOE epsilon4 were used to study the effects of APOE polymorphism and PSEN1 mutation on the autophagy pathway, mitochondrial network fragmentation, superoxide anion levels, lysosome clustering, and p62/SQSTM1 levels.

### 15. APOE / PMID [36646419](https://pubmed.ncbi.nlm.nih.gov/36646419/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `inflammatory` / `Neuroinflammation hypothesis,Amyloid hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Microglia differentiated from AD-hiPSCs derived from patients bearing the APOE4 variant displayed a decreased ability to uptake Abeta peptide and alterations in the expression of pro-inflammatory signaling pathway genes compared to isogenic APOE3-hiPSC-derived microglia.

### 16. APOE / PMID [34876200](https://pubmed.ncbi.nlm.nih.gov/34876200/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `collagen` / `Amyloid Hypothesis,Vascular Hypothesis`
- Mechanism strata: amyloid/tau axis; vascular/metabolic axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: For example, increased collagen IV expression is found in the BL of 3xTG (APPswe/PSEN1M146V/TauP301L) transgenic mice, decreased collagen IV level is observed in APPswe (APPK670N, M671L) and APOE4 transgenic mice, while unaltered collagen IV level is reported in PSEN1P117L mice.

### 17. APOE / PMID [35298921](https://pubmed.ncbi.nlm.nih.gov/35298921/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `metabolic process` / `Amyloid hypothesis,Vascular hypothesis`
- Mechanism strata: amyloid/tau axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis; proteostasis/autophagy axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: We have also recently reported that a rare apoE3 variant, APOE3 p.V236E referred to as APOE3 Jacksonville variant, reduces amyloid plaques and neuronal damage by preventing apoE self-oligomerization and promoting lipid metabolism.

### 18. APOE / PMID [35847516](https://pubmed.ncbi.nlm.nih.gov/35847516/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `early endosome` / `Amyloid Hypothesis`
- Mechanism strata: amyloid/tau axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: In addition, a recent study has shown that pharmacological and genetic inhibition of NHE6, a primary protein involved in proton leak channel in early endosome, completely restores the APOE4-induced recycling block of APOE receptor and counteracts Abeta-induced LTP suppression in APOE-knockin mice.


## Additional High-Scoring Evidence Traces

### 1. APOE / PMID [32417770](https://pubmed.ncbi.nlm.nih.gov/32417770/)

- Expert score: `100.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `Cerebral hemorrhage` / `Neuroinflammation Hypothesis,Amyloid Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis; proteostasis/autophagy axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: In murine models, blocking apoE4 with the apoE mimetic peptide drug CN-105 reduced neuro-inflammation and improved cognitive, neurobehavioral, and motor outcomes in traumatic brain injury, ischemic stroke, and cerebral hemorrhage models.

### 2. APOE / PMID [27025652](https://pubmed.ncbi.nlm.nih.gov/27025652/)

- Expert score: `99.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `-` / `Amyloid Hypothesis,Neuroinflammation Hypothesis,Vascular Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Duplication of the wild-type APP gene in Down's syndrome leads to Abeta deposits in the teens, followed by microgliosis, astrocytosis, and neurofibrillary tangles typical of AD Apolipoprotein E4, which predisposes to AD in > 40% of cases, has been found to impair Abeta clearance from the brain.

### 3. APP / PMID [35216123](https://pubmed.ncbi.nlm.nih.gov/35216123/)

- Expert score: `98.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APP` / `senescence` / `Amyloid hypothesis,Neuroinflammation hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: showed that the expression of cell senescence marker p16 is significantly increased in neurons, although not in astrocytes or microglia, in 5XFAD transgenic mice, which overexpress human amyloid beta (A4) precursor protein 695 (APP) with three mutations detected in familial Alzheimer's disease (FAD) and human presenilin 1 (PS1) harboring two FAD mutations.

### 4. APOE / PMID [37019383](https://pubmed.ncbi.nlm.nih.gov/37019383/)

- Expert score: `98.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `cAMP-dependent protein kinase complex` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: For instance, hVASP interactions with microfilament motor activity proteins Myo1b, Myo1c, and Myo5a were increased following PKA inhibition in apoE4 Neuro-2a cells.

### 5. APOE / PMID [24644280](https://pubmed.ncbi.nlm.nih.gov/24644280/)

- Expert score: `98.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `reactive oxygen species biosynthetic process` / `Amyloid hypothesis,Oxidative stress hypothesis`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: Specifically, apoE4[L28P] promoted the cellular uptake of extracellular amyloid beta peptide 42 (Abeta42) by human neuroblastoma SK-N-SH cells as well as by primary mouse neuronal cells and led to increased formation of intracellular reactive oxygen species that persisted for at least 24 h. Furthermore, lipoprotein particles containing apoE4[L28P] induced intracellular reactive oxygen species formation and reduced SK-N-SH cell viability.

### 6. APOE / PMID [38203341](https://pubmed.ncbi.nlm.nih.gov/38203341/)

- Expert score: `98.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `brain microstructure damage` / `Amyloid Hypothesis,Vascular Hypothesis`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; vascular/metabolic axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: The level of HMGCR in AD patients is positively correlated with AD-related cognitive impairment and brain microstructure damage, and variation in the APOE gene further increases the expression of HMGCR.

### 7. APOE / PMID [36597122](https://pubmed.ncbi.nlm.nih.gov/36597122/)

- Expert score: `98.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `Blood Platelet Disorders` / `Amyloid Hypothesis,Tau Protein Hypothesis`
- Mechanism strata: amyloid/tau axis; vascular/metabolic axis; proteostasis/autophagy axis
- Reasons: model_or_intervention evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: BACKGROUND: APOE variants are strongly associated with abnormal amyloid aggregation and additional direct effects of APOE on tau aggregation are reported in animal and human cell models.

### 8. APOE / PMID [37927337](https://pubmed.ncbi.nlm.nih.gov/37927337/)

- Expert score: `98.0`; tier: `high_insight`; decision: `include`
- Gene/term/hypothesis: `APOE` / `low-density lipoprotein` / `Neuroinflammation hypothesis,Amyloid hypothesis`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; vascular/metabolic axis
- Reasons: molecular_mechanism evidence; informative original sentence; AD-pathology vocabulary present; molecular or experimental mechanism detail; maps to a candidate AD mechanism stratum; long-tail signal with possible discovery value
- Cautions: -
- Original sentence: These variants affect the stability of TREM2, impair its phagocytic ability, and alter its affinity for APOE4, clusterin (ApoJ), low-density lipoprotein, and Abeta.


## Secondary Evidence Traces

No evidence rows available.

## Deprioritized Evidence Summary

| Rank | Target | Score | PMID | Gene | Phenotype | Mechanism strata | Expert reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| - | - | - | - | - | - | - | No evidence rows were deprioritized by the expert screen. |

## Source Payloads

- `APOE` overview: http://117.72.176.137/api/adalterome/gene/overview?gene=APOE
- `APOE` curation/evidence: http://117.72.176.137/api/adalterome/gene/curation?gene=APOE&selected_limit=80
- `APP` overview: http://117.72.176.137/api/adalterome/gene/overview?gene=APP
- `APP` curation/evidence: http://117.72.176.137/api/adalterome/gene/curation?gene=APP&selected_limit=80
