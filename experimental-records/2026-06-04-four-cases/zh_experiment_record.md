## 案例一：单基因查询

### 自然语言输入

请使用 adalterome-gene-report 查询 MAPT 单基因，使用 full-pool curation，selected-limit=5，用中文输出完整报告。

### 完整输出

# AD-Alterome 深度单基因报告：MAPT

## 查询范围与数据来源

- 目标基因：`MAPT`
- API base URL：`http://117.72.176.137/api/adalterome`
- Gene overview request：`http://117.72.176.137/api/adalterome/gene/overview?gene=MAPT`
- Curation evidence source：`http://117.72.176.137/api/adalterome/gene/curation?gene=MAPT&selected_limit=5`
- Curation package：`data/curation.json`

## 全局证据景观

AD-Alterome 中与 `MAPT` 相关的事件记录共有 27822 条，覆盖 4480 个 PMID、914 个 term、166 个 AD hypothesis 字段。这些记录应解释为经过整理的句子级文献证据，而不是直接因果证明。

### Top overview terms

- Dementia (HPO)：1498
- Frontotemporal dementia (HPO)：1382
- protein (GO)：1235
- chromosome (GO)：1021
- Alzheimer Disease (MeSH)：966
- Parkinsonism (HPO)：830
- Tauopathies (MeSH)：746
- Pallidopontonigral Degeneration (MeSH)：486
- Neurodegeneration (HPO)：415
- Neurodegenerative Diseases (MeSH)：330

### Top overview hypotheses

- Tau Protein Hypothesis：10796
- Amyloid Hypothesis,Tau Protein Hypothesis：2610
- Tau Protein Hypothesis,Neuroinflammation Hypothesis：775
- Tau Protein Hypothesis,Abnormal Autophagy Hypothesis：402
- Tau Protein Hypothesis,Mitochondrial Autophagy Hypothesis：351
- Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis：271
- Tau Protein Hypothesis,Vascular Hypothesis：198
- Tau Protein Hypothesis,Oxidative Stress Hypothesis：196
- Amyloid Hypothesis：189
- Amyloid Hypothesis,Tau Protein Hypothesis,Mitochondrial Autophagy Hypothesis：157

## 证据中间层

- skills 报告不使用也不展示 raw API scoring fields。
- 句子级证据来源：remote_api (`server_full_query_pool`)。
- Curation pool rows：27822；按 query-specific event key 去重后 event-unique rows：8010。
- API overview reported event rows：27822。
- Event deduplication key：gene-fixed event key，即 alteration taxonomy + phenotype/term + hypothesis；结构字段稀疏时回退到 PMID/sentence。
- Curation pool 中 unique PMIDs：3042；genes：1；phenotypes：897；alteration taxonomies：28；gene-alteration pairs：28。
- Long-tail 规则：在 event-level deduplication 后，对 phenotype、gene_alteration、hypothesis 等维度按 query-specific frequency 判断，阈值为 `{'phenotype': 1, 'gene_alteration': 10, 'hypothesis': 2}`。

### Dominant PMIDs

- 33255694：24
- 26198711：23
- 31907603：22
- 34314701：22
- 36845551：19

### Top genes

- MAPT：8010

### Top gene-alteration pairs

- MAPT / point mutations:mutations：2445
- MAPT / normalized variants:dna change：1932
- MAPT / structural variation:deletion：516
- MAPT / expression changes:dysregulation：460
- MAPT / epigenic changes:phosphorylation：448

### Top phenotypes

- Alzheimer Disease：109
- protein：106
- Neurodegeneration：81
- Dementia：77
- phosphorylation：69

### Dominant alteration taxonomy

- point mutations:mutations：2445
- normalized variants:dna change：1932
- structural variation:deletion：516
- expression changes:dysregulation：460
- epigenic changes:phosphorylation：448

### Evidence type distribution

- alteration_evidence：5409
- model_or_intervention：2601

### Mechanism strata distribution

- amyloid/tau axis：8010
- proteostasis/autophagy axis：2996
- synaptic and neuronal dysfunction axis：2909
- mitochondrial and oxidative stress axis：1395
- neuroinflammation and microglia axis：995

### Query-relative top 与 long-tail patterns

| 维度 | Top values | Long-tail values |
| --- | --- | --- |
| Phenotype | Neurodegeneration (81); phosphorylation (69); biosynthetic process (65); Nerve Degeneration (61); AD (58); Cognition Disorders (57); Tauopathies (56); hyperphosphorylation (56) | 101084670 (1); 10919 (1); 10922 (1); 11315 (1); 11596 (1); 117 (1); 12349 (1); 12569 (1) |
| Gene-alteration | MAPT / point mutations:mutations (2445); MAPT / normalized variants:dna change (1932); MAPT / structural variation:deletion (516); MAPT / expression changes:dysregulation (460); MAPT / epigenic changes:phosphorylation (448); MAPT / structural variation:chromosomal variation (332); MAPT / expression changes:underexpression (266); MAPT / genetic manipulation:gene aggregation (239) | MAPT / structural variation:frameshift (2) |
| Hypothesis | Tau Protein Hypothesis (2048); Tau protein hypothesis (831); Amyloid Hypothesis,Tau Protein Hypothesis (797); Tau Protein Hypothesis,Neuroinflammation Hypothesis (298); Tau Protein Hypothesis,Abnormal Autophagy Hypothesis (202); Tau Protein Hypothesis,Mitochondrial Autophagy Hypothesis (172); Amyloid hypothesis,Tau protein hypothesis (152); Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis (131) | Abnormal autophagy hypothesis,Amyloid hypothesis,Tau protein hypothesis (1); Abnormal autophagy hypothesis,Mitochondrial autophagy hypothesis (1); Amyloid Hypothesis,Glutamatergic Excitotoxicity Hypothesis (1); Amyloid hypothesis,Neuroinflammation hypothesis (1); Amyloid hypothesis,Oxidative stress hypothesis,Vascular hypothesis (1); Cholinergic Hypothesis,Glutamatergic Excitotoxicity Hypothesis (1); Cholinergic Hypothesis,Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis (1); Microbiota-Gut-Brain Axis hypothesis,Tau Protein Hypothesis (1) |

## 机制分层证据图

| Candidate mechanism stratum | Selected evidence rows | Representative PMIDs |
| --- | --- | --- |
| amyloid/tau axis | 5 | 32049030, 37727721, 28769871, 37092231, 36622561 |
| mitochondrial and oxidative stress axis | 2 | 32049030, 37727721 |
| neuroinflammation and microglia axis | 2 | 32049030, 37727721 |
| proteostasis/autophagy axis | 1 | 37092231 |
| synaptic and neuronal dysfunction axis | 1 | 32049030 |
| vascular/metabolic axis | 1 | 28769871 |

这些 strata 是专家复核和 LLM 辅助组织的中间层，不应被当作最终 ontology 标签。

## 代表性分子与病理证据

