# 2026-06-07 Skill Implementation Audit and Consistency Fixes

## 背景

本次更新对 AD-Alterome skills 做了一轮实现与文档一致性检查，重点确认 GitHub README、skill metadata、报告输出模块和脚本行为是否一致。

## 修复内容

1. 统一 phenotype/process 文案。
   - 将用户可见的 `Top phenotypes` 调整为 `Top phenotype/process features`。
   - 将 `AD-Alterome Term Report` 的 agent 显示名调整为 `AD-Alterome Phenotype / Process Report`。
   - 保留 CLI/API 参数 `--term` 与 `/term/*` endpoint，以兼容现有 API contract。

2. 修正 hypothesis 名称。
   - 统一入口中将不存在于当前 API hypothesis list 的 `Mitochondrial Cascade Hypothesis` 改为 `Mitochondrial Autophagy Hypothesis`。

3. 澄清 EvidenceScore 与 EvidenceQualityScore。
   - skill-facing 报告继续隐藏和忽略原始 `EvidenceScore`。
   - 轻量 API 输出中可显示 `EvidenceQualityScore`，但明确它只是句子可用性信号，不是证据强度或因果证明。

4. 对齐 expert case-study 的 cache provenance。
   - `adalterome-case-study-expert` 的 curation coverage scope 现在会写入 `local_raw_payload_cache` 和 `local_cache_hit`。
   - expert case-study 的 curation request 复用统一的 `selected_limit` 上限规则。

5. 修正 GitHub README 与实际仓库结构。
   - 将根目录示例命令从 `python scripts/query_adalterome.py ...` 改为 `python skills/adalterome-api/scripts/query_adalterome.py ...`。
   - 更新 `DESIGN.md`，明确 deep reports 优先使用 `/gene/curation`、`/term/curation` 和 `/hypothesis/curation`，事件 endpoint 只是 capped fallback。

## 风险评估

- 本次没有改变公共 API contract。
- 本次没有改变 query 参数名、输出 JSON 文件名或报告目录结构。
- 修改主要影响用户可见文案、metadata、审计字段和 README/DESIGN 描述。
- 对 report 内容的科学解释只做措辞澄清，不改变 evidence selection 逻辑。

## 验证

已完成：

- 全部 skill Python 脚本 `py_compile`。
- `adalterome-api` hypotheses 与 gene-events smoke test。
- `adalterome-gene-report`、`adalterome-term-report`、`adalterome-hypothesis-report`、`adalterome-compare-report` 和 `adalterome-case-study-expert` 短报告生成 smoke test。
- 检查所有 smoke test 输出均生成 `data/cache_manifest.json`。
- `git diff --check`。
