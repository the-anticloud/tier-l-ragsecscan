"""LLM Guard package"""

from .evaluate import scan_output, scan_prompt


# --- Anticloud patch: enforce declared offline posture -------------------
try:  # pragma: no cover - the guard is optional, its absence is not fatal
    from ._anticloud_egress import install as _anticloud_install
    _anticloud_install()
except Exception:  # noqa: BLE001 - never break the package on import
    pass
