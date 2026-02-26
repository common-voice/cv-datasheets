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
- Added `--diff` option to compile script for release-to-release changelog generation
- Added `edit_mode` field classification: additive (extend) vs descriptive (rewrite)
- Added `docs/` directory (`ARCHITECTURE.md`, `CONTRIBUTING.md`, `COMPILING.md`)
- Added auto-fill detection in extraction: filters auto-generated bundler stats (corpus counts, domain tables, transcription metrics), boilerplate links, and OMSF funding
- Added `[Not provided]` placeholder and broken HTML comment cleanup in extraction
- Moved legacy scripts and generated datasheets to `_legacy/`
- Fixed: `variants` is now a language-level (shared) field, available in both SCS and SPS

#### API-Driven Metadata

- Created `scripts/fetch_api_metadata.py` — fetches SCS languagedata + SPS locales from Common Voice APIs into a single snapshot
- Added `metadata/api-snapshots/` — timestamped API snapshots as the source of truth for language names, text direction, variants, and accents
- Added `metadata/locale-extras.json` — manually maintained entries for locales not in the API (`el-CY`, `ms-MY`)
- Added `metadata/template-languages.json` — template language overrides (13 locales using `es`, default `en`)
- Replaced `--languages-file` with required `--api-snapshot` flag — locale lists now derive from API data
- Removed `datasheet-languages.tsv` — locale lists are API-driven, no manual TSV maintenance
- Retired old metadata pipeline: `generate-metadata.py`, `merge-metadata.py`, `update-metadata.sh`, `metadata.tsv`, `scs-metadata.json`, `sps-metadata.json`, `sps-locales.json`
- Added `predefined_accents` as a new community field and template section
- Added auto-generation of `variant_description` and `predefined_accents_description` from API data when no community content exists
- Added `text_direction` to locale metadata output
- SPS locale list now fetched from SPS API (79 contributable locales, up from manually maintained 58)
- Added translated datasheet guide to `docs/CONTRIBUTING.md`
- Auto-discovered template languages from `templates/i18n/*.json` — removed hardcoded `TEMPLATE_LANGS` constant

#### Mergeable Fields

- Added `mergeable` property (boolean) for fields that combine community content with bundler-generated stats
- `mergeable` is orthogonal to `edit_mode` — each field retains its additive/descriptive edit policy
- Mergeable fields: `corpus`, `sources`, `text_domain`, `variants`, `predefined_accents`, `transcriptions`
- Added template-level auto placeholders (`{{*_STATS}}`) adjacent to community field placeholders
- Bundler fills stats when available; unfilled placeholders are stripped (no bundler changes needed)

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
