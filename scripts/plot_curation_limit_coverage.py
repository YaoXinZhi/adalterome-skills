#!/usr/bin/env python3
"""Plot top query-pool sizes against the current curation API limit."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sqlite3
from pathlib import Path
from statistics import median


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = REPO_ROOT.parent / "data" / "ad-alterome-db" / "ad_alterome_curated.db"
DEFAULT_OUTDIR = REPO_ROOT / "experimental-records" / "2026-06-21-curation-limit-coverage"
API_LIMIT = 500

CANONICAL_HYPOTHESES = [
    "Cholinergic Hypothesis",
    "Amyloid Hypothesis",
    "Tau Protein Hypothesis",
    "Neuroinflammation Hypothesis",
    "Oxidative Stress Hypothesis",
    "Metal Ion Hypothesis",
    "Glutamatergic Excitotoxicity Hypothesis",
    "Microbiota-Gut-Brain Axis Hypothesis",
    "Abnormal Autophagy Hypothesis",
    "Mitochondrial Autophagy Hypothesis",
    "Vascular Hypothesis",
]


def percentile(values: list[int], pct: float) -> int:
    if not values:
        return 0
    ordered = sorted(values)
    index = round((len(ordered) - 1) * pct)
    return ordered[index]


def strip_hypothesis_prefix(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^for ad:\s*", "", value, flags=re.IGNORECASE)
    value = re.sub(r"^\(\d+\)\s*", "", value)
    return value.strip()


def canonical_hypothesis(value: str) -> str | None:
    cleaned = strip_hypothesis_prefix(value)
    cleaned_lower = cleaned.lower()
    for hypothesis in CANONICAL_HYPOTHESES:
        if hypothesis.lower() in cleaned_lower:
            return hypothesis
    return None


def load_rows(db_path: Path) -> dict[str, list[dict[str, object]]]:
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        gene_rows = load_top_rows(conn, "gene", "Genes")
        term_rows = load_top_rows(conn, "term", "Phenotype/process")
        hypothesis_rows = load_hypothesis_rows(conn)
    finally:
        conn.close()
    return {
        "Genes": gene_rows,
        "Phenotype/process": term_rows,
        "Hypotheses": hypothesis_rows,
    }


def load_top_rows(conn: sqlite3.Connection, query_type: str, category: str) -> list[dict[str, object]]:
    records = conn.execute(
        """
        SELECT query_value, event_unique_count, curated_pool_count
        FROM curated_query_stats
        WHERE query_type = ?
        ORDER BY curated_pool_count DESC, event_unique_count DESC, query_value
        LIMIT 100
        """,
        (query_type,),
    ).fetchall()
    return [
        {
            "category": category,
            "rank": idx,
            "query_value": row["query_value"],
            "event_unique_count": int(row["event_unique_count"]),
            "curated_pool_count": int(row["curated_pool_count"]),
            "exceeds_500": int(row["curated_pool_count"]) > API_LIMIT,
        }
        for idx, row in enumerate(records, start=1)
    ]


def load_hypothesis_rows(conn: sqlite3.Connection) -> list[dict[str, object]]:
    grouped: dict[str, dict[str, object]] = {}
    for row in conn.execute(
        """
        SELECT query_value, event_unique_count, curated_pool_count
        FROM curated_query_stats
        WHERE query_type = 'hypothesis'
        """
    ):
        canonical = canonical_hypothesis(row["query_value"])
        if canonical is None:
            continue
        current = grouped.get(canonical)
        candidate = {
            "query_value": canonical,
            "event_unique_count": int(row["event_unique_count"]),
            "curated_pool_count": int(row["curated_pool_count"]),
        }
        if current is None or candidate["curated_pool_count"] > current["curated_pool_count"]:
            grouped[canonical] = candidate

    rows = sorted(
        grouped.values(),
        key=lambda row: (-int(row["curated_pool_count"]), -int(row["event_unique_count"]), str(row["query_value"])),
    )
    return [
        {
            "category": "Hypotheses",
            "rank": idx,
            "query_value": row["query_value"],
            "event_unique_count": int(row["event_unique_count"]),
            "curated_pool_count": int(row["curated_pool_count"]),
            "exceeds_500": int(row["curated_pool_count"]) > API_LIMIT,
        }
        for idx, row in enumerate(rows, start=1)
    ]


def summarize(rows_by_category: dict[str, list[dict[str, object]]]) -> dict[str, dict[str, object]]:
    summary: dict[str, dict[str, object]] = {}
    for category, rows in rows_by_category.items():
        counts = [int(row["curated_pool_count"]) for row in rows]
        summary[category] = {
            "n": len(rows),
            "above_500": sum(count > API_LIMIT for count in counts),
            "at_or_below_500": sum(count <= API_LIMIT for count in counts),
            "median": int(median(counts)) if counts else 0,
            "p90": percentile(counts, 0.90),
            "p95": percentile(counts, 0.95),
            "max": max(counts) if counts else 0,
            "max_query": rows[0]["query_value"] if rows else "",
        }
    return summary


def write_csv(rows_by_category: dict[str, list[dict[str, object]]], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            lineterminator="\n",
            fieldnames=[
                "category",
                "rank",
                "query_value",
                "event_unique_count",
                "curated_pool_count",
                "exceeds_500",
            ],
        )
        writer.writeheader()
        for rows in rows_by_category.values():
            writer.writerows(rows)


def plot(rows_by_category: dict[str, list[dict[str, object]]], summary: dict[str, dict[str, object]], png_path: Path) -> None:
    import matplotlib.pyplot as plt

    colors = {
        "Genes": "#2B6CB0",
        "Phenotype/process": "#2F855A",
        "Hypotheses": "#805AD5",
    }
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.8), sharey=True)
    for ax, (category, rows) in zip(axes, rows_by_category.items()):
        x_values = [int(row["rank"]) for row in rows]
        y_values = [int(row["curated_pool_count"]) for row in rows]
        ax.plot(x_values, y_values, marker="o", markersize=3, linewidth=1.8, color=colors[category])
        ax.axhline(API_LIMIT, color="#C53030", linestyle="--", linewidth=1.5)
        ax.set_yscale("log")
        ax.set_title(category, fontsize=12, weight="bold")
        ax.set_xlabel("Rank by curated pool size")
        ax.grid(True, which="major", axis="y", alpha=0.25)
        ax.grid(True, which="minor", axis="y", alpha=0.12)
        stats = summary[category]
        ax.text(
            0.98,
            0.96,
            f"n={stats['n']}\n>500: {stats['above_500']}\nmedian: {stats['median']}\np90: {stats['p90']}",
            ha="right",
            va="top",
            transform=ax.transAxes,
            fontsize=9,
            bbox={"boxstyle": "round,pad=0.35", "facecolor": "white", "edgecolor": "#CBD5E0", "alpha": 0.92},
        )
        if rows:
            ax.annotate(
                str(y_values[0]),
                xy=(x_values[0], y_values[0]),
                xytext=(8, 0),
                textcoords="offset points",
                va="center",
                fontsize=8,
            )
    axes[0].set_ylabel("Curated rows needed for full return (log scale)")
    fig.suptitle("AD-Alterome curated query-pool burden vs API selected_limit=500", fontsize=14, weight="bold")
    fig.text(
        0.5,
        0.01,
        "Rows are curated_pool_count from curated_query_stats; hypotheses are canonicalized by stripping numeric prefixes and merging aliases.",
        ha="center",
        fontsize=9,
        color="#4A5568",
    )
    fig.tight_layout(rect=(0, 0.04, 1, 0.93))
    fig.savefig(png_path, dpi=200)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB, help="Path to ad_alterome_curated.db")
    parser.add_argument("--outdir", type=Path, default=DEFAULT_OUTDIR, help="Output directory")
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)
    rows_by_category = load_rows(args.db)
    summary = summarize(rows_by_category)

    csv_path = args.outdir / "top100_query_pool_counts.csv"
    summary_path = args.outdir / "top100_query_pool_summary.json"
    png_path = args.outdir / "top100_query_pool_counts.png"

    write_csv(rows_by_category, csv_path)
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    plot(rows_by_category, summary, png_path)

    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print(f"Wrote {csv_path}")
    print(f"Wrote {png_path}")


if __name__ == "__main__":
    main()
