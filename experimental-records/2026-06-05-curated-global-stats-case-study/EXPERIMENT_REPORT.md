# AD-Alterome API 0.4.1 与新版 skills 人类专家 case 对照实验报告

生成日期：2026-06-05

## 1. 结论摘要

本轮更新后的核心变化是：API 的 curation 响应不再只让报告看到少量代表证据，而是额外暴露 `global_statistics`，用于描述完整查询池的真实分布。skills 在写报告时同时呈现两层信息：完整匹配池/curated pool 的统计，以及进入正文的代表性证据。

与 2026-06-04 的实验相比，四个 case 都已经走到 `curated_pool / offline_full_query_pool_prescreened`，不再出现昨天 APOE、mitochondrial dysfunction、neuroinflammation 只使用 50 条 API sample 的问题。MAPT、APOE、APP、Neuroinflammation Hypothesis 能显示完整匹配事件数、event-unique 数、curated pool 数、top genes、top phenotypes、top gene-alterations、alteration taxonomy、evidence types 和 mechanism strata；mitochondrial dysfunction 也能显示跨 4 个 term alias 合并后的完整统计。

和人类专家策展 case 相比，新版 skills 已经更接近“专家证据包”：它能保留完整分布、显式去重、保护 long-tail、保存 PubMed 原句、区分 LLM-reviewed 与 heuristic-only 注释。但它仍不是论文作者式人工策展的替代品。人类专家仍在研究问题定义、外部数据库对照、机制取舍、低频候选判断和论文级叙事上更强。最佳定位是：skills 先生成可审计证据包和 case 初稿，人类专家再做科学论证。

## 2. 更新与部署确认

| 项目 | 结果 |
| --- | --- |
| API 版本 | `0.4.1` |
| 公共 API | `http://117.72.176.137/api/adalterome` |
| 云端服务 | `ad-alterome-api.service`，已重启并处于 active |
| GitHub 提交 | `40694dd Expose complete curated query statistics in reports` |
| API 关键变更 | curation payload 新增/填充 `global_statistics`，并保留 `curated_pool_statistics` |
| skills 关键变更 | 报告新增 `Complete query-pool statistics`，从完整查询池展示 top genes、phenotypes、gene-alterations、hypotheses、alteration taxonomy、evidence types、mechanism strata |
| 验证 | 本地 `py_compile`、本地 8011 smoke test、云端 public smoke test、四个 case-study builder 均通过 |

## 3. 测评设计

本次沿用昨天的人类专家基线：`reports/adalterome_human_vs_skills_case_study_2026-06-04/EXPERIMENT_REPORT.md` 与论文文本 `materials/AD_Alterome.2026-06-04.txt`。自动侧使用新版 API 0.4.1 和新版 installed skills，重跑四个自然语言 case。

| Case | 自然语言输入 | 自动输出 |
| --- | --- | --- |
| 案例一：单基因查询 MAPT | MAPT evidence如何支持tau相关AD病理机制，以及新版curated pool是否能给出比人工筛选更透明的证据包？ | `skill_runs/gene_mapt/case_study_report.md` |
| 案例二：单表型/病理过程查询 mitochondrial dysfunction | mitochondrial dysfunction作为表型/病理过程时，AD-Alterome如何推荐和解释相关基因及长尾机制证据？ | `skill_runs/term_mitochondrial_dysfunction/case_study_report.md` |
| 案例三：假说查询 Neuroinflammation Hypothesis | Neuroinflammation Hypothesis的证据池是否能重建TREM2/APOE等炎症相关AD病理线索？ | `skill_runs/hypothesis_neuroinflammation/case_study_report.md` |
| 案例四：基因比较 APOE vs APP | APOE和APP在AD病理机制中有哪些共享和特异的遗传改变-表型-假说模式？ | `skill_runs/compare_apoe_app/case_study_report.md` |

评价维度包括：完整池覆盖、event-level 去重、curated pool 策略、long-tail 保护、alteration 解读、机制分层、与人类专家 case 的一致性，以及仍需人工介入的部分。

## 4. 自动运行结果总览

