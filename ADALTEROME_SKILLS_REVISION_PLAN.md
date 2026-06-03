# AD-Alterome Skills 修订计划：Evidence Curation Layer

> Implementation status (2026-06-03): this design record has been implemented through server-side full-pool curation endpoints (`/gene/curation`, `/term/curation`, `/hypothesis/curation`). The final implementation no longer depends on expanding local top-k event samples for report-grade curation.

## 1. 修订背景

当前 AD-Alterome skills 已能完成 API 查询、固定格式报告、gene/term/hypothesis/compare 深度报告生成，但最终报告仍明显受 API top-k 排序影响。

主要问题：

- 排序后证据同质性严重，常集中在少数 PMID、少数宽泛表型或少数重复句。
- 高频 term 和宽泛 disease/background evidence 容易挤占分子机制证据。
- 长尾但有洞察价值的证据很难进入最终总结。
- `EvidenceScore` 容易被误读为证据强度或可信度，不应继续作为用户可见指标或中间层参考指标。
- AD-Alterome 的亮点之一是 genetic alteration 事件抽取与解释，但当前报告没有系统突出 alteration-level evidence。

本计划目标是在 API 返回与最终报告之间增加一个可解释的中间层：`Evidence Curation Layer`。它先对证据进行统计、去重、标签化、分层采样、长尾挖掘和时间线整理，再将精选证据包交给最终报告生成逻辑。

## 2. 核心目标

### 2.1 保留全面统计

保留 API 的全局统计价值：

- event count
- PMID count
- gene count
- term count
- hypothesis count
- top genes
- top terms
- top hypotheses
- shared/unique terms and hypotheses in comparison

这些统计应作为 evidence landscape，而不是直接决定最终证据选择。

### 2.2 提升研究洞察

最终报告应更接近人类专家人工分析返回数据后的输出：

- 告诉用户哪些证据只是高频背景，哪些证据真正值得细看。
- 明确解释每条精选证据为什么值得看。
- 突出 genetic alteration、molecular mechanism、model evidence、long-tail signals。
- 呈现机制发展脉络，而不是简单堆叠证据句。
- 提醒文献密度偏差、重复报道偏差、宽泛 term 偏差和数据库标签解释边界。

### 2.3 避免误导性指标

`EvidenceScore` 不再用于：

- 用户可见表格
- evidence ranking
- evidence sampling
- case selection
- report interpretation

如果 raw API 出于兼容性暂时保留该字段，skills 层和中间层仍应忽略它。最终报告用更可解释的标签和理由替代分数。

## 3. 总体架构

建议流程从当前：

```text
API top-k results -> report builder -> final report
```

修订为：

```text
API overview + server-side full-pool curation package
  -> Evidence Curation Layer
  -> curated evidence package
  -> report builder
  -> final expert-style report
```

中间层输出一个结构化对象：

```json
{
  "query": {},
  "global_statistics": {},
  "dominant_clusters": [],
  "mechanism_clusters": [],
  "alteration_insights": [],
  "evidence_type_groups": [],
  "high_value_molecular_evidence": [],
  "long_tail_signals": [],
  "chronological_trajectory": [],
  "distribution_notes": [],
  "recommended_cases": [],
  "curation_notes": []
}
```

最终报告只消费这个 curated package，而不是直接消费 API top-k。报告不应单独加入 `Bias, Coverage, and Limitations` 模块；如果需要讨论发表密度或重复报道偏差，应在解释段落中结合真实返回分布简短说明。

## 4. 中间层输入

### 4.1 Overview 输入

按任务类型读取不同 overview：

| 报告类型 | Overview endpoint |
| --- | --- |
| gene report | `/gene/overview` |
| term report | `/term/overview` |
| hypothesis report | `/hypothesis/overview` |
| compare report | `/compare/genes` plus per-gene overview |

Overview 用于全局统计和背景定位，不直接作为证据强弱依据。

### 4.2 Evidence pool 输入

中间层需要比当前 top-k 更大的候选池。建议：

| 场景 | 初始候选池 |
| --- | --- |
| 快速报告 | top 50 |
| 标准深度报告 | top 100-200 |
| 专家深度报告 | top 300-500 |

如果 API 支持分页，优先使用分页；如果仅支持 `top_k`，先通过较大 `top_k` 拉取候选池。

### 4.3 字段输入

中间层重点使用这些字段：

