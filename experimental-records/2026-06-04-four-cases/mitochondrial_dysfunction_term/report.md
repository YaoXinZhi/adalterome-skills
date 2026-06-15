# AD-Alterome Term Report: mitochondrial dysfunction

## Query Scope and Data Provenance

- Target term: `mitochondrial dysfunction`
- API base URL: `http://117.72.176.137/api/adalterome`
- Overview request: http://117.72.176.137/api/adalterome/term/overview?term=mitochondrial+dysfunction
- Curation evidence source: http://117.72.176.137/api/adalterome/term/curation?term=mitochondrial+dysfunction&selected_limit=5
- Curation package: `data/curation.json`

## Global Evidence Landscape

AD-Alterome links `mitochondrial dysfunction` to 925 event records, 427 PMID(s), 219 gene(s), and 43 AD hypothesis field(s). Treat this as a curated literature evidence map rather than a causal conclusion.

### Top genes

- PINK1: 73
- SOD1: 66
- MAPT: 65
- LRRK2: 51
- PARK7: 46
- SNCA: 44
- APP: 32
- HTT: 28
- PRKN: 27
- APOE: 19

### Top hypotheses

- Mitochondrial autophagy hypothesis: 93
- Oxidative stress hypothesis,Mitochondrial autophagy hypothesis: 61
- Amyloid Hypothesis,Mitochondrial Autophagy Hypothesis: 41
- Tau Protein Hypothesis,Mitochondrial Autophagy Hypothesis: 36
- Amyloid Hypothesis,Tau Protein Hypothesis,Mitochondrial Autophagy Hypothesis: 19
- Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis,Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis: 14
- Neuroinflammation Hypothesis,Mitochondrial autophagy hypothesis: 13
- Amyloid Hypothesis,Tau Protein Hypothesis,Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis: 13
- Amyloid hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis: 11
- Abnormal Autophagy Hypothesis,Mitochondrial Autophagy Hypothesis: 11

## Evidence Curation Layer

- Raw API scoring fields are ignored in skill reports and curation decisions.
- Sentence-level evidence source: remote_api (server_full_query_pool).
- Curation pool rows: 925; event-unique rows after query-specific deduplication: 440.
- Overview event rows reported by the API: 925.
- Event deduplication key: term-fixed event key: gene + alteration taxonomy + hypothesis; fallback to PMID/sentence when structured fields are sparse.
- Unique PMIDs in curation pool: 305; genes: 219; phenotypes: 9; alteration taxonomies: 19; gene-alteration pairs: 340.
- Long-tail rule: Query-specific frequency <= min(Q25, 10) after event-level deduplication across dimensions gene, gene_alteration, phenotype, hypothesis; thresholds={'gene': 1, 'gene_alteration': 1, 'phenotype': 1, 'hypothesis': 2}.

### Dominant PMIDs

- 35892559: 7
- 37240173: 6
- 34177463: 6
- 37489441: 4
- 35821838: 4

### Top genes

- MAPT: 33
- PINK1: 15
- APP: 15
- SNCA: 13
- APOE: 12

### Top gene-alteration pairs

- APP / point mutations:mutations: 8
- MAPT / normalized variants:dna change: 8
- PSEN1 / point mutations:mutations: 7
- MAPT / point mutations:mutations: 7
- APOE / point mutations:mutations: 7

### Top phenotypes

- Mitochondrial Diseases: 258
- Mitochondrial inheritance: 123
- Abnormality of mitochondrial metabolism: 49
- Parkinson Disease, Mitochondrial: 2
- mitochondrial dysfunctions: 2

### Dominant alteration taxonomy

- point mutations:mutations: 161
- structural variation:deletion: 66
- expression changes:underexpression: 38
- expression changes:dysregulation: 36
- normalized variants:dna change: 29

### Evidence type distribution

- alteration_evidence: 325
- model_or_intervention: 115

### Mechanism strata distribution

- mitochondrial and oxidative stress axis: 440
- amyloid/tau axis: 304
- proteostasis/autophagy axis: 272
- synaptic and neuronal dysfunction axis: 126
- vascular/metabolic axis: 63

### Query-relative top and long-tail patterns

