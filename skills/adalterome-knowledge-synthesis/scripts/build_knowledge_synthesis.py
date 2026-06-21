#!/usr/bin/env python3
"""Build AD-Alterome knowledge synthesis packets for expert evaluation."""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any


SKILLS_DIR = Path(__file__).resolve().parents[2]
CASE_STUDY_SCRIPT_DIR = SKILLS_DIR / "adalterome-case-study-expert" / "scripts"
API_SCRIPT_DIR = SKILLS_DIR / "adalterome-api" / "scripts"
sys.path.insert(0, str(CASE_STUDY_SCRIPT_DIR))
sys.path.insert(0, str(API_SCRIPT_DIR))

import build_case_study_expert as legacy  # noqa: E402
from evidence_fetch import API_MAX_TOP_K, SERVER_CURATION_MAX_SELECTED_LIMIT, api_selected_limit  # noqa: E402
from evidence_curation import hypothesis_values, md  # noqa: E402
from query_cache import write_cache_manifest  # noqa: E402


DEFAULT_BASE_URL = os.environ.get("ADALTEROME_API_BASE_URL", "http://117.72.176.137/api/adalterome")
DEFAULT_KNOWLEDGE_CANDIDATE_LIMIT = SERVER_CURATION_MAX_SELECTED_LIMIT
MIN_KNOWLEDGE_CANDIDATE_LIMIT = 20

PATTERNS = {
    "auto",
    "single_gene",
    "multi_gene",
    "gene_set",
    "recommendation",
    "phenotype_process",
    "hypothesis",
    "hypothesis_network",
    "compound",
}

REVIEW_DIMENSIONS = [
    {
        "field": "TraceabilityScore_1_5",
        "label": "Traceability",
        "question": "Are important statements backed by PMID and original sentence evidence?",
    },
    {
        "field": "AccuracyScore_1_5",
        "label": "Accuracy",
        "question": "Are gene, alteration, phenotype/process, and hypothesis attributions correct?",
    },
    {
        "field": "BreadthScore_1_5",
        "label": "Breadth",
        "question": "Does the packet cover the relevant evidence space rather than only dominant high-frequency records?",
    },
    {
        "field": "DepthScore_1_5",
        "label": "Depth",
        "question": "Does the organized evidence include molecular, cellular, pathological, or model-level detail?",
    },
    {
        "field": "OrganizationUsefulness_1_5",
        "label": "Organization usefulness",
        "question": "Do the evidence groups make the complex AD evidence easier to review?",
    },
    {
        "field": "LongTailUsefulness_1_5",
        "label": "Long-tail usefulness",
        "question": "Are low-frequency but potentially informative records surfaced for review?",
    },
    {
        "field": "HallucinationOrOverclaimRisk_1_5",
        "label": "Hallucination or overclaim risk",
        "question": "Score high when hallucination or unsupported overclaim risk is low.",
    },
    {
        "field": "Inspiration_1_5",
        "label": "Inspiration",
        "question": "Does the packet help generate useful review, mechanism, or experiment questions?",
    },
    {
        "field": "ReviewEfficiency_1_5",
        "label": "Review efficiency",
        "question": "Does the packet reduce the time needed to inspect the evidence?",
    },
    {
        "field": "OverallUsefulness_1_5",
        "label": "Overall usefulness",
        "question": "Does the packet meet the user need better than unstructured search or generic LLM output?",
    },
]


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def normalize_output_name(value: str) -> str:
    return legacy.normalize_identifier(value)


def tsv_cell(value: Any) -> str:
    if isinstance(value, list):
        return "; ".join(str(item) for item in value if item not in (None, ""))
    return str(value or "")


def infer_request_mode(args: argparse.Namespace) -> str:
    if args.gene_a and args.gene_b:
        return "compare"
    if args.gene_set:
        return "gene_set"
    axis_count = sum(1 for value in [args.gene, args.term, args.hypothesis] if value)
    if axis_count >= 2:
        return "compound"
    if args.gene:
        return "gene"
    if args.term:
        return "term"
    if args.hypothesis:
        return "hypothesis"
    raise SystemExit("Provide --gene, --term, --hypothesis, --gene-set, or both --gene-a and --gene-b.")


def infer_pattern(args: argparse.Namespace, mode: str) -> str:
    if args.pattern != "auto":
        return args.pattern
    if mode == "compound":
        return "compound"
    if args.axis or (args.gene_set and args.hypothesis):
        return "hypothesis_network"
    if mode == "compare":
        return "multi_gene"
    if mode == "gene_set":
        return "gene_set"
    if mode == "term":
        return "phenotype_process"
    if mode == "hypothesis":
        return "hypothesis"
    lowered = (args.question or "").lower()
    if "phenotype" in lowered or "landscape" in lowered or "recommend" in lowered:
        return "recommendation"
    return "single_gene"