- `Gene`
- `Entrez`
- `AlterationMention`
- `AlterationID`
- `AlterationType`
- `TriggerWord`
- `RegType`
- `TermMention`
- `TermID`
- `TermName`
- `TermType`
- `AncestorName`
- `PMID`
- `Sentence`
- `RichSentence`
- `Journal`
- `Year`
- `DiseaseRelated`
- `MechanismProvided`
- `MechanismReason`
- `Hypothesis`
- `HypothesisReason`
- `ExtendedExplanation`
- `RelevantToAD`
- `Event`

中间层不使用 `EvidenceScore`。

## 5. Evidence Curation Layer 功能设计

### 5.1 去重与去中心化

目的：避免少数 PMID、少数句子、少数宽泛 term 垄断报告。

规则建议：

- 同一 `PMID + Sentence` 只保留一次。
- 同一 `PMID` 在最终精选证据中默认最多贡献 2 条。
- 同一 `TermName` 在机制精选证据中默认最多贡献 3 条。
- 同一 `Hypothesis` cluster 默认最多贡献 3 条。
- 如果一个 PMID 同时覆盖多个重要机制，可保留多条，但需标注 `same_pmid_cluster`。

输出标签：

- `deduplicated`
- `same_pmid_cluster`
- `dominant_report`
- `overrepresented_cluster`

报告呈现方式：

```text
This evidence belongs to a dominant PMID cluster and is shown as a representative record, not as independent repeated support.
```

### 5.2 宽泛 term 降权与具体 term 提权

宽泛 term 不删除，因为它们对全局统计有价值，但不应主导机制证据。

降权 term 示例：

- Alzheimer Disease
- Alzheimer disease
- Dementia
- protein
- chromosome
- Sporadic
- Onset
- All
- developmental process
- metabolic process
- biological process

提权 term 示例：

- mitochondrial dysfunction
- protein aggregation
- tau phosphorylation
- amyloid precursor protein cleavage
- microglial activation
- NLRP3 inflammasome
- synaptic dysfunction
- long-term potentiation
- oxidative stress
- autophagy
- mitophagy
- neuroinflammation
- insulin resistance
- lipid metabolism
- vascular dysfunction

输出标签：

- `broad_term`
- `specific_phenotype`
- `molecular_process`
- `pathway_specific`
- `cellular_process`

报告呈现方式：

| 标签 | 用户含义 |
| --- | --- |
| `broad_term` | 适合作为背景统计，不适合作为机制结论核心证据 |
| `molecular_process` | 具有分子或细胞过程信息，值得进入机制解读 |
| `pathway_specific` | 指向明确通路或病理过程 |

### 5.3 分子机制标签化

中间层应对每条证据打机制标签。标签可以来自 term、sentence、hypothesis、event 和 alteration fields。

建议一级机制标签：

- `amyloid_processing`
- `tau_pathology`
- `neuroinflammation`
- `mitochondrial_dysfunction`
- `oxidative_stress`
- `autophagy_mitophagy`
- `synaptic_dysfunction`
- `vascular_metabolism`
- `lipid_metabolism`
- `proteostasis_aggregation`
- `metal_ion_homeostasis`
- `cholinergic_glutamatergic`
- `microbiota_gut_brain_axis`
- `genetic_alteration`
- `cell_death_stress_response`

可由关键词、term 和 hypothesis 混合判定。例如：

| 标签 | 关键词或字段信号 |
| --- | --- |
| `tau_pathology` | tau, MAPT, phosphorylation, tangle, tauopathy, PHF1 |
| `mitochondrial_dysfunction` | mitochondria, TOMM40, PINK1, PARK7, mitophagy, mitochondrial dysfunction |
| `neuroinflammation` | microglia, NLRP3, TNF, IL-1beta, inflammatory, neuroinflammation |
| `proteostasis_aggregation` | aggregation, misfolded, proteasome, protein clearance |
| `synaptic_dysfunction` | synapse, LTP, potentiation, neurotransmission, dendritic |

输出字段：

```json
{
  "mechanism_tags": ["tau_pathology", "synaptic_dysfunction"],
  "mechanism_tag_reason": "Sentence mentions MAPT P301L, p-tau, misfolded tau, and long-term potentiation."
}
```

### 5.4 Genetic alteration 事件解读

这是 AD-Alterome 的核心亮点，应单独成为中间层模块。

重点字段：

- `AlterationMention`
- `AlterationID`
- `AlterationType`
- `TriggerWord`
- `RegType`
- `Gene`
- `Event`
- `Sentence`

中间层应识别：