| Dimension | Top values | Long-tail values |
| --- | --- | --- |
| Gene | MAPT (33); PINK1 (15); APP (15); SNCA (13); APOE (12); SOD1 (10); PSEN1 (9); HTT (9) | ABCA7 (1); ABCB8 (1); ABCD1 (1); ABL1 (1); AFG3L2 (1); AKT1 (1); ALKBH1 (1); alpha-synuclein (1) |
| Gene-alteration | APP / point mutations:mutations (8); MAPT / normalized variants:dna change (8); PSEN1 / point mutations:mutations (7); MAPT / point mutations:mutations (7); APOE / point mutations:mutations (7); SNCA / point mutations:mutations (5); HTT / point mutations:mutations (5); MAPT / genetic manipulation:gene aggregation (5) | ABCA7 / structural variation:deletion (1); ABCB8 / point mutations:mutations (1); ABCD1 / point mutations:mutations (1); ABL1 / expression changes:inactivation (1); AFG3L2 / expression changes:dysregulation (1); AKT1 / expression changes:underexpression (1); ALKBH1 / genetic manipulation:knockout (1); alpha-synuclein / structural variation:chromosomal variation (1) |
| Phenotype | Mitochondrial Diseases (258); Mitochondrial inheritance (123); Abnormality of mitochondrial metabolism (49); Mitochondrial dysfunction (3); Parkinson Disease, Mitochondrial (2); mitochondrial dysfunctions (2); Hyperglycemia (1); Progressive (1) | Brain Diseases, Metabolic (1); Hyperglycemia (1); Progressive (1) |
| Hypothesis | Mitochondrial autophagy hypothesis (35); Mitochondrial Autophagy Hypothesis (34); Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis (25); Oxidative stress hypothesis,Mitochondrial autophagy hypothesis (22); Amyloid Hypothesis,Mitochondrial Autophagy Hypothesis (15); Tau Protein Hypothesis,Mitochondrial Autophagy Hypothesis (10); Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis,Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis (7); Amyloid Hypothesis,Tau Protein Hypothesis,Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis (6) | Glutamatergic excitotoxicity hypothesis (1); Neuroinflammation Hypothesis,Mitochondrial Autophagy Hypothesis (1); Neuroinflammation hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis (1); Neuroinflammation hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis,Vascular hypothesis (1); Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis,Glutamatergic Excitotoxicity Hypothesis (1); Tau Protein Hypothesis,Amyloid Hypothesis,Oxidative Stress Hypothesis,Neuroinflammation Hypothesis,Mitochondrial Autophagy Hypothesis (1); Tau Protein Hypothesis,Neuroinflammation Hypothesis,Mitochondrial Autophagy Hypothesis (1); Tau Protein Hypothesis,Oxidative Stress Hypothesis (1) |

## Mechanism-Stratified Evidence Map

| Candidate mechanism stratum | Selected evidence rows | Representative genes |
| --- | --- | --- |
| mitochondrial and oxidative stress axis | 5 | LDLR, PTN, TOMM40, NEIL1 |
| neuroinflammation and microglia axis | 4 | LDLR, PTN, TOMM40 |
| proteostasis/autophagy axis | 5 | LDLR, PTN, TOMM40, NEIL1 |
| synaptic and neuronal dysfunction axis | 1 | LDLR |
| vascular/metabolic axis | 3 | LDLR, PTN, NEIL1 |

These strata organize molecular and pathological mechanisms for expert review; they are not hard ontology labels.

## Representative Molecular and Pathological Evidence

