# AD-Alterome Knowledge Synthesis Packet: APOE vs APP

## Query Scope and User Intent

- User question: Organize AD-Alterome evidence comparing APOE and APP for expert review.
- Output role: AI-organized evidence structure for expert evaluation.
- Manuscript role: evaluation object for AI-for-biomedical-knowledge-synthesis, not paper-ready biological conclusion.

## Analytical Pattern

- Pattern: `multi_gene`
- Targets: APOE, APP

## Event Schema Used

| Layer | Fields | Use in this packet |
| --- | --- | --- |
| Gene | `Gene`, `Entrez` | Anchors the alteration evidence to a genetic entity. |
| Alteration | `AlterationType`, `AlterationMention`, `AlterationID` | Keeps AD-Alterome alteration-centered rather than only gene-centered. |
| Event relation | `TriggerWord`, `RegType`, `Event` | Records the extracted relation context; not treated as genetic alteration labels. |
| Phenotype/process | `TermName`, `TermID`, `TermType`, ontology fields | Organizes downstream biological processes, clinical phenotypes, and pathology features. |
| AD interpretation | `Hypothesis`, `MechanismProvided`, `HypothesisReason`, `ExtendedExplanation` | Used as curated interpretation fields that require expert review. |
| Provenance | `PMID`, `Journal`, `Year`, `Sentence`, `PubMedURL` | Makes every organized item traceable to source sentences. |

`EvidenceScore` is intentionally not used or displayed as evidence strength.

## Evidence Landscape and Coverage

| Target | Curation scope | Pool rows | Event-unique rows | Matched events | Unique PMIDs | Coverage warnings |
| --- | --- | --- | --- | --- | --- | --- |
| APOE | offline_full_query_pool_prescreened | 1844 | 1844 | 13322 | 1167 | - |
| APP | offline_full_query_pool_prescreened | 2310 | 2310 | 18636 | 1606 | - |

