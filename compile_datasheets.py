#!/usr/bin/env python3
"""compile_datasheets.py

Compiles Jinja2 templates, atomized community content, and metadata into
a single datasheets JSON file for consumption by the bundler.

Inputs:
    templates/*.j2          Jinja2 templates (base + child per modality)
    templates/i18n/*.json   Localized strings per template language
    content/locales/        Atomized community content per locale
    content/_defaults/      Fallback content per template language
    content/_field_map.json Field-to-key mapping
    metadata/               Language names, funding, template language mapping

Output:
    releases/datasheets-{version}.json

Usage:
    python compile_datasheets.py <version> --api-snapshot PATH
                                           [--output PATH] [--pretty]
                                           [--diff PREVIOUS_JSON]

    Example:
        python compile_datasheets.py 24.0-2025-12-05 --api-snapshot metadata/api-snapshots/languagedata-20260226.json
        python compile_datasheets.py 24.0-2025-12-05 --api-snapshot metadata/api-snapshots/languagedata-20260226.json --diff releases/datasheets-23.0-2025-09-05.json
"""

from __future__ import annotations

import csv
import json
import re
import sys
from datetime import UTC, datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SCHEMA_VERSION = "2.0.0"

REPO_ROOT = Path(__file__).resolve().parent
TEMPLATES_DIR = REPO_ROOT / "templates"
I18N_DIR = TEMPLATES_DIR / "i18n"
CONTENT_DIR = REPO_ROOT / "content"
FIELD_MAP_PATH = CONTENT_DIR / "_field_map.json"
DEFAULTS_DIR = CONTENT_DIR / "_defaults"
LOCALES_DIR = CONTENT_DIR / "locales"
METADATA_DIR = REPO_ROOT / "metadata"
LOCALE_EXTRAS_PATH = METADATA_DIR / "locale-extras.json"
TEMPLATE_LANGS_PATH = METADATA_DIR / "template-languages.json"
SPS_LOCALES_PATH = METADATA_DIR / "sps-locales.json"

MODALITY_MAP = {"scs": "scripted", "sps": "spontaneous"}
TEMPLATE_FILE = {"scs": "scripted.md.j2", "sps": "spontaneous.md.j2"}

# Template variable names that differ from field_map field names
TEMPLATE_VAR_ALIASES = {"text_corpus": "corpus"}

# OMSF funding text per template language — injected at compile time
# only for locales listed in metadata/funding.tsv.
OMSF_FUNDING_TEXT = {
    "en": (
        "This dataset was partially funded by the "
        "*Open Multilingual Speech Fund* managed by Mozilla Common Voice."
    ),
    "es": (
        "Este proyecto recibió financiamiento del "
        "*Open Multilingual Speech Fund* gestionado por Mozilla Common Voice."
    ),
}

# Auto-generated field placeholders (filled by bundler, not community)
AUTO_FIELDS = {
    "gender_table": "GENDER_TABLE",
    "age_table": "AGE_TABLE",
    "sentences_sample": "SENTENCES_SAMPLE",
    "questions_sample": "QUESTIONS_SAMPLE",
    "transcriptions_sample": "TRANSCRIPTIONS_SAMPLE",
    # Mergeable field stats (bundler fills these alongside community content)
    "text_corpus_stats": "TEXT_CORPUS_STATS",
    "sources_stats": "SOURCES_STATS",
    "text_domain_stats": "TEXT_DOMAIN_STATS",
    "variant_stats": "VARIANT_STATS",
    "accent_stats": "ACCENT_STATS",
    "transcription_stats": "TRANSCRIPTION_STATS",
}

# Stats header placeholders (filled by bundler)
STATS_FIELDS = {
    "native_name": "NATIVE_NAME",
    "english_name": "ENGLISH_NAME",
    "locale": "LOCALE",
}

# Header intro variable → bundler key mapping
HEADER_VAR_MAP = {
    "version": "VERSION",
    "english_name": "ENGLISH_NAME",
    "locale": "LOCALE",
    "clips": "CLIPS",
    "hours_recorded": "HOURS_RECORDED",
    "hours_validated": "HOURS_VALIDATED",
    "speakers": "SPEAKERS",
}


