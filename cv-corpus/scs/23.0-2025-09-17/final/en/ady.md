# *Адыгабзэ* &mdash; Adyghe (`ady`)

This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Adyghe (`ady`). The dataset contains 48 hours of recorded
speech (32 hours validated) from 108 speakers.

## Language

<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->
**Adyghe** (/ˈædɪɡeɪ/ or /ˌɑːdɪˈɡeɪ/, also known as *West Circassian*) is a Northwest Caucasian language spoken by the western subgroups of Adygheans (Circassians). Identified by the ISO 639-3 code [ady](https://iso639-3.sil.org/code/ady), it belongs to the **Northwest Caucasian language family**. Adyghe is also one of the official languages of the Republic of Adygea, a federal subject of the Russian Federation.

The [Adyghean (West Circassians)](https://en.wikipedia.org/wiki/Circassians) population is estimated to be between 1,200,000 to 2,000,000 although the number of active speakers is significantly lower. Adygheans are primarily located in the **Republic of Adygea**, **Russia**, with additional diaspora populations in **Turkey**, **Jordan**, **Israel**, **Syria**, the United States, **Canada**, and various **European countries** due to historical migrations. However, **only about 10% of the Adyghe population is considered literate in the language**.

For more information about the global distribution of Adyghe population, see:  
[The Adyghe (Circassian) Diaspora Today](https://www.researchgate.net/publication/384043948_ADIGE_CERKES_DIASPORASININ_BUGUNU).


### Variants 

<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->
# Circassian Language Variants

The following table presents the general language variants of the Adyghe language used in the Common Voice project.

| Language Variant                                               | BCP-47 Tag                         | Script                  | Short Description        |
|----------------------------------------------------------------|------------------------------------|--------------------------|--------------------------|
| Adyghe/West Circassian (Cyrillic)                              | ady-Cyrl                           | Cyrillic                | Indicated for all literate speakers.|
| Adyghe/West Circassian (Cyrillic, Russia)                      | ady-RU                             | Cyrillic                | Specified for literate speakers in Russia. |
| Adyghe/West Circassian (Cyrillic, Turkey)                      | ady-Cyrl-TR                        | Cyrillic                | Specified for literate speakers in Turkey. |
| Adyghe/West Circassian (Latin, Turkey, transliteration)        | ady-Latn-TR-t-ady-cyrl-tr          | Turkish transliteration | Specifies for non-literate speakers in Turkey. |
| Adyghe/West Circassian (Cyrillic, Jordan)                      | ady-Cyrl-JOR                       | Cyrillic                | Specified for literate speakers in Jordan. |
| Adyghe/West Circassian (Cyrillic, Syria)                       | ady-Cyrl-SY                        | Cyrillic                | Specified for literate speakers in Syria. |

**Semtences in the MCV project are provided in Cyrillic and Turkish transliteration to support non-literate users from the Turkish diaspora.** With "literacy" we mean being able to read the Adyghean alphabet.

## Demographic information
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->
The dataset includes the following distribution of age and gender.

### Gender

Self-declared gender information, frequency refers to the number of clips annotated with this gender.

<!-- {{GENDER_TABLE}} -->
<!-- @ AUTOMATICALLY GENERATED @ -->
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

## Text corpus

<!-- {{TEXT_CORPUS_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- An overview of the text corpus, with information such as average length (in characters and words) of validated sentences. -->
The text corpus for the Adyghe language in the Common Voice project consists of a diverse collection of sentences contributed by native speakers. These sentences cover a wide range of topics, including everyday conversations, cultural references, and various domains such as literature, news articles, conversational texts, technology, health, and education. The maximum length of Adyghe sentences in this dataset is limited to 15 words and 140 characters due to restrictions in the Common Voice interface. However, Adyghe sentences can naturally be much longer. In this dataset, the average length has been aimed to be maintained at around 6–8 words and 80–100 characters to reflect the typical structure and complexity of the Adyghe language. The corpus has been curated to ensure a broad representation of vocabulary and grammatical constructs, making it suitable for training robust speech recognition models.

### Writing system

<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->
The Adyghe language uses the **Cyrillic script** with some additional letters to represent specific sounds in the language. The [alphabet](https://www.omniglot.com/writing/adyghe.htm) consists of **66 letters**, including **33 standard** Cyrillic letters and **33 additional** letters unique to Adyghe. The writing system is phonetic, meaning that words are generally spelled as they are pronounced. Adyghe is written from left to right. 

During the period when there was no Adyghe keyboard option, the recorded text content was written with the Russian keyboard as the closest alternative. The characters in the Adyghe alphabet defined by the **Unicode Consortium** as **"Cyrillic Letter Palocka ('Ӏ': u04C0, utf-8)"** and **"Cyrillic Letter Small Palocka ('ӏ': u04CF, utf-8)"** are not defined in this keyboard model. For this reason, since the early days of computers, when creating digital data in Adyghe or Kabardian, one of the characters **"Latin Capital Letter i ('I': u0049, utf-8)"**, **"Latin Small Letter L ('l': u006C, utf-8)"** or **"Digit One ('1': u0031, utf-8)"**, albeit rarely **"Vertical Line ('|': u007C, utf-8)"** was used randomly due to their visual similarities ([Nemlioğlu, 2018](https://www.researchgate.net/publication/385579626_BILISIM_ve_INTERNETTE_ADIGE_DILININ_KULLANIMININ_YAYGINLASMASININ_SAGLANMASI)). This situation emerges as an important factor that negatively affects data quality ([Nemlioğlu,2025](https://www.researchgate.net/publication/395242067_ADYGABZEKE_KLAVIATURER_GEFEDENYM_ERYS_AKYLYM_ISKUSSTVENNYJ_INTELLEKT_IGESENYGE_MEHANEU_SYRIER)). 

Therefore we allowed the use of only the keyboard layout specially designed for Adyghe language in the Common Voice project. This keyboard layout includes all the letters of the Adyghe alphabet, including the special characters **"Cyrillic Letter Palocka ('Ӏ': u04C0, utf-8)"** and **"Cyrillic Letter Small Palocka ('ӏ': u04CF, utf-8)"**. The use of this keyboard layout has significantly improved the quality of the text data in Adyghe. [Click here to download Adyghe Keyboard for Windows](https://www.nemerko.org/adyghe-circassian-keyboard-for-windows-7-11/).


#### Symbol table

<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->
**Main Alphabet:** (Ordered by ascending) <br>
а б в г {гу} {гъ} {гъу} д {дж} {дз} {дзу} е ё ж {жъ} {жъу} {жь} з и й к {ку} {къ} {къу} {кӏ} {кӏу} л {лъ} {лӏ} м н о п {пӏ} {пӏу} р с т {тӏ} {тӏу} у ф х {хъ} {хъу} {хь} ц {цу} {цӏ} ч {чъ} {чӏ} ш {шъ} {шъу} {шӏ} {шӏу} щ ъ ы ь э ю я ӏ {ӏу}

**Orthographic–Phonetic Table (IPA):** <br>

| А а (ä) | Б б (b) | В в (v) | Г г (g) | Гу гу (ɡʷ) | Гъ гъ (ʁ) | Гъу гъу (ʁʷ) | Д д (d) | Дж дж (dʒ) | Дз дз (dz) | Дзу дзу (dzʷ) |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|

| Е е (je) | Ё ё (jo) | Ж ж (ʒ) | Жъ жъ (ʐ) | Жъу жъу (ʒʷ) | Жь жь (ʑ) | З з (z) | И и (i) | Й й (j) | К к (k) | Ку ку (kʷ) |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|

| Къ къ (q) | Къу къу (qʷ) | Кӏ кӏ (t͡ʃ) | Кӏу кӏу (kʷʼ) | Л л (l) | Лъ лъ (ɬ) | Лӏ лӏ (ɬʼ) | М м (m) | Н н (n) | О о (o, w) | П п (p) |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|

| Пӏ пӏ (pʼ) | Пӏу пӏу (pʷʼ) | Р р (r) | С с (s) | Т т (t) | Тӏ тӏ(tʼ) | Тӏу тӏу (tʷʼ) | У у (u, w) | Ф ф (f) | Х х (x) | Хъ хъ (χ) |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|

| Хъу хъу (χʷ) | Хь хь (ħ) | Ц ц (ts) | Цу цу (tsʷ) | Цӏ цӏ (tsʼ) | Ч ч (tʃ) | Чъ чъ (tʂ) | Чӏ чӏ (tʂʼ) | Ш ш (ʃ) | Шъ шъ (ʂ) | Шъу шъу (ʃʷ) |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|

| Шӏ шӏ (ʃʼ) | Шӏу шӏу (ʃʷʼ) | Щ щ (ɕ) | Ъ ъ (′) | Ы ы (ə) | Ь ь (′) | Э э (a,ɘ) | Ю ю (ju) | Я я (ja) | Ӏ ӏ (ʔ) | Ӏу ӏу (ʔʷ) |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|


**Auxiliary exemplar:** <br>
The following letters may also be present in the dataset, but are not part of the official Adyghe alphabet. They are used to represent three specific sounds in the Shapsug dialect. They could potentially appear in some dialogues or quoted sentences.

**{гь}:** [_Voiced dorso-palatal plosive_ [ɟ]](https://en.wikipedia.org/wiki/Voiced_palatal_implosive) (e.g. егьэ (jeɟɘ) [Shapsug] = еджэ [Adyghe]: _reading_)<br>
**{кь}:** [_Voiceless dorso-palato-velar plosive_ [kʲ]](https://en.wikipedia.org/wiki/Voiceless_palatal_plosive) (e.g. кьэт (kʲɘt) [Shapsug] = чэт [Adyghe]: _chicken_ )<br>
**{кӏь}:** [_Glottalized voiceless dorso-palato-velar plosive_ [kʲʼ]](https://en.wikipedia.org/wiki/Velar_ejective_stop) (e.g. кӏьакӏьэ (kʲʼäkʲʼɘ) [Shapsug] = кӏэнкӏэ [Adyghe]: _egg_)<br>

**Other Languages:** <br>
Some entries in the dataset include words originating from other languages, such as Russian or Turkish. These words have been phonetically transcribed using the Adyghe alphabet, with characters chosen to approximate their original pronunciation as closely as possible.<br>

### Sample

There follows a randomly selected sample of five sentences from the corpus.

<!-- {{SENTENCES_SAMPLE}} -->

### Sources

<!-- {{SOURCES_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- A list of sentence sources, can be curated to the top-N -->
All sentences in this dataset were created specifically for the Common Voice project by native Adyghe speakers. The sentences were carefully crafted to cover a wide range of topics and linguistic structures, ensuring a diverse and representative corpus for speech recognition training.

### Text domains

<!-- {{TEXT_DOMAIN_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What text domains are represented in the corpus? -->

| Domain                   | en                          | ady                                                   |
|--------------------------|-----------------------------|-------------------------------------------------------|
| agriculture_food         | Agriculture and Food        | Мэкъу-мэщымрэ гъомлапхъэхэмрэ                         |
| automotive_transport     | Automotive and Transport    | Ку секторымрэ транспортымрэ                           |
| finance                  | Finance                     | Финанс                                                |
| service_retail           | Service and Retail          | Фэӏо-фашӏэмрэ зырыз сатыумрэ                          |
| general                  | General                     | Пстэумэ зэдыряе                                       |
| healthcare               | Healthcare                  | Псауныгъэм иухъумэн                                   |
| history_law_government   | History, Law and Government | Тарихъ, хабзэ ыкӏи къэралыгъо                         |
| language_fundamentals    | Language Fundamentals       | Бзэм ылъапсэхэр (гущ. пае: пчъагъэхэр, хьарыфхэр)     |
| media_entertainment      | Media and Entertainment     | Медия ыкӏи зэщтегъэуныгъ                              |
| nature_environment       | Nature and Environment      | Чӏыопсымрэ тыкъэзыуцухьэрэ дунаимрэ                   |
| news_current_affairs     | News and Current Affairs    | Къэбархэр ыкӏи мэхьанэ зиӏэ хъугъэ-шӏагъэхэр          |
| technology_robotics      | Technology and Robotics     | Технологиехэмрэ робототехникэмрэ                      |

### Processing

<!-- {{PROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- How has the text data been processed -->
The text data in this dataset has undergone several processing steps to ensure quality and consistency:
#### Preparation of Sentences:
The sentences prepared by the community were mostly reviewed by Adyghe language experts before being transferred into the system. Prior to transfer, not only spelling errors but also character compatibility (such as corrections of Cyrillic Small Letter Palochka [u04CF] and Cyrillic Letter Palochka [u04C0]) were checked to ensure accuracy.
#### Normalization:
The text data has been normalized to ensure consistency in formatting and representation. This includes standardizing punctuation, capitalization, and spacing. Special attention was given to the unique characters in the Adyghe alphabet to ensure they are correctly represented.
#### Validation:
The sentences have been validated by native Adyghe speakers to ensure linguistic accuracy and naturalness. This validation process helps to eliminate any sentences that may be awkward or unnatural in everyday speech.
#### Filtering:
Sentences that contained inappropriate content, offensive language, or were deemed unsuitable for public use were filtered out during the review process.
#### Reporting and Corrections:
A system has been established for users to report any errors or issues they encounter in the text data. Reported issues are reviewed by language experts, and necessary corrections are made in subsequent releases of the dataset.
#### Quality Assurance:
Regular quality assurance checks are conducted to maintain the integrity of the text data. This includes periodic reviews of the sentences to ensure they continue to meet the established standards.

### Recommended post-processing

<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What should people do before they use the data, for example Unicode normalisation -->
These sentences are provided as-is, and no additional post-processing is required. However, users may choose to perform Unicode normalization (NFC or NFD) depending on their specific use case.

Although the sentences (questions/translation texts) have been written and verified using correct Unicode characters via the [**ady & kbd keyboard for Windows**](https://www.nemerko.org/adyghe-circassian-keyboard-for-windows-7-11/), it is possible that some text inputs beyond our control may have been submitted due to **Common Voice’s open participation model**.

After the datasets are published, we **re-audit** these entries and take the necessary steps to ensure **corrections in the next release**.


## Get involved!

### Community links

<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->
If you want to join ady community, start here: https://bit.ly/cv_circassian_start_here

You can find more information about how to participate in the Common Voice Project on the following page:  
[Community Participation Guidelines](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)

### Discussions

<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->
Comming soon.

### Contribute

<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->
We do not advice to contribute to this dataset directly, because of writting system-keyboard issues. Please, read the section "Writing system" above and the following article: https://www.nemerko.org/the-importance-of-adyghe-keyboard-usage-for-artificial-intelligence-training/

If you want to contribute to the Adyghe language, please visit the following links:
https://bit.ly/cv_circassian_start_here


	A special thanks to all the volunteers who contributed to this dataset.

## Acknowledgements

### Datasheet authors

<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->
M.Ugur Nemlioglu <nemerko@nemerko.com> <br>
Murat Topçu <murattopcu67@hotmail.com> <br>	

### Dataset curators
<!-- {{DATASET_CURATORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com>-->	
M.Uğur Nemlioğlu <nemerko@nemerko.com><br>
Saida Abregova <br>
Elizaveta Gogunokova <br>
Murat Topçu <br>

### Advisors
<!-- {{ADVISORS_LIST}} -->
<!-- A list in the format of: Your Name-->
Bülent Özden (Technical Advisor)<br>

### Citation guidelines

<!-- {{CITATION_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you published a paper and would like people to cite it, you can include the BiBTeX here -->

### Funding

<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->
This dataset was partially funded by the Open Multilingual Speech Fund.

## Licence

This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.

