#!/usr/bin/env python3
"""Local cache helpers for AD-Alterome API payloads."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


CACHE_VERSION = 1
DEFAULT_CACHE_DIR = Path(os.environ.get("ADALTEROME_CACHE_DIR", "~/.adalterome-skills/cache")).expanduser()
DEFAULT_MAX_AGE_DAYS = float(os.environ.get("ADALTEROME_CACHE_MAX_AGE_DAYS", "30"))


def build_url(base_url: str, path: str, params: dict[str, Any]) -> str:
    query = urlencode(params, doseq=True)
    url = f"{base_url.rstrip('/')}{path}"
    return f"{url}?{query}" if query else url


def cache_enabled() -> bool:
    return os.environ.get("ADALTEROME_DISABLE_CACHE", "").strip().lower() not in {"1", "true", "yes"}


def refresh_requested() -> bool:
    return os.environ.get("ADALTEROME_REFRESH_CACHE", "").strip().lower() in {"1", "true", "yes"}


def cache_file_for_url(url: str, cache_dir: Path | None = None) -> Path:
    root = cache_dir or DEFAULT_CACHE_DIR
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()
    return root / "requests" / digest[:2] / f"{digest}.json"


def index_file(cache_dir: Path | None = None) -> Path:
    return (cache_dir or DEFAULT_CACHE_DIR) / "index.jsonl"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _strip_cache_meta(payload: dict[str, Any]) -> dict[str, Any]:
    clean = copy.deepcopy(payload)
    meta = clean.get("meta")
    if isinstance(meta, dict):
        meta.pop("_local_cache", None)
    return clean


def _cache_meta(
    *,
    url: str,
    path: Path,
    cache_hit: bool,
    saved_at: str | None,
    age_seconds: float | None = None,
) -> dict[str, Any]:
    return {
        "enabled": True,
        "cache_hit": cache_hit,
        "request_url": url,
        "cache_file": str(path),
        "cache_dir": str(path.parents[2]),
        "index_file": str(index_file(path.parents[2])),
        "saved_at": saved_at,
        "age_seconds": round(age_seconds, 3) if age_seconds is not None else None,
    }


def attach_cache_meta(payload: dict[str, Any], meta: dict[str, Any]) -> dict[str, Any]:
    output = copy.deepcopy(payload)
    payload_meta = output.setdefault("meta", {})
    if isinstance(payload_meta, dict):
        payload_meta["_local_cache"] = meta
    return output


def load_cached_payload(
    url: str,
    *,
    cache_dir: Path | None = None,
    max_age_days: float = DEFAULT_MAX_AGE_DAYS,
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    path = cache_file_for_url(url, cache_dir)
    if not path.exists():
        return None, None
    try:
        envelope = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None, None
    saved_epoch = float(envelope.get("saved_at_epoch") or 0)
    age_seconds = max(0.0, time.time() - saved_epoch) if saved_epoch else None
    if age_seconds is not None and max_age_days >= 0 and age_seconds > max_age_days * 86400:
        return None, None
    payload = envelope.get("payload")
    if not isinstance(payload, dict):
        return None, None
    meta = _cache_meta(
        url=url,
        path=path,
        cache_hit=True,
        saved_at=envelope.get("saved_at"),
        age_seconds=age_seconds,
    )
    return payload, meta


def save_payload(
    url: str,
    payload: dict[str, Any],
    *,
    base_url: str,
    path: str,
    params: dict[str, Any],
    cache_dir: Path | None = None,
) -> dict[str, Any]:
    cache_path = cache_file_for_url(url, cache_dir)
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    saved_at = _now_iso()
    envelope = {
        "cache_version": CACHE_VERSION,
        "saved_at": saved_at,
        "saved_at_epoch": time.time(),
        "base_url": base_url.rstrip("/"),
        "path": path,
        "params": params,
        "request_url": url,
        "payload": _strip_cache_meta(payload),
    }
    cache_path.write_text(json.dumps(envelope, ensure_ascii=False, indent=2), encoding="utf-8")
    idx = index_file(cache_dir)
    idx.parent.mkdir(parents=True, exist_ok=True)
    idx.write_text("", encoding="utf-8") if not idx.exists() else None
    with idx.open("a", encoding="utf-8") as handle:
        handle.write(
            json.dumps(
                {
                    "saved_at": saved_at,
                    "base_url": base_url.rstrip("/"),
                    "path": path,
                    "params": params,
                    "request_url": url,
                    "cache_file": str(cache_path),
                },
                ensure_ascii=False,
            )
            + "\n"
        )
    return _cache_meta(url=url, path=cache_path, cache_hit=False, saved_at=saved_at)


def fetch_json_with_cache(
    base_url: str,
    path: str,
    params: dict[str, Any],
    timeout: float,
) -> tuple[str, dict[str, Any]]:
    url = build_url(base_url, path, params)
    if cache_enabled() and not refresh_requested():
        cached, meta = load_cached_payload(url)
        if cached is not None and meta is not None:
            return url, attach_cache_meta(cached, meta)

    request = Request(url, headers={"Accept": "application/json"})
    try:
        with urlopen(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        raise SystemExit(f"API HTTP error {exc.code}: {exc.reason}") from exc
    except URLError as exc:
        raise SystemExit(f"API connection error: {exc.reason}") from exc

    if isinstance(payload, dict) and cache_enabled():
        meta = save_payload(url, payload, base_url=base_url, path=path, params=params)
        payload = attach_cache_meta(payload, meta)
    return url, payload


def fetch_json_optional_with_cache(
    base_url: str,
    path: str,
    params: dict[str, Any],
    timeout: float,
) -> tuple[str, dict[str, Any] | None, str | None]:
    try:
        url, payload = fetch_json_with_cache(base_url, path, params, timeout)
        return url, payload, None
    except SystemExit as exc:
        return build_url(base_url, path, params), None, str(exc)
    except Exception as exc:
        return build_url(base_url, path, params), None, f"API request failed: {exc}"


def payload_cache_meta(payload: dict[str, Any] | None) -> dict[str, Any] | None:
    if not isinstance(payload, dict):
        return None
    meta = payload.get("meta")
    if not isinstance(meta, dict):
        return None
    cache_meta = meta.get("_local_cache")
    return cache_meta if isinstance(cache_meta, dict) else None


def cache_provenance_lines(named_payloads: list[tuple[str, dict[str, Any] | None]]) -> list[str]:
    lines: list[str] = []
    seen_files = set()
    index_path = None
    for label, payload in named_payloads:
        meta = payload_cache_meta(payload)
        if not meta:
            continue
        cache_file = meta.get("cache_file")
        if not cache_file or cache_file in seen_files:
            continue
        seen_files.add(cache_file)
        index_path = meta.get("index_file") or index_path
        status = "reused" if meta.get("cache_hit") else "saved"
        lines.append(f"- {label} raw API payload cache ({status}): `{cache_file}`")
    if index_path:
        lines.append(f"- Local cache index: `{index_path}`")
    return lines


def cache_manifest(named_payloads: list[tuple[str, dict[str, Any] | None]]) -> dict[str, Any]:
    entries = []
    for label, payload in named_payloads:
        meta = payload_cache_meta(payload)
        if meta:
            entries.append({"label": label, **meta})
    return {
        "cache_dir": str(DEFAULT_CACHE_DIR),
        "index_file": str(index_file()),
        "entries": entries,
        "note": (
            "These files preserve raw API JSON payloads for exact repeat requests. "
            "Set ADALTEROME_REFRESH_CACHE=1 to force a fresh API request or "
            "ADALTEROME_DISABLE_CACHE=1 to bypass caching."
        ),
    }


def write_cache_manifest(
    path: Path,
    named_payloads: list[tuple[str, dict[str, Any] | None]],
) -> list[str]:
    manifest = cache_manifest(named_payloads)
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = cache_provenance_lines(named_payloads)
    if lines:
        lines.append(f"- Output cache manifest: `{path}`")
    return lines
