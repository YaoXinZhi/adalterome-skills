# Two-Gene Comparison Report Contract

Use this structure:

1. Query scope and comparison frame
2. Side-by-side overview
3. Shared terms and hypotheses
4. Gene-A-specific patterns
5. Gene-B-specific patterns
6. Evidence curation layer for gene A and gene B
7. Mechanism-stratified evidence map for each gene
8. Representative and long-tail evidence for each gene
9. Comparative interpretation guide and follow-up priorities

## Required Standards

- Include both gene symbols and request URLs.
- Include `/compare/genes` shared and unique terms/hypotheses.
- Include sentence-level evidence for both genes.
- Include `data/gene_a_curation.json` and `data/gene_b_curation.json` when using the builder script.
- Keep evidence traces separated by gene.
- Mention record counts as database representation, not biological importance.
- Curate each gene with a gene-fixed event key: alteration taxonomy + phenotype/term + hypothesis.
- Include query-relative top and long-tail phenotype and gene-alteration patterns for each gene.
- Treat `AlterationType` as the genetic alteration taxonomy; do not count `TriggerWord` or `RegType` as alteration labels.

## Interpretation Rules

- More records do not automatically mean greater importance.
- Shared terms may reflect different mechanisms; verify using original sentences.
- Distinct hypotheses should be described as AD-Alterome evidence patterns, not definitive gene functions.
