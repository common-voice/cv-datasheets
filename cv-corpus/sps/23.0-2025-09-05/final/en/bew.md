# *Betawi* &mdash; Betawi (`bew`)
This datasheet is for version 1.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Betawi (`bew`). The dataset contains 11 hours of recorded
speech (11 hours validated) from 21 speakers.

## Language
Betawi language originally belongs to Austronesian language with a full name of Melayu-Betawi. This language is considered as one of Malay dialects, but historically it grew together with other major languages, such as Arabic, Hokkien, Sundanese, Javanese, and Malay in Sumatra - a tiny portion with Portuguese and Dutch. The language vitality status is Endangered according to https://www.ethnologue.com/language/bew/. At the moment, Indonesian standard and English in general influence the native speakers, allowing code switching and code mixing happens in a spontaneous speech. The specific variation of this dataset is Betawi Ora or Betawi Pinggiran (Peripheral Betawi), taken from several locations of Bekasi District/City, West Java Province, Indonesia. This variation is unique in terms of geo-politics: language is spoken only in the community, but it is not taught at school. Instead, the community is taught Sundanese language, which is dominated in West Java Province in general.
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
The transcription system uses general Latin script, but involves allophone variants of three /e/, these are /é/, /è/, and /e/.
<!-- {{TRANSCRIPTIONS_DESCRIPTION}} -->
<!-- A description of the transcription system used -->

### Writing system
Historically, this language used Pegon, Arabic script, but now Latin is adapted.The writing system in this dataset uses general Latin script, but involves allophone variants of three /e/, these are /é/, /è/, and /e/.
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

#### Symbol table
```
a b c d é è ȇ e f g h i j k l m n o p q r s t u v w y z 
```
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->

### Samples

#### Questions
There follows a randomly selected sample of transcribed responses from the corpus.

```
Begimané pendidikan keluargé di masyarakat sekitar Ente? 
Pigimané masyarakat di lingkungan Ente ngejagé atow melestarikan alam di sekitar? 
Menurut Ente déwék, seberapé besar peran tuh kesenian buat acaré khusus? 
Elmu apé nyang bakalan penting buat dipelajarin di masé depan? 
Begimané caré kité ngedidik generasi mudé biar lebih peduli ngejagé lingkungan?
```
<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.
```
Kalo di sini mah pendidikan paling utama, ya minimal lulus SMA. 
Jadinya di sini mah bagan emaknya pada kuli nandur yang penting anaknya sekolȇh. 
Jadinya diusahain banget pendidikan di sini. 
Bagan boleh utang kék, èmaknya boleh kuli nandur, kuli nyuci, yang penting anaknyé sekolȇh.
```
<!-- {{TRANSCRIPTIONS_SAMPLE}} -->

### Recommended post-processing
(1) Observe the non-linguistic aspects, such as filler, (2) Make sure your machine learning does not differ the suprasegmental aspect, like intonation which does not change the word and its meaning.
<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What should people do before they use the data, for example Unicode normalisation or normalisation of extralinguistic tags -->

## Get involved!

### Community links
* https://referensi.data.kemendikdasmen.go.id/budayakita/wbtb/objek/AA000491  
* https://petabahasa.kemdikbud.go.id/  (Web of peta bahasa does not consider Betawi language is part of Indonesia, particularly in Jakarta and West Jawa Province.
<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->

### Contribute
* [Common Voice: Spontaneous Speech](https://commonvoice.mozilla.org/spontaneous-speech/beta/)
<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->

## Acknowledgements

### Datasheet authors
* Yacub Fahmilda <yacub.fahmilda@gmail.com>
* Riska Legistari Febri <riskalegistari25@gmail.com>
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->

### Funding
This dataset was partially funded by the *Open Multilingual Speech Fund* managed by Mozilla Common Voice.
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.