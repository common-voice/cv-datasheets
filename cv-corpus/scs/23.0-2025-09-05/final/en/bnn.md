# *Bunun* &mdash; Bunun (`bnn`)
> This datasheet has been generated automatically, we would love to include more information, if you would like to help out, [get in touch](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)!

 This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Bunun (`bnn`). The dataset contains 8220 clips representing 12 hours of recorded
speech (11 hours validated) from 18 speakers.

The recordings cover the Indigenous Languages Curriculum (K-12) textbook materials, level 1 to 9.

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->
Bunun is the language of the Bunun people, one of the Indigenous peoples of Taiwan.

### Variants
<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->

This speech corpus includes the following dialect groups:

- Takituduh (`takitudu`)
- Takibakha (`bakha`)
- Isbukun (`bubukun`)
- Takbanuaz (`banuaz`)
- Takivatan (`vatan`)

## Demographic information
The dataset includes the following distribution of age and gender.
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->

### Gender
Self-declared gender information, percentage refers to the number of clips annotated with this gender.

(The MozTW / Wikimedia Taiwan Indigenous language recording project in early 2025 did not collect this information; therefore, these figures may be relatively inaccurate.)

| Gender | Pertentage |
|-|-|
| Undefined | 18.0% |
| Male Masculine | 6.0% |
| Female Feminine | 41.0% |
| Do Not Wish To Say | 35.0% |
<!-- {{GENDER_TABLE}} -->
<!-- @ AUTOMATICALLY GENERATED @ -->
<!-- | Gender | Frequency |
|--------|-----------|
| male, masculine | ? |
| undeclared | ? |
| female, feminine | ? | -->

### Age
Self-declared age information, percentage refers to the number of clips annotated with this age band.

(The MozTW / Wikimedia Taiwan Indigenous language recording project in early 2025 did not collect this information; therefore, these figures may be relatively inaccurate.)

| Age Band | Percentage |
|-|-|
| Undefined | 60.0% |
| Fifties | 6.0% |
| Sixties | 34.0% |
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
The official data splits for modelling this language are as follows. Of the validated clips, 40.67% are included in the splits.

 | Split | Count |
|-|-|
| Train | 1040 |
| Test | 960 |
| Dev | 958 |

## Text corpus
The text corpus contains `3175` sentences, of which `3167` are validated, `8` are invalidated and `3` are reported.
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
Pinunpia’in nitu naipun tu maku’aqin dau naipa laupaku?
Inaam tu lumaq
pintamasazun saam tu
Niap asu tu maima’aq a buqul sintas’i?
Asa tu makadim mas haini-anan, aupa kadukuun laupakadau a hanian
```
<!-- {{SENTENCES_SAMPLE}} -->

### Sources
<!-- {{SOURCES_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- A list of sentence sources, can be curated to the top-N -->

The recording texts are taken from the Indigenous Languages Curriculum (K-12) textbook content (in romanization) for stages 1 to 9. They were uploaded by Wikimedia Taiwan under authorization from the K-12 Education Administration, Ministry of Education (Taiwan, ROC) at https://www.k12ea.gov.tw. Special thanks to Deputy Minister Ping-Cheng Yeh for facilitating the authorization.

For the Isbukun dialect, 118 selected verses from the Bunun Bible (see https://cb.fhl.net) are also included, thanks to authorization by The Bible Society in Taiwan.

During the recording project, we noticed that some text contained semantic mismatches or typographical/spelling mistakes. Due to Common Voice system constraints, these issues could not be fixed in advance and recordings proceeded as-is. Recorders and textbook providers collaborated closely; we note this for transparency.

### Text domains
| Domain | Count |
|-|-|
| Undefined | 273 |
| General | 10094 |
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
<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->

MozTW (Mozilla Taiwan) Common Voice project site: https://moztw.org/commonvoice/

For questions, suggestions, outreach, donating text, or collaboration, please reach out via:

- Telegram group: https://t.me/+gvmHEcAtd-IwNzFl
- Line group: https://line.me/ti/g/_PLyjCSe_8

Communities involved in the 2025 Indigenous language recording project:

- Wikimedia Taiwan: https://www.facebook.com/wikimedia.tw
- Special thanks to Bunun teacher Aping (Wu A-Hao) for her support

### Discussions
<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->

* Discourse forum (zh-TW): https://discourse.mozilla.org/c/voice/zh-tw/286
* Related news: https://hackmd.io/@moztw/common-voice-news

### Contribute
* [Speak](https://commonvoice.mozilla.org/bnn/speak)
* [Listen](https://commonvoice.mozilla.org/bnn/listen)

<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->

## Acknowledgements

### Datasheet authors
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->

- Irvin Chen (MozTW Community Contact) <irvin@moztw.org>

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