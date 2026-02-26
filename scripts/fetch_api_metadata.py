#!/usr/bin/env python3
"""fetch_api_metadata.py

Fetches language metadata from the Common Voice API and produces two
snapshot files:

    1. Raw snapshot  — exact API response (archival)
    2. Cleaned snapshot — filtered to contributable locales, IDs stripped

The cleaned snapshot is the single source of truth for language names,
text direction, variants, and predefined accents used by
compile_datasheets.py.

Usage:
    python scripts/fetch_api_metadata.py
    python scripts/fetch_api_metadata.py --api-url https://example.com/api/v1/languagedata
"""

from __future__ import annotations

import csv
import json
import sys
import urllib.request
from datetime import UTC, datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DEFAULT_API_URL = "https://commonvoice.mozilla.org/api/v1/languagedata"

REPO_ROOT = Path(__file__).resolve().parent.parent
METADATA_DIR = REPO_ROOT / "metadata"
SNAPSHOTS_DIR = METADATA_DIR / "api-snapshots"
DS_LANGS_PATH = METADATA_DIR / "datasheet-languages.tsv"

# ---------------------------------------------------------------------------
# Fetch
# ---------------------------------------------------------------------------


def fetch_api(url: str) -> list[dict]:
    """Fetch the languagedata API endpoint."""
    print(f"Fetching {url} ...")
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    print(f"  Received {len(data)} locales")
    return data


# ---------------------------------------------------------------------------
# Clean
# ---------------------------------------------------------------------------


def clean_locale(entry: dict) -> dict:
    """Strip implementation-dependent IDs, keep meaningful fields."""
    variants = [
        {"code": v["code"], "name": v["name"]} for v in entry.get("variants", [])
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
        "is_translated": entry.get("is_translated", 0),
        "target_sentence_count": entry.get("target_sentence_count", 0),
        "variants": variants,
        "predefined_accents": accents,
    }


def build_cleaned(raw_data: list[dict], api_url: str, fetched_at: str) -> dict:
    """Build the cleaned snapshot from raw API data."""
    contributable = [e for e in raw_data if e.get("is_contributable") == 1]

    locales: dict[str, dict] = {}
    for entry in sorted(contributable, key=lambda e: e.get("code", "")):
        code = entry.get("code", "")
        if not code:
            continue
        locales[code] = clean_locale(entry)

    return {
        "_metadata": {
            "fetched_at": fetched_at,
            "api_url": api_url,
            "total_locales": len(raw_data),
            "contributable_locales": len(locales),
        },
        "locales": locales,
    }


# ---------------------------------------------------------------------------
# Consistency checks
# ---------------------------------------------------------------------------


def check_consistency(cleaned: dict) -> None:
    """Compare cleaned snapshot against datasheet-languages.tsv."""
    if not DS_LANGS_PATH.exists():
        print("\n  [SKIP] datasheet-languages.tsv not found, skipping checks")
        return

    api_codes = set(cleaned["locales"].keys())

    # Load datasheet-languages.tsv with modality info
    ds_codes: set[str] = set()
    scs_codes: set[str] = set()
    sps_only_codes: set[str] = set()
    with open(DS_LANGS_PATH, newline="", encoding="utf-8") as f:
        locale_mods: dict[str, set[str]] = {}
        for row in csv.DictReader(f, delimiter="\t"):
            code = row["code"]
            ds_codes.add(code)
            locale_mods.setdefault(code, set()).add(row["modality"])
    for code, mods in locale_mods.items():
        if "scs" in mods:
            scs_codes.add(code)
        if mods == {"sps"}:
            sps_only_codes.add(code)

    in_api_not_ds = sorted(api_codes - ds_codes)
    in_ds_not_api = sorted(ds_codes - api_codes)

    # Separate SPS-only from genuinely missing SCS locales
    sps_only_missing = sorted(sps_only_codes & set(in_ds_not_api))
    scs_missing = sorted(set(in_ds_not_api) - sps_only_codes)

    print(f"\n  API contributable: {len(api_codes)}")
    print(f"  datasheet-languages.tsv: {len(ds_codes)} (unique codes)")
    print(f"    SCS: {len(scs_codes)}, SPS-only: {len(sps_only_codes)}")

    if in_api_not_ds:
        print(
            f"  [INFO] {len(in_api_not_ds)} contributable locales not in "
            f"datasheet-languages.tsv:"
        )
        for i in range(0, len(in_api_not_ds), 10):
            chunk = in_api_not_ds[i : i + 10]
            print(f"         {', '.join(chunk)}")
    if scs_missing:
        print(
            f"  [WARN] {len(scs_missing)} SCS locales in "
            f"datasheet-languages.tsv but not in API:"
        )
        for code in scs_missing:
            print(f"         {code}")
    if sps_only_missing:
        print(
            f"  [INFO] {len(sps_only_missing)} SPS-only locales "
            f"(not expected in SCS API)"
        )
    if not in_api_not_ds and not in_ds_not_api:
        print("  All locales match.")


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------


def print_summary(cleaned: dict) -> None:
    """Print a summary of the cleaned snapshot."""
    locales = cleaned["locales"]
    with_variants = sum(1 for v in locales.values() if v.get("variants"))
    with_accents = sum(1 for v in locales.values() if v.get("predefined_accents"))
    rtl_count = sum(1 for v in locales.values() if v.get("text_direction") == "RTL")
    missing_native = sum(1 for v in locales.values() if not v.get("native_name"))

    print("\nSummary:")
    print(f"  Contributable locales: {len(locales)}")
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

    api_url = DEFAULT_API_URL

    i = 0
    while i < len(args):
        if args[i] == "--api-url" and i + 1 < len(args):
            api_url = args[i + 1]
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

    # --- Fetch and save raw snapshot ---
    raw_data = fetch_api(api_url)

    raw_path = SNAPSHOTS_DIR / f"languagedata-{timestamp}-raw.json"
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(raw_data, f, indent=2, ensure_ascii=False)
    print(f"  Raw snapshot: {raw_path}")

    # --- Build and save cleaned snapshot ---
    cleaned = build_cleaned(raw_data, api_url, fetched_at)

    cleaned_path = SNAPSHOTS_DIR / f"languagedata-{timestamp}.json"
    with open(cleaned_path, "w", encoding="utf-8") as f:
        json.dump(cleaned, f, indent=2, ensure_ascii=False)
    print(f"  Cleaned snapshot: {cleaned_path}")

    # --- Summary and checks ---
    print_summary(cleaned)
    check_consistency(cleaned)

    print("\nDone.")


if __name__ == "__main__":
    main()
