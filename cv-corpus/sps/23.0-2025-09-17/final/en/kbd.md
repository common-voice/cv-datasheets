# *Адыгэбзэ (Къэбэрдей)* &mdash; Kabardian (East Circassian) (`kbd`)

This datasheet is for version 23.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Kabardian (East Circassian) (`kbd`). The dataset contains 8 hours of recorded
speech (6 hours validated) from 25 speakers.

## Language

<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->
**Kabardian** (/kəˈbɑːrdiən/, also known as *East Circassian*) is a Northwest Caucasian language spoken by the eastern subgroups of Adygheans (Circassians). Identified by the ISO 639-3 code [kbd](https://iso639-3.sil.org/code/kbd), it belongs to the **Northwest Caucasian language family** and is widely considered to be the eastern dialect of Adyghe. Kabardian is also one of the official languages of the Kabardino-Balkarian Republic and the Karachay-Cherkess Republic, both federal subjects of the Russian Federation.

The [Kabardian (East Circassians)](https://en.wikipedia.org/wiki/Kabardians) population is estimated at 500,000 to 750,000, yet only around 300,000 are believed to actively speak the language. Kabardians are primarily located in the **Kabardino-Balkaria** and **Karachay-Cherkessia** republics of **Russia**, with additional diaspora populations in **Turkey**, **Jordan**, **Syria**, and other countries due to historical migrations. The language includes several dialects, with the **Baksan** and **Malka** varieties being the most prominent. However, **only a limited portion of the Kabardian population is considered literate in the language**.

There is no definitive and official publication on this matter. Data published by organizations such as [Wikipedia](https://en.wikipedia.org/wiki/Kabardians), Etnologue, and the Joshua Project do not reflect reality. Many Kabardians living in both the Caucasus and the Diaspora identify themselves as Adyghe unless specifically asked. Therefore, to obtain reliable results, researchers must be well-versed in the Adyghe tribes and their culture.

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

## Transcriptions

<!-- {{TRANSCRIPTIONS_DESCRIPTION}} -->
<!-- A description of the transcription system used -->

### Writing system

<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->
The Kabardian language uses the Cyrillic script with some additional letters to represent specific sounds in the language. The [alphabet](https://www.omniglot.com/writing/kabardian.htm) consists of 59 letters, including 33 standard Cyrillic letters and 26 additional letters unique to Kabardian. The writing system is phonetic, meaning that words are generally spelled as they are pronounced. Kabardian is written from left to right.

During the period when there was no Kabardian keyboard option, the recorded text content was written with the Russian keyboard as the closest alternative. The characters in the Kabardian alphabet defined by the Unicode Consortium as "Cyrillic Letter Palocka ('Ӏ': u04C0, utf-8)" and "Cyrillic Letter Small Palocka ('ӏ': u04CF, utf-8)" are not defined in this keyboard model. For this reason, since the early days of computers, when creating digital data in Adyghe or Kabardian, one of the characters "Latin Capital Letter i ('I': u0049, utf-8)", "Latin Small Letter L ('l': u006C, utf-8)" or "Digit One ('1': u0031, utf-8)", albeit rarely "Vertical Line ('|': u007C, utf-8)" was used randomly due to their visual similarities ([Nemlioğlu, 2018](https://www.researchgate.net/publication/385579626_BILISIM_ve_INTERNETTE_ADIGE_DILININ_KULLANIMININ_YAYGINLASMASININ_SAGLANMASI)). This situation emerges as an important factor that negatively affects data quality ([Nemlioğlu,2025](https://www.researchgate.net/publication/395242067_ADYGABZEKE_KLAVIATURER_GEFEDENYM_ERYS_AKYLYM_ISKUSSTVENNYJ_INTELLEKT_IGESENYGE_MEHANEU_SYRIER)). 

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

#### Extralinguistic tags

<!-- {{EXTRALINGUISTIC_TAGS_DESCRIPTION}} -->
| Tag          | Meaning                                                                                                                                 |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [laugh]      | The sound of laughter.                                                                                                                  |
| [disfluency] | A filler word or sound used as a placeholder whilst a speaker decides what to say. In English, common hesitation sounds are “err”, “um”, “huh”, etc. |
| [unclear]    | A word or sequence of words that cannot be understood.                                                                                  |
| [noise]      | Any other type of noise, such as the speaker coughing or clearing their throat, a car honking, the sound of something hitting the microphone, a phone buzzing, etc. |


### Variants
<!-- {{VARIANT_DESCRIPTIONS}} -->
<!-- @ OPTIONAL @ -->
The following table presents the general language variants of the Kabardian language used in the Common Voice project.

| Language Variant                                               | BCP-47 Tag                         | Script                  | Short Description       |
|----------------------------------------------------------------|------------------------------------|--------------------------|---------------------------|
| Kabardian/East Circassian (Cyrillic)                           | kbd-Cyrl                           | Cyrillic                | Indicated for all literate speakers. |
| Kabardian/East Circassian (Cyrillic, Russia)                   | kbd-RU                             | Cyrillic                | Specified for literate speakers in Russia. |
| Kabardian/East Circassian (Cyrillic, Turkey)                   | kbd-Cyrl-TR                        | Cyrillic                | Specified for literate speakers in Turkey. |
| Kabardian/East Circassian (Latin, Turkey, transliteration)     | kbd-Latn-TR-t-kbd-cyrl-tr          | Turkish transliteration | Specified for non-literate speakers in Turkey. |
| Kabardian/East Circassian (Cyrillic, Jordan)                   | kbd-Cyrl-JOR                       | Cyrillic                | Specified for literate speakers in Jordan. |
| Kabardian/East Circassian (Cyrillic, Syria)                    | kbd-Cyrl-SY                        | Cyrillic                | Specified for literate speakers in Syria. |

**Questions in the MCV-SS project are provided in Cyrillic and Turkish transliteration to support non-literate users from the Turkish diaspora.** With "literacy" we mean being able to read the Kabardian alphabet.

### Samples

#### Questions

There follows a randomly selected sample of transcribed responses from the corpus.

<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses

There follows a randomly selected sample of transcribed responses from the corpus.

<!-- {{TRANSCRIPTIONS_SAMPLE}} -->

### Recommended post-processing

<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What should people do before they use the data, for example Unicode normalisation or normalisation of extralinguistic tags -->
These transcriptions are provided as-is, and no additional post-processing is required. However, users may choose to perform Unicode normalization (NFC or NFD) depending on their specific use case.

Although the sentences (questions/translation texts) have been written and verified using correct Unicode characters via the [**ady & kbd keyboard for Windows**](https://www.nemerko.org/adyghe-circassian-keyboard-for-windows-7-11/), it is possible that some text inputs beyond our control may have been submitted due to **Common Voice’s open participation model**.

After the datasets are published, we **re-audit** these entries and take the necessary steps to ensure **corrections in the next release**.

## Get involved!

### Community links

<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->
If you want to join kbd community, start here: https://bit.ly/cv_circassian_start_here

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

