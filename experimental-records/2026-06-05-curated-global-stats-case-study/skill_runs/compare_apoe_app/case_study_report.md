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