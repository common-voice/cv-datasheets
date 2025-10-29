# *台語* &mdash; Taiwanese (Minnan) (`nan-tw`)
> This datasheet has been generated automatically, we would love to include more information, if you would like to help out, [get in touch](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)!

 This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Taiwanese (Minnan) (`nan-tw`). The dataset contains 31951 clips representing 24 hours of recorded
speech (21 hours validated) from 290 speakers.

Please note: This speech dataset is a Han character–speech dataset.
The text corpus primarily uses Han characters, with bracketed TL/POJ romanization as reference pronunciations.

The corpus and speakers are primarily contributed by individual volunteers in Taiwan.

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->

Taiwanese (POJ: Tâi-oân-ōe; TL: Tâi-uân-uē), also known as Tai-gi (台語/臺語) or Taiwanese Minnan (臺灣閩南語), is spoken across Taiwan and the Penghu archipelago, and is one of Taiwan’s national languages.

### Variants
<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->

Starting from v23.0, the Taiwanese (nan-tw) locale allows (optional) selection of the following writing variants; however, most texts are still a mixture of both systems:

- POJ (`pehoeji`)
- TL (`tailo`)

If you’d like to help curate or update the existing texts, please see the Community section below.

## Demographic information
The dataset includes the following distribution of age and gender.
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->

### Gender
Self-declared gender information, percentage refers to the number of clips annotated with this gender.
| Gender | Pertentage |
|-|-|
| Undefined | 26.0% |
| Male Masculine | 63.0% |
| Female Feminine | 11.0% |
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
| Undefined | 13.0% |
| Twenties | 50.0% |
| Thirties | 15.0% |
| Teens | 1.0% |
| Fourties | 17.0% |
| Fifties | 1.0% |
| Sixties | 2.0% |
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
The official data splits for modelling this language are as follows. Of the validated clips, 81.31% are included in the splits.

 | Split | Count |
|-|-|
| Train | 11584 |
| Test | 6523 |
| Dev | 5705 |

## Text corpus
The text corpus contains `27277` sentences, of which `26907` are validated, `370` are invalidated and `226` are reported.
<!-- {{TEXT_CORPUS_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- An overview of the text corpus, with information such as average length (in characters and words) of validated sentences. -->

Most of the text corpus was curated in the MozTW CC0 Sentences repository: https://github.com/moztw/cc0-sentences, primarily contributed by MozTW and g0v community members.

Due to the lack of publicly licensed Taiwanese sentences, recordings in the Taiwanese locale are currently dominated by single-word prompts.

We welcome donations of everyday sentences written in Taiwanese. Please reach out via the community channels below.

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
喙（tshuì）
乞食趕廟公（khit-chia̍h kóaⁿ biō-kong）
鹿港人講話無相仝（Lo̍k-káng lâng kóng uē bô sio-kâng）
功夫到厝，欲食就有（kang-hu kàu tshù, beh tsia̍h tio̍h ū）
人食一點氣（lâng tsia̍h tsi̍t tiám khuì）
```
<!-- {{SENTENCES_SAMPLE}} -->

### Sources
<!-- {{SOURCES_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- A list of sentence sources, can be curated to the top-N -->

The text corpus is built by Mozilla Taiwan community, the g0v community, and other open-source contributors.

Earlier Taiwanese entries were primarily sourced from the “2016-itaigi Mandarin–Taiwanese Dictionary”. See Sources and Licensing at: https://github.com/moztw/cc0-sentences/tree/master/nan-TW#%E8%B3%87%E6%96%99%E4%BE%86%E6%BA%90%E8%88%87%E6%8E%88%E6%AC%8A

### Text domains
| Domain | Count |
|-|-|
| Undefined | 31563 |
| Agriculture Food | 4 |
| Service Retail | 2 |
| General | 327 |
| Healthcare | 100.0% |
| Language Fundamentals | 55 |
| Nature Environment | 55 |
<!-- {{TEXT_DOMAIN_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What text domains are represented in the corpus? -->

Due to the lack of publicly licensed sentence data, recordings in Taiwanese remain predominantly single words.

We welcome more everyday sentences. If you would like to donate your own text (e.g., your original writing), please contact us via the community links below.

### Processing
<!-- {{PROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- How has the text data been processed -->

### Recommended post-processing
<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What should people do before they use the data, for example Unicode normalisation -->

Because the bracketed romanization is for reference only and a) mixes TL and POJ systems, and b) does not consistently mark all tones, it cannot be treated as an authoritative phonetic annotation for the recordings.

We recommend removing bracketed pronunciations `（）` and using only the Han character portion when pre-processing the text.

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

### Discussions
<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->

* Discourse forum (zh-TW): https://discourse.mozilla.org/c/voice/zh-tw/286
* Related news: https://hackmd.io/@moztw/common-voice-news

### Contribute
* [Speak](https://commonvoice.mozilla.org/nan-tw/speak)
* [Listen](https://commonvoice.mozilla.org/nan-tw/listen)
* Donate your sentences — If you would like to donate text you own (e.g., original writing) for recording, please contact Irvin (irvin@moztw.org) or discuss in the Line/Telegram groups above.

<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->

## Acknowledgements

### Datasheet authors
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->

 - Irvin Chen (MozTW Community Contact) <irvin@moztw.org>
 - Dennis Chen (Common Voice Community Facilitator, Wikimedia Taiwan) <dennis@wikimedia.tw>

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