- mutation
- variant
- SNP
- allele
- haplotype
- phosphorylation
- methylation
- acetylation
- expression change
- upregulation/downregulation
- cleavage
- aggregation
- misfolding
- knockout/knockdown/silencing
- overexpression
- transgenic model

建议输出：

```json
{
  "alteration_profile": {
    "has_alteration": true,
    "alteration_type": "mutation",
    "alteration_mention": "MAPT P301L",
    "regulation_or_trigger": "harbouring",
    "event_summary": "MAPT P301L mutation linked to p-tau, misfolded tau, interneuron loss, and altered LTP.",
    "interpretation_level": "model_mechanism",
    "why_it_matters": "Connects a specific genetic alteration to tau pathology and synaptic physiology."
  }
}
```

Alteration insight 标签：

- `specific_mutation`
- `risk_allele`
- `haplotype_signal`
- `expression_change`
- `post_translational_modification`
- `proteolytic_processing`
- `aggregation_event`
- `model_perturbation`
- `therapeutic_perturbation`

报告中单独增加：

```text
Genetic Alteration Highlights
```

每个 highlight 包括：

- alteration
- gene
- disease context
- mechanism consequence
- PMID
- original sentence
- caveat

### 5.5 证据类型分类

中间层应判断每条 evidence 属于什么证据类型。

建议证据类型：

- `genetic_association`
- `specific_mutation_case`
- `familial_ad_variant`
- `risk_allele_or_haplotype`
- `expression_or_regulation`
- `post_translational_modification`
- `pathway_mechanism`
- `animal_model`
- `cell_model`
- `human_cohort`
- `clinical_observation`
- `therapeutic_intervention`
- `review_or_background`
- `database_or_general_statement`

证据类型不是互斥的，一条证据可以有多个标签。

输出示例：

```json
{
  "evidence_type_tags": ["animal_model", "specific_mutation_case", "pathway_mechanism"],
  "evidence_type_reason": "Sentence describes JNPL3 transgenic mice carrying MAPT P301L mutation and downstream tau/synaptic phenotypes."
}
```

报告呈现方式：

| 标签 | 解释 |
| --- | --- |
| `animal_model` | 来自动物模型，机制性较强但需注意外推限制 |
| `review_or_background` | 适合作背景，不应作为强机制结论 |
| `specific_mutation_case` | 涉及具体突变或变异，适合进入 alteration highlight |

### 5.6 高价值分子证据筛选

高价值证据不是高 `EvidenceScore`，而是具有以下特征：

- 具体 gene + alteration + phenotype/term。
- 句子含有机制动词或因果/扰动结构。
- 包含细胞模型、动物模型、人群队列或治疗干预。
- 指向明确 molecular pathway。
- term 不是过宽泛背景词。
- 年份较新或能补足机制演化脉络。
- 来自低频但有解释价值的 cluster。

建议规则分数只用于内部排序，不在报告中展示为单一分数。

内部维度：

| 维度 | 含义 |
| --- | --- |
| `specificity_signal` | term 和句子是否具体 |
| `mechanism_signal` | 是否有明确机制 |
| `alteration_signal` | 是否有 genetic alteration 或调控事件 |
| `model_signal` | 是否有 animal/cell/human/intervention context |
| `diversity_signal` | 是否能补足当前证据多样性 |
| `long_tail_signal` | 是否来自低频但有信息量的 cluster |
| `recency_signal` | 是否反映近年机制趋势 |

报告中展示为标签和理由，不展示一个综合分数。

### 5.7 长尾证据雷达

长尾证据用于发现低频但有价值的信号。

候选条件：

- term frequency 低，但 term 具体。
- gene frequency 低，但 sentence 机制明确。
- hypothesis combination 少见，但有合理机制连接。
- 新近年份出现。
- 有具体 mutation、variant、model 或 perturbation。
- 不属于 dominant PMID cluster。

输出结构：

```json
{
  "long_tail_signals": [
    {
      "signal_type": "rare_specific_term",
      "gene": "TOMM40",
      "term": "mitochondrial dysfunction",
      "mechanism_tags": ["mitochondrial_dysfunction", "neuroinflammation"],
      "why_it_matters": "Links TOMM40 variation to mitochondrial dysfunction and microglial activation.",
      "pmid": "36835494",
      "sentence": "..."
    }
  ]
}
```

报告小节：

```text
Long-tail Signals Worth Reviewing
```

每条 long-tail signal 需要说明：

- 为什么不是简单低频噪音。
- 它补充了哪个主流机制之外的角度。
- 需要怎样的后续验证。

