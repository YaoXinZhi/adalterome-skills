#!/usr/bin/env python3
"""Build an AD pathologist-style AD-Alterome expert case-study report."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


SKILLS_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(SKILLS_DIR / "adalterome-api" / "scripts"))

from evidence_curation import build_curation_package, md  # noqa: E402
from evidence_fetch import (  # noqa: E402
    API_MAX_TOP_K,
    curation_package_from_response,
    fetch_gene_events_for_curation,
    fetch_hypothesis_support_for_curation,
    fetch_term_events_for_curation,
    request_json_optional,
)


DEFAULT_BASE_URL = os.environ.get("ADALTEROME_API_BASE_URL", "http://117.72.176.137/api/adalterome")

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

UNINFORMATIVE_DISPLAY_VALUES = {
    "-",
    "all",
    "catalytic activity",
    "clinical course",
    "disease",
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


def get_json(base_url: str, path: str, params: dict[str, Any], timeout: float) -> tuple[str, dict[str, Any]]:
    query = urlencode(params, doseq=True)
    url = f"{base_url.rstrip('/')}{path}"
    if query:
        url = f"{url}?{query}"
    request = Request(url, headers={"Accept": "application/json"})
    try:
        with urlopen(request, timeout=timeout) as response:
            return url, json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        raise SystemExit(f"API HTTP error {exc.code}: {exc.reason}") from exc
    except URLError as exc:
        raise SystemExit(f"API connection error: {exc.reason}") from exc


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def normalize_identifier(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", value.strip()).strip("_").lower() or "target"


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

    if cautions and decision == "include" and score < 56:
        decision = "secondary"
        tier = "context"

    return {
        **item,
        "Target": target_label,
        "ExpertScore": score,
        "ExpertTier": tier,
        "ExpertDecision": decision,
        "ExpertReasons": reasons[:6],
        "ExpertCautions": cautions[:5],
    }


def coverage_record(label: str, curation: dict[str, Any], fallback_reason: str | None = None) -> dict[str, Any]:
    scope = curation.get("coverage_scope") or {}
    dedupe = curation.get("deduplication_summary") or {}
    curation_scope = scope.get("curation_scope") or "unknown"
    coverage_ratio = scope.get("coverage_ratio")
    warnings: list[str] = []
    if curation_scope == "api_sentence_sample":
        warnings.append("fallback_to_capped_api_sentence_sample")
    if coverage_ratio is not None and as_float(coverage_ratio) < 0.1:
        warnings.append("low_fraction_of_matched_events_in_curation_pool")
    if dedupe.get("event_unique_rows", 0) and dedupe.get("curation_pool_row_count", 0) == API_MAX_TOP_K:
        warnings.append("curation_pool_may_be_api_capped")
    if fallback_reason:
        warnings.append(f"full_pool_curation_unavailable: {fallback_reason}")
    return {
        "label": label,
        "curation_source": scope.get("curation_source"),
        "curation_scope": curation_scope,
        "overview_event_count": scope.get("overview_event_count"),
        "matched_event_count": scope.get("matched_event_count"),
        "curation_pool_rows": dedupe.get("curation_pool_row_count"),
        "event_unique_rows": dedupe.get("event_unique_rows"),
        "unique_pmids": dedupe.get("unique_pmids"),
        "coverage_ratio": coverage_ratio,
        "warnings": warnings,
    }


def balance_status(records: list[dict[str, Any]]) -> dict[str, Any]:
    if len(records) < 2:
        return {"status": "not_applicable", "notes": []}
    notes: list[str] = []
    scopes = {record.get("curation_scope") for record in records}
    ratios = [as_float(record.get("coverage_ratio"), default=-1) for record in records if record.get("coverage_ratio") is not None]
    status = "balanced"
    if len(scopes) > 1:
        status = "imbalanced"
        notes.append("Targets used different curation scopes.")
    if any(record.get("curation_scope") == "api_sentence_sample" for record in records):
        status = "exploratory"
        notes.append("At least one target fell back to capped sentence sampling.")
    if len(ratios) >= 2 and max(ratios) - min(ratios) > 0.3:
        status = "imbalanced" if status == "balanced" else status
        notes.append("Coverage ratios differ substantially across targets.")
    if status == "balanced":
        notes.append("Targets have comparable curation scope for case-study synthesis.")
    return {"status": status, "notes": notes}


def try_curation(
    base_url: str,
    path: str,
    params: dict[str, Any],
    timeout: float,
    candidate_limit: int,
) -> tuple[str, dict[str, Any] | None, str | None]:
    url, payload, error = request_json_optional(
        base_url,
        path,
        {**params, "selected_limit": candidate_limit},
        timeout,
    )
    if error:
        return url, None, error
    if not isinstance(payload, dict) or payload.get("status") != "ok":
        return url, None, "curation endpoint returned no ok payload"
    curation = (payload.get("data") or {}).get("curation")
    if not isinstance(curation, dict):
        return url, None, "curation endpoint returned no curation object"
    scope = curation.setdefault("coverage_scope", {})
    scope["curation_endpoint_url"] = url
    scope.setdefault("curation_source", payload.get("meta", {}).get("curation_source", "remote_api"))
    scope.setdefault("curation_scope", payload.get("meta", {}).get("curation_scope", "server_full_query_pool"))
    return url, payload, None


def fetch_target(
    *,
    kind: str,
    label: str,
    base_url: str,
    timeout: float,
    candidate_limit: int,
    curation_limit: int,
) -> dict[str, Any]:
    query_type = {"gene": "gene", "term": "term", "hypothesis": "hypothesis", "compare_gene": "compare_gene"}[kind]
    if kind in {"gene", "compare_gene"}:
        overview_url, overview = get_json(base_url, "/gene/overview", {"gene": label}, timeout)
        curation_url, curation_payload, fallback_reason = try_curation(
            base_url,
            "/gene/curation",
            {"gene": label},
            timeout,
            candidate_limit,
        )
        if curation_payload:
            evidence_url = curation_url
            evidence_payload = curation_payload
            curation = curation_package_from_response(curation_payload) or {}
        else:
            evidence_url, evidence_payload = fetch_gene_events_for_curation(
                base_url,
                label,
                timeout,
                curation_limit=curation_limit,
            )
            curation = build_curation_package(
                evidence_payload,
                overview=overview,
                selected_limit=candidate_limit,
                query_type=query_type,
            )
    elif kind == "term":
        overview_url, overview = get_json(base_url, "/term/overview", {"term": label}, timeout)
        curation_url, curation_payload, fallback_reason = try_curation(
            base_url,
            "/term/curation",
            {"term": label},
            timeout,
            candidate_limit,
        )
        if curation_payload:
            evidence_url = curation_url
            evidence_payload = curation_payload
            curation = curation_package_from_response(curation_payload) or {}
        else:
            evidence_url, evidence_payload = fetch_term_events_for_curation(
                base_url,
                label,
                timeout,
                curation_limit=curation_limit,
            )
            curation = build_curation_package(
                evidence_payload,
                overview=overview,
                selected_limit=candidate_limit,
                query_type=query_type,
            )
    elif kind == "hypothesis":
        overview_url, overview = get_json(base_url, "/hypothesis/overview", {"hypothesis": label}, timeout)
        curation_url, curation_payload, fallback_reason = try_curation(
            base_url,
            "/hypothesis/curation",
            {"hypothesis": label},
            timeout,
            candidate_limit,
        )
        if curation_payload:
            evidence_url = curation_url
            evidence_payload = curation_payload
            curation = curation_package_from_response(curation_payload) or {}
        else:
            evidence_url, evidence_payload = fetch_hypothesis_support_for_curation(
                base_url,
                label,
                timeout,
                curation_limit=curation_limit,
            )
            curation = build_curation_package(
                evidence_payload,
                overview=overview,
                selected_limit=candidate_limit,
                query_type=query_type,
            )
    else:
        raise ValueError(f"Unsupported target kind: {kind}")

    return {
        "kind": kind,
        "label": label,
        "overview_url": overview_url,
        "evidence_url": evidence_url,
        "overview": overview,
        "evidence_payload": evidence_payload,
        "curation": curation,
        "fallback_reason": fallback_reason,
    }


def infer_mode(args: argparse.Namespace) -> str:
    if args.gene_a and args.gene_b:
        return "compare"
    if args.gene:
        return "gene"
    if args.term:
        return "term"
    if args.hypothesis:
        return "hypothesis"
    raise SystemExit("Provide --gene, --term, --hypothesis, or both --gene-a and --gene-b.")


def default_question(args: argparse.Namespace, mode: str) -> str:
    if args.question:
        return args.question
    if mode == "compare":
        return f"How do {args.gene_a} and {args.gene_b} differ or converge in AD pathological mechanisms?"
    if mode == "gene":
        return f"What AD-relevant molecular and pathological mechanisms are supported for {args.gene}?"
    if mode == "term":
        return f"Which AD genes and mechanisms make {args.term} a biologically meaningful pathological process?"
    return f"What gene and phenotype evidence supports the {args.hypothesis} in AD-Alterome?"


def collect_candidate_items(datasets: list[dict[str, Any]]) -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()
    for dataset in datasets:
        curation = dataset.get("curation") or {}
        rows = list(curation.get("selected_evidence") or [])
        rows.extend(curation.get("long_tail_signals") or [])
        for item in rows:
            key = (
                str(dataset.get("label") or ""),
                str(item.get("PMID") or "-"),
                str(item.get("Sentence") or "-")[:220],
            )
            if key in seen:
                continue
            seen.add(key)
            candidates.append({**item, "Target": dataset.get("label")})
    return candidates


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
        for target, items in by_target.items():
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
        and str(item.get(field) or "").strip().lower() not in UNINFORMATIVE_DISPLAY_VALUES
    )
    return [value for value, _ in counter.most_common(limit)]


def unique_preserve(values: list[str], limit: int = 6) -> list[str]:
    output: list[str] = []
    seen: set[str] = set()
    for value in values:
        clean = str(value or "").strip()
        if not clean or clean.lower() in UNINFORMATIVE_DISPLAY_VALUES or clean in seen:
            continue
        seen.add(clean)
        output.append(clean)
        if len(output) >= limit:
            break
    return output


def evidence_reason_text(item: dict[str, Any]) -> str:
    reasons = item.get("ExpertReasons") or []
    cautions = item.get("ExpertCautions") or []
    text = "; ".join(reasons[:3]) or "traceable AD-Alterome evidence"
    if cautions:
        text += f" (caution: {'; '.join(cautions[:2])})"
    return text


def render_coverage_table(coverage: dict[str, Any]) -> list[str]:
    lines = [
        "## Coverage and Balance Check",
        "",
        "| Target | Curation scope | Pool rows | Event-unique rows | Matched events | Coverage ratio | Warnings |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for record in coverage.get("targets") or []:
        ratio = record.get("coverage_ratio")
        ratio_text = "-" if ratio is None else f"{float(ratio):.2%}"
        lines.append(
            "| {label} | {scope} | {pool} | {unique} | {matched} | {ratio} | {warnings} |".format(
                label=md(record.get("label")),
                scope=md(record.get("curation_scope")),
                pool=md(record.get("curation_pool_rows")),
                unique=md(record.get("event_unique_rows")),
                matched=md(record.get("matched_event_count")),
                ratio=ratio_text,
                warnings=md("; ".join(record.get("warnings") or []) or "-"),
            )
        )
    balance = coverage.get("balance") or {}
    lines.extend(["", f"- Balance status: `{balance.get('status')}`"])
    for note in balance.get("notes") or []:
        lines.append(f"- {note}")
    return lines


def render_included_table(
    items: list[dict[str, Any]],
    title: str,
    empty_message: str = "No evidence rows available.",
) -> list[str]:
    lines = [
        f"## {title}",
        "",
        "| Rank | Target | Score | PMID | Gene | Phenotype | Mechanism strata | Expert reason |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    if not items:
        lines.append(f"| - | - | - | - | - | - | - | {md(empty_message)} |")
        return lines
    for idx, item in enumerate(items, start=1):
        pmid = item.get("PMID") or "-"
        url = item.get("PubMedURL") or ""
        pmid_text = f"[{pmid}]({url})" if url else str(pmid)
        lines.append(
            "| {idx} | {target} | {score} | {pmid} | {gene} | {term} | {strata} | {reason} |".format(
                idx=idx,
                target=md(item.get("Target")),
                score=md(item.get("ExpertScore")),
                pmid=pmid_text,
                gene=md(item.get("Gene")),
                term=md(item.get("TermName")),
                strata=md("; ".join(item.get("MechanismStrata") or [])),
                reason=md(evidence_reason_text(item)),
            )
        )
    return lines


def render_trace_list(items: list[dict[str, Any]], title: str) -> list[str]:
    lines = [f"## {title}", ""]
    if not items:
        lines.append("No evidence rows available.")
        return lines
    for idx, item in enumerate(items, start=1):
        pmid = item.get("PMID") or "-"
        url = item.get("PubMedURL") or ""
        pmid_text = f"[{pmid}]({url})" if url else str(pmid)
        reasons = "; ".join(item.get("ExpertReasons") or []) or "-"
        cautions = "; ".join(item.get("ExpertCautions") or []) or "-"
        lines.extend(
            [
                f"### {idx}. {md(item.get('Target'))} / PMID {pmid_text}",
                "",
                f"- Expert score: `{item.get('ExpertScore')}`; tier: `{item.get('ExpertTier')}`; decision: `{item.get('ExpertDecision')}`",
                f"- Gene/term/hypothesis: `{md(item.get('Gene'))}` / `{md(item.get('TermName'))}` / `{md(item.get('Hypothesis'))}`",
                f"- Mechanism strata: {md('; '.join(item.get('MechanismStrata') or []) or '-')}",
                f"- Reasons: {md(reasons)}",
                f"- Cautions: {md(cautions)}",
                f"- Original sentence: {md(item.get('Sentence'))}",
                "",
            ]
        )
    return lines


def render_expert_synthesis(
    *,
    mode: str,
    title: str,
    question: str,
    included: list[dict[str, Any]],
    secondary: list[dict[str, Any]],
    coverage: dict[str, Any],
) -> list[str]:
    lines = [
        "## AD Pathologist-Style Synthesis",
        "",
    ]
    if not included:
        lines.append("The expert screen did not find enough high-insight evidence to support a strong case-study argument. Treat this output as an audit package and rerun with broader coverage or review the secondary evidence manually.")
        return lines

    strata = mechanism_counts(included)
    dominant_strata = [value for value, _ in strata.most_common(4)]
    genes = top_field(included, "Gene", limit=6)
    terms = top_field(included, "TermName", limit=6)
    balance = (coverage.get("balance") or {}).get("status")

    if mode == "compare":
        by_target: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for item in included:
            by_target[str(item.get("Target") or "target")].append(item)
        lines.append(
            f"For the question `{md(question)}`, the strongest AD-Alterome case-study frame is a coverage-aware contrast across {', '.join(by_target)}. The visible high-insight evidence clusters around {md(', '.join(dominant_strata) or 'mixed mechanisms')}."
        )
        if balance != "balanced":
            lines.append(
                f"Because the balance status is `{balance}`, this should be written as an exploratory contrast rather than a definitive ranking of the genes."
            )
        for target, items in by_target.items():
            target_strata = [value for value, _ in mechanism_counts(items).most_common(3)]
            lines.append(
                f"- `{md(target)}`: prioritize {md(', '.join(target_strata) or 'mixed evidence')} and verify extracted phenotype labels against the original sentences before writing fine-grained biological claims."
            )
    elif mode == "gene":
        lines.append(
            f"For `{md(title)}`, the report should argue the scientific question through {md(', '.join(dominant_strata) or 'mixed AD mechanisms')}. The highest-value evidence is the original sentence-level molecular and pathological mechanism support; extracted phenotype labels should be treated as audit fields rather than the main biological conclusion."
        )
    elif mode == "term":
        lines.append(
            f"For `{md(title)}`, AD-Alterome supports a process-centered case study anchored in genes such as {md(', '.join(genes) or '-')}. The expert screen favors evidence that turns the term from a broad disease label into mechanisms across {md(', '.join(dominant_strata) or 'mixed pathology')}."
        )
    else:
        lines.append(
            f"For `{md(title)}`, the useful case-study argument is not that the hypothesis is proven, but that AD-Alterome organizes gene and phenotype evidence into {md(', '.join(dominant_strata) or 'multiple support patterns')}."
        )

    long_tail = [item for item in included if item.get("IsLongTailEvidence")]
    if long_tail:
        candidates = []
        for item in long_tail[:6]:
            label = item.get("GeneAlteration") or item.get("Gene") or item.get("TermName") or item.get("Target")
            candidates.append(str(label))
        candidates = unique_preserve(candidates)
        lines.append(
            f"Long-tail evidence should be protected rather than discarded: {md(', '.join(candidates))} may provide mechanistic leads that a frequency-only report would under-emphasize."
        )

    if secondary:
        lines.append(
            "Secondary evidence can support caveats and background, but the main narrative should rely on the included evidence table and original sentence traces."
        )
    return lines


def render_report(
    *,
    mode: str,
    title: str,
    question: str,
    strategy: list[str],
    datasets: list[dict[str, Any]],
    coverage: dict[str, Any],
    expert_evidence: dict[str, Any],
) -> str:
    included = expert_evidence.get("included_evidence") or []
    additional = expert_evidence.get("additional_high_scoring_evidence") or []
    secondary = expert_evidence.get("secondary_evidence") or []
    deprioritized = expert_evidence.get("deprioritized_evidence") or []
    lines = [
        f"# AD-Alterome Expert Case Study: {title}",
        "",
        "## Interpreted Scientific Question",
        "",
        question,
        "",
        "## Evidence Strategy",
        "",
    ]
    for item in strategy:
        lines.append(f"- {item}")
    lines.extend([""])
    lines.extend(render_coverage_table(coverage))
    lines.extend([""])
    lines.extend(
        render_expert_synthesis(
            mode=mode,
            title=title,
            question=question,
            included=included,
            secondary=secondary,
            coverage=coverage,
        )
    )
    lines.extend([""])
    lines.extend(render_included_table(included, "Expert-Included Evidence", "No evidence passed the expert inclusion screen."))
    lines.extend([""])
    lines.extend(render_included_table(additional[:12], "Additional High-Scoring Evidence Not Used in the Main Narrative", "No extra high-scoring evidence remained after the main narrative limit."))
    long_tail_included = [item for item in included if item.get("IsLongTailEvidence")]
    lines.extend([""])
    lines.extend(render_included_table(long_tail_included, "Long-Tail Candidates Worth Expert Attention", "No included evidence was flagged as long-tail."))
    lines.extend(
        [
            "",
            "## Limitations and Common-Sense Boundaries",
            "",
            "- This expert layer scores evidence for case-study usefulness; it is not a human gold relevance label.",
            "- Additional high-scoring evidence was not rejected; it was held back to keep the main argument concise and auditable.",
            "- AD-Alterome sentence evidence supports traceable arguments, not final causal proof.",
            "- When coverage warnings are present, use the report to generate hypotheses and prioritize manual review.",
            "- Raw API scoring fields such as EvidenceScore are not used for expert conclusions.",
            "",
            "## Audit Appendix: Original Sentence Traces",
            "",
        ]
    )
    lines.extend(render_trace_list(included, "Included Evidence Traces"))
    lines.extend([""])
    lines.extend(render_trace_list(additional[:8], "Additional High-Scoring Evidence Traces"))
    lines.extend([""])
    lines.extend(render_trace_list(secondary[:12], "Secondary Evidence Traces"))
    lines.extend([""])
    lines.extend(render_included_table(deprioritized[:12], "Deprioritized Evidence Summary", "No evidence rows were deprioritized by the expert screen."))
    lines.extend(
        [
            "",
            "## Source Payloads",
            "",
        ]
    )
    for dataset in datasets:
        lines.append(f"- `{md(dataset.get('label'))}` overview: {dataset.get('overview_url')}")
        lines.append(f"- `{md(dataset.get('label'))}` curation/evidence: {dataset.get('evidence_url')}")
    return "\n".join(lines)


def build_strategy(mode: str, candidate_limit: int, expert_limit: int) -> list[str]:
    base = [
        "Use AD-Alterome full-pool curation first; fall back to capped event samples only when the curation endpoint is unavailable.",
        f"Fetch up to {candidate_limit} candidate evidence rows, then keep up to {expert_limit} expert-included rows for the main narrative.",
        "Score evidence by AD specificity, mechanism depth, long-tail insight, user-question fit, traceability, and sentence informativeness.",
        "Apply an AD pathologist-style biological cut: keep molecular/pathological evidence in the main argument and demote generic background evidence.",
    ]
    if mode == "compare":
        base.append("Enforce target balance before writing contrastive claims; imbalanced coverage downgrades the report to exploratory comparison.")
    return base


def main() -> int:
    parser = argparse.ArgumentParser(description="Build AD-Alterome expert case-study report.")
    parser.add_argument("--gene")
    parser.add_argument("--term")
    parser.add_argument("--hypothesis")
    parser.add_argument("--gene-a")
    parser.add_argument("--gene-b")
    parser.add_argument("--question", default="")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--candidate-limit", type=int, default=80, help="Candidate rows requested from the server-side curation package. API max is enforced server-side.")
    parser.add_argument("--expert-limit", type=int, default=18, help="Rows kept in the main expert narrative.")
    parser.add_argument("--curation-limit", type=int, default=API_MAX_TOP_K, help="Fallback rows requested from capped event endpoints if full-pool curation is unavailable.")
    parser.add_argument("--timeout", type=float, default=240)
    args = parser.parse_args()

    mode = infer_mode(args)
    question = default_question(args, mode)
    output_dir = Path(args.output_dir)
    data_dir = output_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    if mode == "compare":
        title = f"{args.gene_a} vs {args.gene_b}"
        compare_url, compare_payload = get_json(
            args.base_url,
            "/compare/genes",
            {"gene_a": args.gene_a, "gene_b": args.gene_b},
            args.timeout,
        )
        datasets = [
            fetch_target(
                kind="compare_gene",
                label=str(args.gene_a).strip().upper(),
                base_url=args.base_url,
                timeout=args.timeout,
                candidate_limit=args.candidate_limit,
                curation_limit=args.curation_limit,
            ),
            fetch_target(
                kind="compare_gene",
                label=str(args.gene_b).strip().upper(),
                base_url=args.base_url,
                timeout=args.timeout,
                candidate_limit=args.candidate_limit,
                curation_limit=args.curation_limit,
            ),
        ]
        write_json(data_dir / "compare.json", compare_payload)
        (data_dir / "compare_url.txt").write_text(compare_url, encoding="utf-8")
    elif mode == "gene":
        title = str(args.gene).strip().upper()
        datasets = [
            fetch_target(
                kind="gene",
                label=title,
                base_url=args.base_url,
                timeout=args.timeout,
                candidate_limit=args.candidate_limit,
                curation_limit=args.curation_limit,
            )
        ]
    elif mode == "term":
        title = str(args.term).strip()
        datasets = [
            fetch_target(
                kind="term",
                label=title,
                base_url=args.base_url,
                timeout=args.timeout,
                candidate_limit=args.candidate_limit,
                curation_limit=args.curation_limit,
            )
        ]
    else:
        title = str(args.hypothesis).strip()
        datasets = [
            fetch_target(
                kind="hypothesis",
                label=title,
                base_url=args.base_url,
                timeout=args.timeout,
                candidate_limit=args.candidate_limit,
                curation_limit=args.curation_limit,
            )
        ]

    for dataset in datasets:
        prefix = normalize_identifier(str(dataset.get("label")))
        write_json(data_dir / f"{prefix}_overview.json", dataset.get("overview"))
        write_json(data_dir / f"{prefix}_evidence.json", dataset.get("evidence_payload"))
        write_json(data_dir / f"{prefix}_curation.json", dataset.get("curation"))

    coverage_targets = [
        coverage_record(str(dataset.get("label")), dataset.get("curation") or {}, dataset.get("fallback_reason"))
        for dataset in datasets
    ]
    coverage = {"targets": coverage_targets, "balance": balance_status(coverage_targets)}

    candidates = collect_candidate_items(datasets)
    scored = [
        score_evidence(item, target_label=str(item.get("Target") or ""), question=question, mode=mode)
        for item in candidates
    ]
    expert_evidence = select_expert_evidence(scored, mode=mode, expert_limit=args.expert_limit)
    strategy = build_strategy(mode, args.candidate_limit, args.expert_limit)

    case_study = {
        "title": title,
        "mode": mode,
        "scientific_question": question,
        "strategy": strategy,
        "coverage": coverage,
        "dominant_mechanism_strata": [
            {"value": value, "count": count}
            for value, count in mechanism_counts(expert_evidence.get("included_evidence") or []).most_common(8)
        ],
        "top_genes": top_field(expert_evidence.get("included_evidence") or [], "Gene", limit=8),
        "top_terms": top_field(expert_evidence.get("included_evidence") or [], "TermName", limit=8),
    }

    write_json(data_dir / "query.json", vars(args))
    write_json(data_dir / "coverage.json", coverage)
    write_json(data_dir / "expert_evidence.json", expert_evidence)
    write_json(data_dir / "case_study.json", case_study)

    report = render_report(
        mode=mode,
        title=title,
        question=question,
        strategy=strategy,
        datasets=datasets,
        coverage=coverage,
        expert_evidence=expert_evidence,
    )
    (output_dir / "case_study_report.md").write_text(report, encoding="utf-8")
    print(output_dir / "case_study_report.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
