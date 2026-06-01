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
    if command == "term-events":
        return "/term/events", {"term": args.term, "top_k": args.top_k}
    if command == "term-overview":
        return "/term/overview", {"term": args.term}
    if command == "hypothesis-support":
        return "/hypothesis/support", {"hypothesis": args.hypothesis, "top_k": args.top_k}
    if command == "hypothesis-overview":
        return "/hypothesis/overview", {"hypothesis": args.hypothesis}
    if command == "compare":
        return "/compare/genes", {"gene_a": args.gene_a, "gene_b": args.gene_b}
    raise SystemExit(f"Unsupported command: {command}")


def results(payload: dict[str, Any]) -> list[dict[str, Any]]:
    data = payload.get("data") or {}
    rows = data.get("results")
    return rows if isinstance(rows, list) else []


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
        score = row.get("EvidenceScore") or ev.get("evidence_score") or "-"
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
                f"   - EvidenceScore: {score}; EvidenceQualityScore: {quality}",
                f"   - Sentence: {sentence}",
            ]
        )
    return lines


def render_summary(payload: dict[str, Any]) -> str:
    data = payload.get("data") or {}
    rows = results(payload)
    summary = {
        "tool": payload.get("tool"),
        "status": payload.get("status"),
        "query": payload.get("query"),
        "count": payload.get("count"),
        "meta": payload.get("meta"),
    }
    if rows:
        summary["top_evidence"] = [
            {
                "Gene": row.get("Gene"),
                "PMID": row.get("PMID"),
                "TermName": row.get("TermName"),
                "Hypothesis": row.get("Hypothesis"),
                "EvidenceScore": row.get("EvidenceScore"),
                "EvidenceQualityScore": row.get("EvidenceQualityScore"),
            }
            for row in rows[:5]
        ]
    else:
        summary["data_keys"] = sorted(data.keys())
        summary["data"] = data
    return json.dumps(summary, ensure_ascii=False, indent=2)


def render_report(payload: dict[str, Any], api_page: str, request_url: str) -> str:
    rows = results(payload)
    data = payload.get("data") or {}
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
        f"- ranking: {meta.get('ranking', '-')}",
        "",
        "## Results",
        "",
    ]
    if rows:
        lines.append("| # | Gene | Term | Hypothesis | PMID | EvidenceScore | Quality |")
        lines.append("| --- | --- | --- | --- | --- | --- | --- |")
        for idx, row in enumerate(rows, start=1):
            pmid = row.get("PMID") or "-"
            lines.append(
                "| {idx} | {gene} | {term} | {hyp} | {pmid} | {score} | {quality} |".format(
                    idx=idx,
                    gene=row.get("Gene") or "-",
                    term=row.get("TermName") or "-",
                    hyp=row.get("Hypothesis") or "-",
                    pmid=pmid,
                    score=row.get("EvidenceScore") or "-",
                    quality=row.get("EvidenceQualityScore") or "-",
                )
            )
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
    else:
        lines.append("- No evidence sentences available for this endpoint or query.")
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- Use returned PubMed links for evidence tracing.",
            "- Treat sentence-level associations as evidence, not standalone causal proof.",
            "- If sentences are generic, prefer records with higher `EvidenceQualityScore` or rerun with a larger `top_k` for manual review.",
        ]
    )
    return "\n".join(lines)


def render_evidence_md(payload: dict[str, Any]) -> str:
    rows = results(payload)
    if not rows:
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
    p = sub.add_parser("term-events")
    p.add_argument("--term", required=True)
    p.add_argument("--top-k", type=int, default=10)
    p = sub.add_parser("term-overview")
    p.add_argument("--term", required=True)
    p = sub.add_parser("hypothesis-support")
    p.add_argument("--hypothesis", required=True)
    p.add_argument("--top-k", type=int, default=10)
    p = sub.add_parser("hypothesis-overview")
    p.add_argument("--hypothesis", required=True)
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
