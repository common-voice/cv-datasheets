# Compiling Datasheets

## Prerequisites

- Python 3.12+
- `uv` package manager (or pip with `jinja2` installed)
- An API snapshot (see [Fetching API Metadata](#fetching-api-metadata))

## Basic Usage

```bash
python3 compile_datasheets.py <snapshot_date> --api-snapshot <snapshot-path> [--pretty] [--output PATH] [--diff PREVIOUS_JSON]
```

### Examples

Compile for a specific release:

```bash
python3 compile_datasheets.py 2026-03-09 \
    --api-snapshot metadata/api-snapshots/languagedata-20260226.json \
    --pretty
```

Custom output path:

```bash
python3 compile_datasheets.py 2026-03-09 \
    --api-snapshot metadata/api-snapshots/languagedata-20260226.json \
    --output /tmp/test-datasheets.json --pretty
```

Compare with a previous release:

```bash
python3 compile_datasheets.py 2026-03-09 \
    --api-snapshot metadata/api-snapshots/languagedata-20260226.json \
    --diff releases/datasheets-2025-09-05.json --pretty
```

## What the Compile Script Does

1. **Loads API snapshot** -- Language names, text direction, and SPS locale list from the snapshot (+ locale-extras for edge cases)
2. **Renders Jinja2 templates** -- Flattens `base.md.j2` -> child templates into flat markdown with `{{KEY}}` placeholders. Processes all i18n strings through `render_inline_vars()` to convert `{variable}` placeholders to `{{KEY}}` bundler markers.
3. **Loads community content** -- Reads `content/locales/` with the fallback chain (modality -> shared -> defaults -> empty)
4. **Injects OMSF funding** -- For locales in `metadata/funding.tsv` that lack community-written funding content
5. **Loads metadata** -- Template-language mapping, funding info
6. **Outputs JSON** -- Single file matching the bundler's expected schema

## Fetching API Metadata

Before compiling, fetch a fresh API snapshot:

```bash
python3 scripts/fetch_api_metadata.py
```

This fetches two endpoints:

1. **SCS languagedata** (`/api/v1/languagedata`) -- all locale metadata (names, variants, accents)
2. **SPS locales** (`/spontaneous-speech/beta/api/v1/locales`) -- contributable locale codes

The snapshot is saved to `metadata/api-snapshots/languagedata-{YYYYMMDD}.json`.

Custom endpoints (e.g. staging):

```bash
python3 scripts/fetch_api_metadata.py --scs-url URL --sps-url URL
```

## Locale Sources

The compile script derives its locale lists from the API snapshot:

- **SCS locales** -- all locales in the snapshot (428+), including non-contributable ones
- **SPS locales** -- from the snapshot's `sps_locales` array (fetched from SPS API)
- **Edge cases** -- `metadata/locale-extras.json` provides entries for locales not in the API (e.g. `el-CY`, `ms-MY` regional codes)

There is no need to maintain a manual locale list. Any locale present in the API snapshot will get a datasheet entry.

## Template Languages

Available template languages are **auto-discovered** from `templates/i18n/*.json` files. The compile script checks each i18n file for `header_intro_scs` / `header_intro_sps` keys to determine which modalities it supports.

Each locale defaults to `en`. The 13 locales that use a non-English template are listed in `metadata/template-languages.json`:

```json
{ "cut": "es", "cux": "es", "hch": "es", ... }
```

To add a new translated template, see [How to Add a Translated Datasheet](CONTRIBUTING.md#how-to-add-a-translated-datasheet).

## Output

Default output: `releases/datasheets-{snapshot_date}.json`

The `--pretty` flag adds indentation for human readability.

## Previewing

Preview how community content will render without needing real bundler statistics:

```bash
python3 scripts/preview_datasheets.py -l ady          # single locale
python3 scripts/preview_datasheets.py -l ady kbd es    # multiple locales
python3 scripts/preview_datasheets.py --changed        # auto-detect from git diff
```

The preview script:

- Compiles directly from the working tree (no pre-compiled JSON needed)
- Fetches API metadata on the fly (cached for 24h in `previews/.api-snapshot.json`)
- Falls back to the latest committed snapshot if the API is unreachable
- Substitutes `{{KEY}}` placeholders with dummy values (marked `?` in tables)
- Strips empty sections (same as the bundler)
- Outputs to `previews/preview-{locale}-{modality}.md` (gitignored)

On Pull Requests, the `preview.yml` workflow runs automatically and posts the rendered preview as a comment.

## Auto-Compile

When changes are merged to `main`, the `compile-latest.yml` workflow automatically recompiles `releases/datasheets-latest.json` using the latest committed API snapshot. This rolling file always reflects the current state of `main`.

The auto-compile triggers on changes to `content/`, `templates/`, `metadata/`, or the compile script itself. The resulting commit (`chore: auto-compile datasheets-latest.json`) does not re-trigger the workflow.

## Release Workflow

1. Fetch a fresh API snapshot: `python3 scripts/fetch_api_metadata.py`
2. Commit the snapshot to `metadata/api-snapshots/`
3. Update community content via PRs (previews are generated automatically)
4. Compile: `python3 compile_datasheets.py {snapshot_date} --api-snapshot metadata/api-snapshots/languagedata-{YYYYMMDD}.json --pretty`
5. Review the changelog diff (use `--diff` against previous release)
6. Commit the release JSON
7. Tag: `datasheets-{snapshot_date}`

Note: `datasheets-latest.json` is updated automatically on merge. Dated release files (`datasheets-{date}.json`) are created manually as part of this workflow.
