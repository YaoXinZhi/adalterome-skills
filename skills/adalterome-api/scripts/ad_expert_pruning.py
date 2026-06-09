"""Reusable AD pathologist-style pruning for AD-Alterome case studies."""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from typing import Any


AD_PATHOLOGY_KEYWORDS = {
    "a beta",
    "abeta",
    "alzheimer",
    "amyloid",
    "apoe",
    "astrocyte",
    "autophagy",
    "bace",
    "cholesterol",
    "cognitive",
    "dementia",
    "endosome",
    "gliosis",
    "inflammation",
    "insulin",
    "lipid",
    "lysosomal",
    "memory",
    "microglia",
    "mitochond",
    "neurodegeneration",
    "neurofibrillary",
    "neuron",
    "neuronal",
    "oxidative",
    "phosphorylation",
    "plaque",
    "proteostasis",
    "psen",
    "ros",
    "synaptic",
    "tangle",
    "tau",
    "vascular",
}

MOLECULAR_MECHANISM_KEYWORDS = {
    "activation",
    "aggregation",
    "binding",
    "cleavage",
    "deposition",
    "expression",
    "inhibition",
    "knockdown",
    "knockout",
    "mutation",
    "oligomer",
    "phosphorylation",
    "polymorphism",
    "receptor",
    "regulation",
    "secretion",
    "silencing",
    "snp",
    "transgenic",
    "variant",
}

GENERIC_PATTERNS = {
    "associated with",
    "may be involved",
    "may play a role",
    "more research",
    "further studies",
    "these findings",
    "this study",
    "various",
}

HYPOTHESIS_FOCUS_TERMS = {
    "amyloid",
    "tau",
    "neuroinflammation",
    "inflammation",
    "cholinergic",
    "mitochondrial",
    "oxidative",
    "synaptic",
    "vascular",
    "hypothesis",
}

UNINFORMATIVE_DISPLAY_VALUES = {
    "-",
    "all",
    "catalytic activity",
    "clinical course",
    "disease",
    "not applicable to any ad hypothesis",
    "occasional",
    "onset",
    "protein",
    "sporadic",
    "various",
}

STOPWORDS = {
    "a",
    "about",
    "and",
    "are",
    "between",
    "does",
    "for",
    "from",
    "how",
    "in",
    "into",
    "is",
    "of",
    "on",
    "or",
    "the",
    "to",
    "what",
    "with",
}

EVIDENCE_TYPE_BONUS = {
    "molecular_mechanism": 20,
    "model_or_intervention": 18,
    "alteration_evidence": 16,
    "cellular_or_pathway_process": 15,
    "clinical_or_cohort_association": 8,
    "unclear_or_mixed": 0,
    "broad_background": -8,
}


def normalize_text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip()).lower()


def normalize_key(value: Any) -> str:
    return re.sub(r"[^a-z0-9]+", " ", normalize_text(value)).strip()


def question_terms(question: str) -> set[str]:
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9_-]{2,}", question.lower())
    return {token for token in tokens if token not in STOPWORDS}


def item_blob(item: dict[str, Any]) -> str:
    parts = [
        item.get("Gene"),
        item.get("TermName"),
        item.get("Hypothesis"),
        item.get("EvidenceType"),
        item.get("AlterationTaxonomy"),
        item.get("AlterationMention"),
        item.get("Event"),
        item.get("Sentence"),
        " ".join(item.get("MechanismStrata") or []),
        " ".join(item.get("CurationReasons") or []),
        item.get("ExpertReason"),
    ]
    return " ".join(str(part) for part in parts if part).lower()


def keyword_hits(blob: str, keywords: set[str]) -> int:
    return sum(1 for keyword in keywords if keyword in blob)


def as_float(value: Any, default: float = 0.0) -> float:
    try:
        if value in (None, "", "-"):
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def yes(value: Any) -> bool:
    return str(value or "").strip().lower() == "yes"


