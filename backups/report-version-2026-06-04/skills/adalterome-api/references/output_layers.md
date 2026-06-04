# Output Layers

Use the lightest output surface that satisfies the task.

## `summary`

Use for exploration and routing. It reports status, count, query, metadata, and compact top evidence fields.

## `report`

Use for user-facing answers. It preserves:

1. `## Query`
2. `## API Links`
3. `## Summary`
4. `## Results`
5. `## Evidence`
6. `## Notes`

## `evidence-md`

Use when the user asks specifically for evidence tracing, PubMed links, or original sentences.

## `json`

Use when exact fields, downstream parsing, debugging, or schema inspection is needed.