def default_question(args: argparse.Namespace, mode: str, pattern: str) -> str:
    if args.question:
        return args.question
    if pattern == "hypothesis_network" and args.axis:
        return f"Organize AD-Alterome evidence for the {args.axis} as a hypothesis/network review object."
    if mode == "compare":
        return f"Organize AD-Alterome evidence comparing {args.gene_a} and {args.gene_b} for expert review."
    if mode == "gene_set":
        genes = ", ".join(args.gene_set or [])
        return f"Organize AD-Alterome evidence for the gene set {genes} for expert review."
    if mode == "compound":
        axes = []
        if args.gene:
            axes.append(f"gene {args.gene}")
        if args.term:
            axes.append(f"phenotype/process {args.term}")
        if args.hypothesis:
            axes.append(f"hypothesis {args.hypothesis}")
        return "Organize AD-Alterome evidence matching " + ", ".join(axes) + " for expert review."
    if mode == "gene" and pattern == "recommendation":
        return f"Organize the {args.gene} phenotype landscape and long-tail evidence for expert review."
    if mode == "gene":
        return f"Organize AD-Alterome evidence for {args.gene} into a knowledge synthesis packet."
    if mode == "term":
        return f"Organize AD-Alterome evidence for {args.term} as a phenotype/process evidence map."
    return f"Organize AD-Alterome evidence supporting {args.hypothesis} for expert review."


def output_title(args: argparse.Namespace, mode: str, pattern: str) -> str:
    if args.axis:
        return args.axis
    if mode == "compare":
        return f"{args.gene_a} vs {args.gene_b}"
    if mode == "gene_set":
        return "Gene set: " + ", ".join(args.gene_set or [])
    if mode == "compound":
        axes = []
        if args.gene:
            axes.append(str(args.gene).strip().upper())
        if args.term:
            axes.append(str(args.term).strip())
        if args.hypothesis:
            axes.append(str(args.hypothesis).strip())
        return " + ".join(axes)
    if mode == "gene":
        return str(args.gene).strip().upper()
    if mode == "term":
        return str(args.term).strip()
    return str(args.hypothesis).strip()


def pruning_mode(mode: str, pattern: str) -> str:
    if pattern in {"multi_gene", "gene_set", "hypothesis_network"}:
        return "compare"
    if pattern in {"hypothesis", "hypothesis_network"}:
        return "hypothesis"
    if pattern == "compound":
        return "compound"
    if mode == "compare":
        return "compare"
    return mode


def normalize_coverage_language(coverage: dict[str, Any]) -> dict[str, Any]:
    balance = coverage.get("balance") or {}
    balance["notes"] = [
        str(note).replace("case-study synthesis", "knowledge synthesis")
        for note in balance.get("notes") or []
    ]
    coverage["balance"] = balance
    return coverage


def fetch_datasets(args: argparse.Namespace, mode: str, pattern: str) -> tuple[list[dict[str, Any]], dict[str, Any] | None, str | None]:
    datasets: list[dict[str, Any]] = []
    compare_payload: dict[str, Any] | None = None
    compare_url: str | None = None

    if mode == "compare":
        compare_url, compare_payload = legacy.get_json(
            args.base_url,
            "/compare/genes",
            {"gene_a": args.gene_a, "gene_b": args.gene_b},
            args.timeout,
        )
        for gene in [args.gene_a, args.gene_b]:
            datasets.append(
                legacy.fetch_target(
                    kind="compare_gene",
                    label=str(gene).strip().upper(),
                    base_url=args.base_url,
                    timeout=args.timeout,
                    candidate_limit=args.candidate_limit,
                    curation_limit=args.curation_limit,
                )
            )
    elif mode == "gene_set":
        for gene in args.gene_set or []:
            datasets.append(
                legacy.fetch_target(
                    kind="gene",
                    label=str(gene).strip().upper(),
                    base_url=args.base_url,
                    timeout=args.timeout,
                    candidate_limit=args.candidate_limit,
                    curation_limit=args.curation_limit,
                )
            )
        if args.hypothesis:
            datasets.append(
                legacy.fetch_target(
                    kind="hypothesis",
                    label=str(args.hypothesis).strip(),
                    base_url=args.base_url,
                    timeout=args.timeout,
                    candidate_limit=args.candidate_limit,
                    curation_limit=args.curation_limit,
                )
            )
    elif mode == "gene":
        datasets.append(
            legacy.fetch_target(
                kind="gene",
                label=str(args.gene).strip().upper(),
                base_url=args.base_url,
                timeout=args.timeout,
                candidate_limit=args.candidate_limit,
                curation_limit=args.curation_limit,
            )
        )
    elif mode == "compound":
        datasets.append(
            legacy.fetch_target(
                kind="compound",
                label=output_title(args, mode, pattern),
                base_url=args.base_url,
                timeout=args.timeout,
                candidate_limit=args.candidate_limit,
                curation_limit=args.curation_limit,
                gene=str(args.gene).strip().upper() if args.gene else None,
                term=str(args.term).strip() if args.term else None,
                hypothesis=str(args.hypothesis).strip() if args.hypothesis else None,
            )
        )
    elif mode == "term":
        datasets.append(
            legacy.fetch_target(
                kind="term",
                label=str(args.term).strip(),
                base_url=args.base_url,
                timeout=args.timeout,
                candidate_limit=args.candidate_limit,
                curation_limit=args.curation_limit,
            )
        )
    else:
        datasets.append(
            legacy.fetch_target(
                kind="hypothesis",
                label=str(args.hypothesis).strip(),
                base_url=args.base_url,
                timeout=args.timeout,
                candidate_limit=args.candidate_limit,
                curation_limit=args.curation_limit,
            )
        )
    return datasets, compare_payload, compare_url


