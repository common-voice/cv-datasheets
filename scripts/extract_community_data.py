#!/usr/bin/env python3
"""
extract_community_data.py — One-time extraction of community content from
legacy cv-corpus rendered datasheets into the new atomized content/ structure.

Reads _legacy/cv-corpus/{scs,sps}/**/en/*.md (and es/, zh-TW/) and writes
individual .md files to content/locales/{locale}/{shared,scripted,spontaneous}/.

Fields classified as "language-level" (e.g. alphabet, writing_system) go to
shared/ — the best (longest) content across all modalities wins.
Modality-specific fields go to scripted/ or spontaneous/ as before.

Priority order (latest wins):
  v24 > v23/final > v23/draft

Usage:
    python3 scripts/extract_community_data.py [--dry-run]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
LEGACY_DIR = REPO_ROOT / "_legacy" / "cv-corpus"
CONTENT_DIR = REPO_ROOT / "content"
FIELD_MAP_PATH = CONTENT_DIR / "_field_map.json"
I18N_DIR = REPO_ROOT / "templates" / "i18n"

# ---------------------------------------------------------------------------
# Section-title → field-name mapping (built from i18n JSON files)
# ---------------------------------------------------------------------------

# Map from i18n key (title_xxx) to field name in _field_map.json
I18N_KEY_TO_FIELD: dict[str, str] = {
    "title_language": "description",
    "title_variants": "variants",
    "title_text_corpus": "corpus",
    "title_writing_system": "writing_system",
    "title_symbol_table": "alphabet",
    "title_sources": "sources",
    "title_text_domains": "text_domain",
    "title_processing": "processing",
    "title_postprocessing": "postprocessing",
    "title_transcriptions": "transcriptions",
    "title_community_links": "community_links",
    "title_discussions": "discussion_links",
    "title_contribute": "contribute_links",
    "title_authors": "authors",
    "title_citation": "citation",
    "title_funding": "funding",
}

# Non-standard section titles found in some locales (map to field names)
# These are titles not present in i18n but used by a few communities
EXTRA_TITLE_MAP: dict[str, str] = {
    "Curators": "authors",
    "Dataset curators": "authors",
    "Compiler": "authors",
    "Compiler / Coordinator": "authors",
    "Contact": "authors",
    "Advisors": "authors",
    "Accents": "variants",
}

# Sections to always skip (auto-generated, structural, or template-level)
SKIP_SECTIONS: set[str] = set()

# Section titles (i18n keys) that are auto-generated / structural
SKIP_I18N_KEYS: set[str] = {
    "title_demographics",
    "title_gender",
    "title_age",
    "title_data_splits",
    "title_sample",
    "title_samples",
    "title_questions",
    "title_responses",
    "title_fields",
    "title_extralinguistic_tags",
    "title_get_involved",
    "title_acknowledgements",
    "title_licence",
}


def build_title_to_field_map() -> dict[str, str]:
    """
    Build a mapping from localized section title → field name.
    Reads all i18n JSON files and maps each title string to its field.
    """
    title_map: dict[str, str] = {}

    for json_path in I18N_DIR.glob("*.json"):
        with open(json_path, encoding="utf-8") as f:
            i18n = json.load(f)

        for i18n_key, field_name in I18N_KEY_TO_FIELD.items():
            if i18n_key in i18n and i18n[i18n_key]:
                title = i18n[i18n_key].strip()
                title_map[title] = field_name

        # Also register skip titles
        for i18n_key in SKIP_I18N_KEYS:
            if i18n_key in i18n and i18n[i18n_key]:
                SKIP_SECTIONS.add(i18n[i18n_key].strip())

    # Add non-standard title mappings
    for title, field in EXTRA_TITLE_MAP.items():
        if title not in title_map:
            title_map[title] = field
        # Also try with trailing space (found in some datasheets)
        title_ws = title + " "
        if title_ws not in title_map:
            title_map[title_ws] = field

    # Handle trailing-space variants of standard titles too
    for title in list(title_map):
        title_ws = title + " "
        if title_ws not in title_map:
            title_map[title_ws] = title_map[title]

    return title_map


# ---------------------------------------------------------------------------
# Content cleaning
# ---------------------------------------------------------------------------

# Placeholder patterns that indicate empty/auto-generated content
PLACEHOLDER_PATTERNS: list[re.Pattern] = [
    re.compile(r"^\s*$"),  # whitespace-only
    re.compile(r"^>\s*This datasheet has been generated automatically"),
    re.compile(r"^\[Not provided\]", re.IGNORECASE),  # template placeholder
]

# HTML comment pattern for stripping (full and partial fragments)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
# Partial fragments from comments split across sections
# Trailing open: "<!--[Not provided]\n" at end (no closing -->)
HTML_COMMENT_OPEN_RE = re.compile(r"<!--(?:(?!-->).)*$", re.DOTALL)
# Leading close: "[Not provided]-->" at start (no opening <!--)
HTML_COMMENT_CLOSE_RE = re.compile(r"^(?:(?!<!--).)*?-->", re.DOTALL)


def clean_section_content(content: str) -> str:
    """
    Strip HTML comments and normalize whitespace.
    Returns empty string if content is only placeholders/comments.
    """
    # Strip full HTML comments
    cleaned = HTML_COMMENT_RE.sub("", content)

    # Strip partial HTML comment fragments (split across sections)
    # Opening fragment at end: "real content\n<!--[Not provided]"
    cleaned = HTML_COMMENT_OPEN_RE.sub("", cleaned)
    # Closing fragment at start: "[Not provided]-->\nreal content"
    cleaned = HTML_COMMENT_CLOSE_RE.sub("", cleaned)

    # Collapse multiple blank lines
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)

    # Strip leading/trailing whitespace
    cleaned = cleaned.strip()

    return cleaned


def is_empty_content(content: str) -> bool:
    """Check if content is empty or placeholder-only."""
    if not content:
        return True
    for pattern in PLACEHOLDER_PATTERNS:
        if pattern.match(content):
            return True
    return False


# ---------------------------------------------------------------------------
# Auto-fill detection — skip content that is auto-generated by the bundler
# pipeline or is default boilerplate, not community-written.
# ---------------------------------------------------------------------------

# Pontoon link pattern (the standard auto-fill for community_links)
_PONTOON_LINK_RE = re.compile(
    r"^\*\s+\[.*\]\(https://pontoon\.mozilla\.org/.+\)\s*$"
)

# Standard SCS contribute links pattern
_SCS_CONTRIBUTE_RE = re.compile(
    r"^\*\s+\[.*\]\(https://commonvoice\.mozilla\.org/.+/"
    r"(speak|write|listen|review)\)\s*$"
)

# Standard SPS contribute links pattern
_SPS_CONTRIBUTE_RE = re.compile(
    r"^\*\s+\[.*\]\(https://commonvoice\.mozilla\.org/"
    r"spontaneous-speech/.+\)\s*$"
)

# OMSF funding boilerplate
_OMSF_FUNDING_RE = re.compile(
    r"Open Multilingual Speech Fund", re.IGNORECASE
)

# CPG (Community Participation Guidelines) link — auto-fill filler
_CPG_LINK_RE = re.compile(
    r"^\*?\s*\[.*\]\(https://github\.com/common-voice/common-voice/"
    r"blob/main/docs/COMMUNITIES\.md\)\s*$"
)

# GitHub language request issue link — auto-fill
_GH_ISSUE_RE = re.compile(
    r"^\*?\s*\[.*\]\(https://github\.com/common-voice/"
    r"common-voice/issues/\d+\)\s*$"
)

# Auto-generated corpus stats ("The text corpus contains `NNN` sentences")
_CORPUS_STATS_RE = re.compile(
    r"^The text corpus contains\s+`?\d", re.IGNORECASE
)
_CORPUS_STATS_ES_RE = re.compile(
    r"^El corpus textual contiene\s+`?\d", re.IGNORECASE
)

# Markdown table line (used for text_domain detection)
_TABLE_LINE_RE = re.compile(r"^\s*\|.*\|\s*$")
_TABLE_SEP_RE = re.compile(r"^\s*\|[-|: ]+\|\s*$")

# Auto-generated transcription metrics ("* Prompts: `NNN`")
_TRANSCRIPTION_METRICS_RE = re.compile(
    r"^\*\s+(Prompts|Duration|Avg\.\s|Valid\s|Total\s)", re.IGNORECASE
)


def is_autofill_content(field_name: str, content: str) -> bool:
    """
    Check if content is auto-generated bundler data or default boilerplate.
    Returns True if the content should be skipped.
    """
    lines = [ln for ln in content.strip().splitlines() if ln.strip()]

    if field_name == "community_links":
        if not lines:
            return True
        return all(
            _PONTOON_LINK_RE.match(ln)
            or _CPG_LINK_RE.match(ln)
            or _GH_ISSUE_RE.match(ln)
            for ln in lines
        )

    if field_name == "contribute_links":
        if not lines:
            return True
        return all(
            _SCS_CONTRIBUTE_RE.match(ln) or _SPS_CONTRIBUTE_RE.match(ln)
            for ln in lines
        )

    if field_name == "funding":
        # OMSF-only boilerplate (no additional paragraphs)
        if _OMSF_FUNDING_RE.search(content):
            paragraphs = [
                p.strip() for p in content.split("\n\n") if p.strip()
            ]
            return len(paragraphs) <= 1
        return False

    if field_name == "corpus":
        # Auto-generated sentence count stats
        stripped = content.strip()
        if _CORPUS_STATS_RE.match(stripped):
            return True
        if _CORPUS_STATS_ES_RE.match(stripped):
            return True
        return False

    if field_name == "text_domain":
        # Auto-generated if content is ONLY a markdown table (no prose)
        if not lines:
            return True
        return all(
            _TABLE_LINE_RE.match(ln) or _TABLE_SEP_RE.match(ln)
            for ln in lines
        )

    if field_name == "transcriptions":
        # Auto-generated metrics bullets
        if not lines:
            return True
        return all(_TRANSCRIPTION_METRICS_RE.match(ln) for ln in lines)

    return False


# ---------------------------------------------------------------------------
# Datasheet parsing (lightweight — we use section titles to map fields)
# ---------------------------------------------------------------------------

def parse_sections(markdown_text: str) -> list[tuple[str, int, str]]:
    """
    Parse markdown into sections: (title, level, content).
    Returns list of (title, heading_level, raw_content).
    """
    sections: list[tuple[str, int, str]] = []
    current_title = ""
    current_level = 0
    current_lines: list[str] = []

    for line in markdown_text.split("\n"):
        heading_match = re.match(r"^(#{1,6})\s+(.*)", line)
        if heading_match:
            # Save previous section
            if current_title or current_lines:
                raw = "\n".join(current_lines)
                sections.append((current_title, current_level, raw))

            current_level = len(heading_match.group(1))
            current_title = heading_match.group(2).strip()
            current_lines = []
        else:
            current_lines.append(line)

    # Save last section
    if current_title or current_lines:
        raw = "\n".join(current_lines)
        sections.append((current_title, current_level, raw))

    return sections


# ---------------------------------------------------------------------------
# Source discovery
# ---------------------------------------------------------------------------

type SourceEntry = tuple[str, str, str, Path]
# (modality, template_lang, locale_code, file_path)


def discover_sources() -> dict[str, dict[str, list[SourceEntry]]]:
    """
    Discover all datasheet source files organized by priority.
    Returns: { "high": {locale: [entries]}, "medium": {...}, "low": {...} }

    Priority:
      high   = v24 (flat structure, no draft/final)
      medium = v23/final
      low    = v23/draft
    """
    priorities: dict[str, dict[str, list[SourceEntry]]] = {
        "high": {},
        "medium": {},
        "low": {},
    }

    for modality_dir in ["scs", "sps"]:
        modality_path = LEGACY_DIR / modality_dir
        if not modality_path.exists():
            continue

        modality = "scripted" if modality_dir == "scs" else "spontaneous"

        for version_dir in sorted(modality_path.iterdir()):
            if not version_dir.is_dir():
                continue

            version_name = version_dir.name  # e.g. "24.0-2025-12-05"
            is_v24 = version_name.startswith("24.")

            if is_v24:
                # Flat structure: version_dir/{en,es,zh-TW}/*.md
                for lang_dir in version_dir.iterdir():
                    if not lang_dir.is_dir():
                        continue
                    template_lang = lang_dir.name
                    for md_file in sorted(lang_dir.glob("*.md")):
                        locale = md_file.stem
                        entry: SourceEntry = (modality, template_lang, locale, md_file)
                        priorities["high"].setdefault(locale, []).append(entry)
            else:
                # v23 structure: version_dir/{draft,final}/{en,es,zh-TW}/*.md
                for stage_dir in ["final", "draft"]:
                    stage_path = version_dir / stage_dir
                    if not stage_path.exists():
                        continue

                    priority = "medium" if stage_dir == "final" else "low"

                    for lang_dir in stage_path.iterdir():
                        if not lang_dir.is_dir():
                            continue
                        template_lang = lang_dir.name
                        for md_file in sorted(lang_dir.glob("*.md")):
                            locale = md_file.stem
                            entry = (modality, template_lang, locale, md_file)
                            priorities[priority].setdefault(locale, []).append(entry)

    return priorities


# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------

def extract_one(
    entry: SourceEntry,
    title_map: dict[str, str],
    field_map: dict[str, dict],
    modality_fields: dict[str, list[str]],
    language_level_fields: set[str],
    already_extracted: set[tuple[str, str, str]],
    dry_run: bool = False,
) -> tuple[dict[str, int], dict[str, str]]:
    """
    Extract community content from a single datasheet file.

    - Modality-specific fields are written immediately to {modality}/.
    - Language-level fields are returned (not written) so the caller
      can pick the best content across modalities and write to shared/.

    Skips fields already extracted from a higher-priority source.
    Multiple sections within the same file mapping to the same field
    are concatenated (e.g. Curators + Compiler + Contact → authors).

    Returns:
        (modality_stats, lang_level_content)
        modality_stats: { field_name: 1 for each modality field written }
        lang_level_content: { field_name: content } for language-level fields
    """
    modality, template_lang, locale, file_path = entry
    modality_stats: dict[str, int] = {}
    lang_level_content: dict[str, str] = {}

    with open(file_path, encoding="utf-8") as f:
        text = f.read()

    sections = parse_sections(text)

    # Which fields are valid for this modality?
    valid_fields = set(modality_fields.get(modality, []))

    # First pass: collect all content per field within this file
    collected: dict[str, list[str]] = {}

    for title, level, raw_content in sections:
        if not title:
            continue

        field_name = title_map.get(title)

        if field_name is None:
            if title in SKIP_SECTIONS:
                continue
            continue

        if field_name not in valid_fields:
            continue

        # For modality fields, skip if already extracted from higher priority
        if field_name not in language_level_fields:
            key = (locale, modality, field_name)
            if key in already_extracted:
                continue

        cleaned = clean_section_content(raw_content)
        if is_empty_content(cleaned):
            continue
        if is_autofill_content(field_name, cleaned):
            continue

        collected.setdefault(field_name, []).append(cleaned)

    # Second pass: write modality fields, collect language-level fields
    for field_name, parts in collected.items():
        file_info = field_map["fields"].get(field_name)
        if file_info is None:
            continue

        content = "\n\n".join(parts)

        if field_name in language_level_fields:
            # Language-level: return content for deferred best-pick writing
            lang_level_content[field_name] = content
        else:
            # Modality-specific: write immediately
            locale_dir = CONTENT_DIR / "locales" / locale / modality
            out_path = locale_dir / file_info["file"]

            if dry_run:
                print(f"  [DRY] {out_path.relative_to(REPO_ROOT)}")
            else:
                locale_dir.mkdir(parents=True, exist_ok=True)
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(content + "\n")

            key = (locale, modality, field_name)
            already_extracted.add(key)
            modality_stats[field_name] = 1

    return modality_stats, lang_level_content


def pick_best_content(candidates: list[str]) -> str:
    """
    Pick the best content from multiple candidates.
    Strategy: longest non-empty content wins (most community detail).
    """
    best = ""
    for content in candidates:
        if len(content) > len(best):
            best = content
    return best


def main():
    dry_run = "--dry-run" in sys.argv

    print("=== Community Data Extraction ===")
    print(f"Source:  {LEGACY_DIR}")
    print(f"Target:  {CONTENT_DIR / 'locales'}")
    if dry_run:
        print("Mode:    DRY RUN (no files written)")
    print()

    # Load field map
    with open(FIELD_MAP_PATH, encoding="utf-8") as f:
        field_map = json.load(f)

    modality_fields = field_map.get("modality_fields", {})
    language_level_fields = set(field_map.get("language_level_fields", []))

    print(f"Language-level fields (→ shared/): {sorted(language_level_fields)}")
    print()

    # Build title → field mapping from i18n
    title_map = build_title_to_field_map()
    print(f"Title mappings loaded: {len(title_map)} entries")
    print()

    # Discover sources
    priorities = discover_sources()

    total_high = sum(len(v) for v in priorities["high"].values())
    total_medium = sum(len(v) for v in priorities["medium"].values())
    total_low = sum(len(v) for v in priorities["low"].values())
    print(f"Sources discovered:")
    print(f"  High priority (v24):       {total_high} files")
    print(f"  Medium priority (v23/final): {total_medium} files")
    print(f"  Low priority (v23/draft):    {total_low} files")
    print()

    # Track what we've already extracted (locale, modality, field)
    # Passed to extract_one so higher-priority sources win for modality fields
    extracted: set[tuple[str, str, str]] = set()

    # Aggregate stats
    total_files_written = 0
    total_locales: set[str] = set()
    field_counts: dict[str, int] = {}

    # Collect language-level candidates across all sources:
    # { (locale, field_name): [(priority_rank, content), ...] }
    # priority_rank: 0=high, 1=medium, 2=low (lower is better)
    lang_level_candidates: dict[
        tuple[str, str], list[tuple[int, str]]
    ] = {}

    priority_ranks = {"high": 0, "medium": 1, "low": 2}

    # Process in priority order: high first, then medium, then low
    for priority_label in ["high", "medium", "low"]:
        entries_by_locale = priorities[priority_label]
        rank = priority_ranks[priority_label]

        for locale, entries in sorted(entries_by_locale.items()):
            for entry in entries:
                modality_stats, lang_content = extract_one(
                    entry, title_map, field_map, modality_fields,
                    language_level_fields, extracted, dry_run,
                )

                # Count modality fields written
                for field_name in modality_stats:
                    total_files_written += 1
                    total_locales.add(locale)
                    field_counts[field_name] = (
                        field_counts.get(field_name, 0) + 1
                    )

                # Accumulate language-level candidates
                for field_name, content in lang_content.items():
                    key = (locale, field_name)
                    lang_level_candidates.setdefault(key, []).append(
                        (rank, content)
                    )

    # Now write language-level fields to shared/
    # For each (locale, field), pick best: highest priority first,
    # then longest content among same-priority candidates
    print("Writing language-level fields to shared/...")
    shared_written = 0

    for (locale, field_name), candidates in sorted(
        lang_level_candidates.items()
    ):
        file_info = field_map["fields"].get(field_name)
        if file_info is None:
            continue

        # Sort by priority rank (ascending), then pick best within
        # the highest available priority
        candidates.sort(key=lambda x: x[0])
        best_rank = candidates[0][0]

        # Get all candidates at the best priority level
        best_candidates = [c for r, c in candidates if r == best_rank]

        # Pick the longest (most detailed) among best-priority candidates
        content = pick_best_content(best_candidates)

        if not content:
            continue

        locale_dir = CONTENT_DIR / "locales" / locale / "shared"
        out_path = locale_dir / file_info["file"]

        if dry_run:
            print(f"  [DRY] {out_path.relative_to(REPO_ROOT)}")
        else:
            locale_dir.mkdir(parents=True, exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(content + "\n")

        shared_written += 1
        total_locales.add(locale)
        field_counts[field_name] = field_counts.get(field_name, 0) + 1

    total_files_written += shared_written

    # Report
    print(f"\n=== Extraction Complete ===")
    print(f"Locales processed:  {len(total_locales)}")
    print(f"Content files:      {total_files_written}")
    print(f"  Modality files:   {total_files_written - shared_written}")
    print(f"  Shared files:     {shared_written}")
    print(f"\nFields extracted (count across all locales):")
    for field, count in sorted(field_counts.items(), key=lambda x: -x[1]):
        is_shared = field in language_level_fields
        marker = " [shared]" if is_shared else ""
        print(f"  {field:40s} {count:>4d}{marker}")


if __name__ == "__main__":
    main()