### 5.8 时间线机制演化

中间层按年份整理机制变化。

建议时间窗口：

- `pre_2010`
- `2010_2015`
- `2016_2020`
- `2021_present`

如果数据集中年份集中，也可动态分位数分段。

每个时间窗口总结：

- top mechanism tags
- representative evidence
- emerging alteration patterns
- newly appearing terms
- caveats

输出示例：

```json
{
  "chronological_trajectory": [
    {
      "period": "2021_present",
      "dominant_mechanisms": ["mitochondrial_dysfunction", "neuroinflammation"],
      "emerging_patterns": ["microglial activation", "NLRP3 inflammasome", "specific TOMM40 variants"],
      "representative_pmids": ["36835494"]
    }
  ]
}
```

报告小节：

```text
Mechanism Trajectory Over Time
```

### 5.9 证据冲突与分布提示

中间层应记录数据分布哪里偏，但最终实验报告不单独输出 `Bias, Coverage, and Limitations` 模块。

偏差类型：

- `pmid_concentration_bias`
- `term_broadness_bias`
- `review_background_bias`
- `literature_density_bias`
- `hypothesis_label_bias`
- `missing_year_or_journal_metadata`
- `weak_sentence_specificity`
- `comparison_imbalance`
- `duplicate_sentence_bias`

输出示例：

```json
{
  "distribution_notes": [
    {
      "bias_type": "pmid_concentration_bias",
      "description": "A small number of PMIDs contribute repeated high-ranked records.",
      "impact": "May inflate apparent support for one mechanism cluster.",
      "mitigation": "Use per-PMID caps and mechanism-stratified sampling."
    }
  ]
}
```

报告中应明确区分：

- database-level label
- sentence-level support
- expert interpretation generated by skills

### 5.10 Case-style 输出

最终报告应加入 case-style 模块，用于输出专家风格案例。

建议 case 类型：

- `genetic_alteration_case`
- `molecular_mechanism_case`
- `long_tail_case`
- `emerging_recent_case`
- `comparison_contrast_case`
- `bias_caveat_case`

Case 格式：

```text
Case: MAPT P301L links tau pathology to synaptic physiology

Why it is worth reading:
Specific mutation, animal model, tau pathology, and synaptic phenotype are connected in one sentence.

Evidence:
PMID: ...
Original sentence: ...

Mechanistic interpretation:
...

Caveat:
...

Follow-up question:
...
```

每份深度报告建议输出：

- 2-4 个 gene report cases
- 3-5 个 term report cases
- 3-5 个 hypothesis report cases
- compare report 每个 gene 2 个 cases，加 2 个 contrast cases

## 6. 标签体系

### 6.1 用户可见标签

用户可见标签应短、直观、有解释力。

| 标签 | 含义 |
| --- | --- |
| `Genetic alteration` | 涉及具体突变、变异、等位基因、单倍型或调控事件 |
| `Molecular mechanism` | 句子包含明确分子或细胞机制 |
| `Specific phenotype` | term 具体，适合机制解读 |
| `Model evidence` | 来自动物、细胞或实验模型 |
| `Human evidence` | 来自人群、临床或患者相关观察 |
| `Intervention evidence` | 涉及药物、干预、silencing、knockout 等 |
| `Long-tail signal` | 低频但有潜在洞察价值 |
| `Recent signal` | 近年出现或更新的机制信号 |
| `Dominant cluster` | 高频或重复报道簇的代表 |
| `Broad background` | 宽泛背景证据，适合作统计不适合作强机制结论 |
| `Bias warning` | 存在文献密度、重复、宽泛 term 或标签偏差 |

### 6.2 内部标签

内部标签用于采样和组织，不一定全部展示：

- mechanism tags
- alteration tags
- evidence type tags
- specificity tags
- diversity tags
- bias tags
- trajectory tags

### 6.3 标签解释输出

每条精选证据不只显示标签，还要显示 `why_selected`：

```json
{
  "visible_tags": ["Genetic alteration", "Model evidence", "Molecular mechanism"],
  "why_selected": "This sentence connects MAPT P301L mutation with p-tau, misfolded tau, interneuron loss, and long-term potentiation in a transgenic mouse model."
}
```

## 7. 报告结构修订

### 7.1 Gene report 新结构

```text
1. Query Scope and Data Provenance
2. Global Evidence Landscape
3. Dominant Evidence Clusters
4. Genetic Alteration Highlights
5. Mechanism-stratified Evidence Map
6. High-value Molecular Evidence
7. Long-tail Signals Worth Reviewing
8. Mechanism Trajectory Over Time
9. Expert-style Cases
10. Bias, Caveats, and Interpretation Boundaries
11. Follow-up Research Questions
```

