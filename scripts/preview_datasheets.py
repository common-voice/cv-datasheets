#!/usr/bin/env python3
"""preview_datasheets.py

Preview datasheets by compiling directly from the working tree and
substituting {{KEY}} bundler placeholders with dummy data.

Each locale + modality combination produces a separate file in previews/ like:
  previews/preview-{locale}-{modality}.md

This lets contributors preview how their community content will look
in the final datasheet without needing real bundler statistics.
Works both locally and in GitHub Actions.

Usage:
    python scripts/preview_datasheets.py --locale CODE [CODE ...]
    python scripts/preview_datasheets.py --changed

Options:
    --locale, -l CODE [CODE ...]  One or more locale codes to preview
    --changed                     Auto-detect changed locales from git diff against main

Examples:
    python scripts/preview_datasheets.py -l ady
    python scripts/preview_datasheets.py -l ady kbd es
    python scripts/preview_datasheets.py --changed
"""

from __future__ import annotations

import io
import json
import re
import subprocess
import sys
from contextlib import redirect_stdout
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PREVIEWS_DIR = REPO_ROOT / "previews"

# Add repo root to path so we can import from compile_datasheets
sys.path.insert(0, str(REPO_ROOT))
import compile_datasheets as compiler  # noqa: E402

# ---------------------------------------------------------------------------
# Dummy data for {{KEY}} placeholders
# ---------------------------------------------------------------------------

DUMMY_STATS = {
    "VERSION": "99.0-preview",
    "CLIPS": "99,999",
    "HOURS_RECORDED": "1,234.56",
    "HOURS_VALIDATED": "987.65",
    "SPEAKERS": "4,567",
    "TOTAL_SENTENCES": "12,345",
    "AVG_DURATION_SECS": "5.2",
    "VALIDATED_CLIPS": "88,888",
    "INVALIDATED_CLIPS": "5,555",
    "OTHER_CLIPS": "5,556",
    "VALIDATED_SENTENCES": "10,000",
    "UNVALIDATED_SENTENCES": "2,345",
    "REJECTED_SENTENCES": "500",
    "PENDING_SENTENCES": "1,845",
    "REPORTED_SENTENCES": "100",
}

# -- SCS dummy tables (match real bundler output format) --

DUMMY_GENDER_TABLE_SCS = """\
| Code | Gender | Clips | Speakers |
|---|---|---:|---:|
| male_masculine | Male, masculine | ? | ? |
| female_feminine | Female, feminine | ? | ? |
| transgender | Transgender | ? | ? |
| non-binary | Non-binary | ? | ? |
| do_not_wish_to_say | Prefer not to say | ? | ? |
| - | Unspecified | ? | ? |

*Gender declared: ? of ? clips (?%), ? of ? speakers (?%)*"""

DUMMY_AGE_TABLE_SCS = """\
| Code | Age | Clips | Speakers |
|---|---|---:|---:|
| teens | Teens | ? | ? |
| twenties | Twenties | ? | ? |
| thirties | Thirties | ? | ? |
| fourties | Fourties | ? | ? |
| fifties | Fifties | ? | ? |
| sixties | Sixties | ? | ? |
| seventies | Seventies | ? | ? |
| eighties | Eighties | ? | ? |
| nineties | Nineties | ? | ? |
| - | Unspecified | ? | ? |

*Age declared: ? of ? clips (?%), ? of ? speakers (?%)*"""

DUMMY_DATA_SPLITS_TABLE_SCS = """\
**Clip buckets**

| Bucket | Clips |
|---|---:|
| Validated | ? |
| Invalidated | ? |
| Other | ? |

**Training splits**

| Split | Clips |
|---|---:|
| Train | ? |
| Dev | ? |
| Test | ? |

*Training split coverage: ? of ? validated clips (?%)*"""

# -- SPS dummy tables (match real bundler output format) --

DUMMY_DATA_SPLITS_TABLE_SPS = """\
### Audio clips

| Bucket | Clips | % |
| --- | ---: | ---: |
| Transcribed & Validated | ? | ? |
| Transcribed & Pending | ? | ? |
| Not transcribed | ? | ? |

### Training splits

| Bucket | Clips | % |
| --- | ---: | ---: |
| Train | ? | ? |
| Dev | ? | ? |
| Test | ? | ? |
| Unassigned | ? | ? |

Training split coverage: ? of ? transcribed & validated clips (?%)"""

DUMMY_TRANSCRIPTION_STATS = """\
### Transcription status

| Bucket | Clips | % |
| --- | ---: | ---: |
| Validated | ? | ? |
| Pending | ? | ? |
| Edited | ? | ? |"""

