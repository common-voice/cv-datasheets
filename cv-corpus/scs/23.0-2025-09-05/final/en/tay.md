# *Atayal* &mdash; Atayal (`tay`)
> This datasheet has been generated automatically, we would love to include more information, if you would like to help out, [get in touch](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)!

 This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Atayal (`tay`). The dataset contains 7857 clips representing 13 hours of recorded
speech (12 hours validated) from 18 speakers.

本語料集包含泰雅族語推組織的 18 位錄音者，錄音範圍為十二年國教課程原住民族語文教材第 1 至 9 階課文文本。

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->
泰雅語（Atayal / Tayal），臺灣原住民泰雅族的語言

### Variants
<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->
本語音語料庫包含以下方言語群

- 賽考利克泰雅語 Squliq Atayal (`squliq`)
- 澤敖利泰雅語 Sʼuli Atayal (`ciuli`)
- 宜蘭澤敖利泰雅語 Klesan Atayal (`klesan`)
- 四季泰雅語 Skikun Atayal (`cquliq`)
- 汶水泰雅語 Matuʼuwal Atayal (`matuuwal`)
- 萬大泰雅語 Plngawan Atayal (`pingawan`)

## Demographic information
The dataset includes the following distribution of age and gender.
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->

### Gender
Self-declared gender information, percentage refers to the number of clips annotated with this gender.

（2025 年初 MozTW / 台灣維基協會族語錄音專案，並未登錄此資訊，故此資料相對不準確。）

| Gender | Pertentage |
|-|-|
| Undefined | 22.0% |
| Female Feminine | 46.0% |
| Do Not Wish To Say | 33.0% |
<!-- {{GENDER_TABLE}} -->
<!-- @ AUTOMATICALLY GENERATED @ -->
<!-- | Gender | Frequency |
|--------|-----------|
| male, masculine | ? |
| undeclared | ? |
| female, feminine | ? | -->

### Age
Self-declared age information, percentage refers to the number of clips annotated with this age band.

（2025 年初 MozTW / 台灣維基協會族語錄音專案，並未登錄此資訊，故此資料相對不準確。）

| Age Band | Percentage |
|-|-|
| Undefined | 33.0% |
| Twenties | 22.0% |
| Fourties | 13.0% |
| Fifties | 18.0% |
| Sixties | 15.0% |
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
The official data splits for modelling this language are as follows. Of the validated clips, 34.94% are included in the splits.

 | Split | Count |
|-|-|
| Train | 1299 |
| Test | 851 |
| Dev | 452 |

## Text corpus
The text corpus contains `3867` sentences, of which `3790` are validated, `77` are invalidated and `0` are reported.
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
kinba’an na knxan binkisan
pyux balay rawin muw
payat kaka mki sku s’ka mayah
ya waṟal hunco’ buse’ ingkaṟalan hani la?
bali nanak ku’ muwani iwana makibaq ’i’ matiq
```
<!-- {{SENTENCES_SAMPLE}} -->

### Sources
<!-- {{SOURCES_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- A list of sentence sources, can be curated to the top-N -->
錄音文本取自《十二年國教原住民族語文教材》第一至九階課文之族語（羅馬字）內容，經[中華民國教育部國民及學前教育署](https://www.k12ea.gov.tw)（K-12 Education Administration, Ministry of Education, Taiwan ROC）授權，由台灣維基媒體協會整理後上傳。特別感謝時任教育部政務次長葉丙成協助協調授權事宜。

賽考利克泰雅語另包含[泰雅爾語聖經](https://cb.fhl.net)選句共 115 句，感謝財團法人台灣聖經公會（The Bible Society in Taiwan）授權。

在族語專案錄音過程中，我們發現部分文本存在文意不符、單詞或拼寫錯誤等情況。因 Common Voice 系統限制，相關內容未能事先更正仍直接進行錄製。錄音者與教材之間是為共同協作關係，特此說明。

### Text domains
| Domain | Count |
|-|-|
| Undefined | 291 |
| General | 9021 |
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
Mozilla 台灣社群 (MozTW) Common Voice 專案網站： [https://moztw.org/commonvoice/](https://moztw.org/commonvoice/)

任何問題與建議、協助推廣、捐贈語料，或其他合作需求，請透過以下社群頻道與我們討論：

- [Telegram group](https://t.me/+gvmHEcAtd-IwNzFl)
- [Line group](https://line.me/ti/g/_PLyjCSe_8)

2025 族語錄音計畫參與社群：

- [台灣維基媒體協會 (Wikimedia Taiwan)](https://www.facebook.com/wikimedia.tw)
- [泰雅族語言推廣組織](https://www.kenatayal.org.tw)、[泰雅族語推動組織 Facebook](https://www.facebook.com/p/%E6%B3%B0%E9%9B%85%E6%97%8F%E8%AA%9E%E6%8E%A8%E5%8B%95%E7%B5%84%E7%B9%94-100064743246737/)
- 特別感謝泰雅語推組織 Sugiy‧Tosi 素伊‧多夕老師協助
<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->

### Discussions
<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->
* [Discourse 討論區](https://discourse.mozilla.org/c/voice/zh-tw/286)
* [相關新聞](https://hackmd.io/@moztw/common-voice-news)

### Contribute
* [Speak](https://commonvoice.mozilla.org/tay/speak)
* [Listen](https://commonvoice.mozilla.org/tay/listen)
<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->

## Acknowledgements

### Datasheet authors
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->
 - Irvin Chen (MozTW 社群聯絡人) <irvin@moztw.org>

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