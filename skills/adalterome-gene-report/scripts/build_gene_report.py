#!/usr/bin/env python3
"""Build a deterministic AD-Alterome deep gene report draft."""

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
    fetch_gene_curation,
    fetch_gene_events_for_curation,
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
    lines.extend(["| Candidate mechanism stratum | Selected evidence rows | Representative PMIDs |", "| --- | --- | --- |"])
    for name, items in strata.items():
        pmids = []
        for item in items:
            value = item.get("PMID")
            if value and value not in pmids:
                pmids.append(value)
        lines.append(f"| {md(name)} | {len(items)} | {md(', '.join(pmids[:5]) or '-')} |")
    lines.extend(
        [
            "",
            "These strata are a curation aid for expert review. They should be refined by the LLM or user against the original sentences rather than treated as hard ontology labels.",
        ]
    )
    return lines


def render_report(
    gene: str,
    base_url: str,
    overview_url: str,
    events_url: str,
    overview: dict[str, Any],
    curation: dict[str, Any],
) -> str:
    summary = (overview.get("data") or {}).get("summary") or {}
    top_terms = (overview.get("data") or {}).get("top_terms") or []
    top_hypotheses = (overview.get("data") or {}).get("top_hypotheses") or []
    lines = [
        f"# AD-Alterome Deep Gene Report: {gene}",
        "",
        "## Query Scope and Data Provenance",
        "",
        f"- Target gene: `{gene}`",
        f"- API base URL: `{base_url.rstrip('/')}`",
        f"- Gene overview request: {overview_url}",
        f"- Curation evidence source: {events_url}",
        f"- Curation package: `data/curation.json`",
        "",
        "## Global Evidence Landscape",
        "",
        f"AD-Alterome contains {summary.get('event_count', 'unknown')} event records for `{gene}` across {summary.get('pmid_count', 'unknown')} PMID(s), {summary.get('term_count', 'unknown')} term(s), and {summary.get('hypothesis_count', 'unknown')} AD hypothesis field(s). Interpret this as curated sentence-level literature evidence rather than direct causal proof.",
        "",
        "### Top overview terms",
        "",
    ]
    if top_terms:
        for item in top_terms[:10]:
            lines.append(f"- {item.get('TermName')} ({item.get('TermType')}): {item.get('freq')}")
    else:
        lines.append("- None returned.")
    lines.extend(["", "### Top overview hypotheses", ""])
    if top_hypotheses:
        for item in top_hypotheses[:10]:
            lines.append(f"- {item.get('Hypothesis')}: {item.get('freq')}")
    else:
        lines.append("- None returned.")
    lines.extend([""])
    lines.extend(render_curation_overview(curation))
    lines.extend(render_mechanism_map(curation))
    lines.extend([""])
    lines.extend(render_selected_table(curation, "Representative Molecular and Pathological Evidence"))
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
            "- Use the global statistics to describe coverage and dominant literature patterns.",
            "- Use curated representative evidence, not raw API ranking, to summarize molecular pathology.",
            "- Keep original sentences and PubMed links attached to every mechanistic claim.",
            "- Treat candidate mechanism strata as LLM-assisted organization for expert review, not as final labels.",
            "- Genetic alteration interpretation should rely on `AlterationType`, `AlterationMention`, and `AlterationID`; `TriggerWord` and `RegType` are event relation context, not genetic alteration labels.",
            "",
            "## Follow-Up Analysis Suggestions",
            "",
            "- Use `--selected-limit` to request a larger displayed set from the server-side full-pool curation endpoint.",
            "- `--curation-limit` only affects fallback mode when the server does not expose `/gene/curation`.",
            "- Review `data/curation.json` to filter by `EvidenceType`, `MechanismStrata`, `IsLongTailEvidence`, year, PMID, phenotype, gene-alteration pair, or alteration taxonomy.",
            "- Add external enrichment from official sources only as a separate section.",
        ]
    )
    return "\n".join(lines)


def resolve_curation_limit(args: argparse.Namespace) -> int:
    if args.top_k is not None:
        return args.top_k
    return args.curation_limit


def main() -> int:
    parser = argparse.ArgumentParser(description="Build AD-Alterome deep gene report draft.")
    parser.add_argument("--gene", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--curation-limit", type=int, default=API_MAX_TOP_K, help=f"Fallback rows to request from the capped API event endpoint if /gene/curation is unavailable. 0 or values above {API_MAX_TOP_K} use {API_MAX_TOP_K}.")
    parser.add_argument("--top-k", type=int, default=None, help="Deprecated alias for --curation-limit. Prefer --selected-limit for display size.")
    parser.add_argument("--selected-limit", type=int, default=30)
    parser.add_argument("--timeout", type=float, default=180)
    args = parser.parse_args()
    output_dir = Path(args.output_dir)
    data_dir = output_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    overview_url, overview = get_json(args.base_url, "/gene/overview", {"gene": args.gene}, args.timeout)
    curation_limit = resolve_curation_limit(args)
    events_url, server_curation = fetch_gene_curation(
        args.base_url,
        args.gene,
        args.timeout,
        selected_limit=args.selected_limit,
    )
    if server_curation:
        events = server_curation
        curation = curation_package_from_response(server_curation) or {}
    else:
        events_url, events = fetch_gene_events_for_curation(
            args.base_url,
            args.gene,
            args.timeout,
            curation_limit=curation_limit,
        )
        curation = build_curation_package(events, overview=overview, selected_limit=args.selected_limit, query_type="gene")
    (data_dir / "query.json").write_text(
        json.dumps(vars(args), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (data_dir / "overview.json").write_text(json.dumps(overview, ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "evidence.json").write_text(json.dumps(events, ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "curation.json").write_text(json.dumps(curation, ensure_ascii=False, indent=2), encoding="utf-8")
    report = render_report(args.gene, args.base_url, overview_url, events_url, overview, curation)
    (output_dir / "report.md").write_text(report, encoding="utf-8")
    print(output_dir / "report.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
