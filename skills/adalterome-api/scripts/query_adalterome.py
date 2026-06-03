#!/usr/bin/env python3
"""Query AD-Alterome REST API and print stable evidence outputs."""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from evidence_curation import (
    md,
    render_chronology,
    render_curation_overview,
    render_long_tail,
    render_selected_table,
)


DEFAULT_BASE_URL = os.environ.get("ADALTEROME_API_BASE_URL", "http://117.72.176.137/api/adalterome")


def request_json(base_url: str, path: str, params: dict[str, Any], timeout: float) -> tuple[str, dict[str, Any]]:
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


def endpoint_for_args(args: argparse.Namespace) -> tuple[str, dict[str, Any]]:
    command = args.command
    if command == "schema":
        return "/schema", {}
    if command == "hypotheses":
        return "/hypotheses", {}
    if command == "gene-events":
        return "/gene/events", {"gene": args.gene, "top_k": args.top_k}
    if command == "gene-overview":
        return "/gene/overview", {"gene": args.gene}
    if command == "gene-curation":
        return "/gene/curation", {"gene": args.gene, "selected_limit": args.selected_limit}
    if command == "term-events":
        return "/term/events", {"term": args.term, "top_k": args.top_k}
    if command == "term-overview":
        return "/term/overview", {"term": args.term}
    if command == "term-curation":
        return "/term/curation", {"term": args.term, "selected_limit": args.selected_limit}
    if command == "hypothesis-support":
        return "/hypothesis/support", {"hypothesis": args.hypothesis, "top_k": args.top_k}
    if command == "hypothesis-overview":
        return "/hypothesis/overview", {"hypothesis": args.hypothesis}
    if command == "hypothesis-curation":
        return "/hypothesis/curation", {"hypothesis": args.hypothesis, "selected_limit": args.selected_limit}
    if command == "compare":
        return "/compare/genes", {"gene_a": args.gene_a, "gene_b": args.gene_b}
    raise SystemExit(f"Unsupported command: {command}")


def results(payload: dict[str, Any]) -> list[dict[str, Any]]:
    data = payload.get("data") or {}
    rows = data.get("results")
    return rows if isinstance(rows, list) else []


def curation_payload(payload: dict[str, Any]) -> dict[str, Any] | None:
    data = payload.get("data") or {}
    curation = data.get("curation")
    return curation if isinstance(curation, dict) else None


def hide_raw_score_names(value: Any) -> Any:
    if isinstance(value, str):
        return value.replace("EvidenceScore/Year", "raw API ranking/year").replace("EvidenceScore", "raw API score")
    if isinstance(value, dict):
        return {key: hide_raw_score_names(item) for key, item in value.items()}
    if isinstance(value, list):
        return [hide_raw_score_names(item) for item in value]
    return value


def evidence_lines(rows: list[dict[str, Any]], limit: int | None = None) -> list[str]:
    lines: list[str] = []
    for idx, row in enumerate(rows[:limit], start=1):
        ev = row.get("Evidence") or {}
        article = ev.get("article") or {}
        pmid = ev.get("pmid") or row.get("PMID") or "-"
        url = ev.get("pubmed_url") or (f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid != "-" else None)
        sentence = ev.get("sentence") or row.get("Sentence") or "-"
        term = row.get("TermName") or "-"
        hyp = row.get("Hypothesis") or "-"
        quality = row.get("EvidenceQualityScore") or ev.get("quality_score") or "-"
        journal = article.get("journal") or row.get("Journal") or "-"
        year = article.get("year") or row.get("Year") or "-"
        pubmed = f"[PMID:{pmid}]({url})" if url else f"PMID:{pmid}"
        lines.extend(
            [
                f"{idx}. {pubmed}",
                f"   - Gene: {row.get('Gene') or '-'}",
                f"   - Term: {term}",
                f"   - Hypothesis: {hyp}",
                f"   - Journal/Year: {journal} / {year}",
                f"   - EvidenceQualityScore: {quality}",
                f"   - Sentence: {sentence}",
            ]
        )
    return lines


