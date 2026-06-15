# AD-Alterome Gene Comparison: APP vs APOE

## Query Scope and Data Provenance

- Gene A: `APP`
- Gene B: `APOE`
- API base URL: `http://117.72.176.137/api/adalterome`
- Compare request: http://117.72.176.137/api/adalterome/compare/genes?gene_a=APP&gene_b=APOE
- Gene A curation evidence source: http://117.72.176.137/api/adalterome/gene/curation?gene=APP&selected_limit=4
- Gene B curation evidence source: http://117.72.176.137/api/adalterome/gene/curation?gene=APOE&selected_limit=4
- Gene A curation package: `data/gene_a_curation.json`
- Gene B curation package: `data/gene_b_curation.json`

## Side-by-Side Global Evidence Landscape

| Metric | Gene A | Gene B |
| --- | --- | --- |
| event_count | 18277 | 13188 |
| pmid_count | 4724 | 3086 |
| term_count | 621 | 660 |
| hypothesis_count | 150 | 138 |

## Shared Terms and Hypotheses

### Shared terms
- Alzheimer Disease: gene A=2459, gene B=1783
- protein: gene A=2030, gene B=291
- Onset: gene A=959, gene B=627
- Dementia: gene A=162, gene B=289
- Sporadic: gene A=173, gene B=266
- Alzheimer disease: gene A=176, gene B=140

### Shared hypotheses
- Amyloid Hypothesis: gene A=13553, gene B=3946
- Amyloid Hypothesis,Vascular Hypothesis: gene A=423, gene B=2843
- Amyloid Hypothesis,Tau Protein Hypothesis: gene A=1185, gene B=313
- Amyloid Hypothesis,Neuroinflammation Hypothesis: gene A=345, gene B=384
- Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis: gene A=167, gene B=92

## APP-Specific Patterns

### Unique terms
- All: 262
- biosynthetic process: 253
- chromosome: 183
- cleavage: 144

### Unique hypotheses
- Amyloid Hypothesis,Mitochondrial Autophagy Hypothesis: 235
- Amyloid Hypothesis,Oxidative Stress Hypothesis: 208
- Amyloid Hypothesis,Abnormal Autophagy Hypothesis: 166
- Amyloid Hypothesis,Metal Ion Hypothesis: 113
- Amyloid Hypothesis,Glutamatergic Excitotoxicity Hypothesis: 101

## APOE-Specific Patterns

### Unique terms
- Late onset: 455
- Cognition Disorders: 173
- developmental process: 164
- Cognitive impairment: 129

### Unique hypotheses
- Vascular Hypothesis: 1507
- Neuroinflammation Hypothesis: 263
- Neuroinflammation Hypothesis,Vascular Hypothesis: 177
- Neuroinflammation Hypothesis,Amyloid Hypothesis: 107
- Oxidative Stress Hypothesis: 88

## Evidence Curation Layer

- Raw API scoring fields are ignored in skill reports and curation decisions.
- Sentence-level evidence source: remote_api (server_full_query_pool).
- Curation pool rows: 18277; event-unique rows after query-specific deduplication: 4985.
- Overview event rows reported by the API: 18277.
- Event deduplication key: gene-fixed event key: alteration taxonomy + phenotype/term + hypothesis; fallback to PMID/sentence when structured fields are sparse.
- Unique PMIDs in curation pool: 2419; genes: 1; phenotypes: 625; alteration taxonomies: 29; gene-alteration pairs: 29.
- Long-tail rule: Query-specific frequency <= min(Q25, 10) after event-level deduplication across dimensions phenotype, gene_alteration, hypothesis; thresholds={'phenotype': 1, 'gene_alteration': 10, 'hypothesis': 3}.

### Dominant PMIDs

- 26452528: 19
- 26198711: 17
- 34366346: 16
- 35623389: 16
- 32033020: 16

### Top genes

- APP: 4985

### Top gene-alteration pairs

- APP / point mutations:mutations: 2288
- APP / normalized variants:dna change: 643
- APP / structural variation:deletion: 274
- APP / expression changes:dysregulation: 241
- APP / expression changes:underexpression: 234

### Top phenotypes

- protein: 121
- Alzheimer Disease: 107
- Onset: 49
- biosynthetic process: 46
- Neurodegeneration: 42

### Dominant alteration taxonomy

- point mutations:mutations: 2288
- normalized variants:dna change: 643
- structural variation:deletion: 274
- expression changes:dysregulation: 241
- expression changes:underexpression: 234