# -- SCS text corpus dummy tables --

DUMMY_TEXT_CORPUS_STATS = """\
**Validated sentences:** ?

| Category | Count |
|---|---:|
| Unvalidated sentences | ? |
| Pending sentences | ? |
| Rejected sentences | ? |
| Reported sentences | ? |"""

DUMMY_SOURCES_STATS = """\
| Source | Sentences |
|---|---:|
| ? | ? |"""

DUMMY_SENTENCES_SAMPLE = """\
1. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
2. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
3. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.
4. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum.
5. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia."""

DUMMY_QUESTIONS_SAMPLE = """\
1. *What is your favorite thing about your city?*
2. *Can you describe a memorable experience from your childhood?*
3. *What do you think about the current state of public transportation?*
4. *How would you explain your job to a five-year-old?*
5. *What changes would you like to see in your community?*"""

DUMMY_TRANSCRIPTIONS_SAMPLE = """\
1. *I think the most important thing is that we all work together as a community and support each other.*
2. *When I was growing up we used to walk to school every morning rain or shine.*
3. *The bus system here is actually pretty good compared to other cities I have lived in.*
4. *Well I basically help people fix their computers when things go wrong.*
5. *I would love to see more green spaces and parks for children to play in.*"""

# Shared auto fields (modality-independent)
_DUMMY_AUTO_SHARED = {
    "SENTENCES_SAMPLE": DUMMY_SENTENCES_SAMPLE,
    "QUESTIONS_SAMPLE": DUMMY_QUESTIONS_SAMPLE,
    "TRANSCRIPTIONS_SAMPLE": DUMMY_TRANSCRIPTIONS_SAMPLE,
    "VARIANT_STATS": "",
    "ACCENT_STATS": "",
    "TEXT_DOMAIN_STATS": "",
}

# SCS-specific auto fields
DUMMY_AUTO_FIELDS_SCS = {
    **_DUMMY_AUTO_SHARED,
    "GENDER_TABLE": DUMMY_GENDER_TABLE_SCS,
    "AGE_TABLE": DUMMY_AGE_TABLE_SCS,
    "DATA_SPLITS_TABLE": DUMMY_DATA_SPLITS_TABLE_SCS,
    "TEXT_CORPUS_STATS": DUMMY_TEXT_CORPUS_STATS,
    "SOURCES_STATS": DUMMY_SOURCES_STATS,
    "TRANSCRIPTION_STATS": "",
}

# SPS-specific auto fields
DUMMY_AUTO_FIELDS_SPS = {
    **_DUMMY_AUTO_SHARED,
    "GENDER_TABLE": "",
    "AGE_TABLE": "",
    "DATA_SPLITS_TABLE": DUMMY_DATA_SPLITS_TABLE_SPS,
    "TEXT_CORPUS_STATS": "",
    "SOURCES_STATS": "",
    "TRANSCRIPTION_STATS": DUMMY_TRANSCRIPTION_STATS,
}


# ---------------------------------------------------------------------------
# Post-render cleanup (emulates bundler behaviour)
# ---------------------------------------------------------------------------


def _heading_level(line: str) -> int:
    """Return the heading level (1-6) or 0 if not a heading."""
    stripped = line.lstrip()
    if not stripped.startswith("#"):
        return 0
    hashes = 0
    for ch in stripped:
        if ch == "#":
            hashes += 1
        else:
            break
    # Must be followed by a space to be a valid heading
    if hashes <= 6 and len(stripped) > hashes and stripped[hashes] == " ":
        return hashes
    return 0


def clean_rendered_markdown(text: str) -> str:
    """Strip empty sections and excessive blank lines like the bundlers.

    An empty section is a heading followed by only blank lines until the
    next heading of the same or higher level (or EOF). Empty sections are
    removed iteratively bottom-up so that parent sections with only empty
    children are also stripped.
    """
    # Iteratively strip empty sections until stable
    changed = True
    while changed:
        changed = False
        lines = text.split("\n")
        keep = [True] * len(lines)

        for i, line in enumerate(lines):
            level = _heading_level(line)
            if level == 0:
                continue

            # Scan forward: is there any non-blank, non-heading content
            # before the next heading of same/higher level (or EOF)?
            has_content = False
            j = i + 1
            while j < len(lines):
                jlevel = _heading_level(lines[j])
                if jlevel > 0 and jlevel <= level:
                    # Hit a same/higher-level heading -> section boundary
                    break
                if lines[j].strip():
                    # Non-blank, non-heading content found
                    if jlevel > 0:
                        # It's a sub-heading, keep scanning for real content
                        j += 1
                        continue
                    has_content = True
                    break
                j += 1

            if not has_content:
                # Mark the heading and trailing blank lines for removal
                keep[i] = False
                for k in range(i + 1, j):
                    if lines[k].strip() == "" or _heading_level(lines[k]) > level:
                        keep[k] = False
                changed = True

        text = "\n".join(line for line, k in zip(lines, keep) if k)

    # Collapse 3+ consecutive blank lines to 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Ensure single trailing newline
    text = text.strip() + "\n"

    return text


