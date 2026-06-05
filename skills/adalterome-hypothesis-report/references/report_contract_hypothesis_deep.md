# Deep Hypothesis Report Contract

Use this structure:

1. Query scope and data provenance
2. Global evidence landscape
3. Evidence curation layer
4. Mechanism-stratified evidence map
5. Representative support evidence
6. Long-tail evidence signals
7. Chronological evidence trajectory
8. Original evidence traces
9. Interpretation guide and follow-up priorities

## Required Standards

- Include the exact hypothesis query and request URLs.
- Include top genes and phenotype/process features from `/hypothesis/overview`.
- Include original evidence sentences and PubMed links from the curation evidence source.
- Do not use or display `EvidenceScore`.
- Use the curation layer's `SentenceQuality` / sentence informativeness only as a readability aid.
- Hypothesis reports deduplicate events by gene + alteration taxonomy + phenotype/term because the hypothesis is fixed by the query.
- Include query-relative top and long-tail gene, gene-alteration, and phenotype patterns from `data/curation.json`.
- Treat `AlterationType` as the genetic alteration taxonomy; do not count `TriggerWord` or `RegType` as alteration labels.
- Include `data/curation.json` when using the builder script.
- Separate primary sentence evidence from `HypothesisReason` and `ExtendedExplanation`.

## Interpretation Rules

- Do not say the hypothesis is proven.
- Use repeated genes, phenotype/process features, and PMIDs to describe support patterns.
- Mention combined hypothesis labels when a record links multiple hypotheses.