def is_not_applicable_hypothesis(value: Any) -> bool:
    text = normalize_key(value)
    return text == "not applicable to any ad hypothesis" or text.startswith("not applicable")


def hypothesis_countable(item: dict[str, Any]) -> bool:
    return not is_not_applicable_hypothesis(item.get("Hypothesis"))


def hypothesis_focused_question(question: str, mode: str) -> bool:
    if mode == "hypothesis":
        return True
    lowered = normalize_text(question)
    if "假说" in lowered:
        return True
    return any(term in lowered for term in HYPOTHESIS_FOCUS_TERMS if term == "hypothesis")


def annotation_confidence_bonus(value: Any) -> tuple[float, str | None]:
    confidence = normalize_text(value)
    if confidence == "high":
        return 6.0, "high-confidence expert annotation"
    if confidence == "medium":
        return 3.0, "medium-confidence expert annotation"
    if confidence == "low":
        return -2.0, "low-confidence expert annotation"
    return 0.0, None


def score_evidence(
    item: dict[str, Any],
    *,
    target_label: str,
    question: str,
    mode: str,
) -> dict[str, Any]:
    blob = item_blob(item)
    q_terms = question_terms(question)
    score = 0.0
    reasons: list[str] = []
    cautions: list[str] = []

    evidence_type = str(item.get("EvidenceType") or "unclear_or_mixed")
    type_bonus = EVIDENCE_TYPE_BONUS.get(evidence_type, 0)
    score += type_bonus
    if type_bonus > 0:
        reasons.append(f"{evidence_type} evidence")
    elif type_bonus < 0:
        cautions.append("broad background evidence")

    sentence_quality = as_float(item.get("SentenceQuality"))
    sq_bonus = max(0.0, min(12.0, sentence_quality / 5.0))
    score += sq_bonus
    if sq_bonus >= 8:
        reasons.append("informative original sentence")

    expert_overall = as_float(item.get("ExpertOverallScore"))
    if expert_overall > 0:
        score += min(18.0, expert_overall * 3.2)
        reasons.append(f"curation expert score {expert_overall:g}/5")

    for field, label in [
        ("ExpertMechanismSpecificityScore", "mechanism specificity"),
        ("ExpertPathologyGranularityScore", "pathology granularity"),
        ("ExpertExperimentalDirectnessScore", "experimental directness"),
        ("ExpertAlterationInformativenessScore", "alteration informativeness"),
    ]:
        value = as_float(item.get(field))
        if value >= 4:
            score += 2.5
            reasons.append(f"strong {label}")

    bonus, confidence_reason = annotation_confidence_bonus(item.get("AnnotationConfidence"))
    score += bonus
    if confidence_reason:
        reasons.append(confidence_reason) if bonus > 0 else cautions.append(confidence_reason)

    annotation_source = normalize_text(item.get("AnnotationSource"))
    if annotation_source == "llm_reviewed":
        score += 4
        reasons.append("LLM-reviewed curation annotation")
    elif annotation_source == "heuristic_only":
        cautions.append("heuristic-only annotation")

    ad_hits = keyword_hits(blob, AD_PATHOLOGY_KEYWORDS)
    if ad_hits:
        score += min(18, ad_hits * 3)
        reasons.append("AD-pathology vocabulary present")

    mechanism_hits = keyword_hits(blob, MOLECULAR_MECHANISM_KEYWORDS)
    if mechanism_hits:
        score += min(14, mechanism_hits * 2)
        reasons.append("molecular or experimental mechanism detail")

    strata = [str(value) for value in item.get("MechanismStrata") or []]
    if strata and not any("unclear" in value.lower() or "broad" in value.lower() for value in strata):
        score += 8
        reasons.append("maps to a candidate AD mechanism stratum")

    if item.get("IsLongTailEvidence"):
        score += 10
        reasons.append("long-tail signal with possible discovery value")

    if yes(item.get("MechanismProvided")):
        score += 8
        reasons.append("AD-Alterome marks a mechanism as provided")

    if yes(item.get("RelevantToAD")):
        score += 8
        reasons.append("AD-Alterome marks the row as AD-relevant")

    pmid = str(item.get("PMID") or "-")
    if pmid != "-":
        score += 4
        reasons.append("PMID-traceable")

    if q_terms:
        overlap = sorted(term for term in q_terms if term in blob)
        if overlap:
            score += min(12, len(overlap) * 3)
            reasons.append(f"matches user question terms: {', '.join(overlap[:5])}")

    not_applicable = not hypothesis_countable(item)
    hypothesis_focused = hypothesis_focused_question(question, mode)
    if not_applicable:
        if hypothesis_focused:
            score -= 18
            cautions.append("not countable as support for a named AD hypothesis")
        else:
            reasons.append("mechanism evidence retained outside hypothesis counts")

    sentence = str(item.get("Sentence") or "")
    if len(sentence) < 60:
        score -= 8
        cautions.append("short sentence may be under-informative")
    if len(sentence) > 850:
        score -= 5
        cautions.append("long sentence may need manual trimming")

    generic_hits = keyword_hits(blob, GENERIC_PATTERNS)
    if generic_hits >= 2:
        score -= 10
        cautions.append("generic association language")
    elif generic_hits == 1 and evidence_type in {"clinical_or_cohort_association", "broad_background"}:
        score -= 4
        cautions.append("association-heavy support")

    if mode == "compare" and target_label and target_label.lower() in blob:
        score += 3

    score = round(score, 2)
    if score >= 68:
        tier = "high_insight"
        decision = "include"
    elif score >= 48:
        tier = "moderate_insight"
        decision = "include"
    elif score >= 32:
        tier = "context"
        decision = "secondary"
    else:
        tier = "low_context"
        decision = "deprioritize"

    if not_applicable and hypothesis_focused and decision == "include":
        decision = "secondary"
        tier = "context"
    if cautions and decision == "include" and score < 56:
        decision = "secondary"
        tier = "context"

    return {
        **item,
        "Target": target_label,
        "ExpertScore": score,
        "ExpertTier": tier,
        "ExpertDecision": decision,
        "ExpertReasons": reasons[:8],
        "ExpertCautions": cautions[:6],
        "HypothesisCountable": not not_applicable,
        "HypothesisRole": "not_counted" if not_applicable else "counted",
        "NarrativeEligibility": "context_only" if not_applicable and hypothesis_focused else "mechanism_eligible",
    }


