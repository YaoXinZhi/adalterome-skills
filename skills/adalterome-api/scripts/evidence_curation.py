"""Evidence curation helpers for AD-Alterome skill reports.

The API may expose raw fields that are useful for compatibility. Skill-facing
reports use this module to build an interpretable evidence package without
using row-level EvidenceScore.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any


BROAD_TERMS = {
    "all",
    "alzheimer disease",
    "alzheimer's disease",
    "dementia",
    "protein",
    "chromosome",
    "sporadic",
    "onset",
    "late onset",
    "disease",
    "neurodegenerative diseases",
}

BROAD_HYPOTHESES = {
    "not applicable to any ad hypothesis",
}

ALTERATION_KEYWORDS = {
    "allele",
    "deletion",
    "duplication",
    "genetic",
    "genotype",
    "haplotype",
    "mutation",
    "p.",
    "polymorphism",
    "rs",
    "snp",
    "substitution",
    "variant",
}

MODEL_KEYWORDS = {
    "agonist",
    "administration",
    "animal model",
    "cell model",
    "cells",
    "hek293",
    "inhibitor",
    "knockdown",
    "knockout",
    "mice",
    "mouse",
    "silencing",
    "transfected",
    "transgenic",
    "treatment",
}

MOLECULAR_KEYWORDS = {
    "acetylation",
    "aggregation",
    "binding",
    "cleavage",
    "deposition",
    "enzyme",
    "expression",
    "misfolded",
    "oligomer",
    "phosphorylation",
    "proteolytic",
    "receptor",
    "transcription",
}

PATHWAY_KEYWORDS = {
    "apoptosis",
    "autophagy",
    "inflammasome",
    "inflammation",
    "metabolic",
    "microglia",
    "mitochond",
    "neuroinflammation",
    "oxidative",
    "synaptic",
    "vascular",
}

CLINICAL_KEYWORDS = {
    "association",
    "atrophy",
    "clinical",
    "cohort",
    "diagnosis",
    "gwas",
    "memory",
    "meta-analysis",
    "onset",
    "patient",
    "risk",
}

MECHANISM_STRATA = [
    ("amyloid/tau axis", {"amyloid", "abeta", "a beta", "tau", "mapt", "app"}),
    ("mitochondrial and oxidative stress axis", {"mitochond", "oxidative", "ros", "sirt", "pink1"}),
    ("neuroinflammation and microglia axis", {"neuroinflammation", "microglia", "inflammasome", "tnf", "il-1", "cytokine"}),
    ("synaptic and neuronal dysfunction axis", {"synaptic", "potentiation", "neuron", "neuronal", "gaba", "glutamat"}),
    ("vascular/metabolic axis", {"vascular", "metabolic", "insulin", "glucose", "lipid", "apoe"}),
    ("proteostasis/autophagy axis", {"autophagy", "proteostasis", "aggregation", "misfold", "proteolytic"}),
]

QUERY_DEDUP_DESCRIPTIONS = {
    "gene": "gene-fixed event key: alteration taxonomy + phenotype/term + hypothesis; fallback to PMID/sentence when structured fields are sparse",
    "term": "term-fixed event key: gene + alteration taxonomy + hypothesis; fallback to PMID/sentence when structured fields are sparse",
    "hypothesis": "hypothesis-fixed event key: gene + alteration taxonomy + phenotype/term; fallback to PMID/sentence when structured fields are sparse",
    "compare_gene": "gene-comparison event key: alteration taxonomy + phenotype/term + hypothesis for each gene independently",
    "generic": "generic event key: gene + alteration taxonomy + phenotype/term + hypothesis; fallback to PMID/sentence",
}

QUERY_LONG_TAIL_DIMENSIONS = {
    "gene": ["phenotype", "gene_alteration", "hypothesis"],
    "term": ["gene", "gene_alteration", "phenotype", "hypothesis"],
    "hypothesis": ["gene", "gene_alteration", "phenotype"],
    "compare_gene": ["phenotype", "gene_alteration", "hypothesis"],
    "generic": ["gene", "gene_alteration", "phenotype", "hypothesis"],
}

DIMENSION_LABELS = {
    "gene": "Gene",
    "gene_alteration": "Gene-alteration",
    "phenotype": "Phenotype",
    "hypothesis": "Hypothesis",
}


def md(value: Any) -> str:
    text = "" if value is None else str(value)
    return text.replace("|", "\\|").replace("\n", " ")


def is_placeholder(value: Any) -> bool:
    if value is None:
        return True
    if not isinstance(value, str):
        return False
    return value.strip().lower() in {"", "-", "nan", "none", "null"}


def clean_text(value: Any) -> str:
    if is_placeholder(value):
        return ""
    return str(value).strip()


def norm(value: Any) -> str:
    return clean_text(value).lower()


def data_rows(payload: dict[str, Any]) -> list[dict[str, Any]]:
    records = (payload.get("data") or {}).get("results")
    return records if isinstance(records, list) else []


def evidence_block(row: dict[str, Any]) -> dict[str, Any]:
    return row.get("Evidence") if isinstance(row.get("Evidence"), dict) else {}


def evidence_nested(row: dict[str, Any], group: str, key: str) -> Any:
    ev = evidence_block(row)
    nested = ev.get(group) if isinstance(ev.get(group), dict) else {}
    return nested.get(key)


def expert_annotation(row: dict[str, Any]) -> dict[str, Any]:
    annotation = row.get("ExpertAnnotation")
    return annotation if isinstance(annotation, dict) else {}


def expert_annotation_value(row: dict[str, Any], key: str) -> Any:
    return expert_annotation(row).get(key)


def expert_score(row: dict[str, Any], key: str) -> int | None:
    value = expert_annotation_value(row, key)
    try:
        if value in (None, "", "-"):
            return None
        score = int(float(str(value)))
    except (TypeError, ValueError):
        return None
    return max(1, min(5, score))


BIOLOGICAL_CONTEXT_KEYS = {
    "Gene": "gene",
    "Entrez": "entrez",
    "AlterationMention": "alteration_mention",
    "AlterationID": "alteration_id",
    "AlterationType": "alteration_type",
    "TriggerWord": "trigger_word",
    "RegType": "regulation_type",
    "TermMention": "term_mention",
    "TermID": "term_id",
    "TermName": "term_name",
    "TermType": "term_type",
    "AncestorID": "ancestor_id",
    "AncestorName": "ancestor_name",
}


def biological_context_value(row: dict[str, Any], key: str) -> Any:
    return row.get(key) or evidence_nested(row, "biological_context", BIOLOGICAL_CONTEXT_KEYS.get(key, key))


def row_text(row: dict[str, Any]) -> str:
    ev = evidence_block(row)
    parts = [
        ev.get("sentence"),
        row.get("Sentence"),
        row.get("Gene"),
        row.get("TermName"),
        row.get("Hypothesis"),
        row.get("Event"),
        row.get("AlterationMention"),
        row.get("AlterationType"),
        row.get("TriggerWord"),
        row.get("MechanismReason"),
        row.get("ExtendedExplanation"),
    ]
    return " ".join(str(part) for part in parts if part).lower()


def sentence(row: dict[str, Any]) -> str:
    ev = evidence_block(row)
    return clean_text(ev.get("sentence") or row.get("Sentence")) or "-"


def pmid(row: dict[str, Any]) -> str:
    ev = evidence_block(row)
    return clean_text(ev.get("pmid") or row.get("PMID")) or "-"


def pubmed_url(row: dict[str, Any]) -> str:
    ev = evidence_block(row)
    row_pmid = pmid(row)
    return clean_text(ev.get("pubmed_url")) or (f"https://pubmed.ncbi.nlm.nih.gov/{row_pmid}/" if row_pmid != "-" else "")


def year(row: dict[str, Any]) -> int | None:
    ev = evidence_block(row)
    article = ev.get("article") if isinstance(ev.get("article"), dict) else {}
    value = article.get("year") or row.get("Year")
    try:
        if value in (None, "", "-"):
            return None
        return int(float(str(value)))
    except (TypeError, ValueError):
        return None


def split_values(value: Any) -> list[str]:
    if is_placeholder(value):
        return []
    output: list[str] = []
    for part in str(value).split(","):
        clean = part.strip()
        if clean and clean != "-":
            output.append(clean)
    return output


def first_value(row: dict[str, Any], keys: list[str], nested_group: str | None = None) -> str:
    for key in keys:
        value = row.get(key)
        if clean_text(value):
            return clean_text(value)
    if nested_group:
        for key in keys:
            if nested_group == "biological_context":
                value = biological_context_value(row, key)
            else:
                value = evidence_nested(row, nested_group, key)
            if clean_text(value):
                return clean_text(value)
    return ""


def gene_signature(row: dict[str, Any]) -> str:
    return first_value(row, ["Gene"], "biological_context")


def term_signature(row: dict[str, Any]) -> str:
    return first_value(row, ["TermID", "TermName", "TermMention", "AncestorName"], "biological_context")


def canonical_hypothesis_label(value: Any) -> str:
    clean = clean_text(value).strip().rstrip(".;")
    if not clean:
        return ""
    tokens = []
    for token in clean.split():
        tokens.append(token if token.isupper() else token[:1].upper() + token[1:])
    return " ".join(tokens)


def hypothesis_values(row: dict[str, Any]) -> list[str]:
    value = first_value(row, ["Hypothesis", "LinkedHypothesis"], "ad_interpretation")
    output: list[str] = []
    seen = set()
    for hypothesis in split_values(value):
        clean = canonical_hypothesis_label(hypothesis)
        key = norm(clean)
        if not clean or key in seen:
            continue
        seen.add(key)
        output.append(clean)
    return output


def hypothesis_signature(row: dict[str, Any]) -> str:
    return ", ".join(sorted(hypothesis_values(row), key=norm))


def _first_pipe_segment(value: Any) -> str:
    clean = clean_text(value)
    if not clean:
        return ""
    return clean.split("|", 1)[0].strip()


def normalize_alteration_taxonomy(value: Any) -> str:
    clean = _first_pipe_segment(value)
    if not clean:
        return ""
    if ":" in clean:
        left, right = clean.split(":", 1)
        left = " ".join(left.strip().lower().split())
        right = " ".join(right.strip().lower().split())
        return f"{left}:{right}" if left and right else clean.lower()
    return " ".join(clean.lower().split())


def alteration_taxonomy(row: dict[str, Any]) -> str:
    for key in ["AlterationType", "AlterationID"]:
        value = normalize_alteration_taxonomy(biological_context_value(row, key))
        if value:
            return value
    return ""


def alteration_mention(row: dict[str, Any]) -> str:
    return clean_text(biological_context_value(row, "AlterationMention"))


def alteration_signature(row: dict[str, Any]) -> str:
    return alteration_taxonomy(row)


def gene_alteration_signature(row: dict[str, Any]) -> str:
    gene = gene_signature(row)
    alteration = alteration_taxonomy(row)
    if gene and alteration:
        return f"{gene} / {alteration}"
    return alteration or gene


def event_fallback(row: dict[str, Any]) -> tuple[str, str]:
    return (pmid(row), sentence(row))


def event_dedup_key(row: dict[str, Any], query_type: str = "generic") -> tuple[str, ...]:
    gene = norm(gene_signature(row))
    term = norm(term_signature(row))
    alteration = norm(alteration_signature(row))
    hypothesis = norm(hypothesis_signature(row))
    event = norm(row.get("Event"))

    if query_type in {"gene", "compare_gene"}:
        components = [alteration, term, hypothesis]
    elif query_type == "term":
        components = [gene, alteration, hypothesis]
    elif query_type == "hypothesis":
        components = [gene, alteration, term]
    else:
        components = [gene, alteration, term, hypothesis]

    informative = [component for component in components if component]
    if len(informative) >= 2:
        return (query_type, *[component or "-" for component in components])
    if len(informative) == 1 and event:
        return (query_type, informative[0], event)
    return ("pmid_sentence", *event_fallback(row))


def sentence_informativeness(row: dict[str, Any]) -> float:
    text = row_text(row)
    sent = sentence(row)
    length = len(sent)
    score = 0.0

    if 80 <= length <= 450:
        score += 18
    elif 45 <= length < 80 or 450 < length <= 800:
        score += 8
    elif length > 800:
        score -= 8
    else:
        score -= 12

    if gene_signature(row) and norm(gene_signature(row)) in sent.lower():
        score += 10
    term = first_value(row, ["TermMention", "TermName"], "biological_context")
    if term and norm(term) in sent.lower():
        score += 8
    alteration_terms = [
        alteration_mention(row),
        clean_text(biological_context_value(row, "AlterationID")),
        alteration_taxonomy(row),
    ]
    if any(term and norm(term) in sent.lower() for term in alteration_terms):
        score += 8
    trigger = first_value(row, ["TriggerWord"], "biological_context")
    if trigger and norm(trigger) in sent.lower():
        score += 5
    if clean_text(row.get("Event")):
        score += 8
    if norm(row.get("MechanismProvided") or evidence_nested(row, "ad_interpretation", "mechanism_provided")) == "yes":
        score += 8
    if norm(row.get("RelevantToAD") or evidence_nested(row, "ad_interpretation", "relevant_to_ad")) == "yes":
        score += 5
    if clean_text(row.get("ExtendedExplanation") or evidence_nested(row, "ad_interpretation", "extended_explanation")):
        score += 4
    if clean_text(row.get("Definition") or evidence_nested(row, "ad_interpretation", "definition")):
        score += 3
    if clean_text(row.get("Journal")):
        score += 2
    if year(row) is not None:
        score += 2
    if any(word in text for word in MOLECULAR_KEYWORDS | PATHWAY_KEYWORDS):
        score += 5
    if any(word in text for word in ALTERATION_KEYWORDS):
        score += 4

    vague_patterns = [
        "these findings",
        "this study",
        "our results",
        "further studies",
        "more research",
        "may play a role",
        "associated with",
        "various",
    ]
    if sum(1 for pattern in vague_patterns if pattern in text) >= 2:
        score -= 10
    if not any(
        value and norm(value) in sent.lower()
        for value in [gene_signature(row), term, alteration_mention(row), clean_text(biological_context_value(row, "AlterationID")), trigger]
    ):
        score -= 12
    return round(score, 3)


def unique_rows(rows: list[dict[str, Any]], query_type: str = "generic") -> list[dict[str, Any]]:
    best_by_key: dict[tuple[str, ...], dict[str, Any]] = {}
    for row in rows:
        key = event_dedup_key(row, query_type=query_type)
        current = best_by_key.get(key)
        if current is None:
            best_by_key[key] = row
            continue
        current_rank = (sentence_informativeness(current), year(current) or 0, len(sentence(current)))
        row_rank = (sentence_informativeness(row), year(row) or 0, len(sentence(row)))
        if row_rank > current_rank:
            best_by_key[key] = row
    return list(best_by_key.values())


def classify_evidence_type(row: dict[str, Any]) -> str:
    text = row_text(row)
    alteration_text = alteration_signature(row).lower()
    if any(word in text for word in MODEL_KEYWORDS):
        return "model_or_intervention"
    if any(word in text or word in alteration_text for word in ALTERATION_KEYWORDS):
        return "alteration_evidence"
    if any(word in text for word in MOLECULAR_KEYWORDS):
        return "molecular_mechanism"
    if any(word in text for word in PATHWAY_KEYWORDS):
        return "cellular_or_pathway_process"
    if any(word in text for word in CLINICAL_KEYWORDS):
        return "clinical_or_cohort_association"
    term = clean_text(row.get("TermName")).lower()
    if term in BROAD_TERMS:
        return "broad_background"
    return "unclear_or_mixed"


def mechanism_strata(row: dict[str, Any]) -> list[str]:
    text = row_text(row)
    strata = [name for name, keywords in MECHANISM_STRATA if any(keyword in text for keyword in keywords)]
    if strata:
        return strata
    if classify_evidence_type(row) in {"broad_background", "clinical_or_cohort_association"}:
        return ["broad disease/clinical association"]
    return ["mechanism unclear or mixed"]


def percentile(values: list[int], fraction: float) -> int:
    if not values:
        return 0
    ordered = sorted(values)
    index = int((len(ordered) - 1) * fraction)
    return ordered[index]


def dimension_value(row: dict[str, Any], dimension: str) -> str:
    if dimension == "gene":
        return gene_signature(row)
    if dimension in {"term", "phenotype"}:
        return clean_text(row.get("TermName")) or term_signature(row)
    if dimension == "alteration":
        return alteration_signature(row)
    if dimension == "gene_alteration":
        return gene_alteration_signature(row)
    if dimension == "hypothesis":
        return hypothesis_signature(row)
    return ""


def dimension_values(row: dict[str, Any], dimension: str) -> list[str]:
    if dimension == "hypothesis":
        return hypothesis_values(row)
    value = dimension_value(row, dimension)
    return [value] if value else []


def is_broad_dimension_value(dimension: str, value: str) -> bool:
    clean = value.strip().lower()
    return (
        not clean
        or (dimension in {"term", "phenotype"} and clean in BROAD_TERMS)
        or (dimension == "hypothesis" and clean in BROAD_HYPOTHESES)
    )


def build_frequency_counters(rows: list[dict[str, Any]], query_type: str) -> dict[str, Counter[str]]:
    counters: dict[str, Counter[str]] = {}
    for dimension in QUERY_LONG_TAIL_DIMENSIONS.get(query_type, QUERY_LONG_TAIL_DIMENSIONS["generic"]):
        counter: Counter[str] = Counter()
        for row in rows:
            for value in dimension_values(row, dimension):
                if not is_broad_dimension_value(dimension, value):
                    counter[value] += 1
        counters[dimension] = counter
    return counters


def dimension_threshold(counter: Counter[str]) -> int:
    counts = list(counter.values())
    if not counts:
        return 0
    return max(1, min(percentile(counts, 0.25), 10))


def long_tail_thresholds(counters: dict[str, Counter[str]]) -> dict[str, int]:
    return {dimension: dimension_threshold(counter) for dimension, counter in counters.items()}


def long_tail_signals_for_row(
    row: dict[str, Any],
    counters: dict[str, Counter[str]],
    thresholds: dict[str, int],
) -> list[dict[str, Any]]:
    signals: list[dict[str, Any]] = []
    for dimension, counter in counters.items():
        threshold = thresholds.get(dimension, 0)
        if not threshold:
            continue
        max_count = max(counter.values()) if counter else 0
        for value in dimension_values(row, dimension):
            if is_broad_dimension_value(dimension, value):
                continue
            count = counter.get(value, 0)
            if count and count <= threshold and count < max_count:
                signals.append({"dimension": dimension, "value": value, "frequency": count, "threshold": threshold})
    return signals


def curation_reasons(
    row: dict[str, Any],
    counters: dict[str, Counter[str]],
    thresholds: dict[str, int],
) -> list[str]:
    reasons: list[str] = []
    etype = classify_evidence_type(row)
    if etype != "broad_background":
        reasons.append(etype)
    if sentence_informativeness(row) >= 45:
        reasons.append("high sentence informativeness")
    signals = long_tail_signals_for_row(row, counters, thresholds)
    if signals:
        reasons.append("long-tail evidence signal")
    if year(row) is not None and year(row) >= 2020:
        reasons.append("recent evidence")
    if pmid(row) != "-":
        reasons.append("PMID-traceable")
    return reasons[:5]


def curation_rank(
    row: dict[str, Any],
    counters: dict[str, Counter[str]],
    thresholds: dict[str, int],
) -> tuple[float, int, int, str]:
    score = sentence_informativeness(row)
    term = clean_text(row.get("TermName"))
    term_specific = 0 if term.lower() in BROAD_TERMS or not term else 1
    long_tail = 1 if long_tail_signals_for_row(row, counters, thresholds) else 0
    row_year = year(row) or 0
    etype_bonus = {
        "model_or_intervention": 8,
        "molecular_mechanism": 8,
        "alteration_evidence": 7,
        "cellular_or_pathway_process": 6,
        "clinical_or_cohort_association": 2,
        "broad_background": -6,
    }.get(classify_evidence_type(row), 0)
    return (score + (6 * term_specific) + (8 * long_tail) + etype_bonus, row_year, len(sentence(row)), pmid(row))


def selection_dimensions(query_type: str) -> list[str]:
    if query_type == "term":
        return ["gene", "gene_alteration", "phenotype", "hypothesis", "pmid"]
    if query_type == "hypothesis":
        return ["gene", "gene_alteration", "phenotype", "pmid"]
    return ["phenotype", "gene_alteration", "hypothesis", "pmid"]


def selection_value(row: dict[str, Any], dimension: str) -> str:
    if dimension == "pmid":
        return pmid(row)
    return dimension_value(row, dimension)


def selection_values(row: dict[str, Any], dimension: str) -> list[str]:
    if dimension == "pmid":
        value = pmid(row)
        return [value] if value else []
    return dimension_values(row, dimension)


def within_selection_quota(
    row: dict[str, Any],
    seen: dict[str, Counter[str]],
    query_type: str,
    quotas: dict[str, int],
) -> bool:
    for dimension in selection_dimensions(query_type):
        for value in selection_values(row, dimension):
            if not value:
                continue
            if seen[dimension][value] >= quotas.get(dimension, 2):
                return False
    return True


def mark_selected(row: dict[str, Any], seen: dict[str, Counter[str]], query_type: str) -> None:
    for dimension in selection_dimensions(query_type):
        for value in selection_values(row, dimension):
            if value:
                seen[dimension][value] += 1


def select_diverse_rows(
    rows: list[dict[str, Any]],
    counters: dict[str, Counter[str]],
    thresholds: dict[str, int],
    query_type: str = "generic",
    limit: int = 30,
) -> list[dict[str, Any]]:
    sorted_rows = sorted(rows, key=lambda row: curation_rank(row, counters, thresholds), reverse=True)
    selected: list[dict[str, Any]] = []
    seen: dict[str, Counter[str]] = defaultdict(Counter)
    quotas = {"pmid": 2, "phenotype": 3, "gene": 3, "gene_alteration": 2, "hypothesis": 3}

    def add_row(row: dict[str, Any], ignore_quota: bool = False) -> bool:
        if row in selected:
            return False
        if not ignore_quota and not within_selection_quota(row, seen, query_type, quotas):
            return False
        selected.append(row)
        mark_selected(row, seen, query_type)
        return True

    for wanted_type in [
        "model_or_intervention",
        "molecular_mechanism",
        "alteration_evidence",
        "cellular_or_pathway_process",
        "clinical_or_cohort_association",
    ]:
        for row in sorted_rows:
            if classify_evidence_type(row) == wanted_type and add_row(row, ignore_quota=True):
                break

    for row in sorted_rows:
        if len(selected) >= limit:
            break
        if long_tail_signals_for_row(row, counters, thresholds):
            add_row(row)

    for row in sorted_rows:
        if len(selected) >= limit:
            break
        add_row(row)

    for row in sorted_rows:
        if len(selected) >= limit:
            break
        add_row(row, ignore_quota=True)

    return selected[:limit]


def normalize_row(
    row: dict[str, Any],
    counters: dict[str, Counter[str]],
    thresholds: dict[str, int],
    query_type: str,
) -> dict[str, Any]:
    ev = evidence_block(row)
    article = ev.get("article") if isinstance(ev.get("article"), dict) else {}
    signals = long_tail_signals_for_row(row, counters, thresholds)
    annotation = expert_annotation(row)
    curated = row.get("_Curated") if isinstance(row.get("_Curated"), dict) else {}
    return {
        "Gene": row.get("Gene"),
        "PMID": pmid(row),
        "PubMedURL": pubmed_url(row),
        "Journal": article.get("journal") or row.get("Journal"),
        "Year": year(row),
        "TermName": row.get("TermName"),
        "TermType": row.get("TermType"),
        "Hypothesis": row.get("Hypothesis"),
        "SentenceQuality": sentence_informativeness(row),
        "ExpertOverallScore": expert_score(row, "overall_expert_score"),
        "ExpertMechanismSpecificityScore": expert_score(row, "mechanism_specificity_score"),
        "ExpertPathologyGranularityScore": expert_score(row, "pathology_granularity_score"),
        "ExpertExperimentalDirectnessScore": expert_score(row, "experimental_directness_score"),
        "ExpertAlterationInformativenessScore": expert_score(row, "alteration_informativeness_score"),
        "AnnotationSource": annotation.get("annotation_source"),
        "AnnotationConfidence": annotation.get("confidence"),
        "ExpertReason": annotation.get("reason"),
        "CuratedPoolRank": curated.get("rank_in_query"),
        "SamplingBucket": curated.get("sampling_bucket"),
        "AlterationTaxonomy": alteration_taxonomy(row),
        "GeneAlteration": gene_alteration_signature(row),
        "AlterationSignature": alteration_taxonomy(row),
        "AlterationType": biological_context_value(row, "AlterationType"),
        "AlterationMention": alteration_mention(row),
        "AlterationID": biological_context_value(row, "AlterationID"),
        "AlterationEvidenceLevel": annotation.get("alteration_evidence_level"),
        "TriggerWord": biological_context_value(row, "TriggerWord"),
        "RegType": biological_context_value(row, "RegType"),
        "MechanismProvided": row.get("MechanismProvided"),
        "RelevantToAD": row.get("RelevantToAD"),
        "Event": row.get("Event"),
        "EventDedupKey": " | ".join(event_dedup_key(row, query_type=query_type)),
        "EvidenceType": classify_evidence_type(row),
        "MechanismStrata": mechanism_strata(row),
        "LongTailSignals": signals,
        "IsLongTailEvidence": bool(signals),
        "CurationReasons": curation_reasons(row, counters, thresholds),
        "Sentence": sentence(row),
    }


def period_for_year(value: int | None) -> str:
    if value is None:
        return "missing year"
    if value < 2010:
        return "before 2010"
    if value < 2015:
        return "2010-2014"
    if value < 2020:
        return "2015-2019"
    if value < 2025:
        return "2020-2024"
    return "2025 onward"


def top_items(counter: Counter[str], limit: int = 5) -> list[dict[str, Any]]:
    return [{"value": value, "count": count} for value, count in counter.most_common(limit) if value]


def tail_items(counter: Counter[str], threshold: int, limit: int = 5) -> list[dict[str, Any]]:
    if not threshold:
        return []
    items = [
        {"value": value, "count": count}
        for value, count in sorted(counter.items(), key=lambda item: (item[1], item[0].lower()))
        if value and count <= threshold
    ]
    return items[:limit]


def query_relative_patterns(counters: dict[str, Counter[str]], thresholds: dict[str, int]) -> dict[str, dict[str, Any]]:
    patterns: dict[str, dict[str, Any]] = {}
    for dimension, counter in counters.items():
        patterns[dimension] = {
            "label": DIMENSION_LABELS.get(dimension, dimension),
            "top": top_items(counter, limit=8),
            "long_tail": tail_items(counter, thresholds.get(dimension, 0), limit=8),
            "long_tail_threshold": thresholds.get(dimension, 0),
        }
    return patterns


def build_curation_package(
    payload: dict[str, Any],
    overview: dict[str, Any] | None = None,
    selected_limit: int = 30,
    query_type: str = "generic",
) -> dict[str, Any]:
    raw = data_rows(payload)
    rows = unique_rows(raw, query_type=query_type)
    counters = build_frequency_counters(rows, query_type=query_type)
    thresholds = long_tail_thresholds(counters)
    selected = select_diverse_rows(rows, counters, thresholds, query_type=query_type, limit=selected_limit)
    normalized = [normalize_row(row, counters, thresholds, query_type) for row in selected]
    requested_selected_limit = selected_limit
    returned_selected_count = len(normalized)
    eligible_after_filter_count = len(rows)
    representative = normalized[: min(30, len(normalized))]
    selection_shortfall_reason = None
    if returned_selected_count < min(requested_selected_limit, eligible_after_filter_count):
        selection_shortfall_reason = "selection_algorithm_returned_fewer_rows_than_available"
    elif eligible_after_filter_count < requested_selected_limit:
        selection_shortfall_reason = "eligible_unique_rows_below_requested_limit"

    pmid_counts = Counter(pmid(row) for row in rows if pmid(row) != "-")
    gene_counts = Counter(gene_signature(row) for row in rows if gene_signature(row))
    phenotype_counts = Counter(clean_text(row.get("TermName")) for row in rows if clean_text(row.get("TermName")))
    hyp_counts: Counter[str] = Counter()
    for row in rows:
        for hypothesis in hypothesis_values(row):
            if not is_broad_dimension_value("hypothesis", hypothesis):
                hyp_counts[hypothesis] += 1
    alteration_counts = Counter(alteration_taxonomy(row) for row in rows if alteration_taxonomy(row))
    gene_alteration_counts = Counter(gene_alteration_signature(row) for row in rows if gene_alteration_signature(row))
    type_counts = Counter(classify_evidence_type(row) for row in rows)
    strata_counts: Counter[str] = Counter()
    period_counts: dict[str, Counter[str]] = defaultdict(Counter)
    period_row_counts: Counter[str] = Counter()
    missing_year = 0
    for row in rows:
        row_year = year(row)
        if row_year is None:
            missing_year += 1
        period = period_for_year(row_year)
        period_row_counts[period] += 1
        for stratum in mechanism_strata(row):
            strata_counts[stratum] += 1
            period_counts[period][stratum] += 1

    long_tail: list[dict[str, Any]] = []
    for row in sorted(rows, key=lambda item: curation_rank(item, counters, thresholds), reverse=True):
        item = normalize_row(row, counters, thresholds, query_type)
        if item["IsLongTailEvidence"]:
            long_tail.append(item)
        if len(long_tail) >= 20:
            break

    broad_count = sum(1 for row in rows if clean_text(row.get("TermName")).lower() in BROAD_TERMS)
    top_pmid = pmid_counts.most_common(1)[0] if pmid_counts else ("-", 0)
    top_gene = gene_counts.most_common(1)[0] if gene_counts else ("-", 0)
    top_phenotype = phenotype_counts.most_common(1)[0] if phenotype_counts else ("-", 0)
    top_alteration = alteration_counts.most_common(1)[0] if alteration_counts else ("-", 0)
    meta = payload.get("meta") or {}
    overview_data = (overview or {}).get("data") or {}
    global_summary = overview_data.get("summary") if isinstance(overview_data.get("summary"), dict) else {}
    overview_event_count = global_summary.get("event_count")
    matched_event_count = meta.get("matched_event_count") or overview_event_count
    unique_count = len(rows)
    raw_count = len(raw)
    coverage_ratio = None
    if matched_event_count:
        try:
            coverage_ratio = round(raw_count / int(matched_event_count), 4)
        except (TypeError, ValueError, ZeroDivisionError):
            coverage_ratio = None

    bias_notes = [
        f"Curation pool source: {meta.get('curation_source', 'api_or_unknown')} ({meta.get('curation_scope', 'unknown scope')}).",
        f"Curation used {raw_count} curation pool row(s) and reduced them to {unique_count} event-unique row(s).",
        f"Event deduplication key: {QUERY_DEDUP_DESCRIPTIONS.get(query_type, QUERY_DEDUP_DESCRIPTIONS['generic'])}.",
    ]
    if matched_event_count:
        ratio_text = f"{coverage_ratio:.2%}" if coverage_ratio is not None else "unknown"
        bias_notes.append(f"The curation pool covers {raw_count} of {matched_event_count} event record(s) matched by the curation query ({ratio_text}).")
    if overview_event_count and matched_event_count and overview_event_count != matched_event_count:
        bias_notes.append(
            f"Overview event_count is {overview_event_count}; curation matched_event_count is {matched_event_count} because support retrieval may use a broader matching predicate than the overview endpoint."
        )
    if meta.get("limit_notice"):
        bias_notes.append(str(meta.get("limit_notice")))
    if unique_count:
        bias_notes.append(f"The most frequent PMID contributes {top_pmid[1]} of {unique_count} event-unique rows.")
        if query_type == "term":
            bias_notes.append(f"The most frequent gene is `{top_gene[0]}` with {top_gene[1]} event-unique row(s).")
        else:
            bias_notes.append(f"The most frequent phenotype is `{top_phenotype[0]}` with {top_phenotype[1]} event-unique row(s).")
        if top_alteration[1]:
            bias_notes.append(f"The most frequent alteration taxonomy appears in {top_alteration[1]} event-unique row(s).")
        bias_notes.append(f"Broad disease/background terms account for {broad_count} of {unique_count} event-unique rows.")
    if missing_year:
        bias_notes.append(f"{missing_year} event-unique row(s) lack usable year metadata.")

    package = {
        "global_statistics": overview_data,
        "coverage_scope": {
            "query_type": query_type,
            "curation_source": meta.get("curation_source"),
            "curation_scope": meta.get("curation_scope"),
            "overview_event_count": overview_event_count,
            "matched_event_count": matched_event_count,
            "curation_pool_rows": raw_count,
            "coverage_ratio": coverage_ratio,
            "api_limit_notice": meta.get("limit_notice"),
            "requested_selected_limit": requested_selected_limit,
            "returned_selected_count": returned_selected_count,
            "eligible_after_filter_count": eligible_after_filter_count,
            "selection_shortfall_reason": selection_shortfall_reason,
        },
        "selection_trace": {
            "requested_selected_limit": requested_selected_limit,
            "returned_selected_count": returned_selected_count,
            "eligible_after_filter_count": eligible_after_filter_count,
            "representative_count": len(representative),
            "selection_shortfall_reason": selection_shortfall_reason,
            "candidate_evidence_semantics": "candidate_evidence is the broad curated pool returned for downstream expert pruning; representative_evidence is the compact display subset.",
        },
        "deduplication_summary": {
            "curation_pool_row_count": raw_count,
            "event_unique_rows": unique_count,
            "event_deduplication_key": QUERY_DEDUP_DESCRIPTIONS.get(query_type, QUERY_DEDUP_DESCRIPTIONS["generic"]),
            "unique_pmids": len(pmid_counts),
            "unique_genes": len(gene_counts),
            "unique_phenotypes": len(phenotype_counts),
            "unique_terms": len(phenotype_counts),
            "unique_alteration_taxonomies": len(alteration_counts),
            "unique_gene_alterations": len(gene_alteration_counts),
            "unique_alteration_signatures": len(alteration_counts),
            "unique_hypotheses": len(hyp_counts),
        },
        "dominant_clusters": {
            "top_pmids": top_items(pmid_counts),
            "top_genes": top_items(gene_counts),
            "top_phenotypes": top_items(phenotype_counts),
            "top_terms": top_items(phenotype_counts),
            "top_gene_alterations": top_items(gene_alteration_counts),
            "top_alteration_taxonomies": top_items(alteration_counts),
            "top_hypotheses": top_items(hyp_counts),
            "evidence_types": top_items(type_counts),
            "mechanism_strata": top_items(strata_counts),
        },
        "query_relative_patterns": query_relative_patterns(counters, thresholds),
        "long_tail_definition": {
            "method": "Query-specific frequency <= min(Q25, 10) after event-level deduplication",
            "dimensions": QUERY_LONG_TAIL_DIMENSIONS.get(query_type, QUERY_LONG_TAIL_DIMENSIONS["generic"]),
            "thresholds": thresholds,
        },
        "long_tail_signals": long_tail,
        "evidence_type_groups": {
            evidence_type: [item for item in normalized if item["EvidenceType"] == evidence_type]
            for evidence_type in sorted({item["EvidenceType"] for item in normalized})
        },
        "mechanism_strata": {
            stratum: [item for item in normalized if stratum in item["MechanismStrata"]]
            for stratum in sorted({stratum for item in normalized for stratum in item["MechanismStrata"]})
        },
        "chronological_summary": [
            {
                "period": period,
                "row_count": period_row_counts.get(period, 0),
                "dominant_mechanism_strata": top_items(counter),
            }
            for period, counter in sorted(period_counts.items())
        ],
        "bias_notes": bias_notes,
        "candidate_evidence": normalized,
        "representative_evidence": representative,
        "selected_evidence": normalized,
    }
    return package


def render_curation_overview(curation: dict[str, Any]) -> list[str]:
    dedupe = curation.get("deduplication_summary") or {}
    long_tail = curation.get("long_tail_definition") or {}
    scope = curation.get("coverage_scope") or {}
    selection = curation.get("selection_trace") or {}
    global_stats = curation.get("global_statistics") or curation.get("curated_pool_statistics") or {}
    global_summary = global_stats.get("summary") if isinstance(global_stats.get("summary"), dict) else {}
    lines = [
        "## Evidence Curation Layer",
        "",
        "- Raw API `EvidenceScore` is ignored in skill reports and curation decisions.",
        f"- Sentence-level evidence source: {scope.get('curation_source') or 'unknown'} ({scope.get('curation_scope') or 'unknown scope'}).",
        f"- Expert annotation source: {scope.get('annotation_source') or 'not reported'}; rows marked invalid by LLM review are excluded from curated evidence by default when the API provides that flag.",
        f"- Curation pool rows: {dedupe.get('curation_pool_row_count', 0)}; event-unique rows after query-specific deduplication: {dedupe.get('event_unique_rows', 0)}.",
        f"- Overview event rows reported by the API: {scope.get('overview_event_count', 'unknown')}.",
        f"- Event deduplication key: {dedupe.get('event_deduplication_key')}.",
        f"- Unique PMIDs in curation pool: {dedupe.get('unique_pmids', 0)}; genes: {dedupe.get('unique_genes', 0)}; phenotypes: {dedupe.get('unique_phenotypes', dedupe.get('unique_terms', 0))}; alteration taxonomies: {dedupe.get('unique_alteration_taxonomies', 0)}; gene-alteration pairs: {dedupe.get('unique_gene_alterations', 0)}.",
        f"- Long-tail rule: {long_tail.get('method')} across dimensions {', '.join(long_tail.get('dimensions') or [])}; thresholds={long_tail.get('thresholds')}.",
        f"- Candidate selection: requested={selection.get('requested_selected_limit', scope.get('requested_selected_limit', 'unknown'))}; returned={selection.get('returned_selected_count', scope.get('returned_selected_count', 'unknown'))}; eligible={selection.get('eligible_after_filter_count', scope.get('eligible_after_filter_count', 'unknown'))}; representative={selection.get('representative_count', 'unknown')}; shortfall={selection.get('selection_shortfall_reason') or scope.get('selection_shortfall_reason') or '-'}.",
        "",
    ]
    if global_summary:
        lines.extend(
            [
                "### Complete query-pool statistics",
                "",
                f"- Statistics source: {global_summary.get('statistics_source') or 'curated_query_stats'}.",
                f"- Raw matched event records: {global_summary.get('raw_event_count', 'unknown')}.",
                f"- Event-unique records before final representative sampling: {global_summary.get('event_unique_count', 'unknown')}.",
                f"- Curated pool records available to the API: {global_summary.get('curated_pool_count', 'unknown')}.",
                f"- High-quality event records: {global_summary.get('high_quality_event_count', 'unknown')}; long-tail event records: {global_summary.get('long_tail_event_count', 'unknown')}; broad-background records: {global_summary.get('broad_background_count', 'unknown')}.",
                "- Selected evidence below is a representative expert-reviewed subset, not the full query distribution.",
                "",
            ]
        )
        for title, key in [
            ("Complete-pool top genes", "top_genes"),
            ("Complete-pool top phenotype/process features", "top_phenotypes"),
            ("Complete-pool top gene-alteration pairs", "top_gene_alterations"),
            ("Complete-pool alteration taxonomy", "top_alteration_taxonomies"),
            ("Complete-pool top hypotheses", "top_hypotheses"),
            ("Complete-pool evidence types", "evidence_types"),
            ("Complete-pool mechanism strata", "mechanism_strata"),
        ]:
            items = global_stats.get(key) or []
            if not items:
                continue
            lines.extend([f"#### {title}", ""])
            for item in items[:8]:
                lines.append(f"- {md(item.get('value'))}: {item.get('count')}")
            lines.append("")
    clusters = curation.get("dominant_clusters") or {}
    for title, key in [
        ("Dominant PMIDs", "top_pmids"),
        ("Top genes", "top_genes"),
        ("Top gene-alteration pairs", "top_gene_alterations"),
        ("Top phenotype/process features", "top_phenotypes"),
        ("Dominant alteration taxonomy", "top_alteration_taxonomies"),
        ("Evidence type distribution", "evidence_types"),
        ("Mechanism strata distribution", "mechanism_strata"),
    ]:
        lines.extend([f"### {title}", ""])
        items = clusters.get(key) or []
        if not items:
            lines.append("- None available.")
        for item in items[:5]:
            lines.append(f"- {md(item.get('value'))}: {item.get('count')}")
        lines.append("")
    patterns = curation.get("query_relative_patterns") or {}
    if patterns:
        lines.extend(["### Query-relative top and long-tail patterns", ""])
        lines.extend(["| Dimension | Top values | Long-tail values |", "| --- | --- | --- |"])
        for dimension, pattern in patterns.items():
            top_text = "; ".join(f"{item.get('value')} ({item.get('count')})" for item in pattern.get("top") or []) or "-"
            tail_text = "; ".join(f"{item.get('value')} ({item.get('count')})" for item in pattern.get("long_tail") or []) or "-"
            lines.append(f"| {md(pattern.get('label') or dimension)} | {md(top_text)} | {md(tail_text)} |")
        lines.append("")
    return lines


def render_selected_table(curation: dict[str, Any], title: str = "Curated Representative Evidence") -> list[str]:
    lines = [
        f"## {title}",
        "",
        "| # | PMID | Gene | Phenotype | Evidence type | Mechanism strata | Expert score | Annotation source |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    selected = curation.get("selected_evidence") or []
    if not selected:
        lines.append("| - | - | - | - | - | - | - | - |")
        return lines
    for idx, item in enumerate(selected, start=1):
        pmid_value = item.get("PMID") or "-"
        url = item.get("PubMedURL") or ""
        pmid_md = f"[{pmid_value}]({url})" if url else str(pmid_value)
        lines.append(
            "| {idx} | {pmid} | {gene} | {term} | {etype} | {strata} | {quality} | {source} |".format(
                idx=idx,
                pmid=pmid_md,
                gene=md(item.get("Gene")),
                term=md(item.get("TermName")),
                etype=md(item.get("EvidenceType")),
                strata=md("; ".join(item.get("MechanismStrata") or [])),
                quality=md(item.get("ExpertOverallScore") or item.get("SentenceQuality")),
                source=md(
                    f"{item.get('AnnotationSource') or '-'}"
                    f" ({item.get('AnnotationConfidence') or '-'})"
                ),
            )
        )
    return lines


def render_evidence_traces(curation: dict[str, Any], title: str = "Original Evidence Traces") -> list[str]:
    lines = [f"## {title}", ""]
    selected = curation.get("selected_evidence") or []
    if not selected:
        lines.append("No sentence-level evidence rows were selected.")
        return lines
    for idx, item in enumerate(selected, start=1):
        signals = []
        for signal in item.get("LongTailSignals") or []:
            signals.append(
                f"{signal.get('dimension')}={signal.get('value')} "
                f"(freq {signal.get('frequency')} <= threshold {signal.get('threshold')})"
            )
        lines.extend(
            [
                f"### Evidence {idx}: PMID {item.get('PMID') or '-'}",
                "",
                f"- PubMed: {item.get('PubMedURL') or '-'}",
                f"- Gene: {item.get('Gene') or '-'}",
                f"- Journal/Year: {item.get('Journal') or '-'} / {item.get('Year') or '-'}",
                f"- Phenotype: {item.get('TermName') or '-'}",
                f"- Hypothesis: {item.get('Hypothesis') or '-'}",
                f"- Evidence type: {item.get('EvidenceType') or '-'}",
                f"- Expert score/source: {item.get('ExpertOverallScore') or '-'} / {item.get('AnnotationSource') or '-'} ({item.get('AnnotationConfidence') or '-'})",
                f"- Expert reason: {item.get('ExpertReason') or '-'}",
                f"- Candidate mechanism strata: {'; '.join(item.get('MechanismStrata') or []) or '-'}",
                f"- Alteration taxonomy: {item.get('AlterationTaxonomy') or '-'}",
                f"- Gene-alteration: {item.get('GeneAlteration') or '-'}",
                f"- Alteration mention: {item.get('AlterationMention') or '-'}",
                f"- Alteration ID: {item.get('AlterationID') or '-'}",
                f"- Trigger/regulation context: {item.get('TriggerWord') or '-'} / {item.get('RegType') or '-'}",
                f"- Event dedup key: {item.get('EventDedupKey') or '-'}",
                f"- Long-tail signals: {', '.join(signals) or '-'}",
                f"- Curation reasons: {', '.join(item.get('CurationReasons') or []) or '-'}",
                f"- Original sentence: {item.get('Sentence') or '-'}",
                "",
            ]
        )
    return lines


def render_long_tail(curation: dict[str, Any]) -> list[str]:
    lines = ["## Long-Tail Evidence Signals", ""]
    signals = curation.get("long_tail_signals") or []
    if not signals:
        lines.append("No query-specific long-tail evidence signals were identified in the event-deduplicated curation pool.")
        return lines
    lines.extend(
        [
            "| # | PMID | Gene | Phenotype | Evidence type | Long-tail dimensions | Reasons |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for idx, item in enumerate(signals, start=1):
        pmid_value = item.get("PMID") or "-"
        url = item.get("PubMedURL") or ""
        pmid_md = f"[{pmid_value}]({url})" if url else str(pmid_value)
        dimension_text = "; ".join(
            f"{signal.get('dimension')}={signal.get('value')} ({signal.get('frequency')})"
            for signal in item.get("LongTailSignals") or []
        )
        lines.append(
            f"| {idx} | {pmid_md} | {md(item.get('Gene'))} | {md(item.get('TermName'))} | {md(item.get('EvidenceType'))} | {md(dimension_text or '-')} | {md(', '.join(item.get('CurationReasons') or []))} |"
        )
    return lines


def render_chronology(curation: dict[str, Any]) -> list[str]:
    lines = ["## Chronological Evidence Trajectory", ""]
    chronology = curation.get("chronological_summary") or []
    if not chronology:
        lines.append("No usable year metadata was available for chronological grouping.")
        return lines
    lines.extend(["| Period | Event-unique rows | Dominant mechanism strata |", "| --- | --- | --- |"])
    for item in chronology:
        strata = "; ".join(f"{entry.get('value')} ({entry.get('count')})" for entry in item.get("dominant_mechanism_strata") or [])
        lines.append(f"| {md(item.get('period'))} | {item.get('row_count')} | {md(strata or '-')} |")
    return lines
