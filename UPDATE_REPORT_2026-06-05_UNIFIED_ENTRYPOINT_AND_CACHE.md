# 2026-06-05 Unified Entrypoint and Local Raw-Data Cache Update

## 背景

此前 AD-Alterome skills 已经分成 API、固定报告、单基因报告、表型/生物过程报告、假说报告、双基因比较报告和 expert case-study 等多个入口。这样的结构对高级用户清晰，但普通用户需要先理解每个 skill 的边界，再决定该调用哪一个。

同时，skills 每次查询远程 API 后虽然会在报告目录保留部分 JSON，但没有一个统一机制告诉用户原始 API payload 具体保留在哪里，也没有自动复用相同请求的本地缓存。对于后续追问、人工检查原始数据、调整研究方向，这会增加重复请求和审计成本。

## 本次更新目标

1. 增加一个统一入口 skill，让用户可以直接用自然语言提出 AD-Alterome 问题。
2. 让每次 API 查询和报告生成都保留原始 API payload 的本地缓存位置。
3. 支持完全相同请求自动复用本地缓存，减少重复访问远程 API。
4. 在报告和文档中明确告诉用户原始数据保存路径，便于人工查看和后续分析。
5. 将用户可见的 `term` 文案调整为更易理解的 `phenotype/process`，同时保留 API 字段与参数兼容。

## 新增统一入口

新增 skill：

```text
adalterome
```

该入口根据用户问题自动路由：

- 简短 API 查询、schema、PMID 证据句子 -> `adalterome-api`
- 固定格式证据包 -> `adalterome-report`
- 单基因报告，如 MAPT、APOE、APP -> `adalterome-gene-report`
- 表型、下游生物过程、病理过程，如 mitochondrial dysfunction、neuroinflammation -> `adalterome-term-report`
- AD 假说，如 Amyloid Hypothesis、Tau Protein Hypothesis -> `adalterome-hypothesis-report`
- 双基因比较，如 APOE vs APP -> `adalterome-compare-report`
- 专家式 case-study、病理机制洞察、论文级论证 -> `adalterome-case-study-expert`

这样用户可以优先使用一个总入口，而不需要先学习每个 specialized skill 的边界。

## 新增本地原始数据缓存

新增脚本：

```text
skills/adalterome-api/scripts/query_cache.py
```

缓存策略：

- 默认缓存目录：`~/.adalterome-skills/cache`
- 按完整 request URL 生成 SHA256 cache key
- 保存原始 API JSON payload
- exact repeat request 自动复用缓存
- 缓存 payload 会在 `meta._local_cache` 中附加本地路径、cache hit 状态、index file、保存时间等信息

可配置环境变量：

```bash
ADALTEROME_CACHE_DIR=/path/to/cache
ADALTEROME_REFRESH_CACHE=1
ADALTEROME_DISABLE_CACHE=1
ADALTEROME_CACHE_MAX_AGE_DAYS=30
```

## 报告输出变化

API `--output report` 新增固定模块：

```text
## Local Data Cache
```

它会告诉用户当前请求的原始 payload 保存或复用位置。

所有深度报告 builder 现在都会在输出目录写入：

```text
data/cache_manifest.json
```

该 manifest 汇总本次报告使用到的原始 API payload cache 文件。典型输出包括：

- `data/query.json`
- `data/overview.json`
- `data/evidence.json`
- `data/curation.json`
- `data/cache_manifest.json`

case-study 报告也会写入 `data/cache_manifest.json`，并在 `Source Payloads` 模块中标注。

## 后续追问的数据复用原则

对于同一调查方向的后续问题，skill 应先检查上一轮报告目录中的：

- `data/*.json`
- `data/cache_manifest.json`

如果这些本地数据已经覆盖用户的新问题，就可以直接基于本地 JSON 继续分析，而不必再次请求远程 API。

自动缓存复用仅针对完全相同 request URL。没有把不同 `selected_limit` 或不同筛选条件的请求自动合并复用，是为了避免报告统计、代表性证据和查询语义被悄悄改变。

## 用户可见文案调整

报告中将原先容易误解的 `term` 展示名改为：

```text
phenotype/process
```

例如：

- `AD-Alterome Term Report` -> `AD-Alterome Phenotype / Process Report`
- `Top terms` -> `Top phenotype/process features`
- `Shared terms` -> `Shared phenotype/process features`

兼容性保持不变：

- API endpoint 仍为 `/term/*`
- CLI 参数仍为 `--term`
- JSON 字段仍为 `TermName`

## 主要修改文件

- `skills/adalterome/SKILL.md`
- `skills/adalterome-api/scripts/query_cache.py`
- `skills/adalterome-api/scripts/evidence_fetch.py`
- `skills/adalterome-api/scripts/query_adalterome.py`
- `skills/adalterome-gene-report/scripts/build_gene_report.py`
- `skills/adalterome-term-report/scripts/build_term_report.py`
- `skills/adalterome-hypothesis-report/scripts/build_hypothesis_report.py`
- `skills/adalterome-compare-report/scripts/build_compare_report.py`
- `skills/adalterome-case-study-expert/scripts/build_case_study_expert.py`
- `README.md`
- `DESIGN.md`

## 验证

已完成本地验证：

- `python3 -m py_compile` 覆盖全部修改脚本。
- `APP gene-overview` 连续请求 smoke test：第一次保存缓存，第二次成功 `cache_hit=true`。
- `APP` deep gene report smoke test：成功生成 `report.md` 和 `data/cache_manifest.json`。
- `MAPT` expert case-study smoke test：成功生成 `case_study_report.md` 和 `data/cache_manifest.json`。
- `git diff --check` 通过。

## 当前边界

- 缓存自动复用只覆盖完全相同 API 请求。
- 如果用户希望改变 `selected_limit`、`source`、目标实体或刷新最新数据，应重新请求 API。
- 本次没有改变远程 API contract，也没有改变 `/term/*` endpoint 和 `TermName` 字段。
- 大型 broad query 的完整报告仍可能受远程 API 响应时间和服务端限制影响。