### Evidence type distribution

- alteration_evidence: 3500
- model_or_intervention: 1485

### Mechanism strata distribution

- amyloid/tau axis: 4985
- proteostasis/autophagy axis: 1593
- synaptic and neuronal dysfunction axis: 1534
- mitochondrial and oxidative stress axis: 905
- vascular/metabolic axis: 747

### Query-relative top and long-tail patterns

| Dimension | Top values | Long-tail values |
| --- | --- | --- |
| Phenotype | AD (57); biosynthetic process (46); Neurodegeneration (42); Cognition Disorders (40); Nerve Degeneration (38); expression (36); memory (34); cell (30) | 102 (1); 1020 (1); 112935892 (1); 12368 (1); 14961 (1); 16002 (1); 16846 (1); 1728 (1) |
| Gene-alteration | APP / point mutations:mutations (2288); APP / normalized variants:dna change (643); APP / structural variation:deletion (274); APP / expression changes:dysregulation (241); APP / expression changes:underexpression (234); APP / structural variation:chromosomal variation (199); APP / genetic manipulation:gene aggregation (149); APP / expression changes:overexpression (116) | APP / copy number variation:fusion (1); APP / epigenic changes:acetylation (1); APP / structural variation:frameshift (1); APP / structural variation:rearrangements (4) |
| Hypothesis | Amyloid Hypothesis (1976); Amyloid Hypothesis,Tau Protein Hypothesis (407); Amyloid hypothesis (333); Amyloid Hypothesis,Vascular Hypothesis (189); Amyloid Hypothesis,Neuroinflammation Hypothesis (169); Amyloid Hypothesis,Oxidative Stress Hypothesis (106); Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis (91); Amyloid Hypothesis,Abnormal Autophagy Hypothesis (85) | Amyloid Hypothesis,Neuroinflammation hypothesis (1); Amyloid Hypothesis,Neuroinflammation hypothesis,Vascular hypothesis (1); Amyloid hypothesis,Oxidative stress hypothesis,Vascular hypothesis (1); Amyloid hypothesis,Tau protein hypothesis,Mitochondrial autophagy hypothesis (1); Amyloid hypothesis,Tau protein hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis (1); Cholinergic Hypothesis (1); Cholinergic Hypothesis,Glutamatergic Excitotoxicity Hypothesis (1); Cholinergic Hypothesis,Neuroinflammation Hypothesis (1) |

## Mechanism-Stratified Evidence Map for APP

| Candidate mechanism stratum | Selected evidence rows | Representative PMIDs |
| --- | --- | --- |
| amyloid/tau axis | 4 | 37513800, 36687366, 37840813, 37895105 |
| mitochondrial and oxidative stress axis | 2 | 37513800, 37840813 |
| neuroinflammation and microglia axis | 1 | 37840813 |
| proteostasis/autophagy axis | 1 | 37840813 |
| synaptic and neuronal dysfunction axis | 1 | 37895105 |

## Representative Evidence for APP

