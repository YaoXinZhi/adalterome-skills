# 2026-06-21 GitHub Documentation and Helper Surface Sync

## Summary

This update aligns the GitHub-facing documentation, skill descriptions, and
advanced API helper command surface with the currently deployed AD-Alterome
compound curation implementation.

## What Changed

- Added a layered architecture section to `README.md`, clarifying that the
  public user surface is `adalterome` plus the research/evaluation entrypoint
  `adalterome-knowledge-synthesis`, while the other skills are internal or
  advanced direct-use helpers.
- Added a current feature matrix covering ordinary lookup, deep reports,
  two-gene comparison, compound gene / phenotype-process / hypothesis queries,
  publication-facing knowledge synthesis, and raw API debugging.
- Added a `compound-curation` example to the README quick API examples.
- Added `compound-curation` to `skills/adalterome-api/scripts/query_adalterome.py`
  so advanced users can reproduce `/compound/curation` calls directly.
- Updated `adalterome-api` and `adalterome-knowledge-synthesis` skill
  descriptions to explain compound curation, strict event intersection,
  fallback semantics, and the natural-language versus script-execution
  boundary.
- Updated `DESIGN.md` to document the remote API-first retrieval architecture
  and to warn that combination questions should not be implemented as local
  top-k merges.

## Current User-Facing Model

Ordinary users should invoke `adalterome` and ask naturally. The router chooses
the smallest appropriate workflow.

Researchers evaluating AI-for-biomedical-knowledge-synthesis can invoke
`adalterome-knowledge-synthesis` directly when they need a knowledge packet,
evidence map, expert review sheet, scoring table, or provenance manifest.

The script-style examples in GitHub are reproducibility contracts, not the
normal interaction style. For example, a natural-language question such as
`PRKN 在线粒体自噬假说中有哪些病理机制证据？` is routed to a compound gene +
hypothesis query internally.

## Verification

- Python compile check passed for the updated API helper and knowledge
  synthesis builder scripts.
- Public API smoke test passed for:

```bash
python3 skills/adalterome-api/scripts/query_adalterome.py compound-curation \
  --gene PRKN \
  --hypothesis "Mitochondrial Autophagy Hypothesis" \
  --selected-limit 5 \
  --output summary
```

The returned payload reported `tool=curate_compound_evidence`,
`curation_scope=offline_full_query_pool_compound_intersection`,
`compound_match_event_count=16`, and `fallback_used=false`.

- `git diff --check` passed.
- README, `DESIGN.md`, `adalterome-api`, `adalterome-knowledge-synthesis`, and
  the API reference now describe the same entrypoint hierarchy and compound
  curation semantics.