# ---------------------------------------------------------------------------
# Metadata loading
# ---------------------------------------------------------------------------


def read_tsv(path: Path) -> list[dict[str, str]]:
    """Read a TSV file with headers into a list of dicts."""
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def load_api_snapshot(path: Path) -> dict:
    """Load an API snapshot and merge locale-extras."""
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    locales = data.get("locales", {})
    meta = data.get("_metadata", {})
    print(f"  API snapshot: {path.name}")
    print(
        f"    {len(locales)} locales "
        f"({meta.get('contributable_locales', '?')} contributable)"
    )
    print(f"    fetched: {meta.get('fetched_at', 'unknown')}")

    # Merge locale-extras (locales not in the API, e.g. regional codes)
    if LOCALE_EXTRAS_PATH.exists():
        with open(LOCALE_EXTRAS_PATH, encoding="utf-8") as f:
            extras = json.load(f)
        extras.pop("_comment", None)
        merged = 0
        for code, entry in extras.items():
            if code not in locales:
                locales[code] = entry
                merged += 1
        if merged:
            print(f"    + {merged} from locale-extras.json")

    return data


def load_metadata(
    api_snapshot: dict,
) -> tuple[
    dict[str, str],
    dict[str, str],
    set[str],
]:
    """
    Load metadata from API snapshot and supporting files.

    Locale lists:
        SCS — all locales in the API snapshot (incl. locale-extras)
        SPS — from API snapshot's sps_locales (fetched from SPS API),
              with fallback to metadata/sps-locales.json

    Names come from the API snapshot (authoritative).
    Template language defaults to "en"; overrides in template-languages.json.

    Returns:
        template_langs: locale -> template_language (only non-"en" entries)
        funding: locale -> funder
        sps_locales: set of SPS locale codes
    """
    # Template language overrides (default is "en")
    template_langs: dict[str, str] = {}
    if TEMPLATE_LANGS_PATH.exists():
        with open(TEMPLATE_LANGS_PATH, encoding="utf-8") as f:
            data = json.load(f)
        data.pop("_comment", None)
        template_langs = data

    # Funding
    funding: dict[str, str] = {}
    funding_path = METADATA_DIR / "funding.tsv"
    if funding_path.exists():
        for row in read_tsv(funding_path):
            funding[row["locale"]] = row["funder"]

    # SPS locale list — prefer snapshot, fallback to sps-locales.json
    sps_list = api_snapshot.get("sps_locales", [])
    if sps_list:
        sps_locales = set(sps_list)
    elif SPS_LOCALES_PATH.exists():
        with open(SPS_LOCALES_PATH, encoding="utf-8") as f:
            data = json.load(f)
        sps_locales = set(data.get("locales", []))
    else:
        sps_locales = set()

    return template_langs, funding, sps_locales


# ---------------------------------------------------------------------------
# Jinja2 template rendering
# ---------------------------------------------------------------------------


def render_header_intro(intro_template: str) -> str:
    """
    Convert i18n header_intro with {variable} placeholders into
    bundler {{KEY}} markers.

    Example: "version {version} for {english_name}"
        → "version {{VERSION}} for {{ENGLISH_NAME}}"
    """
    result = intro_template
    for var_name, key in HEADER_VAR_MAP.items():
        result = result.replace("{" + var_name + "}", "{{" + key + "}}")
    return result


def build_jinja_context(
    modality_short: str,
    i18n: dict[str, str],
    field_map: dict[str, dict],
) -> dict:
    """
    Build the Jinja2 rendering context for template compilation.

    All community and auto fields become {{KEY}} bundler placeholders.
    i18n strings are rendered as literal text.
    """
    # stats.* → {{KEY}} placeholders
    stats = {name: "{{" + key + "}}" for name, key in STATS_FIELDS.items()}

    # auto.* → {{KEY}} placeholders
    auto = {name: "{{" + key + "}}" for name, key in AUTO_FIELDS.items()}

    # community.* → {{KEY}} placeholders from field_map
    community: dict[str, str] = {}
    for field_name, info in field_map["fields"].items():
        bundler_key = info["key"].upper()
        community[field_name] = "{{" + bundler_key + "}}"

    # Add aliases for template variable names that differ
    for alias, field_name in TEMPLATE_VAR_ALIASES.items():
        if field_name in community:
            community[alias] = community[field_name]

    # header_intro — pick modality-specific intro, convert {var} → {{KEY}}
    intro_key = (
        "header_intro_scs" if modality_short == "scs" else "header_intro_sps"
    )
    header_intro = render_header_intro(i18n.get(intro_key, ""))

    return {
        "stats": stats,
        "auto": auto,
        "community": community,
        "i18n": i18n,
        "header_intro": header_intro,
    }


