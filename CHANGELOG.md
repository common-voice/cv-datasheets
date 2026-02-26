# Changelog

All notable changes to this project are documented in this file.

The changelog has two sections:

- **Code & Workflow** — changes to scripts, templates, tooling, and processes
- **Data vNN.N** — changes to compiled releases (new locales, content updates)

---

## [Unreleased]

### Code & Workflow

- Migrated to Jinja2 template inheritance (`base.md.j2` → `scripted.md.j2` / `spontaneous.md.j2`)
- Atomized community content into `content/locales/{code}/{shared,scripted,spontaneous}/`
- Created `compile_datasheets.py` — compiles templates + content + metadata into bundler-ready JSON
- Created `scripts/extract_community_data.py` — one-time extraction from legacy `cv-corpus/` datasheets
- Added i18n support for section titles (`templates/i18n/`)
- Added OMSF funding auto-injection via `metadata/funding.tsv`
- Added content fallback chain: modality → shared → defaults → empty
- Added `content/_template/` and `content/_example/` (Klingon) for contributors
- Added `--languages-file` option for version-specific locale lists
- Added `--diff` option to compile script for release-to-release changelog generation
- Added `edit_mode` field classification: additive (extend) vs descriptive (rewrite)
- Added `docs/` directory (`ARCHITECTURE.md`, `CONTRIBUTING.md`, `COMPILING.md`)
- Added auto-fill detection in extraction: filters auto-generated bundler stats (corpus counts, domain tables, transcription metrics), boilerplate links, and OMSF funding
- Added `[Not provided]` placeholder and broken HTML comment cleanup in extraction
- Moved legacy scripts and generated datasheets to `_legacy/`
- Fixed: `fy-NL` was missing from SPS in `datasheet-languages.tsv`
- Fixed: `variants` is now a language-level (shared) field, available in both SCS and SPS

---

## datasheets-24.0-2025-12-05

### Data v24.0

**SCS (Scripted Speech):** 289 locales

- 1 new locale: `dsb`

**SPS (Spontaneous Speech):** 58 locales

- No locale changes

---

## datasheets-23.0-2025-09-05

### Data v23.0

**SCS (Scripted Speech):** 288 locales

- Initial compiled release from extracted legacy data

**SPS (Spontaneous Speech):** 58 locales

- Initial compiled release from extracted legacy data
