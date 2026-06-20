# AD-Alterome Knowledge Synthesis 与人类专家 Case 对比报告

日期：2026-06-20

## 1. 对比目的

本报告用于说明本次 `adalterome-knowledge-synthesis` 更新后，AI 输出与人类专家 case 分析之间的关系。

核心定位不是让 AI 直接替代专家撰写机制结论，而是让 AI 把 AD-Alterome 的复杂证据组织成可追溯、可评分、可复核的 evidence organization object。人类专家再基于该对象评价其准确性、深度、广度、启发性和幻觉风险。

因此，论文中的问题应从：

> AI 能否直接写出可信 AD 机制 case？

调整为：

> AI 加 AD-Alterome 是否能可靠组织复杂疾病证据，并提高专家形成 case 判断的效率和覆盖度？

## 2. 对比对象

### 2.1 AI knowledge synthesis packet

本次更新生成的 AI 对象包括：

- `knowledge_packet.md`
- `evidence_map.md`
- `expert_review_sheet.tsv`
- `evaluation_record.json`
- `provenance_manifest.json`
- raw API/cache JSON

AI 输出主要负责：

- 保留 PMID、PubMed URL 和原始句子。
- 展示 curated pool、event-unique row、PMID coverage 等覆盖度信息。
- 按 gene、alteration、phenotype/process、hypothesis 和 mechanism strata 组织证据。
- 保护 long-tail evidence，避免只呈现高频宽泛证据。
- 生成专家评分表，让人类专家逐条评分。

AI 输出不负责：

- 证明某个 AD 病理机制成立。
- 替代专家判断证据是否真正支持机制链条。
- 直接生成论文正文中的最终 case 结论。

### 2.2 人类专家 case

人类专家 case 的核心价值是：

- 判断证据是否真正具备 AD 病理学意义。
- 判断 broad phenotype、clinical association、model evidence 和 molecular mechanism evidence 的可信层级。
- 识别 AI 可能过度连接、错误归因或遗漏背景知识的地方。
- 将证据转化为论文中可承担责任的机制解释。

人类专家 case 应被用作 AI 输出的评测基准，而不是被 AI 输出替代。

## 3. 对比维度

| 维度 | AI knowledge synthesis packet | 人类专家 case |
| --- | --- | --- |
| 主要功能 | 组织和呈现复杂证据 | 判断和解释证据意义 |
| 输出性质 | 可评分评测对象 | 专家判断或论文候选结论 |
| 证据覆盖 | 依赖 AD-Alterome API、curated pool、long-tail rescue | 依赖专家阅读、领域经验和必要补充文献 |
| 可追溯性 | 强制保留 PMID、PubMed URL、原始句子和 raw payload | 取决于专家记录方式 |
| 长尾证据 | 通过 scoring 和 sampling 主动暴露 | 专家判断其是否值得纳入 |
| 幻觉控制 | 通过 non-claims、review sheet、原始句子约束 | 通过专家知识和人工复核控制 |
| 机制深度 | 提供 mechanism strata 和候选组织 | 专家判断机制链条是否成立 |
| 论文使用方式 | 作为被评测的 AI 证据组织结果 | 作为人工评价、修正和最终解释依据 |

## 4. 四个测试案例的专家对比要点

### 4.1 PSEN1 single-gene entry

AI packet 已提供：

- PSEN1 curated pool rows: 2398
- event-unique rows: 2398
- unique PMIDs: 1481
- organized evidence rows: 6
- expert review sheet rows: 6

专家应重点评价：

- AI 是否优先呈现了与 familial AD、amyloid processing、synaptic/neuronal pathology 等相关的高价值证据。
- AI 是否把宽泛的 AD association 误写成机制证明。
- 原始句子是否足以支撑 packet 中的 evidence grouping。

预期论文表述：

PSEN1 case 用于评估 AI 能否在高证据量基因中组织出可追溯的 review candidates，而不是证明 PSEN1 的 AD 机制。

### 4.2 APOE vs APP multi-gene entry

