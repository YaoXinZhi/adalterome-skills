"""Fetch AD-Alterome evidence from the live REST API for report curation."""

from __future__ import annotations

import json
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


API_MAX_TOP_K = 50
SERVER_CURATION_MAX_SELECTED_LIMIT = 100


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


def request_json_optional(
    base_url: str,
    path: str,
    params: dict[str, Any],
    timeout: float,
) -> tuple[str, dict[str, Any] | None, str | None]:
    query = urlencode(params, doseq=True)
    url = f"{base_url.rstrip('/')}{path}"
    if query:
        url = f"{url}?{query}"
    request = Request(url, headers={"Accept": "application/json"})
    try:
        with urlopen(request, timeout=timeout) as response:
            return url, json.loads(response.read().decode("utf-8")), None
    except HTTPError as exc:
        return url, None, f"API HTTP error {exc.code}: {exc.reason}"
    except URLError as exc:
        return url, None, f"API connection error: {exc.reason}"
    except Exception as exc:
        return url, None, f"API request failed: {exc}"


def api_top_k(requested_curation_limit: int) -> int:
    if requested_curation_limit <= 0:
        return API_MAX_TOP_K
    return min(requested_curation_limit, API_MAX_TOP_K)


def api_selected_limit(requested_selected_limit: int) -> int:
    if requested_selected_limit <= 0:
        return 30
    return min(requested_selected_limit, SERVER_CURATION_MAX_SELECTED_LIMIT)


def _remote_curation(
    base_url: str,
    path: str,
    params: dict[str, Any],
    timeout: float,
    selected_limit: int,
) -> tuple[str, dict[str, Any] | None]:
    requested_selected_limit = api_selected_limit(selected_limit)
    url, payload, error = request_json_optional(
        base_url,
        path,
        {**params, "selected_limit": requested_selected_limit},
        timeout,
    )
    if error or not isinstance(payload, dict):
        return url, None
    curation = (payload.get("data") or {}).get("curation")
    if payload.get("status") != "ok" or not isinstance(curation, dict):
        return url, None
    scope = curation.setdefault("coverage_scope", {})
    scope["curation_endpoint_url"] = url
    scope.setdefault("curation_source", payload.get("meta", {}).get("curation_source", "remote_api"))
    scope.setdefault("curation_scope", payload.get("meta", {}).get("curation_scope", "server_full_query_pool"))
    return url, payload


def curation_package_from_response(payload: dict[str, Any]) -> dict[str, Any] | None:
    curation = (payload.get("data") or {}).get("curation")
    return curation if isinstance(curation, dict) else None


def _remote_events(
    base_url: str,
    path: str,
    params: dict[str, Any],
    timeout: float,
    requested_curation_limit: int,
) -> tuple[str, dict[str, Any]]:
    requested_top_k = api_top_k(requested_curation_limit)
    url, payload = request_json(base_url, path, {**params, "top_k": requested_top_k}, timeout)
    meta = payload.setdefault("meta", {})
    meta.update(
        {
            "curation_source": "remote_api",
            "curation_scope": "api_sentence_sample",
            "api_max_top_k": API_MAX_TOP_K,
            "requested_curation_limit": requested_curation_limit,
            "returned_curation_rows": payload.get("count"),
            "limit_notice": (
                "AD-Alterome public event endpoints return a capped sentence-level evidence sample "
                f"(max top_k={API_MAX_TOP_K}); overview endpoints provide aggregate counts."
            ),
        }
    )
    return url, payload


def fetch_gene_events_for_curation(
    base_url: str,
    gene: str,
    timeout: float,
    curation_limit: int = API_MAX_TOP_K,
) -> tuple[str, dict[str, Any]]:
    return _remote_events(
        base_url,
        "/gene/events",
        {"gene": str(gene).strip().upper()},
        timeout,
        curation_limit,
    )


def fetch_gene_curation(
    base_url: str,
    gene: str,
    timeout: float,
    selected_limit: int = 30,
) -> tuple[str, dict[str, Any] | None]:
    return _remote_curation(
        base_url,
        "/gene/curation",
        {"gene": str(gene).strip().upper()},
        timeout,
        selected_limit,
    )


def fetch_term_events_for_curation(
    base_url: str,
    term: str,
    timeout: float,
    curation_limit: int = API_MAX_TOP_K,
) -> tuple[str, dict[str, Any]]:
    return _remote_events(
        base_url,
        "/term/events",
        {"term": str(term).strip()},
        timeout,
        curation_limit,
    )


def fetch_term_curation(
    base_url: str,
    term: str,
    timeout: float,
    selected_limit: int = 30,
) -> tuple[str, dict[str, Any] | None]:
    return _remote_curation(
        base_url,
        "/term/curation",
        {"term": str(term).strip()},
        timeout,
        selected_limit,
    )


def fetch_hypothesis_support_for_curation(
    base_url: str,
    hypothesis: str,
    timeout: float,
    curation_limit: int = API_MAX_TOP_K,
) -> tuple[str, dict[str, Any]]:
    return _remote_events(
        base_url,
        "/hypothesis/support",
        {"hypothesis": str(hypothesis).strip()},
        timeout,
        curation_limit,
    )


def fetch_hypothesis_curation(
    base_url: str,
    hypothesis: str,
    timeout: float,
    selected_limit: int = 30,
) -> tuple[str, dict[str, Any] | None]:
    return _remote_curation(
        base_url,
        "/hypothesis/curation",
        {"hypothesis": str(hypothesis).strip()},
        timeout,
        selected_limit,
    )
