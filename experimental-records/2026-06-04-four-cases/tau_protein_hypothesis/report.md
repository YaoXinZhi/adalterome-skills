# AD-Alterome Hypothesis Report: Tau Protein Hypothesis

## Query Scope and Data Provenance

- Target hypothesis: `Tau Protein Hypothesis`
- API base URL: `http://117.72.176.137/api/adalterome`
- Overview request: http://117.72.176.137/api/adalterome/hypothesis/overview?hypothesis=Tau+Protein+Hypothesis
- Curation evidence source: http://117.72.176.137/api/adalterome/hypothesis/curation?hypothesis=Tau+Protein+Hypothesis&selected_limit=5
- Curation package: `data/curation.json`

## Global Evidence Landscape

AD-Alterome links `Tau Protein Hypothesis` to 38095 event records across 5580 PMID(s), 1410 gene(s), and 1024 term(s). This supports an evidence map for the hypothesis, not proof that the hypothesis is complete or causal.

### Top genes

- MAPT: 16999
- APP: 1736
- PSEN1: 1562
- APOE: 757
- SNCA: 650
- TAS2R62P: 574
- GRN: 494
- TARDBP: 473
- TREM2: 435
- PSEN2: 374

### Top terms

- Alzheimer Disease (MeSH): 2335
- protein (GO): 1341
- Dementia (HPO): 864
- phosphorylation (GO): 809
- Tauopathies (MeSH): 780
- Neurodegeneration (HPO): 598
- Frontotemporal dementia (HPO): 565
- Nerve Degeneration (MeSH): 510
- biosynthetic process (GO): 468
- hyperphosphorylation (GO): 458

## Evidence Curation Layer

- Raw API scoring fields are ignored in skill reports and curation decisions.
- Sentence-level evidence source: remote_api (server_full_query_pool).
- Curation pool rows: 38103; event-unique rows after query-specific deduplication: 17537.
- Overview event rows reported by the API: 38095.
- Event deduplication key: hypothesis-fixed event key: gene + alteration taxonomy + phenotype/term; fallback to PMID/sentence when structured fields are sparse.
- Unique PMIDs in curation pool: 4520; genes: 1410; phenotypes: 1039; alteration taxonomies: 28; gene-alteration pairs: 2731.
- Long-tail rule: Query-specific frequency <= min(Q25, 10) after event-level deduplication across dimensions gene, gene_alteration, phenotype; thresholds={'gene': 2, 'gene_alteration': 1, 'phenotype': 1}.

### Dominant PMIDs

- 33419465: 77
- 30249283: 54
- 32325732: 52
- 31405128: 49
- 37131250: 48

### Top genes

- MAPT: 4533
- APP: 695
- PSEN1: 573
- SNCA: 321
- TAS2R62P: 320

### Top gene-alteration pairs

- MAPT / point mutations:mutations: 1104
- MAPT / normalized variants:dna change: 1074
- MAPT / structural variation:deletion: 322
- MAPT / epigenic changes:phosphorylation: 312
- PSEN1 / point mutations:mutations: 293

### Top phenotypes

- Alzheimer Disease: 524
- protein: 378
- phosphorylation: 337
- Neurodegeneration: 203
- hyperphosphorylation: 190

### Dominant alteration taxonomy

- point mutations:mutations: 5508
- normalized variants:dna change: 2341
- structural variation:deletion: 1615
- expression changes:dysregulation: 1347
- expression changes:underexpression: 1273

### Evidence type distribution

- alteration_evidence: 11755
- model_or_intervention: 5782

### Mechanism strata distribution

- amyloid/tau axis: 17537
- synaptic and neuronal dysfunction axis: 6254
- proteostasis/autophagy axis: 6133
- neuroinflammation and microglia axis: 3228
- mitochondrial and oxidative stress axis: 3141

### Query-relative top and long-tail patterns

