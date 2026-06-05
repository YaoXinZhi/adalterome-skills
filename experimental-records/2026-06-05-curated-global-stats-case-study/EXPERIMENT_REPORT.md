# AD-Alterome 2026-06-05 新版 Skills 实验报告

生成日期：2026-06-05
实验目录：`experimental-records/2026-06-05-curated-global-stats-case-study/`

## 1. 实验结论

本次实验验证的是新版 AD-Alterome API 与 skills 在“完整查询池统计 + curated evidence + expert case-study 初稿”这一工作流中的表现。核心结论是：新版系统已经从过去的 top-k evidence summary，推进到可以支撑专家复核的 case dossier。它不只返回少量证据句子，而是同时暴露完整匹配池统计、event-level 去重结果、curated pool 规模、代表性证据、long-tail 信号、机制分层和原始 PubMed 句子。

四个测试问题分别覆盖单基因、单表型/病理过程、单假说和双基因比较。结果显示：MAPT、mitochondrial dysfunction、Neuroinflammation Hypothesis、APOE vs APP 都能走到 `offline_full_query_pool_prescreened`，不再只是 50 条 capped API sample。对于高频对象，报告能够显示完整分布；对于长尾证据，报告能够保留低频但有机制价值的候选；对于双基因比较，报告能够检查 APOE 与 APP 的 coverage balance。

需要强调的是，skills 生成的是可审计证据包和 case-study 初稿，不是论文作者式最终结论。它已经适合批量生成“人类专家可复核的 AD-Alterome case dossier”；最终科学论证仍需要专家完成研究问题定义、外部数据库对照、ontology 噪声删除、机制模型抽象和论文叙事。

## 2. 实验版本与材料

| 项目 | 内容 |
| --- | --- |
| 实验日期 | 2026-06-05 |
| 公共 API | `http://117.72.176.137/api/adalterome` |
| API 版本 | `0.4.1` |
| 实验数据记录 | `data/skill_run_metrics.json` |
| 完整自动输出 | `skill_runs/*/case_study_report.md` |
| API/skills global statistics 提交 | `40694dd Expose complete curated query statistics in reports` |
| 2026-06-05 后续 skills 实现提交 | `1f05a4a Make AD-Alterome skills easier to route and audit` |
| 2026-06-05 更新日记提交 | `6fa5f78 Document unified AD-Alterome skill routing and cache` |

本实验的核心数据来自 `data/skill_run_metrics.json`。该文件已经汇总了四个 case 的 coverage、curation、global statistics、expert evidence summary 和代表性证据指标。

后续同一天完成的 unified entrypoint 与 local raw-data cache 更新，没有重新生成四个 case 的原始实验数据；它属于 skills 使用层的改进，应作为 2026-06-05 最终 skills 状态记录，而不是混入本次 case metrics。

## 3. 实验问题设计

| 案例 | 类型 | 自然语言输入 | 自动输出文件 |
| --- | --- | --- | --- |
| 案例一 | 单基因 | MAPT evidence如何支持tau相关AD病理机制，以及新版curated pool是否能给出比人工筛选更透明的证据包？ | `skill_runs/gene_mapt/case_study_report.md` |
| 案例二 | 单表型/病理过程 | mitochondrial dysfunction作为表型/病理过程时，AD-Alterome如何推荐和解释相关基因及长尾机制证据？ | `skill_runs/term_mitochondrial_dysfunction/case_study_report.md` |
| 案例三 | 单假说 | Neuroinflammation Hypothesis的证据池是否能重建TREM2/APOE等炎症相关AD病理线索？ | `skill_runs/hypothesis_neuroinflammation/case_study_report.md` |
| 案例四 | 双基因比较 | APOE和APP在AD病理机制中有哪些共享和特异的遗传改变-表型-假说模式？ | `skill_runs/compare_apoe_app/case_study_report.md` |

这四个问题覆盖了 AD-Alterome 最重要的使用场景：gene-centered evidence dossier、phenotype/process-centered gene recommendation、hypothesis-centered mechanism mapping，以及 cross-gene comparison。

## 4. 自动运行结果总览