| # | PMID | Gene | Phenotype | Evidence type | Mechanism strata | Sentence informativeness |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [32049030](https://pubmed.ncbi.nlm.nih.gov/32049030/) | MAPT | Ichthyosis follicularis atrichia photophobia syndrome | model_or_intervention | amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis | 90.0 |
| 2 | [37727721](https://pubmed.ncbi.nlm.nih.gov/37727721/) | MAPT | catalytic activity | alteration_evidence | amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis | 90.0 |
| 3 | [28769871](https://pubmed.ncbi.nlm.nih.gov/28769871/) | MAPT | protein metabolic process | model_or_intervention | amyloid/tau axis; vascular/metabolic axis | 90.0 |
| 4 | [37092231](https://pubmed.ncbi.nlm.nih.gov/37092231/) | MAPT | progressive supranuclear palsy | alteration_evidence | amyloid/tau axis; proteostasis/autophagy axis | 90.0 |
| 5 | [36622561](https://pubmed.ncbi.nlm.nih.gov/36622561/) | MAPT | tau hyperphosphorylation | alteration_evidence | amyloid/tau axis | 90.0 |

## Long-tail evidence signals

| # | PMID | Gene | Phenotype | Evidence type | Long-tail dimensions | Reasons |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [32049030](https://pubmed.ncbi.nlm.nih.gov/32049030/) | MAPT | Ichthyosis follicularis atrichia photophobia syndrome | model_or_intervention | phenotype=Ichthyosis follicularis atrichia photophobia syndrome (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 2 | [28769871](https://pubmed.ncbi.nlm.nih.gov/28769871/) | MAPT | protein metabolic process | model_or_intervention | phenotype=protein metabolic process (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable |
| 3 | [37727721](https://pubmed.ncbi.nlm.nih.gov/37727721/) | MAPT | catalytic activity | alteration_evidence | phenotype=catalytic activity (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 4 | [37092231](https://pubmed.ncbi.nlm.nih.gov/37092231/) | MAPT | progressive supranuclear palsy | alteration_evidence | phenotype=progressive supranuclear palsy (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 5 | [36622561](https://pubmed.ncbi.nlm.nih.gov/36622561/) | MAPT | tau hyperphosphorylation | alteration_evidence | phenotype=tau hyperphosphorylation (1) | alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |

## 时间序列证据轨迹

| Period | Event-unique rows | Dominant mechanism strata |
| --- | --- | --- |
| 2010-2014 | 872 | amyloid/tau axis (872); synaptic and neuronal dysfunction axis (271); proteostasis/autophagy axis (268); mitochondrial and oxidative stress axis (142); vascular/metabolic axis (44) |
| 2015-2019 | 2110 | amyloid/tau axis (2110); synaptic and neuronal dysfunction axis (744); proteostasis/autophagy axis (657); mitochondrial and oxidative stress axis (362); neuroinflammation and microglia axis (240) |
| 2020-2024 | 4221 | amyloid/tau axis (4221); proteostasis/autophagy axis (1793); synaptic and neuronal dysfunction axis (1601); mitochondrial and oxidative stress axis (778); neuroinflammation and microglia axis (659) |
| before 2010 | 361 | amyloid/tau axis (361); proteostasis/autophagy axis (140); synaptic and neuronal dysfunction axis (107); mitochondrial and oxidative stress axis (37); vascular/metabolic axis (22) |
| missing year | 446 | amyloid/tau axis (446); synaptic and neuronal dysfunction axis (186); proteostasis/autophagy axis (138); mitochondrial and oxidative stress axis (76); neuroinflammation and microglia axis (51) |

## 原始证据追踪

### Evidence 1：PMID 32049030

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/32049030/`
- Gene：MAPT
- Journal/Year：Cell Rep. 2020 Feb 11 / 2020
- Phenotype：Ichthyosis follicularis atrichia photophobia syndrome
- Hypothesis：Neuroinflammation Hypothesis
- Evidence type：model_or_intervention
- Candidate mechanism strata：amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis
- Alteration taxonomy：normalized variants:dna change
- Gene-alteration：MAPT / normalized variants:dna change
- Alteration mention：P301L
- Alteration ID：rs63751273
- Trigger/regulation context：upregulation / PosReg
- Event dedup key：gene | normalized variants:dna change | mesh:c536085 | neuroinflammation hypothesis
- Long-tail signals：phenotype=Ichthyosis follicularis atrichia photophobia syndrome (freq 1 <= threshold 1)
- Curation reasons：model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：We found that Gfap was dramatically upregulated across age groups (Figure 3A; likelihood ratio test [LRT] statistic = 106.321, FDR = 1.28E-18), similar to results from another study reporting age-dependent (12-18 months) upregulation of hippocampal Gfap in tau (CaMKII-MAPT P301L) and amyloid (APP/PSEN1) mouse models and paralleling the astrogliosis observed in human AD brain.

### Evidence 2：PMID 37727721

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/37727721/`
- Gene：MAPT
- Journal/Year：World J Clin Cases / 2023
- Phenotype：catalytic activity
- Hypothesis：Tau Protein Hypothesis,Neuroinflammation Hypothesis,Oxidative Stress Hypothesis
- Evidence type：alteration_evidence
- Candidate mechanism strata：amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis
- Alteration taxonomy：point mutations:mutations
- Gene-alteration：MAPT / point mutations:mutations
- Alteration mention：mutations
- Alteration ID：point mutations:Mutations
- Trigger/regulation context：Increased / PosReg
- Event dedup key：gene | point mutations:mutations | go:0003824 | tau protein hypothesis,neuroinflammation hypothesis,oxidative stress hypothesis
- Long-tail signals：phenotype=catalytic activity (freq 1 <= threshold 1)
- Curation reasons：alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：This occurs through the following mechanisms: Increased enzyme activity of Cdk5 or GSK-3beta, decreased PPA2, mutations associated with the MAPT gene, increased neuroinflammatory response, enhanced influx of intracellular Ca2+, and impairment of oxidative phosphorylation.

### Evidence 3：PMID 28769871

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/28769871/`
- Gene：MAPT
- Journal/Year：Front Neurol / 2017
- Phenotype：protein metabolic process
- Hypothesis：Tau Protein Hypothesis
- Evidence type：model_or_intervention
- Candidate mechanism strata：amyloid/tau axis; vascular/metabolic axis
- Alteration taxonomy：genetic manipulation:knockout
- Gene-alteration：MAPT / genetic manipulation:knockout
- Alteration mention：knockout
- Alteration ID：genetic manipulation:knockout
- Trigger/regulation context：resulted in / Reg
- Event dedup key：gene | genetic manipulation:knockout | go:0019538 | tau protein hypothesis
- Long-tail signals：phenotype=protein metabolic process (freq 1 <= threshold 1)
- Curation reasons：model_or_intervention, high sentence informativeness, long-tail evidence signal, PMID-traceable
- Original sentence：Recent studies have shown that conditional knockout of the Dicer gene in the mouse brain created an extensive miRNA deficiency, which resulted in abnormal Tau protein metabolism in mice with AD-like Tau hyperphosphorylation and aberrant splicing of MAPT.

### Evidence 4：PMID 37092231

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/37092231/`
- Gene：MAPT
- Journal/Year：J Huntingtons Dis;2023; 12 (1) 1. doi:10.3233/JHD-230569 / 2023
- Phenotype：progressive supranuclear palsy
- Hypothesis：Tau Protein Hypothesis
- Evidence type：alteration_evidence
- Candidate mechanism strata：amyloid/tau axis; proteostasis/autophagy axis
- Alteration taxonomy：structural variation:chromosomal variation
- Gene-alteration：MAPT / structural variation:chromosomal variation
- Alteration mention：haplotype
- Alteration ID：-
- Trigger/regulation context：associated / Reg
- Event dedup key：gene | structural variation:chromosomal variation | mesh:d013494 | tau protein hypothesis
- Long-tail signals：phenotype=progressive supranuclear palsy (freq 1 <= threshold 1)
- Curation reasons：alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：Studies have shown that the MAPT haplotype can influence the development of neurodegenerative disorders: the H1 haplotype has been associated with progressive supranuclear palsy, corticobasal degeneration, and Alzheimer's disease (AD).

### Evidence 5：PMID 36622561

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/36622561/`
- Gene：MAPT
- Journal/Year：Mol Neurobiol. 2023 Apr;60(4):2174-2185. doi: 10.1007/s12035-022-03190-x. Epub / 2023
- Phenotype：tau hyperphosphorylation
- Hypothesis：Tau Protein Hypothesis
- Evidence type：alteration_evidence
- Candidate mechanism strata：amyloid/tau axis
- Alteration taxonomy：point mutations:mutations
- Gene-alteration：MAPT / point mutations:mutations
- Alteration mention：mutations
- Alteration ID：point mutations:Mutations
- Trigger/regulation context：result from / Reg
- Event dedup key：gene | point mutations:mutations | mesh:c536599 | tau protein hypothesis
- Long-tail signals：phenotype=tau hyperphosphorylation (freq 1 <= threshold 1)
- Curation reasons：alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：Tauopathies are traditionally defined as a group of conditions that result from tau hyperphosphorylation, abnormal tau splicing, or mutations in the microtubule-associated protein tau (MAPT) gene.

## 用户问题解释指南

- 全局统计用于描述覆盖度和主导文献模式。
- 分子病理总结应优先依据 curated representative evidence，而不是 raw API ranking。
- 每个机制判断都应保留 original sentence 和 PubMed 链接。
- Candidate mechanism strata 是专家复核辅助，不是最终标签。
- Genetic alteration 解释应基于 `AlterationType`、`AlterationMention`、`AlterationID`；`TriggerWord` 与 `RegType` 是事件关系上下文，不是 genetic alteration 标签。

## 后续分析建议

- 如需展示更多代表证据，可增加 `--selected-limit`。
- `--curation-limit` 仅在服务器不暴露 `/gene/curation` 时影响 fallback mode。
- 可在 `data/curation.json` 中按 `EvidenceType`、`MechanismStrata`、`IsLongTailEvidence`、year、PMID、phenotype、gene-alteration pair 或 alteration taxonomy 过滤。
- 外部数据库补充应作为单独模块加入。

## 案例二：单表型查询

### 自然语言输入

请使用 adalterome-term-report 查询 mitochondrial dysfunction 单表型，使用 full-pool curation，selected-limit=5，用中文输出完整报告。

### 完整输出

# AD-Alterome 单表型报告：mitochondrial dysfunction

## 查询范围与数据来源

- 目标 term：`mitochondrial dysfunction`
- API base URL：`http://117.72.176.137/api/adalterome`
- Overview request：`http://117.72.176.137/api/adalterome/term/overview?term=mitochondrial+dysfunction`
- Curation evidence source：`http://117.72.176.137/api/adalterome/term/curation?term=mitochondrial+dysfunction&selected_limit=5`
- Curation package：`data/curation.json`

## 全局证据景观

AD-Alterome 将 `mitochondrial dysfunction` 关联到 925 条 event records、427 个 PMID、219 个 gene、43 个 AD hypothesis 字段。该结果应被理解为文献证据地图，而不是单一因果结论。

### Top genes

- PINK1：73
- SOD1：66
- MAPT：65
- LRRK2：51
- PARK7：46
- SNCA：44
- APP：32
- HTT：28
- PRKN：27
- APOE：19

### Top hypotheses

- Mitochondrial autophagy hypothesis：93
- Oxidative stress hypothesis,Mitochondrial autophagy hypothesis：61
- Amyloid Hypothesis,Mitochondrial Autophagy Hypothesis：41
- Tau Protein Hypothesis,Mitochondrial Autophagy Hypothesis：36
- Amyloid Hypothesis,Tau Protein Hypothesis,Mitochondrial Autophagy Hypothesis：19
- Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis,Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis：14
- Neuroinflammation Hypothesis,Mitochondrial autophagy hypothesis：13
- Amyloid Hypothesis,Tau Protein Hypothesis,Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis：13
- Amyloid hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis：11
- Abnormal Autophagy Hypothesis,Mitochondrial Autophagy Hypothesis：11

## 证据中间层

- skills 报告不使用也不展示 raw API scoring fields。
- 句子级证据来源：remote_api (`server_full_query_pool`)。
- Curation pool rows：925；按 query-specific event key 去重后 event-unique rows：440。
- API overview reported event rows：925。
- Event deduplication key：term-fixed event key，即 gene + alteration taxonomy + hypothesis；结构字段稀疏时回退到 PMID/sentence。
- Curation pool 中 unique PMIDs：305；genes：219；phenotypes：9；alteration taxonomies：19；gene-alteration pairs：340。
- Long-tail 规则：在 event-level deduplication 后，对 gene、gene_alteration、phenotype、hypothesis 等维度按 query-specific frequency 判断，阈值为 `{'gene': 1, 'gene_alteration': 1, 'phenotype': 1, 'hypothesis': 2}`。

### Dominant PMIDs

- 35892559：7
- 37240173：6
- 34177463：6
- 37489441：4
- 35821838：4

### Top genes

- MAPT：33
- PINK1：15
- APP：15
- SNCA：13
- APOE：12

### Top gene-alteration pairs

- APP / point mutations:mutations：8
- MAPT / normalized variants:dna change：8
- PSEN1 / point mutations:mutations：7
- MAPT / point mutations:mutations：7
- APOE / point mutations:mutations：7

### Top phenotypes

- Mitochondrial Diseases：258
- Mitochondrial inheritance：123
- Abnormality of mitochondrial metabolism：49
- Parkinson Disease, Mitochondrial：2
- mitochondrial dysfunctions：2

### Dominant alteration taxonomy

- point mutations:mutations：161
- structural variation:deletion：66
- expression changes:underexpression：38
- expression changes:dysregulation：36
- normalized variants:dna change：29

### Evidence type distribution

- alteration_evidence：325
- model_or_intervention：115

### Mechanism strata distribution

- mitochondrial and oxidative stress axis：440
- amyloid/tau axis：304
- proteostasis/autophagy axis：272
- synaptic and neuronal dysfunction axis：126
- vascular/metabolic axis：63

### Query-relative top 与 long-tail patterns

| 维度 | Top values | Long-tail values |
| --- | --- | --- |
| Gene | MAPT (33); PINK1 (15); APP (15); SNCA (13); APOE (12); SOD1 (10); PSEN1 (9); HTT (9) | ABCA7 (1); ABCB8 (1); ABCD1 (1); ABL1 (1); AFG3L2 (1); AKT1 (1); ALKBH1 (1); alpha-synuclein (1) |
| Gene-alteration | APP / point mutations:mutations (8); MAPT / normalized variants:dna change (8); PSEN1 / point mutations:mutations (7); MAPT / point mutations:mutations (7); APOE / point mutations:mutations (7); SNCA / point mutations:mutations (5); HTT / point mutations:mutations (5); MAPT / genetic manipulation:gene aggregation (5) | ABCA7 / structural variation:deletion (1); ABCB8 / point mutations:mutations (1); ABCD1 / point mutations:mutations (1); ABL1 / expression changes:inactivation (1); AFG3L2 / expression changes:dysregulation (1); AKT1 / expression changes:underexpression (1); ALKBH1 / genetic manipulation:knockout (1); alpha-synuclein / structural variation:chromosomal variation (1) |
| Phenotype | Mitochondrial Diseases (258); Mitochondrial inheritance (123); Abnormality of mitochondrial metabolism (49); Mitochondrial dysfunction (3); Parkinson Disease, Mitochondrial (2); mitochondrial dysfunctions (2); Hyperglycemia (1); Progressive (1) | Brain Diseases, Metabolic (1); Hyperglycemia (1); Progressive (1) |
| Hypothesis | Mitochondrial autophagy hypothesis (35); Mitochondrial Autophagy Hypothesis (34); Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis (25); Oxidative stress hypothesis,Mitochondrial autophagy hypothesis (22); Amyloid Hypothesis,Mitochondrial Autophagy Hypothesis (15); Tau Protein Hypothesis,Mitochondrial Autophagy Hypothesis (10); Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis,Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis (7); Amyloid Hypothesis,Tau Protein Hypothesis,Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis (6) | Glutamatergic excitotoxicity hypothesis (1); Neuroinflammation Hypothesis,Mitochondrial Autophagy Hypothesis (1); Neuroinflammation hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis (1); Neuroinflammation hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis,Vascular hypothesis (1); Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis,Glutamatergic Excitotoxicity Hypothesis (1); Tau Protein Hypothesis,Amyloid Hypothesis,Oxidative Stress Hypothesis,Neuroinflammation Hypothesis,Mitochondrial Autophagy Hypothesis (1); Tau Protein Hypothesis,Neuroinflammation Hypothesis,Mitochondrial Autophagy Hypothesis (1); Tau Protein Hypothesis,Oxidative Stress Hypothesis (1) |

## 机制分层证据图

| Candidate mechanism stratum | Selected evidence rows | Representative genes |
| --- | --- | --- |
| mitochondrial and oxidative stress axis | 5 | LDLR, PTN, TOMM40, NEIL1 |
| neuroinflammation and microglia axis | 4 | LDLR, PTN, TOMM40 |
| proteostasis/autophagy axis | 5 | LDLR, PTN, TOMM40, NEIL1 |
| synaptic and neuronal dysfunction axis | 1 | LDLR |
| vascular/metabolic axis | 3 | LDLR, PTN, NEIL1 |

这些 strata 用于组织分子与病理机制，供专家复核；它们不是硬性 ontology 标签。

## 代表性分子与病理证据

| # | PMID | Gene | Phenotype | Evidence type | Mechanism strata | Sentence informativeness |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [38056504](https://pubmed.ncbi.nlm.nih.gov/38056504/) | LDLR | Mitochondrial Diseases | model_or_intervention | mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis; proteostasis/autophagy axis | 90.0 |
| 2 | [37484951](https://pubmed.ncbi.nlm.nih.gov/37484951/) | PTN | Mitochondrial Diseases | alteration_evidence | mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; vascular/metabolic axis; proteostasis/autophagy axis | 90.0 |
| 3 | [36835494](https://pubmed.ncbi.nlm.nih.gov/36835494/) | TOMM40 | Mitochondrial inheritance | model_or_intervention | mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis | 90.0 |
| 4 | [36835494](https://pubmed.ncbi.nlm.nih.gov/36835494/) | TOMM40 | Mitochondrial Diseases | model_or_intervention | mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis | 90.0 |
| 5 | [35252966](https://pubmed.ncbi.nlm.nih.gov/35252966/) | NEIL1 | Mitochondrial inheritance | model_or_intervention | mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis | 90.0 |

## Long-tail evidence signals

| # | PMID | Gene | Phenotype | Evidence type | Long-tail dimensions | Reasons |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [38056504](https://pubmed.ncbi.nlm.nih.gov/38056504/) | LDLR | Mitochondrial Diseases | model_or_intervention | hypothesis=Neuroinflammation hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis,Vascular hypothesis (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 2 | [36835494](https://pubmed.ncbi.nlm.nih.gov/36835494/) | TOMM40 | Mitochondrial inheritance | model_or_intervention | gene_alteration=TOMM40 / normalized variants:dna change (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 3 | [36835494](https://pubmed.ncbi.nlm.nih.gov/36835494/) | TOMM40 | Mitochondrial Diseases | model_or_intervention | hypothesis=Neuroinflammation Hypothesis,Mitochondrial Autophagy Hypothesis (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 4 | [36231104](https://pubmed.ncbi.nlm.nih.gov/36231104/) | FRMD6 | Mitochondrial Diseases | model_or_intervention | gene=FRMD6 (1); gene_alteration=FRMD6 / genetic manipulation:knockout (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 5 | [35252966](https://pubmed.ncbi.nlm.nih.gov/35252966/) | NEIL1 | Mitochondrial inheritance | model_or_intervention | gene=NEIL1 (1); gene_alteration=NEIL1 / genetic manipulation:knockout (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |

## 时间序列证据轨迹

| Period | Event-unique rows | Dominant mechanism strata |
| --- | --- | --- |
| 2010-2014 | 46 | mitochondrial and oxidative stress axis (46); proteostasis/autophagy axis (33); amyloid/tau axis (27); synaptic and neuronal dysfunction axis (11); vascular/metabolic axis (10) |
| 2015-2019 | 111 | mitochondrial and oxidative stress axis (111); amyloid/tau axis (79); proteostasis/autophagy axis (78); synaptic and neuronal dysfunction axis (33); vascular/metabolic axis (18) |
| 2020-2024 | 230 | mitochondrial and oxidative stress axis (230); amyloid/tau axis (168); proteostasis/autophagy axis (129); synaptic and neuronal dysfunction axis (68); vascular/metabolic axis (31) |
| before 2010 | 6 | mitochondrial and oxidative stress axis (6); amyloid/tau axis (4); proteostasis/autophagy axis (3); vascular/metabolic axis (2); synaptic and neuronal dysfunction axis (2) |
| missing year | 47 | mitochondrial and oxidative stress axis (47); proteostasis/autophagy axis (29); amyloid/tau axis (26); synaptic and neuronal dysfunction axis (12); neuroinflammation and microglia axis (3) |

## 原始证据追踪

### Evidence 1：PMID 38056504

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/38056504/`
- Gene：LDLR
- Journal/Year：Ageing Res Rev / 2023
- Phenotype：Mitochondrial Diseases
- Hypothesis：Neuroinflammation hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis,Vascular hypothesis
- Evidence type：model_or_intervention
- Candidate mechanism strata：mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis; proteostasis/autophagy axis
- Alteration taxonomy：genetic manipulation:knockout
- Gene-alteration：LDLR / genetic manipulation:knockout
- Alteration mention：knockout
- Alteration ID：genetic manipulation:knockout
- Trigger/regulation context：associated / Reg
- Event dedup key：term | ldlr | genetic manipulation:knockout | neuroinflammation hypothesis,oxidative stress hypothesis,mitochondrial autophagy hypothesis,vascular hypothesis
- Long-tail signals：hypothesis=Neuroinflammation hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis,Vascular hypothesis (freq 1 <= threshold 2)
- Curation reasons：model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：Cognitive and emotional behavioral impairments in LDL receptor knockout (LDLr-/-) mice are associated with neuroinflammation, blood-brain barrier dysfunction, impaired neurogenesis, brain oxidative stress, and mitochondrial dysfunction.

### Evidence 2：PMID 37484951

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/37484951/`
- Gene：PTN
- Journal/Year：Front Endocrinol (Lausanne) / 2023
- Phenotype：Mitochondrial Diseases
- Hypothesis：Neuroinflammation hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis
- Evidence type：alteration_evidence
- Candidate mechanism strata：mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; vascular/metabolic axis; proteostasis/autophagy axis
- Alteration taxonomy：structural variation:deletion
- Gene-alteration：PTN / structural variation:deletion
- Alteration mention：deletion
- Alteration ID：structural variation:deletion
- Trigger/regulation context：protects / PosReg
- Event dedup key：term | ptn | structural variation:deletion | neuroinflammation hypothesis,oxidative stress hypothesis,mitochondrial autophagy hypothesis
- Long-tail signals：gene=PTN (freq 1 <= threshold 1), gene_alteration=PTN / structural variation:deletion (freq 1 <= threshold 1), hypothesis=Neuroinflammation hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis (freq 1 <= threshold 2)
- Curation reasons：alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：Moreover, recent reports have evidenced that PTN is implicated in the regulation of peripheral metainflammation, metabolic homeostasis, thermogenesis, as well as insulin sensitivity in the peripheral tissues Furthermore, Ptn deletion protects against neuroinflammation, mitochondrial dysfunction, and aberrant protein aggregation in a high fat diet (HFD) induced obesity model.

### Evidence 3：PMID 36835494

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/36835494/`
- Gene：TOMM40
- Journal/Year：Int J Mol Sci / 2023
- Phenotype：Mitochondrial inheritance
- Hypothesis：Neuroinflammation Hypothesis,Oxidative Stress Hypothesis,Mitochondrial Autophagy Hypothesis
- Evidence type：model_or_intervention
- Candidate mechanism strata：mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis
- Alteration taxonomy：normalized variants:dna change
- Gene-alteration：TOMM40 / normalized variants:dna change
- Alteration mention：F113L
- Alteration ID：rs157581
- Trigger/regulation context：induced / Reg
- Event dedup key：term | tomm40 | normalized variants:dna change | neuroinflammation hypothesis,oxidative stress hypothesis,mitochondrial autophagy hypothesis
- Long-tail signals：gene_alteration=TOMM40 / normalized variants:dna change (freq 1 <= threshold 1)
- Curation reasons：model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：When expressed in BV2 microglial cells, the AD-associated mutant (F113L) or (F131L) TOMM40 induced mitochondrial dysfunction and oxidative stress-induced activation of microglia and NLRP3 inflammasome.

### Evidence 4：PMID 36835494

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/36835494/`
- Gene：TOMM40
- Journal/Year：Int J Mol Sci / 2023
- Phenotype：Mitochondrial Diseases
- Hypothesis：Neuroinflammation Hypothesis,Mitochondrial Autophagy Hypothesis
- Evidence type：model_or_intervention
- Candidate mechanism strata：mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis
- Alteration taxonomy：point mutations:mutations
- Gene-alteration：TOMM40 / point mutations:mutations
- Alteration mention：variation
- Alteration ID：point mutations:Mutations
- Trigger/regulation context：role / Reg
- Event dedup key：term | tomm40 | point mutations:mutations | neuroinflammation hypothesis,mitochondrial autophagy hypothesis
- Long-tail signals：hypothesis=Neuroinflammation Hypothesis,Mitochondrial Autophagy Hypothesis (freq 1 <= threshold 2)
- Curation reasons：model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：We further utilized cell models to examine the role of TOMM40 variation in mitochondrial dysfunction that causes microglial activation and neuroinflammation.

### Evidence 5：PMID 35252966

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/35252966/`
- Gene：NEIL1
- Journal/Year：Front Aging / 2022
- Phenotype：Mitochondrial inheritance
- Hypothesis：Oxidative stress hypothesis,Mitochondrial autophagy hypothesis
- Evidence type：model_or_intervention
- Candidate mechanism strata：mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis
- Alteration taxonomy：genetic manipulation:knockout
- Gene-alteration：NEIL1 / genetic manipulation:knockout
- Alteration mention：Knockout
- Alteration ID：genetic manipulation:knockout
- Trigger/regulation context：results in / Reg
- Event dedup key：term | neil1 | genetic manipulation:knockout | oxidative stress hypothesis,mitochondrial autophagy hypothesis
- Long-tail signals：gene=NEIL1 (freq 1 <= threshold 1), gene_alteration=NEIL1 / genetic manipulation:knockout (freq 1 <= threshold 1)
- Curation reasons：model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：Knockout of mitochondrial OGG1 and NEIL1, which remove 8-oxo-dG and formamidopyrimidine lesions, respectively, in mice results in mitochondrial dysfunction and a metabolic syndrome phenotype.

## 用户问题解释指南

- 全局统计用于描述该表型跨 genes 与 hypotheses 的覆盖情况。
- 分子机制总结应使用 curated representative evidence，而不是 raw API ranking。
- Candidate mechanism strata 是专家复核辅助。
- 宽泛 disease association evidence 应与 molecular 或 model-based evidence 分开。

## 后续研究重点

- 可增加 `--selected-limit` 展示更多来自 full-pool curation endpoint 的代表证据。
- `--curation-limit` 仅在服务器不暴露 `/term/curation` 时影响 fallback mode。
- 可在 `data/curation.json` 中按 `EvidenceType`、`MechanismStrata`、`IsLongTailEvidence`、year、gene、phenotype、gene-alteration pair 或 alteration taxonomy 过滤。
- 需要人工复核 selected mechanisms 是否来自原始实验、综述句子或 curated interpretation fields。

## 案例三：假说查询

### 自然语言输入

请使用 adalterome-hypothesis-report 查询 Tau Protein Hypothesis，使用 full-pool curation，selected-limit=5，用中文输出完整报告。

### 完整输出

# AD-Alterome 假说报告：Tau Protein Hypothesis

## 查询范围与数据来源

- 目标 hypothesis：`Tau Protein Hypothesis`
- API base URL：`http://117.72.176.137/api/adalterome`
- Overview request：`http://117.72.176.137/api/adalterome/hypothesis/overview?hypothesis=Tau+Protein+Hypothesis`
- Curation evidence source：`http://117.72.176.137/api/adalterome/hypothesis/curation?hypothesis=Tau+Protein+Hypothesis&selected_limit=5`
- Curation package：`data/curation.json`

## 全局证据景观

AD-Alterome 将 `Tau Protein Hypothesis` 关联到 38095 条 event records，覆盖 5580 个 PMID、1410 个 gene、1024 个 term。该结果支持构建该假说的证据地图，但不表示该假说已被句子级数据库证据完整证明。

### Top genes

- MAPT：16999
- APP：1736
- PSEN1：1562
- APOE：757
- SNCA：650
- TAS2R62P：574
- GRN：494
- TARDBP：473
- TREM2：435
- PSEN2：374

### Top terms

- Alzheimer Disease (MeSH)：2335
- protein (GO)：1341
- Dementia (HPO)：864
- phosphorylation (GO)：809
- Tauopathies (MeSH)：780
- Neurodegeneration (HPO)：598
- Frontotemporal dementia (HPO)：565
- Nerve Degeneration (MeSH)：510
- biosynthetic process (GO)：468
- hyperphosphorylation (GO)：458

## 证据中间层

- skills 报告不使用也不展示 raw API scoring fields。
- 句子级证据来源：remote_api (`server_full_query_pool`)。
- Curation pool rows：38103；按 query-specific event key 去重后 event-unique rows：17537。
- API overview reported event rows：38095。
- Event deduplication key：hypothesis-fixed event key，即 gene + alteration taxonomy + phenotype/term；结构字段稀疏时回退到 PMID/sentence。
- Curation pool 中 unique PMIDs：4520；genes：1410；phenotypes：1039；alteration taxonomies：28；gene-alteration pairs：2731。
- Long-tail 规则：在 event-level deduplication 后，对 gene、gene_alteration、phenotype 等维度按 query-specific frequency 判断，阈值为 `{'gene': 2, 'gene_alteration': 1, 'phenotype': 1}`。

### Dominant PMIDs

- 33419465：77
- 30249283：54
- 32325732：52
- 31405128：49
- 37131250：48

### Top genes

- MAPT：4533
- APP：695
- PSEN1：573
- SNCA：321
- TAS2R62P：320

### Top gene-alteration pairs

- MAPT / point mutations:mutations：1104
- MAPT / normalized variants:dna change：1074
- MAPT / structural variation:deletion：322
- MAPT / epigenic changes:phosphorylation：312
- PSEN1 / point mutations:mutations：293

### Top phenotypes

- Alzheimer Disease：524
- protein：378
- phosphorylation：337
- Neurodegeneration：203
- hyperphosphorylation：190

### Dominant alteration taxonomy

- point mutations:mutations：5508
- normalized variants:dna change：2341
- structural variation:deletion：1615
- expression changes:dysregulation：1347
- expression changes:underexpression：1273

### Evidence type distribution

- alteration_evidence：11755
- model_or_intervention：5782

### Mechanism strata distribution

- amyloid/tau axis：17537
- synaptic and neuronal dysfunction axis：6254
- proteostasis/autophagy axis：6133
- neuroinflammation and microglia axis：3228
- mitochondrial and oxidative stress axis：3141

### Query-relative top 与 long-tail patterns

| 维度 | Top values | Long-tail values |
| --- | --- | --- |
| Gene | MAPT (4533); APP (695); PSEN1 (573); SNCA (321); TAS2R62P (320); APOE (310); TREM2 (267); TARDBP (211) | ABCC1 (1); ABCC6 (1); ABT1 (1); ACVR1 (1); ADGRB3 (1); AGER (1); AGPS (1); AIF1 (1) |
| Gene-alteration | MAPT / point mutations:mutations (1104); MAPT / normalized variants:dna change (1074); MAPT / structural variation:deletion (322); MAPT / epigenic changes:phosphorylation (312); PSEN1 / point mutations:mutations (293); APP / point mutations:mutations (293); MAPT / expression changes:dysregulation (275); PSEN1 / normalized variants:dna change (196) | ABCC1 / normalized variants:rsid normalized (1); ABCC6 / point mutations:mutations (1); ABI3 / normalized variants:protein change (1); ABT1 / point mutations:mutations (1); ACAT2 / normalized variants:dna change (1); ACAT2 / point mutations:mutations (1); ACHE / expression changes:underexpression (1); ACHE / point mutations:mutations (1) |
| Phenotype | phosphorylation (337); AD (309); 4137 (292); Neurodegeneration (203); hyperphosphorylation (190); biosynthetic process (174); Nerve Degeneration (161); Tauopathies (157) | 1-phosphatidylinositol-3-kinase activity (1); 100506658 (1); 101084670 (1); 10376 (1); 10919 (1); 10922 (1); 10971 (1); 112935892 (1) |

## 机制分层证据图

| Candidate mechanism stratum | Selected evidence rows | Representative genes |
| --- | --- | --- |
| amyloid/tau axis | 5 | UCP1, MAPT, MAG, CD68 |
| mitochondrial and oxidative stress axis | 2 | UCP1 |
| neuroinflammation and microglia axis | 1 | CD68 |
| proteostasis/autophagy axis | 1 | MAPT |
| synaptic and neuronal dysfunction axis | 3 | MAPT, MAG, CD68 |
| vascular/metabolic axis | 2 | MAG, CD68 |

这些 strata 用于组织假说支持模式。Hypothesis labels 是 AD-Alterome curated assignments，不是因果证明。

## 代表性支持证据

| # | PMID | Gene | Phenotype | Evidence type | Mechanism strata | Sentence informativeness |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [36769062](https://pubmed.ncbi.nlm.nih.gov/36769062/) | UCP1 | phosphorylation | model_or_intervention | amyloid/tau axis; mitochondrial and oxidative stress axis | 90.0 |
| 2 | [37929088](https://pubmed.ncbi.nlm.nih.gov/37929088/) | MAPT | Generalized | alteration_evidence | amyloid/tau axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis | 90.0 |
| 3 | [36769062](https://pubmed.ncbi.nlm.nih.gov/36769062/) | UCP1 | Memory impairment | model_or_intervention | amyloid/tau axis; mitochondrial and oxidative stress axis | 90.0 |
| 4 | [37927337](https://pubmed.ncbi.nlm.nih.gov/37927337/) | MAG | biosynthetic process | model_or_intervention | amyloid/tau axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | 90.0 |
| 5 | [36966157](https://pubmed.ncbi.nlm.nih.gov/36966157/) | CD68 | Auditory Diseases, Central | model_or_intervention | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | 90.0 |

## Long-tail evidence signals

| # | PMID | Gene | Phenotype | Evidence type | Long-tail dimensions | Reasons |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [36769062](https://pubmed.ncbi.nlm.nih.gov/36769062/) | UCP1 | phosphorylation | model_or_intervention | gene=UCP1 (2) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 2 | [36769062](https://pubmed.ncbi.nlm.nih.gov/36769062/) | UCP1 | Memory impairment | model_or_intervention | gene=UCP1 (2) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 3 | [37927337](https://pubmed.ncbi.nlm.nih.gov/37927337/) | MAG | biosynthetic process | model_or_intervention | gene=MAG (1); gene_alteration=MAG / structural variation:deletion (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 4 | [36966157](https://pubmed.ncbi.nlm.nih.gov/36966157/) | CD68 | Auditory Diseases, Central | model_or_intervention | gene_alteration=CD68 / genetic manipulation:knockout (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |
| 5 | [37507386](https://pubmed.ncbi.nlm.nih.gov/37507386/) | UCHL1 | biosynthetic process | model_or_intervention | gene_alteration=UCHL1 / genetic manipulation:knockout (1) | model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable |

## 时间序列证据轨迹

| Period | Event-unique rows | Dominant mechanism strata |
| --- | --- | --- |
| 2010-2014 | 2098 | amyloid/tau axis (2098); synaptic and neuronal dysfunction axis (795); proteostasis/autophagy axis (610); mitochondrial and oxidative stress axis (378); neuroinflammation and microglia axis (224) |
| 2015-2019 | 4697 | amyloid/tau axis (4697); synaptic and neuronal dysfunction axis (1617); proteostasis/autophagy axis (1529); neuroinflammation and microglia axis (916); mitochondrial and oxidative stress axis (867) |
| 2020-2024 | 8605 | amyloid/tau axis (8605); proteostasis/autophagy axis (3370); synaptic and neuronal dysfunction axis (3123); neuroinflammation and microglia axis (1753); mitochondrial and oxidative stress axis (1560) |
| before 2010 | 795 | amyloid/tau axis (795); synaptic and neuronal dysfunction axis (266); proteostasis/autophagy axis (239); mitochondrial and oxidative stress axis (137); vascular/metabolic axis (102) |
| missing year | 1342 | amyloid/tau axis (1342); synaptic and neuronal dysfunction axis (453); proteostasis/autophagy axis (385); neuroinflammation and microglia axis (268); mitochondrial and oxidative stress axis (199) |

## 原始证据追踪

### Evidence 1：PMID 36769062

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/36769062/`
- Gene：UCP1
- Journal/Year：Int J Mol Sci / 2023
- Phenotype：phosphorylation
- Hypothesis：Amyloid hypothesis,Tau protein hypothesis,Oxidative stress hypothesis
- Evidence type：model_or_intervention
- Candidate mechanism strata：amyloid/tau axis; mitochondrial and oxidative stress axis
- Alteration taxonomy：structural variation:deletion
- Gene-alteration：UCP1 / structural variation:deletion
- Alteration mention：Deletion
- Alteration ID：structural variation:deletion
- Trigger/regulation context：leading to / Reg
- Event dedup key：hypothesis | ucp1 | structural variation:deletion | go:0016310
- Long-tail signals：gene=UCP1 (freq 2 <= threshold 2)
- Curation reasons：model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：Deletion of UCP1 in Tg2576 Mice Increases Body Temperature and Exacerbates Alzheimer's Disease-Related Pathologies We previously demonstrated that the Alzheimer's disease (AD)-like model mice, Tg2576, housed at a high ambient temperature of 30 C for 13 months, exhibited increased body temperature, which increased amyloid-beta (Abeta) levels and tau stability, leading to tau phosphorylation and ultimately inducing memory impairment.

### Evidence 2：PMID 37929088

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/37929088/`
- Gene：MAPT
- Journal/Year：ACS Omega / 2023
- Phenotype：Generalized
- Hypothesis：Tau Protein Hypothesis
- Evidence type：alteration_evidence
- Candidate mechanism strata：amyloid/tau axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis
- Alteration taxonomy：point mutations:substitution
- Gene-alteration：MAPT / point mutations:substitution
- Alteration mention：substitution
- Alteration ID：point mutations:substitution
- Trigger/regulation context：effect / Reg
- Event dedup key：hypothesis | mapt | point mutations:substitution | hp:0012837
- Long-tail signals：phenotype=Generalized (freq 1 <= threshold 1)
- Curation reasons：alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：Interestingly, our study also evaluated the impact of missense mutations on the MAPT protein and found that the substitution of lysine with asparagine (K > N) in nine different transcript-level SNPs resulted in a generalized destabilizing effect on the protein's stability, function, and dynamics.

### Evidence 3：PMID 36769062

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/36769062/`
- Gene：UCP1
- Journal/Year：Int J Mol Sci / 2023
- Phenotype：Memory impairment
- Hypothesis：Amyloid hypothesis,Tau protein hypothesis,Oxidative stress hypothesis
- Evidence type：model_or_intervention
- Candidate mechanism strata：amyloid/tau axis; mitochondrial and oxidative stress axis
- Alteration taxonomy：structural variation:deletion
- Gene-alteration：UCP1 / structural variation:deletion
- Alteration mention：Deletion
- Alteration ID：structural variation:deletion
- Trigger/regulation context：inducing / Reg
- Event dedup key：hypothesis | ucp1 | structural variation:deletion | hp:0002354
- Long-tail signals：gene=UCP1 (freq 2 <= threshold 2)
- Curation reasons：model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：Deletion of UCP1 in Tg2576 Mice Increases Body Temperature and Exacerbates Alzheimer's Disease-Related Pathologies We previously demonstrated that the Alzheimer's disease (AD)-like model mice, Tg2576, housed at a high ambient temperature of 30 C for 13 months, exhibited increased body temperature, which increased amyloid-beta (Abeta) levels and tau stability, leading to tau phosphorylation and ultimately inducing memory impairment.

### Evidence 4：PMID 37927337

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/37927337/`
- Gene：MAG
- Journal/Year：Front Aging Neurosci / 2023
- Phenotype：biosynthetic process
- Hypothesis：Tau Protein Hypothesis,Glutamatergic Excitotoxicity Hypothesis
- Evidence type：model_or_intervention
- Candidate mechanism strata：amyloid/tau axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis
- Alteration taxonomy：structural variation:deletion
- Gene-alteration：MAG / structural variation:deletion
- Alteration mention：deficient
- Alteration ID：structural variation:deletion
- Trigger/regulation context：altered / Reg
- Event dedup key：hypothesis | mag | structural variation:deletion | go:0009058
- Long-tail signals：gene=MAG (freq 1 <= threshold 2), gene_alteration=MAG / structural variation:deletion (freq 1 <= threshold 1)
- Curation reasons：model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：Previous studies have demonstrated that axonal pathology preceding axonal degeneration includes impairment of axonal transport and altered formation of axonal spheroids in mice deficient in PLP (proteolipid protein) and CNP (2',3'-cyclic nucleotide 3'-phosphodiesterase), as well as reduced neurofilament phosphorylation and smaller axonal diameter in MAG (myelin-associated glycoprotein) deficient mice.

### Evidence 5：PMID 36966157

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/36966157/`
- Gene：CD68
- Journal/Year：Nat Commun / 2023
- Phenotype：Auditory Diseases, Central
- Hypothesis：Tau protein hypothesis,Neuroinflammation hypothesis
- Evidence type：model_or_intervention
- Candidate mechanism strata：amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis
- Alteration taxonomy：genetic manipulation:knockout
- Gene-alteration：CD68 / genetic manipulation:knockout
- Alteration mention：knockdown
- Alteration ID：genetic manipulation:knockout
- Trigger/regulation context：increased / PosReg
- Event dedup key：hypothesis | cd68 | genetic manipulation:knockout | mesh:d001304
- Long-tail signals：gene_alteration=CD68 / genetic manipulation:knockout (freq 1 <= threshold 1)
- Curation reasons：model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：Reinforcing earlier discussion on hp-tau aggregates and neuronal phagoptosis, APOE knockdown in P301S mice significantly reduced hippocampal and entorhinal cortex loss; APOE preservation increased Iba1 + (suggesting microglia and macrophage populations) cells that were positive with CD68 + phagocytic inclusions.

## 用户问题解释指南

- direct sentence support 与 AD-Alterome hypothesis assignment fields 应分开解释。
- 假说支持模式应基于 curated representative evidence。
- Candidate mechanism strata 是专家复核辅助。
- 不应声称句子级数据库证据已经证明 Tau Protein Hypothesis。

## 后续分析重点

- 可增加 `--selected-limit` 展示更多 full-pool representative evidence。
- `--curation-limit` 仅在服务器不暴露 `/hypothesis/curation` 时影响 fallback mode。
- 可在 `data/curation.json` 中按 `EvidenceType`、`MechanismStrata`、`IsLongTailEvidence`、year、gene、phenotype、gene-alteration pair 或 alteration taxonomy 过滤。
- 当 hypothesis combinations 在返回证据中占主导时，应与相邻假说进行对照分析。

## 案例四：APP 与 APOE 比较查询

### 自然语言输入

请使用 adalterome-compare-report 比较 APP 和 APOE，使用 full-pool curation，每个基因 selected-limit=4，用中文输出完整比较报告。

### 完整输出

# AD-Alterome 基因比较报告：APP vs APOE

## 查询范围与数据来源

- Gene A：`APP`
- Gene B：`APOE`
- API base URL：`http://117.72.176.137/api/adalterome`
- Compare request：`http://117.72.176.137/api/adalterome/compare/genes?gene_a=APP&gene_b=APOE`
- Gene A curation evidence source：`http://117.72.176.137/api/adalterome/gene/curation?gene=APP&selected_limit=4`
- Gene B curation evidence source：`http://117.72.176.137/api/adalterome/gene/curation?gene=APOE&selected_limit=4`
- Gene A curation package：`data/gene_a_curation.json`
- Gene B curation package：`data/gene_b_curation.json`

## 并列全局证据景观

| Metric | APP | APOE |
| --- | --- | --- |
| event_count | 18277 | 13188 |
| pmid_count | 4724 | 3086 |
| term_count | 621 | 660 |
| hypothesis_count | 150 | 138 |

## Shared terms and hypotheses

### Shared terms

- Alzheimer Disease：APP=2459，APOE=1783
- protein：APP=2030，APOE=291
- Onset：APP=959，APOE=627
- Dementia：APP=162，APOE=289
- Sporadic：APP=173，APOE=266
- Alzheimer disease：APP=176，APOE=140

### Shared hypotheses

- Amyloid Hypothesis：APP=13553，APOE=3946
- Amyloid Hypothesis,Vascular Hypothesis：APP=423，APOE=2843
- Amyloid Hypothesis,Tau Protein Hypothesis：APP=1185，APOE=313
- Amyloid Hypothesis,Neuroinflammation Hypothesis：APP=345，APOE=384
- Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis：APP=167，APOE=92

## APP-specific patterns

### Unique terms

- All：262
- biosynthetic process：253
- chromosome：183
- cleavage：144

### Unique hypotheses

- Amyloid Hypothesis,Mitochondrial Autophagy Hypothesis：235
- Amyloid Hypothesis,Oxidative Stress Hypothesis：208
- Amyloid Hypothesis,Abnormal Autophagy Hypothesis：166
- Amyloid Hypothesis,Metal Ion Hypothesis：113
- Amyloid Hypothesis,Glutamatergic Excitotoxicity Hypothesis：101

## APOE-specific patterns

### Unique terms

- Late onset：455
- Cognition Disorders：173
- developmental process：164
- Cognitive impairment：129

### Unique hypotheses

- Vascular Hypothesis：1507
- Neuroinflammation Hypothesis：263
- Neuroinflammation Hypothesis,Vascular Hypothesis：177
- Neuroinflammation Hypothesis,Amyloid Hypothesis：107
- Oxidative Stress Hypothesis：88

## APP 证据中间层

- skills 报告不使用也不展示 raw API scoring fields。
- 句子级证据来源：remote_api (`server_full_query_pool`)。
- Curation pool rows：18277；按 query-specific event key 去重后 event-unique rows：4985。
- API overview reported event rows：18277。
- Event deduplication key：gene-fixed event key，即 alteration taxonomy + phenotype/term + hypothesis；结构字段稀疏时回退到 PMID/sentence。
- Unique PMIDs：2419；genes：1；phenotypes：625；alteration taxonomies：29；gene-alteration pairs：29。
- Long-tail 阈值：`{'phenotype': 1, 'gene_alteration': 10, 'hypothesis': 3}`。

### APP top gene-alteration pairs

- APP / point mutations:mutations：2288
- APP / normalized variants:dna change：643
- APP / structural variation:deletion：274
- APP / expression changes:dysregulation：241
- APP / expression changes:underexpression：234

### APP top phenotypes

- protein：121
- Alzheimer Disease：107
- Onset：49
- biosynthetic process：46
- Neurodegeneration：42

### APP dominant alteration taxonomy

- point mutations:mutations：2288
- normalized variants:dna change：643
- structural variation:deletion：274
- expression changes:dysregulation：241
- expression changes:underexpression：234

### APP evidence type distribution

- alteration_evidence：3500
- model_or_intervention：1485

### APP mechanism strata distribution

- amyloid/tau axis：4985
- proteostasis/autophagy axis：1593
- synaptic and neuronal dysfunction axis：1534
- mitochondrial and oxidative stress axis：905
- vascular/metabolic axis：747

### APP query-relative top 与 long-tail patterns

| 维度 | Top values | Long-tail values |
| --- | --- | --- |
| Phenotype | AD (57); biosynthetic process (46); Neurodegeneration (42); Cognition Disorders (40); Nerve Degeneration (38); expression (36); memory (34); cell (30) | 102 (1); 1020 (1); 112935892 (1); 12368 (1); 14961 (1); 16002 (1); 16846 (1); 1728 (1) |
| Gene-alteration | APP / point mutations:mutations (2288); APP / normalized variants:dna change (643); APP / structural variation:deletion (274); APP / expression changes:dysregulation (241); APP / expression changes:underexpression (234); APP / structural variation:chromosomal variation (199); APP / genetic manipulation:gene aggregation (149); APP / expression changes:overexpression (116) | APP / copy number variation:fusion (1); APP / epigenic changes:acetylation (1); APP / structural variation:frameshift (1); APP / structural variation:rearrangements (4) |
| Hypothesis | Amyloid Hypothesis (1976); Amyloid Hypothesis,Tau Protein Hypothesis (407); Amyloid hypothesis (333); Amyloid Hypothesis,Vascular Hypothesis (189); Amyloid Hypothesis,Neuroinflammation Hypothesis (169); Amyloid Hypothesis,Oxidative Stress Hypothesis (106); Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis (91); Amyloid Hypothesis,Abnormal Autophagy Hypothesis (85) | Amyloid Hypothesis,Neuroinflammation hypothesis (1); Amyloid Hypothesis,Neuroinflammation hypothesis,Vascular hypothesis (1); Amyloid hypothesis,Oxidative stress hypothesis,Vascular hypothesis (1); Amyloid hypothesis,Tau protein hypothesis,Mitochondrial autophagy hypothesis (1); Amyloid hypothesis,Tau protein hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis (1); Cholinergic Hypothesis (1); Cholinergic Hypothesis,Glutamatergic Excitotoxicity Hypothesis (1); Cholinergic Hypothesis,Neuroinflammation Hypothesis (1) |

## APP 机制分层证据图

| Candidate mechanism stratum | Selected evidence rows | Representative PMIDs |
| --- | --- | --- |
| amyloid/tau axis | 4 | 37513800, 36687366, 37840813, 37895105 |
| mitochondrial and oxidative stress axis | 2 | 37513800, 37840813 |
| neuroinflammation and microglia axis | 1 | 37840813 |
| proteostasis/autophagy axis | 1 | 37840813 |
| synaptic and neuronal dysfunction axis | 1 | 37895105 |

## APP 代表性证据

| # | PMID | Gene | Phenotype | Evidence type | Mechanism strata | Sentence informativeness |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [37513800](https://pubmed.ncbi.nlm.nih.gov/37513800/) | APP | Roseolovirus Infections | model_or_intervention | amyloid/tau axis; mitochondrial and oxidative stress axis | 90.0 |
| 2 | [36687366](https://pubmed.ncbi.nlm.nih.gov/36687366/) | APP | Polydactyly, Postaxial | alteration_evidence | amyloid/tau axis | 90.0 |
| 3 | [37840813](https://pubmed.ncbi.nlm.nih.gov/37840813/) | APP | autophagy | model_or_intervention | amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis | 90.0 |
| 4 | [37895105](https://pubmed.ncbi.nlm.nih.gov/37895105/) | APP | Ischemic Attack, Transient | model_or_intervention | amyloid/tau axis; synaptic and neuronal dysfunction axis | 90.0 |

## APP 时间序列证据轨迹

| Period | Event-unique rows | Dominant mechanism strata |
| --- | --- | --- |
| 2010-2014 | 863 | amyloid/tau axis (863); synaptic and neuronal dysfunction axis (282); proteostasis/autophagy axis (271); mitochondrial and oxidative stress axis (177); vascular/metabolic axis (149) |
| 2015-2019 | 1182 | amyloid/tau axis (1182); proteostasis/autophagy axis (400); synaptic and neuronal dysfunction axis (369); mitochondrial and oxidative stress axis (231); vascular/metabolic axis (147) |
| 2020-2024 | 2024 | amyloid/tau axis (2024); proteostasis/autophagy axis (717); synaptic and neuronal dysfunction axis (667); mitochondrial and oxidative stress axis (358); neuroinflammation and microglia axis (353) |
| before 2010 | 531 | amyloid/tau axis (531); synaptic and neuronal dysfunction axis (124); proteostasis/autophagy axis (121); mitochondrial and oxidative stress axis (87); vascular/metabolic axis (80) |
| missing year | 385 | amyloid/tau axis (385); synaptic and neuronal dysfunction axis (92); proteostasis/autophagy axis (84); vascular/metabolic axis (76); mitochondrial and oxidative stress axis (52) |

## APP 原始证据追踪

### Evidence 1：PMID 37513800

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/37513800/`
- Gene：APP
- Journal/Year：Pathogens / 2023
- Phenotype：Roseolovirus Infections
- Hypothesis：Amyloid Hypothesis
- Evidence type：model_or_intervention
- Candidate mechanism strata：amyloid/tau axis; mitochondrial and oxidative stress axis
- Alteration taxonomy：point mutations:mutations
- Gene-alteration：APP / point mutations:mutations
- Alteration mention：mutants
- Alteration ID：point mutations:Mutations
- Trigger/regulation context：link / Reg
- Event dedup key：gene | point mutations:mutations | mesh:d019349 | amyloid hypothesis
- Long-tail signals：phenotype=Roseolovirus Infections (freq 1 <= threshold 1)
- Curation reasons：model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：To investigate a potential link between roseolovirus infection and Alzheimer's disease, Bigley and colleagues used MRV to infect a transgenic mouse model in which overexpression of mutants of the human amyloid precursor protein (APP) and presenilin-1 leads to plaque formation.

### Evidence 2：PMID 36687366

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/36687366/`
- Gene：APP
- Journal/Year：Neuronal Signal / 2023
- Phenotype：Polydactyly, Postaxial
- Hypothesis：Amyloid Hypothesis
- Evidence type：alteration_evidence
- Candidate mechanism strata：amyloid/tau axis
- Alteration taxonomy：point mutations:mutations
- Gene-alteration：APP / point mutations:mutations
- Alteration mention：mutations
- Alteration ID：point mutations:Mutations
- Trigger/regulation context：affect / Reg
- Event dedup key：gene | point mutations:mutations | mesh:c562429 | amyloid hypothesis
- Long-tail signals：phenotype=Polydactyly, Postaxial (freq 1 <= threshold 1)
- Curation reasons：alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：All of the responsible mutations identified affect either the genes coding for the amyloid precursor protein (APP) from which Abeta is formed via a multistep processing pathway, or the genes coding for the presenilin (PS) 1 and 2 proteins that function within this processing pathway as part of an enzyme complex responsible for cleaving Abeta from its immediate precursor.

### Evidence 3：PMID 37840813

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/37840813/`
- Gene：APP
- Journal/Year：Front Aging / 2023
- Phenotype：autophagy
- Hypothesis：Amyloid Hypothesis,Neuroinflammation Hypothesis,Abnormal Autophagy Hypothesis
- Evidence type：model_or_intervention
- Candidate mechanism strata：amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis; proteostasis/autophagy axis
- Alteration taxonomy：expression changes:dysregulation
- Gene-alteration：APP / expression changes:dysregulation
- Alteration mention：lacking
- Alteration ID：expression changes:dysregulation
- Trigger/regulation context：accumulation / PosReg
- Event dedup key：gene | expression changes:dysregulation | go:0006914 | amyloid hypothesis,neuroinflammation hypothesis,abnormal autophagy hypothesis
- Long-tail signals：hypothesis=Amyloid Hypothesis,Neuroinflammation Hypothesis,Abnormal Autophagy Hypothesis (freq 2 <= threshold 3)
- Curation reasons：model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：For example, amyloid precursor protein/presenilin 1 (APP/PS1) mice lacking NRF2 exhibited autophagy dysfunction-dependent accumulation of insoluble Abeta aggregates, resulting in an increased pro-inflammatory phenotype.

### Evidence 4：PMID 37895105

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/37895105/`
- Gene：APP
- Journal/Year：Int J Mol Sci / 2023
- Phenotype：Ischemic Attack, Transient
- Hypothesis：Amyloid Hypothesis,Glutamatergic Excitotoxicity Hypothesis
- Evidence type：model_or_intervention
- Candidate mechanism strata：amyloid/tau axis; synaptic and neuronal dysfunction axis
- Alteration taxonomy：genetic manipulation:knock-in
- Gene-alteration：APP / genetic manipulation:knock-in
- Alteration mention：knock-in
- Alteration ID：-
- Trigger/regulation context：protect / Reg
- Event dedup key：gene | genetic manipulation:knock-in | mesh:d002546 | amyloid hypothesis,glutamatergic excitotoxicity hypothesis
- Long-tail signals：phenotype=Ischemic Attack, Transient (freq 1 <= threshold 1)
- Curation reasons：model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：TRPC6 overexpression has been shown to rescue mushroom spine loss in presenilin and amyloid precursor protein (APP) knock-in mouse models of AD and also protect neurons from ischemic brain damage.

## APOE 证据中间层

- skills 报告不使用也不展示 raw API scoring fields。
- 句子级证据来源：remote_api (`server_full_query_pool`)。
- Curation pool rows：13188；按 query-specific event key 去重后 event-unique rows：4002。
- API overview reported event rows：13188。
- Event deduplication key：gene-fixed event key，即 alteration taxonomy + phenotype/term + hypothesis；结构字段稀疏时回退到 PMID/sentence。
- Unique PMIDs：1898；genes：1；phenotypes：657；alteration taxonomies：26；gene-alteration pairs：26。
- Long-tail 阈值：`{'phenotype': 1, 'gene_alteration': 10, 'hypothesis': 3}`。

### APOE top gene-alteration pairs

- APOE / point mutations:mutations：2586
- APOE / normalized variants:rsid normalized：330
- APOE / structural variation:deletion：184
- APOE / normalized variants:dna change：169
- APOE / genetic manipulation:knockout：112

### APOE top phenotypes

- Alzheimer Disease：81
- Onset：47
- protein：46
- Dementia：33
- Cognition Disorders：30

### APOE dominant alteration taxonomy

- point mutations:mutations：2586
- normalized variants:rsid normalized：330
- structural variation:deletion：184
- normalized variants:dna change：169
- genetic manipulation:knockout：112

### APOE evidence type distribution

- alteration_evidence：3301
- model_or_intervention：701

### APOE mechanism strata distribution

- vascular/metabolic axis：4002
- amyloid/tau axis：3126
- proteostasis/autophagy axis：771
- neuroinflammation and microglia axis：766
- mitochondrial and oxidative stress axis：678

### APOE query-relative top 与 long-tail patterns

| 维度 | Top values | Long-tail values |
| --- | --- | --- |
| Phenotype | AD (62); expression (36); Cognition Disorders (30); inflammatory response (25); Neurodegeneration (24); metabolic process (24); developmental process (23); aging (22) | 100770679 (1); 10T-BNT scores (1); 11816 (1); 1191 (1); 12346 (1); 12774 (1); 1401 (1); 16019 (1) |
| Gene-alteration | APOE / point mutations:mutations (2586); APOE / normalized variants:rsid normalized (330); APOE / structural variation:deletion (184); APOE / normalized variants:dna change (169); APOE / genetic manipulation:knockout (112); APOE / expression changes:dysregulation (103); APOE / structural variation:chromosomal variation (103); APOE / genetic manipulation:knock-in (94) | APOE / structural variation:insertion (1); APOE / genetic manipulation:gene aggregation (2); APOE / structural variation:rearrangements (2); APOE / structural variation:frameshift (3); APOE / epigenic changes:epigenetics (7); APOE / normalized variants:cdna change (9); APOE / copy number variation:amplification (10) |
| Hypothesis | Amyloid Hypothesis (642); Amyloid Hypothesis,Vascular Hypothesis (477); Vascular Hypothesis (323); Vascular hypothesis (176); Amyloid Hypothesis,Neuroinflammation Hypothesis (128); Amyloid hypothesis,Vascular hypothesis (119); Amyloid Hypothesis,Tau Protein Hypothesis (102); Neuroinflammation Hypothesis (88) | Abnormal Autophagy Hypothesis,Vascular Hypothesis (1); Amyloid Hypothesis,Neuroinflammation Hypothesis. (1); Amyloid Hypothesis,Oxidative Stress Hypothesis,Metal Ion Hypothesis (1); Cholinergic hypothesis,Vascular hypothesis (1); Glutamatergic excitotoxicity hypothesis,Microbiota-Gut-Brain Axis hypothesis (1); Mitochondrial Autophagy Hypothesis,Oxidative Stress Hypothesis (1); Mitochondrial autophagy hypothesis,Vascular hypothesis (1); Neuroinflammation Hypothesis,Abnormal Autophagy Hypothesis (1) |

## APOE 机制分层证据图

| Candidate mechanism stratum | Selected evidence rows | Representative PMIDs |
| --- | --- | --- |
| amyloid/tau axis | 3 | 36966157, 38004343, 36927428 |
| mitochondrial and oxidative stress axis | 1 | 36927428 |
| neuroinflammation and microglia axis | 2 | 36966157, 36835187 |
| proteostasis/autophagy axis | 2 | 38004343, 36927428 |
| synaptic and neuronal dysfunction axis | 1 | 36966157 |
| vascular/metabolic axis | 4 | 36966157, 38004343, 36835187, 36927428 |

## APOE 代表性证据

| # | PMID | Gene | Phenotype | Evidence type | Mechanism strata | Sentence informativeness |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [36966157](https://pubmed.ncbi.nlm.nih.gov/36966157/) | APOE | Auditory Diseases, Central | model_or_intervention | amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis | 90.0 |
| 2 | [38004343](https://pubmed.ncbi.nlm.nih.gov/38004343/) | APOE | of amyloid beta | alteration_evidence | amyloid/tau axis; vascular/metabolic axis; proteostasis/autophagy axis | 90.0 |
| 3 | [36835187](https://pubmed.ncbi.nlm.nih.gov/36835187/) | APOE | isotype switching | model_or_intervention | neuroinflammation and microglia axis; vascular/metabolic axis | 90.0 |
| 4 | [36927428](https://pubmed.ncbi.nlm.nih.gov/36927428/) | APOE | Mitochondrial inheritance | model_or_intervention | amyloid/tau axis; mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis | 90.0 |

## APOE 时间序列证据轨迹

| Period | Event-unique rows | Dominant mechanism strata |
| --- | --- | --- |
| 2010-2014 | 588 | vascular/metabolic axis (588); amyloid/tau axis (457); proteostasis/autophagy axis (114); mitochondrial and oxidative stress axis (102); neuroinflammation and microglia axis (83) |
| 2015-2019 | 994 | vascular/metabolic axis (994); amyloid/tau axis (764); proteostasis/autophagy axis (181); mitochondrial and oxidative stress axis (170); neuroinflammation and microglia axis (137) |
| 2020-2024 | 1736 | vascular/metabolic axis (1736); amyloid/tau axis (1351); neuroinflammation and microglia axis (423); proteostasis/autophagy axis (386); mitochondrial and oxidative stress axis (273) |
| before 2010 | 381 | vascular/metabolic axis (381); amyloid/tau axis (305); mitochondrial and oxidative stress axis (89); synaptic and neuronal dysfunction axis (53); proteostasis/autophagy axis (48) |
| missing year | 303 | vascular/metabolic axis (303); amyloid/tau axis (249); neuroinflammation and microglia axis (86); mitochondrial and oxidative stress axis (44); proteostasis/autophagy axis (42) |

## APOE 原始证据追踪

### Evidence 1：PMID 36966157

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/36966157/`
- Gene：APOE
- Journal/Year：Nat Commun / 2023
- Phenotype：Auditory Diseases, Central
- Hypothesis：Tau protein hypothesis,Neuroinflammation hypothesis
- Evidence type：model_or_intervention
- Candidate mechanism strata：amyloid/tau axis; neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis
- Alteration taxonomy：genetic manipulation:knockout
- Gene-alteration：APOE / genetic manipulation:knockout
- Alteration mention：knockdown
- Alteration ID：genetic manipulation:knockout
- Trigger/regulation context：increased / PosReg
- Event dedup key：gene | genetic manipulation:knockout | mesh:d001304 | tau protein hypothesis,neuroinflammation hypothesis
- Long-tail signals：phenotype=Auditory Diseases, Central (freq 1 <= threshold 1)
- Curation reasons：model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：Reinforcing earlier discussion on hp-tau aggregates and neuronal phagoptosis, APOE knockdown in P301S mice significantly reduced hippocampal and entorhinal cortex loss; APOE preservation increased Iba1 + (suggesting microglia and macrophage populations) cells that were positive with CD68 + phagocytic inclusions.

### Evidence 2：PMID 38004343

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/38004343/`
- Gene：APOE
- Journal/Year：Life (Basel);2023Nov13; 13 (11) . doi:10.3390/life13112203 / 2023
- Phenotype：of amyloid beta
- Hypothesis：Amyloid Hypothesis
- Evidence type：alteration_evidence
- Candidate mechanism strata：amyloid/tau axis; vascular/metabolic axis; proteostasis/autophagy axis
- Alteration taxonomy：point mutations:mutations
- Gene-alteration：APOE / point mutations:mutations
- Alteration mention：mutations
- Alteration ID：point mutations:Mutations
- Trigger/regulation context：overproduction / PosReg
- Event dedup key：gene | point mutations:mutations | mesh:c000718787 | amyloid hypothesis
- Long-tail signals：phenotype=of amyloid beta (freq 1 <= threshold 1)
- Curation reasons：alteration_evidence, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：EOAD is a very uncommon condition associated with genetic factors such as mutations in susceptibility genes like amyloid precursor protein (APP), apolipoprotein E4 (ApoE4), presenilin 1 (PSEN1), and presenilin 2 (PSEN2), which can lead to an overproduction of amyloid beta.

### Evidence 3：PMID 36835187

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/36835187/`
- Gene：APOE
- Journal/Year：Int J Mol Sci / 2023
- Phenotype：isotype switching
- Hypothesis：Neuroinflammation hypothesis,Vascular hypothesis
- Evidence type：model_or_intervention
- Candidate mechanism strata：neuroinflammation and microglia axis; vascular/metabolic axis
- Alteration taxonomy：genetic manipulation:knock-in
- Gene-alteration：APOE / genetic manipulation:knock-in
- Alteration mention：knock-in
- Alteration ID：-
- Trigger/regulation context：high / PosReg
- Event dedup key：gene | genetic manipulation:knock-in | go:0045190 | neuroinflammation hypothesis,vascular hypothesis
- Long-tail signals：phenotype=isotype switching (freq 1 <= threshold 1)
- Curation reasons：model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：Another study has demonstrated lower total IgG and IgA levels in the spleen of APOE4 knock-in mice compared with APOE3, but the levels of IgG2a subtype and IgM were quite high in APOE4 mice, suggesting differential Ig class switching in APOE4 mice compared with APOE3 or APOE2 mice.

### Evidence 4：PMID 36927428

- PubMed：`https://pubmed.ncbi.nlm.nih.gov/36927428/`
- Gene：APOE
- Journal/Year：Curr Neuropharmacol / 2023
- Phenotype：Mitochondrial inheritance
- Hypothesis：Amyloid hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis
- Evidence type：model_or_intervention
- Candidate mechanism strata：amyloid/tau axis; mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis
- Alteration taxonomy：point mutations:mutations
- Gene-alteration：APOE / point mutations:mutations
- Alteration mention：mutants
- Alteration ID：point mutations:Mutations
- Trigger/regulation context：cause / Reg
- Event dedup key：gene | point mutations:mutations | hp:0001427 | amyloid hypothesis,oxidative stress hypothesis,mitochondrial autophagy hypothesis
- Long-tail signals：hypothesis=Amyloid hypothesis,Oxidative stress hypothesis,Mitochondrial autophagy hypothesis (freq 3 <= threshold 3)
- Curation reasons：model_or_intervention, high sentence informativeness, long-tail evidence signal, recent evidence, PMID-traceable
- Original sentence：Recent research in cellular, biochemical and animal models have shown that AD mutants affecting the presenilins, Ass, APP, and ApoE4 are associated with mitochondria and cause mitochondrial dysfunction and oxidative damage in AD (Fig.

## 比较解释指南

- Overview counts 用于描述数据库表示，不等于生物学重要性。
- 机制比较应优先使用 curated representative evidence，而不是 raw API ranking。
- shared terms 与 shared hypotheses 需要结合两个基因各自的 original sentences 解读。
- Candidate mechanism strata 是专家复核辅助。

## 后续分析重点

- 可增加 `--selected-limit` 展示每个基因更多 representative evidence。
- `--curation-limit` 仅在服务器不暴露 `/gene/curation` 时影响 fallback mode。
- 可在 `data/gene_a_curation.json` 与 `data/gene_b_curation.json` 中按 `EvidenceType`、`MechanismStrata`、`IsLongTailEvidence`、year、phenotype、gene-alteration pair 或 alteration taxonomy 过滤。
- 不应仅根据 event count 差异判断两个基因的生物学重要性；event count 首先反映 literature density。
