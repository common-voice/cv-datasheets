# *Drekay* &mdash; Rukai (`dru`)
> This datasheet has been generated automatically, we would love to include more information, if you would like to help out, [get in touch](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)!

 This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Rukai (`dru`), 含茂林語 (Teldreka), 萬山語 ('Oponoho). The dataset contains 6692 clips representing 11 hours of recorded
speech (11 hours validated) from 20 speakers.

本語料集包含排灣經典工作室協助招募的魯凱族，以及茂林及萬山語社群總計 20 位錄音者。
錄音範圍為十二年國教課程原住民族語文教材第 1 至 9 階課文文本。

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->
魯凱語（Drekay）、茂林語（Teldreka）、萬山語（'Oponoho），臺灣原住民魯凱族的語言

### Variants
<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->
本語音語料庫包含以下方言語群

- 東魯凱語 Eastern Rukai (`taromak`)
- 霧臺魯凱語 Wutai Rukai (`veday`)
- 大武魯凱語 Dawu Rukai (`labuane`)
- 萬山語 Oponoho (`oponoho`)
- 茂林語 Teldreka (`teldreka`)

## Demographic information
The dataset includes the following distribution of age and gender.
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->

### Gender
Self-declared gender information, percentage refers to the number of clips annotated with this gender.

（2025 年初 MozTW / 台灣維基協會族語錄音專案，並未登錄此資訊，故此資料相對不準確。）

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

（2025 年初 MozTW / 台灣維基協會族語錄音專案，並未登錄此資訊，故此資料相對不準確。）

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

錄音文本取自《十二年國教原住民族語文教材》第一至九階課文之族語（羅馬字）內容，經[中華民國教育部國民及學前教育署](https://www.k12ea.gov.tw)（K-12 Education Administration, Ministry of Education, Taiwan ROC）授權，由台灣維基媒體協會整理後上傳。特別感謝時任教育部政務次長葉丙成協助協調授權事宜。

部分霧台魯凱語（`veday`）文本，由國⽴台灣⼤學語⾔學研究所《[台⼤台灣南島語語料庫](https://corpus.linguistics.ntu.edu.tw/)》（NTU Corpus of Formosan Languages, Graduate Institute of Linguistics, National Taiwan University）提供。感謝宋麗梅老師協助。

多納語、萬山語、茂林語另包含[馬可福音](https://cb.fhl.net)選句各 59 句，感謝財團法人台灣聖經公會（The Bible Society in Taiwan）授權。

在族語專案錄音過程中，我們發現部分文本存在文意不符、單詞或拼寫錯誤等情況。因 Common Voice 系統限制，相關內容未能事先更正仍直接進行錄製。錄音者與教材之間是為共同協作關係，特此說明。

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

Mozilla 台灣社群 (MozTW) Common Voice 專案網站： [https://moztw.org/commonvoice/](https://moztw.org/commonvoice/)

任何問題與建議、協助推廣、捐贈語料，或其他合作需求，請透過以下社群頻道與我們討論：

- [Telegram group](https://t.me/+gvmHEcAtd-IwNzFl)
- [Line group](https://line.me/ti/g/_PLyjCSe_8)

2025 族語錄音計畫參與社群：

- [台灣維基媒體協會 (Wikimedia Taiwan)](https://www.facebook.com/wikimedia.tw)
- [排灣經典 Payuan Classic](https://www.facebook.com/PayuanClassic/)
- 特別感謝排灣經典葉王靖 kuliw 協助招募與錄音事宜
- 
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
* [Speak](https://commonvoice.mozilla.org/dru/speak)
* [Listen](https://commonvoice.mozilla.org/dru/listen)
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