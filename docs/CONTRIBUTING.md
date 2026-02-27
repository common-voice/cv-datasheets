# Contributing Content

This guide explains how to add or update datasheet content for your language.

## What Are Datasheets?

Datasheets describe each language dataset in Common Voice. They include information about the language, its writing system, text sources, and community contributors.

## How to Contribute

### Via Pull Request (preferred)

1. Fork this repository
2. Look at `content/_template/` for the directory structure and file list
3. Look at `content/_example/` for a filled-in reference
4. Create or edit files under `content/locales/{your-locale-code}/`
5. Submit a Pull Request

### Via Google Form

Datasheets can also be submitted via Google Form (English and Spanish):

**Scripted/Read Speech:**

- (`en`) [MCV Datasheet: Scripted speech](https://docs.google.com/forms/d/e/1FAIpQLSc5QnmXd7MrfPd375RZ2YFh-Z3I_BGAf7e2cTD2h5xtWV8klQ/viewform?usp=dialog)
- (`es`) [MCV Datasheet: Habla leída](https://docs.google.com/forms/d/e/1FAIpQLSdk1IITzjpjrXKKLyHhzb5d0VoGvNNbscBywqJZf1BnBcf7Pw/viewform?usp=dialog)

**Spontaneous Speech:**

- (`en`) [MCV Datasheet: Spontaneous speech](https://docs.google.com/forms/d/e/1FAIpQLSfYI6CXK97boZ951gb3l2ysl77Hnyyi8qeSagXAlB1v32adqQ/viewform?usp=dialog)
- (`es`) [MCV Datasheet: Habla espontánea](https://docs.google.com/forms/d/e/1FAIpQLSdhHHYqgj1x6Cki8OYCHjVr3l3KmahBfcWvOgF70B6gV1jfbw/viewform?usp=dialog)

### Via Email

If you cannot access GitHub or the form, email the Common Voice team at <commonvoice@mozilla.com>.

## Directory Structure

```txt
content/locales/{locale}/
  shared/              # Language-level (shared across SCS and SPS)
    description.md       About the language
    variants.md          Dialect / accent variants
    predefined_accents.md  Predefined accent options
    writing_system.md    Writing system description
    alphabet.md          Symbol table
    community_links.md   Community resource links

  scripted/            # Scripted Speech (SCS) only
    corpus.md            Text corpus description
    sources.md           Corpus sources
    text_domain.md       Text domain descriptions
    processing.md        Text processing applied
    postprocessing.md    Recommended post-processing
    discussion_links.md  Discussion links
    contribute_links.md  Non-standard contribute links
    authors.md           Datasheet authors
    citation.md          Citation guidelines
    funding.md           Non-OMSF or additional funding

  spontaneous/         # Spontaneous Speech (SPS) only
    transcriptions.md    Transcription process description
    postprocessing.md    Recommended post-processing
    discussion_links.md  Discussion links
    contribute_links.md  Non-standard contribute links
    authors.md           Datasheet authors
    citation.md          Citation guidelines
    funding.md           Non-OMSF or additional funding
```

## Guidelines

- **Only create files you have content for.** Empty files are ignored.
- **`shared/`** fields apply to both SCS and SPS. Write them once here instead of duplicating across `scripted/` and `spontaneous/`.
- Write plain Markdown -- no Jinja2 or HTML needed.
- List items (bullets, numbered lists) are deduplicated at compile time as a safety net.

### Field Edit Modes

Datasheet content is built by the community over time. Fields have two
edit modes that indicate how they should be maintained.

**Additive fields -- extend, do not replace:**

| Field                 | Why it grows                                        |
| --------------------- | --------------------------------------------------- |
| `sources.md`          | New text sources are added across releases          |
| `authors.md`          | New contributors and community leads join over time |
| `citation.md`         | New publications reference the dataset              |
| `funding.md`          | Additional funders may support the project          |
| `community_links.md`  | New community spaces are created                    |
| `discussion_links.md` | New discussion channels open                        |
| `contribute_links.md` | New contribution paths become available             |

When editing additive fields, **add your entries below the existing content**.
Do not remove previous contributions -- they represent the work of earlier
community members. Include version references where helpful (e.g.
`v24.0`, `v22.0-present`).

**Descriptive fields -- rewrite or improve freely:**

| Field                   | What it describes                   |
| ----------------------- | ----------------------------------- |
| `description.md`        | The language itself                 |
| `variants.md`           | Dialect / accent variants           |
| `predefined_accents.md` | Predefined accent options           |
| `corpus.md`             | Text corpus description             |
| `text_domain.md`        | Text domain descriptions            |
| `transcriptions.md`     | Transcription process               |
| `writing_system.md`     | How the language is written         |
| `alphabet.md`           | Symbol table or character list      |
| `processing.md`         | Current text processing pipeline    |
| `postprocessing.md`     | Current recommended post-processing |

These fields describe the current state. They can be rewritten entirely when
the understanding improves -- they are not a historical record.

**Mergeable fields -- community content + auto-generated data:**

Some fields are also **mergeable**: the bundler generates data (tables, counts,
metrics) for these sections. Your community content is optional -- if you
provide it, your text appears before the auto-generated data. If you don't
provide it, only the bundler's data appears. Each mergeable field is still
either additive or descriptive -- follow the edit rules above.

| Field                   | Edit mode   | Bundler generates             |
| ----------------------- | ----------- | ----------------------------- |
| `sources.md`            | additive    | Per-source counts             |
| `corpus.md`             | descriptive | Corpus statistics             |
| `text_domain.md`        | descriptive | Domain breakdown              |
| `variants.md`           | descriptive | Per-variant recording stats   |
| `predefined_accents.md` | descriptive | Per-accent recording stats    |
| `transcriptions.md`     | descriptive | Transcription quality metrics |

See `content/_example/` for examples, particularly
`scripted/sources.md` and `scripted/authors.md` for the additive style.

### Fields With Auto-Defaults

Some fields are filled automatically if you don't provide them:

- **`contribute_links.md`** -- Standard Speak/Write/Listen/Review links are added
- **`community_links.md`** -- Pontoon translators link is added
- **`funding.md`** -- OMSF funding text is added for eligible locales

Only create these files if you have additional or different content. Community content always overrides auto-generated defaults.

---

## How to Add a Translated Datasheet

By default, datasheets are generated in English. You can add support for a new language so that speakers of that language see the datasheet in their own language.

A translated datasheet requires two things:

1. **i18n strings** -- section titles and boilerplate text in an i18n JSON file
2. **Template language mapping** -- telling the compile script which locales use the new language

The compile script **auto-discovers** available template languages by scanning `templates/i18n/*.json`. No code changes are needed -- just add the files.

### Step 1: Add i18n Strings

Create a new file in `templates/i18n/{lang-code}.json` by copying `templates/i18n/en.json` and translating all values. Keep the JSON keys unchanged.

The compile script detects which modalities the translation supports by checking for `header_intro_scs` and/or `header_intro_sps` keys. To support both SCS and SPS, include both keys. To support only one modality, include only the relevant key.

Use the English file as the reference for the complete list of keys. All shared keys (titles, labels) must be present; modality-specific keys can be omitted for unsupported modalities.

Existing translations:

| File         | Language            | Keys | Coverage             |
| ------------ | ------------------- | ---- | -------------------- |
| `en.json`    | English             | 47   | Complete (SCS + SPS) |
| `es.json`    | Spanish             | 47   | Complete (SCS + SPS) |
| `zh-TW.json` | Traditional Chinese | 34   | SCS only             |

### Step 2: Map Locales to the Template Language

Edit `metadata/template-languages.json` to assign locales to your new template language. Only non-English locales need entries -- English is the default.

```json
{
  "_comment": "Template language overrides. Locales not listed here default to 'en'.",
  "fr": "fr",
  "fr-CA": "fr"
}
```

### Step 3: Add Default Content (optional)

If you want default content (contribute links, community links, OMSF funding text) in the new language:

- Create `content/_defaults/{lang-code}/` with the relevant `.md` files. See `content/_defaults/en/` and `content/_defaults/es/` for the pattern.
- Add a translated OMSF funding string to `OMSF_FUNDING_TEXT` in `compile_datasheets.py`.

### Step 4: Compile and Verify

```bash
python3 compile_datasheets.py {version} \
    --api-snapshot metadata/api-snapshots/languagedata-{date}.json \
    --pretty
```

Check that the output JSON contains your new template in `templates.scs.{lang}` (or `templates.sps.{lang}`) and that the mapped locales reference the correct `template_language`.
