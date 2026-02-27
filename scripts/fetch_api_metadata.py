#!/usr/bin/env python3
"""fetch_api_metadata.py

Fetches language metadata from the Common Voice APIs and produces a single
snapshot file with implementation IDs stripped.

Two endpoints are fetched:
    1. SCS languagedata — all locale metadata (names, variants, accents)
    2. SPS locales — contributable locale codes for Spontaneous Speech

The snapshot is the single source of truth for language names, text
direction, variants, predefined accents, and SPS locale lists used by
compile_datasheets.py.

Usage:
    python scripts/fetch_api_metadata.py
    python scripts/fetch_api_metadata.py --scs-url URL --sps-url URL
"""

from __future__ import annotations

import json
import sys
import urllib.request
from datetime import UTC, datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DEFAULT_SCS_URL = "https://commonvoice.mozilla.org/api/v1/languagedata"
DEFAULT_SPS_URL = (
    "https://commonvoice.mozilla.org/spontaneous-speech/beta/api/v1/locales"
)

REPO_ROOT = Path(__file__).resolve().parent.parent
METADATA_DIR = REPO_ROOT / "metadata"
SNAPSHOTS_DIR = METADATA_DIR / "api-snapshots"

# ---------------------------------------------------------------------------
# Fetch
# ---------------------------------------------------------------------------


def fetch_json(url: str) -> dict | list:
    """Fetch a JSON endpoint."""
    print(f"Fetching {url} ...")
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


# ---------------------------------------------------------------------------
# Process
# ---------------------------------------------------------------------------


def clean_locale(entry: dict) -> dict:
    """Strip implementation-dependent IDs, keep meaningful fields."""
    variants = [
        {"code": v["code"], "name": v["name"]}
        for v in entry.get("variants", [])
    ]
    accents = [
        {"code": a["code"], "name": a["name"]}
        for a in entry.get("predefined_accents", [])
    ]
    return {
        "code": entry.get("code", ""),
        "english_name": entry.get("english_name", ""),
        "native_name": entry.get("native_name", ""),
        "text_direction": entry.get("text_direction", "LTR"),
        "is_contributable": entry.get("is_contributable", 0),
        "is_translated": entry.get("is_translated", 0),
        "target_sentence_count": entry.get("target_sentence_count", 0),
        "variants": variants,
        "predefined_accents": accents,
    }


def build_snapshot(
    scs_raw: list[dict],
    sps_data: dict,
    scs_url: str,
    sps_url: str,
    fetched_at: str,
) -> dict:
    """Build the snapshot from SCS + SPS API data."""
    # Process SCS locales
    locales: dict[str, dict] = {}
    for entry in sorted(scs_raw, key=lambda e: e.get("code", "")):
        code = entry.get("code", "")
        if not code:
            continue
        locales[code] = clean_locale(entry)

    contributable = sum(
        1 for v in locales.values() if v.get("is_contributable") == 1
    )

    # Extract SPS locale lists
    sps_locales = sps_data.get("locales", {})
    sps_contributable = sorted(sps_locales.get("contributable", []))

    return {
        "_metadata": {
            "fetched_at": fetched_at,
            "scs_api_url": scs_url,
            "sps_api_url": sps_url,
            "total_locales": len(locales),
            "contributable_locales": contributable,
            "sps_contributable_locales": len(sps_contributable),
        },
        "locales": locales,
        "sps_locales": sps_contributable,
    }


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------


def print_summary(snapshot: dict) -> None:
    """Print a summary of the snapshot."""
    locales = snapshot["locales"]
    meta = snapshot["_metadata"]
    contributable = meta.get("contributable_locales", 0)
    sps_count = meta.get("sps_contributable_locales", 0)
    with_variants = sum(1 for v in locales.values() if v.get("variants"))
    with_accents = sum(
        1 for v in locales.values() if v.get("predefined_accents")
    )
    rtl_count = sum(
        1 for v in locales.values() if v.get("text_direction") == "RTL"
    )
    missing_native = sum(
        1 for v in locales.values() if not v.get("native_name")
    )

    print("\nSummary:")
    print(f"  Total locales (SCS):   {len(locales)}")
    print(f"  SCS contributable:     {contributable}")
    print(f"  SPS contributable:     {sps_count}")
    print(f"  With variants:         {with_variants}")
    print(f"  With accents:          {with_accents}")
    print(f"  RTL:                   {rtl_count}")
    if missing_native:
        print(f"  Missing native_name:   {missing_native}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    args = sys.argv[1:]

    scs_url = DEFAULT_SCS_URL
    sps_url = DEFAULT_SPS_URL

    i = 0
    while i < len(args):
        if args[i] == "--scs-url" and i + 1 < len(args):
            scs_url = args[i + 1]
            i += 2
        elif args[i] == "--sps-url" and i + 1 < len(args):
            sps_url = args[i + 1]
            i += 2
        elif args[i] in ("-h", "--help"):
            print((__doc__ or "").strip())
            sys.exit(0)
        else:
            print(f"Unknown option: {args[i]}", file=sys.stderr)
            sys.exit(1)

    SNAPSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(UTC)
    timestamp = now.strftime("%Y%m%d")
    fetched_at = now.isoformat()

    # --- Fetch SCS languagedata ---
    scs_raw = fetch_json(scs_url)
    print(f"  SCS: {len(scs_raw)} locales")

    # --- Fetch SPS locales ---
    sps_data = fetch_json(sps_url)
    sps_contributable = sps_data.get("locales", {}).get("contributable", [])
    print(f"  SPS: {len(sps_contributable)} contributable locales")

    # --- Build and save snapshot ---
    snapshot = build_snapshot(scs_raw, sps_data, scs_url, sps_url, fetched_at)

    snapshot_path = SNAPSHOTS_DIR / f"languagedata-{timestamp}.json"
    with open(snapshot_path, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=2, ensure_ascii=False)
    print(f"  Snapshot: {snapshot_path}")

    # --- Summary ---
    print_summary(snapshot)

    print("\nDone.")


if __name__ == "__main__":
    main()