### 7.2 Term report 新结构

```text
1. Query Scope and Data Provenance
2. Term-centered Evidence Landscape
3. Top Genes and Hypothesis Distribution
4. Mechanism Clusters Under This Term
5. Genetic Alteration and Event Signals
6. Representative Molecular Evidence by Cluster
7. Long-tail Gene/Term Signals
8. Chronological Development of Mechanism Context
9. Expert-style Cases
10. Bias and Follow-up Priorities
```

### 7.3 Hypothesis report 新结构

```text
1. Query Scope and Hypothesis Definition
2. Hypothesis Evidence Landscape
3. Dominant Gene and Term Clusters
4. Genetic Alteration Signals Supporting This Hypothesis
5. Mechanism-stratified Support
6. Sentence-level vs Database-label Support
7. Long-tail and Emerging Support Patterns
8. Chronological Support Trajectory
9. Expert-style Cases
10. Bias, Caveats, and Testable Questions
```

### 7.4 Compare report 新结构

```text
1. Query Scope and Comparison Frame
2. Side-by-side Evidence Landscape
3. Shared Mechanism Clusters
4. Gene A-specific Alteration and Mechanism Signals
5. Gene B-specific Alteration and Mechanism Signals
6. Long-tail Contrast Signals
7. Chronological Contrast
8. Expert-style Comparison Cases
9. Literature-density Bias and Interpretation Boundaries
10. Follow-up Comparative Questions
```

## 8. Token 消耗控制

### 8.1 原则

中间层尽量用脚本完成，不把大证据池直接交给 LLM。

LLM 应只看到：

- global statistics summary
- curated evidence package
- selected original sentences
- curation reasons
- report contract

### 8.2 推荐规模

| 报告模式 | API 候选池 | curated evidence | cases | 预计上下文消耗 |
| --- | --- | --- | --- | --- |
| quick | 50 | 12-20 | 2-3 | 6k-12k tokens |
| standard | 100-200 | 25-40 | 4-6 | 12k-25k tokens |
| expert | 300-500 | 40-70 | 6-10 | 25k-45k tokens |

### 8.3 压缩策略

- 原始 sentence 只保留精选证据。
- 非精选证据只保留统计计数。
- 重复 PMID 和重复 sentence 只保留代表。
- 每个 mechanism cluster 限制 evidence 数量。
- long-tail signals 单独限制数量。
- case-style 输出优先使用最强可解释证据。

## 9. 技术实施计划

### Phase 1: 输出层清理

目标：先消除误导。

任务：

- 从所有 report table 中移除 `EvidenceScore`。
- 所有 summary/report/evidence-md 输出不展示 `EvidenceScore`。
- scripts 内部不再使用 `EvidenceScore` 进行排序或解释。
- 保留 `EvidenceQualityScore` 与否需再讨论；如果保留，应改名或解释为 sentence informativeness，而非证据强度。

验收：

- 所有报告中不出现 `EvidenceScore`。
- 报告中没有 “score 越高证据越强” 的暗示。

### Phase 2: Curation package 原型

目标：新增中间层结构化输出。

任务：

- 新增 curation script 或模块，例如 `scripts/curate_evidence.py`。
- 输入：overview JSON + evidence JSON。
- 输出：`data/curation.json`。
- 实现基础去重、term broadness 标记、mechanism tags、alteration tags、evidence type tags。

验收：

- gene/term/hypothesis/compare builder 都能生成 `curation.json`。
- `curation.json` 中每条精选证据有 `visible_tags` 和 `why_selected`。

### Phase 3: 分层采样与长尾雷达

目标：解决同质性和长尾缺失。

任务：

- per-PMID cap。
- per-term cap。
- mechanism-stratified sampling。
- long-tail candidate detection。
- broad term downweighting。
- molecular/specific term upweighting。

验收：

- MAPT 报告不再被少数重复 PMID 主导。
- term/hypothesis 报告中每个主要机制 cluster 有代表证据。
- 报告出现 long-tail signals 小节。

### Phase 4: Genetic alteration insight

目标：突出 AD-Alterome 的 alteration/event 优势。

任务：

- 解析 `AlterationMention`、`AlterationType`、`TriggerWord`、`RegType`、`Event`。
- 生成 `alteration_insights`。
- 在 gene/term/hypothesis/compare 报告中加入 alteration highlights。

