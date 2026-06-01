#!/usr/bin/env python3
"""Build a deterministic AD-Alterome deep gene report draft."""

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


def evidence_rows(payload: dict[str, Any]) -> list[dict[str, Any]]:
    rows = (payload.get("data") or {}).get("results")
    if not isinstance(rows, list):
        return []
    seen: set[tuple[str, str]] = set()
    unique_rows: list[dict[str, Any]] = []
    for row in rows:
        ev = row.get("Evidence") or {}
        key = (str(ev.get("pmid") or row.get("PMID") or ""), str(ev.get("sentence") or row.get("Sentence") or ""))
        if key in seen:
            continue
        seen.add(key)
        unique_rows.append(row)
    return unique_rows


def md_escape(value: Any) -> str:
    text = "" if value is None else str(value)
    return text.replace("|", "\\|").replace("\n", " ")


def count_values(rows: list[dict[str, Any]], key: str, limit: int = 10) -> list[tuple[str, int]]:
    counts: dict[str, int] = {}
    for row in rows:
        value = row.get(key)
        if value in (None, "", "-"):
            continue
        for part in str(value).split(","):
            clean = part.strip()
            if clean and clean != "-":
                counts[clean] = counts.get(clean, 0) + 1
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:limit]


def render_report(
    gene: str,
    base_url: str,
    overview_url: str,
    events_url: str,
    overview: dict[str, Any],
    events: dict[str, Any],
) -> str:
    rows = evidence_rows(events)
    summary = (overview.get("data") or {}).get("summary") or {}
    top_terms = (overview.get("data") or {}).get("top_terms") or []
    top_hypotheses = (overview.get("data") or {}).get("top_hypotheses") or []
    term_counts = count_values(rows, "TermName")
    hyp_counts = count_values(rows, "Hypothesis")
    lines = [
        f"# AD-Alterome Deep Gene Report: {gene}",
        "",
        "## 1. Query Scope and Provenance",
        "",
        f"- Target gene: `{gene}`",
        f"- API base URL: `{base_url.rstrip('/')}`",
        f"- Gene overview request: {overview_url}",
        f"- Evidence request: {events_url}",
        f"- Returned evidence rows: {len(rows)}",
        "",
        "## 2. Executive Claim",
        "",
        f"AD-Alterome contains {summary.get('event_count', 'unknown')} event records for `{gene}` across {summary.get('pmid_count', 'unknown')} PMID(s), {summary.get('term_count', 'unknown')} term(s), and {summary.get('hypothesis_count', 'unknown')} AD hypothesis field(s). Interpret this as curated sentence-level literature evidence rather than direct causal proof.",
        "",
        "## 3. Evidence and Source Map",
        "",
        "| # | PMID | Gene | Term | Hypothesis | EvidenceScore | Quality |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for idx, row in enumerate(rows, start=1):
        ev = row.get("Evidence") or {}
        pmid = row.get("PMID") or ev.get("pmid") or "-"
        url = ev.get("pubmed_url") or (f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid != "-" else "")
        pmid_md = f"[{pmid}]({url})" if url else pmid
        lines.append(
            "| {idx} | {pmid} | {gene} | {term} | {hyp} | {score} | {quality} |".format(
                idx=idx,
                pmid=pmid_md,
                gene=md_escape(row.get("Gene")),
                term=md_escape(row.get("TermName")),
                hyp=md_escape(row.get("Hypothesis")),
                score=md_escape(row.get("EvidenceScore")),
                quality=md_escape(row.get("EvidenceQualityScore")),
            )
        )
    lines.extend(["", "## 4. High-Quality Original Evidence", ""])
    for idx, row in enumerate(rows, start=1):
        ev = row.get("Evidence") or {}
        article = ev.get("article") or {}
        pmid = ev.get("pmid") or row.get("PMID") or "-"
        url = ev.get("pubmed_url") or (f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid != "-" else "")
        sentence = ev.get("sentence") or row.get("Sentence") or "-"
        lines.extend(
            [
                f"### Evidence {idx}: PMID {pmid}",
                "",
                f"- PubMed: {url or '-'}",
                f"- Journal/Year: {article.get('journal') or row.get('Journal') or '-'} / {article.get('year') or row.get('Year') or '-'}",
                f"- Term: {row.get('TermName') or '-'}",
                f"- Hypothesis: {row.get('Hypothesis') or '-'}",
                f"- EvidenceScore: {row.get('EvidenceScore') or '-'}; EvidenceQualityScore: {row.get('EvidenceQualityScore') or '-'}",
                f"- Original sentence: {sentence}",
                "",
            ]
        )
    lines.extend(
        [
            "## 5. Phenotype and Ontology-Term Interpretation",
            "",
            "| Term | Frequency in selected evidence |",
            "| --- | --- |",
        ]
    )
    for term, freq in term_counts:
        lines.append(f"| {md_escape(term)} | {freq} |")
    if not term_counts:
        lines.append("| No normalized term in selected evidence | - |")
    lines.extend(["", "Top overview terms:"])
    for item in top_terms[:10]:
        lines.append(f"- {item.get('TermName')} ({item.get('TermType')}): {item.get('freq')}")
    lines.extend(
        [
            "",
            "## 6. AD Hypothesis Interpretation",
            "",
            "| Hypothesis | Frequency in selected evidence |",
            "| --- | --- |",
        ]
    )
    for hyp, freq in hyp_counts:
        lines.append(f"| {md_escape(hyp)} | {freq} |")
    if not hyp_counts:
        lines.append("| No AD hypothesis in selected evidence | - |")
    lines.extend(["", "Top overview hypotheses:"])
    for item in top_hypotheses[:10]:
        lines.append(f"- {item.get('Hypothesis')}: {item.get('freq')}")
    lines.extend(
        [
            "",
            "## 7. Mechanism Synthesis",
            "",
            "Synthesize mechanisms from the exact sentences, Event chains, and AD interpretation fields. Separate direct sentence content from database-level interpretation. Avoid causal wording unless perturbation or validation evidence is explicit.",
            "",
            "## 8. Evidence Strength and Limitations",
            "",
            "- High `EvidenceScore` and `EvidenceQualityScore` indicate better sentence-level support, not automatic causality.",
            "- Generic sentences should be treated as weak evidence even when the gene or term is present.",
            "- Missing journal/year or MeSH metadata should be reported as a provenance limitation.",
            "",
            "## 9. Research Gaps and Follow-Up Priorities",
            "",
            "- Prioritize terms and hypotheses supported by multiple PMIDs.",
            "- Validate whether top mechanisms are supported by functional perturbation, genetics, animal models, or only text-mined association.",
            "- Add external enrichment from official sources only as a separate section.",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build AD-Alterome deep gene report draft.")
    parser.add_argument("--gene", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--top-k", type=int, default=12)
    parser.add_argument("--timeout", type=float, default=180)
    args = parser.parse_args()
    output_dir = Path(args.output_dir)
    data_dir = output_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    overview_url, overview = get_json(args.base_url, "/gene/overview", {"gene": args.gene}, args.timeout)
    events_url, events = get_json(args.base_url, "/gene/events", {"gene": args.gene, "top_k": args.top_k}, args.timeout)
    (data_dir / "query.json").write_text(
        json.dumps({"gene": args.gene, "base_url": args.base_url, "top_k": args.top_k}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (data_dir / "overview.json").write_text(json.dumps(overview, ensure_ascii=False, indent=2), encoding="utf-8")
    (data_dir / "evidence.json").write_text(json.dumps(events, ensure_ascii=False, indent=2), encoding="utf-8")
    report = render_report(args.gene, args.base_url, overview_url, events_url, overview, events)
    (output_dir / "report.md").write_text(report, encoding="utf-8")
    print(output_dir / "report.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