| Dimension | Top values | Long-tail values |
| --- | --- | --- |
| Gene | MAPT (4533); APP (695); PSEN1 (573); SNCA (321); TAS2R62P (320); APOE (310); TREM2 (267); TARDBP (211) | ABCC1 (1); ABCC6 (1); ABT1 (1); ACVR1 (1); ADGRB3 (1); AGER (1); AGPS (1); AIF1 (1) |
| Gene-alteration | MAPT / point mutations:mutations (1104); MAPT / normalized variants:dna change (1074); MAPT / structural variation:deletion (322); MAPT / epigenic changes:phosphorylation (312); PSEN1 / point mutations:mutations (293); APP / point mutations:mutations (293); MAPT / expression changes:dysregulation (275); PSEN1 / normalized variants:dna change (196) | ABCC1 / normalized variants:rsid normalized (1); ABCC6 / point mutations:mutations (1); ABI3 / normalized variants:protein change (1); ABT1 / point mutations:mutations (1); ACAT2 / normalized variants:dna change (1); ACAT2 / point mutations:mutations (1); ACHE / expression changes:underexpression (1); ACHE / point mutations:mutations (1) |
| Phenotype | phosphorylation (337); AD (309); 4137 (292); Neurodegeneration (203); hyperphosphorylation (190); biosynthetic process (174); Nerve Degeneration (161); Tauopathies (157) | 1-phosphatidylinositol-3-kinase activity (1); 100506658 (1); 101084670 (1); 10376 (1); 10919 (1); 10922 (1); 10971 (1); 112935892 (1) |

## Mechanism-Stratified Evidence Map

| Candidate mechanism stratum | Selected evidence rows | Representative genes |
| --- | --- | --- |
| amyloid/tau axis | 5 | UCP1, MAPT, MAG, CD68 |
| mitochondrial and oxidative stress axis | 2 | UCP1 |
| neuroinflammation and microglia axis | 1 | CD68 |
| proteostasis/autophagy axis | 1 | MAPT |
| synaptic and neuronal dysfunction axis | 3 | MAPT, MAG, CD68 |
| vascular/metabolic axis | 2 | MAG, CD68 |

These strata organize support patterns for expert review. Hypothesis labels remain curated AD-Alterome assignments, not proof of causality.

## Representative Support Evidence

