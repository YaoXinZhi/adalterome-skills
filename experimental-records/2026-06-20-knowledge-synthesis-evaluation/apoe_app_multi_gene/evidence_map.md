# AD-Alterome Evidence Map: APOE vs APP

- Analytical pattern: `multi_gene`
- Organized evidence rows: `6`
- Scored candidate rows after duplicate merge: `53`
- Long-tail organized rows: `6`

## Evidence Landscape and Coverage

| Target | Curation scope | Pool rows | Event-unique rows | Matched events | Unique PMIDs | Coverage warnings |
| --- | --- | --- | --- | --- | --- | --- |
| APOE | offline_full_query_pool_prescreened | 1844 | 1844 | 13322 | 1167 | - |
| APP | offline_full_query_pool_prescreened | 2310 | 2310 | 18636 | 1606 | - |

- Balance status: `balanced`
- Targets have comparable curation scope for knowledge synthesis.

## Target Curation Summaries

### APOE

- Curation source/scope: `curated_pool` / `offline_full_query_pool_prescreened`
- Matched events: `13322`; curation pool rows: `1844`; event-unique rows: `1844`; unique PMIDs: `1167`
- Selection trace: `{"requested_selected_limit": 12, "returned_selected_count": 12, "representative_count": 12, "selection_shortfall_reason": null}`

### APP

- Curation source/scope: `curated_pool` / `offline_full_query_pool_prescreened`
- Matched events: `18636`; curation pool rows: `2310`; event-unique rows: `2310`; unique PMIDs: `1606`
- Selection trace: `{"requested_selected_limit": 12, "returned_selected_count": 12, "representative_count": 12, "selection_shortfall_reason": null}`

## Organized Evidence Groups

### model_or_intervention

- Organized evidence rows: `4`
- Genes represented: APP, amyloid precursor protein, APOE
- Phenotype/process features represented: mitophagy, chemical synaptic transmission, reactive gliosis, lysosome
- Mechanism strata: amyloid/tau axis (4), mitochondrial and oxidative stress axis (3), synaptic and neuronal dysfunction axis (2), proteostasis/autophagy axis (2)

### molecular_mechanism

- Organized evidence rows: `2`
- Genes represented: APOE
- Phenotype/process features represented: lipid binding, inflammatory
- Mechanism strata: neuroinflammation and microglia axis (2), synaptic and neuronal dysfunction axis (1), vascular/metabolic axis (1), amyloid/tau axis (1)


## Gene-Alteration-Phenotype/Hypothesis Map

| Gene | Alteration taxonomy | Phenotype/process | Hypothesis | Evidence rows | Long-tail rows |
| --- | --- | --- | --- | --- | --- |
| APP | normalized variants:dna change | mitophagy | Amyloid Hypothesis,Mitochondrial Autophagy Hypothesis | 1 | 1 |
| APP | normalized variants:dna change | chemical synaptic transmission | Cholinergic Hypothesis,Amyloid Hypothesis | 1 | 1 |
| amyloid precursor protein | point mutations:mutations | reactive gliosis | Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis | 1 | 1 |
| APOE | point mutations:mutations | lipid binding | Neuroinflammation Hypothesis,Vascular Hypothesis | 1 | 1 |
| APOE | normalized variants:dna change | lysosome | Oxidative Stress Hypothesis,Abnormal Autophagy Hypothesis,Mitochondrial Autophagy Hypothesis | 1 | 1 |
| APOE | point mutations:mutations | inflammatory | Amyloid Hypothesis,Neuroinflammation Hypothesis | 1 | 1 |

## Long-Tail Evidence Candidates

| Rank | Target | PMID | Gene | Phenotype/process | Why review it |
| --- | --- | --- | --- | --- | --- |
| 1 | APP | [37109499](https://pubmed.ncbi.nlm.nih.gov/37109499/) | APP | mitophagy | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 2 | APP | [36170028](https://pubmed.ncbi.nlm.nih.gov/36170028/) | APP | chemical synaptic transmission | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 3 | APP | [37693648](https://pubmed.ncbi.nlm.nih.gov/37693648/) | amyloid precursor protein | reactive gliosis | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 4 | APOE | [37108421](https://pubmed.ncbi.nlm.nih.gov/37108421/) | APOE | lipid binding | molecular_mechanism evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 5 | APOE | [37455931](https://pubmed.ncbi.nlm.nih.gov/37455931/) | APOE | lysosome | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 6 | APOE | [36646419](https://pubmed.ncbi.nlm.nih.gov/36646419/) | APOE | inflammatory | molecular_mechanism evidence; informative original sentence; curation expert score 5/5 [long-tail] |