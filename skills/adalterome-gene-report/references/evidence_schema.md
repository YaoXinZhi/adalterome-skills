# Evidence Schema

Deep reports should use these fields first:

- `Evidence.sentence`: original sentence for quotation and traceability.
- `Evidence.pubmed_url`: PubMed link.
- `Evidence.event`: AD-Alterome event chain.
- `Evidence.evidence_score`: evidence score.
- `Evidence.quality_score` or row-level `EvidenceQualityScore`: sentence quality score.
- `Evidence.article.journal`, `Evidence.article.year`: source context.
- `Evidence.article.mesh_index`, `major_mesh_index`, `pubtypes`, `substances`: literature metadata.
- `Evidence.biological_context`: gene, alteration, trigger, term, ontology.
- `Evidence.ad_interpretation`: AD hypothesis, mechanism, relevance, explanation.

## Interpretation

Use `Sentence` and `Event` for primary claims.
Use `ExtendedExplanation`, `HypothesisReason`, and related AD interpretation fields as database interpretation, not as independent experimental evidence.
