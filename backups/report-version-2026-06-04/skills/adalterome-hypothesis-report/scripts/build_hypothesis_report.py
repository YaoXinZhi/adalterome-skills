#!/usr/bin/env python3
"""Build a deterministic AD-Alterome hypothesis support report."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


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
    fetch_hypothesis_curation,
    fetch_hypothesis_support_for_curation,
)


DEFAULT_BASE_URL = os.environ.get("ADALTEROME_API_BASE_URL", "http://117.72.176.137/api/adalterome")


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
    summary = (overview.get("data") or {}).get("summary") or {}
    top_genes = (overview.get("data") or {}).get("top_genes") or []
    top_terms = (overview.get("data") or {}).get("top_terms") or []
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
        "",
        "## Global Evidence Landscape",
        "",
        f"AD-Alterome links `{hypothesis}` to {summary.get('event_count', 'unknown')} event records across {summary.get('pmid_count', 'unknown')} PMID(s), {summary.get('gene_count', 'unknown')} gene(s), and {summary.get('term_count', 'unknown')} term(s). This supports an evidence map for the hypothesis, not proof that the hypothesis is complete or causal.",
        "",
        "### Top genes",
        "",
    ]
    if top_genes:
        for item in top_genes[:10]:
            lines.append(f"- {item.get('Gene')}: {item.get('freq')}")
    else:
        lines.append("- None returned.")
    lines.extend(["", "### Top terms", ""])
    if top_terms:
        for item in top_terms[:10]:
            lines.append(f"- {item.get('TermName')} ({item.get('TermType')}): {item.get('freq')}")
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
            "- Use curated representative evidence to discuss support patterns across genes and terms.",
            "- Treat candidate mechanism strata as LLM-assisted organization for expert review.",
            "- Avoid claiming that the hypothesis is proven by sentence-level database evidence.",
            "",
            "## Follow-Up Analysis Priorities",
            "",
            "- Use `--selected-limit` to request a larger displayed set from the server-side full-pool curation endpoint.",
            "- `--curation-limit` only affects fallback mode when the server does not expose `/hypothesis/curation`.",
            "- Review `data/curation.json` to filter by `EvidenceType`, `MechanismStrata`, `IsLongTailEvidence`, year, gene, phenotype, gene-alteration pair, or alteration taxonomy.",
            "- Compare support against adjacent hypotheses when hypothesis combinations dominate returned evidence.",
        ]
    )
    return "\n".join(lines)


def resolve_curation_limit(args: argparse.Namespace) -> int:
    if args.top_k is not None:
        return args.top_k
    return args.curation_limit


def main() -> int:
    parser = argparse.ArgumentParser(description="Build AD-Alterome hypothesis support report.")
    parser.add_argument("--hypothesis", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--curation-limit", type=int, default=API_MAX_TOP_K, help=f"Fallback rows to request from the capped API event endpoint if /hypothesis/curation is unavailable. 0 or values above {API_MAX_TOP_K} use {API_MAX_TOP_K}.")
    parser.add_argument("--top-k", type=int, default=None, help="Deprecated alias for --curation-limit. Prefer --selected-limit for display size.")
    parser.add_argument("--selected-limit", type=int, default=30)
    parser.add_argument("--timeout", type=float, default=180)
    args = parser.parse_args()
    output_dir = Path(args.output_dir)
    data_dir = output_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    overview_url, overview = get_json(args.base_url, "/hypothesis/overview", {"hypothesis": args.hypothesis}, args.timeout)
    curation_limit = resolve_curation_limit(args)
    evidence_url, server_curation = fetch_hypothesis_curation(
        args.base_url,
        args.hypothesis,
        args.timeout,
        selected_limit=args.selected_limit,
    )
    if server_curation:
        evidence = server_curation
        curation = curation_package_from_response(server_curation) or {}
    else:
        evidence_url, evidence = fetch_hypothesis_support_for_curation(
            args.base_url,
            args.hypothesis,
            args.timeout,
            curation_limit=curation_limit,
        )
        curation = build_curation_package(evidence, overview=overview, selected_limit=args.selected_limit, query_type="hypothesis")
    (data_dir / "query.json").write_text(json.dumps(vars(args), ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "overview.json").write_text(json.dumps(overview, ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "evidence.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "curation.json").write_text(json.dumps(curation, ensure_ascii=False, indent=2), encoding="utf-8")
    (output_dir / "report.md").write_text(render(args.hypothesis, args.base_url, overview_url, evidence_url, overview, curation), encoding="utf-8")
    print(output_dir / "report.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