# ---------------------------------------------------------------------------
# Working tree compilation (single locale)
# ---------------------------------------------------------------------------


CACHED_SNAPSHOT_PATH = PREVIEWS_DIR / ".api-snapshot.json"

# Import fetch helpers from sibling script
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import fetch_api_metadata as fetcher  # noqa: E402


def fetch_api_snapshot_live() -> dict | None:
    """Fetch a fresh API snapshot from the Common Voice APIs.

    Returns the snapshot dict, or None if the API is unreachable.
    """
    try:
        print("  Fetching from SCS API...", file=sys.stderr)
        with redirect_stdout(io.StringIO()):
            scs_raw: list[dict] = fetcher.fetch_json(fetcher.DEFAULT_SCS_URL)  # type: ignore[assignment]
        print("  Fetching from SPS API...", file=sys.stderr)
        with redirect_stdout(io.StringIO()):
            sps_data: dict = fetcher.fetch_json(fetcher.DEFAULT_SPS_URL)  # type: ignore[assignment]
    except Exception as exc:
        print(f"  API fetch failed: {exc}", file=sys.stderr)
        return None

    from datetime import UTC, datetime

    snapshot = fetcher.build_snapshot(
        scs_raw,
        sps_data,
        fetcher.DEFAULT_SCS_URL,
        fetcher.DEFAULT_SPS_URL,
        datetime.now(UTC).isoformat(),
    )
    return snapshot


def load_api_snapshot() -> dict:
    """Load an API snapshot with fallback chain:

    1. Cached temp file (previews/.api-snapshot.json) if < 24h old
    2. Fresh fetch from API -> cache to temp file
    3. Latest committed snapshot in metadata/api-snapshots/
    4. Empty snapshot (locale codes used as names)
    """
    import time

    # 1. Check cached temp file (< 24h old)
    if CACHED_SNAPSHOT_PATH.exists():
        age_hours = (time.time() - CACHED_SNAPSHOT_PATH.stat().st_mtime) / 3600
        if age_hours < 24:
            print(f"  Using cached snapshot ({age_hours:.1f}h old)", file=sys.stderr)
            with open(CACHED_SNAPSHOT_PATH, encoding="utf-8") as f:
                return json.load(f)
        else:
            print(f"  Cached snapshot expired ({age_hours:.0f}h old)", file=sys.stderr)

    # 2. Fetch fresh from API
    snapshot = fetch_api_snapshot_live()
    if snapshot:
        PREVIEWS_DIR.mkdir(parents=True, exist_ok=True)
        with open(CACHED_SNAPSHOT_PATH, "w", encoding="utf-8") as f:
            json.dump(snapshot, f, ensure_ascii=False)
        locales = snapshot.get("locales", {})
        print(f"  Fetched {len(locales)} locales, cached to {CACHED_SNAPSHOT_PATH.name}", file=sys.stderr)
        return snapshot

    # 3. Fall back to latest committed snapshot
    snapshots_dir = compiler.METADATA_DIR / "api-snapshots"
    snapshots = sorted(snapshots_dir.glob("languagedata-*.json"))
    if snapshots:
        fallback = snapshots[-1]
        print(f"  Falling back to committed snapshot: {fallback.name}", file=sys.stderr)
        with redirect_stdout(io.StringIO()):
            return compiler.load_api_snapshot(fallback)

    # 4. Empty snapshot (last resort)
    print("  WARNING: No API snapshot available. Using empty snapshot.", file=sys.stderr)
    return {"locales": {}, "sps_locales": []}


def build_accent_stats_table(api_locale_data: dict | None) -> str:
    """Build a dummy accent stats table from API predefined_accents."""
    if not api_locale_data:
        return ""
    accents = api_locale_data.get("predefined_accents", [])
    if not accents:
        return ""

    lines = ["| Code | Accent | Clips | Speakers |", "|---|---|---:|---:|"]
    for acc in accents:
        code = acc.get("code", "")
        name = acc.get("name", "")
        lines.append(f"| {code} | {name} | ? | ? |")
    lines.append("| - | Other | ? | ? |")
    return "\n".join(lines)


