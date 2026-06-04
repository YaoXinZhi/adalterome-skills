# Deep Gene Report Contract

Use this structure for final reports:

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

- Include PubMed links for every evidence row when PMID is present.
- Include exact original evidence sentences.
- Do not use or display `EvidenceScore` in skill-facing reports.
- Use the curation layer's `SentenceQuality` / sentence informativeness only as a readability aid, not as proof strength.
- Gene reports deduplicate events by alteration taxonomy + phenotype/term + hypothesis because the gene is fixed by the query.
- Include query-relative top and long-tail phenotype and gene-alteration patterns from `data/curation.json`.
- Treat `AlterationType` as the genetic alteration taxonomy; do not count `TriggerWord` or `RegType` as alteration labels.
- Include `data/curation.json` when using the builder script.
- Distinguish original sentence content from AD-Alterome interpretation fields.
- Avoid causal claims unless the sentence supports intervention, perturbation, genetic validation, or equivalent evidence.
- If evidence is sparse, say so and avoid padding.
