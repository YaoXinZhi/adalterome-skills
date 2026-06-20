# AD-Alterome Knowledge Synthesis Skills 中文评估报告

日期：2026-06-20

## 1. 本次评估目标

本次更新的目标不是让 skills 直接生成可作为论文正文的 AD 机制结论，而是把 AD-Alterome 的结构化证据组织成可追溯、可筛选、可由专家评分的 knowledge synthesis packet。

新的论文定位为：

> AI for Biomedical Knowledge Synthesis：AI 是否能可靠组织复杂疾病证据，而不是 AI 是否能直接猜测或证明疾病机制。

因此，本次评估重点检查：

- 是否能生成 researcher-facing knowledge packet。
- 是否能保留 PMID、PubMed URL、原始句子和 raw payload provenance。
- 是否能输出专家评分表。
- 是否能支持 single-gene、multi-gene、recommendation、hypothesis/network 四类 analytical patterns。
- 是否明确声明 AI 输出是专家评测对象，不是最终生物学结论。

配套的人类专家 case 对比报告见：

`experimental-records/2026-06-20-knowledge-synthesis-evaluation/zh_expert_case_comparison_report.md`

## 2. 实施内容

本次新增了 `adalterome-knowledge-synthesis` skill。

该 skill 输出：

- `knowledge_packet.md`
- `evidence_map.md`
- `expert_review_sheet.tsv`
- `evaluation_record.json`
- `provenance_manifest.json`
- `data/query.json`
- `data/coverage.json`
- `data/knowledge_synthesis.json`
- `data/ad_expert_pruning.json`
- `data/cache_manifest.json`
- target-specific overview/evidence/curation JSON

同时更新：

- `README.md`
- `DESIGN.md`
- `skills/adalterome/SKILL.md`
- `skills/adalterome-api/SKILL.md`
- `skills/adalterome-case-study-expert/SKILL.md`

旧的 `adalterome-case-study-expert` 保留为兼容模式；新的论文主路径改为 `adalterome-knowledge-synthesis`。

## 3. 专家评分表设计

`expert_review_sheet.tsv` 每一行对应一条 AI-organized evidence item。

自动填充字段包括：

- EvidenceID
- AnalyticalPattern
- Target
- PMID
- PubMedURL
- Gene
- AlterationTaxonomy
- AlterationMention
- PhenotypeProcess
- Hypothesis
- EvidenceType
- MechanismStrata
- IsLongTailEvidence
- AIOrganizationScore
- AIOrganizationDecision
- AIOrganizationReasons
- OriginalSentence

留给专家填写的评分维度包括：

- TraceabilityScore_1_5
- AccuracyScore_1_5
- BreadthScore_1_5
- DepthScore_1_5
- OrganizationUsefulness_1_5
- LongTailUsefulness_1_5
- HallucinationOrOverclaimRisk_1_5
- Inspiration_1_5
- ReviewEfficiency_1_5
- OverallUsefulness_1_5
- CannotJudge
- ReviewerNotes
- ReviewStatus

## 4. 测试案例

所有测试输出位于：

`experimental-records/2026-06-20-knowledge-synthesis-evaluation/`

### 4.1 Single-gene entry: PSEN1

自然语言问题：

> Generate a PSEN1 knowledge synthesis packet for expert evaluation.

运行命令：

```bash
python3 skills/adalterome-knowledge-synthesis/scripts/build_knowledge_synthesis.py --gene PSEN1 --pattern single_gene --output-dir experimental-records/2026-06-20-knowledge-synthesis-evaluation/psen1_single_gene --candidate-limit 20 --organized-limit 6
```

结果：

- Analytical pattern: `single_gene`
- Pre-merge candidates: 36
- Post-merge candidates: 36
- Organized evidence rows: 6
- Review sheet rows: 6
- Target curation pool rows: PSEN1 = 2398
- Event-unique rows: PSEN1 = 2398
- Unique PMIDs: PSEN1 = 1481
- Balance status: not applicable

验收：

- 成功生成 knowledge packet、evidence map、expert review sheet、evaluation record 和 provenance manifest。
- 输出中明确声明该 packet 不证明 AD 机制，AI-organized groups 是专家评测对象。

### 4.2 Multi-gene entry: APOE vs APP

自然语言问题：

> Organize AD-Alterome evidence comparing APOE and APP for expert review.

运行命令：

```bash
python3 skills/adalterome-knowledge-synthesis/scripts/build_knowledge_synthesis.py --gene-a APOE --gene-b APP --pattern multi_gene --output-dir experimental-records/2026-06-20-knowledge-synthesis-evaluation/apoe_app_multi_gene --candidate-limit 12 --organized-limit 6
```

结果：

- Analytical pattern: `multi_gene`
- Pre-merge candidates: 53
- Post-merge candidates: 53
- Organized evidence rows: 6
- Review sheet rows: 6
- Target curation pool rows: APOE = 1844; APP = 2310
- Event-unique rows: APOE = 1844; APP = 2310
- Unique PMIDs: APOE = 1167; APP = 1606
- Balance status: balanced

验收：

- 成功生成双基因 evidence organization。
- Expert review sheet 同时包含 APOE 与 APP evidence rows。
- Coverage note 已改为 knowledge synthesis，不再使用旧的 case-study synthesis 表述。

### 4.3 Recommendation entry: MAPT phenotype landscape

自然语言问题：