def render_summary(payload: dict[str, Any]) -> str:
    data = payload.get("data") or {}
    rows = results(payload)
    curation = curation_payload(payload)
    summary = {
        "tool": payload.get("tool"),
        "status": payload.get("status"),
        "query": payload.get("query"),
        "count": payload.get("count"),
        "meta": hide_raw_score_names(payload.get("meta")),
    }
    if rows:
        summary["top_evidence"] = [
            {
                "Gene": row.get("Gene"),
                "PMID": row.get("PMID"),
                "TermName": row.get("TermName"),
                "Hypothesis": row.get("Hypothesis"),
                "EvidenceQualityScore": row.get("EvidenceQualityScore"),
            }
            for row in rows[:5]
        ]
    elif curation:
        summary["coverage_scope"] = curation.get("coverage_scope")
        summary["deduplication_summary"] = curation.get("deduplication_summary")
        summary["query_relative_patterns"] = curation.get("query_relative_patterns")
        summary["selected_evidence_preview"] = [
            {
                "Gene": row.get("Gene"),
                "PMID": row.get("PMID"),
                "TermName": row.get("TermName"),
                "Hypothesis": row.get("Hypothesis"),
                "EvidenceType": row.get("EvidenceType"),
                "IsLongTailEvidence": row.get("IsLongTailEvidence"),
            }
            for row in (curation.get("selected_evidence") or [])[:5]
        ]
    else:
        summary["data_keys"] = sorted(data.keys())
        summary["data"] = data
    return json.dumps(summary, ensure_ascii=False, indent=2)


def render_report(payload: dict[str, Any], api_page: str, request_url: str) -> str:
    rows = results(payload)
    data = payload.get("data") or {}
    curation = curation_payload(payload)
    query = payload.get("query") or {}
    meta = payload.get("meta") or {}
    lines = [
        "## Query",
        "",
        f"- tool: `{payload.get('tool')}`",
        f"- status: `{payload.get('status')}`",
        f"- query: `{json.dumps(query, ensure_ascii=False)}`",
        "",
        "## API Links",
        "",
        f"- api_page: {api_page}",
        f"- request_url: {request_url}",
        "",
        "## Summary",
        "",
        f"- returned_count: {payload.get('count')}",
        f"- top_k: {meta.get('top_k', '-')}",
        f"- candidate_limit: {meta.get('candidate_limit', '-')}",
        f"- ranking: {hide_raw_score_names(meta.get('ranking', '-'))}",
        "",
        "## Results",
        "",
    ]
    if rows:
        lines.append("| # | Gene | Term | Hypothesis | PMID | Sentence quality |")
        lines.append("| --- | --- | --- | --- | --- | --- |")
        for idx, row in enumerate(rows, start=1):
            pmid = row.get("PMID") or "-"
            lines.append(
                "| {idx} | {gene} | {term} | {hyp} | {pmid} | {quality} |".format(
                    idx=idx,
                    gene=md(row.get("Gene") or "-"),
                    term=md(row.get("TermName") or "-"),
                    hyp=md(row.get("Hypothesis") or "-"),
                    pmid=pmid,
                    quality=row.get("EvidenceQualityScore") or "-",
                )
            )
    elif curation:
        lines.extend(render_curation_overview(curation))
        lines.extend([""])
        lines.extend(render_selected_table(curation, "Server-Side Full-Pool Curated Evidence"))
        lines.extend([""])
        lines.extend(render_long_tail(curation))
        lines.extend([""])
        lines.extend(render_chronology(curation))
    else:
        lines.append("No sentence-level result rows were returned.")
        if data:
            lines.append("")
            lines.append("```json")
            lines.append(json.dumps(data, ensure_ascii=False, indent=2))
            lines.append("```")
    lines.extend(["", "## Evidence", ""])
    if rows:
        lines.extend(evidence_lines(rows))
    elif curation:
        selected = curation.get("selected_evidence") or []
        if not selected:
            lines.append("- No curated evidence sentences were selected.")
        for idx, item in enumerate(selected, start=1):
            pmid = item.get("PMID") or "-"
            url = item.get("PubMedURL") or ""
            pubmed = f"[PMID:{pmid}]({url})" if url else f"PMID:{pmid}"
            lines.extend(
                [
                    f"{idx}. {pubmed}",
                    f"   - Gene: {item.get('Gene') or '-'}",
                    f"   - Term: {item.get('TermName') or '-'}",
                    f"   - Evidence type: {item.get('EvidenceType') or '-'}",
                    f"   - Long-tail: {item.get('IsLongTailEvidence')}",
                    f"   - Sentence: {item.get('Sentence') or '-'}",
                ]
            )
    else:
        lines.append("- No evidence sentences available for this endpoint or query.")
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- Use returned PubMed links for evidence tracing.",
            "- Treat sentence-level associations as evidence, not standalone causal proof.",
            "- Raw API scoring fields are intentionally hidden in skill outputs; use exact sentences, provenance, diversity, and mechanism specificity for interpretation.",
            "- If sentences are generic, use a deep report builder so curation can run over the broadest available evidence pool before summarizing mechanisms.",
        ]
    )
    return "\n".join(lines)