def discover_template_langs() -> dict[str, list[str]]:
    """Discover available template languages from i18n JSON files.

    Scans templates/i18n/*.json (skipping _-prefixed files). A language
    supports a modality if its i18n file contains the header_intro key
    for that modality (header_intro_scs, header_intro_sps).
    """
    result: dict[str, list[str]] = {mod: [] for mod in MODALITY_MAP}
    for path in sorted(I18N_DIR.glob("*.json")):
        if path.name.startswith("_"):
            continue
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        lang = path.stem
        for mod_short in MODALITY_MAP:
            if f"header_intro_{mod_short}" in data:
                result[mod_short].append(lang)
    return result


def render_templates(
    field_map: dict,
) -> dict[str, dict[str, str]]:
    """
    Render all Jinja2 templates for each modality × template language.

    Languages are auto-discovered from templates/i18n/*.json files.
    Returns: { modality_short: { lang: flat_template_string } }
    """
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        keep_trailing_newline=True,
    )

    template_langs = discover_template_langs()
    templates: dict[str, dict[str, str]] = {}

    for mod_short, langs in template_langs.items():
        templates[mod_short] = {}
        template = env.get_template(TEMPLATE_FILE[mod_short])

        for lang in langs:
            i18n_path = I18N_DIR / f"{lang}.json"
            if not i18n_path.exists():
                print(f"  [WARN] Missing i18n: {i18n_path}")
                continue

            with open(i18n_path, encoding="utf-8") as f:
                i18n = json.load(f)

            ctx = build_jinja_context(mod_short, i18n, field_map)
            rendered = template.render(**ctx)

            # Clean up excessive blank lines from Jinja2 block rendering
            rendered = re.sub(r"\n{3,}", "\n\n", rendered).strip() + "\n"

            templates[mod_short][lang] = rendered
            print(f"  Rendered {mod_short}/{lang}: {len(rendered)} chars")

    return templates


# ---------------------------------------------------------------------------
# Community content loading (fallback chain)
# ---------------------------------------------------------------------------


def load_community_field(
    locale: str,
    modality_dir: str,
    field_file: str,
    template_lang: str,
) -> str:
    """
    Load a single community field using the fallback chain:
        1. content/locales/{locale}/{modality}/{field_file}
        2. content/locales/{locale}/shared/{field_file}
        3. content/_defaults/{template_lang}/{field_file}  (resolve {locale})
        4. "" (empty)
    """
    # 1. Modality-specific
    path = LOCALES_DIR / locale / modality_dir / field_file
    if path.exists():
        return path.read_text(encoding="utf-8").strip()

    # 2. Shared
    path = LOCALES_DIR / locale / "shared" / field_file
    if path.exists():
        return path.read_text(encoding="utf-8").strip()

    # 3. Default (with {locale} placeholder resolution)
    path = DEFAULTS_DIR / template_lang / field_file
    if path.exists():
        content = path.read_text(encoding="utf-8").strip()
        return content.replace("{locale}", locale)

    # Fallback to en defaults if template_lang default doesn't exist
    if template_lang != "en":
        path = DEFAULTS_DIR / "en" / field_file
        if path.exists():
            content = path.read_text(encoding="utf-8").strip()
            return content.replace("{locale}", locale)

    # 4. Empty
    return ""