def duplicate_key(item: dict[str, Any]) -> tuple[str, str, str]:
    target = normalize_key(item.get("Target") or "")
    pmid = normalize_key(item.get("PMID") or "-")
    sentence = normalize_key(item.get("Sentence") or "")
    event_key = normalize_key(item.get("EventDedupKey") or "")
    if pmid and sentence:
        return ("pmid_sentence", target, f"{pmid}|{sentence[:260]}")
    if pmid and event_key:
        return ("pmid_event", target, f"{pmid}|{event_key}")
    fallback = "|".join(
        normalize_key(item.get(field) or "")
        for field in ["Gene", "TermName", "Hypothesis", "GeneAlteration", "Event"]
    )
    return ("fallback", target, fallback)


def unique_values(items: list[dict[str, Any]], field: str, limit: int = 12) -> list[str]:
    values: list[str] = []
    seen: set[str] = set()
    for item in items:
        value = str(item.get(field) or "").strip()
        if not value or normalize_text(value) in UNINFORMATIVE_DISPLAY_VALUES:
            continue
        key = normalize_key(value)
        if key in seen:
            continue
        seen.add(key)
        values.append(value)
        if len(values) >= limit:
            break
    return values


def merge_duplicate_group(group_id: str, items: list[dict[str, Any]]) -> dict[str, Any]:
    ordered = sorted(
        items,
        key=lambda item: (
            item.get("ExpertScore", 0),
            1 if item.get("HypothesisCountable") else 0,
            as_float(item.get("SentenceQuality")),
            as_float(item.get("ExpertOverallScore")),
        ),
        reverse=True,
    )
    representative = dict(ordered[0])
    representative["DuplicateGroupID"] = group_id
    representative["DuplicateGroupSize"] = len(items)
    representative["MergedFrom"] = [
        {
            "PMID": item.get("PMID"),
            "Gene": item.get("Gene"),
            "TermName": item.get("TermName"),
            "Hypothesis": item.get("Hypothesis"),
            "EventDedupKey": item.get("EventDedupKey"),
        }
        for item in ordered
    ]
    representative["MergedHypotheses"] = unique_values(ordered, "Hypothesis")
    representative["MergedPhenotypes"] = unique_values(ordered, "TermName")
    representative["MergedGeneAlterations"] = unique_values(ordered, "GeneAlteration")

    merged_strata: list[str] = []
    seen_strata: set[str] = set()
    for item in ordered:
        for value in item.get("MechanismStrata") or []:
            clean = str(value or "").strip()
            key = normalize_key(clean)
            if clean and key not in seen_strata:
                seen_strata.add(key)
                merged_strata.append(clean)
    if merged_strata:
        representative["MechanismStrata"] = merged_strata[:10]

    if len(items) > 1:
        reasons = list(representative.get("ExpertReasons") or [])
        reasons.append(f"merged {len(items)} duplicate or overlapping evidence rows")
        representative["ExpertReasons"] = reasons[:8]
        representative["ExpertCautions"] = list(representative.get("ExpertCautions") or [])[:6]
    return representative


