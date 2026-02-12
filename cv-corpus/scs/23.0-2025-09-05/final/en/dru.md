# *Drekay* &mdash; Rukai (`dru`)
> This datasheet has been generated automatically, we would love to include more information, if you would like to help out, [get in touch](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)!

 This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Rukai (`dru`) (including Teldreka and 'Oponoho). The dataset contains 6692 clips representing 11 hours of recorded
speech (11 hours validated) from 20 speakers.

This dataset includes 20 speakers from the Rukai community recruited with support from Payuan Classic Studio, as well as speakers from the Teldreka and Oponoho communities. The recordings cover the Indigenous Languages Curriculum (K-12) textbook materials, level 1 to 9.

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->
Rukai (Drekay), including Teldreka and Oponoho, are Indigenous languages of the Rukai people in Taiwan.

### Variants
<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->
This speech corpus includes the following dialect groups:

- Eastern Rukai (`taromak`)
- Wutai Rukai (`veday`)
- Dawu Rukai (`labuane`)
- Oponoho (`oponoho`)
- Teldreka (`teldreka`)

## Demographic information
The dataset includes the following distribution of age and gender.
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->

### Gender
Self-declared gender information, percentage refers to the number of clips annotated with this gender.

(The MozTW / Wikimedia Taiwan Indigenous language recording project in early 2025 did not collect this information; therefore, these figures may be relatively inaccurate.)

| Gender | Pertentage |
|-|-|
| Female Feminine | 12.0% |
| Do Not Wish To Say | 87.0% |
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
| Undefined | 88.0% |
| Fourties | 12.0% |
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
The official data splits for modelling this language are as follows. Of the validated clips, 45.07% are included in the splits.

 | Split | Count |
|-|-|
| Train | 1074 |
| Test | 957 |
| Dev | 933 |

## Text corpus
The text corpus contains `4344` sentences, of which `3867` are validated, `477` are invalidated and `2` are reported.
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
wamiso no si’a?
syaakay lwadrame na baa no sa’avelevelini
mbalte dra ki nina ka emecɨ thkebe?
sesane ki singsi ka paigo’o namiya tibolay
Taiwan ka ’iyakay nyani madraw na egeege?
```
<!-- {{SENTENCES_SAMPLE}} -->

### Sources
<!-- {{SOURCES_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- A list of sentence sources, can be curated to the top-N -->

The recording texts are taken from the Indigenous Languages Curriculum (K-12) textbook content (in romanization) for levels 1 to 9, uploaded by Wikimedia Taiwan under authorization from the K-12 Education Administration, Ministry of Education (Taiwan, ROC): https://www.k12ea.gov.tw. Special thanks to Deputy Minister Ping-Cheng Yeh for facilitating the authorization.

Some Wutai Rukai (`veday`) texts are provided by the NTU Corpus of Formosan Languages (Graduate Institute of Linguistics, National Taiwan University): https://corpus.linguistics.ntu.edu.tw/ (thanks to Prof. Li-May Sung for assistance).

For Tona, Oponoho and Teldreka, 59 selected verses each from the Gospel of Mark (see https://cb.fhl.net) are included, with authorization from The Bible Society in Taiwan.

During the recording project, we noticed certain semantic mismatches and typographical/spelling issues in parts of the text. Due to Common Voice system constraints, these were not corrected in advance and recordings proceeded as-is. Recorders and textbook providers collaborated closely; this note is provided for transparency.

### Text domains
| Domain | Count |
|-|-|
| Undefined | 70 |
| General | 10031 |
| Language Fundamentals | 1759 |
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

MozTW (Mozilla Taiwan) Common Voice project site: https://moztw.org/commonvoice/

For questions, suggestions, outreach, donating text, or collaboration, please reach out via:

- Telegram group: https://t.me/+gvmHEcAtd-IwNzFl
- Line group: https://line.me/ti/g/_PLyjCSe_8

Communities involved in the 2025 Indigenous language recording project:

- Wikimedia Taiwan: https://www.facebook.com/wikimedia.tw
- Payuan Classic: https://www.facebook.com/PayuanClassic/
- Special thanks to Kuliw from Payuan Classic for recruitment and recording support
- 
<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->

### Discussions
<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->

* Discourse forum (zh-TW): https://discourse.mozilla.org/c/voice/zh-tw/286
* Related news: https://hackmd.io/@moztw/common-voice-news

### Contribute
* [Speak](https://commonvoice.mozilla.org/dru/speak)
* [Listen](https://commonvoice.mozilla.org/dru/listen)
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