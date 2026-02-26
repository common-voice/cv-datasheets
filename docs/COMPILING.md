# Compiling Datasheets

## Prerequisites

- Python 3.12+
- `uv` package manager (or pip with `jinja2` installed)

## Basic Usage

```bash
python3 compile_datasheets.py <version> [--pretty] [--output PATH] [--languages-file PATH]
```

### Examples

Compile for a specific release:

```bash
python3 compile_datasheets.py 24.0-2025-12-05 --pretty
```

Compile with a version-specific locale list:

```bash
python3 compile_datasheets.py 23.0-2025-09-05 --languages-file metadata/datasheet-languages-23.tsv --pretty
```

Custom output path:

```bash
python3 compile_datasheets.py 24.0-2025-12-05 --output /tmp/test-datasheets.json --pretty
```

## What the Compile Script Does

1. **Renders Jinja2 templates** — Flattens `base.md.j2` → child templates into flat markdown with `{{KEY}}` placeholders
2. **Loads community content** — Reads `content/locales/` with the fallback chain (modality → shared → defaults → empty)
3. **Injects OMSF funding** — For locales in `metadata/funding.tsv` that lack community-written funding content
4. **Loads metadata** — Language names, template-language mapping, funding info
5. **Outputs JSON** — Single file matching the bundler's expected schema

## Output

Default output: `releases/datasheets-{version}.json`

The `--pretty` flag adds indentation for human readability.

## Version-Specific Locale Lists

The default locale list is `metadata/datasheet-languages.tsv` (current release). For older releases with different locale sets, create a version-specific TSV (e.g. `metadata/datasheet-languages-23.tsv`) and pass it via `--languages-file`.

## Release Workflow

1. Update community content via PRs
2. Compile: `python3 compile_datasheets.py {version} --pretty`
3. Review the changelog diff
4. Commit the release JSON
5. Tag: `datasheets-v{version}`