def load_community_fields(
    locale: str,
    modality_short: str,
    modality_dir: str,
    template_lang: str,
    field_map: dict,
    modality_fields: list[str],
    funder: str = "",
) -> dict[str, str]:
    """
    Load all community fields for a locale using the fallback chain.

    Auto-injection rules (only when no community content exists):
    - funding: OMSF boilerplate if locale is OMSF-funded

    Returns: { bundler_key: content } for each field valid in this modality.
    """
    fields: dict[str, str] = {}

    for field_name in modality_fields:
        info = field_map["fields"].get(field_name)
        if not info:
            continue

        content = load_community_field(
            locale, modality_dir, info["file"], template_lang
        )

        # Inject OMSF funding if no community content and locale is funded
        if field_name == "funding" and not content and funder == "omsf":
            content = OMSF_FUNDING_TEXT.get(
                template_lang, OMSF_FUNDING_TEXT["en"]
            )

        fields[info["key"]] = content

    return fields


# ---------------------------------------------------------------------------
# Main compilation
# ---------------------------------------------------------------------------


def compile_datasheets(
    version: str,
    output_path: Path,
    *,
    pretty: bool = False,
    api_snapshot_path: Path,
) -> None:
    """Compile templates, community data, and metadata into JSON."""
    print(f"Compiling datasheets for version {version}...")
    print(f"Output: {output_path}\n")

    # Load field map
    with open(FIELD_MAP_PATH, encoding="utf-8") as f:
        field_map = json.load(f)

    modality_fields_config = field_map.get("modality_fields", {})

    # Load API snapshot (includes locale-extras)
    api_snapshot = load_api_snapshot(api_snapshot_path)
    api_locales = api_snapshot.get("locales", {})
    print()

    # Load metadata
    template_langs, funding, sps_locales = load_metadata(api_snapshot)

    # Render templates
    print("Rendering templates...")
    templates = render_templates(field_map)
    print()

    output = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(UTC).isoformat(),
        "source_version": version,
        "templates": templates,
        "locales": {},
    }

    for mod_short, modality_dir in MODALITY_MAP.items():
        print(f"{'=' * 50}")
        print(f"  {mod_short.upper()} ({modality_dir})")
        print(f"{'=' * 50}")

        valid_fields = modality_fields_config.get(modality_dir, [])

        # Locale list: SCS = all API locales, SPS = explicit list
        if mod_short == "scs":
            modality_locales = set(api_locales.keys())
        else:
            modality_locales = sps_locales

        print(f"  Locales: {len(modality_locales)}")

        output["locales"][mod_short] = {}
        filled_count = 0

        for locale in sorted(modality_locales):
            template_lang = template_langs.get(locale, "en")
            api_locale_data = api_locales.get(locale)

            locale_metadata: dict[str, str] = {
                "native_name": "",
                "english_name": "",
                "funding": funding.get(locale, ""),
            }

            if api_locale_data:
                locale_metadata["native_name"] = api_locale_data.get(
                    "native_name", ""
                )
                locale_metadata["english_name"] = api_locale_data.get(
                    "english_name", ""
                )
                locale_metadata["text_direction"] = api_locale_data.get(
                    "text_direction", "LTR"
                )

            funder = funding.get(locale, "")

            community_fields = load_community_fields(
                locale,
                mod_short,
                modality_dir,
                template_lang,
                field_map,
                valid_fields,
                funder=funder,
            )

            has_community = any(v for v in community_fields.values())
            if has_community:
                filled_count += 1

            output["locales"][mod_short][locale] = {
                "template_language": template_lang,
                "metadata": locale_metadata,
                "community_fields": community_fields,
            }

        total = len(output["locales"][mod_short])
        print(f"  Compiled: {total} locales ({filled_count} with content)")

    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    indent = 2 if pretty else None
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=indent, ensure_ascii=False)

    size = output_path.stat().st_size
    size_str = (
        f"{size / (1024 * 1024):.1f} MB"
        if size > 1024 * 1024
        else f"{size / 1024:.1f} KB"
    )
    print(f"\nDone. Output: {output_path} ({size_str})")

    for mod_short in MODALITY_MAP:
        tpls = len(output["templates"].get(mod_short, {}))
        locs = len(output["locales"].get(mod_short, {}))
        print(f"  {mod_short.upper()}: {tpls} templates, {locs} locales")