- Balance status: `balanced`
- Targets have comparable curation scope for knowledge synthesis.

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
| 7 | APOE | [34876200](https://pubmed.ncbi.nlm.nih.gov/34876200/) | APOE | collagen | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 8 | APOE | [37927337](https://pubmed.ncbi.nlm.nih.gov/37927337/) | APOE | low-density lipoprotein | molecular_mechanism evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 9 | APP | [37165437](https://pubmed.ncbi.nlm.nih.gov/37165437/) | APP | neuronal cell loss or NFTs | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 10 | APP | [37873467](https://pubmed.ncbi.nlm.nih.gov/37873467/) | APP | hypersensitivity | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 11 | APP | [35216123](https://pubmed.ncbi.nlm.nih.gov/35216123/) | APP | senescence | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 12 | APOE | [37019383](https://pubmed.ncbi.nlm.nih.gov/37019383/) | APOE | cAMP-dependent protein kinase complex | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 13 | APOE | [26346625](https://pubmed.ncbi.nlm.nih.gov/26346625/) | APOE | Insulin signaling | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 14 | APOE | [24644280](https://pubmed.ncbi.nlm.nih.gov/24644280/) | APOE | reactive oxygen species biosynthetic process | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 15 | APP | [28973312](https://pubmed.ncbi.nlm.nih.gov/28973312/) | APP | lysosomal deficits | molecular_mechanism evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 16 | APP | [35012639](https://pubmed.ncbi.nlm.nih.gov/35012639/) | APP | impairment and behavioral deficits | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |

## AI-Organized Synthesis for Expert Review

For `APOE vs APP`, the skill organized evidence for the question: `Organize AD-Alterome evidence comparing APOE and APP for expert review.`.

This section is a review object. It proposes a structure for expert inspection and should not be copied as a final manuscript conclusion.

- Analytical pattern: `multi_gene`
- Dominant mechanism strata among organized evidence: amyloid/tau axis (5), mitochondrial and oxidative stress axis (3), synaptic and neuronal dysfunction axis (3), neuroinflammation and microglia axis (3), proteostasis/autophagy axis (2)
- Frequently represented genes: APOE, APP, amyloid precursor protein
- Frequently represented phenotype/process features: mitophagy, chemical synaptic transmission, reactive gliosis, lipid binding, lysosome, inflammatory
- Frequently represented hypotheses: Amyloid Hypothesis,Mitochondrial Autophagy Hypothesis, Cholinergic Hypothesis,Amyloid Hypothesis, Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis, Neuroinflammation Hypothesis,Vascular Hypothesis, Oxidative Stress Hypothesis,Abnormal Autophagy Hypothesis,Mitochondrial Autophagy Hypothesis, Amyloid Hypothesis,Neuroinflammation Hypothesis
- Long-tail rows retained for review: `6`

## Expert Review Worksheet

Reviewer-facing worksheet: `expert_review_sheet.tsv`.

Suggested reviewer groups:

- clinical or translational AD experts
- AD or neurodegeneration researchers
- biomedical graduate students or postdocs

Recommended scoring dimensions use 1-5 scores, with `cannot_judge` allowed:

| Dimension | Reviewer question |
| --- | --- |
| Traceability | Are important statements backed by PMID and original sentence evidence? |
| Accuracy | Are gene, alteration, phenotype/process, and hypothesis attributions correct? |
| Breadth | Does the packet cover the relevant evidence space rather than only dominant high-frequency records? |
| Depth | Does the organized evidence include molecular, cellular, pathological, or model-level detail? |
| Organization usefulness | Do the evidence groups make the complex AD evidence easier to review? |
| Long-tail usefulness | Are low-frequency but potentially informative records surfaced for review? |
| Hallucination or overclaim risk | Score high when hallucination or unsupported overclaim risk is low. |
| Inspiration | Does the packet help generate useful review, mechanism, or experiment questions? |
| Review efficiency | Does the packet reduce the time needed to inspect the evidence? |
| Overall usefulness | Does the packet meet the user need better than unstructured search or generic LLM output? |

## Original Evidence Traces

### 1. APP / PMID [37109499](https://pubmed.ncbi.nlm.nih.gov/37109499/)

- AI organization score: `146.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `APP` / `normalized variants:dna change` / `mitophagy` / `Amyloid Hypothesis,Mitochondrial Autophagy Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; synaptic and neuronal dysfunction axis; proteostasis/autophagy axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: Previous investigations have examined the effects of PINK1 in a preclinical AD exemplary presentation and showed that intraneurons in brain tissue cause stereotaxic vaccinations of AAV2-hPINK1 in transgenic rats at six months, exhibiting an upregulation of hAPP comportment Indiana (V717F), and that Swedish mutations trigger the stimulation of mitophagy via an over-regulation of both NDP52 and OPTN mitophagy receptors.

### 2. APP / PMID [36170028](https://pubmed.ncbi.nlm.nih.gov/36170028/)

- AI organization score: `144.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `APP` / `normalized variants:dna change` / `chemical synaptic transmission` / `Cholinergic Hypothesis,Amyloid Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: amyloid/tau axis; synaptic and neuronal dysfunction axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: In addition to targeting TRKB, neurotrophic receptor tyrosine kinase 1 (TRKA) agonist D3 have been shown to provide beneficial effects to activate TRKA-related signaling cascades and enhance cholinergic neurotransmission in transgenic mice overexpressing human APP with KM670/671NL and V717F mutations.

### 3. APP / PMID [37693648](https://pubmed.ncbi.nlm.nih.gov/37693648/)

- AI organization score: `140.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `amyloid precursor protein` / `point mutations:mutations` / `reactive gliosis` / `Amyloid Hypothesis,Tau Protein Hypothesis,Neuroinflammation Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: Double transgenic (APP/ALDH2*2 OE) mice from a cross between Tg2576 mice expressing a mutant form of human amyloid precursor protein (APP) and DAL mice over expressing the mutant form of ALDH2 (ALDH2*2 OE) showed cognitive dysfunction already at 3 months, accelerated gliosis from 6 months, tau phosphorylation from around 9 months, and Abeta accumulation beginning around 6 months that increased significantly after 12 months.

### 4. APOE / PMID [37108421](https://pubmed.ncbi.nlm.nih.gov/37108421/)

- AI organization score: `144.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `APOE` / `point mutations:mutations` / `lipid binding` / `Neuroinflammation Hypothesis,Vascular Hypothesis`
- Evidence type: `molecular_mechanism`
- Mechanism strata: neuroinflammation and microglia axis; synaptic and neuronal dysfunction axis; vascular/metabolic axis
- Organization reasons: molecular_mechanism evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: These polymorphisms cause differences in the lipid binding properties of the APOE isoforms and receptor affinities; APOE4 is hypolipidated compared to APOE3 and APOE2 (Figure 3).

### 5. APOE / PMID [37455931](https://pubmed.ncbi.nlm.nih.gov/37455931/)

- AI organization score: `142.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `APOE` / `normalized variants:dna change` / `lysosome` / `Oxidative Stress Hypothesis,Abnormal Autophagy Hypothesis,Mitochondrial Autophagy Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; vascular/metabolic axis; proteostasis/autophagy axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: Methods: Fibroblasts from Alzheimer's patients with APOE 3/4 + G206D-PSEN1 mutation and homozygous APOE epsilon4 were used to study the effects of APOE polymorphism and PSEN1 mutation on the autophagy pathway, mitochondrial network fragmentation, superoxide anion levels, lysosome clustering, and p62/SQSTM1 levels.

### 6. APOE / PMID [36646419](https://pubmed.ncbi.nlm.nih.gov/36646419/)

- AI organization score: `142.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `APOE` / `point mutations:mutations` / `inflammatory` / `Amyloid Hypothesis,Neuroinflammation Hypothesis`
- Evidence type: `molecular_mechanism`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis
- Organization reasons: molecular_mechanism evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: Microglia differentiated from AD-hiPSCs derived from patients bearing the APOE4 variant displayed a decreased ability to uptake Abeta peptide and alterations in the expression of pro-inflammatory signaling pathway genes compared to isogenic APOE3-hiPSC-derived microglia.


## Limitations and Non-Claims

- This packet organizes AD-Alterome sentence-level evidence; it does not prove an AD mechanism.
- This packet does not replace expert review.
- AI-organized evidence groups are review candidates, not manuscript conclusions.
- Human experts should score traceability, accuracy, depth, breadth, hallucination or overclaim risk, and usefulness before using the packet in a manuscript.
- `EvidenceScore` is not used or displayed as evidence strength.
- `EvidenceQualityScore`, when present in raw payloads, is a sentence-usefulness signal rather than proof strength.
- PubMed-linked sentences support provenance, not direct causal validation.
- Curation scope and coverage warnings should be reported when comparing targets.

## Source Payloads

- Raw API cache manifest: `data/cache_manifest.json`
- Provenance manifest: `provenance_manifest.json`
- Gene comparison endpoint: http://117.72.176.137/api/adalterome/compare/genes?gene_a=APOE&gene_b=APP
- `APOE` overview: http://117.72.176.137/api/adalterome/gene/overview?gene=APOE
- `APOE` curation/evidence: http://117.72.176.137/api/adalterome/gene/curation?gene=APOE&selected_limit=12
- `APP` overview: http://117.72.176.137/api/adalterome/gene/overview?gene=APP
- `APP` curation/evidence: http://117.72.176.137/api/adalterome/gene/curation?gene=APP&selected_limit=12