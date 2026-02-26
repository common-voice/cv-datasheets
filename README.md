# cv-datasheets

Datasheets are documents that describe each language dataset in [Common Voice](https://commonvoice.mozilla.org/). This repository maintains **templates, community-written content, and metadata** that are compiled into a single JSON file consumed by the bundler pipeline at release time.

## How it works

```txt
templates/          Jinja2 templates (base + scripted + spontaneous)
content/locales/    Community-written content per locale
metadata/           Language names, funding, template-language mapping
        │
        ▼
  compile_datasheets.py
        │
        ▼
releases/datasheets-{version}.json  ──►  Bundler fills {{KEY}} with live stats
                                                │
                                          README.md per locale in dataset tar
```

For details on the compile-time vs runtime split, Jinja2 role, and bundler integration, see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Community contribution

Language communities are the experts on their languages. We ask community members to contribute datasheet content for their language(s) via Pull Requests.

1. Look at `content/_template/` for the directory structure, file list, and field types
2. Look at `content/_example/` for a filled-in reference (fictional Klingon locale)
3. Create or edit files under `content/locales/{your-locale-code}/`
4. Submit a Pull Request

Datasheets can also be submitted via Google Forms or email. For the full contributor guide, directory structure, additive vs descriptive field rules, and form links, see [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md).

## Repository structure

```txt
cv-datasheets/
├── templates/                  Jinja2 templates
│   ├── base.md.j2                Shared skeleton
│   ├── scripted.md.j2            SCS child template
│   ├── spontaneous.md.j2        SPS child template
│   ├── i18n/                     Section title translations (en, es, zh-TW)
│   └── _legacy/                  Old plain markdown templates (reference)
│
├── content/                    Community content
│   ├── _field_map.json           Field-to-bundler-key mapping
│   ├── _defaults/                Fallback content per template language
│   ├── _template/                Empty file structure for contributors
│   ├── _example/                 Filled-in example (Klingon)
│   └── locales/{code}/           Per-locale content (shared/, scripted/, spontaneous/)
│
├── metadata/                   TSV/JSON metadata
│   ├── metadata.tsv              Language names per modality
│   ├── datasheet-languages.tsv   (modality, locale) → template language
│   └── funding.tsv               Locale → funder mapping
│
├── compile_datasheets.py       Main compile script
├── scripts/
│   └── extract_community_data.py One-time extraction from legacy datasheets
│
├── docs/                       Documentation
│   ├── ARCHITECTURE.md           System design and bundler integration
│   ├── CONTRIBUTING.md           Community contribution guide
│   └── COMPILING.md              Compile script usage and release workflow
│
├── releases/                   Compiled output (datasheets-{version}.json)
│
└── _legacy/                    Deprecated scripts and generated datasheets
    ├── cv-corpus/                Old rendered datasheets (reference)
    └── *.py                      Old generation/processing scripts
```

## Quick start

Compile datasheets for a release:

```bash
python3 compile_datasheets.py 24.0-2025-12-05 --pretty
```

Compare against a previous release:

```bash
python3 compile_datasheets.py 24.0-2025-12-05 --pretty --diff releases/datasheets-23.0-2025-09-05.json
```

For all options, version-specific locale lists, and the release workflow, see [docs/COMPILING.md](docs/COMPILING.md).
