# AD-Alterome Fixed Report Contract

Keep this section order exactly:

1. `## Query`
2. `## API Links`
3. `## Local Data Cache`
4. `## Summary`
5. `## Results`
6. `## Evidence`
7. `## Notes`

## Required Content

- `## Query`: tool name, status, normalized query.
- `## API Links`: `api_page` and `request_url`.
- `## Local Data Cache`: local raw payload cache file and cache index when caching is enabled.
- `## Summary`: count, top_k, candidate_limit, ranking note when present.
- `## Results`: compact table of returned records.
- `## Evidence`: PMID/PubMed link, original sentence, phenotype/process feature, hypothesis, and sentence quality.
- `## Notes`: caveats about sentence-level evidence and causality.

## Evidence Rules

- Always preserve the original sentence exactly.
- Use PubMed markdown links when `Evidence.pubmed_url` is available.
- Do not display or interpret `EvidenceScore`.
- Keep weak/generic evidence caveated.
- Never add records absent from the API response.
