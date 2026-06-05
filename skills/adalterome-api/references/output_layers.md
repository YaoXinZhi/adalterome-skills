# Output Layers

Use the lightest output surface that satisfies the task.

## `summary`

Use for exploration and routing. It reports status, count, query, metadata, and compact top evidence fields.

## `report`

Use for user-facing answers. It preserves:

1. `## Query`
2. `## API Links`
3. `## Local Data Cache`
4. `## Summary`
5. `## Results`
6. `## Evidence`
7. `## Notes`

The local data cache section reports where the raw API payload was saved or
reused. This lets users inspect the original JSON and lets exact repeat requests
avoid another remote API call.

## `evidence-md`

Use when the user asks specifically for evidence tracing, PubMed links, or original sentences.

## `json`

Use when exact fields, downstream parsing, debugging, or schema inspection is needed.
