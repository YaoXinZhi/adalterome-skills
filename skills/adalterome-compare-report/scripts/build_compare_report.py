#!/usr/bin/env python3
"""Build a deterministic AD-Alterome two-gene comparison report."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


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


def evidence_section(title: str, evidence_rows: list[dict[str, Any]]) -> list[str]:
    lines = [f"## {title}", ""]
    for i, row in enumerate(evidence_rows, start=1):
        ev = row.get("Evidence") or {}
        pmid = ev.get("pmid") or row.get("PMID") or "-"
        lines.extend([
            f"### Evidence {i}: PMID {pmid}",
            "",
            f"- PubMed: {ev.get('pubmed_url') or '-'}",
            f"- Gene: {row.get('Gene') or '-'}",
            f"- Term: {row.get('TermName') or '-'}",
            f"- Hypothesis: {row.get('Hypothesis') or '-'}",
            f"- EvidenceScore: {row.get('EvidenceScore') or '-'}; EvidenceQualityScore: {row.get('EvidenceQualityScore') or '-'}",
            f"- Original sentence: {ev.get('sentence') or row.get('Sentence') or '-'}",
            "",
        ])
    if not evidence_rows:
        lines.append("No evidence rows returned.")
    return lines


def render(gene_a: str, gene_b: str, base_url: str, compare_url: str, gene_a_url: str, gene_b_url: str, compare: dict[str, Any], evidence_a: dict[str, Any], evidence_b: dict[str, Any]) -> str:
    data = compare.get("data") or {}
    rows_a = rows(evidence_a)
    rows_b = rows(evidence_b)
    lines = [
        f"# AD-Alterome Gene Comparison: {gene_a} vs {gene_b}",
        "",
        "## 1. Query Scope and Comparison Frame",
        "",
        f"- Gene A: `{gene_a}`",
        f"- Gene B: `{gene_b}`",
        f"- API base URL: `{base_url.rstrip('/')}`",
        f"- Compare request: {compare_url}",
        f"- Gene A evidence request: {gene_a_url}",
        f"- Gene B evidence request: {gene_b_url}",
        "",
        "## 2. Side-by-Side Overview",
        "",
        "| Metric | Gene A | Gene B |",
        "| --- | --- | --- |",
    ]
    overview_a = data.get("gene_a_overview") or {}
    overview_b = data.get("gene_b_overview") or {}
    for key in ["event_count", "pmid_count", "term_count", "hypothesis_count", "avg_evidence_score"]:
        lines.append(f"| {key} | {md(overview_a.get(key))} | {md(overview_b.get(key))} |")
    lines.extend(["", "## 3. Shared Terms and Hypotheses", "", "### Shared terms"])
    lines.extend(bullet_items(data.get("shared_terms") or [], "TermName"))
    lines.extend(["", "### Shared hypotheses"])
    lines.extend(bullet_items(data.get("shared_hypotheses") or [], "Hypothesis"))
    lines.extend(["", f"## 4. {gene_a}-Specific Patterns", "", "### Unique terms"])
    lines.extend(bullet_items(data.get("unique_terms_a") or [], "TermName"))
    lines.extend(["", "### Unique hypotheses"])
    lines.extend(bullet_items(data.get("unique_hypotheses_a") or [], "Hypothesis"))
    lines.extend(["", f"## 5. {gene_b}-Specific Patterns", "", "### Unique terms"])
    lines.extend(bullet_items(data.get("unique_terms_b") or [], "TermName"))
    lines.extend(["", "### Unique hypotheses"])
    lines.extend(bullet_items(data.get("unique_hypotheses_b") or [], "Hypothesis"))
    lines.extend([""])
    lines.extend(evidence_section(f"6. High-Quality Evidence for {gene_a}", rows_a))
    lines.extend(evidence_section(f"7. High-Quality Evidence for {gene_b}", rows_b))
    lines.extend([
        "## 8. Comparative Mechanism Synthesis",
        "",
        "Use shared terms and hypotheses to describe common AD-Alterome patterns. Use unique terms, unique hypotheses, and original sentence evidence to describe gene-specific mechanisms.",
        "",
        "## 9. Limitations and Follow-Up Priorities",
        "",
        "- Record counts can reflect literature density and curation bias.",
        "- Compare claims should cite sentence-level evidence for both genes.",
        "- Follow-up work should test whether shared terms reflect the same mechanism or different routes to similar phenotypes.",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build AD-Alterome two-gene comparison report.")
    parser.add_argument("--gene-a", required=True)
    parser.add_argument("--gene-b", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--top-k", type=int, default=8)
    parser.add_argument("--timeout", type=float, default=180)
    args = parser.parse_args()
    output_dir = Path(args.output_dir)
    data_dir = output_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    compare_url, compare = get_json(args.base_url, "/compare/genes", {"gene_a": args.gene_a, "gene_b": args.gene_b}, args.timeout)
    gene_a_url, evidence_a = get_json(args.base_url, "/gene/events", {"gene": args.gene_a, "top_k": args.top_k}, args.timeout)
    gene_b_url, evidence_b = get_json(args.base_url, "/gene/events", {"gene": args.gene_b, "top_k": args.top_k}, args.timeout)
    (data_dir / "query.json").write_text(json.dumps(vars(args), ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "compare.json").write_text(json.dumps(compare, ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "gene_a_evidence.json").write_text(json.dumps(evidence_a, ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "gene_b_evidence.json").write_text(json.dumps(evidence_b, ensure_ascii=False, indent=2), encoding="utf-8")
    (output_dir / "report.md").write_text(render(args.gene_a, args.gene_b, args.base_url, compare_url, gene_a_url, gene_b_url, compare, evidence_a, evidence_b), encoding="utf-8")
    print(output_dir / "report.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