def build_variant_stats_table(api_locale_data: dict | None) -> str:
    """Build a dummy variant stats table from API variants."""
    if not api_locale_data:
        return ""
    variants = api_locale_data.get("variants", [])
    if not variants:
        return ""

    lines = ["| Code | Variant | Clips | Speakers |", "|---|---|---:|---:|"]
    for var in variants:
        code = var.get("code", "")
        name = var.get("name", "")
        lines.append(f"| {code} | {name} | ? | ? |")
    return "\n".join(lines)


def compile_locale_from_tree(
    locale: str,
    api_snapshot: dict,
    template_langs: dict[str, str],
    funding: dict[str, str],
    sps_locales: set[str],
    field_map: dict,
    templates: dict[str, dict[str, str]],
) -> list[tuple[str, str, str]]:
    """Compile a single locale from the working tree.

    Returns list of (locale, modality, rendered_template) for each modality
    where the locale exists.
    """
    api_locales = api_snapshot.get("locales", {})
    modality_fields_config = field_map.get("modality_fields", {})
    results: list[tuple[str, str, str]] = []

    for mod_short, modality_dir in compiler.MODALITY_MAP.items():
        # Check if locale exists in this modality
        if mod_short == "scs":
            if locale not in api_locales:
                continue
        else:
            if locale not in sps_locales:
                continue

        template_lang = template_langs.get(locale, "en")
        api_locale_data = api_locales.get(locale)

        # Get template
        mod_templates = templates.get(mod_short, {})
        template = mod_templates.get(template_lang) or mod_templates.get("en", "")
        if not template:
            continue

        # Metadata
        metadata_native = ""
        metadata_english = ""
        if api_locale_data:
            metadata_native = api_locale_data.get("native_name", "")
            metadata_english = api_locale_data.get("english_name", "")

        # Load community fields from working tree
        valid_fields = modality_fields_config.get(modality_dir, [])
        funder = funding.get(locale, "")
        community_fields = compiler.load_community_fields(
            locale,
            mod_short,
            modality_dir,
            template_lang,
            field_map,
            valid_fields,
            funder=funder,
        )

        # Build substitution map
        subs: dict[str, str] = {}
        subs["NATIVE_NAME"] = metadata_native or locale
        subs["ENGLISH_NAME"] = metadata_english or locale
        subs["LOCALE"] = locale
        subs.update(DUMMY_STATS)

        if mod_short == "sps":
            subs.update(DUMMY_AUTO_FIELDS_SPS)
        else:
            subs.update(DUMMY_AUTO_FIELDS_SCS)

        # Generate accent/variant stats tables from API data
        subs["ACCENT_STATS"] = build_accent_stats_table(api_locale_data)
        subs["VARIANT_STATS"] = build_variant_stats_table(api_locale_data)

        # Community fields (from working tree)
        for key, value in community_fields.items():
            subs[key.upper()] = value

        # Substitute all {{KEY}} placeholders
        result = template
        for key, value in subs.items():
            result = result.replace("{{" + key + "}}", value)

        # Replace any remaining {{KEY}} with a placeholder notice
        result = re.sub(r"\{\{([A-Z_]+)\}\}", r"*(placeholder: \1)*", result)

        # Post-render cleanup: strip empty sections, collapse blank lines
        result = clean_rendered_markdown(result)

        # Add disclaimer at the top
        from datetime import UTC, datetime

        timestamp = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")
        disclaimer = (
            f"> **Preview** - This is a preview with dummy numeric data. "
            f"Tables marked with `?` will be filled by the bundler at release time. "
            f"Generated: {timestamp}\n"
        )
        result = disclaimer + "\n" + result

        results.append((locale, mod_short, result))

    return results


# ---------------------------------------------------------------------------
# Changed locale detection
# ---------------------------------------------------------------------------


def _git_diff_names(path: str = "") -> list[str]:
    """Get changed file names from git diff against main."""
    cmd = ["git", "diff", "--name-only", "main"]
    if path:
        cmd += ["--", path]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return [l for l in result.stdout.strip().splitlines() if l]
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []


