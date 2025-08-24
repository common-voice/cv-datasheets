# *台語* &mdash; Taiwanese (Minnan) (`nan-tw`)

This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Taiwanese (Minnan) (`nan-tw`).

## Language

<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->

Common Voice 台語語音語料集為「*漢字-語音資料集*」。
文本語料以漢字為主，並標注台羅或白話字發音參考。
錄音者主要為台灣參與者台灣口音。

### Variants 

<!-- {{VARIANT_DESCRIPTION}} -->
<!-- Describe the variants (MCV variants) of your language -->

台語語音資料集，於 v23.0 版本開始允許錄音與文本貢獻者選擇以下 Variants 項目（可選）。
但目前文字文本仍以兩者混合呈現為大宗。

- 白話字 (POJ): nan-TW-pehoeji
- 台羅 (TL): nan-TW-tailo

### Accents

<!-- {{ACCENT_DESCRIPTION}} -->

目前台語語音資料集中，允許錄音者於口音欄位選擇以下出生地資訊，作為預設口音資料（可選）。
錄音者亦也可自行輸入其他口音資訊。

- 出生地：基隆市 (birthplace: keelung_city)
- 出生地：臺北市 (birthplace: taipei_city)
- 出生地：新北市 (birthplace: new_taipei_city)
- 出生地：桃園市 (birthplace: taoyuan_city)
- 出生地：新竹縣 (birthplace: hsinchu_county)
- 出生地：新竹市 (birthplace: hsinchu_city)
- 出生地：苗栗縣 (birthplace: miaoli_county)
- 出生地：臺中市 (birthplace: taichung_city)
- 出生地：彰化縣 (birthplace: changhua_county)
- 出生地：南投縣 (birthplace: nantou_county)
- 出生地：雲林縣 (birthplace: yunlin_county)
- 出生地：嘉義縣 (birthplace: chiayi_county)
- 出生地：嘉義市 (birthplace: chiayi_city)
- 出生地：臺南市 (birthplace: tainan_city)
- 出生地：高雄市 (birthplace: kaohsiung_city)
- 出生地：屏東縣 (birthplace: pingtung_county)
- 出生地：宜蘭縣 (birthplace: yilan_county)
- 出生地：花蓮縣 (birthplace: hualien_county)
- 出生地：臺東縣 (birthplace: taitung_county)
- 出生地：澎湖縣 (birthplace: penghu_county)
- 出生地：金門縣 (birthplace: kinmen_county)
- 出生地：連江縣 (birthplace: lienchiang_county)
- 出生地：其他 (other_county)

#### Predefined

<!-- {{PREDEFINED_ACCENT_DESCRIPTION}} -->

<!-- {{PREDEFINED_ACCENT_TABLE}} -->

#### User defined

<!-- {{USER_DEFINED_ACCENT_DESCRPIPTION}} -->

<!-- {{USER_DEFINED_ACCENT_TABLE}} -->

## Demographic information
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->
The dataset includes the following distribution of age and gender.

### Gender

Self-declared gender information, frequency refers to the number of clips annotated with this gender.

<!-- {{GENDER_TABLE}} -->
<!-- 
| Gender | Frequency |
|--------|-----------|
| male, masculine | ? |
| undeclared | ? |
| female, feminine | ? |
-->
### Age

Self-declared age information, frequency refers to the number of clips annotated with this age band.

<!-- {{AGE_TABLE}} -->
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

## Text corpus

<!-- {{TEXT_CORPUS_DESCRIPTION}} -->
<!-- An overview of the text corpus, with information such as average length (in characters and words) of validated sentences. -->

### Writing system

<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

#### Symbol table

<!-- {{ALPHABET_TABLE}} -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->

### Sample

There follows a randomly selected sample of five sentences from the corpus.

<!-- {{SENTENCES_SAMPLE}} -->

三兩人講四斤話 （sann niú lâng kóng sì kin uē）
土地公廟仔 （Thóo-tē-kong biō-á）
開向（khui-hiàng）
菜蟲食菜菜跤死（Tshài-thâng tsia̍h tshài, tshài-kha sí）
兩翁仔某（nn̄g ang-á-bóo）
補眠（póo-bîn）
辛亥國小（Sin-hāi Kok-sió）
蔡厝（Tshuà-tshù | Chhòa-chhù）

### Sources

<!-- {{SOURCES_LIST}} -->
<!-- A list of sentence sources, can be curated to the top-N -->

大部分台語文本語料整理於：[MozTW CC0 語料庫](https://github.com/moztw/cc0-sentences)。
早期的台語語料主要來自「2016-itaigi華台對照典」。請參考[資料來源與授權](https://github.com/moztw/cc0-sentences/tree/master/nan-TW#資料來源與授權)了解原始資料出處。

### Text domains

<!-- {{TEXT_DOMAIN_DESCRIPTION}} -->
<!-- What text domains are represented in the corpus? -->

由於目前缺乏公共授權的「句子」資料，Common Voice 台語語料目前仍以「單詞」為大宗。我們亟需更多「日常生活用句」，歡迎捐贈您以台語書寫的作品。請參考 [社群頻道資訊](#community-links) 與我們聯繫。

### Processing

<!-- {{PROCESSING_DESCRIPTION}} -->
<!-- How has the text data been processed -->

### Recommended post-processing

<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- What should people do before they use the data, for example Unicode normalisation -->

因為句子、單詞所標示的羅馬字為參考用，且混用台羅與白話字系統，也未能標出所有腔調的發音，
我們建議使用時先行移除用`（）`包裝的參考發音部分，僅取用漢字。

## Get involved!

### Community links

<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- Links to community chats / fora -->

MozTW 社群 Common Voice 專案網站： [https://moztw.org/commonvoice/](https://moztw.org/commonvoice/)

如有任何問題與建議，或有興趣協助推廣、協力建構語料，請加入以下社群群組，與大家一起討論：

- [Telegram group](https://t.me/+gvmHEcAtd-IwNzFl)
- [Line group](https://line.me/ti/g/_PLyjCSe_8)

### Discussions

<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->

相關報導 - [https://hackmd.io/@moztw/common-voice-news](https://hackmd.io/@moztw/common-voice-news)

### Contribute

<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->

## Acknowledgements

### Datasheet authors

<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->

Mozilla 台灣社群、G0v 社群、及其他開放原始碼運動參與者共同建立。  

- Irvin Chen (MozTW 志工聯絡人) <irvin@moztw.org>
- Dennis <>

### Citation guidelines

<!-- {{CITATION_DESCRIPTION}} -->
<!-- If you published a paper and would like people to cite it, you can include the BiBTeX here -->

### Funding

<!-- {{FUNDING_DESCRIPTION}} -->
<!-- If you received any funding, you can include the acknowledgement here -->

## Licence

此資料集以 [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) 授權釋出至公共領域。
下載這個資料集，代表你同意不對資料集中的個別發音者進行識別。
