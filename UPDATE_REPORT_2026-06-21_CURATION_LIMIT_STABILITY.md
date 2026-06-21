# 2026-06-21 Curation Limit Stability Test

## Question

Can AD-Alterome skills default to returning as much curated evidence as possible
for knowledge synthesis?

## Result

The current remote curation API does not support true full-pool row return
through `selected_limit`. Direct requests above 500 return HTTP 422, and
special values such as `0`, `-1`, `all`, `max`, and `999999` also return HTTP
422.

Therefore, the practical "as much as possible" value for the current API is:

```text
selected_limit = 500
```

The knowledge synthesis builder now uses this value by default for
`--candidate-limit`.

## Direct API Stability Checks

Representative direct `/curation` requests with `source=curated`:

| Query | selected_limit | Result | Time | Payload | Returned |
| --- | ---: | --- | ---: | ---: | ---: |
| MAPT gene | 30 | ok | 2.66 s | 0.48 MB | 30 |
| MAPT gene | 500 | ok | 14.65 s | 5.90 MB | 500 |
| APOE gene | 30 | ok | 28.36 s | 0.48 MB | 30 |
| APOE gene | 500 | ok | 15.79 s | 6.10 MB | 500 |
| mitochondrial dysfunction term | 30 | ok | 2.52 s | 0.58 MB | 30 |
| mitochondrial dysfunction term | 500 | ok | 8.76 s | 3.47 MB | 232 |
| Alzheimer's Disease term | 30 | ok | 2.48 s | 0.45 MB | 30 |
| Alzheimer's Disease term | 500 | ok | 14.48 s | 5.67 MB | 500 |
| Neuroinflammation Hypothesis | 100 | ok | 6.11 s | 1.38 MB | 100 |
| Neuroinflammation Hypothesis | 200 | ok | 8.99 s | 2.57 MB | 200 |
| Neuroinflammation Hypothesis | 300 | ok | 10.65 s | 3.72 MB | 300 |
| Neuroinflammation Hypothesis | 500 | ok | 15.84 s | 6.09 MB | 500 |

Direct requests with `selected_limit=1000` or `selected_limit=2000` returned
HTTP 422 for MAPT, APOE, and Neuroinflammation Hypothesis.

## End-to-End Knowledge Synthesis Checks

| Case | candidate_limit | Result | Notes |
| --- | ---: | --- | --- |
| MAPT phenotype landscape | 500 | ok | Produced 18 review rows; output directory was about 20 MB. |
| TREM2-DAP12 neuroinflammatory axis | 500 per target | ok | Produced 18 review rows from 905 post-merge candidates; output directory was about 46 MB. |
| PSEN1 low-limit smoke | requested 6, effective 20 | ok | The builder raised the candidate limit to 20 and produced a non-empty review sheet. |

## Decision

Use 500 as the default knowledge-synthesis candidate limit because it is the
largest stable value accepted by the current API. Keep `--organized-limit`
separate so the final packet remains readable.

Do not change the defaults of stable report builders yet: their `selected-limit`
controls displayed report evidence rather than upstream candidate coverage, so
defaulting them to 500 would make ordinary reports much heavier.

## Boundary

"Full curation pool" is still not the same as returning every raw event row.
The API exposes complete aggregate statistics and a curated pool, then returns
up to 500 selected candidate rows for downstream evidence organization.