验收：

- MAPT P301L、APOE allele、APP mutation 等能进入 alteration highlight。
- 每个 highlight 有 mechanism consequence 和 caveat。

### Phase 5: 时间线与 case-style 报告

目标：形成专家分析效果。

任务：

- 按年份窗口聚合 mechanism tags。
- 识别 recent/emerging signals。
- 生成 expert-style cases。
- 修改各 report contract。

验收：

- 每份深度报告包含 mechanism trajectory。
- 每份深度报告包含 2-6 个 case-style insight。
- case 中包含 why worth reading、evidence、interpretation、caveat、follow-up question。

### Phase 6: 回归测试与文档

目标：保证稳定性。

任务：

- 更新 README。
- 更新 SKILL.md。
- 添加测试样例。
- 生成标准测试报告。
- 对比旧版和新版输出差异。

验收：

- 6 个 skills 全部通过自动测试。
- 新版报告更少重复、更高机制密度、更明确标注偏差。

## 10. 需要进一步讨论的问题

### 10.1 API 层是否移除 EvidenceScore

选择 A：raw API 直接移除。

- 优点：彻底避免误解。
- 风险：可能破坏旧脚本或外部用户。

选择 B：raw API 保留但 deprecated，skills 完全隐藏和忽略。

- 优点：兼容性好。
- 风险：API 用户仍可能看到该字段。

选择 C：新增 public response profile，默认隐藏 `EvidenceScore`，debug/raw 模式才返回。

- 优点：兼顾兼容性和用户体验。
- 风险：API 需要多一层输出控制。

建议先采用 B 或 C。

### 10.2 EvidenceQualityScore 是否保留

当前 `EvidenceQualityScore` 比 `EvidenceScore` 更接近 sentence informativeness，但也可能被用户误解。

可选方案：

- 保留但改名为 `SentenceInformativeness`。
- 只在内部使用，不在用户报告展示。
- 展示为标签而非数字，例如 `High sentence specificity`。

建议：最终报告不展示数字，只展示标签和 `why_selected`。

### 10.3 机制标签是规则驱动还是 LLM 辅助

规则驱动：

- 成本低。
- 稳定可复现。
- 适合第一版。

LLM 辅助：

- 标签更灵活。
- 可识别复杂语义。
- token 成本更高，稳定性需测试。

建议第一版使用规则驱动，后续可加入可选 LLM refinement。

### 10.4 Long-tail 的定义

需要确定长尾阈值：

- term frequency 小于 top term 中位数？
- 不在 top 10 terms/hypotheses？
- PMID cluster 不重复？
- 年份新近？
- 是否必须有 alteration 或 mechanism 标签？

建议先用组合规则，不用单一频率阈值。

## 11. 推荐的第一轮实施范围

第一轮不要一次做满所有功能，建议先做最能改善报告质量的最小闭环：

1. 所有报告移除 `EvidenceScore`。
2. 新增 `curation.json`。
3. 实现去重、per-PMID cap、broad term 降权。
4. 实现机制标签和 evidence type 标签。
5. 实现 genetic alteration highlights。
6. 报告中展示标签和 `why_selected`。
7. 增加 long-tail signals 小节。

这 7 项完成后，报告质量会有明显跃迁；时间线机制演化和复杂 case-style 输出可以作为第二轮增强。

## 12. 预期新版报告效果

新版报告不再只是：

```text
Top evidence rows for MAPT...
```

而是更像：

```text
MAPT has a large AD-Alterome evidence landscape dominated by tau pathology and dementia-related terms. However, the most useful mechanistic evidence is not the most frequent background evidence. After deduplication and mechanism-stratified curation, several high-value signals stand out:

1. MAPT P301L links a specific genetic alteration to p-tau, misfolded tau, interneuron loss, and long-term potentiation changes in a transgenic model.
2. MAPT-related protein aggregation appears as a molecular process signal distinct from broad dementia annotations.
3. Several lower-frequency records connect tau pathology with neuroinflammation, mitochondrial/autophagy hypotheses, or synaptic physiology and should be reviewed as long-tail mechanistic leads.
```

最终目标是让用户看到：

- 数据全局有多大。
- 高频证据是什么。
- 高频证据有什么偏。
- 哪些机制证据真正值得读。
- 哪些 genetic alteration 事件最有解释价值。
- 哪些长尾信号值得追。
- 这个领域的机制认识如何随年份发展。
- 哪些结论可以说，哪些不能说。