| Case | curation scope | raw matched events | event-unique before curation | curated pool count | case pool rows | unique PMIDs | main evidence | 覆盖判断 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| MAPT | offline_full_query_pool_prescreened | 27,921 | 8,014 | 2,687 | 2,687 | 1,636 | 16 | low_fraction_of_matched_events_in_curation_pool |
| mitochondrial dysfunction | offline_full_query_pool_prescreened | 4,159 | 1,907 | 858 | 244 | 152 | 16 | - |
| Neuroinflammation Hypothesis | offline_full_query_pool_prescreened | 34,060 | 20,229 | 5,225 | 5,225 | 3,030 | 16 | - |
| APOE in APOE vs APP | offline_full_query_pool_prescreened | 13,322 | 4,025 | 1,840 | 1,839 | 1,159 | compare 共 18 | balanced |
| APP in APOE vs APP | offline_full_query_pool_prescreened | 18,639 | 4,994 | 2,300 | 2,300 | 1,592 | compare 共 18 | balanced |

说明：`raw matched events`、`event-unique before curation` 和 `curated pool count` 来自 API 0.4.1 的 `global_statistics`，代表完整查询池统计；`case pool rows` 是进入当前 case-study builder 的有效 curated rows；`main evidence` 是正文保留的专家证据条数。

## 5. Case-by-Case 对照

### 5.1 MAPT 单基因

人类专家 case 的重点是 MAPT gene-centric phenotype prioritization：论文中人工评估 MAPT top 50 phenotypes，60.0% 为高相关、30.0% 为中等相关，并将 hyperphosphorylated tau dystrophic neurites、microtubule polymerization/binding、neurofibrillary tangles，以及 cell senescence、synaptic plasticity、chromosomal instability 等方向组织成 tau hypothesis 叙事。

新版 skills 的 MAPT case 从完整查询池看到 27,921 条 raw event records，event-level 去重后 8,014 条，候选高质量事件 6,553 条，最终 curated pool 2,687 条。正文保留 16 条 main evidence，全部为 LLM-reviewed、ExpertOverallScore=5、long-tail included。

| 维度 | 新版 skills 输出 |
| --- | --- |
| Complete-pool top phenotypes | protein [GO:0003675]（106）；Alzheimer Disease [MESH:D000544]（103）；Neurodegeneration [HP:0002180]（81）；phosphorylation [GO:0016310]（69）；biosynthetic process [GO:0009058]（65）；Dementia [HP:0000726]（64） |
| Complete-pool top gene-alterations | MAPT / point mutations:mutations（2,439）；MAPT / normalized variants:dna change（1,931）；MAPT / structural variation:deletion（516）；MAPT / expression changes:dysregulation（460）；MAPT / epigenic changes:phosphorylation（448）；MAPT / structural variation:chromosomal variation（332） |
| Alteration taxonomy | point mutations:mutations（2,448）；normalized variants:dna change（1,932）；structural variation:deletion（517）；expression changes:dysregulation（460）；epigenic changes:phosphorylation（448）；structural variation:chromosomal variation（332） |
| Mechanism strata | amyloid/tau axis（8,014）；proteostasis/autophagy axis（3,078）；synaptic and neuronal dysfunction axis（2,926）；mitochondrial and oxidative stress axis（1,418）；neuroinflammation and microglia axis（1,003）；vascular/metabolic axis（676） |
| Evidence types | molecular_mechanism（3,434）；model_or_intervention（2,998）；alteration_evidence（1,169）；cellular_or_pathway_process（413） |

对照结论：新版 skills 能更透明地给出 MAPT 的完整证据地形，尤其能区分高频突变/变异/表达/磷酸化证据与 long-tail 分子机制证据。它可以很好地服务于专家复核，但还没有自动复现论文中的 phenotype recommendation ranking、外部数据库 overlap 与人工 high/medium/low relevance 标注。

### 5.2 mitochondrial dysfunction 单表型/病理过程

人类专家 case 是 phenotype-centric gene recommendation：论文中 mitochondrial dysfunction 涉及 359 个 unique pathogenic genetic events 和 234 个 genes，并与既有 gene-phenotype association databases 中的 176 个相关基因做 overlap。专家将 SOD1、PINK1、SNCA 视为已知强相关，将 LRRK2、PRKN、POLGARF 视为 underappreciated，将 DAPK2、HSPB8、GDNF、NRF1 视为低频但机制上有价值的候选。

新版 API 对该 term 合并了 4 个 query values：Mitochondrial dysfunction；Mitochondrial inheritance [HP:0001427]；Abnormality of mitochondrial metabolism [HP:0003287]；mitochondrial injury [MESH:D028361]。完整统计为 4,159 条 raw events、1,907 条 event-unique、889 条候选高质量事件、858 条 curated pool。当前 case-study builder 从有效 term-filtered curated rows 中进入 244 条 pool rows、228 条 event-unique rows、152 个 PMID，再保留 16 条 main evidence。

