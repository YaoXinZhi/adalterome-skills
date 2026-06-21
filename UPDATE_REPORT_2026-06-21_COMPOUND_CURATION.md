# 2026-06-21 Compound Curation Update

## Summary

This update adds true compound curation for AD-Alterome knowledge synthesis.
Questions that combine any two or three of gene, phenotype/process, and AD
hypothesis now use a server-side compound query before evidence organization.

## What Changed

- Added `/compound/curation` to the AD-Alterome API contract.
- Added `curate_compound_evidence` to backend tools, API client, and MCP tool
  surfaces.
- Added compound fetch support to skill scripts.
- Updated `adalterome-knowledge-synthesis` so `--gene`, `--term`, and
  `--hypothesis` combinations automatically use compound mode.
- Kept `adalterome` as the ordinary natural-language entrypoint; compound mode
  is an internal routing behavior, not a new user-facing skill to memorize.
- Updated knowledge synthesis hypothesis counts so comma-separated hypothesis
  fields are split before top-hypothesis summaries.

## Query Semantics

Compound curation resolves each provided axis into offline curated query IDs,
retrieves the curated pool for each axis, and intersects records by
`raw_event_id`. Diversity sampling, long-tail detection, and expert annotation
ranking are applied after this strict combination query.

If no event is shared by every requested axis, the default `fallback=axis_merge`
returns a clearly marked exploratory union of the axis pools. Users or scripts
can set `fallback=none` when a strict intersection is required.

## Example

Natural-language request:

```text
PRKN 在线粒体自噬假说中有哪些病理机制证据？
```

Equivalent reproducible script call:

```bash
python skills/adalterome-knowledge-synthesis/scripts/build_knowledge_synthesis.py \
  --gene PRKN \
  --hypothesis "Mitochondrial Autophagy Hypothesis" \
  --output-dir outputs/prkn_mitochondrial_autophagy
```

The script call is the reproducible execution layer. Ordinary users can ask in
natural language through `adalterome` or `adalterome-knowledge-synthesis`.

## Verification

- Python compile checks passed for updated API, backend, MCP, and skill scripts.
- Direct backend tests confirmed:
  - `PRKN + Mitochondrial Autophagy Hypothesis`: strict compound intersection,
    16 matched event IDs.
  - `mitochondrial dysfunction + Mitochondrial Autophagy Hypothesis`: strict
    compound intersection, selected evidence returned from the intersected pool.
  - `PRKN + mitochondrial dysfunction + Mitochondrial Autophagy Hypothesis`:
    strict three-axis intersection, 1 matched event ID.
  - `PRKN + Cholinergic Hypothesis`: no strict intersection; returned
    `axis_merge` fallback with `fallback_used=true`.
- End-to-end knowledge-synthesis test generated a compound packet for
  `PRKN + Mitochondrial Autophagy Hypothesis`; output mode and analytical
  pattern were both `compound`, and raw payloads were preserved in the local
  cache manifest.
- Public API deployment validation passed after restarting
  `ad-alterome-api.service` on `117.72.176.137`:
  - API index reports version `0.4.3` and includes `/compound/curation`.
  - Default-base-url skill smoke test generated a compound packet through
    `http://117.72.176.137/api/adalterome/compound/curation`.