def count_values(items: list[dict[str, Any]], field: str, limit: int = 10) -> list[dict[str, Any]]:
    counter = Counter(str(item.get(field) or "").strip() for item in items if str(item.get(field) or "").strip())
    return [{"value": value, "count": count} for value, count in counter.most_common(limit)]


def count_hypotheses(items: list[dict[str, Any]], limit: int = 10) -> list[dict[str, Any]]:
    counter: Counter[str] = Counter()
    for item in items:
        for hypothesis in hypothesis_values(item):
            if hypothesis.lower() not in legacy.UNINFORMATIVE_DISPLAY_VALUES:
                counter[hypothesis] += 1
    return [{"value": value, "count": count} for value, count in counter.most_common(limit)]


def top_hypothesis_labels(items: list[dict[str, Any]], limit: int = 6) -> list[str]:
    return [item["value"] for item in count_hypotheses(items, limit=limit)]


def curation_summary(dataset: dict[str, Any]) -> dict[str, Any]:
    curation = dataset.get("curation") or {}
    scope = curation.get("coverage_scope") or {}
    dedupe = curation.get("deduplication_summary") or {}
    selection = curation.get("selection_trace") or {}
    patterns = curation.get("query_relative_patterns") or {}
    global_stats = curation.get("global_statistics") or curation.get("curated_pool_statistics") or {}
    return {
        "label": dataset.get("label"),
        "kind": dataset.get("kind"),
        "curation_scope": scope.get("curation_scope"),
        "curation_source": scope.get("curation_source"),
        "matched_event_count": scope.get("matched_event_count"),
        "curation_pool_rows": dedupe.get("curation_pool_row_count"),
        "event_unique_rows": dedupe.get("event_unique_rows"),
        "unique_pmids": dedupe.get("unique_pmids"),
        "selection_trace": {
            "requested_selected_limit": selection.get("requested_selected_limit", scope.get("requested_selected_limit")),
            "returned_selected_count": selection.get("returned_selected_count", scope.get("returned_selected_count")),
            "representative_count": selection.get("representative_count"),
            "selection_shortfall_reason": selection.get("selection_shortfall_reason") or scope.get("selection_shortfall_reason"),
        },
        "top_patterns": {
            "top_genes": patterns.get("top_genes") or global_stats.get("top_genes"),
            "top_gene_alterations": patterns.get("top_gene_alterations") or global_stats.get("top_gene_alterations"),
            "top_phenotypes": patterns.get("top_phenotypes") or global_stats.get("top_phenotypes"),
            "top_hypotheses": patterns.get("top_hypotheses") or global_stats.get("top_hypotheses"),
            "long_tail_genes": patterns.get("long_tail_genes"),
            "long_tail_gene_alterations": patterns.get("long_tail_gene_alterations"),
            "long_tail_phenotypes": patterns.get("long_tail_phenotypes"),
        },
    }


def render_event_schema() -> list[str]:
    return [
        "## Event Schema Used",
        "",
        "| Layer | Fields | Use in this packet |",
        "| --- | --- | --- |",
        "| Gene | `Gene`, `Entrez` | Anchors the alteration evidence to a genetic entity. |",
        "| Alteration | `AlterationType`, `AlterationMention`, `AlterationID` | Keeps AD-Alterome alteration-centered rather than only gene-centered. |",
        "| Event relation | `TriggerWord`, `RegType`, `Event` | Records the extracted relation context; not treated as genetic alteration labels. |",
        "| Phenotype/process | `TermName`, `TermID`, `TermType`, ontology fields | Organizes downstream biological processes, clinical phenotypes, and pathology features. |",
        "| AD interpretation | `Hypothesis`, `MechanismProvided`, `HypothesisReason`, `ExtendedExplanation` | Used as curated interpretation fields that require expert review. |",
        "| Provenance | `PMID`, `Journal`, `Year`, `Sentence`, `PubMedURL` | Makes every organized item traceable to source sentences. |",
        "",
        "`EvidenceScore` is intentionally not used or displayed as evidence strength.",
    ]


