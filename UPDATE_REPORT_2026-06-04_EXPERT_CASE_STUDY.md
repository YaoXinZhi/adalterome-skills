# 2026-06-04 Expert Case-Study Skill Update

## 背景

这次修订不是把 TF-IDF 推荐、外部数据库 overlap、人工 gold relevance 分级或 AD-LitPathoNet 网络解析并入 skills。修订目标更窄：记录当前 AD-Alterome skills 作为追溯型 evidence report 暴露的问题，并新增一个可选 expert 层，让 skills 在用户明确需要 case study 时更像 AD 病理学专家。

## 当前 Report 版暴露的问题

1. 大证据池基因容易退回 capped sample  
   对 APOE 这类证据量很大的基因，full-pool curation 可能因为接口延迟、超时或服务端限制失败，报告会退回 `api_sentence_sample`。这会降低覆盖度，并可能错过低频但重要的机制证据。

2. 覆盖度风险需要更显式  
   现有 report 版会记录 curation scope 和 coverage ratio，但用户容易只看摘要而忽略 fallback。expert 版需要把覆盖度作为第一层判断：full-pool 可以支撑较强 case-study 叙述；sample fallback 只能支撑探索性结论。

3. 两基因比较需要平衡性检查  
   如果 APOE 一侧是 sample，APP 一侧是 full-pool，直接写强比较会不稳。expert 版必须检查两侧 curation scope 和 coverage ratio，并在不平衡时降级为 exploratory contrast。

4. Long-tail 证据需要专家判断  
   report 版能展示 long-tail signal，但不会判断一个低频候选是噪音、背景，还是有分子病理机制价值。expert 版需要保护“低频但机制上有意思”的证据，而不是只按频次或代表性排序。

5. 机制解读需要生物学裁剪  
   report 版适合证据追溯；case study 需要进一步筛掉泛泛相关句子，优先保留能形成 AD 病理链条的证据，例如 alteration -> molecular process -> cellular pathology -> AD phenotype/hypothesis。

6. 缺少用户科学问题理解层  
   人类专家会先判断用户真正关心的是基因机制、候选靶点、病理过程、假说支持，还是 AD-Alterome 的数据库价值展示。expert 版需要先解释 scientific question，再决定证据筛选策略。

## 新增 Expert 版设计

新增统一 skill：

```text
adalterome-case-study-expert
```

它作为上层专家解释器，不替代现有 report skills。现有 `adalterome-gene-report`、`adalterome-term-report`、`adalterome-hypothesis-report`、`adalterome-compare-report` 继续保留为稳定 report 版。

## Expert 版能力边界

Expert 版做：

- 作为 AD 病理学专家理解用户科学问题。
- 设定证据策略。
- 优先使用 AD-Alterome full-pool curation。
- 检查覆盖度、fallback 和比较平衡性。
- 对 candidate evidence 进行透明 expert score。
- 优先筛选更有 AD 生物学洞察的证据。
- 保护 low-frequency / long-tail 但机制合理的候选。
- 做分子病理机制层面的 biological cut。
- 输出两层报告：case-study narrative + audit appendix。

Expert 版不做：

- TF-IDF 推荐。
- 外部数据库 overlap 评估。
- 人工 gold relevance 分级复现。
- AD-LitPathoNet 网络解析。
- 把 sentence-level evidence 夸大成因果证明。

## 双版本共存

Report 版：

- 用于纯证据包、PMID、原句、API trace、可复现报告。
- 适合交给人类专家继续解读。
- 保持固定结构和低解释风险。

Expert 版：

- 用于 case study、论文级报告、AD 病理学洞察、机制裁剪。
- 适合用户希望 skills 主动扮演专家时使用。
- 输出 expert score，但该 score 是透明筛选依据，不是人工 gold label。

自动选择原则：

- 用户说“证据、追溯、PMID、原句、固定 report、整理给专家看”时，使用 report 版。
- 用户说“case study、专家解读、科学问题、病理机制、论文级、洞察、论证”时，使用 `adalterome-case-study-expert`。

## 备份

本次修改前的 report 版 skills 已备份到：

- `backups/report-version-2026-06-04/skills/`
- `${CODEX_HOME:-$HOME/.codex}/skills/_backups/adalterome-report-version-2026-06-04/skills/`

这些备份包含修改前的 `adalterome-api`、`adalterome-report`、`adalterome-gene-report`、`adalterome-term-report`、`adalterome-hypothesis-report` 和 `adalterome-compare-report`。

## 新增文件

- `skills/adalterome-case-study-expert/SKILL.md`
- `skills/adalterome-case-study-expert/scripts/build_case_study_expert.py`
- `skills/adalterome-case-study-expert/references/case_study_expert_contract.md`

## 验证重点

后续验证应覆盖：

- gene mode smoke test
- compare mode smoke test
- fallback to `api_sentence_sample` 时 coverage warning 是否出现
- two-gene curation scope 不一致时是否标记为 exploratory/imbalanced
- `expert_evidence.json` 是否包含 included、secondary、deprioritized 三层
- `case_study_report.md` 是否保留 PMID、PubMed link 和 original sentence traces
