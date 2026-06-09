#!/usr/bin/env python3
"""Build a deterministic AD-Alterome hypothesis support report."""

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
    md,
    render_chronology,
    render_curation_overview,
    render_evidence_traces,
    render_long_tail,
    render_selected_table,
)
from evidence_fetch import (  # noqa: E402
    curation_package_from_response,
    curation_unavailable_response,
    fetch_hypothesis_curation_with_error,
    request_json,
    request_json_optional,
)
from query_cache import write_cache_manifest  # noqa: E402


DEFAULT_BASE_URL = os.environ.get("ADALTEROME_API_BASE_URL", "http://117.72.176.137/api/adalterome")


def get_json(base_url: str, path: str, params: dict[str, Any], timeout: float) -> tuple[str, dict[str, Any]]:
    return request_json(base_url, path, params, timeout)


def get_json_optional(base_url: str, path: str, params: dict[str, Any], timeout: float) -> tuple[str, dict[str, Any], str | None]:
    url, payload, error = request_json_optional(base_url, path, params, timeout)
    if isinstance(payload, dict):
        return url, payload, None
    return (
        url,
        {
            "tool": "optional_overview",
            "status": "partial",
            "query": params,
            "count": 0,
            "data": {},
            "meta": {"overview_failure_reason": error or "overview endpoint returned no payload"},
        },
        error or "overview endpoint returned no payload",
    )


def curation_global_stats(curation: dict[str, Any]) -> dict[str, Any]:
    stats = curation.get("global_statistics") or curation.get("curated_pool_statistics") or {}
    return stats if isinstance(stats, dict) else {}


def curation_global_summary(curation: dict[str, Any]) -> dict[str, Any]:
    summary = curation_global_stats(curation).get("summary")
    return summary if isinstance(summary, dict) else {}


def item_label(item: dict[str, Any], *keys: str) -> str:
    for key in keys:
        value = item.get(key)
        if value:
            return str(value)
    return "-"


def item_count(item: dict[str, Any]) -> Any:
    return item.get("freq", item.get("count", "-"))


def render_mechanism_map(curation: dict[str, Any]) -> list[str]:
    lines = ["## Mechanism-Stratified Evidence Map", ""]
    strata = curation.get("mechanism_strata") or {}
    if not strata:
        lines.append("No mechanism strata were inferred from the selected evidence.")
        return lines
    lines.extend(["| Candidate mechanism stratum | Selected evidence rows | Representative genes |", "| --- | --- | --- |"])
    for name, items in strata.items():
        genes = []
        for item in items:
            value = item.get("Gene")
            if value and value not in genes:
                genes.append(value)
        lines.append(f"| {md(name)} | {len(items)} | {md(', '.join(genes[:8]) or '-')} |")
    lines.extend(
        [
            "",
            "These strata organize support patterns for expert review. Hypothesis labels remain curated AD-Alterome assignments, not proof of causality.",
        ]
    )
    return lines


