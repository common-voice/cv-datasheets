# *ⵜⴰⵎⴰⵣⵉⵖⵜ* &mdash; Tamazight (`zgh`)
> This datasheet has been generated automatically, we would love to include more information, if you would like to help out, [get in touch](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)!

This datasheet is for version 24.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Tamazight (`zgh`). The dataset contains 2169 clips representing 2.1 hours of recorded
speech (1.36 hours validated) from 38 speakers.

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->

### Variants
<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->

## Demographic information
The dataset includes the following distribution of age and gender.
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->

### Gender
Self-declared gender information, percentage refers to the number of clips annotated with this gender.
| Gender | Pertentage |
|-|-|
| Undefined | 15.0% |
| Male Masculine | 82.0% |
| Female Feminine | 3.0% |

<!-- {{GENDER_TABLE}} -->
<!-- @ AUTOMATICALLY GENERATED @ -->
<!-- | Gender | Frequency |
|--------|-----------|
| male, masculine | ? |
| undeclared | ? |
| female, feminine | ? | -->

### Age
Self-declared age information, percentage refers to the number of clips annotated with this age band.
| Age Band | Percentage |
|-|-|
| Undefined | 10.0% |
| Twenties | 38.0% |
| Thirties | 52.0% |

<!-- {{AGE_TABLE}} -->
<!-- @ AUTOMATICALLY GENERATED @ -->
<!-- | Age band | Frequency |
|----------|-----------|
| teens | ? |
| twenties | ? |
| thirties | ? |
| fourties | ? |
| fifties | ? |
   ...if other age ranges are present in your data, add rows... -->

## Data splits for modelling
The official data splits for modelling this language are as follows. Of the validated clips, 100.00% are included in the splits.

 | Split | Count |
|-|-|
| Train | 855 |
| Test | 230 |
| Dev | 297 |

## Text corpus
The text corpus contains `3087` sentences, of which `2737` are validated, `350` are invalidated and `6` are reported.
<!-- {{TEXT_CORPUS_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- An overview of the text corpus, with information such as average length (in characters and words) of validated sentences. -->

### Writing system
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

#### Symbol table
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->

### Sample
There follows a randomly selected sample of five sentences from the corpus.

```
ⵜⵍⵍⴰ ⵍⵇⵀⵡⴰ ⵏⴳⵔ ⵜⴱⵓⵙⵟⴰ ⴷ ⵜⵙⴰⵙⴼⵔⵜ.
ⵎⵉⵏ ⵉⵕⵥⴰⵏ ⵡⴰ?
ⵉⵙⵙⵉⵜⵎ ⵜⵓⵎ ⵎⵜⴰⴷⴷ ⵉⵙ ⵀⵍⵍⵉ ⵓⵔ ⵉⵥⵕⵉ.
ⴰⵡⴷ ⵢⴰⵏ ⵓⵔ ⵉⵎⵍⵉ ⵎⴰⴷ ⵓⴽⴰⵏ ⵖⵉⵏⵏ ⵉⵙⴽⴰⵔ ⴼⴰⴹⵉⵍ.
ⴰⵡⴰ ⵉⵙⵙⵓⵛⴽⴰ ⵜⵜ ⵉⴷ ⴳⵉⵙ, ⵉⵎⵔⵣ ⴰⵙ ⵙ ⵢⴰⵏ ⵓⴳⴳⵓⵏ ⵎⵇⵇⵓⵔⵏ.
```
<!-- {{SENTENCES_SAMPLE}} -->

### Sources
<!-- {{SOURCES_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- A list of sentence sources, can be curated to the top-N -->

### Text domains

| Domain | Count |
|-|-|
| Undefined | 2126 |
| General | 34 |
| Healthcare | 3 |
| Language Fundamentals | 5 |
| Technology Robotics | 100.0% |

<!-- {{TEXT_DOMAIN_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What text domains are represented in the corpus? -->

### Processing
<!-- {{PROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- How has the text data been processed -->

### Recommended post-processing
<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What should people do before they use the data, for example Unicode normalisation -->

### Fields
Each row of a `tsv` file represents a single audio clip, and contains the following information:

* `client_id` - hashed UUID of a given user
* `path` - relative path of the audio file
* `text` - supposed transcription of the audio
* `up_votes` - number of people who said audio matches the text
* `down_votes` - number of people who said audio does not match text
* `age` - age of the speaker[^1]
* `gender` - gender of the speaker[^1]
* `accent` - accent of the speaker[^1]
* `segment` - if sentence belongs to a custom dataset segment, it will be listed here

#### 
[^1]: For a full list of age, gender, and accent options, see the
[demograpics
spec](https://github.com/common-voice/common-voice/blob/main/web/src/stores/demographics.ts). These
will only be reported if the speaker opted in to provide that
information.

## Get involved!

### Community links
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/zgh/common-voice/contributors/)
<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->

### Discussions
<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->

### Contribute
* [Speak](https://commonvoice.mozilla.org/zgh/speak)
* [Write](https://commonvoice.mozilla.org/zgh/write)
* [Listen](https://commonvoice.mozilla.org/zgh/listen)
* [Review](https://commonvoice.mozilla.org/zgh/review)
<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->

## Acknowledgements

### Datasheet authors
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->

### Citation guidelines
<!-- {{CITATION_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you published a paper and would like people to cite it, you can include the BiBTeX here -->

### Funding
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.