| 维度 | 新版 skills 输出 |
| --- | --- |
| Complete-pool top genes | MAPT [Entrez:4137]（78）；PINK1 [Entrez:65018]（40）；APP [Entrez:351]（39）；SNCA [Entrez:6622]（27）；SIRT3 [Entrez:23410]（25）；PPIF [Entrez:10105]（20）；MFN2 [Entrez:9927]（16）；DAPK2 [Entrez:23604]（16）；SOD1 [Entrez:6647]（14）；PSEN1 [Entrez:5663]（13） |
| Complete-pool top gene-alterations | MAPT / point mutations:mutations（17）；APP / point mutations:mutations（16）；MAPT / normalized variants:dna change（12）；PINK1 / point mutations:mutations（9）；PSEN1 / point mutations:mutations（8）；TAS2R62P / point mutations:mutations（7）；APOE / point mutations:mutations（7）；PPIF / structural variation:deletion（6） |
| Mechanism strata | mitochondrial and oxidative stress axis（1,907）；amyloid/tau axis（1,373）；proteostasis/autophagy axis（903）；synaptic and neuronal dysfunction axis（466）；vascular/metabolic axis（261）；neuroinflammation and microglia axis（103） |
| Evidence types | model_or_intervention（693）；cellular_or_pathway_process（622）；molecular_mechanism（592） |

对照结论：新版完整池统计已经能把人类专家提到的 PINK1、SNCA、SOD1、DAPK2、PRKN、LRRK2 拉回可见范围，比昨天的 50-row sample 明显更接近 phenotype-centric recommendation case。差距仍在于：skills 还没有自动接入外部数据库 overlap，也没有把候选分成 established、underappreciated、low-literature mechanistic candidate 三类，这一步仍需专家完成。

### 5.3 Neuroinflammation Hypothesis 假说查询

人类专家 case 是 hypothesis-aware network interpretation：论文把 neuroinflammation 组织成免疫调控、glial activation、synaptic dysfunction 的网络模型，强调 TREM2 与 APOE 作为 hub，GRN、MAPT、TNF、APP、NLRP3 等提供补充路径，并形成 TREM2-DAP12 axis 的机制叙事。

新版 skills 从完整查询池看到 34,060 条 raw events、20,229 条 event-unique、20,173 条候选高质量事件、5,225 条 curated pool。正文保留 16 条 main evidence，全部 LLM-reviewed、ExpertOverallScore=5、long-tail included。

| 维度 | 新版 skills 输出 |
| --- | --- |
| Complete-pool top genes | TREM2 [Entrez:54209]（1,333）；MAPT [Entrez:4137]（757）；APOE [Entrez:348]（519）；APP [Entrez:351]（486）；TAS2R62P [Entrez:338399]（462）；TNF [Entrez:7124]（383）；IL6 [Entrez:3569]（363）；BDNF-AS [Entrez:497258]（338） |
| Complete-pool top phenotypes | Alzheimer Disease [MESH:D000544]（634）；AD（428）；expression（400）；protein [GO:0003675]（381）；inflammatory response [GO:0006954]（340）；activation [ADMO:0000042]（331）；signaling [GO:0023052]（269）；Neuroinflammation [HP:0033429]（262） |
| Complete-pool top gene-alterations | TREM2 / point mutations:mutations（368）；TREM2 / normalized variants:dna change（305）；APOE / point mutations:mutations（273）；MAPT / normalized variants:dna change（213）；TREM2 / structural variation:deletion（182）；APP / point mutations:mutations（180）；MAPT / point mutations:mutations（178）；PSEN1 / point mutations:mutations（176） |
| Mechanism strata | neuroinflammation and microglia axis（20,229）；amyloid/tau axis（10,105）；synaptic and neuronal dysfunction axis（6,365）；mitochondrial and oxidative stress axis（4,460）；vascular/metabolic axis（3,100）；proteostasis/autophagy axis（3,037） |

对照结论：新版完整统计清楚捕捉到 TREM2、MAPT、APOE、APP、TNF、IL6 等炎症网络核心，并且代表证据中也出现 TYROBP、GRN、NLRP3 等人工专家关心的路径。它已经能作为 network interpretation 的证据底稿；但它仍不会自动构建 AD-LitPathoNet 风格的网络结构，也不会自动把 TREM2-DAP12 axis 提炼为机制模型。

