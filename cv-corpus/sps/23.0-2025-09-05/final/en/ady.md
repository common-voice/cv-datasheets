# *Адыгабзэ* &mdash; Adyghe (West Circassian) (`ady`)
This datasheet is for version 1.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Adyghe (West Circassian) (`ady`). The dataset contains 6 hours of recorded
speech (6 hours validated) from 22 speakers.

## Language
**Adyghe** (/ˈædɪɡeɪ/ or /ˌɑːdɪˈɡeɪ/, also known as *West Circassian*) is a Northwest Caucasian language spoken by the western subgroups of Adygheans (Circassians). Identified by the ISO 639-3 code [ady](https://iso639-3.sil.org/code/ady), it belongs to the **Northwest Caucasian language family**. Adyghe is also one of the official languages of the Republic of Adygea, a federal subject of the Russian Federation.

The [Adyghean (West Circassians)](https://en.wikipedia.org/wiki/Circassians) population is estimated to be between 1,200,000 to 2,000,000 although the number of active speakers is significantly lower. Adygheans are primarily located in the **Republic of Adygea**, **Russia**, with additional diaspora populations in **Turkey**, **Jordan**, **Israel**, **Syria**, the United States, **Canada**, and various **European countries** due to historical migrations. However, **only about 10% of the Adyghe population is considered literate in the language**.

For more information about the global distribution of Adyghe population, see:  
[The Adyghe (Circassian) Diaspora Today](https://www.researchgate.net/publication/384043948_ADIGE_CERKES_DIASPORASININ_BUGUNU).
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->

## Demographic information
The dataset includes the following distribution of age and gender.
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->

### Gender
Self-declared gender information, frequency refers to the number of clips annotated with this gender.
<!-- {{GENDER_TABLE}} -->
<!-- @ AUTOMATICALLY GENERATED @ -->
<!-- | Gender | Frequency |
|--------|-----------|
| male, masculine | ? |
| undeclared | ? |
| female, feminine | ? | -->

### Age
Self-declared age information, frequency refers to the number of clips annotated with this age band.
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

## Transcriptions
<!-- {{TRANSCRIPTIONS_DESCRIPTION}} -->
<!-- A description of the transcription system used -->

### Writing system
The Adyghe language uses the Cyrillic script with some additional letters to represent specific sounds in the language. The [alphabet](https://www.omniglot.com/writing/adyghe.htm) consists of 66 letters, including 33 standard Cyrillic letters and 33 additional letters unique to Adyghe. The writing system is phonetic, meaning that words are generally spelled as they are pronounced. Adyghe is written from left to right. 

During the period when there was no Adyghe keyboard option, the recorded text content was written with the Russian keyboard as the closest alternative. The characters in the Adyghe alphabet defined by the Unicode Consortium as "Cyrillic Letter Palocka ('Ӏ': u04C0, utf-8)" and "Cyrillic Letter Small Palocka ('ӏ': u04CF, utf-8)" are not defined in this keyboard model. For this reason, since the early days of computers, when creating digital data in Adyghe or Kabardian, one of the characters "Latin Capital Letter i ('I': u0049, utf-8)", "Latin Small Letter L ('l': u006C, utf-8)" or "Digit One ('1': u0031, utf-8)", albeit rarely "Vertical Line ('|': u007C, utf-8)" was used randomly due to their visual similarities ([Nemlioğlu, 2018](https://www.researchgate.net/publication/385579626_BILISIM_ve_INTERNETTE_ADIGE_DILININ_KULLANIMININ_YAYGINLASMASININ_SAGLANMASI)). This situation emerges as an important factor that negatively affects data quality ([Nemlioğlu,2025](https://www.researchgate.net/publication/395242067_ADYGABZEKE_KLAVIATURER_GEFEDENYM_ERYS_AKYLYM_ISKUSSTVENNYJ_INTELLEKT_IGESENYGE_MEHANEU_SYRIER)). 

Therefore we allowed the use of only the keyboard layout specially designed for Adyghe language in the Common Voice project. This keyboard layout includes all the letters of the Adyghe alphabet, including the special characters "Cyrillic Letter Palocka ('Ӏ': u04C0, utf-8)" and "Cyrillic Letter Small Palocka ('ӏ': u04CF, utf-8)". The use of this keyboard layout has significantly improved the quality of the text data in Adyghe. [Click here to download Adyghe Keyboard for Windows](https://www.nemerko.org/adyghe-circassian-keyboard-for-windows-7-11/).
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

#### Symbol table
**Main Alphabet:** (Ordered by ascending) <br>
```а б в г {гу} {гъ} {гъу} д {дж} {дз} {дзу} е ё ж {жъ} {жъу} {жь} з и й к {ку} {къ} {къу} {кӏ} {кӏу} л {лъ} {лӏ} м н о п {пӏ} {пӏу} р с т {тӏ} {тӏу} у ф х {хъ} {хъу} {хь} ц {цу} {цӏ} ч {чъ} {чӏ} ш {шъ} {шъу} {шӏ} {шӏу} щ ъ ы ь э ю я ӏ {ӏу}```

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
The following letters are also present in the dataset, but are not part of the official Adyghe alphabet. They are used to represent two specific sounds in the Shapsug dialect.<br>

**{гь}:** [_Voiced dorso-palatal plosive_ [ɟ]](https://en.wikipedia.org/wiki/Voiced_palatal_implosive) (e.g. егьэ (jeɟɘ) [Shapsug] = еджэ [Adyghe]: _reading_)<br>
**{кь}:** [_Voiceless dorso-palato-velar plosive_ [kʲ]](https://en.wikipedia.org/wiki/Voiceless_palatal_plosive) (e.g. кьэт (kʲɘt) [Shapsug] = чэт [Adyghe]: _chicken_ )<br>
**{кӏь}:** [_Glottalized voiceless dorso-palato-velar plosive_ [kʲʼ]](https://en.wikipedia.org/wiki/Velar_ejective_stop) (e.g. кӏьакӏьэ (kʲʼäkʲʼɘ) [Shapsug] = кӏэнкӏэ [Adyghe]: _egg_)<br>

**Other Languages:** <br>
Some entries in the dataset include words originating from other languages, such as Russian or Turkish. These words have been phonetically transcribed using the Adyghe alphabet, with characters chosen to approximate their original pronunciation as closely as possible.<br>
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->

#### Extralinguistic tags
| Tag          | Meaning                                                                                                                                 |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [laugh]      | The sound of laughter.                                                                                                                  |
| [disfluency] | A filler word or sound used as a placeholder whilst a speaker decides what to say. In English, common hesitation sounds are “err”, “um”, “huh”, etc. |
| [unclear]    | A word or sequence of words that cannot be understood.                                                                                  |
| [noise]      | Any other type of noise, such as the speaker coughing or clearing their throat, a car honking, the sound of something hitting the microphone, a phone buzzing, etc. |
<!-- {{EXTRALINGUISTIC_TAGS_DESCRIPTION}} -->

### Variants
The following table presents the general language variants of the Adyghe language used in the Common Voice project.

| Language Variant                                               | BCP-47 Tag                         | Script                  | Short Description        |
|----------------------------------------------------------------|------------------------------------|--------------------------|--------------------------|
| Adyghe/West Circassian (Cyrillic)                              | ady-Cyrl                           | Cyrillic                | Indicated for all literate speakers.|
| Adyghe/West Circassian (Cyrillic, Russia)                      | ady-RU                             | Cyrillic                | Specified for literate speakers in Russia. |
| Adyghe/West Circassian (Cyrillic, Turkey)                      | ady-Cyrl-TR                        | Cyrillic                | Specified for literate speakers in Turkey. |
| Adyghe/West Circassian (Latin, Turkey, transliteration)        | ady-Latn-TR-t-ady-cyrl-tr          | Turkish transliteration | Specifies for non-literate speakers in Turkey. |
| Adyghe/West Circassian (Cyrillic, Jordan)                      | ady-Cyrl-JOR                       | Cyrillic                | Specified for literate speakers in Jordan. |
| Adyghe/West Circassian (Cyrillic, Syria)                       | ady-Cyrl-SY                        | Cyrillic                | Specified for literate speakers in Syria. |

**Questions in the MCV-SS project are provided in Cyrillic and Turkish transliteration to support non-literate users from the Turkish diaspora.** With "literacy" we mean being able to read the Adyghe alphabet.
<!-- {{VARIANT_DESCRIPTIONS}} -->
<!-- @ OPTIONAL @ -->

### Samples

#### Questions
There follows a randomly selected sample of transcribed responses from the corpus.
<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.
<!-- {{TRANSCRIPTIONS_SAMPLE}} -->

### Recommended post-processing
These transcriptions are provided as-is, and no additional post-processing is required. However, users may choose to perform Unicode normalization (NFC or NFD) depending on their specific use case.

Although the sentences (questions/translation texts) have been written and verified using correct Unicode characters via the [**ady & kbd keyboard for Windows**](https://www.nemerko.org/adyghe-circassian-keyboard-for-windows-7-11/), it is possible that some text inputs beyond our control may have been submitted due to **Common Voice’s open participation model**.

After the datasets are published, we **re-audit** these entries and take the necessary steps to ensure **corrections in the next release**.
<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What should people do before they use the data, for example Unicode normalisation or normalisation of extralinguistic tags -->

## Get involved!

### Community links
If you want to join ady community, start here: https://bit.ly/cv_circassian_start_here

You can find more information about how to participate in the Common Voice Project on the following page:  
[Community Participation Guidelines](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)
<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->

### Contribute
We do not advice to contribute to this dataset directly, because of writting system-keyboard issues. Please, read the section "Writing system" above and the following article: https://www.nemerko.org/the-importance-of-adyghe-keyboard-usage-for-artificial-intelligence-training/

If you want to contribute to the Adyghe language, please visit the following links:
https://bit.ly/cv_circassian_start_here


	A special thanks to all the volunteers who contributed to this dataset.
<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->

## Acknowledgements

### Datasheet authors
* M.Ugur Nemlioglu <nemerko@nemerko.com> <br>
* Murat Topçu <murattopcu67@hotmail.com> <br>
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->

### Dataset curators
* M.Uğur Nemlioğlu <nemerko@nemerko.com><br>
* Saida Abregova <br>
* Elizaveta Gogunokova <br>
* Murat Topçu <br>
<!-- {{DATASET_CURATORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->

### Advisors
* Bülent Özden (Technical Advisor)<br>
<!-- {{ADVISORS_LIST}} -->
<!-- A list in the format of: Your Name -->

### Funding
This dataset was partially funded by the *Open Multilingual Speech Fund* managed by Mozilla Common Voice.
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.