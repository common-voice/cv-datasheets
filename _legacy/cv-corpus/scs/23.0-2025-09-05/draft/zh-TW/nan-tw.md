# *台語* &mdash; Taiwanese (Minnan) (`nan-tw`)

Mozilla Common Voice 23.0 台語（臺灣閩南語，Tâi-gí／Taiwanese Hokkien, `nan-tw`）*文本錄音* 語料集。
本語料集包含 290 位錄音者，共 24 小時的錄音資料，其中 21 小時已驗證（經另二名參與者確認）。

請特別注意：本語音語料集為「*漢字——語音資料集*」。
本語料集文本語料以漢字為主，同時括號標注台羅或白話字參考發音。

本語料及錄音者為主要來自台灣的個別志工參與者。

## 語言

<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->

臺灣話（白話字：Tâi-oân-ōe；臺羅：Tâi-uân-uē），又稱為台語／臺語或臺灣閩南語，通行於臺灣及澎湖群島，中華民國（臺灣）國家語言之一。

### 方言／變體（Variants）

<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->

於 v23.0 版本開始，Common Voice 台語版本允許錄音與文本貢獻者選擇（非必選）以下書寫系統變體（Variant）。但目前文本語料仍以兩者混合（非特定系統）為大宗。

- 白話字（POJ） (`pehoeji`)
- 台羅（TL） (`tailo`)

如欲協助更新現有語料，請往下到 Community 欄目與我們聯繫。

## 統計資料
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->
本資料集包含以下年齡與性別分布。

### 性別

錄音者自行宣告的性別（Gender）資訊。頻次（Frequency）為標記此性別的錄音數。

<!-- {{GENDER_TABLE}} -->
<!-- @ AUTOMATICALLY GENERATED @ -->
<!-- 
| Gender | Frequency |
|--------|-----------|
| male, masculine | ? |
| undeclared | ? |
| female, feminine | ? |
-->
### 年齡

錄音者自行宣告的年齡層（Age band）資訊。頻次（Frequency）為標記此年齡的錄音數。

<!-- {{AGE_TABLE}} -->
<!-- @ AUTOMATICALLY GENERATED @ -->
<!-- 
| Age band | Frequency |
|----------|-----------|
| teens | ? |
| twenties | ? |
| thirties | ? |
| fourties | ? |
| fifties | ? |
   ...if other age ranges are present in your data, add rows...
-->

## 文本語料

<!-- {{TEXT_CORPUS_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- An overview of the text corpus, with information such as average length (in characters and words) of validated sentences. -->

此錄音集大部分文本語料整理於：[MozTW CC0 語料庫](https://github.com/moztw/cc0-sentences)，主要來自 MozTW ／ g0v 社群個別參與者。

由於目前缺乏公共授權（無已知授權限制）的台語「句子」文本語料，Common Voice 台語錄音目前以「單詞」為大宗。

我們亟需更多「日常生活用句」，歡迎捐贈您以台語書寫的作品。請參考下方社群頻道資訊與我們聯繫。

### 書寫系統

<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

#### 符號表

<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->

### 樣本

以下為五個隨機選擇的錄音句子樣本

<!-- {{SENTENCES_SAMPLE}} -->

### 來源

<!-- {{SOURCES_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- A list of sentence sources, can be curated to the top-N -->

文本語料由 Mozilla 台灣社群、g0v 社群、及其他開放原始碼運動參與者共同建立。

早期的台語語料主要來自「2016-itaigi華台對照典」。請參考[資料來源與授權](https://github.com/moztw/cc0-sentences/tree/master/nan-TW#資料來源與授權)了解原始資料出處。

### 文本領域

<!-- {{TEXT_DOMAIN_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What text domains are represented in the corpus? -->

由於目前缺乏公共授權的「句子」資料，Common Voice 台語語料目前仍以「單詞」為大宗。

我們亟需更多「日常生活用句」，歡迎捐贈您以台語書寫的作品。請參考 [社群頻道資訊](#community-links) 與我們聯繫。

### 處理

<!-- {{PROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- How has the text data been processed -->

### 建議後處理流程步驟

<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What should people do before they use the data, for example Unicode normalisation -->

因為句子、單詞所標示的羅馬字為參考用，且 a) 混用台羅與白話字系統，b) 也未能標出所有腔調的發音，顧無法作為實際錄音者發音之對應標注。

我們建議使用前先行移除用`（）`包夾的參考發音，僅取用漢字部分。

## 參與！

### 社群連結

<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->

Mozilla 台灣社群 (MozTW) Common Voice 專案網站： [https://moztw.org/commonvoice/](https://moztw.org/commonvoice/)

任何問題與建議、協助推廣、捐贈語料，或其他合作需求，請透過以下社群頻道與我們討論：

- [Telegram group](https://t.me/+gvmHEcAtd-IwNzFl)
- [Line group](https://line.me/ti/g/_PLyjCSe_8)

### 討論

<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->

- [Discourse 討論區](https://discourse.mozilla.org/c/voice/zh-tw/286)
- [相關新聞](https://hackmd.io/@moztw/common-voice-news)

### 貢獻

<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->

* [協助錄音](https://commonvoice.mozilla.org/nan-tw/speak)
* [協助驗證錄音](https://commonvoice.mozilla.org/nan-tw/listen)
* 捐出你的句子 - 如您有意願捐出你擁有的文本語料（例如您的個人創作）供參與者錄音，請先聯絡 Irvin （ irvin@moztw.org ）或於以上 Line / Telegram 群組討論。

## 誌謝

### 資料表編撰

<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->

- Irvin Chen (MozTW 社群聯絡人) <irvin@moztw.org>
- Dennis Chen (Common Voice Community Facilitator, Wikimedia Taiwan) <dennis@wikimedia.tw>

### 引用說明

<!-- {{CITATION_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you published a paper and would like people to cite it, you can include the BiBTeX here -->

### 經費

<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->

## 授權

此資料集以 [創用 CC 公眾領域貢獻宣告 (CC-0)](https://creativecommons.org/public-domain/cc0/) 釋出至公共領域。
下載這個資料集，即代表你同意不對資料集中的個別參與者進行識別。