def render(hypothesis: str, base_url: str, overview_url: str, evidence_url: str, overview: dict[str, Any], curation: dict[str, Any]) -> str:
    overview_data = overview.get("data") or {}
    summary = overview_data.get("summary") or {}
    curated_summary = curation_global_summary(curation)
    curated_stats = curation_global_stats(curation)
    top_genes = overview_data.get("top_genes") or curated_stats.get("top_genes") or []
    top_terms = overview_data.get("top_terms") or curated_stats.get("top_phenotypes") or []
    overview_error = (overview.get("meta") or {}).get("overview_failure_reason")
    event_count = summary.get("event_count", curated_summary.get("raw_event_count", "unknown"))
    lines = [
        f"# AD-Alterome Hypothesis Report: {hypothesis}",
        "",
        "## Query Scope and Data Provenance",
        "",
        f"- Target hypothesis: `{hypothesis}`",
        f"- API base URL: `{base_url.rstrip('/')}`",
        f"- Overview request: {overview_url}",
        f"- Curation evidence source: {evidence_url}",
        f"- Curation package: `data/curation.json`",
        f"- Raw API cache manifest: `data/cache_manifest.json`",
        "",
        "## Global Evidence Landscape",
        "",
        f"AD-Alterome links `{hypothesis}` to {event_count} event records across {summary.get('pmid_count', 'unknown')} PMID(s), {summary.get('gene_count', 'unknown')} gene(s), and {summary.get('term_count', 'unknown')} phenotype/process feature(s). This supports an evidence map for the hypothesis, not proof that the hypothesis is complete or causal.",
        "",
        "### Top genes",
        "",
    ]
    if overview_error:
        lines.extend(
            [
                f"- Overview endpoint unavailable for this run: {overview_error}",
                "- Complete query-pool statistics below come from the curated curation endpoint when available.",
                "",
            ]
        )
    if top_genes:
        for item in top_genes[:10]:
            lines.append(f"- {item_label(item, 'Gene', 'value')}: {item_count(item)}")
    else:
        lines.append("- None returned.")
    lines.extend(["", "### Top phenotype/process features", ""])
    if top_terms:
        for item in top_terms[:10]:
            term_type = item.get("TermType")
            type_text = f" ({term_type})" if term_type else ""
            lines.append(f"- {item_label(item, 'TermName', 'value')}{type_text}: {item_count(item)}")
    else:
        lines.append("- None returned.")
    lines.extend([""])
    lines.extend(render_curation_overview(curation))
    lines.extend(render_mechanism_map(curation))
    lines.extend([""])
    lines.extend(render_selected_table(curation, "Representative Support Evidence"))
    lines.extend([""])
    lines.extend(render_long_tail(curation))
    lines.extend([""])
    lines.extend(render_chronology(curation))
    lines.extend([""])
    lines.extend(render_evidence_traces(curation))
    lines.extend(
        [
            "",
            "## Interpretation Guide for the User Question",
            "",
            "- Separate direct sentence support from AD-Alterome hypothesis assignment fields.",
            "- Use curated representative evidence to discuss support patterns across genes and phenotype/process features.",
            "- Treat candidate mechanism strata as LLM-assisted organization for expert review.",
            "- Avoid claiming that the hypothesis is proven by sentence-level database evidence.",
            "",
            "## Follow-Up Analysis Priorities",
            "",
            "- Use `--selected-limit` to request a larger displayed set from the server-side full-pool curation endpoint.",
            "- `--curation-limit` and `--top-k` are deprecated compatibility options; capped `/hypothesis/support` fallback is disabled for reports.",
            "- Review `data/curation.json` to filter by `EvidenceType`, `MechanismStrata`, `IsLongTailEvidence`, year, gene, phenotype, gene-alteration pair, or alteration taxonomy.",
            "- Compare support against adjacent hypotheses when hypothesis combinations dominate returned evidence.",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build AD-Alterome hypothesis support report.")
    parser.add_argument("--hypothesis", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--curation-limit", type=int, default=50, help="Deprecated no-op retained for old commands; capped event-endpoint fallback is disabled.")
    parser.add_argument("--top-k", type=int, default=None, help="Deprecated no-op retained for old commands. Prefer --selected-limit for display size.")
    parser.add_argument("--selected-limit", type=int, default=30)
    parser.add_argument("--timeout", type=float, default=180)
    args = parser.parse_args()
    output_dir = Path(args.output_dir)
    data_dir = output_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    evidence_url, server_curation, curation_error = fetch_hypothesis_curation_with_error(
        args.base_url,
        args.hypothesis,
        args.timeout,
        selected_limit=args.selected_limit,
    )
    if server_curation:
        evidence = server_curation
        curation = curation_package_from_response(server_curation) or {}
    else:
        evidence = curation_unavailable_response(
            tool="query_hypothesis_curation",
            query={"hypothesis": args.hypothesis, "selected_limit": args.selected_limit},
            query_type="hypothesis",
            request_url=evidence_url,
            reason=curation_error,
        )
        curation = curation_package_from_response(evidence) or {}
    overview_url, overview, overview_error = get_json_optional(args.base_url, "/hypothesis/overview", {"hypothesis": args.hypothesis}, args.timeout)
    if overview_error and curation:
        scope = curation.setdefault("coverage_scope", {})
        scope["overview_failure_reason"] = overview_error
    if curation.get("coverage_scope", {}).get("curation_source") == "unavailable":
        evidence = curation_unavailable_response(
            tool="query_hypothesis_curation",
            query={"hypothesis": args.hypothesis, "selected_limit": args.selected_limit},
            query_type="hypothesis",
            request_url=evidence_url,
            reason=curation_error,
            overview=overview,
        )
        curation = curation_package_from_response(evidence) or {}
    (data_dir / "query.json").write_text(json.dumps(vars(args), ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "overview.json").write_text(json.dumps(overview, ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "evidence.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "curation.json").write_text(json.dumps(curation, ensure_ascii=False, indent=2), encoding="utf-8")
    write_cache_manifest(data_dir / "cache_manifest.json", [("hypothesis overview", overview), ("curation/evidence", evidence)])
    (output_dir / "report.md").write_text(render(args.hypothesis, args.base_url, overview_url, evidence_url, overview, curation), encoding="utf-8")
    print(output_dir / "report.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