> Organize the MAPT phenotype landscape for expert review.

运行命令：

```bash
python3 skills/adalterome-knowledge-synthesis/scripts/build_knowledge_synthesis.py --gene MAPT --pattern recommendation --question "Organize the MAPT phenotype landscape for expert review." --output-dir experimental-records/2026-06-20-knowledge-synthesis-evaluation/mapt_phenotype_landscape --candidate-limit 20 --organized-limit 6
```

结果：

- Analytical pattern: `recommendation`
- Pre-merge candidates: 25
- Post-merge candidates: 25
- Organized evidence rows: 6
- Review sheet rows: 6
- Target curation pool rows: MAPT = 2700
- Event-unique rows: MAPT = 2700
- Unique PMIDs: MAPT = 1640
- Balance status: not applicable

验收：

- 成功按 recommendation/landscape 方式组织 MAPT phenotype evidence。
- 输出保留 long-tail flag、mechanism strata、AI organization reasons 和原始句子，便于专家筛选后续综述方向。

### 4.4 Hypothesis/network entry: TREM2-DAP12 neuroinflammatory axis

自然语言问题：

> Organize AD-Alterome evidence for the TREM2-DAP12 neuroinflammatory axis as a hypothesis/network review object.

运行命令：

```bash
python3 skills/adalterome-knowledge-synthesis/scripts/build_knowledge_synthesis.py --gene-set TREM2 TYROBP --hypothesis "Neuroinflammation Hypothesis" --axis "TREM2-DAP12 neuroinflammatory axis" --pattern hypothesis_network --output-dir experimental-records/2026-06-20-knowledge-synthesis-evaluation/trem2_dap12_hypothesis_network --candidate-limit 12 --organized-limit 6
```

结果：

- Analytical pattern: `hypothesis_network`
- Pre-merge candidates: 69
- Post-merge candidates: 69
- Organized evidence rows: 6
- Review sheet rows: 6
- Target curation pool rows: TREM2 = 1019; TYROBP = 189; Neuroinflammation Hypothesis = 5304
- Event-unique rows: TREM2 = 1019; TYROBP = 189; Neuroinflammation Hypothesis = 5304
- Unique PMIDs: TREM2 = 486; TYROBP = 57; Neuroinflammation Hypothesis = 3063
- Balance status: balanced

调试记录：

- 初次运行时，大型 Neuroinflammation Hypothesis pool 更容易支配 top evidence。
- 已修复为 hypothesis/network pattern 使用 target-balanced selection，确保 TREM2、TYROBP 和 hypothesis context 都能进入 review sheet。

验收：

- 成功生成 gene-set + hypothesis 混合路径。
- Expert review sheet 中同时包含 TREM2、TYROBP 和 Neuroinflammation Hypothesis target rows。
- 输出明确作为 hypothesis/network review object，而不是 AI 直接推断系统生物学因果网络。

## 5. 自动验证结果

已完成：

- `python3 -m py_compile` 覆盖所有 skill scripts。
- 四个 knowledge synthesis smoke/evaluation cases 均成功运行。
- 每个 case 均生成 required output files。
- 每个 case 均生成 `expert_review_sheet.tsv`。
- 每个 case 均生成 `evaluation_record.json`，包含 reviewer types、scoring dimensions、recommended baselines、fairness controls 和 non-claims。
- 检索确认新的 knowledge synthesis 输出中不再出现旧的 `case-study synthesis` 表述。
- 检索确认 generated packets 包含 `does not prove an AD mechanism`、`does not replace expert review`、`review candidates, not manuscript conclusions` 等边界声明。

## 6. 是否达到预期效果

本次修订达到了预期效果：

1. Skills 定位已从“AI 生成专家式机制 narrative”转向“AI 组织复杂疾病证据供专家评测”。
2. 新增 `adalterome-knowledge-synthesis` 支持论文中规划的多种 analytical patterns。
3. 输出结构不再是单一 narrative report，而是 knowledge packet、evidence map、expert review sheet、evaluation record 和 provenance manifest。
4. 专家评分表已经具备深度、广度、准确性、幻觉/过度推断风险、启发性、效率等维度。
5. 生成内容中明确包含 non-claims，避免将 AI 输出误当成论文正文或机制证明。
6. 现有 AD-Alterome API、full-pool curation、long-tail rescue、PMID provenance 和 local cache 机制被完整复用。

## 7. 仍需人工完成的部分

以下内容不能由 skill 自动替代：

- 专家实际评分。
- 将 `expert_review_sheet.tsv` 与人类专家 case 判断逐项对照。
- 多评审者一致性分析。
- 与 generic LLM、generic RAG、frequency top-k 等 baseline 的正式盲评。
- 对评测结果进行统计检验和论文图表整理。

## 8. 推荐下一步

正式论文实验建议使用更大的 candidate limit：

- PSEN1: 200
- APOE vs APP: 200 per gene
- MAPT phenotype landscape: 200
- TREM2-DAP12 axis: 200-500, 视 API 延迟和 coverage 需求调整

正式评测建议至少比较：

- generic LLM
- generic LLM + ordinary RAG
- frequency top-k AD-Alterome
- AD-Alterome without long-tail rescue
- AD-Alterome knowledge synthesis skill

专家类型建议包括：

- 临床/转化 AD 专家
- AD 或神经退行性疾病科研人员
- 生物医学研究生或博士后
