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
- Write plain Markdown — no Jinja2 or HTML needed.
- List items (bullets, numbered lists) are deduplicated at compile time as a safety net.

### Additive vs Descriptive Fields

Datasheet content is built by the community over time. Some fields accumulate
entries across releases, while others describe the current state.

**Additive fields — extend, do not replace:**

| Field | Why it grows |
| --- | --- |
| `sources.md` | New text/audio sources are added each release |
| `corpus.md` | Corpus description grows as new sources join |
| `text_domain.md` | New domains appear as the corpus expands |
| `authors.md` | New contributors and community leads join over time |
| `citation.md` | New publications reference the dataset |
| `funding.md` | Additional funders may support the project |
| `community_links.md` | New community spaces are created |
| `discussion_links.md` | New discussion channels open |
| `contribute_links.md` | New contribution paths become available |

When editing additive fields, **add your entries below the existing content**.
Do not remove previous contributions — they represent the work of earlier
community members. Include version references where helpful (e.g.
`v24.0`, `v22.0–present`).

**Descriptive fields — rewrite or improve freely:**

| Field | What it describes |
| --- | --- |
| `description.md` | The language itself |
| `variants.md` | Dialect and accent landscape |
| `writing_system.md` | How the language is written |
| `alphabet.md` | Symbol table or character list |
| `processing.md` | Current text processing pipeline |
| `postprocessing.md` | Current recommended post-processing |
| `transcriptions.md` | Current transcription process |

These fields describe the current state. They can be rewritten entirely when
the understanding improves — they are not a historical record.

See `content/_example/` for examples of both patterns, particularly
`scripted/sources.md` and `scripted/authors.md` for the additive style.

### Fields With Auto-Defaults

Some fields are filled automatically if you don't provide them:

- **`contribute_links.md`** — Standard Speak/Write/Listen/Review links are added
- **`community_links.md`** — Pontoon translators link is added
- **`funding.md`** — OMSF funding text is added for eligible locales

Only create these files if you have additional or different content.
