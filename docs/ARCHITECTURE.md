# Architecture

## Overview

cv-datasheets is the **data supplier** for dataset documentation in Common Voice. It maintains Jinja2 templates, community-written content, and static metadata that are compiled into a JSON file consumed by the bundler pipeline at release time.

```txt
cv-datasheets (compile-time)              Bundler (runtime)
─────────────────────────────────         ─────────────────────────
API snapshot ─────┐
Jinja2 templates ─┤
content/ files ───┤── compile ──►  datasheets.json ──► datasheetsFetcher.ts
metadata/ files ──┘                                        │
                                                   DatasheetLocalePayload
                                                   { template, community_fields, metadata }
                                                           │
                                                   datasheets.ts fills {{KEY}} with
                                                   live stats + community data
                                                           │
                                                   README.md → tar.gz + GCS /datasheets/
```

## Jinja2 Role

Jinja2 runs **at compile time only** inside this repository. It resolves template inheritance (`base.md.j2` → child templates) and produces flat markdown strings with `{{KEY}}` markers. The bundler never touches Jinja2.

**How it works:**

1. `base.md.j2` defines the shared skeleton (header, demographics, links, licence)
2. `scripted.md.j2` and `spontaneous.md.j2` extend the base with modality-specific blocks
3. The compile script renders each child template with placeholder values:
   - `{{ stats.clips }}` outputs literal `{{CLIPS}}`
   - `{{ community.description }}` outputs literal `{{LANGUAGE_DESCRIPTION}}`
   - `{% block %}` / `{% extends %}` are resolved (inheritance flattened)
4. Result: flat markdown with `{{KEY}}` markers — same format the bundler already consumes

## API Snapshot

Language metadata comes from a snapshot of the Common Voice APIs, fetched by `scripts/fetch_api_metadata.py`:

| Source | Endpoint | Data |
| --- | --- | --- |
| SCS languagedata | `/api/v1/languagedata` | Names, text direction, variants, predefined accents, contributable status |
| SPS locales | `/spontaneous-speech/beta/api/v1/locales` | Contributable SPS locale codes |

The snapshot is stored in `metadata/api-snapshots/languagedata-{YYYYMMDD}.json` and passed to the compile script via `--api-snapshot`.

**Locale extras:** Regional codes not present in the API (e.g. `el-CY`, `ms-MY`) are defined in `metadata/locale-extras.json` and merged into the snapshot at load time.

**Template languages:** Auto-discovered from `templates/i18n/*.json` — the compile script checks for `header_intro_scs`/`header_intro_sps` keys to determine modality support. Default locale mapping is `en`; non-English overrides are in `metadata/template-languages.json` (currently 13 locales using `es`).

## Auto-Generated Content

The compile script auto-generates content from API data when no community file exists:

| Field | Source | Condition |
| --- | --- | --- |
| `variant_description` | API `variants` list | No `variants.md` in content |
| `predefined_accents_description` | API `predefined_accents` list | No `predefined_accents.md` in content |
| `funding_description` | OMSF funding text | Locale in `funding.tsv`, no `funding.md` in content |
| `contribute_links_list` | Standard Speak/Write/Listen/Review links | No `contribute_links.md` in content |
| `community_links_list` | Pontoon translators link | No `community_links.md` in content |

Community content always takes precedence over auto-generated content.

## Content Fallback Chain

When the compile script loads community content for a locale, it checks four locations in order:

```txt
1. content/locales/{code}/{modality}/{field}.md     ← modality-specific (highest)
2. content/locales/{code}/shared/{field}.md         ← explicit shared (opt-in)
3. content/_defaults/{template_lang}/{field}.md     ← template language default
4. content/_defaults/en/{field}.md                  ← English default
5. ""                                               ← empty (bundler handles)
```

## Compile Output

The compile script produces a single JSON file per release:

```json
{
  "schema_version": "2.0.0",
  "generated_at": "2026-02-26T...",
  "source_version": "24.0-2025-12-05",
  "templates": {
    "scs": { "en": "flat markdown...", "es": "...", "zh-TW": "..." },
    "sps": { "en": "flat markdown...", "es": "..." }
  },
  "locales": {
    "scs": {
      "{locale}": {
        "template_language": "en",
        "metadata": {
          "native_name": "...", "english_name": "...",
          "text_direction": "LTR", "funding": "..."
        },
        "community_fields": {
          "language_description": "...",
          "variant_description": "...",
          "predefined_accents_description": "...",
          ...
        }
      }
    },
    "sps": { "..." }
  }
}
```

## Bundler Integration

The SCS bundler fetches the JSON by release name:

```txt
https://raw.githubusercontent.com/common-voice/cv-datasheets/main/releases/datasheets-{releaseName}.json
```

It then:

1. Picks the correct template using `entry.template_language`
2. Builds a replacement map from auto-generated stats + community fields + metadata
3. Replaces `{{KEY}}` placeholders via regex
4. Writes `README.md` per locale into the dataset tar

## What Goes Where

| Content type | Handled by | Bundler sees |
| --- | --- | --- |
| Community-written content | compile_datasheets.py | Filled `community_fields` values |
| API-derived names & direction | compile_datasheets.py (API snapshot) | `metadata.native_name`, `metadata.english_name`, `metadata.text_direction` |
| Auto-generated variants/accents | compile_datasheets.py (API data) | Pre-filled in `community_fields` |
| Pontoon / contribute link defaults | compile_datasheets.py (`_defaults/`) | Pre-filled in `community_fields` |
| OMSF funding | compile_datasheets.py (`metadata/funding.tsv`) | Pre-filled `funding_description` |
| Auto-generated stats (clips, hours, demographics) | Bundler at runtime | `{{KEY}}` placeholders in template |
| Sentence/question samples | Bundler at runtime | `{{KEY}}` placeholders in template |