| # | PMID | Gene | Phenotype | Evidence type | Mechanism strata | Sentence informativeness |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [37513800](https://pubmed.ncbi.nlm.nih.gov/37513800/) | APP | Roseolovirus Infections | model_or_intervention | amyloid/tau axis; mitochondrial and oxidative stress axis | 90.0 |
| 2 | [36687366](https://pubmed.ncbi.nlm.nih.gov/36687366/) | APP | Polydactyly, Postaxial | alteration_evidence | amyloid/tau axis | 90.0 |
| 3 | [37840813](https://pubmed.ncbi.nlm.nih.gov/37840813/) | APP | autophagy | model_or_intervention | amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis | 90.0 |
| 4 | [37895105](https://pubmed.ncbi.nlm.nih.gov/37895105/) | APP | Ischemic Attack, Transient | model_or_intervention | amyloid/tau axis; synaptic and neuronal dysfunction axis | 90.0 |

## Long-Tail Evidence Signals

| # | PMID | Gene | Phenotype | Evidence type | Long-tail dimensions | Reasons |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [37513800](https://pubmed.ncbi.nlm.nih.gov/37513800/) | APP | Roseolovirus Infections | model_or_intervention | phenotype=Roseolovirus Infections (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 2 | [37840813](https://pubmed.ncbi.nlm.nih.gov/37840813/) | APP | autophagy | model_or_intervention | hypothesis=Amyloid Hypothesis,Neuroinflammation Hypothesis,Abnormal Autophagy Hypothesis (2) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 3 | [37895105](https://pubmed.ncbi.nlm.nih.gov/37895105/) | APP | Ischemic Attack, Transient | model_or_intervention | phenotype=Ischemic Attack, Transient (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 4 | [38017562](https://pubmed.ncbi.nlm.nih.gov/38017562/) | APP | behavioral deficits | model_or_intervention | phenotype=behavioral deficits (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 5 | [36281858](https://pubmed.ncbi.nlm.nih.gov/36281858/) | APP | myelin sheath | model_or_intervention | phenotype=myelin sheath (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 6 | [34206322](https://pubmed.ncbi.nlm.nih.gov/34206322/) | APP | Cushing Syndrome | model_or_intervention | phenotype=Cushing Syndrome (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 7 | [34880748](https://pubmed.ncbi.nlm.nih.gov/34880748/) | APP | protein import | model_or_intervention | phenotype=protein import (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 8 | [34867159](https://pubmed.ncbi.nlm.nih.gov/34867159/) | APP | GTPase activity | model_or_intervention | phenotype=GTPase activity (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 9 | [35052511](https://pubmed.ncbi.nlm.nih.gov/35052511/) | APP | Neurofibrillary tangles | model_or_intervention | hypothesis=Amyloid hypothesis,Tau protein hypothesis,Oxidative stress hypothesis (2) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 10 | [32356173](https://pubmed.ncbi.nlm.nih.gov/32356173/) | APP | ceramide metabolic process | model_or_intervention | phenotype=ceramide metabolic process (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 11 | [32486013](https://pubmed.ncbi.nlm.nih.gov/32486013/) | APP | positive regulation of mitochondrial membrane permeability | model_or_intervention | phenotype=positive regulation of mitochondrial membrane permeability (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 12 | [32356173](https://pubmed.ncbi.nlm.nih.gov/32356173/) | APP | sphingolipid metabolic process | model_or_intervention | phenotype=sphingolipid metabolic process (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 13 | [31569571](https://pubmed.ncbi.nlm.nih.gov/31569571/) | APP | Hypertelorism with esophageal abnormality and hypospadias | model_or_intervention | phenotype=Hypertelorism with esophageal abnormality and hypospadias (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 14 | [30778297](https://pubmed.ncbi.nlm.nih.gov/30778297/) | APP | Encephalitis | model_or_intervention | phenotype=Encephalitis (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 15 | [31744008](https://pubmed.ncbi.nlm.nih.gov/31744008/) | APP | cytochrome-c oxidase activity | model_or_intervention | phenotype=cytochrome-c oxidase activity (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 16 | [29100987](https://pubmed.ncbi.nlm.nih.gov/29100987/) | APP | Forebrain Defects | model_or_intervention | phenotype=Forebrain Defects (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 17 | [28360125](https://pubmed.ncbi.nlm.nih.gov/28360125/) | APP | cytoskeleton | model_or_intervention | phenotype=cytoskeleton (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 18 | [28025715](https://pubmed.ncbi.nlm.nih.gov/28025715/) | APP | cell body | model_or_intervention | phenotype=cell body (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 19 | [28973985](https://pubmed.ncbi.nlm.nih.gov/28973985/) | APP | one-carbon metabolic process | model_or_intervention | phenotype=one-carbon metabolic process (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 20 | [28085665](https://pubmed.ncbi.nlm.nih.gov/28085665/) | APP | transport | model_or_intervention | hypothesis=Abnormal Autophagy Hypothesis,Mitochondrial Autophagy Hypothesis (3) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |

## Chronological Evidence Trajectory

| Period | Event-unique rows | Dominant mechanism strata |
| --- | --- | --- |
| 2010-2014 | 863 | amyloid/tau axis (863); synaptic and neuronal dysfunction axis (282); proteostasis/autophagy axis (271); mitochondrial and oxidative stress axis (177); vascular/metabolic axis (149) |
| 2015-2019 | 1182 | amyloid/tau axis (1182); proteostasis/autophagy axis (400); synaptic and neuronal dysfunction axis (369); mitochondrial and oxidative stress axis (231); vascular/metabolic axis (147) |
| 2020-2024 | 2024 | amyloid/tau axis (2024); proteostasis/autophagy axis (717); synaptic and neuronal dysfunction axis (667); mitochondrial and oxidative stress axis (358); neuroinflammation and microglia axis (353) |
| before 2010 | 531 | amyloid/tau axis (531); synaptic and neuronal dysfunction axis (124); proteostasis/autophagy axis (121); mitochondrial and oxidative stress axis (87); vascular/metabolic axis (80) |
| missing year | 385 | amyloid/tau axis (385); synaptic and neuronal dysfunction axis (92); proteostasis/autophagy axis (84); vascular/metabolic axis (76); mitochondrial and oxidative stress axis (52) |

## Original Evidence Traces for APP

### Evidence 1: PMID 37513800

- PubMed: https://pubmed.ncbi.nlm.nih.gov/37513800/
- Gene: APP
- Journal/Year: Pathogens / 2023
- Phenotype: Roseolovirus Infections
- Hypothesis: Amyloid Hypothesis
- Evidence type: model_or_intervention
- Candidate mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis
- Alteration taxonomy: point mutations:mutations
- Gene-alteration: APP / point mutations:mutations
- Alteration mention: mutants
- Alteration ID: point mutations:Mutations
- Trigger/regulation context: link / Reg
- Event dedup key: gene | point mutations:mutations | mesh:d019349 | amyloid hypothesis
- Long-tail signals: phenotype=Roseolovirus Infections (freq 1 <= threshold 1)
- Curation reasons: model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: To investigate a potential link between roseolovirus infection and Alzheimer's disease, Bigley and colleagues used MRV to infect a transgenic mouse model in which overexpression of mutants of the human amyloid precursor protein (APP) and presenilin-1 leads to plaque formation.

### Evidence 2: PMID 36687366

- PubMed: https://pubmed.ncbi.nlm.nih.gov/36687366/
- Gene: APP
- Journal/Year: Neuronal Signal / 2023
- Phenotype: Polydactyly, Postaxial
- Hypothesis: Amyloid Hypothesis
- Evidence type: alteration_evidence
- Candidate mechanism strata: amyloid/tau axis
- Alteration taxonomy: point mutations:mutations
- Gene-alteration: APP / point mutations:mutations
- Alteration mention: mutations
- Alteration ID: point mutations:Mutations
- Trigger/regulation context: affect / Reg
- Event dedup key: gene | point mutations:mutations | mesh:c562429 | amyloid hypothesis
- Long-tail signals: phenotype=Polydactyly, Postaxial (freq 1 <= threshold 1)
- Curation reasons: alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: All of the responsible mutations identified affect either the genes coding for the amyloid precursor protein (APP) from which Abeta is formed via a multistep processing pathway, or the genes coding for the presenilin (PS) 1 and 2 proteins that function within this processing pathway as part of an enzyme complex responsible for cleaving Abeta from its immediate precursor.

### Evidence 3: PMID 37840813

- PubMed: https://pubmed.ncbi.nlm.nih.gov/37840813/
- Gene: APP
- Journal/Year: Front Aging / 2023
- Phenotype: autophagy
- Hypothesis: Amyloid Hypothesis,Neuroinflammation Hypothesis,Abnormal Autophagy Hypothesis
- Evidence type: model_or_intervention
- Candidate mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis
- Alteration taxonomy: expression changes:dysregulation
- Gene-alteration: APP / expression changes:dysregulation
- Alteration mention: lacking
- Alteration ID: expression changes:dysregulation
- Trigger/regulation context: accumulation / PosReg
- Event dedup key: gene | expression changes:dysregulation | go:0006914 | amyloid hypothesis,neuroinflammation hypothesis,abnormal autophagy hypothesis
- Long-tail signals: hypothesis=Amyloid Hypothesis,Neuroinflammation Hypothesis,Abnormal Autophagy Hypothesis (freq 2 <= threshold 3)
- Curation reasons: model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: For example, amyloid precursor protein/presenilin 1 (APP/PS1) mice lacking NRF2 exhibited autophagy dysfunction-dependent accumulation of insoluble Abeta aggregates, resulting in an increased pro-inflammatory phenotype.

### Evidence 4: PMID 37895105

- PubMed: https://pubmed.ncbi.nlm.nih.gov/37895105/
- Gene: APP
- Journal/Year: Int J Mol Sci / 2023
- Phenotype: Ischemic Attack, Transient
- Hypothesis: Amyloid Hypothesis,Glutamatergic Excitotoxicity Hypothesis
- Evidence type: model_or_intervention
- Candidate mechanism strata: amyloid/tau axis; synaptic and neuronal dysfunction axis
- Alteration taxonomy: genetic manipulation:knock-in
- Gene-alteration: APP / genetic manipulation:knock-in
- Alteration mention: knock-in
- Alteration ID: -
- Trigger/regulation context: protect / Reg
- Event dedup key: gene | genetic manipulation:knock-in | mesh:d002546 | amyloid hypothesis,glutamatergic excitotoxicity hypothesis
- Long-tail signals: phenotype=Ischemic Attack, Transient (freq 1 <= threshold 1)
- Curation reasons: model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: TRPC6 overexpression has been shown to rescue mushroom spine loss in presenilin and amyloid precursor protein (APP) knock-in mouse models of AD and also protect neurons from ischemic brain damage.


## Evidence Curation Layer

- Raw API scoring fields are ignored in skill reports and curation decisions.
- Sentence-level evidence source: remote_api (server_full_query_pool).
- Curation pool rows: 13188; event-unique rows after query-specific deduplication: 4002.
- Overview event rows reported by the API: 13188.
- Event deduplication key: gene-fixed event key: alteration taxonomy + phenotype/term + hypothesis; fallback to PMID/sentence when structured fields are sparse.
- Unique PMIDs in curation pool: 1898; genes: 1; phenotypes: 657; alteration taxonomies: 26; gene-alteration pairs: 26.
- Long-tail rule: Query-specific frequency <= min(Q25, 10) after event-level deduplication across dimensions phenotype, gene_alteration, hypothesis; thresholds={'phenotype': 1, 'gene_alteration': 10, 'hypothesis': 3}.

### Dominant PMIDs

- 25737044: 21
- 37455931: 20
- 36077289: 15
- 37588688: 12
- 26969397: 12

### Top genes

- APOE: 4002

### Top gene-alteration pairs

- APOE / point mutations:mutations: 2586
- APOE / normalized variants:rsid normalized: 330
- APOE / structural variation:deletion: 184
- APOE / normalized variants:dna change: 169
- APOE / genetic manipulation:knockout: 112

### Top phenotypes

- Alzheimer Disease: 81
- Onset: 47
- protein: 46
- Dementia: 33
- Cognition Disorders: 30

### Dominant alteration taxonomy

- point mutations:mutations: 2586
- normalized variants:rsid normalized: 330
- structural variation:deletion: 184
- normalized variants:dna change: 169
- genetic manipulation:knockout: 112

### Evidence type distribution

- alteration_evidence: 3301
- model_or_intervention: 701

### Mechanism strata distribution

- vascular/metabolic axis: 4002
- amyloid/tau axis: 3126
- proteostasis/autophagy axis: 771
- neuroinflammation and microglia axis: 766
- mitochondrial and oxidative stress axis: 678

### Query-relative top and long-tail patterns

| Dimension | Top values | Long-tail values |
| --- | --- | --- |
| Phenotype | AD (62); expression (36); Cognition Disorders (30); inflammatory response (25); Neurodegeneration (24); metabolic process (24); developmental process (23); aging (22) | 100770679 (1); 10T-BNT scores (1); 11816 (1); 1191 (1); 12346 (1); 12774 (1); 1401 (1); 16019 (1) |
| Gene-alteration | APOE / point mutations:mutations (2586); APOE / normalized variants:rsid normalized (330); APOE / structural variation:deletion (184); APOE / normalized variants:dna change (169); APOE / genetic manipulation:knockout (112); APOE / expression changes:dysregulation (103); APOE / structural variation:chromosomal variation (103); APOE / genetic manipulation:knock-in (94) | APOE / structural variation:insertion (1); APOE / genetic manipulation:gene aggregation (2); APOE / structural variation:rearrangements (2); APOE / structural variation:frameshift (3); APOE / epigenic changes:epigenetics (7); APOE / normalized variants:cdna change (9); APOE / copy number variation:amplification (10) |
| Hypothesis | Amyloid Hypothesis (642); Amyloid Hypothesis,Vascular Hypothesis (477); Vascular Hypothesis (323); Vascular hypothesis (176); Amyloid Hypothesis,Neuroinflammation Hypothesis (128); Amyloid hypothesis,Vascular hypothesis (119); Amyloid Hypothesis,Tau Protein Hypothesis (102); Neuroinflammation Hypothesis (88) | Abnormal Autophagy Hypothesis,Vascular Hypothesis (1); Amyloid Hypothesis,Neuroinflammation Hypothesis. (1); Amyloid Hypothesis,Oxidative Stress Hypothesis,Metal Ion Hypothesis (1); Cholinergic hypothesis,Vascular hypothesis (1); Glutamatergic excitotoxicity hypothesis,Microbiota-Gut-Brain Axis hypothesis (1); Mitochondrial Autophagy Hypothesis,Oxidative Stress Hypothesis (1); Mitochondrial autophagy hypothesis,Vascular hypothesis (1); Neuroinflammation Hypothesis,Abnormal Autophagy Hypothesis (1) |

## Mechanism-Stratified Evidence Map for APOE

| Candidate mechanism stratum | Selected evidence rows | Representative PMIDs |
| --- | --- | --- |
| amyloid/tau axis | 3 | 36966157, 38004343, 36927428 |
| mitochondrial and oxidative stress axis | 1 | 36927428 |
| neuroinflammation and microglia axis | 2 | 36966157, 36835187 |
| proteostasis/autophagy axis | 2 | 38004343, 36927428 |
| synaptic and neuronal dysfunction axis | 1 | 36966157 |
| vascular/metabolic axis | 4 | 36966157, 38004343, 36835187, 36927428 |

## Representative Evidence for APOE

| # | PMID | Gene | Phenotype | Evidence type | Mechanism strata | Sentence informativeness |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [36966157](https://pubmed.ncbi.nlm.nih.gov/36966157/) | APOE | Auditory Diseases, Central | model_or_intervention | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | 90.0 |
| 2 | [38004343](https://pubmed.ncbi.nlm.nih.gov/38004343/) | APOE | of amyloid beta | alteration_evidence | amyloid/tau axis; vascular/metabolic axis; proteostasis/autophagy axis | 90.0 |
| 3 | [36835187](https://pubmed.ncbi.nlm.nih.gov/36835187/) | APOE | isotype switching | model_or_intervention | neuroinflammation and microglia axis; vascular/metabolic axis | 90.0 |
| 4 | [36927428](https://pubmed.ncbi.nlm.nih.gov/36927428/) | APOE | Mitochondrial inheritance | model_or_intervention | amyloid/tau axis; mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis | 90.0 |

## Long-Tail Evidence Signals

| # | PMID | Gene | Phenotype | Evidence type | Long-tail dimensions | Reasons |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [36966157](https://pubmed.ncbi.nlm.nih.gov/36966157/) | APOE | Auditory Diseases, Central | model_or_intervention | phenotype=Auditory Diseases, Central (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 2 | [36835187](https://pubmed.ncbi.nlm.nih.gov/36835187/) | APOE | isotype switching | model_or_intervention | phenotype=isotype switching (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 3 | [36927428](https://pubmed.ncbi.nlm.nih.gov/36927428/) | APOE | Mitochondrial inheritance | model_or_intervention | hypothesis=Amyloid hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis (3) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 4 | [36927428](https://pubmed.ncbi.nlm.nih.gov/36927428/) | APOE | mitochondrion | model_or_intervention | hypothesis=Amyloid hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis (3) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 5 | [37036005](https://pubmed.ncbi.nlm.nih.gov/37036005/) | APOE | Crohn Disease | model_or_intervention | phenotype=Crohn Disease (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 6 | [37199411](https://pubmed.ncbi.nlm.nih.gov/37199411/) | APOE | phospholipid efflux | model_or_intervention | phenotype=phospholipid efflux (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 7 | [36717892](https://pubmed.ncbi.nlm.nih.gov/36717892/) | APOE | SARS-CoV-2-infected | model_or_intervention | phenotype=SARS-CoV-2-infected (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 8 | [37019383](https://pubmed.ncbi.nlm.nih.gov/37019383/) | APOE | cAMP-dependent protein kinase complex | model_or_intervention | phenotype=cAMP-dependent protein kinase complex (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 9 | [36720919](https://pubmed.ncbi.nlm.nih.gov/36720919/) | APOE | Immune System Diseases | model_or_intervention | phenotype=Immune System Diseases (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 10 | [35847516](https://pubmed.ncbi.nlm.nih.gov/35847516/) | APOE | early endosome | model_or_intervention | phenotype=early endosome (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 11 | [34514662](https://pubmed.ncbi.nlm.nih.gov/34514662/) | APOE | lysosomal transport | model_or_intervention | phenotype=lysosomal transport (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 12 | [35111364](https://pubmed.ncbi.nlm.nih.gov/35111364/) | APOE | inflammatory response | model_or_intervention | hypothesis=Neuroinflammation Hypothesis,Oxidative stress hypothesis,Vascular hypothesis (3) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 13 | [35115575](https://pubmed.ncbi.nlm.nih.gov/35115575/) | APOE | inflammatory response | model_or_intervention | hypothesis=Neuroinflammation hypothesis,Microbiota-Gut-Brain Axis hypothesis (3) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 14 | [35115575](https://pubmed.ncbi.nlm.nih.gov/35115575/) | APOE | response to lipopolysaccharide | model_or_intervention | phenotype=response to lipopolysaccharide (1); hypothesis=Neuroinflammation hypothesis,Microbiota-Gut-Brain Axis hypothesis (3) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 15 | [33676568](https://pubmed.ncbi.nlm.nih.gov/33676568/) | APOE | calcium ion transport | model_or_intervention | phenotype=calcium ion transport (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 16 | [34876200](https://pubmed.ncbi.nlm.nih.gov/34876200/) | APOE | collagen | model_or_intervention | phenotype=collagen (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 17 | [33573856](https://pubmed.ncbi.nlm.nih.gov/33573856/) | APOE | chemical synaptic transmission | model_or_intervention | hypothesis=Microbiota-Gut-Brain Axis hypothesis,Neuroinflammation hypothesis (3) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 18 | [33573856](https://pubmed.ncbi.nlm.nih.gov/33573856/) | APOE | memory | model_or_intervention | hypothesis=Microbiota-Gut-Brain Axis hypothesis,Neuroinflammation hypothesis (3) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 19 | [36199750](https://pubmed.ncbi.nlm.nih.gov/36199750/) | APOE | Prune Belly Syndrome | model_or_intervention | phenotype=Prune Belly Syndrome (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 20 | [34151801](https://pubmed.ncbi.nlm.nih.gov/34151801/) | APOE | Mitochondrial Diseases | model_or_intervention | hypothesis=Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis,Neuroinflammation Hypothesis (3) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |

## Chronological Evidence Trajectory

| Period | Event-unique rows | Dominant mechanism strata |
| --- | --- | --- |
| 2010-2014 | 588 | vascular/metabolic axis (588); amyloid/tau axis (457); proteostasis/autophagy axis (114); mitochondrial and oxidative stress axis (102); neuroinflammation and microglia axis (83) |
| 2015-2019 | 994 | vascular/metabolic axis (994); amyloid/tau axis (764); proteostasis/autophagy axis (181); mitochondrial and oxidative stress axis (170); neuroinflammation and microglia axis (137) |
| 2020-2024 | 1736 | vascular/metabolic axis (1736); amyloid/tau axis (1351); neuroinflammation and microglia axis (423); proteostasis/autophagy axis (386); mitochondrial and oxidative stress axis (273) |
| before 2010 | 381 | vascular/metabolic axis (381); amyloid/tau axis (305); mitochondrial and oxidative stress axis (89); synaptic and neuronal dysfunction axis (53); proteostasis/autophagy axis (48) |
| missing year | 303 | vascular/metabolic axis (303); amyloid/tau axis (249); neuroinflammation and microglia axis (86); mitochondrial and oxidative stress axis (44); proteostasis/autophagy axis (42) |

## Original Evidence Traces for APOE

### Evidence 1: PMID 36966157

- PubMed: https://pubmed.ncbi.nlm.nih.gov/36966157/
- Gene: APOE
- Journal/Year: Nat Commun / 2023
- Phenotype: Auditory Diseases, Central
- Hypothesis: Tau protein hypothesis,Neuroinflammation hypothesis
- Evidence type: model_or_intervention
- Candidate mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis
- Alteration taxonomy: genetic manipulation:knockout
- Gene-alteration: APOE / genetic manipulation:knockout
- Alteration mention: knockdown
- Alteration ID: genetic manipulation:knockout
- Trigger/regulation context: increased / PosReg
- Event dedup key: gene | genetic manipulation:knockout | mesh:d001304 | tau protein hypothesis,neuroinflammation hypothesis
- Long-tail signals: phenotype=Auditory Diseases, Central (freq 1 <= threshold 1)
- Curation reasons: model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: Reinforcing earlier discussion on hp-tau aggregates and neuronal phagoptosis, APOE knockdown in P301S mice significantly reduced hippocampal and entorhinal cortex loss; APOE preservation increased Iba1 + (suggesting microglia and macrophage populations) cells that were positive with CD68 + phagocytic inclusions.

### Evidence 2: PMID 38004343

- PubMed: https://pubmed.ncbi.nlm.nih.gov/38004343/
- Gene: APOE
- Journal/Year: Life (Basel);2023Nov13; 13 (11) . doi:10.3390/life13112203 / 2023
- Phenotype: of amyloid beta
- Hypothesis: Amyloid Hypothesis
- Evidence type: alteration_evidence
- Candidate mechanism strata: amyloid/tau axis; vascular/metabolic axis; proteostasis/autophagy axis
- Alteration taxonomy: point mutations:mutations
- Gene-alteration: APOE / point mutations:mutations
- Alteration mention: mutations
- Alteration ID: point mutations:Mutations
- Trigger/regulation context: overproduction / PosReg
- Event dedup key: gene | point mutations:mutations | mesh:c000718787 | amyloid hypothesis
- Long-tail signals: phenotype=of amyloid beta (freq 1 <= threshold 1)
- Curation reasons: alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: EOAD is a very uncommon condition associated with genetic factors such as mutations in susceptibility genes like amyloid precursor protein (APP), apolipoprotein E4 (ApoE4), presenilin 1 (PSEN1), and presenilin 2 (PSEN2), which can lead to an overproduction of amyloid beta.

### Evidence 3: PMID 36835187

- PubMed: https://pubmed.ncbi.nlm.nih.gov/36835187/
- Gene: APOE
- Journal/Year: Int J Mol Sci / 2023
- Phenotype: isotype switching
- Hypothesis: Neuroinflammation hypothesis,Vascular hypothesis
- Evidence type: model_or_intervention
- Candidate mechanism strata: neuroinflammation and microglia axis; vascular/metabolic axis
- Alteration taxonomy: genetic manipulation:knock-in
- Gene-alteration: APOE / genetic manipulation:knock-in
- Alteration mention: knock-in
- Alteration ID: -
- Trigger/regulation context: high / PosReg
- Event dedup key: gene | genetic manipulation:knock-in | go:0045190 | neuroinflammation hypothesis,vascular hypothesis
- Long-tail signals: phenotype=isotype switching (freq 1 <= threshold 1)
- Curation reasons: model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: Another study has demonstrated lower total IgG and IgA levels in the spleen of APOE4 knock-in mice compared with APOE3, but the levels of IgG2a subtype and IgM were quite high in APOE4 mice, suggesting differential Ig class switching in APOE4 mice compared with APOE3 or APOE2 mice.

### Evidence 4: PMID 36927428

- PubMed: https://pubmed.ncbi.nlm.nih.gov/36927428/
- Gene: APOE
- Journal/Year: Curr Neuropharmacol / 2023
- Phenotype: Mitochondrial inheritance
- Hypothesis: Amyloid hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis
- Evidence type: model_or_intervention
- Candidate mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis
- Alteration taxonomy: point mutations:mutations
- Gene-alteration: APOE / point mutations:mutations
- Alteration mention: mutants
- Alteration ID: point mutations:Mutations
- Trigger/regulation context: cause / Reg
- Event dedup key: gene | point mutations:mutations | hp:0001427 | amyloid hypothesis,oxidative stress hypothesis,mitochondrial autophagy hypothesis
- Long-tail signals: hypothesis=Amyloid hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis (freq 3 <= threshold 3)
- Curation reasons: model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: Recent research in cellular, biochemical and animal models have shown that AD mutants affecting the presenilins, Ass, APP, and ApoE4 are associated with mitochondria and cause mitochondrial dysfunction and oxidative damage in AD (Fig.


## Comparative Interpretation Guide

- Use overview counts to describe database representation, not biological importance.
- Use curated representative evidence to compare mechanisms; avoid relying on raw API ranking.
- Compare shared terms and hypotheses against original sentences from both genes.
- Treat candidate mechanism strata as LLM-assisted organization for expert review.

## Follow-Up Priorities

- Use `--selected-limit` to request a larger displayed set from each server-side full-pool gene curation endpoint.
- `--curation-limit` only affects fallback mode when the server does not expose `/gene/curation`.
- Review `data/gene_a_curation.json` and `data/gene_b_curation.json` to filter by `EvidenceType`, `MechanismStrata`, `IsLongTailEvidence`, year, phenotype, gene-alteration pair, or alteration taxonomy.
- Treat unequal event counts as a literature-density signal before making contrastive biological claims.