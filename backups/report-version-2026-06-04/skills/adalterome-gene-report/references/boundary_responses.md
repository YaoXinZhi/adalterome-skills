# Boundary Responses

## No Gene Records

Report that the gene was not found in AD-Alterome. Suggest checking the gene symbol and running `adalterome-api` schema or gene search if available.

## Sparse Evidence

If fewer than three curated representative evidence records are returned, deliver a short evidence note rather than a full mechanistic report.

## Generic Sentences

If sentences are vague or lack gene/term/alteration detail, preserve them as evidence traces but state that mechanistic interpretation is weak.

## API Unreachable

Stop and report the API connection problem. Do not fill the report with external memory.
