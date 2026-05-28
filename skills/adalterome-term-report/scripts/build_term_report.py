#!/usr/bin/env python3
"""Build a deterministic AD-Alterome term or phenotype report."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


DEFAULT_BASE_URL = os.environ.get("ADALTEROME_API_BASE_URL", "http://127.0.0.1:8010")


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


def rows(payload: dict[str, Any]) -> list[dict[str, Any]]:
    records = (payload.get("data") or {}).get("results")
    if not isinstance(records, list):
        return []
    seen: set[tuple[str, str]] = set()
    unique: list[dict[str, Any]] = []
    for row in records:
        ev = row.get("Evidence") or {}
        key = (str(ev.get("pmid") or row.get("PMID") or ""), str(ev.get("sentence") or row.get("Sentence") or ""))
        if key not in seen:
            seen.add(key)
            unique.append(row)
    return unique


def md(value: Any) -> str:
    return ("" if value is None else str(value)).replace("|", "\\|").replace("\n", " ")


def render(term: str, base_url: str, overview_url: str, evidence_url: str, overview: dict[str, Any], evidence: dict[str, Any]) -> str:
    evidence_rows = rows(evidence)
    summary = (overview.get("data") or {}).get("summary") or {}
    top_genes = (overview.get("data") or {}).get("top_genes") or []
    top_hypotheses = (overview.get("data") or {}).get("top_hypotheses") or []
    lines = [
        f"# AD-Alterome Term Report: {term}",
        "",
        "## 1. Query Scope and Provenance",
        "",
        f"- Target term: `{term}`",
        f"- API base URL: `{base_url.rstrip('/')}`",
        f"- Overview request: {overview_url}",
        f"- Evidence request: {evidence_url}",
        f"- Returned unique evidence rows: {len(evidence_rows)}",
        "",
        "## 2. Term-Centered Executive Claim",
        "",
        f"AD-Alterome links `{term}` to {summary.get('event_count', 'unknown')} event records, {summary.get('pmid_count', 'unknown')} PMID(s), {summary.get('gene_count', 'unknown')} gene(s), and {summary.get('hypothesis_count', 'unknown')} AD hypothesis field(s). Treat this as a curated literature evidence map rather than a causal conclusion.",
        "",
        "## 3. Top Genes and Hypotheses",
        "",
        "### Top genes",
    ]
    for item in top_genes[:10]:
        lines.append(f"- {item.get('Gene')}: {item.get('freq')}")
    lines.append("")
    lines.append("### Top hypotheses")
    for item in top_hypotheses[:10]:
        lines.append(f"- {item.get('Hypothesis')}: {item.get('freq')}")
    lines.extend(["", "## 4. High-Quality Evidence Table", "", "| # | PMID | Gene | Term | Hypothesis | Score | Quality |", "| --- | --- | --- | --- | --- | --- | --- |"])
    for i, row in enumerate(evidence_rows, start=1):
        ev = row.get("Evidence") or {}
        pmid = ev.get("pmid") or row.get("PMID") or "-"
        url = ev.get("pubmed_url") or (f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid != "-" else "")
        lines.append(f"| {i} | [{pmid}]({url}) | {md(row.get('Gene'))} | {md(row.get('TermName'))} | {md(row.get('Hypothesis'))} | {md(row.get('EvidenceScore'))} | {md(row.get('EvidenceQualityScore'))} |")
    lines.extend(["", "## 5. Original Evidence Traces", ""])
    for i, row in enumerate(evidence_rows, start=1):
        ev = row.get("Evidence") or {}
        article = ev.get("article") or {}
        pmid = ev.get("pmid") or row.get("PMID") or "-"
        sentence = ev.get("sentence") or row.get("Sentence") or "-"
        lines.extend([
            f"### Evidence {i}: PMID {pmid}",
            "",
            f"- PubMed: {ev.get('pubmed_url') or '-'}",
            f"- Gene: {row.get('Gene') or '-'}",
            f"- Journal/Year: {article.get('journal') or row.get('Journal') or '-'} / {article.get('year') or row.get('Year') or '-'}",
            f"- Original sentence: {sentence}",
            "",
        ])
    lines.extend([
        "## 6. Mechanism and Pathway Interpretation",
        "",
        "Group mechanisms by recurring genes, terms, Event chains, and hypothesis labels. Keep direct sentence evidence separate from curated AD-Alterome interpretation.",
        "",
        "## 7. Evidence Limitations",
        "",
        "- Broad terms may aggregate heterogeneous mechanisms.",
        "- Record count can reflect literature density rather than biological importance.",
        "- Generic sentences should be treated as weak evidence even when ranked highly.",
        "",
        "## 8. Follow-Up Research Priorities",
        "",
        "- Prioritize top genes supported by multiple PMIDs.",
        "- Check whether support comes from original experiments, reviews, or database interpretation.",
        "- Add external validation sources only in a separate enrichment section.",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build AD-Alterome term report.")
    parser.add_argument("--term", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--top-k", type=int, default=12)
    parser.add_argument("--timeout", type=float, default=180)
    args = parser.parse_args()
    output_dir = Path(args.output_dir)
    data_dir = output_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    overview_url, overview = get_json(args.base_url, "/term/overview", {"term": args.term}, args.timeout)
    evidence_url, evidence = get_json(args.base_url, "/term/events", {"term": args.term, "top_k": args.top_k}, args.timeout)
    (data_dir / "query.json").write_text(json.dumps(vars(args), ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "overview.json").write_text(json.dumps(overview, ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "evidence.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
    report = render(args.term, args.base_url, overview_url, evidence_url, overview, evidence)
    (output_dir / "report.md").write_text(report, encoding="utf-8")
    print(output_dir / "report.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
