# Deep Term Report Contract

Use this structure:

1. Query scope and data provenance
2. Global evidence landscape
3. Evidence curation layer
4. Mechanism-stratified evidence map
5. Representative molecular and pathological evidence
6. Long-tail evidence signals
7. Chronological evidence trajectory
8. Original evidence traces
9. Interpretation guide and follow-up priorities

## Required Standards

- Include the exact target term and request URLs.
- Include top genes and hypotheses from `/term/overview`.
- Include PubMed links and exact original sentences from the curation evidence source.
- Do not use or display `EvidenceScore`.
- Use the curation layer's `SentenceQuality` / sentence informativeness only as a readability aid.
- Term reports deduplicate events by gene + alteration taxonomy + hypothesis because the phenotype/term is fixed by the query.
- Include query-relative top and long-tail gene, gene-alteration, and phenotype patterns from `data/curation.json`.
- Treat `AlterationType` as the genetic alteration taxonomy; do not count `TriggerWord` or `RegType` as alteration labels.
- Include `data/curation.json` when using the builder script.
- Caveat broad terms as evidence maps, not narrow causal mechanisms.

## Interpretation Rules

- Treat high-frequency genes as candidates for review, not automatically as key drivers.
- Use repeated PMIDs, specific Event chains, curated evidence types, mechanism strata, and exact original sentences to support stronger claims.
- Keep AD-Alterome interpretation fields separate from primary sentence evidence.
