# AD-Alterome Knowledge Synthesis Packet: MAPT

## Query Scope and User Intent

- User question: Organize the MAPT phenotype landscape for expert review.
- Output role: AI-organized evidence structure for expert evaluation.
- Manuscript role: evaluation object for AI-for-biomedical-knowledge-synthesis, not paper-ready biological conclusion.

## Analytical Pattern

- Pattern: `recommendation`
- Targets: MAPT

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
| MAPT | offline_full_query_pool_prescreened | 2700 | 2700 | 27921 | 1640 | low_fraction_of_matched_events_in_curation_pool |

- Balance status: `not_applicable`

## Organized Evidence Groups

### model_or_intervention

- Organized evidence rows: `4`
- Genes represented: MAPT
- Phenotype/process features represented: Drosophila tauopathy, neuropathological abnormalities, import across plasma membrane, translation
- Mechanism strata: amyloid/tau axis (4), proteostasis/autophagy axis (3), mitochondrial and oxidative stress axis (1), neuroinflammation and microglia axis (1)

### molecular_mechanism

- Organized evidence rows: `2`
- Genes represented: MAPT
- Phenotype/process features represented: process
- Mechanism strata: amyloid/tau axis (2), proteostasis/autophagy axis (1), synaptic and neuronal dysfunction axis (1), neuroinflammation and microglia axis (1)


## Gene-Alteration-Phenotype/Hypothesis Map

| Gene | Alteration taxonomy | Phenotype/process | Hypothesis | Evidence rows | Long-tail rows |
| --- | --- | --- | --- | --- | --- |
| MAPT | expression changes:dysregulation | - | Abnormal Autophagy Hypothesis,Mitochondrial Autophagy Hypothesis | 1 | 1 |
| MAPT | normalized variants:dna change | Drosophila tauopathy | Tau Protein Hypothesis,Neuroinflammation Hypothesis | 1 | 1 |
| MAPT | normalized variants:dna change | neuropathological abnormalities | Amyloid Hypothesis,Vascular Hypothesis | 1 | 1 |
| MAPT | normalized variants:dna change | import across plasma membrane | Tau Protein Hypothesis,Abnormal Autophagy Hypothesis | 1 | 1 |
| MAPT | expression changes:dysregulation | process | Neuroinflammation Hypothesis,Microbiota-Gut-Brain Axis Hypothesis | 1 | 1 |
| MAPT | point mutations:mutations | translation | Amyloid Hypothesis,Tau Protein Hypothesis,Abnormal Autophagy Hypothesis | 1 | 1 |

## Long-Tail Evidence Candidates