| # | PMID | Gene | Phenotype | Evidence type | Mechanism strata | Sentence informativeness |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [38056504](https://pubmed.ncbi.nlm.nih.gov/38056504/) | LDLR | Mitochondrial Diseases | model_or_intervention | mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis; proteostasis/autophagy axis | 90.0 |
| 2 | [37484951](https://pubmed.ncbi.nlm.nih.gov/37484951/) | PTN | Mitochondrial Diseases | alteration_evidence | mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; vascular/metabolic axis; proteostasis/autophagy axis | 90.0 |
| 3 | [36835494](https://pubmed.ncbi.nlm.nih.gov/36835494/) | TOMM40 | Mitochondrial inheritance | model_or_intervention | mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis | 90.0 |
| 4 | [36835494](https://pubmed.ncbi.nlm.nih.gov/36835494/) | TOMM40 | Mitochondrial Diseases | model_or_intervention | mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis | 90.0 |
| 5 | [35252966](https://pubmed.ncbi.nlm.nih.gov/35252966/) | NEIL1 | Mitochondrial inheritance | model_or_intervention | mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis | 90.0 |

## Long-Tail Evidence Signals

| # | PMID | Gene | Phenotype | Evidence type | Long-tail dimensions | Reasons |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [38056504](https://pubmed.ncbi.nlm.nih.gov/38056504/) | LDLR | Mitochondrial Diseases | model_or_intervention | hypothesis=Neuroinflammation hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis,Vascular hypothesis (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 2 | [36835494](https://pubmed.ncbi.nlm.nih.gov/36835494/) | TOMM40 | Mitochondrial inheritance | model_or_intervention | gene_alteration=TOMM40 / normalized variants:dna change (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 3 | [36835494](https://pubmed.ncbi.nlm.nih.gov/36835494/) | TOMM40 | Mitochondrial Diseases | model_or_intervention | hypothesis=Neuroinflammation Hypothesis,Mitochondrial Autophagy Hypothesis (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 4 | [36231104](https://pubmed.ncbi.nlm.nih.gov/36231104/) | FRMD6 | Mitochondrial Diseases | model_or_intervention | gene=FRMD6 (1); gene_alteration=FRMD6 / genetic manipulation:knockout (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 5 | [35252966](https://pubmed.ncbi.nlm.nih.gov/35252966/) | NEIL1 | Mitochondrial inheritance | model_or_intervention | gene=NEIL1 (1); gene_alteration=NEIL1 / genetic manipulation:knockout (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 6 | [35252966](https://pubmed.ncbi.nlm.nih.gov/35252966/) | OGG1 | Mitochondrial inheritance | model_or_intervention | gene=OGG1 (1); gene_alteration=OGG1 / genetic manipulation:knockout (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 7 | [36727091](https://pubmed.ncbi.nlm.nih.gov/36727091/) | FXN | Abnormality of mitochondrial metabolism | model_or_intervention | gene_alteration=FXN / epigenic changes:silencing (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 8 | [33676568](https://pubmed.ncbi.nlm.nih.gov/33676568/) | APOE | Mitochondrial inheritance | model_or_intervention | gene_alteration=APOE / epigenic changes:silencing (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 9 | [37181110](https://pubmed.ncbi.nlm.nih.gov/37181110/) | WFS1 | Mitochondrial Diseases | model_or_intervention | gene=WFS1 (1); gene_alteration=WFS1 / epigenic changes:silencing (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 10 | [33062068](https://pubmed.ncbi.nlm.nih.gov/33062068/) | CISD2 | Mitochondrial Diseases | model_or_intervention | gene_alteration=CISD2 / structural variation:deletion (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 11 | [30144530](https://pubmed.ncbi.nlm.nih.gov/30144530/) | BACE1 | Mitochondrial Diseases | model_or_intervention | gene_alteration=BACE1 / expression changes:underexpression (1); hypothesis=Amyloid Hypothesis,Mitochondrial autophagy hypothesis (2) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 12 | [30010002](https://pubmed.ncbi.nlm.nih.gov/30010002/) | NRF1 | Mitochondrial Diseases | model_or_intervention | gene_alteration=NRF1 / expression changes:inactivation (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 13 | [28767121](https://pubmed.ncbi.nlm.nih.gov/28767121/) | APOE | Mitochondrial Diseases | model_or_intervention | hypothesis=Amyloid Hypothesis,Tau Protein Hypothesis,Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis,Vascular Hypothesis (2) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 14 | [28767121](https://pubmed.ncbi.nlm.nih.gov/28767121/) | APP | Mitochondrial Diseases | model_or_intervention | hypothesis=Amyloid Hypothesis,Tau Protein Hypothesis,Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis,Vascular Hypothesis (2) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 15 | [29067327](https://pubmed.ncbi.nlm.nih.gov/29067327/) | WWOX | Mitochondrial Diseases | model_or_intervention | gene=WWOX (1); gene_alteration=WWOX / point mutations:mutations (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 16 | [27535796](https://pubmed.ncbi.nlm.nih.gov/27535796/) | MFN2 | Mitochondrial Diseases | model_or_intervention | gene=MFN2 (1); gene_alteration=MFN2 / genetic manipulation:knockout (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 17 | [21933711](https://pubmed.ncbi.nlm.nih.gov/21933711/) | BACE1 | Mitochondrial Diseases | model_or_intervention | gene_alteration=BACE1 / structural variation:deletion (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 18 | [37484951](https://pubmed.ncbi.nlm.nih.gov/37484951/) | PTN | Mitochondrial Diseases | alteration_evidence | gene=PTN (1); gene_alteration=PTN / structural variation:deletion (1); hypothesis=Neuroinflammation hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 19 | [37371116](https://pubmed.ncbi.nlm.nih.gov/37371116/) | CAT | Mitochondrial inheritance | alteration_evidence | gene=CAT (1); gene_alteration=CAT / epigenic changes:phosphorylation (1); hypothesis=Tau Protein Hypothesis,Oxidative Stress Hypothesis (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 20 | [37238605](https://pubmed.ncbi.nlm.nih.gov/37238605/) | APOE | Abnormality of mitochondrial metabolism | alteration_evidence | gene_alteration=APOE / expression changes:expression (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |

## Chronological Evidence Trajectory

| Period | Event-unique rows | Dominant mechanism strata |
| --- | --- | --- |
| 2010-2014 | 46 | mitochondrial and oxidative stress axis (46); proteostasis/autophagy axis (33); amyloid/tau axis (27); synaptic and neuronal dysfunction axis (11); vascular/metabolic axis (10) |
| 2015-2019 | 111 | mitochondrial and oxidative stress axis (111); amyloid/tau axis (79); proteostasis/autophagy axis (78); synaptic and neuronal dysfunction axis (33); vascular/metabolic axis (18) |
| 2020-2024 | 230 | mitochondrial and oxidative stress axis (230); amyloid/tau axis (168); proteostasis/autophagy axis (129); synaptic and neuronal dysfunction axis (68); vascular/metabolic axis (31) |
| before 2010 | 6 | mitochondrial and oxidative stress axis (6); amyloid/tau axis (4); proteostasis/autophagy axis (3); vascular/metabolic axis (2); synaptic and neuronal dysfunction axis (2) |
| missing year | 47 | mitochondrial and oxidative stress axis (47); proteostasis/autophagy axis (29); amyloid/tau axis (26); synaptic and neuronal dysfunction axis (12); neuroinflammation and microglia axis (3) |

## Original Evidence Traces

### Evidence 1: PMID 38056504

- PubMed: https://pubmed.ncbi.nlm.nih.gov/38056504/
- Gene: LDLR
- Journal/Year: Ageing Res Rev / 2023
- Phenotype: Mitochondrial Diseases
- Hypothesis: Neuroinflammation hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis,Vascular hypothesis
- Evidence type: model_or_intervention
- Candidate mechanism strata: mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis; proteostasis/autophagy axis
- Alteration taxonomy: genetic manipulation:knockout
- Gene-alteration: LDLR / genetic manipulation:knockout
- Alteration mention: knockout
- Alteration ID: genetic manipulation:knockout
- Trigger/regulation context: associated / Reg
- Event dedup key: term | ldlr | genetic manipulation:knockout | neuroinflammation hypothesis,oxidative stress hypothesis,mitochondrial autophagy hypothesis,vascular hypothesis
- Long-tail signals: hypothesis=Neuroinflammation hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis,Vascular hypothesis (freq 1 <= threshold 2)
- Curation reasons: model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: Cognitive and emotional behavioral impairments in LDL receptor knockout (LDLr-/-) mice are associated with neuroinflammation, blood-brain barrier dysfunction, impaired neurogenesis, brain oxidative stress, and mitochondrial dysfunction.

### Evidence 2: PMID 37484951

- PubMed: https://pubmed.ncbi.nlm.nih.gov/37484951/
- Gene: PTN
- Journal/Year: Front Endocrinol (Lausanne) / 2023
- Phenotype: Mitochondrial Diseases
- Hypothesis: Neuroinflammation hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis
- Evidence type: alteration_evidence
- Candidate mechanism strata: mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; vascular/metabolic axis; proteostasis/autophagy axis
- Alteration taxonomy: structural variation:deletion
- Gene-alteration: PTN / structural variation:deletion
- Alteration mention: deletion
- Alteration ID: structural variation:deletion
- Trigger/regulation context: protects / PosReg
- Event dedup key: term | ptn | structural variation:deletion | neuroinflammation hypothesis,oxidative stress hypothesis,mitochondrial autophagy hypothesis
- Long-tail signals: gene=PTN (freq 1 <= threshold 1), gene_alteration=PTN / structural variation:deletion (freq 1 <= threshold 1), hypothesis=Neuroinflammation hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis (freq 1 <= threshold 2)
- Curation reasons: alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: Moreover, recent reports have evidenced that PTN is implicated in the regulation of peripheral metainflammation, metabolic homeostasis, thermogenesis, as well as insulin sensitivity in the peripheral tissues Furthermore, Ptn deletion protects against neuroinflammation, mitochondrial dysfunction, and aberrant protein aggregation in a high fat diet (HFD) induced obesity model.

### Evidence 3: PMID 36835494

- PubMed: https://pubmed.ncbi.nlm.nih.gov/36835494/
- Gene: TOMM40
- Journal/Year: Int J Mol Sci / 2023
- Phenotype: Mitochondrial inheritance
- Hypothesis: Neuroinflammation Hypothesis,Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis
- Evidence type: model_or_intervention
- Candidate mechanism strata: mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis
- Alteration taxonomy: normalized variants:dna change
- Gene-alteration: TOMM40 / normalized variants:dna change
- Alteration mention: F113L
- Alteration ID: rs157581
- Trigger/regulation context: induced / Reg
- Event dedup key: term | tomm40 | normalized variants:dna change | neuroinflammation hypothesis,oxidative stress hypothesis,mitochondrial autophagy hypothesis
- Long-tail signals: gene_alteration=TOMM40 / normalized variants:dna change (freq 1 <= threshold 1)
- Curation reasons: model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: When expressed in BV2 microglial cells, the AD-associated mutant (F113L) or (F131L) TOMM40 induced mitochondrial dysfunction and oxidative stress-induced activation of microglia and NLRP3 inflammasome.

### Evidence 4: PMID 36835494

- PubMed: https://pubmed.ncbi.nlm.nih.gov/36835494/
- Gene: TOMM40
- Journal/Year: Int J Mol Sci / 2023
- Phenotype: Mitochondrial Diseases
- Hypothesis: Neuroinflammation Hypothesis,Mitochondrial Autophagy Hypothesis
- Evidence type: model_or_intervention
- Candidate mechanism strata: mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis
- Alteration taxonomy: point mutations:mutations
- Gene-alteration: TOMM40 / point mutations:mutations
- Alteration mention: variation
- Alteration ID: point mutations:Mutations
- Trigger/regulation context: role / Reg
- Event dedup key: term | tomm40 | point mutations:mutations | neuroinflammation hypothesis,mitochondrial autophagy hypothesis
- Long-tail signals: hypothesis=Neuroinflammation Hypothesis,Mitochondrial Autophagy Hypothesis (freq 1 <= threshold 2)
- Curation reasons: model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: We further utilized cell models to examine the role of TOMM40 variation in mitochondrial dysfunction that causes microglial activation and neuroinflammation.

### Evidence 5: PMID 35252966

- PubMed: https://pubmed.ncbi.nlm.nih.gov/35252966/
- Gene: NEIL1
- Journal/Year: Front Aging / 2022
- Phenotype: Mitochondrial inheritance
- Hypothesis: Oxidative stress hypothesis,Mitochondrial autophagy hypothesis
- Evidence type: model_or_intervention
- Candidate mechanism strata: mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis
- Alteration taxonomy: genetic manipulation:knockout
- Gene-alteration: NEIL1 / genetic manipulation:knockout
- Alteration mention: Knockout
- Alteration ID: genetic manipulation:knockout
- Trigger/regulation context: results in / Reg
- Event dedup key: term | neil1 | genetic manipulation:knockout | oxidative stress hypothesis,mitochondrial autophagy hypothesis
- Long-tail signals: gene=NEIL1 (freq 1 <= threshold 1), gene_alteration=NEIL1 / genetic manipulation:knockout (freq 1 <= threshold 1)
- Curation reasons: model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: Knockout of mitochondrial OGG1 and NEIL1, which remove 8-oxo-dG and formamidopyrimidine lesions, respectively, in mice results in mitochondrial dysfunction and a metabolic syndrome phenotype.


## Interpretation Guide for the User Question

- Use the global statistics to describe how broadly this term is represented across genes and hypotheses.
- Use curated representative evidence to summarize molecular mechanisms instead of relying on raw API ranking.
- Treat candidate mechanism strata as LLM-assisted organization for expert review.
- Keep broad disease association evidence separate from molecular or model-based evidence.

## Follow-Up Research Priorities

- Use `--selected-limit` to request a larger displayed set from the server-side full-pool curation endpoint.
- `--curation-limit` only affects fallback mode when the server does not expose `/term/curation`.
- Review `data/curation.json` to filter by `EvidenceType`, `MechanismStrata`, `IsLongTailEvidence`, year, gene, phenotype, gene-alteration pair, or alteration taxonomy.
- Validate whether selected mechanisms are supported by original experiments, reviews, or curated interpretation fields.