# Content Template

Use this template when adding or updating datasheet content for a locale.
Copy the relevant directories into `content/locales/{locale}/` and fill in
the files you want to contribute.

## Directory structure

Fields marked with `+` are **additive** -- extend them, do not replace previous
content. Fields marked with `~` are **descriptive** -- can be rewritten freely.
Fields marked with `*` are **mergeable** -- the final datasheet shows both your
content and auto-generated data.

```txt
content/locales/{locale}/
  shared/              # Language-level fields (shared across SCS and SPS)
  ~ description.md       # About the language
  *~ variants.md         # Dialect / regional variants
  *~ accents.md          # Speaker accent options
  ~ writing_system.md    # Writing system description
  ~ alphabet.md          # Symbol table / alphabet list
  *+ community_links.md  # Links to community resources

  scripted/            # Scripted Speech (SCS) only
  *~ corpus.md           # Description of the text corpus
  *+ sources.md          # Sources of the text corpus
  *~ text_domain.md      # Text domain descriptions
  ~ processing.md        # Text processing applied to the corpus
  ~ postprocessing.md    # Recommended post-processing steps
  *~ discussion_links.md # Discussion forum / chat links
  *~ contribute_links.md # Additional contribution links
  + authors.md           # Datasheet authors / community leads
  + citation.md          # How to cite this dataset
  + funding.md           # Funding information (only if non-OMSF or additional)

  spontaneous/         # Spontaneous Speech (SPS) only
  *~ transcriptions.md   # Description of the transcription process
  ~ postprocessing.md    # Recommended post-processing steps
  *~ discussion_links.md # Discussion forum / chat links
  *~ contribute_links.md # Additional contribution links
  + authors.md           # Datasheet authors / community leads
  + citation.md          # How to cite this dataset
  + funding.md           # Funding information (only if non-OMSF or additional)
```

## Additive vs Descriptive Fields

**Additive (`+`)** fields build up over time across releases. When editing
these files, **add your entries above the existing content** -- do not remove
or replace previous contributions. Include version references where helpful
(e.g. `v24.0`, `v22.0-present`).

Examples of additive content:

- `sources.md` -- each new text source is a new list entry
- `authors.md` -- new contributors are appended with their role and version range
- `citation.md` -- new papers referencing the dataset are added

**Descriptive (`~`)** fields describe the current state of the language or
process. These can be rewritten or improved freely -- they represent the latest
understanding, not a historical record.

**Mergeable (`*`)** fields show auto-generated data alongside your content
in the final datasheet. Each mergeable field is still either additive (`*+`)
or descriptive (`*~`) -- follow the same edit rules above.

## Fields with Auto-Generated Defaults

Three link fields always include default links in the final datasheet.
Your community content appears **before** the defaults. Do not duplicate
the default links in your files.

- **`community_links.md`**: Pontoon translators + Communities page are added
  automatically. Only add community-specific links (forums, Discord, etc.).
- **`discussion_links.md`**: Matrix, Discourse, Discord, and Telegram links
  are added automatically. Only add community-specific discussion channels.
- **`contribute_links.md`**: Standard contribution links are added
  automatically (Speak/Write/Listen/Review for SCS, question/transcription
  links for SPS). Only add community-specific contribution paths.

## Guidelines

- **Only create files you have content for.** Empty files are ignored.
- **`shared/`** fields apply to both SCS and SPS. Write them once here.
- **`funding.md`**: Only needed for non-OMSF or additional funding. OMSF
  funding is injected automatically for locales in `metadata/funding.tsv`.
- Write plain Markdown. No Jinja2 or HTML needed.
- See `content/_example/` for a filled-in reference with additive patterns.
