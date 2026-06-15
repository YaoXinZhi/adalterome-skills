# AD-Alterome Deep Gene Report: MAPT

## Query Scope and Data Provenance

- Target gene: `MAPT`
- API base URL: `http://117.72.176.137/api/adalterome`
- Gene overview request: http://117.72.176.137/api/adalterome/gene/overview?gene=MAPT
- Curation evidence source: http://117.72.176.137/api/adalterome/gene/curation?gene=MAPT&selected_limit=5
- Curation package: `data/curation.json`

## Global Evidence Landscape

AD-Alterome contains 27822 event records for `MAPT` across 4480 PMID(s), 914 term(s), and 166 AD hypothesis field(s). Interpret this as curated sentence-level literature evidence rather than direct causal proof.

### Top overview terms

- Dementia (HPO): 1498
- Frontotemporal dementia (HPO): 1382
- protein (GO): 1235
- chromosome (GO): 1021
- Alzheimer Disease (MeSH): 966
- Parkinsonism (HPO): 830
- Tauopathies (MeSH): 746
- Pallidopontonigral Degeneration (MeSH): 486
- Neurodegeneration (HPO): 415
- Neurodegenerative Diseases (MeSH): 330

### Top overview hypotheses

- Tau Protein Hypothesis: 10796
- Amyloid Hypothesis,Tau Protein Hypothesis: 2610
- Tau Protein Hypothesis,Neuroinflammation Hypothesis: 775
- Tau Protein Hypothesis,Abnormal Autophagy Hypothesis: 402
- Tau Protein Hypothesis,Mitochondrial Autophagy Hypothesis: 351
- Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis: 271
- Tau Protein Hypothesis,Vascular Hypothesis: 198
- Tau Protein Hypothesis,Oxidative Stress Hypothesis: 196
- Amyloid Hypothesis: 189
- Amyloid Hypothesis,Tau Protein Hypothesis,Mitochondrial Autophagy Hypothesis: 157

## Evidence Curation Layer

- Raw API scoring fields are ignored in skill reports and curation decisions.
- Sentence-level evidence source: remote_api (server_full_query_pool).
- Curation pool rows: 27822; event-unique rows after query-specific deduplication: 8010.
- Overview event rows reported by the API: 27822.
- Event deduplication key: gene-fixed event key: alteration taxonomy + phenotype/term + hypothesis; fallback to PMID/sentence when structured fields are sparse.
- Unique PMIDs in curation pool: 3042; genes: 1; phenotypes: 897; alteration taxonomies: 28; gene-alteration pairs: 28.
- Long-tail rule: Query-specific frequency <= min(Q25, 10) after event-level deduplication across dimensions phenotype, gene_alteration, hypothesis; thresholds={'phenotype': 1, 'gene_alteration': 10, 'hypothesis': 2}.

### Dominant PMIDs

- 33255694: 24
- 26198711: 23
- 31907603: 22
- 34314701: 22
- 36845551: 19

### Top genes

- MAPT: 8010

### Top gene-alteration pairs

- MAPT / point mutations:mutations: 2445
- MAPT / normalized variants:dna change: 1932
- MAPT / structural variation:deletion: 516
- MAPT / expression changes:dysregulation: 460
- MAPT / epigenic changes:phosphorylation: 448

### Top phenotypes

- Alzheimer Disease: 109
- protein: 106
- Neurodegeneration: 81
- Dementia: 77
- phosphorylation: 69

### Dominant alteration taxonomy

- point mutations:mutations: 2445
- normalized variants:dna change: 1932
- structural variation:deletion: 516
- expression changes:dysregulation: 460
- epigenic changes:phosphorylation: 448

### Evidence type distribution

- alteration_evidence: 5409
- model_or_intervention: 2601

### Mechanism strata distribution

- amyloid/tau axis: 8010
- proteostasis/autophagy axis: 2996
- synaptic and neuronal dysfunction axis: 2909
- mitochondrial and oxidative stress axis: 1395
- neuroinflammation and microglia axis: 995

### Query-relative top and long-tail patterns

