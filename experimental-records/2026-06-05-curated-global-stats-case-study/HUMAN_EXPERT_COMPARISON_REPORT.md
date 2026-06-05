# AD-Alterome Skills 与人类专家 Case Study 比较报告

生成日期：2026-06-05
自动实验目录：`experimental-records/2026-06-05-curated-global-stats-case-study/`
人类专家基线：`reports/adalterome_human_vs_skills_case_study_2026-06-04/EXPERIMENT_REPORT.md`

## 1. 总体判断

人类专家 case study 和 AD-Alterome skills 自动 case study 的目标不同。人类专家做的是“科学论证”：定义问题、选择证据、引入外部数据库、裁剪机制、组织成论文可读叙事。新版 skills 做的是“可审计证据包”：保留完整查询池统计、去重策略、curated pool、representative evidence、long-tail 信号、annotation source、PubMed 原句和机制分层。

2026-06-05 的新版 skills 已经明显接近人类专家分析前的“证据准备层”。它能在 MAPT、mitochondrial dysfunction、Neuroinflammation Hypothesis 和 APOE vs APP 四个 case 中暴露真实数据分布，不再把 top-k selected evidence 当作全局事实。但它仍无法替代人类专家：外部知识对照、低频候选价值判断、网络机制抽象、ontology 噪声删除和论文级叙事仍需要人工完成。

最合理的使用方式是混合工作流：skills 先生成完整、可复查、可追溯的 case dossier；人类专家再把 dossier 提炼成高可信度科学论证。

## 2. 对比基线

### 2.1 人类专家 case 的任务类型

人类专家在论文和前一轮评估中主要完成四类任务：

| Case | 人类专家任务本质 | 关键人工判断 |
| --- | --- | --- |
| MAPT | Gene-centric phenotype prioritization | 人工评估 MAPT top 50 phenotypes：60.0% 高相关，30.0% 中等相关；把 tau pathology、microtubule、NFT、synaptic plasticity 等组织成 tau hypothesis 叙事 |
| mitochondrial dysfunction | Phenotype-centric gene recommendation | 将 SOD1、PINK1、SNCA 视为已知强相关；LRRK2、PRKN、POLGARF 视为 underappreciated；DAPK2、HSPB8、GDNF、NRF1 视为低频但机制有价值 |
| Neuroinflammation Hypothesis | Hypothesis-aware network interpretation | 识别 TREM2/APOE hub，整合 GRN、MAPT、TNF、APP、NLRP3 等路径，并形成 TREM2-DAP12 axis 机制模型 |
| APOE vs APP | Cross-gene mechanistic comparison | 判断 APOE 更偏 immune/systemic/vascular-metabolic，APP 更偏 amyloid/metabolic/neurocognitive/synaptic |

### 2.2 新版 skills 的任务类型

新版 skills 更像 evidence dossier builder：

- 从完整查询池暴露 raw matched events、event-unique records 和 curated pool count。
- 按 query type 做 event-level 去重。
- 保存 top genes、phenotype/process features、gene-alteration pairs、hypotheses、alteration taxonomy、evidence types 和 mechanism strata。
- 选出少量代表证据，保留 PMID、PubMed link、原始句子和 annotation source。
- 在 expert case-study 层给出初步机制 synthesis，但不声称替代人类专家。

## 3. 总体能力矩阵

| 维度 | 人类专家 case | 新版 skills case |
| --- | --- | --- |
| 研究问题定义 | 强。能把“查证据”转化为 phenotype prioritization、gene recommendation、network interpretation 或机制比较 | 中等。能识别 gene/term/hypothesis/compare，但问题框架仍较模板化 |
| 数据覆盖透明度 | 中等。论文叙事通常只展示关键结果，不完整暴露候选池 | 强。显示 raw matched events、event-unique、curated pool、PMID 数和 coverage |
| 证据可追溯性 | 中等。能引用证据，但不一定保存完整 API request 与排除项 | 强。保留原始句子、PubMed link、curation JSON 和 metrics |
| 长尾证据处理 | 强。专家能判断少文献候选是否有机制价值 | 中上。能保护 long-tail，但还不能可靠判断其科学重要性 |
| alteration 解读 | 强。人类自然关注真实 mutation/variant/expression/epigenic/manipulation | 中上。已按 alteration taxonomy 汇总，不把 trigger/reg 当 alteration |
| 外部数据库对照 | 强。mitochondrial dysfunction case 中外部 overlap 是关键论据 | 弱。当前 skills 尚未自动接入外部数据库 overlap |
| 网络机制抽象 | 强。能形成 TREM2-DAP12 axis、tau cascade 等论文级模型 | 弱到中等。能给出 mechanism strata，但不能自动构建网络 |
| 批量化 | 弱。人工 case 成本高 | 强。四类 case 可批量运行 |
| 论文可写性 | 强。能直接变成 Results/Discussion 叙事 | 中等。需要人工裁剪后才能进入论文 |

