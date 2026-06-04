# Evidence Schema

Deep reports should use these fields first:

- `Evidence.sentence`: original sentence for quotation and traceability.
- `Evidence.pubmed_url`: PubMed link.
- `Evidence.event`: AD-Alterome event chain.
- `Evidence.evidence_score`: raw API compatibility field; do not use or display in skill reports.
- `SentenceQuality`: curation-layer sentence informativeness used for ordering selected evidence.
- `Evidence.quality_score` or row-level `EvidenceQualityScore`: API-side sentence quality field; do not treat it as proof strength.
- `Evidence.article.journal`, `Evidence.article.year`: source context.
- `Evidence.article.mesh_index`, `major_mesh_index`, `pubtypes`, `substances`: literature metadata.
- `Evidence.biological_context`: gene, alteration, trigger, term, ontology.
- `Evidence.ad_interpretation`: AD hypothesis, mechanism, relevance, explanation.

## Interpretation

Use `Sentence` and `Event` for primary claims.
Use `ExtendedExplanation`, `HypothesisReason`, and related AD interpretation fields as database interpretation, not as independent experimental evidence.
Use `AlterationType` as the genetic alteration taxonomy and keep only the leading pipe-separated taxonomy segment for alteration aggregation. Use `AlterationMention` and `AlterationID` as supporting context. `TriggerWord` and `RegType` describe event relation/regulation context and must not be counted as genetic alteration labels.
