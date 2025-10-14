# *台語* &mdash; Taiwanese (Minnan) (`nan-tw`)
> This datasheet has been generated automatically, we would love to include more information, if you would like to help out, [get in touch](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)!

 This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Taiwanese (Minnan) (`nan-tw`). The dataset contains 31951 clips representing 24 hours of recorded
speech (21 hours validated) from 290 speakers.

請特別注意：本語音語料集為「*漢字——語音資料集*」。
本語料集文本語料以漢字為主，同時括號標注台羅或白話字參考發音。

本語料及錄音者為主要來自台灣的個別志工參與者。

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->

臺灣話（白話字：Tâi-oân-ōe；臺羅：Tâi-uân-uē），又稱為台語／臺語或臺灣閩南語，通行於臺灣及澎湖群島，中華民國（臺灣）國家語言之一。

### Variants
<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->

於 v23.0 版本開始，Common Voice 台語版本允許錄音與文本貢獻者選擇（非必選）以下書寫系統變體（Variant）。但目前文本語料仍以兩者混合（非特定系統）為大宗。

- 白話字（POJ） (`pehoeji`)
- 台羅（TL） (`tailo`)

如欲協助更新現有語料，請往下到 Community 欄目與我們聯繫。

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

此錄音集大部分文本語料整理於：[MozTW CC0 語料庫](https://github.com/moztw/cc0-sentences)，主要來自 MozTW ／ g0v 社群個別參與者。

由於目前缺乏公共授權（無已知授權限制）的台語「句子」文本語料，Common Voice 台語錄音目前以「單詞」為大宗。

我們亟需更多「日常生活用句」，歡迎捐贈您以台語書寫的作品。請參考下方社群頻道資訊與我們聯繫。

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

文本語料由 Mozilla 台灣社群、g0v 社群、及其他開放原始碼運動參與者共同建立。

早期的台語語料主要來自「2016-itaigi華台對照典」。請參考[資料來源與授權](https://github.com/moztw/cc0-sentences/tree/master/nan-TW#資料來源與授權)了解原始資料出處。

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

由於目前缺乏公共授權的「句子」資料，Common Voice 台語語料目前仍以「單詞」為大宗。

我們亟需更多「日常生活用句」，歡迎捐贈您以台語書寫的作品。請參考 [社群頻道資訊](#community-links) 與我們聯繫。

### Processing
<!-- {{PROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- How has the text data been processed -->

### Recommended post-processing
<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What should people do before they use the data, for example Unicode normalisation -->

因為句子、單詞所標示的羅馬字為參考用，且 a) 混用台羅與白話字系統，b) 也未能標出所有腔調的發音，顧無法作為實際錄音者發音之對應標注。

我們建議使用前先行移除用`（）`包夾的參考發音，僅取用漢字部分。

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

### Discussions
<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->

* [Discourse 討論區](https://discourse.mozilla.org/c/voice/zh-tw/286)
* [相關新聞](https://hackmd.io/@moztw/common-voice-news)

### Contribute
* [Speak](https://commonvoice.mozilla.org/nan-tw/speak)
* [Listen](https://commonvoice.mozilla.org/nan-tw/listen)
* 捐出你的句子 - 如您有意願捐出你擁有的文本語料（例如您的個人創作）供參與者錄音，請先聯絡 Irvin （ irvin@moztw.org ）或於以上 Line / Telegram 群組討論。

<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->

## Acknowledgements

### Datasheet authors
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->

 - Irvin Chen (MozTW 社群聯絡人) <irvin@moztw.org>
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