## 4. Case-by-Case 对比

### 4.1 MAPT

人类专家在 MAPT case 中证明的是 AD-Alterome 的 phenotype prioritization 能产生生物学上合理的 tau-centered phenotype ranking。重点不只是 MAPT 有多少证据，而是 top phenotypes 是否能解释 tau pathology、microtubule function、neurofibrillary tangles、synaptic plasticity、cell senescence 等 AD 相关机制。

新版 skills 从完整池看到 27,921 条 raw events、8,014 条 event-unique records 和 2,687 条 curated pool。它能展示 MAPT 的主导 alteration signatures，如 `point mutations:mutations`、`normalized variants:dna change`、`structural variation:deletion`、`expression changes:dysregulation` 和 `epigenic changes:phosphorylation`。机制分层也准确地把 MAPT 放在 amyloid/tau、proteostasis/autophagy、synaptic dysfunction、mitochondrial dysfunction 和 neuroinflammation 交叉区域。

对比判断：

- skills 优于人工文本的地方：完整分布、去重、PMID 原句、long-tail 和 alteration taxonomy 更透明。
- 人类专家优于 skills 的地方：能判断 top phenotype 的 biological relevance，并把 phenotype list 转化为 tau hypothesis 叙事。
- 最佳组合：用 skills 生成 MAPT evidence landscape，再由专家人工标注 high/medium/low relevance 并写成 phenotype prioritization case。

### 4.2 Mitochondrial Dysfunction

人类专家在 mitochondrial dysfunction case 中做的是 gene recommendation，而不是单纯 evidence summary。专家把 AD-Alterome 结果与既有 gene-phenotype association databases 对照，强调既有库中的 176 个相关基因只有少部分与 AD-Alterome 中 AD-specific associations 重叠，并将候选基因分成已知强相关、underappreciated 和低频机制候选。

新版 skills 的完整池统计显示 4,159 条 raw events、1,907 条 event-unique records、858 条 curated pool。top genes 中出现 MAPT、PINK1、APP、SNCA、SIRT3、PPIF、MFN2、DAPK2、SOD1、PSEN1，已经能覆盖很多人类专家关心的 mitochondrial pathology genes。机制分层也清楚显示 mitochondrial/oxidative stress、amyloid/tau、proteostasis/autophagy 的交叉。

对比判断：

- skills 已解决过去 sample 丢失长尾的问题，能把 PINK1、SNCA、SOD1、DAPK2 等拉回完整分布。
- skills 还不能自动完成 external database overlap，因此无法直接复现人类专家的 gene recommendation 论证。
- skills 没有自动将基因分成 established、underappreciated 和 low-literature mechanistic candidate。
- 最佳组合：用 skills 提供完整候选池和机制证据，再由专家结合外部数据库和 AD 背景知识做候选分层。

### 4.3 Neuroinflammation Hypothesis

人类专家在 neuroinflammation case 中做的是 network interpretation。核心是识别 TREM2/APOE hub，连接 GRN、MAPT、TNF、APP、NLRP3 等节点，最终形成 TREM2-DAP12 axis 和 microglia/inflammatory signaling 的机制叙事。

新版 skills 从完整池看到 34,060 条 raw events、20,229 条 event-unique records 和 5,225 条 curated pool。top genes 包含 TREM2、MAPT、APOE、APP、TNF、IL6 等；top gene-alterations 包含 TREM2、APOE、MAPT、APP 的多类 mutation/variant signatures；机制分层中 neuroinflammation and microglia axis 覆盖 20,229 条 event-unique records。

对比判断：

- skills 已经能稳定找回 neuroinflammation 的核心节点和完整 evidence landscape。
- skills 能提示该假说与 amyloid/tau、synaptic dysfunction、mitochondrial stress、vascular/metabolic 和 proteostasis/autophagy 的交叉。
- skills 仍不会自动构建网络边、hub ranking、axis model 或 macro-to-micro mechanism flow。
- 最佳组合：skills 作为 network interpretation 的证据底稿，专家用它筛选节点和原句，再构建 TREM2-DAP12 等机制模型。

### 4.4 APOE vs APP

人类专家在 APOE vs APP case 中做的是机制差异裁剪。APOE 与 APP 都是 AD 重要基因，但专家会把 APOE 解释为更偏 immune/systemic/vascular-metabolic abnormalities，把 APP 解释为更偏 amyloid/metabolic/neurocognitive/synaptic dysfunction。