### 5.4 APOE vs APP 基因比较

人类专家 case 的目标是机制对比：APOE 与 APP 都收敛于 neurodegenerative phenotypes，但 APOE 更偏 immune-related/systemic/vascular-metabolic abnormalities，APP 更偏 amyloid、metabolic、neurocognitive 和 synaptic dysfunction。

新版 compare 已通过 coverage gate：APOE 与 APP 都为 `offline_full_query_pool_prescreened`，balance status 为 `balanced`。APOE 完整池为 13,322 raw / 4,025 event-unique / 1,840 curated；APP 为 18,639 raw / 4,994 event-unique / 2,300 curated。正文保留 18 条 main evidence，APOE 与 APP 两侧均进入主叙事。

| 维度 | APOE | APP |
| --- | --- | --- |
| Complete-pool top gene-alterations | APOE / point mutations:mutations（2,575）；APOE / normalized variants:rsid normalized（329）；APOE / structural variation:deletion（184）；APOE / normalized variants:dna change（168）；APOE / genetic manipulation:knockout（112） | APP / point mutations:mutations（2,268）；APP / normalized variants:dna change（643）；APP / structural variation:deletion（274）；APP / expression changes:dysregulation（240）；APP / expression changes:underexpression（234） |
| Alteration taxonomy | point mutations:mutations（2,595）；normalized variants:rsid normalized（331）；structural variation:deletion（184）；normalized variants:dna change（170）；genetic manipulation:knockout（112） | point mutations:mutations（2,291）；normalized variants:dna change（643）；structural variation:deletion（274）；expression changes:dysregulation（241）；expression changes:underexpression（234） |
| Top hypotheses | Amyloid Hypothesis（642）；Amyloid Hypothesis,Vascular Hypothesis（601）；Vascular Hypothesis（499）；Amyloid Hypothesis,Neuroinflammation Hypothesis（129）；Amyloid Hypothesis,Tau Protein Hypothesis（105） | Amyloid Hypothesis（2,315）；Amyloid Hypothesis,Tau Protein Hypothesis（408）；Amyloid Hypothesis,Vascular Hypothesis（186）；Amyloid Hypothesis,Neuroinflammation Hypothesis（166）；Amyloid Hypothesis,Oxidative Stress Hypothesis（106） |
| Mechanism strata | vascular/metabolic axis（4,024）；amyloid/tau axis（3,161）；proteostasis/autophagy axis（835）；neuroinflammation and microglia axis（765）；mitochondrial and oxidative stress axis（691）；synaptic and neuronal dysfunction axis（513） | amyloid/tau axis（4,994）；proteostasis/autophagy axis（1,635）；synaptic and neuronal dysfunction axis（1,547）；mitochondrial and oxidative stress axis（907）；vascular/metabolic axis（761）；neuroinflammation and microglia axis（663） |

对照结论：新版 compare 修复了昨天 APOE sample vs APP full-pool 的不公平比较。当前结果支持一个更稳定的对比框架：APOE 的 complete-pool 机制以 vascular/metabolic、amyloid/tau、neuroinflammation 为重要维度；APP 的 complete-pool 机制以 amyloid/tau、proteostasis/autophagy、synaptic/neuronal dysfunction 为核心。人类专家仍优于自动报告的部分，是能把这些分布裁剪成更清晰的 biological contrast，并剔除 ontology 噪声。

## 6. 人类专家策展 vs 新版 skills

| 维度 | 人类专家策展 case | 新版 skills/API case |
| --- | --- | --- |
| 研究问题 | 能把“查证据”转化为 phenotype prioritization、gene recommendation、network interpretation 等科学问题 | 能根据自然语言问题生成 evidence strategy 和 case-study 初稿，但问题设计仍较模板化 |
| 数据覆盖 | 选择性展示最能支持论文论点的数据，完整查询过程不总是展开 | 暴露完整 query-pool 统计、event-level 去重、curated pool 和代表证据，审计性更强 |
| 长尾证据 | 专家能判断少文献候选是否真正有机制价值 | long-tail 被显式保护，但仍需专家判断是否为噪声或新线索 |
| alteration 解读 | 人类会忽略无意义的调控触发词，关注真实 mutation/variant/expression/epigenic/manipulation | 已按 alteration taxonomy 展示前段突变类型/子类型，避免把 cause/reg 当 alteration signature |
| 机制分层 | 能形成 tau cascade、mitochondrial cascade、TREM2-DAP12 axis 等论文级机制叙事 | 能给出 amyloid/tau、mitochondrial、neuroinflammation、synaptic、vascular、proteostasis 等中间层分布 |
| 外部知识 | 能做数据库 overlap、文献背景、人工相关性分级 | 当前未自动完成外部数据库 overlap 和人工 high/medium/low relevance benchmark |
| 可复现性 | 文字论证强，但查询参数、排除项和完整候选池不一定可复现 | 每个 case 保存 query、coverage、curation、expert evidence、原始句子和完整 Markdown 输出 |