def merge_duplicate_evidence(scored: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    groups: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for item in scored:
        groups[duplicate_key(item)].append(item)

    merged: list[dict[str, Any]] = []
    duplicate_groups: list[dict[str, Any]] = []
    for index, (key, items) in enumerate(groups.items(), start=1):
        group_id = f"dup_{index:04d}"
        representative = merge_duplicate_group(group_id, items)
        merged.append(representative)
        if len(items) > 1:
            duplicate_groups.append(
                {
                    "DuplicateGroupID": group_id,
                    "DuplicateKey": "|".join(key),
                    "row_count": len(items),
                    "representative_pmid": representative.get("PMID"),
                    "representative_sentence": representative.get("Sentence"),
                    "merged_hypotheses": representative.get("MergedHypotheses"),
                    "merged_phenotypes": representative.get("MergedPhenotypes"),
                }
            )
    return merged, duplicate_groups


def select_expert_evidence(
    scored: list[dict[str, Any]],
    *,
    mode: str,
    expert_limit: int,
) -> dict[str, Any]:
    scored_sorted = sorted(scored, key=lambda item: (item.get("ExpertScore", 0), item.get("SentenceQuality", 0)), reverse=True)
    included: list[dict[str, Any]] = []
    additional: list[dict[str, Any]] = []
    secondary: list[dict[str, Any]] = []
    deprioritized: list[dict[str, Any]] = []

    if mode == "compare":
        by_target: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for item in scored_sorted:
            by_target[str(item.get("Target") or "target")].append(item)
        per_target_floor = max(1, expert_limit // max(1, len(by_target)))
        for _target, items in by_target.items():
            target_included = [item for item in items if item.get("ExpertDecision") == "include"][:per_target_floor]
            included.extend(target_included)
        for item in scored_sorted:
            if len(included) >= expert_limit:
                break
            if item.get("ExpertDecision") == "include" and item not in included:
                included.append(item)
    else:
        included = [item for item in scored_sorted if item.get("ExpertDecision") == "include"][:expert_limit]

    included_keys = {(item.get("Target"), item.get("PMID"), item.get("Sentence")) for item in included}
    for item in scored_sorted:
        key = (item.get("Target"), item.get("PMID"), item.get("Sentence"))
        if key in included_keys:
            continue
        if item.get("ExpertDecision") == "include":
            additional.append(item)
        elif item.get("ExpertDecision") == "secondary":
            secondary.append(item)
        else:
            deprioritized.append(item)

    return {
        "included_evidence": included[:expert_limit],
        "additional_high_scoring_evidence": additional[: max(10, expert_limit)],
        "secondary_evidence": secondary[: max(10, expert_limit)],
        "deprioritized_evidence": deprioritized[: max(10, expert_limit)],
        "all_scored_evidence": scored_sorted,
    }


def mechanism_counts(items: list[dict[str, Any]]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for item in items:
        for stratum in item.get("MechanismStrata") or []:
            counter[str(stratum)] += 1
    return counter


def top_field(items: list[dict[str, Any]], field: str, limit: int = 5) -> list[str]:
    counter = Counter(
        str(item.get(field) or "").strip()
        for item in items
        if str(item.get(field) or "").strip()
        and normalize_text(item.get(field)) not in UNINFORMATIVE_DISPLAY_VALUES
    )
    return [value for value, _ in counter.most_common(limit)]


def unique_preserve(values: list[str], limit: int = 6) -> list[str]:
    output: list[str] = []
    seen: set[str] = set()
    for value in values:
        clean = str(value or "").strip()
        key = normalize_key(clean)
        if not clean or normalize_text(clean) in UNINFORMATIVE_DISPLAY_VALUES or key in seen:
            continue
        seen.add(key)
        output.append(clean)
        if len(output) >= limit:
            break
    return output


def evidence_reason_text(item: dict[str, Any]) -> str:
    reasons = item.get("ExpertReasons") or []
    cautions = item.get("ExpertCautions") or []
    text = "; ".join(reasons[:3]) or "traceable AD-Alterome evidence"
    flags: list[str] = []
    if item.get("DuplicateGroupSize", 1) > 1:
        flags.append(f"merged x{item.get('DuplicateGroupSize')}")
    if not item.get("HypothesisCountable", True):
        flags.append("not counted for hypothesis statistics")
    if item.get("IsLongTailEvidence"):
        flags.append("long-tail")
    if flags:
        text += f" [{'; '.join(flags)}]"
    if cautions:
        text += f" (caution: {'; '.join(cautions[:2])})"
    return text


def pruning_policy(question: str, mode: str, expert_limit: int) -> dict[str, Any]:
    return {
        "role": "AD pathologist biological pruning over AD-Alterome curated evidence",
        "question": question,
        "mode": mode,
        "expert_limit": expert_limit,
        "hypothesis_focused_question": hypothesis_focused_question(question, mode),
        "not_applicable_rule": (
            "Not-applicable hypothesis labels are not counted in hypothesis statistics. "
            "They may remain eligible for mechanism narrative unless the user asks for a named hypothesis."
        ),
        "duplicate_rule": (
            "Merge exact or overlapping evidence by target, PMID, sentence, and EventDedupKey before selecting narrative evidence."
        ),
    }


def run_ad_expert_pruning(
    candidates: list[dict[str, Any]],
    *,
    mode: str,
    question: str,
    expert_limit: int,
) -> dict[str, Any]:
    scored = [
        score_evidence(item, target_label=str(item.get("Target") or ""), question=question, mode=mode)
        for item in candidates
    ]
    merged, duplicate_groups = merge_duplicate_evidence(scored)
    selected = select_expert_evidence(merged, mode=mode, expert_limit=expert_limit)
    selected["premerge_candidate_count"] = len(candidates)
    selected["postmerge_candidate_count"] = len(merged)
    selected["duplicate_group_count"] = len(duplicate_groups)
    selected["duplicate_groups"] = duplicate_groups
    selected["pruning_policy"] = pruning_policy(question, mode, expert_limit)
    selected["merged_evidence"] = merged
    selected["excluded_or_deprioritized_evidence"] = (
        selected.get("secondary_evidence", []) + selected.get("deprioritized_evidence", [])
    )
    selected["hypothesis_count_summary"] = {
        "countable": sum(1 for item in merged if item.get("HypothesisCountable")),
        "not_counted": sum(1 for item in merged if not item.get("HypothesisCountable")),
    }
    return selected