新版 skills 的比较已经通过 coverage balance：APOE 和 APP 均为 `offline_full_query_pool_prescreened`，不再是一侧 sample、一侧 full-pool。APOE 完整池为 13,322 raw events、4,025 event-unique records、1,840 curated pool；APP 完整池为 18,639 raw events、4,994 event-unique records、2,300 curated pool。

对比判断：

- skills 能公平展示两侧完整分布，并且明确 APOE 的 vascular/metabolic axis 更强，APP 的 amyloid/tau、proteostasis/autophagy 和 synaptic/neuronal dysfunction 更强。
- skills 能列出两侧主要 alteration taxonomy：APOE 以 point mutations、rsid normalized、deletion、dna change、knockout 等为主；APP 以 point mutations、dna change、deletion、expression dysregulation/underexpression 等为主。
- 人类专家仍需要删除 ontology 噪声，避免把 broad phenotype 当作强机制差异。
- 最佳组合：skills 用于 coverage-balanced evidence audit，专家用于撰写最终 biological contrast。

## 5. 新版 Skills 相比人类专家的优势

1. 更可复现。每个 case 都有 metrics、coverage、curation、expert evidence 和完整 Markdown 输出。
2. 更适合审计。报告能看到完整池规模、event-level 去重、curated pool 和 selected evidence 的关系。
3. 更不容易被 top-k 误导。完整池统计与正文代表证据分开呈现。
4. 更适合批量探索。同一套 workflow 可以快速跑 gene、phenotype/process、hypothesis 和 compare。
5. 更容易发现偏倚。比如 broad background、dominant PMIDs、high-frequency alteration signatures 和 long-tail evidence 都可以显式展示。
6. 更容易交给下一轮 LLM 或人类专家继续处理，因为每条证据都有结构化字段和 PubMed 原句。

## 6. 人类专家仍不可替代的部分

1. 研究问题定义。专家知道什么时候该做 phenotype prioritization，什么时候该做 gene recommendation，什么时候该做 network interpretation。
2. 外部数据库对照。当前 skills 还不能自动复现 mitochondrial dysfunction case 中最关键的 external gene-phenotype overlap。
3. 生物学取舍。专家能判断低频候选是噪声、偶然背景，还是值得写入论文的机制线索。
4. 网络模型抽象。TREM2-DAP12 axis、tau cascade、mitochondrial cascade 这类机制模型目前仍需要专家构建。
5. 论文叙事。skills 输出是证据包，不能直接等同于 Results/Discussion。
6. 错误发现。专家能识别 ontology term、phenotype label 或抽取句子中不适合进入主叙事的内容。

## 7. 对 AD-Alterome 发表价值的影响

新版 skills 的价值不是替代人类专家写论文，而是提高 AD-Alterome 的“可被 LLM 时代使用和复核”的能力。它可以证明 AD-Alterome 不只是一个静态数据库，而是能被自然语言查询、完整统计、分层采样、长尾保护、机制注释和专家报告工作流调用的证据系统。

对于论文发表，建议把二者关系表述为：

- AD-Alterome provides AD-specific event-level evidence and curated query-pool statistics.
- Skills provide a reproducible evidence-to-report interface for LLM-era interrogation.
- Human experts remain responsible for biological interpretation, external validation, and manuscript-level synthesis.

这种定位更稳。它不会夸大自动报告的专家能力，同时突出 AD-Alterome 在可复现、可审计、可交互分析上的优势。

## 8. 推荐混合工作流

1. 用户用自然语言提出问题。
2. unified `adalterome` skill 判断任务类型：gene、phenotype/process、hypothesis、compare 或 expert case-study。
3. skills 查询 API，保留完整 statistics、curated evidence、raw payload cache 和 PubMed 原句。
4. skills 输出第一版 case dossier，明确 statistics 与 recommendation 分层。
5. 人类专家检查 annotation source、long-tail evidence、broad phenotype、dominant PMIDs 和机制分层。
6. 人类专家加入外部数据库 overlap、网络解释和论文级 biological cut。
7. 最终形成可发表 case study，并保留 skills 输出作为审计附录。

## 9. 结论

2026-06-05 的新版 skills 已经能胜任“人类专家前置证据整理”这一角色。它的强项是完整、透明、可复现、可批量；人类专家的强项是判断、裁剪、建模和写作。

如果目标是生成可信的 AD-Alterome case study，最优方案不是二选一，而是让 skills 先生成完整证据包，再由人类专家完成最终科学论证。这样既保留数据库和 LLM 工作流的速度与审计性，也保留人工专家对 AD 病理机制的判断力。

一句话总结：新版 skills 已经接近“专家可复核的自动 case dossier”；人类专家 case 仍是“可发表科学论证”的最后一公里。
