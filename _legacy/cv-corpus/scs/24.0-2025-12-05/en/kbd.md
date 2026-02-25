# *Адыгэбзэ (Къэбэрдей)* &mdash; Kabardian (`kbd`)

This datasheet is for version 24.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Kabardian (`kbd`). The dataset contains 112462 clips representing 194.74 hours of recorded
speech (177.25 hours validated) from 289 speakers.

## Language

<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->
**Kabardian** (/kəˈbɑːrdiən/, also known as *East Circassian*) is a Northwest Caucasian language spoken by the eastern subgroups of Adygheans (Circassians). Identified by the ISO 639-3 code [kbd](https://iso639-3.sil.org/code/kbd), it belongs to the **Northwest Caucasian language family** and is widely considered to be the eastern dialect of Adyghe. Kabardian is also one of the official languages of the Kabardino-Balkarian Republic and the Karachay-Cherkess Republic, both federal subjects of the Russian Federation.

The [Kabardian (East Circassians)](https://en.wikipedia.org/wiki/Kabardians) population is estimated at 500,000 to 750,000, yet only around 300,000 are believed to actively speak the language. Kabardians are primarily located in the **Kabardino-Balkaria** and **Karachay-Cherkessia** republics of **Russia**, with additional diaspora populations in **Turkey**, **Jordan**, **Syria**, and other countries due to historical migrations. The language includes several dialects, with the **Baksan** and **Malka** varieties being the most prominent. However, **only a limited portion of the Kabardian population is considered literate in the language**.

There is no definitive and official publication on this matter. Data published by organizations such as [Wikipedia](https://en.wikipedia.org/wiki/Kabardians), Etnologue, and the Joshua Project do not reflect reality. Many Kabardians living in both the Caucasus and the Diaspora identify themselves as Adyghe unless specifically asked. Therefore, to obtain reliable results, researchers must be well-versed in the Adyghe tribes and their culture.

### Variants 

<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->
The following table presents the general language variants of the Kabardian language used in the Common Voice project.

| Language Variant                                               | BCP-47 Tag                         | Script                  | Short Description       |
|----------------------------------------------------------------|------------------------------------|--------------------------|---------------------------|
| Kabardian/East Circassian (Cyrillic)                           | kbd-Cyrl                           | Cyrillic                | Indicated for all literate speakers. |
| Kabardian/East Circassian (Cyrillic, Russia)                   | kbd-RU                             | Cyrillic                | Specified for literate speakers in Russia. |
| Kabardian/East Circassian (Cyrillic, Turkey)                   | kbd-Cyrl-TR                        | Cyrillic                | Specified for literate speakers in Turkey. |
| Kabardian/East Circassian (Latin, Turkey, transliteration)     | kbd-Latn-TR-t-kbd-cyrl-tr          | Turkish transliteration | Specified for non-literate speakers in Turkey. |
| Kabardian/East Circassian (Cyrillic, Jordan)                   | kbd-Cyrl-JOR                       | Cyrillic                | Specified for literate speakers in Jordan. |
| Kabardian/East Circassian (Cyrillic, Syria)                    | kbd-Cyrl-SY                        | Cyrillic                | Specified for literate speakers in Syria. |

**Semtences in the MCV project are provided in Cyrillic and Turkish transliteration to support non-literate users from the Turkish diaspora.** With "literacy" we mean being able to read the Kabardian alphabet.

## Demographic information
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->
The dataset includes the following distribution of age and gender.

### Gender

Self-declared gender information, frequency refers to the number of clips annotated with this gender.


| Gender | Pertentage |
|-|-|
| Undefined | 51.0% |
| Female Feminine | 48.0% |
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

| Age Band | Percentage |
|-|-|
| Undefined | 15.0% |
| Twenties | 19.0% |
| Thirties | 28.0% |
| Teens | 3.0% |
| Fourties | 11.0% |
| Fifties | 24.0% |
| Sixties | 1.0% |
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

## Data splits for modelling
The official data splits for modelling this language are as follows. Of the validated clips, 29.27% are included in the splits.

| Split | Count |
|-|-|
| Train | 8134 |
| Test | 5416 |
| Dev | 5423 |

## Text corpus

<!-- {{TEXT_CORPUS_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- An overview of the text corpus, with information such as average length (in characters and words) of validated sentences. -->
The text corpus for the Kabardian language in the Common Voice project consists of a diverse collection of sentences contributed by native speakers. These sentences cover a wide range of topics, including everyday conversations, cultural references, and various domains such as literature, news articles, conversational texts, technology, health, and education. The maximum length of Kabardian sentences in this dataset is limited to 15 words and 140 characters due to restrictions in the Common Voice interface. However, Kabardian sentences can naturally be much longer. In this dataset, the average length has been aimed to be maintained at around 6–8 words and 80–100 characters to reflect the typical structure and complexity of the Kabardian language. The corpus has been curated to ensure a broad representation of vocabulary and grammatical constructs, making it suitable for training robust speech recognition models.

### Writing system

<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->
The Kabardian language uses the **Cyrillic script** with some additional letters to represent specific sounds in the language. The [alphabet](https://www.omniglot.com/writing/kabardian.htm) consists of **59 letters**, including **33 standard** Cyrillic letters and **26 additional** letters unique to Kabardian. The writing system is phonetic, meaning that words are generally spelled as they are pronounced. Kabardian is written from left to right.

During the period when there was no Kabardian keyboard option, the recorded text content was written with the Russian keyboard as the closest alternative. The characters in the Kabardian alphabet defined by the **Unicode Consortium** as **"Cyrillic Letter Palocka ('Ӏ': u04C0, utf-8)"** and **"Cyrillic Letter Small Palocka ('ӏ': u04CF, utf-8)"** are not defined in this keyboard model. For this reason, since the early days of computers, when creating digital data in Adyghe or Kabardian, one of the characters **"Latin Capital Letter i ('I': u0049, utf-8)"**, **"Latin Small Letter L ('l': u006C, utf-8)"** or **"Digit One ('1': u0031, utf-8)"**, albeit rarely **"Vertical Line ('|': u007C, utf-8)"** was used randomly due to their visual similarities ([Nemlioğlu, 2018](https://www.researchgate.net/publication/385579626_BILISIM_ve_INTERNETTE_ADIGE_DILININ_KULLANIMININ_YAYGINLASMASININ_SAGLANMASI)). This situation emerges as an important factor that negatively affects data quality ([Nemlioğlu,2025](https://www.researchgate.net/publication/395242067_ADYGABZEKE_KLAVIATURER_GEFEDENYM_ERYS_AKYLYM_ISKUSSTVENNYJ_INTELLEKT_IGESENYGE_MEHANEU_SYRIER)). 

#### Symbol table

<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->
**Main Alphabet:** (Ordered by ascending) <br>
а э б в г {гу} {гъ} {гъу} д {дж} {дз} е ё ж {жь} з и й к {ку} {кӏ} {кӏу} {къ} {къу} {кхъ} {кхъу} л {лъ} {лӏ} м н о п {пӏ} р с т {тӏ} у ф {фӏ} х {ху} {хь} {хъ} {хъу} ц {цӏ} ч  ш щ {щӏ} ъ ы ь ю я ӏ {ӏу} 

**Orthographic–Phonetic Table (IPA):** <br>

| А а (aː) |  Э э (a,ɘ) | Б б (b) | В в (v) | Г г (g) | Гу гу (ɡʷ) | Гъ гъ (ʁ) | Гъу гъу (ʁʷ) | Д д (d) | Дж дж (dʒ) |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|

| Дз дз (dz) | Е е (je) | Ё ё (jo) | Ж ж (ʒ) | Жь жь (ʑ) | З з (z) | И и (i) | Й й (j) | К к (k) | Ку ку (kʷ) |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|

| Кӏ кӏ (t͡ʃ) | Кӏу кӏу (kʷʼ) | Къ къ (q) | Къу къу (qʷ) | Кхъ кхъ (qχ) | Кхъу кхъу (qχʷ) | Л л (l) | Лъ лъ (ɬ) | Лӏ лӏ (ɬʼ) | М м (m) |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|

| Н н (n) | О о (o, w) | П п (p) | Пӏ пӏ (pʼ) | Р р (r) | С с (s) | Т т (t) | Тӏ тӏ (tʼ) | У у (u, w) | Ф ф (f) |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|

| Фӏ фӏ (fʼ) | Х х (x) | Ху ху (xʷ) | Хъ хъ (χ) | Хъу хъу (χʷ) | Хь хь (ħ) | Ц ц (ts) | Цӏ цӏ (tsʼ) | Ч ч (tʃ) | Ш ш (ʃ) |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|

| Щ щ (ɕ) | Щӏ щӏ (ɕʼ) | Ъ ъ (′) | Ы ы (ə) | Ь ь (′) | Ю ю (ju) | Я я (ja) | Ӏ ӏ (ʔ) | Ӏу ӏу (ʔʷ) |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|

**Auxiliary exemplar:** <br>
The following letters are also present in the dataset, but are not part of the official Kabardian alphabet. They are used to represent three specific sounds in the different sub dialects.<br>

**{гь}:** [_Voiced dorso-palatal plosive_ [ʄ]](https://en.wikipedia.org/wiki/Voiced_palatal_implosive) (e.g. гьанэ (ɟa:ne) [Some dialects of Kabardian] = джанэ [Kabardian]: _shirt/dress_)<br>
**{кь}:** [_Voiceless dorso-palato-velar plosive_ [kʲ]](https://en.wikipedia.org/wiki/Voiceless_palatal_plosive) (e.g. кьыржын (kʲərʒən) [Some dialects of Kabardian] = чыржын [Kabardian]: _a type of cookie made from corn flour_ )<br>
**{кӏь}:** [_Glottalized voiceless dorso-palato-velar plosive_ [kʲʼ]](https://en.wikipedia.org/wiki/Velar_ejective_stop) (e.g. гьэдыкIьэ (ɟedəkʲ’e) [Some dialects of Kabardian] = джэдыкӏэ [Kabardian]: _egg_)<br>

**_Prior to dataset utilization, the following transformations should be applied to resolve transcription inconsistencies related to dialectal phoneme representation:_**
> г' -> гь <br>
> чӏ -> кӏь <br>

**Other Languages:** <br>
Some entries in the dataset include words originating from other languages, such as Russian or Turkish. These words have been phonetically transcribed using the Kabadrian alphabet, with characters chosen to approximate their original pronunciation as closely as possible.<br>

### Sample

There follows a randomly selected sample of five sentences from the corpus.

<!-- {{SENTENCES_SAMPLE}} -->

### Sources

<!-- {{SOURCES_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- A list of sentence sources, can be curated to the top-N -->
All sentences in this dataset were created specifically for the Common Voice project by native Kabardian speakers. The sentences were carefully crafted to cover a wide range of topics and linguistic structures, ensuring a diverse and representative corpus for speech recognition training.

### Text domains

| Domain | Count |
|-|-|
| Undefined | 2728 |
| Agriculture Food | 4 |
| Automotive Transport | 5 |
| General | 121798 |
| Healthcare | 64 |
| History Law Government | 245 |
| Language Fundamentals | 16 |
| Media Entertainment | 7 |
| Nature Environment | 131 |
| News Current Affairs | 5 |

| Domain                   | en                          | kbd                                                   |
|--------------------------|-----------------------------|-------------------------------------------------------|
| agriculture_food         | Agriculture and Food        | Мэкъумэшымрэ ерыскъыпхъэхэмрэ                         |
| automotive_transport     | Automotive and Transport    | Автомобиль ухуэныгъэмрэ транспортымрэ                 |
| finance                  | Finance                     | Финанс                                                |
| service_retail           | Service and Retail          | Ӏуэхутхьэбзэхэмрэ зырызу сатумрэ                      |
| general                  | General                     | Зэдай темэхэр                                         |
| healthcare               | Healthcare                  | Узыншагъэр хъумэныгъэ                                 |
| history_law_government   | History, Law and Government | Тхыдэ, хабзэ, къэрал унафэщӏ                          |
| language_fundamentals    | Language Fundamentals       | Бзэм и лъабжьэхэр                                     |
| media_entertainment      | Media and Entertainment     | Медиа, нэгузыужьыгъуэ                                 |
| nature_environment       | Nature and Environment      | Щӏыуэпсымрэ дыкъэзыухъуреихь дунеймрэ                 |
| news_current_affairs     | News and Current Affairs    | Хъыбарыщӏэхэмрэ мыхьэнэ зиӏэ къэхъукъащӏэхэмрэ        |
| technology_robotics      | Technology and Robotics     | Технологиехэмрэ робототехникэмрэ                      |

### Processing

<!-- {{PROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- How has the text data been processed -->
The text data in this dataset has undergone several processing steps to ensure quality and consistency:
#### Preparation of Sentences:
The sentences prepared by the community were mostly reviewed by Adyghe language experts before being transferred into the system. Prior to transfer, not only spelling errors but also character compatibility (such as corrections of Cyrillic Small Letter Palochka [u04CF] and Cyrillic Letter Palochka [u04C0]) were checked to ensure accuracy.
#### Normalization:
The text data has been normalized to ensure consistency in formatting and representation. This includes standardizing punctuation, capitalization, and spacing. Special attention was given to the unique characters in the Kabardian alphabet to ensure they are correctly represented.
#### Validation:
The sentences have been validated by native Kabardian speakers to ensure linguistic accuracy and naturalness. This validation process helps to eliminate any sentences that may be awkward or unnatural in everyday speech.
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
* If you want to join kbd community, start here: https://bit.ly/cv_circassian_start_here
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/kbd/common-voice/contributors/)

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

If you want to contribute to the Kabardian language, please visit the following links:
https://bit.ly/cv_circassian_start_here


	A special thanks to all the volunteers who contributed to this dataset.


* [Speak](https://commonvoice.mozilla.org/kbd/speak)
* [Write](https://commonvoice.mozilla.org/kbd/write)
* [Listen](https://commonvoice.mozilla.org/kbd/listen)
* [Review](https://commonvoice.mozilla.org/kbd/review)

## Acknowledgements

### Datasheet authors

<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->
M.Ugur Nemlioglu <nemerko@nemerko.com> <br>
Murat Topçu <murattopcu67@hotmail.com> <br>	

### Dataset curators
<!-- {{DATASET_CURATORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com>-->
Murat Topçu <murattopcu67@hotmail.com> <br>	
Elizaveta Gogunokova <br>
Saida Abregova <br>
M.Uğur Nemlioğlu <br>

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