| Dimension | Top values | Long-tail values |
| --- | --- | --- |
| Phenotype | Neurodegeneration (81); phosphorylation (69); biosynthetic process (65); Nerve Degeneration (61); AD (58); Cognition Disorders (57); Tauopathies (56); hyperphosphorylation (56) | 101084670 (1); 10919 (1); 10922 (1); 11315 (1); 11596 (1); 117 (1); 12349 (1); 12569 (1) |
| Gene-alteration | MAPT / point mutations:mutations (2445); MAPT / normalized variants:dna change (1932); MAPT / structural variation:deletion (516); MAPT / expression changes:dysregulation (460); MAPT / epigenic changes:phosphorylation (448); MAPT / structural variation:chromosomal variation (332); MAPT / expression changes:underexpression (266); MAPT / genetic manipulation:gene aggregation (239) | MAPT / structural variation:frameshift (2) |
| Hypothesis | Tau Protein Hypothesis (2048); Tau protein hypothesis (831); Amyloid Hypothesis,Tau Protein Hypothesis (797); Tau Protein Hypothesis,Neuroinflammation Hypothesis (298); Tau Protein Hypothesis,Abnormal Autophagy Hypothesis (202); Tau Protein Hypothesis,Mitochondrial Autophagy Hypothesis (172); Amyloid hypothesis,Tau protein hypothesis (152); Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis (131) | Abnormal autophagy hypothesis,Amyloid hypothesis,Tau protein hypothesis (1); Abnormal autophagy hypothesis,Mitochondrial autophagy hypothesis (1); Amyloid Hypothesis,Glutamatergic Excitotoxicity Hypothesis (1); Amyloid hypothesis,Neuroinflammation hypothesis (1); Amyloid hypothesis,Oxidative stress hypothesis,Vascular hypothesis (1); Cholinergic Hypothesis,Glutamatergic Excitotoxicity Hypothesis (1); Cholinergic Hypothesis,Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis (1); Microbiota-Gut-Brain Axis hypothesis,Tau Protein Hypothesis (1) |

## Mechanism-Stratified Evidence Map

| Candidate mechanism stratum | Selected evidence rows | Representative PMIDs |
| --- | --- | --- |
| amyloid/tau axis | 5 | 32049030, 37727721, 28769871, 37092231, 36622561 |
| mitochondrial and oxidative stress axis | 2 | 32049030, 37727721 |
| neuroinflammation and microglia axis | 2 | 32049030, 37727721 |
| proteostasis/autophagy axis | 1 | 37092231 |
| synaptic and neuronal dysfunction axis | 1 | 32049030 |
| vascular/metabolic axis | 1 | 28769871 |

These strata are a curation aid for expert review. They should be refined by the LLM or user against the original sentences rather than treated as hard ontology labels.

## Representative Molecular and Pathological Evidence

