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
    python compile_datasheets.py <version> [--output PATH] [--pretty]

    Example:
        python compile_datasheets.py 24.0-2025-12-05
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

MODALITY_MAP = {"scs": "scripted", "sps": "spontaneous"}
TEMPLATE_FILE = {"scs": "scripted.md.j2", "sps": "spontaneous.md.j2"}
TEMPLATE_LANGS = {"scs": ["en", "es", "zh-TW"], "sps": ["en", "es"]}

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


def load_metadata() -> tuple[
    dict[tuple[str, str], str],
    dict[str, str],
    dict[tuple[str, str], dict[str, str]],
]:
    """
    Load all metadata files.

    Returns:
        lang_map: (modality_short, code) -> template_language
        funding: locale -> funder
        names: (modality_short, code) -> {native_name, english_name}
    """
    # Template language mapping
    lang_map: dict[tuple[str, str], str] = {}
    ds_langs_path = METADATA_DIR / "datasheet-languages.tsv"
    if ds_langs_path.exists():
        for row in read_tsv(ds_langs_path):
            lang_map[(row["modality"], row["code"])] = row[
                "language_of_datasheet"
            ]

    # Funding
    funding: dict[str, str] = {}
    funding_path = METADATA_DIR / "funding.tsv"
    if funding_path.exists():
        for row in read_tsv(funding_path):
            funding[row["locale"]] = row["funder"]

    # Language names from metadata.tsv
    names: dict[tuple[str, str], dict[str, str]] = {}
    metadata_tsv = METADATA_DIR / "metadata.tsv"
    if metadata_tsv.exists():
        for row in read_tsv(metadata_tsv):
            key = (row["modality"], row["code"])
            native = row.get("native_name", "")
            english = row.get("english_name", "")
            names[key] = {
                "native_name": native if native != "_" else "",
                "english_name": english if english != "_" else "",
            }

    # Supplement from per-modality metadata.json
    for mod_short in MODALITY_MAP:
        json_path = METADATA_DIR / mod_short / "metadata.json"
        if not json_path.exists():
            continue
        with open(json_path, encoding="utf-8") as f:
            data = json.loads(f.read(), strict=False)
        for code, info in data.items():
            key = (mod_short, code)
            if key not in names:
                names[key] = {
                    "native_name": info.get("native_name", ""),
                    "english_name": info.get("english_name", ""),
                }
            else:
                if not names[key]["native_name"]:
                    names[key]["native_name"] = info.get("native_name", "")
                if not names[key]["english_name"]:
                    names[key]["english_name"] = info.get(
                        "english_name", ""
                    )

    return lang_map, funding, names


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


def render_templates(
    field_map: dict,
) -> dict[str, dict[str, str]]:
    """
    Render all Jinja2 templates for each modality × template language.

    Returns: { modality_short: { lang: flat_template_string } }
    """
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        keep_trailing_newline=True,
    )

    templates: dict[str, dict[str, str]] = {}

    for mod_short, langs in TEMPLATE_LANGS.items():
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

    If the locale has OMSF funding (from metadata/funding.tsv) and no
    community-written funding content exists, the OMSF boilerplate is
    injected automatically.

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
    version: str, output_path: Path, *, pretty: bool = False
) -> None:
    """Compile templates, community data, and metadata into JSON."""
    print(f"Compiling datasheets for version {version}...")
    print(f"Output: {output_path}\n")

    # Load field map
    with open(FIELD_MAP_PATH, encoding="utf-8") as f:
        field_map = json.load(f)

    modality_fields_config = field_map.get("modality_fields", {})

    # Load metadata
    lang_map, funding, names = load_metadata()

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

        # Collect all locales for this modality
        modality_locales: set[str] = set()
        for (mod, code), _ in lang_map.items():
            if mod == mod_short:
                modality_locales.add(code)

        print(f"  Locales: {len(modality_locales)}")

        output["locales"][mod_short] = {}
        filled_count = 0

        for locale in sorted(modality_locales):
            template_lang = lang_map.get((mod_short, locale), "en")
            name_info = names.get((mod_short, locale), {})

            locale_metadata = {
                "native_name": name_info.get("native_name", ""),
                "english_name": name_info.get("english_name", ""),
                "funding": funding.get(locale, ""),
            }

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

    i = 1
    while i < len(args):
        if args[i] in ("--output", "-o") and i + 1 < len(args):
            output_path = Path(args[i + 1])
            i += 2
        elif args[i] == "--pretty":
            pretty = True
            i += 1
        else:
            print(f"Unknown option: {args[i]}", file=sys.stderr)
            sys.exit(1)

    compile_datasheets(version, output_path, pretty=pretty)


if __name__ == "__main__":
    main()