def render_coverage(coverage: dict[str, Any]) -> list[str]:
    lines = [
        "## Evidence Landscape and Coverage",
        "",
        "| Target | Curation scope | Pool rows | Event-unique rows | Matched events | Unique PMIDs | Coverage warnings |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for record in coverage.get("targets") or []:
        lines.append(
            "| {label} | {scope} | {pool} | {unique} | {matched} | {pmids} | {warnings} |".format(
                label=md(record.get("label")),
                scope=md(record.get("curation_scope")),
                pool=md(record.get("curation_pool_rows")),
                unique=md(record.get("event_unique_rows")),
                matched=md(record.get("matched_event_count")),
                pmids=md(record.get("unique_pmids")),
                warnings=md("; ".join(record.get("warnings") or []) or "-"),
            )
        )
    balance = coverage.get("balance") or {}
    lines.extend(["", f"- Balance status: `{balance.get('status')}`"])
    for note in balance.get("notes") or []:
        lines.append(f"- {note}")
    return lines


def render_organized_groups(items: list[dict[str, Any]]) -> list[str]:
    by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in items:
        by_type[str(item.get("EvidenceType") or "unclear_or_mixed")].append(item)
    lines = ["## Organized Evidence Groups", ""]
    if not items:
        lines.append("No organized evidence passed the current selection screen.")
        return lines
    for evidence_type, rows in sorted(by_type.items(), key=lambda pair: len(pair[1]), reverse=True):
        genes = ", ".join(legacy.unique_preserve([str(row.get("Gene") or "") for row in rows], limit=6)) or "-"
        terms = ", ".join(legacy.unique_preserve([str(row.get("TermName") or "") for row in rows], limit=6)) or "-"
        strata = legacy.mechanism_counts(rows).most_common(4)
        strata_text = ", ".join(f"{value} ({count})" for value, count in strata) or "-"
        lines.extend(
            [
                f"### {md(evidence_type)}",
                "",
                f"- Organized evidence rows: `{len(rows)}`",
                f"- Genes represented: {md(genes)}",
                f"- Phenotype/process features represented: {md(terms)}",
                f"- Mechanism strata: {md(strata_text)}",
                "",
            ]
        )
    return lines


def render_gene_alteration_map(items: list[dict[str, Any]]) -> list[str]:
    lines = [
        "## Gene-Alteration-Phenotype/Hypothesis Map",
        "",
        "| Gene | Alteration taxonomy | Phenotype/process | Hypothesis | Evidence rows | Long-tail rows |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    if not items:
        lines.append("| - | - | - | - | - | - |")
        return lines
    grouped: dict[tuple[str, str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for item in items:
        key = (
            str(item.get("Gene") or "-"),
            str(item.get("AlterationTaxonomy") or item.get("AlterationType") or "-"),
            str(item.get("TermName") or "-"),
            str(item.get("Hypothesis") or "-"),
        )
        grouped[key].append(item)
    for (gene, alteration, term, hypothesis), rows in sorted(grouped.items(), key=lambda pair: len(pair[1]), reverse=True)[:30]:
        long_tail = sum(1 for row in rows if row.get("IsLongTailEvidence"))
        lines.append(
            f"| {md(gene)} | {md(alteration)} | {md(term)} | {md(hypothesis)} | {len(rows)} | {long_tail} |"
        )
    return lines


def render_long_tail(items: list[dict[str, Any]]) -> list[str]:
    long_tail = [item for item in items if item.get("IsLongTailEvidence")]
    lines = [
        "## Long-Tail Evidence Candidates",
        "",
        "| Rank | Target | PMID | Gene | Phenotype/process | Why review it |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    if not long_tail:
        lines.append("| - | - | - | - | - | No selected evidence row was marked as long-tail. |")
        return lines
    for index, item in enumerate(long_tail[:20], start=1):
        pmid = item.get("PMID") or "-"
        url = item.get("PubMedURL") or ""
        pmid_text = f"[{pmid}]({url})" if url else str(pmid)
        lines.append(
            "| {index} | {target} | {pmid} | {gene} | {term} | {reason} |".format(
                index=index,
                target=md(item.get("Target")),
                pmid=pmid_text,
                gene=md(item.get("Gene")),
                term=md(item.get("TermName")),
                reason=md(legacy.evidence_reason_text(item)),
            )
        )
    return lines


def render_ai_synthesis(
    *,
    title: str,
    question: str,
    pattern: str,
    items: list[dict[str, Any]],
    secondary: list[dict[str, Any]],
) -> list[str]:
    lines = [
        "## AI-Organized Synthesis for Expert Review",
        "",
    ]
    if not items:
        lines.append("No high-priority evidence was selected. Treat the packet as a coverage/provenance record and inspect secondary evidence manually.")
        return lines
    strata = legacy.mechanism_counts(items).most_common(5)
    genes = legacy.top_field(items, "Gene", limit=8)
    terms = legacy.top_field(items, "TermName", limit=8)
    hypotheses = top_hypothesis_labels(items, limit=6)
    long_tail_count = sum(1 for item in items if item.get("IsLongTailEvidence"))
    lines.extend(
        [
            f"For `{md(title)}`, the skill organized evidence for the question: `{md(question)}`.",
            "",
            "This section is a review object. It proposes a structure for expert inspection and should not be copied as a final manuscript conclusion.",
            "",
            f"- Analytical pattern: `{pattern}`",
            f"- Dominant mechanism strata among organized evidence: {md(', '.join(f'{value} ({count})' for value, count in strata) or '-')}",
            f"- Frequently represented genes: {md(', '.join(genes) or '-')}",
            f"- Frequently represented phenotype/process features: {md(', '.join(terms) or '-')}",
            f"- Frequently represented hypotheses: {md(', '.join(hypotheses) or '-')}",
            f"- Long-tail rows retained for review: `{long_tail_count}`",
        ]
    )
    if secondary:
        lines.append("- Secondary evidence is retained in `data/ad_expert_pruning.json` and can support caveats, but should not drive strong claims without manual review.")
    return lines


def render_review_instructions() -> list[str]:
    lines = [
        "## Expert Review Worksheet",
        "",
        "Reviewer-facing worksheet: `expert_review_sheet.tsv`.",
        "",
        "Suggested reviewer groups:",
        "",
        "- clinical or translational AD experts",
        "- AD or neurodegeneration researchers",
        "- biomedical graduate students or postdocs",
        "",
        "Recommended scoring dimensions use 1-5 scores, with `cannot_judge` allowed:",
        "",
        "| Dimension | Reviewer question |",
        "| --- | --- |",
    ]
    for item in REVIEW_DIMENSIONS:
        lines.append(f"| {md(item['label'])} | {md(item['question'])} |")
    return lines


def render_traces(items: list[dict[str, Any]], title: str = "Original Evidence Traces") -> list[str]:
    lines = [f"## {title}", ""]
    if not items:
        lines.append("No evidence rows available.")
        return lines
    for index, item in enumerate(items, start=1):
        pmid = item.get("PMID") or "-"
        url = item.get("PubMedURL") or ""
        pmid_text = f"[{pmid}]({url})" if url else str(pmid)
        lines.extend(
            [
                f"### {index}. {md(item.get('Target'))} / PMID {pmid_text}",
                "",
                f"- AI organization score: `{item.get('ExpertScore')}`; decision: `{item.get('ExpertDecision')}`; tier: `{item.get('ExpertTier')}`",
                f"- Gene / alteration / phenotype-process / hypothesis: `{md(item.get('Gene'))}` / `{md(item.get('AlterationTaxonomy') or item.get('AlterationType'))}` / `{md(item.get('TermName'))}` / `{md(item.get('Hypothesis'))}`",
                f"- Evidence type: `{md(item.get('EvidenceType'))}`",
                f"- Mechanism strata: {md('; '.join(item.get('MechanismStrata') or []) or '-')}",
                f"- Organization reasons: {md('; '.join(item.get('ExpertReasons') or []) or '-')}",
                f"- Cautions: {md('; '.join(item.get('ExpertCautions') or []) or '-')}",
                f"- Original sentence: {md(item.get('Sentence'))}",
                "",
            ]
        )
    return lines


def render_limitations() -> list[str]:
    return [
        "## Limitations and Non-Claims",
        "",
        "- This packet organizes AD-Alterome sentence-level evidence; it does not prove an AD mechanism.",
        "- This packet does not replace expert review.",
        "- AI-organized evidence groups are review candidates, not manuscript conclusions.",
        "- Human experts should score traceability, accuracy, depth, breadth, hallucination or overclaim risk, and usefulness before using the packet in a manuscript.",
        "- `EvidenceScore` is not used or displayed as evidence strength.",
        "- `EvidenceQualityScore`, when present in raw payloads, is a sentence-usefulness signal rather than proof strength.",
        "- PubMed-linked sentences support provenance, not direct causal validation.",
        "- Curation scope and coverage warnings should be reported when comparing targets.",
    ]


def render_source_payloads(datasets: list[dict[str, Any]], compare_url: str | None) -> list[str]:
    lines = [
        "## Source Payloads",
        "",
        "- Raw API cache manifest: `data/cache_manifest.json`",
        "- Provenance manifest: `provenance_manifest.json`",
    ]
    if compare_url:
        lines.append(f"- Gene comparison endpoint: {compare_url}")
    for dataset in datasets:
        lines.append(f"- `{md(dataset.get('label'))}` overview: {dataset.get('overview_url')}")
        lines.append(f"- `{md(dataset.get('label'))}` curation/evidence: {dataset.get('evidence_url')}")
    return lines


def render_knowledge_packet(
    *,
    title: str,
    question: str,
    pattern: str,
    datasets: list[dict[str, Any]],
    coverage: dict[str, Any],
    expert_evidence: dict[str, Any],
    compare_url: str | None,
) -> str:
    included = expert_evidence.get("included_evidence") or []
    additional = expert_evidence.get("additional_high_scoring_evidence") or []
    secondary = expert_evidence.get("secondary_evidence") or []
    lines = [
        f"# AD-Alterome Knowledge Synthesis Packet: {title}",
        "",
        "## Query Scope and User Intent",
        "",
        f"- User question: {md(question)}",
        "- Output role: AI-organized evidence structure for expert evaluation.",
        "- Manuscript role: evaluation object for AI-for-biomedical-knowledge-synthesis, not paper-ready biological conclusion.",
        "",
        "## Analytical Pattern",
        "",
        f"- Pattern: `{pattern}`",
        f"- Targets: {md(', '.join(str(dataset.get('label')) for dataset in datasets))}",
        "",
    ]
    lines.extend(render_event_schema())
    lines.extend([""])
    lines.extend(render_coverage(coverage))
    lines.extend([""])
    lines.extend(render_organized_groups(included))
    lines.extend([""])
    lines.extend(render_gene_alteration_map(included))
    lines.extend([""])
    lines.extend(render_long_tail(included + additional[:12]))
    lines.extend([""])
    lines.extend(render_ai_synthesis(title=title, question=question, pattern=pattern, items=included, secondary=secondary))
    lines.extend([""])
    lines.extend(render_review_instructions())
    lines.extend([""])
    lines.extend(render_traces(included, "Original Evidence Traces"))
    lines.extend([""])
    lines.extend(render_limitations())
    lines.extend([""])
    lines.extend(render_source_payloads(datasets, compare_url))
    return "\n".join(lines)


def render_evidence_map(
    *,
    title: str,
    pattern: str,
    datasets: list[dict[str, Any]],
    coverage: dict[str, Any],
    expert_evidence: dict[str, Any],
) -> str:
    included = expert_evidence.get("included_evidence") or []
    all_scored = expert_evidence.get("all_scored_evidence") or []
    lines = [
        f"# AD-Alterome Evidence Map: {title}",
        "",
        f"- Analytical pattern: `{pattern}`",
        f"- Organized evidence rows: `{len(included)}`",
        f"- Scored candidate rows after duplicate merge: `{len(all_scored)}`",
        f"- Long-tail organized rows: `{sum(1 for item in included if item.get('IsLongTailEvidence'))}`",
        "",
    ]
    lines.extend(render_coverage(coverage))
    lines.extend(["", "## Target Curation Summaries", ""])
    for dataset in datasets:
        summary = curation_summary(dataset)
        lines.extend(
            [
                f"### {md(summary.get('label'))}",
                "",
                f"- Curation source/scope: `{summary.get('curation_source')}` / `{summary.get('curation_scope')}`",
                f"- Matched events: `{summary.get('matched_event_count')}`; curation pool rows: `{summary.get('curation_pool_rows')}`; event-unique rows: `{summary.get('event_unique_rows')}`; unique PMIDs: `{summary.get('unique_pmids')}`",
                f"- Selection trace: `{json.dumps(summary.get('selection_trace'), ensure_ascii=False)}`",
                "",
            ]
        )
    lines.extend(render_organized_groups(included))
    lines.extend([""])
    lines.extend(render_gene_alteration_map(included))
    lines.extend([""])
    lines.extend(render_long_tail(included))
    return "\n".join(lines)


def write_review_sheet(path: Path, *, pattern: str, items: list[dict[str, Any]]) -> None:
    columns = [
        "EvidenceID",
        "AnalyticalPattern",
        "Target",
        "PMID",
        "PubMedURL",
        "Gene",
        "AlterationTaxonomy",
        "AlterationMention",
        "PhenotypeProcess",
        "Hypothesis",
        "EvidenceType",
        "MechanismStrata",
        "IsLongTailEvidence",
        "AIOrganizationScore",
        "AIOrganizationDecision",
        "AIOrganizationReasons",
        "OriginalSentence",
    ] + [item["field"] for item in REVIEW_DIMENSIONS] + ["CannotJudge", "ReviewerNotes", "ReviewStatus"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for index, item in enumerate(items, start=1):
            row = {
                "EvidenceID": f"E{index:04d}",
                "AnalyticalPattern": pattern,
                "Target": item.get("Target"),
                "PMID": item.get("PMID"),
                "PubMedURL": item.get("PubMedURL"),
                "Gene": item.get("Gene"),
                "AlterationTaxonomy": item.get("AlterationTaxonomy") or item.get("AlterationType"),
                "AlterationMention": item.get("AlterationMention"),
                "PhenotypeProcess": item.get("TermName"),
                "Hypothesis": item.get("Hypothesis"),
                "EvidenceType": item.get("EvidenceType"),
                "MechanismStrata": tsv_cell(item.get("MechanismStrata")),
                "IsLongTailEvidence": item.get("IsLongTailEvidence"),
                "AIOrganizationScore": item.get("ExpertScore"),
                "AIOrganizationDecision": item.get("ExpertDecision"),
                "AIOrganizationReasons": tsv_cell(item.get("ExpertReasons")),
                "OriginalSentence": item.get("Sentence"),
                "CannotJudge": "",
                "ReviewerNotes": "",
                "ReviewStatus": "pending_human_review",
            }
            for dimension in REVIEW_DIMENSIONS:
                row[dimension["field"]] = ""
            writer.writerow({column: tsv_cell(row.get(column)) for column in columns})


def evaluation_record(
    *,
    title: str,
    question: str,
    pattern: str,
    mode: str,
    args: argparse.Namespace,
    coverage: dict[str, Any],
    expert_evidence: dict[str, Any],
) -> dict[str, Any]:
    return {
        "title": title,
        "created_date": date.today().isoformat(),
        "framing": "AI for Biomedical Knowledge Synthesis",
        "output_role": "AI-organized evidence packet for expert evaluation",
        "mode": mode,
        "analytical_pattern": pattern,
        "question": question,
        "candidate_limit_requested": getattr(args, "candidate_limit_requested", args.candidate_limit),
        "candidate_limit_effective": args.candidate_limit,
        "candidate_limit_api_capped": api_selected_limit(args.candidate_limit),
        "organized_limit": args.organized_limit,
        "coverage": coverage,
        "candidate_counts": {
            "premerge_candidate_count": expert_evidence.get("premerge_candidate_count"),
            "postmerge_candidate_count": expert_evidence.get("postmerge_candidate_count"),
            "duplicate_group_count": expert_evidence.get("duplicate_group_count"),
            "included_evidence_count": len(expert_evidence.get("included_evidence") or []),
            "secondary_evidence_count": len(expert_evidence.get("secondary_evidence") or []),
            "deprioritized_evidence_count": len(expert_evidence.get("deprioritized_evidence") or []),
        },
        "reviewer_types": [
            "clinical_or_translational_AD_expert",
            "AD_or_neurodegeneration_researcher",
            "biomedical_graduate_student_or_postdoc",
        ],
        "scoring_dimensions": REVIEW_DIMENSIONS,
        "recommended_baselines": [
            "generic_LLM_without_AD_Alterome",
            "generic_LLM_plus_ordinary_RAG",
            "frequency_top_k_AD_Alterome",
            "AD_Alterome_without_long_tail_rescue",
            "AD_Alterome_knowledge_synthesis_skill",
        ],
        "fairness_controls": [
            "same_natural_language_question",
            "same_model_when_comparing_LLM_conditions",
            "same_output_length_budget",
            "same_time_budget",
            "same_scoring_rubric",
            "blinded_method_labels_when_feasible",
        ],
        "non_claims": [
            "The packet does not prove an AD mechanism.",
            "The packet does not replace expert review.",
            "AI-organized evidence groups are review candidates, not manuscript conclusions.",
            "Sentence-level PubMed evidence is provenance, not causal validation.",
            "Raw EvidenceScore is not used as evidence strength.",
        ],
    }


def provenance_manifest(
    *,
    args: argparse.Namespace,
    title: str,
    mode: str,
    pattern: str,
    question: str,
    datasets: list[dict[str, Any]],
    compare_url: str | None,
) -> dict[str, Any]:
    return {
        "title": title,
        "mode": mode,
        "analytical_pattern": pattern,
        "question": question,
        "base_url": args.base_url,
        "candidate_limit_requested": getattr(args, "candidate_limit_requested", args.candidate_limit),
        "candidate_limit": args.candidate_limit,
        "organized_limit": args.organized_limit,
        "timeout": args.timeout,
        "compare_url": compare_url,
        "source_payloads": [
            {
                "label": dataset.get("label"),
                "kind": dataset.get("kind"),
                "overview_url": dataset.get("overview_url"),
                "evidence_url": dataset.get("evidence_url"),
                "fallback_reason": dataset.get("fallback_reason"),
                "coverage_scope": (dataset.get("curation") or {}).get("coverage_scope"),
            }
            for dataset in datasets
        ],
        "local_files": {
            "knowledge_packet": "knowledge_packet.md",
            "evidence_map": "evidence_map.md",
            "expert_review_sheet": "expert_review_sheet.tsv",
            "evaluation_record": "evaluation_record.json",
            "cache_manifest": "data/cache_manifest.json",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build AD-Alterome knowledge synthesis packet.")
    parser.add_argument("--gene")
    parser.add_argument("--term")
    parser.add_argument("--hypothesis")
    parser.add_argument("--gene-a")
    parser.add_argument("--gene-b")
    parser.add_argument("--gene-set", nargs="+")
    parser.add_argument("--axis")
    parser.add_argument("--pattern", choices=sorted(PATTERNS), default="auto")
    parser.add_argument("--question", default="")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument(
        "--candidate-limit",
        type=int,
        default=DEFAULT_KNOWLEDGE_CANDIDATE_LIMIT,
        help="Candidate rows requested from server-side curation before evidence organization; defaults to the API maximum, and values below 20 are raised to 20 for usable coverage.",
    )
    parser.add_argument("--organized-limit", type=int, default=18, help="Rows kept in the main organized packet.")
    parser.add_argument("--expert-limit", type=int, default=None, help="Deprecated alias for --organized-limit.")
    parser.add_argument("--curation-limit", type=int, default=API_MAX_TOP_K, help="Deprecated no-op retained for compatibility; capped event fallback remains disabled.")
    parser.add_argument("--timeout", type=float, default=240)
    args = parser.parse_args()
    if args.expert_limit is not None:
        args.organized_limit = args.expert_limit
    args.candidate_limit_requested = args.candidate_limit
    if args.candidate_limit < MIN_KNOWLEDGE_CANDIDATE_LIMIT:
        print(
            f"Adjusted --candidate-limit from {args.candidate_limit} to {MIN_KNOWLEDGE_CANDIDATE_LIMIT} for usable knowledge-synthesis coverage.",
            file=sys.stderr,
        )
        args.candidate_limit = MIN_KNOWLEDGE_CANDIDATE_LIMIT

    mode = infer_request_mode(args)
    pattern = infer_pattern(args, mode)
    question = default_question(args, mode, pattern)
    title = output_title(args, mode, pattern)

    output_dir = Path(args.output_dir)
    data_dir = output_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    datasets, compare_payload, compare_url = fetch_datasets(args, mode, pattern)
    for dataset in datasets:
        prefix = normalize_output_name(str(dataset.get("label")))
        write_json(data_dir / f"{prefix}_overview.json", dataset.get("overview"))
        write_json(data_dir / f"{prefix}_evidence.json", dataset.get("evidence_payload"))
        write_json(data_dir / f"{prefix}_curation.json", dataset.get("curation"))

    if compare_payload:
        write_json(data_dir / "compare.json", compare_payload)
        if compare_url:
            (data_dir / "compare_url.txt").write_text(compare_url, encoding="utf-8")

    coverage_targets = [
        legacy.coverage_record(str(dataset.get("label")), dataset.get("curation") or {}, dataset.get("fallback_reason"))
        for dataset in datasets
    ]
    coverage = normalize_coverage_language({"targets": coverage_targets, "balance": legacy.balance_status(coverage_targets)})

    candidates = legacy.collect_candidate_items(datasets)
    expert_evidence = legacy.expert_pruning.run_ad_expert_pruning(
        candidates,
        mode=pruning_mode(mode, pattern),
        question=question,
        expert_limit=args.organized_limit,
    )

    included = expert_evidence.get("included_evidence") or []
    knowledge_synthesis = {
        "title": title,
        "mode": mode,
        "analytical_pattern": pattern,
        "question": question,
        "coverage": coverage,
        "target_summaries": [curation_summary(dataset) for dataset in datasets],
        "dominant_mechanism_strata": [
            {"value": value, "count": count}
            for value, count in legacy.mechanism_counts(included).most_common(10)
        ],
        "top_genes": count_values(included, "Gene", limit=10),
        "top_phenotype_processes": count_values(included, "TermName", limit=10),
        "top_hypotheses": count_hypotheses(included, limit=10),
        "long_tail_organized_count": sum(1 for item in included if item.get("IsLongTailEvidence")),
        "non_claims": evaluation_record(
            title=title,
            question=question,
            pattern=pattern,
            mode=mode,
            args=args,
            coverage=coverage,
            expert_evidence=expert_evidence,
        )["non_claims"],
    }

    write_json(data_dir / "query.json", vars(args))
    write_json(data_dir / "coverage.json", coverage)
    write_json(data_dir / "knowledge_synthesis.json", knowledge_synthesis)
    write_json(data_dir / "ad_expert_pruning.json", expert_evidence)
    write_json(data_dir / "merged_evidence.json", expert_evidence.get("merged_evidence") or [])
    write_json(data_dir / "excluded_or_deprioritized_evidence.json", expert_evidence.get("excluded_or_deprioritized_evidence") or [])

    cache_payloads: list[tuple[str, dict[str, Any] | None]] = []
    if compare_payload:
        cache_payloads.append(("gene comparison", compare_payload))
    for dataset in datasets:
        cache_payloads.append((f"{dataset.get('label')} overview", dataset.get("overview")))
        cache_payloads.append((f"{dataset.get('label')} curation/evidence", dataset.get("evidence_payload")))
    write_cache_manifest(data_dir / "cache_manifest.json", cache_payloads)

    eval_record = evaluation_record(
        title=title,
        question=question,
        pattern=pattern,
        mode=mode,
        args=args,
        coverage=coverage,
        expert_evidence=expert_evidence,
    )
    provenance = provenance_manifest(
        args=args,
        title=title,
        mode=mode,
        pattern=pattern,
        question=question,
        datasets=datasets,
        compare_url=compare_url,
    )

    write_json(output_dir / "evaluation_record.json", eval_record)
    write_json(output_dir / "provenance_manifest.json", provenance)
    write_review_sheet(output_dir / "expert_review_sheet.tsv", pattern=pattern, items=included)

    packet = render_knowledge_packet(
        title=title,
        question=question,
        pattern=pattern,
        datasets=datasets,
        coverage=coverage,
        expert_evidence=expert_evidence,
        compare_url=compare_url,
    )
    evidence_map = render_evidence_map(
        title=title,
        pattern=pattern,
        datasets=datasets,
        coverage=coverage,
        expert_evidence=expert_evidence,
    )
    (output_dir / "knowledge_packet.md").write_text(packet, encoding="utf-8")
    (output_dir / "evidence_map.md").write_text(evidence_map, encoding="utf-8")
    print(output_dir / "knowledge_packet.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