| # | PMID | Gene | Phenotype | Evidence type | Mechanism strata | Sentence informativeness |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [32049030](https://pubmed.ncbi.nlm.nih.gov/32049030/) | MAPT | Ichthyosis follicularis atrichia photophobia syndrome | model_or_intervention | amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | 90.0 |
| 2 | [37727721](https://pubmed.ncbi.nlm.nih.gov/37727721/) | MAPT | catalytic activity | alteration_evidence | amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis | 90.0 |
| 3 | [28769871](https://pubmed.ncbi.nlm.nih.gov/28769871/) | MAPT | protein metabolic process | model_or_intervention | amyloid/tau axis; vascular/metabolic axis | 90.0 |
| 4 | [37092231](https://pubmed.ncbi.nlm.nih.gov/37092231/) | MAPT | progressive supranuclear palsy | alteration_evidence | amyloid/tau axis; proteostasis/autophagy axis | 90.0 |
| 5 | [36622561](https://pubmed.ncbi.nlm.nih.gov/36622561/) | MAPT | tau hyperphosphorylation | alteration_evidence | amyloid/tau axis | 90.0 |

## Long-Tail Evidence Signals

| # | PMID | Gene | Phenotype | Evidence type | Long-tail dimensions | Reasons |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [32049030](https://pubmed.ncbi.nlm.nih.gov/32049030/) | MAPT | Ichthyosis follicularis atrichia photophobia syndrome | model_or_intervention | phenotype=Ichthyosis follicularis atrichia photophobia syndrome (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 2 | [28769871](https://pubmed.ncbi.nlm.nih.gov/28769871/) | MAPT | protein metabolic process | model_or_intervention | phenotype=protein metabolic process (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 3 | [37727721](https://pubmed.ncbi.nlm.nih.gov/37727721/) | MAPT | catalytic activity | alteration_evidence | phenotype=catalytic activity (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 4 | [37092231](https://pubmed.ncbi.nlm.nih.gov/37092231/) | MAPT | progressive supranuclear palsy | alteration_evidence | phenotype=progressive supranuclear palsy (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 5 | [36622561](https://pubmed.ncbi.nlm.nih.gov/36622561/) | MAPT | tau hyperphosphorylation | alteration_evidence | phenotype=tau hyperphosphorylation (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 6 | [35985329](https://pubmed.ncbi.nlm.nih.gov/35985329/) | MAPT | fatty acid biosynthetic process | alteration_evidence | phenotype=fatty acid biosynthetic process (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 7 | [35985329](https://pubmed.ncbi.nlm.nih.gov/35985329/) | MAPT | Ventricular Dysfunction | alteration_evidence | phenotype=Ventricular Dysfunction (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 8 | [33494262](https://pubmed.ncbi.nlm.nih.gov/33494262/) | MAPT | Occasional | alteration_evidence | phenotype=Occasional (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 9 | [32184751](https://pubmed.ncbi.nlm.nih.gov/32184751/) | MAPT | acetylcholinesterase activity | alteration_evidence | phenotype=acetylcholinesterase activity (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 10 | [31585367](https://pubmed.ncbi.nlm.nih.gov/31585367/) | MAPT | Basal Laminar Drusen | alteration_evidence | phenotype=Basal Laminar Drusen (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 11 | [30590647](https://pubmed.ncbi.nlm.nih.gov/30590647/) | MAPT | retrograde axonal transport | alteration_evidence | phenotype=retrograde axonal transport (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 12 | [27242557](https://pubmed.ncbi.nlm.nih.gov/27242557/) | MAPT | cortical Lewy body | alteration_evidence | phenotype=cortical Lewy body (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 13 | [26139368](https://pubmed.ncbi.nlm.nih.gov/26139368/) | MAPT | U1 snRNP | alteration_evidence | phenotype=U1 snRNP (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 14 | [23727082](https://pubmed.ncbi.nlm.nih.gov/23727082/) | MAPT | Clinical course | alteration_evidence | phenotype=Clinical course (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 15 | [38994964](https://pubmed.ncbi.nlm.nih.gov/38994964/) | MAPT | myelin sheath | model_or_intervention | phenotype=myelin sheath (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 16 | [26697132](https://pubmed.ncbi.nlm.nih.gov/26697132/) | MAPT | gamma-secretase complex | model_or_intervention | phenotype=gamma-secretase complex (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 17 | [38930877](https://pubmed.ncbi.nlm.nih.gov/38930877/) | MAPT | corticobasal ganglionic degeneration | alteration_evidence | phenotype=corticobasal ganglionic degeneration (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 18 | [37131250](https://pubmed.ncbi.nlm.nih.gov/37131250/) | MAPT | protein self-association | alteration_evidence | phenotype=protein self-association (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 19 | [37730840](https://pubmed.ncbi.nlm.nih.gov/37730840/) | MAPT | impaired neuronal function | alteration_evidence | phenotype=impaired neuronal function (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 20 | [39757022](https://pubmed.ncbi.nlm.nih.gov/39757022/) | MAPT | synaptic injury | alteration_evidence | phenotype=synaptic injury (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, PMID-traceable |

## Chronological Evidence Trajectory

| Period | Event-unique rows | Dominant mechanism strata |
| --- | --- | --- |
| 2010-2014 | 872 | amyloid/tau axis (872); synaptic and neuronal dysfunction axis (271); proteostasis/autophagy axis (268); mitochondrial and oxidative stress axis (142); vascular/metabolic axis (44) |
| 2015-2019 | 2110 | amyloid/tau axis (2110); synaptic and neuronal dysfunction axis (744); proteostasis/autophagy axis (657); mitochondrial and oxidative stress axis (362); neuroinflammation and microglia axis (240) |
| 2020-2024 | 4221 | amyloid/tau axis (4221); proteostasis/autophagy axis (1793); synaptic and neuronal dysfunction axis (1601); mitochondrial and oxidative stress axis (778); neuroinflammation and microglia axis (659) |
| before 2010 | 361 | amyloid/tau axis (361); proteostasis/autophagy axis (140); synaptic and neuronal dysfunction axis (107); mitochondrial and oxidative stress axis (37); vascular/metabolic axis (22) |
| missing year | 446 | amyloid/tau axis (446); synaptic and neuronal dysfunction axis (186); proteostasis/autophagy axis (138); mitochondrial and oxidative stress axis (76); neuroinflammation and microglia axis (51) |

## Original Evidence Traces

### Evidence 1: PMID 32049030

- PubMed: https://pubmed.ncbi.nlm.nih.gov/32049030/
- Gene: MAPT
- Journal/Year: Cell Rep. 2020 Feb 11 / 2020
- Phenotype: Ichthyosis follicularis atrichia photophobia syndrome
- Hypothesis: Neuroinflammation Hypothesis
- Evidence type: model_or_intervention
- Candidate mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Alteration taxonomy: normalized variants:dna change
- Gene-alteration: MAPT / normalized variants:dna change
- Alteration mention: P301L
- Alteration ID: rs63751273
- Trigger/regulation context: upregulation / PosReg
- Event dedup key: gene | normalized variants:dna change | mesh:c536085 | neuroinflammation hypothesis
- Long-tail signals: phenotype=Ichthyosis follicularis atrichia photophobia syndrome (freq 1 <= threshold 1)
- Curation reasons: model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: We found that Gfap was dramatically upregulated across age groups (Figure 3A; likelihood ratio test [LRT] statistic = 106.321, FDR = 1.28E-18), similar to results from another study reporting age-dependent (12-18 months) upregulation of hippocampal Gfap in tau (CaMKII-MAPT P301L) and amyloid (APP/PSEN1) mouse models and paralleling the astrogliosis observed in human AD brain.

### Evidence 2: PMID 37727721

- PubMed: https://pubmed.ncbi.nlm.nih.gov/37727721/
- Gene: MAPT
- Journal/Year: World J Clin Cases / 2023
- Phenotype: catalytic activity
- Hypothesis: Tau Protein Hypothesis,Neuroinflammation Hypothesis,Oxidative Stress Hypothesis
- Evidence type: alteration_evidence
- Candidate mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis
- Alteration taxonomy: point mutations:mutations
- Gene-alteration: MAPT / point mutations:mutations
- Alteration mention: mutations
- Alteration ID: point mutations:Mutations
- Trigger/regulation context: Increased / PosReg
- Event dedup key: gene | point mutations:mutations | go:0003824 | tau protein hypothesis,neuroinflammation hypothesis,oxidative stress hypothesis
- Long-tail signals: phenotype=catalytic activity (freq 1 <= threshold 1)
- Curation reasons: alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: This occurs through the following mechanisms: Increased enzyme activity of Cdk5 or GSK-3beta, decreased PPA2, mutations associated with the MAPT gene, increased neuroinflammatory response, enhanced influx of intracellular Ca2+, and impairment of oxidative phosphorylation.

### Evidence 3: PMID 28769871

- PubMed: https://pubmed.ncbi.nlm.nih.gov/28769871/
- Gene: MAPT
- Journal/Year: Front Neurol / 2017
- Phenotype: protein metabolic process
- Hypothesis: Tau Protein Hypothesis
- Evidence type: model_or_intervention
- Candidate mechanism strata: amyloid/tau axis; vascular/metabolic axis
- Alteration taxonomy: genetic manipulation:knockout
- Gene-alteration: MAPT / genetic manipulation:knockout
- Alteration mention: knockout
- Alteration ID: genetic manipulation:knockout
- Trigger/regulation context: resulted in / Reg
- Event dedup key: gene | genetic manipulation:knockout | go:0019538 | tau protein hypothesis
- Long-tail signals: phenotype=protein metabolic process (freq 1 <= threshold 1)
- Curation reasons: model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable
- Original sentence: Recent studies have shown that conditional knockout of the Dicer gene in the mouse brain created an extensive miRNA deficiency, which resulted in abnormal Tau protein metabolism in mice with AD-like Tau hyperphosphorylation and aberrant splicing of MAPT.

### Evidence 4: PMID 37092231

- PubMed: https://pubmed.ncbi.nlm.nih.gov/37092231/
- Gene: MAPT
- Journal/Year: J Huntingtons Dis;2023; 12 (1) 1. doi:10.3233/JHD-230569 / 2023
- Phenotype: progressive supranuclear palsy
- Hypothesis: Tau Protein Hypothesis
- Evidence type: alteration_evidence
- Candidate mechanism strata: amyloid/tau axis; proteostasis/autophagy axis
- Alteration taxonomy: structural variation:chromosomal variation
- Gene-alteration: MAPT / structural variation:chromosomal variation
- Alteration mention: haplotype
- Alteration ID: -
- Trigger/regulation context: associated / Reg
- Event dedup key: gene | structural variation:chromosomal variation | mesh:d013494 | tau protein hypothesis
- Long-tail signals: phenotype=progressive supranuclear palsy (freq 1 <= threshold 1)
- Curation reasons: alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: Studies have shown that the MAPT haplotype can influence the development of neurodegenerative disorders: the H1 haplotype has been associated with progressive supranuclear palsy, corticobasal degeneration, and Alzheimer's disease (AD).

### Evidence 5: PMID 36622561

- PubMed: https://pubmed.ncbi.nlm.nih.gov/36622561/
- Gene: MAPT
- Journal/Year: Mol Neurobiol. 2023 Apr;60(4):2174-2185. doi: 10.1007/s12035-022-03190-x. Epub  / 2023
- Phenotype: tau hyperphosphorylation
- Hypothesis: Tau Protein Hypothesis
- Evidence type: alteration_evidence
- Candidate mechanism strata: amyloid/tau axis
- Alteration taxonomy: point mutations:mutations
- Gene-alteration: MAPT / point mutations:mutations
- Alteration mention: mutations
- Alteration ID: point mutations:Mutations
- Trigger/regulation context: result from / Reg
- Event dedup key: gene | point mutations:mutations | mesh:c536599 | tau protein hypothesis
- Long-tail signals: phenotype=tau hyperphosphorylation (freq 1 <= threshold 1)
- Curation reasons: alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence: Tauopathies are traditionally defined as a group of conditions that result from tau hyperphosphorylation, abnormal tau splicing, or mutations in the microtubule-associated protein tau (MAPT) gene.


## Interpretation Guide for the User Question

- Use the global statistics to describe coverage and dominant literature patterns.
- Use curated representative evidence, not raw API ranking, to summarize molecular pathology.
- Keep original sentences and PubMed links attached to every mechanistic claim.
- Treat candidate mechanism strata as LLM-assisted organization for expert review, not as final labels.
- Genetic alteration interpretation should rely on `AlterationType`, `AlterationMention`, and `AlterationID`; `TriggerWord` and `RegType` are event relation context, not genetic alteration labels.

## Follow-Up Analysis Suggestions

- Use `--selected-limit` to request a larger displayed set from the server-side full-pool curation endpoint.
- `--curation-limit` only affects fallback mode when the server does not expose `/gene/curation`.
- Review `data/curation.json` to filter by `EvidenceType`, `MechanismStrata`, `IsLongTailEvidence`, year, PMID, phenotype, gene-alteration pair, or alteration taxonomy.
- Add external enrichment from official sources only as a separate section.