# *華語（台灣）* &mdash; Chinese (Taiwan) (`zh-TW`)
> This datasheet has been generated automatically, we would love to include more information, if you would like to help out, [get in touch](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)!

 This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Chinese (Taiwan) (`zh-TW`). The dataset contains 139721 clips representing 131 hours of recorded
speech (77 hours validated) from 2291 speakers.

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->
Taiwan Mandarin in Traditional Chinese script.

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
| Undefined | 29.0% |
| Male Masculine | 49.0% |
| Female Feminine | 22.0% |
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
| Undefined | 27.0% |
| Twenties | 30.0% |
| Thirties | 19.0% |
| Teens | 6.0% |
| Fourties | 9.0% |
| Fifties | 9.0% |
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
The official data splits for modelling this language are as follows. Of the validated clips, 20.71% are included in the splits.

 | Split | Count |
|-|-|
| Train | 7356 |
| Test | 5100 |
| Dev | 5100 |

## Text corpus
The text corpus contains `21589` sentences, of which `20748` are validated, `841` are invalidated and `179` are reported.
<!-- {{TEXT_CORPUS_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- An overview of the text corpus, with information such as average length (in characters and words) of validated sentences. -->

Most of the Traditional Chinese text corpus is curated in the MozTW CC0 Sentences repository: https://github.com/moztw/cc0-sentences.

Summary statistics (see the repo for methods):

> There are 3573 characters in the corpus, covering about 85.6% of the MOU 2015 common chars data (MoE 2015 common characters 99.75% (3593 chars)).
>
> 1046 phonetics are covered, about 66.75% of the total phonetics in CnsPhonetic2016-08v2.cin.

We welcome more everyday sentences in Mandarin (Traditional Chinese). Please reach out via the community links below.

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
簽到
新一批語音資料
大家戰力好強
底迪和姊姊的戰爭
抖內起來
```
<!-- {{SENTENCES_SAMPLE}} -->

### Sources
<!-- {{SOURCES_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- A list of sentence sources, can be curated to the top-N -->

The text corpus is built by the Mozilla Taiwan community, the g0v community, and other open-source contributors.

### Text domains
| Domain | Count |
|-|-|
| Undefined | 138740 |
| Agriculture Food | 12 |
| Automotive Transport | 271 |
| Finance | 100.0% |
| Service Retail | 150 |
| General | 605 |
| Healthcare | 21 |
| History Law Government | 164 |
| Language Fundamentals | 8 |
| Media Entertainment | 165 |
| Nature Environment | 11 |
| News Current Affairs | 42 |
| Technology Robotics | 257 |
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

Mozilla 台灣社群 (MozTW) Common Voice 專案網站： [https://moztw.org/commonvoice/](https://moztw.org/commonvoice/)

任何問題與建議、協助推廣、捐贈語料，或其他合作需求，請透過以下社群頻道與我們討論：

- [Telegram group](https://t.me/+gvmHEcAtd-IwNzFl)
- [Line group](https://line.me/ti/g/_PLyjCSe_8)
- 

### Discussions
<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->

* Discourse forum (zh-TW): https://discourse.mozilla.org/c/voice/zh-tw/286
* Related news: https://hackmd.io/@moztw/common-voice-news

### Contribute
* [Speak](https://commonvoice.mozilla.org/zh-TW/speak)
* [Listen](https://commonvoice.mozilla.org/zh-TW/listen)
* Donate your sentences — If you would like to donate text you own (e.g., original writing) for recording, please contact Irvin (irvin@moztw.org) or discuss in the Line/Telegram groups above.

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
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.