| Rank | Target | PMID | Gene | Phenotype/process | Why review it |
| --- | --- | --- | --- | --- | --- |
| 1 | MAPT | [36453392](https://pubmed.ncbi.nlm.nih.gov/36453392/) | MAPT | - | molecular_mechanism evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 2 | MAPT | [36608133](https://pubmed.ncbi.nlm.nih.gov/36608133/) | MAPT | Drosophila tauopathy | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 3 | MAPT | [37337279](https://pubmed.ncbi.nlm.nih.gov/37337279/) | MAPT | neuropathological abnormalities | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 4 | MAPT | [37452321](https://pubmed.ncbi.nlm.nih.gov/37452321/) | MAPT | import across plasma membrane | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 5 | MAPT | [37959365](https://pubmed.ncbi.nlm.nih.gov/37959365/) | MAPT | process | molecular_mechanism evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 6 | MAPT | [38010524](https://pubmed.ncbi.nlm.nih.gov/38010524/) | MAPT | translation | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 7 | MAPT | [37998336](https://pubmed.ncbi.nlm.nih.gov/37998336/) | MAPT | Affected | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 8 | MAPT | [37873467](https://pubmed.ncbi.nlm.nih.gov/37873467/) | MAPT | hypersensitivity | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 9 | MAPT | [37111315](https://pubmed.ncbi.nlm.nih.gov/37111315/) | MAPT | microgliosis and astrocytosis | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 10 | MAPT | [35012639](https://pubmed.ncbi.nlm.nih.gov/35012639/) | MAPT | impairment and behavioral deficits | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 11 | MAPT | [34753904](https://pubmed.ncbi.nlm.nih.gov/34753904/) | TAU | Progressive Supranuclear Palsy | molecular_mechanism evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 12 | MAPT | [37298443](https://pubmed.ncbi.nlm.nih.gov/37298443/) | MAPT | voluntary alcohol consumption | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 13 | MAPT | [38020775](https://pubmed.ncbi.nlm.nih.gov/38020775/) | MAPT | angiogenesis | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 14 | MAPT | [36688823](https://pubmed.ncbi.nlm.nih.gov/36688823/) | MAPT | - | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 15 | MAPT | [33679286](https://pubmed.ncbi.nlm.nih.gov/33679286/) | MAPT | - | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |
| 16 | MAPT | [36982371](https://pubmed.ncbi.nlm.nih.gov/36982371/) | MAPT | autophagosome-lysosome fusion | model_or_intervention evidence; informative original sentence; curation expert score 5/5 [long-tail] |

## AI-Organized Synthesis for Expert Review

For `MAPT`, the skill organized evidence for the question: `Organize the MAPT phenotype landscape for expert review.`.

This section is a review object. It proposes a structure for expert inspection and should not be copied as a final manuscript conclusion.

- Analytical pattern: `recommendation`
- Dominant mechanism strata among organized evidence: amyloid/tau axis (6), proteostasis/autophagy axis (4), neuroinflammation and microglia axis (2), synaptic and neuronal dysfunction axis (1), mitochondrial and oxidative stress axis (1)
- Frequently represented genes: MAPT
- Frequently represented phenotype/process features: Drosophila tauopathy, neuropathological abnormalities, import across plasma membrane, process, translation
- Frequently represented hypotheses: Abnormal Autophagy Hypothesis,Mitochondrial Autophagy Hypothesis, Tau Protein Hypothesis,Neuroinflammation Hypothesis, Amyloid Hypothesis,Vascular Hypothesis, Tau Protein Hypothesis,Abnormal Autophagy Hypothesis, Neuroinflammation Hypothesis,Microbiota-Gut-Brain Axis Hypothesis, Amyloid Hypothesis,Tau Protein Hypothesis,Abnormal Autophagy Hypothesis
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

### 1. MAPT / PMID [36453392](https://pubmed.ncbi.nlm.nih.gov/36453392/)

- AI organization score: `140.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `MAPT` / `expression changes:dysregulation` / `-` / `Abnormal Autophagy Hypothesis,Mitochondrial Autophagy Hypothesis`
- Evidence type: `molecular_mechanism`
- Mechanism strata: proteostasis/autophagy axis; amyloid/tau axis; synaptic and neuronal dysfunction axis
- Organization reasons: molecular_mechanism evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: Abnormalities in UPS function associated with neurodegenerative disorders not only promote accumulation and aggregation of damaged or misfolded proteins such as amyloid-beta, tau, alpha-synuclein, fused-in-sarcoma, or HTT but also promote the activation and progression of the abnormal cell cycle.

### 2. MAPT / PMID [36608133](https://pubmed.ncbi.nlm.nih.gov/36608133/)

- AI organization score: `136.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `MAPT` / `normalized variants:dna change` / `Drosophila tauopathy` / `Tau Protein Hypothesis,Neuroinflammation Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: amyloid/tau axis; mitochondrial and oxidative stress axis; neuroinflammation and microglia axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: Together, these data indicate that pathogenic forms of tau cause an elevation of dsRNA in astrocytes of human, mouse, and Drosophila tauopathy and that dsRNA elevation occurs in the context of toxic forms of wild-type tau (Alzheimer's disease and PSP) and from mutations in the microtubule-associated protein tau (MAPT) gene that cause familial forms of frontotemporal dementia (FTD) [rTg4510 mice (P301L) and tau transgenic Drosophila (R406W)].

### 3. MAPT / PMID [37337279](https://pubmed.ncbi.nlm.nih.gov/37337279/)

- AI organization score: `136.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `MAPT` / `normalized variants:dna change` / `neuropathological abnormalities` / `Amyloid Hypothesis,Vascular Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: amyloid/tau axis; vascular/metabolic axis; proteostasis/autophagy axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: Humanized APOE genotypes influence lifespan independently of tau aggregation in the P301S mouse model of tauopathy Apolipoprotein (APOE) E4 isoform is a major risk factor of Alzheimer's disease and contributes to metabolic and neuropathological abnormalities during brain aging.

### 4. MAPT / PMID [37452321](https://pubmed.ncbi.nlm.nih.gov/37452321/)

- AI organization score: `136.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `MAPT` / `normalized variants:dna change` / `import across plasma membrane` / `Tau Protein Hypothesis,Abnormal Autophagy Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: proteostasis/autophagy axis; amyloid/tau axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: Overexpression of transcription factor EB (TFEB, a regulator of lysosomal biogenesis) in astrocytes promotes tau fibril species uptake and lysosomal activity as well as attenuates tau spreading and pathology in the hippocampus of P301S tauopathy mice (Fig.

### 5. MAPT / PMID [37959365](https://pubmed.ncbi.nlm.nih.gov/37959365/)

- AI organization score: `136.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `MAPT` / `expression changes:dysregulation` / `process` / `Neuroinflammation Hypothesis,Microbiota-Gut-Brain Axis Hypothesis`
- Evidence type: `molecular_mechanism`
- Mechanism strata: amyloid/tau axis; neuroinflammation and microglia axis
- Organization reasons: molecular_mechanism evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: Of note, the resulting astrogliosis is a process associated with abnormalities of Aquaporin-4, also known as AQP-4, which is an encoded water channel protein, leading to disturbances of the glymphatic flow which plays a crucial role in the removal of debris (including amyloid beta (Abeta) and tau aggregates) across the neuronal interstitial space.

### 6. MAPT / PMID [38010524](https://pubmed.ncbi.nlm.nih.gov/38010524/)

- AI organization score: `134.0`; decision: `include`; tier: `high_insight`
- Gene / alteration / phenotype-process / hypothesis: `MAPT` / `point mutations:mutations` / `translation` / `Amyloid Hypothesis,Tau Protein Hypothesis,Abnormal Autophagy Hypothesis`
- Evidence type: `model_or_intervention`
- Mechanism strata: amyloid/tau axis; proteostasis/autophagy axis
- Organization reasons: model_or_intervention evidence; informative original sentence; curation expert score 5/5; strong mechanism specificity; strong pathology granularity; strong experimental directness; strong alteration informativeness; high-confidence expert annotation
- Cautions: -
- Original sentence: To experimentally challenge the role of protein homeostasis in the accumulation of Alzheimer's associated protein Abeta and levels of associated Tau phosphorylation, we disturbed proteostasis in single APP knock-in mouse models of AD building upon Rps9 D95N, a recently identified mammalian ram mutation which confers heightened levels of error-prone translation together with an increased propensity for random protein aggregation and which is associated with accelerated aging.


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
- `MAPT` overview: http://117.72.176.137/api/adalterome/gene/overview?gene=MAPT
- `MAPT` curation/evidence: http://117.72.176.137/api/adalterome/gene/curation?gene=MAPT&selected_limit=20