def render_evidence_md(payload: dict[str, Any]) -> str:
    rows = results(payload)
    curation = curation_payload(payload)
    if not rows:
        if curation:
            selected = curation.get("selected_evidence") or []
            return "\n".join(
                [
                    f"{idx}. PMID:{item.get('PMID') or '-'} | {item.get('Gene') or '-'} | {item.get('TermName') or '-'}\n"
                    f"   - {item.get('Sentence') or '-'}"
                    for idx, item in enumerate(selected, start=1)
                ]
            ) or "No curated evidence sentences were selected."
        return "No sentence-level evidence rows were returned."
    return "\n".join(evidence_lines(rows))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Query AD-Alterome REST API.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--timeout", type=float, default=180)
    parser.add_argument("--output", choices=["json", "summary", "report", "evidence-md"], default="summary")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("schema")
    sub.add_parser("hypotheses")
    p = sub.add_parser("gene-events")
    p.add_argument("--gene", required=True)
    p.add_argument("--top-k", type=int, default=10)
    p = sub.add_parser("gene-overview")
    p.add_argument("--gene", required=True)
    p = sub.add_parser("gene-curation")
    p.add_argument("--gene", required=True)
    p.add_argument("--selected-limit", type=int, default=30)
    p = sub.add_parser("term-events")
    p.add_argument("--term", required=True)
    p.add_argument("--top-k", type=int, default=10)
    p = sub.add_parser("term-overview")
    p.add_argument("--term", required=True)
    p = sub.add_parser("term-curation")
    p.add_argument("--term", required=True)
    p.add_argument("--selected-limit", type=int, default=30)
    p = sub.add_parser("hypothesis-support")
    p.add_argument("--hypothesis", required=True)
    p.add_argument("--top-k", type=int, default=10)
    p = sub.add_parser("hypothesis-overview")
    p.add_argument("--hypothesis", required=True)
    p = sub.add_parser("hypothesis-curation")
    p.add_argument("--hypothesis", required=True)
    p.add_argument("--selected-limit", type=int, default=30)
    p = sub.add_parser("compare")
    p.add_argument("--gene-a", required=True)
    p.add_argument("--gene-b", required=True)
    return parser


def normalize_argv(argv: list[str]) -> list[str]:
    global_options = {"--base-url", "--timeout", "--output"}
    normalized: list[str] = []
    delayed: list[str] = []
    i = 0
    while i < len(argv):
        item = argv[i]
        if item in global_options and i + 1 < len(argv):
            delayed.extend([item, argv[i + 1]])
            i += 2
            continue
        normalized.append(item)
        i += 1
    return delayed + normalized


def main() -> int:
    args = build_parser().parse_args(normalize_argv(sys.argv[1:]))
    path, params = endpoint_for_args(args)
    request_url, payload = request_json(args.base_url, path, params, args.timeout)
    api_page = f"{args.base_url.rstrip('/')}/docs"
    if args.output == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    elif args.output == "summary":
        print(render_summary(payload))
    elif args.output == "report":
        print(render_report(payload, api_page, request_url))
    elif args.output == "evidence-md":
        print(render_evidence_md(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
