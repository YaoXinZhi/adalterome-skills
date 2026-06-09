"""Fetch AD-Alterome evidence from the live REST API for report curation."""

from __future__ import annotations

from typing import Any

from query_cache import fetch_json_optional_with_cache, fetch_json_with_cache, payload_cache_meta


API_MAX_TOP_K = 50
SERVER_CURATION_MAX_SELECTED_LIMIT = 500
LEGACY_SERVER_CURATION_MAX_SELECTED_LIMIT = 100


def request_json(base_url: str, path: str, params: dict[str, Any], timeout: float) -> tuple[str, dict[str, Any]]:
    return fetch_json_with_cache(base_url, path, params, timeout)


def request_json_optional(
    base_url: str,
    path: str,
    params: dict[str, Any],
    timeout: float,
) -> tuple[str, dict[str, Any] | None, str | None]:
    return fetch_json_optional_with_cache(base_url, path, params, timeout)


def api_top_k(requested_curation_limit: int) -> int:
    if requested_curation_limit <= 0:
        return API_MAX_TOP_K
    return min(requested_curation_limit, API_MAX_TOP_K)


def api_selected_limit(requested_selected_limit: int) -> int:
    if requested_selected_limit <= 0:
        return 30
    return min(requested_selected_limit, SERVER_CURATION_MAX_SELECTED_LIMIT)


def selected_limit_attempts(requested_selected_limit: int) -> list[int]:
    """Try the requested curation size first, then legacy-safe fallbacks."""
    first = api_selected_limit(requested_selected_limit)
    attempts = [first]
    for fallback in (LEGACY_SERVER_CURATION_MAX_SELECTED_LIMIT, 30):
        if first > fallback and fallback not in attempts:
            attempts.append(fallback)
    return attempts


def _remote_curation(
    base_url: str,
    path: str,
    params: dict[str, Any],
    timeout: float,
    selected_limit: int,
) -> tuple[str, dict[str, Any] | None]:
    url, payload, _error = _remote_curation_with_error(base_url, path, params, timeout, selected_limit)
    return url, payload


def _remote_curation_with_error(
    base_url: str,
    path: str,
    params: dict[str, Any],
    timeout: float,
    selected_limit: int,
) -> tuple[str, dict[str, Any] | None, str | None]:
    requested_selected_limit = api_selected_limit(selected_limit)
    url = ""
    payload: dict[str, Any] | None = None
    error: str | None = None
    used_selected_limit = requested_selected_limit
    for attempted_selected_limit in selected_limit_attempts(selected_limit):
        used_selected_limit = attempted_selected_limit
        url, payload, error = request_json_optional(
            base_url,
            path,
            {**params, "selected_limit": attempted_selected_limit},
            timeout,
        )
        if not error or "HTTP error 422" not in str(error):
            break
    if error or not isinstance(payload, dict):
        return url, None, error or "curation endpoint returned no payload"
    curation = (payload.get("data") or {}).get("curation")
    if payload.get("status") != "ok" or not isinstance(curation, dict):
        message = (payload.get("meta") or {}).get("message") or payload.get("status") or "curation endpoint returned no curation object"
        return url, None, str(message)
    scope = curation.setdefault("coverage_scope", {})
    scope["curation_endpoint_url"] = url
    scope["requested_selected_limit"] = requested_selected_limit
    scope["used_selected_limit"] = used_selected_limit
    if used_selected_limit != requested_selected_limit:
        scope["selected_limit_retry_reason"] = "server rejected larger selected_limit; retried with a legacy-compatible limit"
    scope.setdefault("curation_source", payload.get("meta", {}).get("curation_source", "remote_api"))
    scope.setdefault("curation_scope", payload.get("meta", {}).get("curation_scope", "server_full_query_pool"))
    cache_meta = payload_cache_meta(payload)
    if cache_meta:
        scope["local_raw_payload_cache"] = cache_meta.get("cache_file")
        scope["local_cache_hit"] = cache_meta.get("cache_hit")
    return url, payload, None


def curation_unavailable_response(
    *,
    tool: str,
    query: dict[str, Any],
    query_type: str,
    request_url: str,
    reason: str | None,
    overview: dict[str, Any] | None = None,
) -> dict[str, Any]:
    overview_summary = ((overview or {}).get("data") or {}).get("summary")
    overview_event_count = overview_summary.get("event_count") if isinstance(overview_summary, dict) else None
    reason_text = reason or "curation endpoint returned no usable payload"
    curation = {
        "global_statistics": {},
        "coverage_scope": {
            "query_type": query_type,
            "curation_source": "unavailable",
            "curation_scope": "curation_endpoint_unavailable",
            "overview_event_count": overview_event_count,
            "matched_event_count": overview_event_count,
            "curation_pool_rows": 0,
            "coverage_ratio": None,
            "curation_endpoint_url": request_url,
            "curation_failure_reason": reason_text,
            "event_endpoint_fallback": "disabled",
            "api_limit_notice": (
                "Report builders do not fall back to capped event endpoints when full-pool "
                "curation is unavailable; selected evidence is intentionally empty."
            ),
        },
        "deduplication_summary": {
            "curation_pool_row_count": 0,
            "event_unique_rows": 0,
            "event_deduplication_key": "not applied because curation endpoint was unavailable",
            "unique_pmids": 0,
            "unique_genes": 0,
            "unique_phenotypes": 0,
            "unique_terms": 0,
            "unique_alteration_taxonomies": 0,
            "unique_gene_alterations": 0,
            "unique_alteration_signatures": 0,
            "unique_hypotheses": 0,
        },
        "dominant_clusters": {},
        "query_relative_patterns": {},
        "long_tail_definition": {
            "method": "not computed because curation endpoint was unavailable",
            "dimensions": [],
            "thresholds": {},
        },
        "long_tail_signals": [],
        "evidence_type_groups": {},
        "mechanism_strata": {},
        "chronological_summary": [],
        "bias_notes": [
            f"Curation endpoint unavailable: {reason_text}",
            "Capped event endpoints were not used as report fallback.",
        ],
        "selected_evidence": [],
    }
    return {
        "tool": tool,
        "status": "partial",
        "query": query,
        "count": 0,
        "data": {"results": [], "curation": curation},
        "meta": {
            "curation_source": "unavailable",
            "curation_scope": "curation_endpoint_unavailable",
            "curation_endpoint_url": request_url,
            "curation_failure_reason": reason_text,
            "event_endpoint_fallback": "disabled",
        },
    }


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
    cache_meta = payload_cache_meta(payload)
    if cache_meta:
        meta["local_raw_payload_cache"] = cache_meta.get("cache_file")
        meta["local_cache_hit"] = cache_meta.get("cache_hit")
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


def fetch_gene_curation_with_error(
    base_url: str,
    gene: str,
    timeout: float,
    selected_limit: int = 30,
) -> tuple[str, dict[str, Any] | None, str | None]:
    return _remote_curation_with_error(
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


def fetch_term_curation_with_error(
    base_url: str,
    term: str,
    timeout: float,
    selected_limit: int = 30,
) -> tuple[str, dict[str, Any] | None, str | None]:
    return _remote_curation_with_error(
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


def fetch_hypothesis_curation_with_error(
    base_url: str,
    hypothesis: str,
    timeout: float,
    selected_limit: int = 30,
) -> tuple[str, dict[str, Any] | None, str | None]:
    return _remote_curation_with_error(
        base_url,
        "/hypothesis/curation",
        {"hypothesis": str(hypothesis).strip()},
        timeout,
        selected_limit,
    )