| Case | Curation scope | Raw matched events | Event-unique before curation | Curated pool | Case pool rows | Unique PMIDs | Main evidence | 备注 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| MAPT | `offline_full_query_pool_prescreened` | 27,921 | 8,014 | 2,687 | 2,687 | 1,636 | 16 | coverage ratio 9.62%，提示 high-frequency gene 经过强下采样 |
| mitochondrial dysfunction | `offline_full_query_pool_prescreened` | 4,159 | 1,907 | 858 | 244 | 152 | 16 | 4 个 alias 合并后统计；正文基于 term-filtered curated rows |
| Neuroinflammation Hypothesis | `offline_full_query_pool_prescreened` | 34,060 | 20,229 | 5,225 | 5,225 | 3,030 | 16 | 超高频假说，完整池统计对理解分布很关键 |
| APOE | `offline_full_query_pool_prescreened` | 13,322 | 4,025 | 1,840 | 1,839 | 1,159 | compare 共 18 | 与 APP coverage scope 平衡 |
| APP | `offline_full_query_pool_prescreened` | 18,639 | 4,994 | 2,300 | 2,300 | 1,592 | compare 共 18 | 与 APOE coverage scope 平衡 |

这里必须区分三层数据：

1. `raw matched events` 表示完整查询池中匹配的原始事件记录。
2. `event-unique before curation` 表示按查询类型做 event-level 去重后的完整统计。
3. `main evidence` 是最终 case-study 正文保留的少量代表证据，不代表全局分布。

## 5. Case 结果分析

### 5.1 MAPT 单基因

MAPT case 的完整查询池包含 27,921 条 raw events，event-level 去重后为 8,014 条，候选高质量事件 6,553 条，最终 curated pool 为 2,687 条。正文保留 16 条 expert-included evidence，全部为 `llm_reviewed`，ExpertOverallScore 均为 5，并且全部带有 long-tail signal。

完整池的主导机制是 amyloid/tau axis（8,014），其次是 proteostasis/autophagy axis（3,078）、synaptic and neuronal dysfunction axis（2,926）、mitochondrial and oxidative stress axis（1,418）、neuroinflammation and microglia axis（1,003）和 vascular/metabolic axis（676）。

| 维度 | 主要结果 |
| --- | --- |
| Top phenotype/process features | protein、Alzheimer Disease、Neurodegeneration、phosphorylation、biosynthetic process、Dementia |
| Top gene-alterations | MAPT / point mutations:mutations；MAPT / normalized variants:dna change；MAPT / structural variation:deletion；MAPT / expression changes:dysregulation；MAPT / epigenic changes:phosphorylation |
| Evidence types | molecular_mechanism（3,434）；model_or_intervention（2,998）；alteration_evidence（1,169）；cellular_or_pathway_process（413） |
| 正文机制 | tau/amyloid、synaptic dysfunction、proteostasis/autophagy、neuroinflammation、mitochondrial dysfunction |

实验判断：MAPT 报告已经能提供比普通 top-k summary 更可靠的专家证据底稿。它既能呈现完整分布，又能把高频通用证据和低频机制证据分开。但它还不是 MAPT phenotype prioritization benchmark；如果要复现论文中的人工 case，需要继续加入 phenotype recommendation ranking、外部数据库 overlap 和人工 high/medium/low relevance 评价。

### 5.2 Mitochondrial Dysfunction 单表型/病理过程

mitochondrial dysfunction case 使用了 4 个 query values：`Mitochondrial dysfunction`、`Mitochondrial inheritance [HP:0001427]`、`Abnormality of mitochondrial metabolism [HP:0003287]` 和 `mitochondrial injury [MESH:D028361]`。完整 alias 合并池包含 4,159 条 raw events，event-unique 为 1,907 条，candidate_event_count 为 889 条，curated_pool_count 为 858 条。

当前 case-study builder 进入正文前的有效 term-filtered pool 为 244 条，event-unique rows 为 228 条，unique PMIDs 为 152。正文保留 16 条 main evidence，其中 11 条为 `heuristic_only`，5 条为 `llm_reviewed`，16 条都被标记为 long-tail included。

