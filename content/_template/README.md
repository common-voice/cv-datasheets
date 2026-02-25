# Content Template

Use this template when adding or updating datasheet content for a locale.
Copy the relevant directories into `content/locales/{locale}/` and fill in
the files you want to contribute.

## Directory structure

```txt
content/locales/{locale}/
  shared/              # Language-level fields (shared across SCS and SPS)
    description.md       # About the language
    variants.md          # Dialect / accent variants
    writing_system.md    # Writing system description
    alphabet.md          # Symbol table / alphabet list
    community_links.md   # Links to community resources

  scripted/            # Scripted Speech (SCS) only
    corpus.md            # Description of the text corpus
    sources.md           # Sources of the text corpus
    text_domain.md       # Text domain descriptions (not auto-generated tables)
    processing.md        # Text processing applied to the corpus
    postprocessing.md    # Recommended post-processing steps
    discussion_links.md  # Discussion forum / chat links
    contribute_links.md  # Links to contribute (only if non-standard)
    authors.md           # Datasheet authors
    citation.md          # How to cite this dataset
    funding.md           # Funding information (only if non-OMSF or additional)

  spontaneous/         # Spontaneous Speech (SPS) only
    transcriptions.md    # Description of the transcription process
    postprocessing.md    # Recommended post-processing steps
    discussion_links.md  # Discussion forum / chat links
    contribute_links.md  # Links to contribute (only if non-standard)
    authors.md           # Datasheet authors
    citation.md          # How to cite this dataset
    funding.md           # Funding information (only if non-OMSF or additional)
```

## Guidelines

- **Only create files you have content for.** Empty files are ignored.
- **`shared/`** fields apply to both SCS and SPS. Write them once here.
- **`contribute_links.md`**: Only needed if the locale has non-standard links.
  Standard Speak/Write/Listen/Review links are added automatically.
- **`community_links.md`**: Only needed if there are additional community links
  beyond the Pontoon translators link (added automatically).
- **`funding.md`**: Only needed for non-OMSF or additional funding. OMSF
  funding is injected automatically for locales in `metadata/funding.tsv`.
- Write plain Markdown. No Jinja2 or HTML needed.
- See `content/_example/` for a filled-in reference.