## 7. 关键改进是否解决原问题

1. 针对 top-k 丢失长尾的问题：已改善。API 0.4.1 在 `global_statistics` 中暴露完整查询池统计，skills 报告不再把 selected evidence 当成全局分布。
2. 针对去重和采样逻辑的问题：已改善。gene 查询按 alteration taxonomy + phenotype/term + hypothesis 去重；term 查询按 gene + alteration taxonomy + hypothesis 去重；hypothesis 查询按 gene + alteration taxonomy + phenotype/term 去重。
3. 针对 dominant alteration signatures 可读性的问题：已改善。报告聚合的是 `point mutations:mutations`、`normalized variants:dna change`、`expression changes:dysregulation` 等 alteration 类型/子类型，不把 trigger word 或 regulation type 当 alteration。
4. 针对远程可安装性的问题：已改善。skills 通过公共 API 获取 curated pool 与 global statistics，不依赖用户本地 sqlite3。
5. 针对人类专家 case 效果的问题：部分改善。自动层能给出透明 evidence dossier 和 case-study synthesis，但外部数据库对照、网络抽象和最终机制裁剪仍需专家。

## 8. 剩余限制

本轮报告不把新版 expert layer 称为人工金标准。`llm_reviewed` 和 `heuristic_only` 是离线/规则/LLM 辅助注释来源，用于提高 evidence packet 的可读性和采样质量；它们不能替代论文作者对科学意义的最终判断。

mitochondrial dysfunction 的完整统计已经覆盖 4 个 alias 合并池，但当前 case-study 正文仍从有效 term-filtered curated rows 中取代表证据，因此完整分布和正文证据数量必须分开解释。

Neuroinflammation Hypothesis 的 top genes 中仍可能出现数据库/抽取噪声或非核心 gene，因此在写论文级网络模型时，仍需要人工挑选 TREM2、APOE、GRN、MAPT、TNF、APP、NLRP3、TYROBP 等真正可解释的节点。

## 9. 最终判断

新版 API + skills 已经从“自动摘要少量 top evidence”前进到“基于完整查询池的专家证据包”。对 MAPT、APOE、APP、mitochondrial dysfunction 和 Neuroinflammation Hypothesis 这类高频/超高频对象，它能暴露真实分布，保护 long-tail，并给出可审计的代表性证据。

但如果目标是复现论文中的人类专家策展 case，仍应把 skills 输出作为第一层实验记录，而不是最终结论。人类专家需要继续负责：定义研究问题、选择外部对照、判断低频候选、删除 ontology 噪声、构建机制模型，以及决定哪些证据能进入论文叙事。

一句话结论：新版 skills 已经适合批量生成“专家可复核的 AD-Alterome case dossier”；人类专家策展仍负责把 dossier 提炼为可信的科学论证。

## 10. 文件索引

| 文件 | 说明 |
| --- | --- |
| `data/skill_run_metrics.json` | 本报告使用的机器可复查运行指标 |
| `zh_experiment_record.md` | 四个自然语言输入与四份完整自动输出的中文实验记录 |
| `skill_runs/gene_mapt/case_study_report.md` | 案例一：单基因查询 MAPT 的完整自动 case-study 输出 |
| `skill_runs/term_mitochondrial_dysfunction/case_study_report.md` | 案例二：单表型/病理过程查询 mitochondrial dysfunction 的完整自动 case-study 输出 |
| `skill_runs/hypothesis_neuroinflammation/case_study_report.md` | 案例三：假说查询 Neuroinflammation Hypothesis 的完整自动 case-study 输出 |
| `skill_runs/compare_apoe_app/case_study_report.md` | 案例四：基因比较 APOE vs APP 的完整自动 case-study 输出 |
| `../adalterome_human_vs_skills_case_study_2026-06-04/EXPERIMENT_REPORT.md` | 昨天的人类专家 case 对照基线 |