# ---------------------------------------------------------------------------
# Release diff
# ---------------------------------------------------------------------------

MODALITY_LABEL = {"scs": "SCS (Scripted Speech)", "sps": "SPS (Spontaneous Speech)"}


def diff_releases(current_path: Path, previous_path: Path) -> str:
    """
    Compare two compiled release JSONs and return a markdown changelog entry.

    Reports: new locales, removed locales, locales with updated community content.
    """
    with open(previous_path, encoding="utf-8") as f:
        prev = json.load(f)
    with open(current_path, encoding="utf-8") as f:
        curr = json.load(f)

    prev_version = prev.get("source_version", "unknown")
    curr_version = curr.get("source_version", "unknown")

    lines: list[str] = [
        f"## datasheets-{curr_version}",
        "",
        f"Compared against: datasheets-{prev_version}",
        "",
        "### Data",
        "",
    ]

    for mod in sorted(MODALITY_MAP.keys()):
        label = MODALITY_LABEL.get(mod, mod.upper())
        prev_locales = set(prev.get("locales", {}).get(mod, {}).keys())
        curr_locales = set(curr.get("locales", {}).get(mod, {}).keys())

        added = sorted(curr_locales - prev_locales)
        removed = sorted(prev_locales - curr_locales)
        common = sorted(prev_locales & curr_locales)

        # Find locales with changed community content
        updated: list[tuple[str, list[str]]] = []
        for loc in common:
            prev_cf = prev["locales"][mod][loc].get("community_fields", {})
            curr_cf = curr["locales"][mod][loc].get("community_fields", {})
            changed = []
            for key in sorted(set(prev_cf) | set(curr_cf)):
                pv = prev_cf.get(key, "")
                cv = curr_cf.get(key, "")
                if pv != cv:
                    changed.append(key)
            if changed:
                updated.append((loc, changed))

        lines.append(f"**{label}:** {len(curr_locales)} locales")
        lines.append("")

        if added:
            lines.append(
                f"- {len(added)} new: {', '.join(f'`{a}`' for a in added)}"
            )
        if removed:
            lines.append(
                f"- {len(removed)} removed: "
                f"{', '.join(f'`{r}`' for r in removed)}"
            )
        if updated:
            lines.append(f"- {len(updated)} updated content:")
            for loc, fields in updated:
                fields_str = ", ".join(fields)
                lines.append(f"  - `{loc}`: {fields_str}")
        if not added and not removed and not updated:
            lines.append("- No changes")

        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print((__doc__ or "").strip())
        sys.exit(0)

    version = args[0]
    releases_dir = REPO_ROOT / "releases"
    output_path = releases_dir / f"datasheets-{version}.json"
    pretty = False
    api_snapshot_path: Path | None = None
    diff_path: Path | None = None

    i = 1
    while i < len(args):
        if args[i] in ("--output", "-o") and i + 1 < len(args):
            output_path = Path(args[i + 1])
            i += 2
        elif args[i] == "--api-snapshot" and i + 1 < len(args):
            api_snapshot_path = Path(args[i + 1])
            i += 2
        elif args[i] == "--diff" and i + 1 < len(args):
            diff_path = Path(args[i + 1])
            i += 2
        elif args[i] == "--pretty":
            pretty = True
            i += 1
        else:
            print(f"Unknown option: {args[i]}", file=sys.stderr)
            sys.exit(1)

    if not api_snapshot_path:
        print(
            "Error: --api-snapshot PATH is required.\n"
            "Run: python scripts/fetch_api_metadata.py",
            file=sys.stderr,
        )
        sys.exit(1)

    compile_datasheets(
        version,
        output_path,
        pretty=pretty,
        api_snapshot_path=api_snapshot_path,
    )

    if diff_path:
        if not diff_path.exists():
            print(f"\n[WARN] Diff file not found: {diff_path}", file=sys.stderr)
        else:
            changelog = diff_releases(output_path, diff_path)
            print(f"\n{'=' * 50}")
            print("  CHANGELOG ENTRY")
            print(f"{'=' * 50}\n")
            print(changelog)


if __name__ == "__main__":
    main()