def _detect_template_lang_changes() -> set[str]:
    """Detect locales affected by template-languages.json changes.

    Compares current vs main version of the file and returns locale codes
    whose template language mapping was added, removed, or changed.
    """
    changed_files = _git_diff_names("metadata/template-languages.json")
    if not changed_files:
        return set()

    # Load current version
    current: dict[str, str] = {}
    tl_path = compiler.TEMPLATE_LANGS_PATH
    if tl_path.exists():
        with open(tl_path, encoding="utf-8") as f:
            current = json.load(f)
        current.pop("_comment", None)

    # Load main version
    previous: dict[str, str] = {}
    try:
        result = subprocess.run(
            ["git", "show", "main:metadata/template-languages.json"],
            capture_output=True, text=True, check=True,
        )
        previous = json.load(__import__("io").StringIO(result.stdout))
        previous.pop("_comment", None)
    except (subprocess.CalledProcessError, json.JSONDecodeError):
        pass

    # Find locales with changed mappings
    all_locales = set(current.keys()) | set(previous.keys())
    changed = set()
    for loc in all_locales:
        if current.get(loc) != previous.get(loc):
            changed.add(loc)

    return changed


def detect_changed_locales() -> tuple[list[str], list[str]]:
    """Detect changed locales from git diff against main.

    Returns:
        (content_locales, metadata_locales) - deduplicated locale code lists.
        content_locales: locales with changed content files.
        metadata_locales: locales affected by template-languages.json changes.
    """
    content_locales: set[str] = set()

    for line in _git_diff_names("content/locales/"):
        # content/locales/{locale}/{modality_dir}/...
        parts = Path(line).parts
        if len(parts) < 4 or parts[0] != "content" or parts[1] != "locales":
            continue
        content_locales.add(parts[2])

    metadata_locales = _detect_template_lang_changes()

    return sorted(content_locales), sorted(metadata_locales)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    """
    Parses command-line arguments to preview rendered templates for
    specified or changed locales, loading metadata and writing output files
    to the previews directory. Displays help or error messages as needed.
    """
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print((__doc__ or "").strip())
        sys.exit(0)

    locales: list[str] = []
    changed = False

    i = 0
    while i < len(args):
        if args[i] in ("--locale", "-l") and i + 1 < len(args):
            i += 1
            # Consume all following args that don't start with --
            while i < len(args) and not args[i].startswith("-"):
                locales.append(args[i])
                i += 1
        elif args[i] == "--changed":
            changed = True
            i += 1
        else:
            print(f"Unknown option: {args[i]}", file=sys.stderr)
            sys.exit(1)

    # Load shared data once
    print("Loading API snapshot...", file=sys.stderr)
    api_snapshot = load_api_snapshot()
    with redirect_stdout(io.StringIO()):
        template_langs, funding, sps_locales = compiler.load_metadata(api_snapshot)

    with open(compiler.FIELD_MAP_PATH, encoding="utf-8") as f:
        field_map = json.load(f)

    print("Rendering templates...", file=sys.stderr)
    with redirect_stdout(io.StringIO()):
        templates = compiler.render_templates(field_map)

    # Determine what to preview
    locales_to_preview: list[str] = []

    if changed:
        content_locales, metadata_locales = detect_changed_locales()
        # Merge both lists, deduplicated
        all_changed = list(dict.fromkeys(content_locales + metadata_locales))
        if not all_changed:
            print("No changed locales detected (compared to main).")
            sys.exit(0)
        locales_to_preview = all_changed
        if content_locales:
            print(
                f"\nContent changes: {', '.join(content_locales)}",
                file=sys.stderr,
            )
        if metadata_locales:
            print(
                f"Template language remapped: {', '.join(metadata_locales)}",
                file=sys.stderr,
            )
    elif locales:
        locales_to_preview = locales
    else:
        print("Error: Specify --locale CODE [CODE ...] or --changed.", file=sys.stderr)
        sys.exit(1)

    # Compile and write previews
    PREVIEWS_DIR.mkdir(parents=True, exist_ok=True)
    total = 0

    print(file=sys.stderr)
    for loc in locales_to_preview:
        results = compile_locale_from_tree(
            loc,
            api_snapshot,
            template_langs,
            funding,
            sps_locales,
            field_map,
            templates,
        )
        if not results:
            print(f"  {loc}: not found in any modality, skipping", file=sys.stderr)
            continue
        for _, mod, rendered in results:
            filename = f"preview-{loc}-{mod}.md"
            filepath = PREVIEWS_DIR / filename
            filepath.write_text(rendered + "\n", encoding="utf-8")
            print(f"  {loc} ({mod.upper()}): {filepath}", file=sys.stderr)
            total += 1

    print(f"\n{total} preview(s) written to {PREVIEWS_DIR}/", file=sys.stderr)


if __name__ == "__main__":
    main()
