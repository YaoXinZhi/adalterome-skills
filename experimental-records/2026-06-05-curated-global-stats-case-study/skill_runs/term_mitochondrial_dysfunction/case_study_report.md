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