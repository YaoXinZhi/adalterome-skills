#!/usr/bin/env python3
"""Build a deterministic AD-Alterome two-gene comparison report."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any


SKILLS_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(SKILLS_DIR / "adalterome-api" / "scripts"))

from evidence_curation import (  # noqa: E402
    build_curation_package,
    md,
    render_chronology,
    render_curation_overview,
    render_evidence_traces,
    render_long_tail,
    render_selected_table,
)
from evidence_fetch import (  # noqa: E402
    API_MAX_TOP_K,
    curation_package_from_response,
    fetch_gene_curation,
    fetch_gene_events_for_curation,
    request_json,
)
from query_cache import write_cache_manifest  # noqa: E402


DEFAULT_BASE_URL = os.environ.get("ADALTEROME_API_BASE_URL", "http://117.72.176.137/api/adalterome")


def get_json(base_url: str, path: str, params: dict[str, Any], timeout: float) -> tuple[str, dict[str, Any]]:
    return request_json(base_url, path, params, timeout)


def bullet_items(items: list[dict[str, Any]], name_key: str = "TermName") -> list[str]:
    if not items:
        return ["- None returned."]
    output = []
    for item in items:
        label = item.get(name_key) or item.get("Hypothesis") or "-"
        if "freq_a" in item:
            output.append(f"- {label}: gene A={item.get('freq_a')}, gene B={item.get('freq_b')}")
        else:
            output.append(f"- {label}: {item.get('freq')}")
    return output


def render_mechanism_map(title: str, curation: dict[str, Any]) -> list[str]:
    lines = [f"## {title}", ""]
    strata = curation.get("mechanism_strata") or {}
    if not strata:
        lines.append("No mechanism strata were inferred from the selected evidence.")
        return lines
    lines.extend(["| Candidate mechanism stratum | Selected evidence rows | Representative PMIDs |", "| --- | --- | --- |"])
    for name, items in strata.items():
        pmids = []
        for item in items:
            value = item.get("PMID")
            if value and value not in pmids:
                pmids.append(value)
        lines.append(f"| {md(name)} | {len(items)} | {md(', '.join(pmids[:5]) or '-')} |")
    return lines


def render(
    gene_a: str,
    gene_b: str,
    base_url: str,
    compare_url: str,
    gene_a_url: str,
    gene_b_url: str,
    compare: dict[str, Any],
    curation_a: dict[str, Any],
    curation_b: dict[str, Any],
) -> str:
    data = compare.get("data") or {}
    overview_a = data.get("gene_a_overview") or {}
    overview_b = data.get("gene_b_overview") or {}
    lines = [
        f"# AD-Alterome Gene Comparison: {gene_a} vs {gene_b}",
        "",
        "## Query Scope and Data Provenance",
        "",
        f"- Gene A: `{gene_a}`",
        f"- Gene B: `{gene_b}`",
        f"- API base URL: `{base_url.rstrip('/')}`",
        f"- Compare request: {compare_url}",
        f"- Gene A curation evidence source: {gene_a_url}",
        f"- Gene B curation evidence source: {gene_b_url}",
        f"- Gene A curation package: `data/gene_a_curation.json`",
        f"- Gene B curation package: `data/gene_b_curation.json`",
        f"- Raw API cache manifest: `data/cache_manifest.json`",
        "",
        "## Side-by-Side Global Evidence Landscape",
        "",
        "| Metric | Gene A | Gene B |",
        "| --- | --- | --- |",
    ]
    for key in ["event_count", "pmid_count", "term_count", "hypothesis_count"]:
        lines.append(f"| {key} | {md(overview_a.get(key))} | {md(overview_b.get(key))} |")
    lines.extend(["", "## Shared Phenotype/Process Features and Hypotheses", "", "### Shared phenotype/process features"])
    lines.extend(bullet_items(data.get("shared_terms") or [], "TermName"))
    lines.extend(["", "### Shared hypotheses"])
    lines.extend(bullet_items(data.get("shared_hypotheses") or [], "Hypothesis"))
    lines.extend(["", f"## {gene_a}-Specific Patterns", "", "### Unique phenotype/process features"])
    lines.extend(bullet_items(data.get("unique_terms_a") or [], "TermName"))
    lines.extend(["", "### Unique hypotheses"])
    lines.extend(bullet_items(data.get("unique_hypotheses_a") or [], "Hypothesis"))
    lines.extend(["", f"## {gene_b}-Specific Patterns", "", "### Unique phenotype/process features"])
    lines.extend(bullet_items(data.get("unique_terms_b") or [], "TermName"))
    lines.extend(["", "### Unique hypotheses"])
    lines.extend(bullet_items(data.get("unique_hypotheses_b") or [], "Hypothesis"))
    lines.extend([""])
    lines.extend(render_curation_overview(curation_a))
    lines.extend(render_mechanism_map(f"Mechanism-Stratified Evidence Map for {gene_a}", curation_a))
    lines.extend([""])
    lines.extend(render_selected_table(curation_a, f"Representative Evidence for {gene_a}"))
    lines.extend([""])
    lines.extend(render_long_tail(curation_a))
    lines.extend([""])
    lines.extend(render_chronology(curation_a))
    lines.extend([""])
    lines.extend(render_evidence_traces(curation_a, f"Original Evidence Traces for {gene_a}"))
    lines.extend([""])
    lines.extend(render_curation_overview(curation_b))
    lines.extend(render_mechanism_map(f"Mechanism-Stratified Evidence Map for {gene_b}", curation_b))
    lines.extend([""])
    lines.extend(render_selected_table(curation_b, f"Representative Evidence for {gene_b}"))
    lines.extend([""])
    lines.extend(render_long_tail(curation_b))
    lines.extend([""])
    lines.extend(render_chronology(curation_b))
    lines.extend([""])
    lines.extend(render_evidence_traces(curation_b, f"Original Evidence Traces for {gene_b}"))
    lines.extend(
        [
            "",
            "## Comparative Interpretation Guide",
            "",
            "- Use overview counts to describe database representation, not biological importance.",
            "- Use curated representative evidence to compare mechanisms; avoid relying on raw API ranking.",
            "- Compare shared phenotype/process features and hypotheses against original sentences from both genes.",
            "- Treat candidate mechanism strata as LLM-assisted organization for expert review.",
        ]
    )
    lines.extend(
        [
            "",
            "## Follow-Up Priorities",
            "",
            "- Use `--selected-limit` to request a larger displayed set from each server-side full-pool gene curation endpoint.",
            "- `--curation-limit` only affects fallback mode when the server does not expose `/gene/curation`.",
            "- Review `data/gene_a_curation.json` and `data/gene_b_curation.json` to filter by `EvidenceType`, `MechanismStrata`, `IsLongTailEvidence`, year, phenotype, gene-alteration pair, or alteration taxonomy.",
            "- Treat unequal event counts as a literature-density signal before making contrastive biological claims.",
        ]
    )
    return "\n".join(lines)


def resolve_curation_limit(args: argparse.Namespace) -> int:
    if args.top_k is not None:
        return args.top_k
    return args.curation_limit


def main() -> int:
    parser = argparse.ArgumentParser(description="Build AD-Alterome two-gene comparison report.")
    parser.add_argument("--gene-a", required=True)
    parser.add_argument("--gene-b", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--curation-limit", type=int, default=API_MAX_TOP_K, help=f"Fallback rows to request from each capped API gene event endpoint if /gene/curation is unavailable. 0 or values above {API_MAX_TOP_K} use {API_MAX_TOP_K}.")
    parser.add_argument("--top-k", type=int, default=None, help="Deprecated alias for --curation-limit. Prefer --selected-limit for display size.")
    parser.add_argument("--selected-limit", type=int, default=24)
    parser.add_argument("--timeout", type=float, default=180)
    args = parser.parse_args()
    output_dir = Path(args.output_dir)
    data_dir = output_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    compare_url, compare = get_json(args.base_url, "/compare/genes", {"gene_a": args.gene_a, "gene_b": args.gene_b}, args.timeout)
    curation_limit = resolve_curation_limit(args)
    gene_a_url, server_curation_a = fetch_gene_curation(
        args.base_url,
        args.gene_a,
        args.timeout,
        selected_limit=args.selected_limit,
    )
    if server_curation_a:
        evidence_a = server_curation_a
        curation_a = curation_package_from_response(server_curation_a) or {}
    else:
        gene_a_url, evidence_a = fetch_gene_events_for_curation(
            args.base_url,
            args.gene_a,
            args.timeout,
            curation_limit=curation_limit,
        )
        curation_a = build_curation_package(evidence_a, selected_limit=args.selected_limit, query_type="compare_gene")
    gene_b_url, server_curation_b = fetch_gene_curation(
        args.base_url,
        args.gene_b,
        args.timeout,
        selected_limit=args.selected_limit,
    )
    if server_curation_b:
        evidence_b = server_curation_b
        curation_b = curation_package_from_response(server_curation_b) or {}
    else:
        gene_b_url, evidence_b = fetch_gene_events_for_curation(
            args.base_url,
            args.gene_b,
            args.timeout,
            curation_limit=curation_limit,
        )
        curation_b = build_curation_package(evidence_b, selected_limit=args.selected_limit, query_type="compare_gene")
    (data_dir / "query.json").write_text(json.dumps(vars(args), ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "compare.json").write_text(json.dumps(compare, ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "gene_a_evidence.json").write_text(json.dumps(evidence_a, ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "gene_b_evidence.json").write_text(json.dumps(evidence_b, ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "gene_a_curation.json").write_text(json.dumps(curation_a, ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "gene_b_curation.json").write_text(json.dumps(curation_b, ensure_ascii=False, indent=2), encoding="utf-8")
    write_cache_manifest(
        data_dir / "cache_manifest.json",
        [
            ("gene comparison", compare),
            (f"{args.gene_a} curation/evidence", evidence_a),
            (f"{args.gene_b} curation/evidence", evidence_b),
        ],
    )
    report = render(args.gene_a, args.gene_b, args.base_url, compare_url, gene_a_url, gene_b_url, compare, curation_a, curation_b)
    (output_dir / "report.md").write_text(report, encoding="utf-8")
    print(output_dir / "report.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