| 维度 | 主要结果 |
| --- | --- |
| Complete-pool top genes | MAPT、PINK1、APP、SNCA、SIRT3、PPIF、MFN2、DAPK2、SOD1、PSEN1 |
| Top gene-alterations | MAPT / point mutations:mutations；APP / point mutations:mutations；PINK1 / point mutations:mutations；PSEN1 / point mutations:mutations |
| Dominant hypotheses | Mitochondrial autophagy hypothesis；Oxidative stress hypothesis + mitochondrial autophagy hypothesis；Amyloid + mitochondrial autophagy |
| Mechanism strata | mitochondrial and oxidative stress axis（1,907）；amyloid/tau axis（1,373）；proteostasis/autophagy axis（903） |

实验判断：新版完整池统计已经能把 PINK1、SNCA、SOD1、DAPK2 等人类专家关心的 mitochondrial pathology genes 拉回可见范围，这比 capped sample 明显更适合 gene recommendation。当前不足是，正文代表证据仍更偏向“机制可读句子”，没有自动输出 established / underappreciated / low-literature mechanistic candidate 三层推荐分类。

### 5.3 Neuroinflammation Hypothesis 单假说

Neuroinflammation Hypothesis case 是本次最能体现完整池价值的场景。完整查询池包含 34,060 条 raw events，event-unique 为 20,229 条，candidate_event_count 为 20,173 条，curated_pool_count 为 5,225 条。正文保留 16 条 main evidence，全部为 `llm_reviewed`，全部为 long-tail included。

完整池的 top genes 包括 TREM2、MAPT、APOE、APP、TNF、IL6 等。机制分层中 neuroinflammation and microglia axis 为 20,229 条，是该假说的主轴；同时 amyloid/tau、synaptic and neuronal dysfunction、mitochondrial/oxidative stress、vascular/metabolic 和 proteostasis/autophagy 都有明显交叉。

| 维度 | 主要结果 |
| --- | --- |
| Top genes | TREM2、MAPT、APOE、APP、TNF、IL6 |
| Top phenotype/process features | Alzheimer Disease、AD、expression、protein、inflammatory response、activation |
| Top gene-alterations | TREM2 / point mutations:mutations；TREM2 / normalized variants:dna change；APOE / point mutations:mutations；MAPT / normalized variants:dna change |
| Mechanism strata | neuroinflammation and microglia axis（20,229）；amyloid/tau axis（10,105）；synaptic and neuronal dysfunction axis（6,365） |

实验判断：该 case 证明新版 skills 已能把 neuroinflammation 的完整 evidence landscape 展开，尤其能捕捉 TREM2、APOE、MAPT、APP、TNF 等核心节点。但它仍只是 evidence map，不会自动构建 AD-LitPathoNet 风格网络，也不会自动提炼 TREM2-DAP12 axis 这样的机制模型。

### 5.4 APOE vs APP 双基因比较

APOE vs APP case 的关键是比较平衡性。新版实验中，两侧都走到 `offline_full_query_pool_prescreened`，balance status 为 `balanced`。APOE 完整池包含 13,322 条 raw events、4,025 条 event-unique rows、1,840 条 curated pool；APP 完整池包含 18,639 条 raw events、4,994 条 event-unique rows、2,300 条 curated pool。

| 维度 | APOE | APP |
| --- | --- | --- |
| Top gene-alterations | APOE / point mutations:mutations；APOE / normalized variants:rsid normalized；APOE / structural variation:deletion；APOE / normalized variants:dna change；APOE / genetic manipulation:knockout | APP / point mutations:mutations；APP / normalized variants:dna change；APP / structural variation:deletion；APP / expression changes:dysregulation；APP / expression changes:underexpression |
| Dominant hypotheses | Amyloid Hypothesis；Amyloid + Vascular；Vascular；Amyloid + Neuroinflammation | Amyloid Hypothesis；Amyloid + Tau；Amyloid + Vascular；Amyloid + Neuroinflammation；Amyloid + Oxidative Stress |
| Mechanism strata | vascular/metabolic axis（4,024）；amyloid/tau axis（3,161）；proteostasis/autophagy axis（835）；neuroinflammation and microglia axis（765） | amyloid/tau axis（4,994）；proteostasis/autophagy axis（1,635）；synaptic and neuronal dysfunction axis（1,547）；mitochondrial and oxidative stress axis（907） |
| Evidence types | molecular_mechanism（1,515）；cellular_or_pathway_process（1,037）；model_or_intervention（795）；alteration_evidence（678） | molecular_mechanism（2,263）；model_or_intervention（1,733）；alteration_evidence（609）；cellular_or_pathway_process（389） |

