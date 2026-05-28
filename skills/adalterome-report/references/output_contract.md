# AD-Alterome Fixed Report Contract

Keep this section order exactly:

1. `## Query`
2. `## API Links`
3. `## Summary`
4. `## Results`
5. `## Evidence`
6. `## Notes`

## Required Content

- `## Query`: tool name, status, normalized query.
- `## API Links`: `api_page` and `request_url`.
- `## Summary`: count, top_k, candidate_limit, ranking note when present.
- `## Results`: compact table of returned records.
- `## Evidence`: PMID/PubMed link, original sentence, term, hypothesis, evidence score, quality score.
- `## Notes`: caveats about sentence-level evidence and causality.

## Evidence Rules

- Always preserve the original sentence exactly.
- Use PubMed markdown links when `Evidence.pubmed_url` is available.
- Keep weak/generic evidence caveated.
- Never add records absent from the API response.