| # | PMID | Gene | Phenotype | Evidence type | Mechanism strata | Sentence informativeness |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [36769062](https://pubmed.ncbi.nlm.nih.gov/36769062/) | UCP1 | phosphorylation | model_or_intervention | amyloid/tau axis; mitochondrial and oxidative stress axis | 90.0 |
| 2 | [37929088](https://pubmed.ncbi.nlm.nih.gov/37929088/) | MAPT | Generalized | alteration_evidence | amyloid/tau axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | 90.0 |
| 3 | [36769062](https://pubmed.ncbi.nlm.nih.gov/36769062/) | UCP1 | Memory impairment | model_or_intervention | amyloid/tau axis; mitochondrial and oxidative stress axis | 90.0 |
| 4 | [37927337](https://pubmed.ncbi.nlm.nih.gov/37927337/) | MAG | biosynthetic process | model_or_intervention | amyloid/tau axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | 90.0 |
| 5 | [36966157](https://pubmed.ncbi.nlm.nih.gov/36966157/) | CD68 | Auditory Diseases, Central | model_or_intervention | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | 90.0 |

## Long-Tail Evidence Signals

| # | PMID | Gene | Phenotype | Evidence type | Long-tail dimensions | Reasons |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [36769062](https://pubmed.ncbi.nlm.nih.gov/36769062/) | UCP1 | phosphorylation | model_or_intervention | gene=UCP1 (2) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 2 | [36769062](https://pubmed.ncbi.nlm.nih.gov/36769062/) | UCP1 | Memory impairment | model_or_intervention | gene=UCP1 (2) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 3 | [37927337](https://pubmed.ncbi.nlm.nih.gov/37927337/) | MAG | biosynthetic process | model_or_intervention | gene=MAG (1); gene_alteration=MAG / structural variation:deletion (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 4 | [36966157](https://pubmed.ncbi.nlm.nih.gov/36966157/) | CD68 | Auditory Diseases, Central | model_or_intervention | gene_alteration=CD68 / genetic manipulation:knockout (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 5 | [37507386](https://pubmed.ncbi.nlm.nih.gov/37507386/) | UCHL1 | biosynthetic process | model_or_intervention | gene_alteration=UCHL1 / genetic manipulation:knockout (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 6 | [37014857](https://pubmed.ncbi.nlm.nih.gov/37014857/) | ADRB1 | Frontotemporal dementia | model_or_intervention | gene=ADRB1 (2) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 7 | [37194065](https://pubmed.ncbi.nlm.nih.gov/37194065/) | DDR1 | PD | model_or_intervention | gene=DDR1 (2) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 8 | [37726816](https://pubmed.ncbi.nlm.nih.gov/37726816/) | USP5 | phosphorylation | model_or_intervention | gene=USP5 (1); gene_alteration=USP5 / genetic manipulation:knockout (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 9 | [36399251](https://pubmed.ncbi.nlm.nih.gov/36399251/) | FLNA | intracellular anatomical structure | model_or_intervention | gene_alteration=FLNA / normalized variants:dna change (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 10 | [37398204](https://pubmed.ncbi.nlm.nih.gov/37398204/) | CUL5 | Obligate | model_or_intervention | gene=CUL5 (2) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 11 | [37398204](https://pubmed.ncbi.nlm.nih.gov/37398204/) | RNF7 | Obligate | model_or_intervention | gene=RNF7 (2) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 12 | [38110916](https://pubmed.ncbi.nlm.nih.gov/38110916/) | DNAJC7 | intracellular anatomical structure | model_or_intervention | gene=DNAJC7 (1); gene_alteration=DNAJC7 / genetic manipulation:knockout (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 13 | [38020758](https://pubmed.ncbi.nlm.nih.gov/38020758/) | PHF1 | Mucolipidoses | model_or_intervention | gene_alteration=PHF1 / genetic manipulation:knockout (1); phenotype=Mucolipidoses (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 14 | [36239352](https://pubmed.ncbi.nlm.nih.gov/36239352/) | MCU | memory | model_or_intervention | gene=MCU (1); gene_alteration=MCU / genetic manipulation:knockout (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 15 | [36551220](https://pubmed.ncbi.nlm.nih.gov/36551220/) | HS3ST1 | binding | model_or_intervention | gene_alteration=HS3ST1 / genetic manipulation:knockout (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 16 | [35929619](https://pubmed.ncbi.nlm.nih.gov/35929619/) | S100A9 | Cardiac Output, Low | model_or_intervention | phenotype=Cardiac Output, Low (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 17 | [36502636](https://pubmed.ncbi.nlm.nih.gov/36502636/) | ZBTB20 | cell | model_or_intervention | gene_alteration=ZBTB20 / genetic manipulation:knockout (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 18 | [34670118](https://pubmed.ncbi.nlm.nih.gov/34670118/) | CAMK2A | Tauopathies | model_or_intervention | gene=CAMK2A (2) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 19 | [35852137](https://pubmed.ncbi.nlm.nih.gov/35852137/) | DRG2 | microtubule | model_or_intervention | gene=DRG2 (1); gene_alteration=DRG2 / genetic manipulation:knockout (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 20 | [36587923](https://pubmed.ncbi.nlm.nih.gov/36587923/) | KDM1A | macroautophagy | model_or_intervention | gene_alteration=KDM1A / expression changes:overexpression (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |

## Chronological Evidence Trajectory

| Period | Event-unique rows | Dominant mechanism strata |
| --- | --- | --- |
| 2010-2014 | 2098 | amyloid/tau axis (2098); synaptic and neuronal dysfunction axis (795); proteostasis/autophagy axis (610); mitochondrial and oxidative stress axis (378); neuroinflammation and microglia axis (224) |
| 2015-2019 | 4697 | amyloid/tau axis (4697); synaptic and neuronal dysfunction axis (1617); proteostasis/autophagy axis (1529); neuroinflammation and microglia axis (916); mitochondrial and oxidative stress axis (867) |
| 2020-2024 | 8605 | amyloid/tau axis (8605); proteostasis/autophagy axis (3370); synaptic and neuronal dysfunction axis (3123); neuroinflammation and microglia axis (1753); mitochondrial and oxidative stress axis (1560) |
| before 2010 | 795 | amyloid/tau axis (795); synaptic and neuronal dysfunction axis (266); proteostasis/autophagy axis (239); mitochondrial and oxidative stress axis (137); vascular/metabolic axis (102) |
| missing year | 1342 | amyloid/tau axis (1342); synaptic and neuronal dysfunction axis (453); proteostasis/autophagy axis (385); neuroinflammation and microglia axis (268); mitochondrial and oxidative stress axis (199) |

## Original Evidence Traces

### Evidence 1: PMID 36769062

- PubMed: https://pubmed.ncbi.nlm.nih.gov/36769062/
- Gene: UCP1
- Journal/Year: Int J Mol Sci / 2023
- Phenotype: phosphorylation
- Hypothesis: Amyloid hypothesis,Tau protein hypothesis,Oxidative stress hypothesis
- Evidence type: model_or_intervention
- Candidate mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis
- Alteration taxonomy: structural variation:deletion
- Gene-alteration: UCP1 / structural variation:deletion
- Alteration mention: Deletion
- Alteration ID: structural variation:deletion
- Trigger/regulation context: leading to / Reg
- Event dedup key: hypothesis | ucp1 | structural variation:deletion | go:0016310
- Long-tail signals: gene=UCP1 (freq 2 <= threshold 2)
- Curation reasons: model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: Deletion of UCP1 in Tg2576 Mice Increases Body Temperature and Exacerbates Alzheimer's Disease-Related Pathologies We previously demonstrated that the Alzheimer's disease (AD)-like model mice, Tg2576, housed at a high ambient temperature of 30 C for 13 months, exhibited increased body temperature, which increased amyloid-beta (Abeta) levels and tau stability, leading to tau phosphorylation and ultimately inducing memory impairment.

### Evidence 2: PMID 37929088

- PubMed: https://pubmed.ncbi.nlm.nih.gov/37929088/
- Gene: MAPT
- Journal/Year: ACS Omega / 2023
- Phenotype: Generalized
- Hypothesis: Tau Protein Hypothesis
- Evidence type: alteration_evidence
- Candidate mechanism strata: amyloid/tau axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis
- Alteration taxonomy: point mutations:substitution
- Gene-alteration: MAPT / point mutations:substitution
- Alteration mention: substitution
- Alteration ID: point mutations:substitution
- Trigger/regulation context: effect / Reg
- Event dedup key: hypothesis | mapt | point mutations:substitution | hp:0012837
- Long-tail signals: phenotype=Generalized (freq 1 <= threshold 1)
- Curation reasons: alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: Interestingly, our study also evaluated the impact of missense mutations on the MAPT protein and found that the substitution of lysine with asparagine (K > N) in nine different transcript-level SNPs resulted in a generalized destabilizing effect on the protein's stability, function, and dynamics.

### Evidence 3: PMID 36769062

- PubMed: https://pubmed.ncbi.nlm.nih.gov/36769062/
- Gene: UCP1
- Journal/Year: Int J Mol Sci / 2023
- Phenotype: Memory impairment
- Hypothesis: Amyloid hypothesis,Tau protein hypothesis,Oxidative stress hypothesis
- Evidence type: model_or_intervention
- Candidate mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis
- Alteration taxonomy: structural variation:deletion
- Gene-alteration: UCP1 / structural variation:deletion
- Alteration mention: Deletion
- Alteration ID: structural variation:deletion
- Trigger/regulation context: inducing / Reg
- Event dedup key: hypothesis | ucp1 | structural variation:deletion | hp:0002354
- Long-tail signals: gene=UCP1 (freq 2 <= threshold 2)
- Curation reasons: model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: Deletion of UCP1 in Tg2576 Mice Increases Body Temperature and Exacerbates Alzheimer's Disease-Related Pathologies We previously demonstrated that the Alzheimer's disease (AD)-like model mice, Tg2576, housed at a high ambient temperature of 30 C for 13 months, exhibited increased body temperature, which increased amyloid-beta (Abeta) levels and tau stability, leading to tau phosphorylation and ultimately inducing memory impairment.

### Evidence 4: PMID 37927337

- PubMed: https://pubmed.ncbi.nlm.nih.gov/37927337/
- Gene: MAG
- Journal/Year: Front Aging Neurosci / 2023
- Phenotype: biosynthetic process
- Hypothesis: Tau Protein Hypothesis,Glutamatergic Excitotoxicity Hypothesis
- Evidence type: model_or_intervention
- Candidate mechanism strata: amyloid/tau axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis
- Alteration taxonomy: structural variation:deletion
- Gene-alteration: MAG / structural variation:deletion
- Alteration mention: deficient
- Alteration ID: structural variation:deletion
- Trigger/regulation context: altered / Reg
- Event dedup key: hypothesis | mag | structural variation:deletion | go:0009058
- Long-tail signals: gene=MAG (freq 1 <= threshold 2), gene_alteration=MAG / structural variation:deletion (freq 1 <= threshold 1)
- Curation reasons: model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: Previous studies have demonstrated that axonal pathology preceding axonal degeneration includes impairment of axonal transport and altered formation of axonal spheroids in mice deficient in PLP (proteolipid protein) and CNP (2',3'-cyclic nucleotide 3'-phosphodiesterase), as well as reduced neurofilament phosphorylation and smaller axonal diameter in MAG (myelin-associated glycoprotein) deficient mice.

### Evidence 5: PMID 36966157

- PubMed: https://pubmed.ncbi.nlm.nih.gov/36966157/
- Gene: CD68
- Journal/Year: Nat Commun / 2023
- Phenotype: Auditory Diseases, Central
- Hypothesis: Tau protein hypothesis,Neuroinflammation hypothesis
- Evidence type: model_or_intervention
- Candidate mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis
- Alteration taxonomy: genetic manipulation:knockout
- Gene-alteration: CD68 / genetic manipulation:knockout
- Alteration mention: knockdown
- Alteration ID: genetic manipulation:knockout
- Trigger/regulation context: increased / PosReg
- Event dedup key: hypothesis | cd68 | genetic manipulation:knockout | mesh:d001304
- Long-tail signals: gene_alteration=CD68 / genetic manipulation:knockout (freq 1 <= threshold 1)
- Curation reasons: model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: Reinforcing earlier discussion on hp-tau aggregates and neuronal phagoptosis, APOE knockdown in P301S mice significantly reduced hippocampal and entorhinal cortex loss; APOE preservation increased Iba1 + (suggesting microglia and macrophage populations) cells that were positive with CD68 + phagocytic inclusions.


## Interpretation Guide for the User Question

- Separate direct sentence support from AD-Alterome hypothesis assignment fields.
- Use curated representative evidence to discuss support patterns across genes and terms.
- Treat candidate mechanism strata as LLM-assisted organization for expert review.
- Avoid claiming that the hypothesis is proven by sentence-level database evidence.

## Follow-Up Analysis Priorities

- Use `--selected-limit` to request a larger displayed set from the server-side full-pool curation endpoint.
- `--curation-limit` only affects fallback mode when the server does not expose `/hypothesis/curation`.
- Review `data/curation.json` to filter by `EvidenceType`, `MechanismStrata`, `IsLongTailEvidence`, year, gene, phenotype, gene-alteration pair, or alteration taxonomy.
- Compare support against adjacent hypotheses when hypothesis combinations dominate returned evidence.