# *اباسیْن کوستَیں* &mdash; Indus Kohistani (`mvy`)
This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Indus Kohistani (`mvy`). The dataset contains 18475 clips representing 26 hours of recorded
speech (23 hours validated) from 56 speakers.

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
| Undefined | 100.0% |

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
| Undefined | 4.0% |
| Twenties | 39.0% |
| Thirties | 47.0% |
| Fourties | 6.0% |
| Fifties | 3.0% |

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

The official data splits for modelling this language are as follows. Of the validated clips, 39.64% are included in the splits.

 | Split | Count |
|-|-|
| Train | 2558 |
| Test | 2076 |
| Dev | 1946 |


## Text corpus

The text corpus contains `6856` sentences, of which `6634` are validated, `222` are invalidated and `90` are reported.
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
او ڙھا تیں بال لر نی تھی، نہ مہ زُنازُو تیں مُخالیۡفت کرم تُھو
چے سِوَیں ژؤن٘دُناں مُختلف حالتیُوں مہ
ادا کرَیں لاقَت لہ تَنہی نی ہُوئ تھی۔
دویُوں مِثال ݜے تھُو چے کماݜ لازمی کمہۡ (واجب)
مُوڙ (چُن٘ڑ بول)، گُو (تھُل بول) یا
```

<!-- {{SENTENCES_SAMPLE}} -->

### Sources
<!-- {{SOURCES_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- A list of sentence sources, can be curated to the top-N -->

### Text domains

| Domain | Count |
|-|-|
| Undefined | 18245 |
| Agriculture Food | 33 |
| General | 108 |
| History Law Government | 78 |
| Media Entertainment | 11 |
| Nature Environment | 7 |
| Technology Robotics | 9 |

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

* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/mvy/common-voice/contributors/)

<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->

### Discussions
<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->

### Contribute

* [Speak](https://commonvoice.mozilla.org/mvy/speak)
* [Write](https://commonvoice.mozilla.org/mvy/write)
* [Listen](https://commonvoice.mozilla.org/mvy/listen)
* [Review](https://commonvoice.mozilla.org/mvy/review)
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

This dataset was partially funded by the *Open Multilingual Speech Fund* managed by Mozilla Common Voice.
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.