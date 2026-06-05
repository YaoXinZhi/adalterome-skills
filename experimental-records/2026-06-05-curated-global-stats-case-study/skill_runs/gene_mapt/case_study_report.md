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