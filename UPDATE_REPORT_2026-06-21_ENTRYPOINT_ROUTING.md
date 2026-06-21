# 2026-06-21 Entrypoint Routing and Skill Hierarchy Update

## Summary

This update tightens the installed skill hierarchy so AD-Alterome no longer
looks like a flat set of equally user-facing skills.

The intended public surface is now:

- `adalterome`: default entrypoint for ordinary AD-Alterome questions.
- `adalterome-knowledge-synthesis`: public research/evaluation entrypoint for
  knowledge packets, expert review sheets, and AI-for-biomedical-knowledge-
  synthesis experiments.

All other `adalterome-*` skills remain installed and callable, but are described
as internal/advanced direct-use helpers. They should normally be selected only
after `adalterome` routes a request, or when a user explicitly asks for a
specific helper skill, builder script, or reproducible output contract.

## What Changed

- Updated `SKILL.md` frontmatter descriptions for helper skills so ordinary
  user questions preferentially match `adalterome`.
- Added direct-use boundary notes to helper skill bodies.
- Kept `adalterome-knowledge-synthesis` as a public research/evaluation
  entrypoint.
- Updated `README.md` with a two-entrypoint invocation model.
- Updated `DESIGN.md` with deployment and trigger strategy notes.
- Added a knowledge-synthesis usability guard that raises very small
  `--candidate-limit` values to 20 while recording the user's original request.

## Expected Effect

- Users can start with one skill: `adalterome`.
- Manuscript/evaluation users can directly choose
  `adalterome-knowledge-synthesis`.
- Gene, term, hypothesis, compare, report, API, and legacy case-study helpers
  remain available without being presented as equally broad user-facing entry
  points.

## Verification

Recommended checks:

- Validate all AD-Alterome `SKILL.md` frontmatter descriptions.
- Confirm only `adalterome` and `adalterome-knowledge-synthesis` are labeled as
  public entrypoints.
- Run script smoke checks for the public research entrypoint and representative
  helper builders.