实验判断：新版 compare 修复了旧实验中 APOE sample vs APP full-pool 的不公平问题。当前结果支持更稳定的机制对比：APOE 更偏 vascular/metabolic、amyloid/tau、neuroinflammation；APP 更偏 amyloid/tau、proteostasis/autophagy、synaptic/neuronal dysfunction。专家仍需要进一步把这些分布裁剪成论文级 biological contrast。

## 6. 本轮实验验证了什么

1. 完整查询池统计是必要的。只看 selected evidence 会误以为正文证据就是全局分布；`global_statistics` 能把 raw_event_count、event_unique_count、curated_pool_count、top genes、top phenotype/process features、top gene-alterations、mechanism strata 全部暴露出来。
2. query-specific 去重逻辑有效。gene 查询按 alteration taxonomy + phenotype/process + hypothesis 去重；term 查询按 gene + alteration taxonomy + hypothesis 去重；hypothesis 查询按 gene + alteration taxonomy + phenotype/process 去重；compare 对每个 gene 独立处理。
3. alteration taxonomy 展示更可读。报告聚合的是 `point mutations:mutations`、`normalized variants:dna change`、`expression changes:dysregulation` 等突变类型/子类型，而不是 trigger word 或 regulation type。
4. long-tail 保护是有价值的。四个 case 的正文证据都保留了 long-tail evidence，这有助于避免高频宽泛 phenotype 或高频 PMID 垄断报告。
5. LLM-reviewed 与 heuristic-only 应分开解释。MAPT 和 Neuroinflammation 正文均为 LLM-reviewed；mitochondrial dysfunction 和 APOE vs APP 混有 heuristic-only，需要专家复核时优先看 annotation source。

## 7. 当前限制

1. Expert score 不是人工金标准。它只能表示证据对 case-study 的可用性，不能替代论文作者判断。
2. ontology 噪声仍存在。例如一些 top phenotype/process features 可能过宽、过泛，或不是人类专家会用于主叙事的术语。
3. 外部数据库 overlap 尚未自动化。mitochondrial dysfunction case 中最有论文价值的部分，是 AD-Alterome 与既有 gene-phenotype databases 的对照；当前 skills 没有自动完成这一步。
4. 网络解释尚未自动化。Neuroinflammation 能给出 TREM2/APOE 等核心节点，但不能自动构建网络模型或机制 axis。
5. 本次实验数据在 unified entrypoint 和 local raw-data cache 更新之前生成，因此 `skill_runs/*` 目录没有本次最终版本会新增的 `data/cache_manifest.json`。

## 8. 后续建议

下一步可以把 skills 从“报告生成器”继续推进为“AD-Alterome 专家工作流”：

1. 增加 phenotype/process recommendation mode，输出 established、underappreciated、low-literature mechanistic candidates 三层。
2. 增加 hypothesis network mode，把 top genes、mechanism strata 和代表证据组织成可解释网络。
3. 在报告中把 statistics 和 recommendation 分开：前者忠实呈现完整分布，后者基于 expert annotation 和问题语境给出候选排序。
4. 对 `llm_reviewed`、`heuristic_only`、future human-reviewed evidence 做更清楚的提示，让专家知道哪些结论更值得信任。
5. 将本次新增的 unified entrypoint 和 raw-data cache 用于后续实验，确保每次报告都能保存原始 API payload 与 cache manifest。

## 9. 文件索引

| 文件 | 说明 |
| --- | --- |
| `data/skill_run_metrics.json` | 本报告使用的机器可复查指标 |
| `zh_experiment_record.md` | 四个自然语言输入与完整自动输出 |
| `skill_runs/gene_mapt/case_study_report.md` | MAPT case-study 完整自动输出 |
| `skill_runs/term_mitochondrial_dysfunction/case_study_report.md` | mitochondrial dysfunction case-study 完整自动输出 |
| `skill_runs/hypothesis_neuroinflammation/case_study_report.md` | Neuroinflammation Hypothesis case-study 完整自动输出 |
| `skill_runs/compare_apoe_app/case_study_report.md` | APOE vs APP case-study 完整自动输出 |
| `HUMAN_EXPERT_COMPARISON_REPORT.md` | 本次实验与人类专家 case 的专门比较报告 |
