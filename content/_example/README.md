# Example: Klingon (`tlh`)

This is a fictional reference example showing how to fill in datasheet
content for a locale. Use it as a guide when creating content for your
own locale.

## Important: Edit Modes

Some fields are **additive** -- they accumulate content over time across
releases. When editing these fields, **add your contribution below the
existing content**. Do not remove or replace previous entries.

Other fields are **descriptive** -- they describe the current state and
can be rewritten or improved freely.

Some fields are also **mergeable** -- the final datasheet shows both your
community-written content and auto-generated data. Mergeable fields
follow the same additive/descriptive edit rules.

See the field list in `content/_template/README.md` for which fields
are additive, descriptive, and mergeable.

### Example of additive editing

If `sources.md` already contains:

```markdown
* Common Voice Wiki Sentences (v17.0-v21.0)
* Tatoeba project sentences (v22.0)
```

And you want to add a new source, append it:

```markdown
* Common Voice Wiki Sentences (v17.0-v21.0)
* Tatoeba project sentences (v22.0)
* Klingon Language Institute corpus (v24.0)
```

Do **not** replace the file with only your new entry.

### Versioning in additive fields

Use version references to help readers track when content was added:

```markdown
* v25.0 New Author -- role description
* v21.0-v24.0 Previous Author -- role description
```

This applies to `authors.md`, `funding.md`, `sources.md`, and
`citation.md`.

### Fields with auto-generated defaults

Three link fields always include auto-generated default links in the
final datasheet. Your community content appears **before** the defaults:

- `community_links.md` -- Pontoon and Communities links are added
- `discussion_links.md` -- Matrix, Discourse, Discord, Telegram links
  are added
- `contribute_links.md` -- Standard contribution links are added
  (Speak/Write/Listen/Review for SCS, question/transcription links
  for SPS)

Do **not** duplicate default links in your community files. Only add
links that are specific to your community.

## Directory Layout

- `shared/` files apply to both Scripted Speech (SCS) and Spontaneous
  Speech (SPS) datasets.
- `scripted/` and `spontaneous/` files apply only to their respective
  modality.
- You only need to create files you have content for. Empty files are
  ignored by the compile script.