AI packet 已提供：

- APOE curated pool rows: 1844
- APP curated pool rows: 2310
- balance status: balanced
- organized evidence rows: 6
- review sheet 同时包含 APOE 与 APP

专家应重点评价：

- AI 是否公平呈现两个基因，而不是被某一侧证据量支配。
- AI 是否能区分 APOE 相关 lipid transport、neuroinflammation、vascular/metabolic context 与 APP 相关 amyloid processing 等证据组织方向。
- AI 是否避免把“比较组织”写成“机制强弱排名”。

预期论文表述：

APOE vs APP case 用于测试 AI 是否能做 balanced comparative evidence organization。

### 4.3 MAPT phenotype landscape recommendation entry

AI packet 已提供：

- MAPT curated pool rows: 2700
- unique PMIDs: 1640
- organized evidence rows: 6
- long-tail flag、mechanism strata 和 AI organization reasons

专家应重点评价：

- AI 是否避免被 Alzheimer Disease 等宽泛表型支配。
- AI 是否能保留与 tau pathology、neuronal degeneration、synaptic impairment、neuroinflammation 或其他细粒度 phenotype/process 相关的证据。
- AI 是否能帮助专家快速形成 MAPT phenotype landscape 的审阅方向。

预期论文表述：

MAPT case 用于测试 AI 是否能在高频 broad phenotype 背景下提供 coverage-first 的 evidence landscape。

### 4.4 TREM2-DAP12 hypothesis/network entry

AI packet 已提供：

- TREM2 curated pool rows: 1019
- TYROBP curated pool rows: 189
- Neuroinflammation Hypothesis curated pool rows: 5304
- balance status: balanced
- organized evidence rows: 6

专家应重点评价：

- AI 是否正确把 TYROBP 作为 DAP12 相关证据入口处理。
- AI 是否在 TREM2、TYROBP 和 neuroinflammation hypothesis 三类证据之间保持平衡。
- AI 是否把 evidence topology 误表达为因果网络。
- AI 是否能帮助专家识别 microglial activation、immune signaling、phagocytosis、synaptic injury 等候选机制线索。

预期论文表述：

TREM2-DAP12 case 用于测试 AI 是否能组织 hypothesis/network review object，而不是自动推断系统生物学因果网络。

## 5. 建议评测设计

### 5.1 评测条件

建议至少比较五类输出：

1. Generic LLM without AD-Alterome
2. Generic LLM plus ordinary RAG
3. Frequency top-k AD-Alterome evidence
4. AD-Alterome without long-tail rescue
5. AD-Alterome knowledge synthesis skill

所有条件应使用相同自然语言问题、相同模型或同等级模型、相同输出长度预算、相同时间预算和相同评分表。

### 5.2 专家评分维度

专家评分使用 `expert_review_sheet.tsv` 中的 1-5 分字段：

- traceability
- accuracy
- breadth
- depth
- organization usefulness
- long-tail usefulness
- hallucination or overclaim risk
- inspiration
- review efficiency
- overall usefulness

### 5.3 统计建议

正式论文中可报告：

- 每个维度的均值和标准差。
- 不同方法之间的 paired comparison。
- 多评审者一致性。
- 专家完成 review 所需时间。
- 幻觉或过度推断案例数。
- 专家 qualitative comments 的主题归纳。

## 6. 当前结论

本次更新已经完成“用于专家评测的 AI evidence organization object”构建：

- 四个案例均成功生成 packet、map、review sheet、evaluation record 和 provenance manifest。
- 输出明确声明 AI 结果不等于机制证明。
- 专家评分表已经具备评价深度、广度、准确性、幻觉风险、启发性和效率的字段。
- AI 输出与人类专家 case 的关系已经转为“被评测对象”与“评测者/最终判断者”的关系。

尚未完成的是实际专家评分与统计分析。这部分需要由临床/科研专家、AD 研究人员和生物医学学生完成盲评或半盲评后，再进入论文结果统计。
