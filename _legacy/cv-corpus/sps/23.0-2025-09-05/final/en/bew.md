# *Betawi* &mdash; Betawi (`bew`)
This datasheet is for version 1.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Betawi (`bew`). The dataset contains 1393 clips representing 11 hours of recorded
speech (11 hours validated) from 21 speakers.

## Language
Betawi language originally belongs to Austronesian language with a full name of Melayu-Betawi. This language is considered as one of Malay dialects, but historically it grew together with other major languages, such as Arabic, Hokkien, Sundanese, Javanese, and Malay in Sumatra - a tiny portion with Portuguese and Dutch. The language vitality status is Endangered according to https://www.ethnologue.com/language/bew/. At the moment, Indonesian standard and English in general influence the native speakers, allowing code switching and code mixing happens in a spontaneous speech. The specific variation of this dataset is Betawi Ora or Betawi Pinggiran (Peripheral Betawi), taken from several locations of Bekasi District/City, West Java Province, Indonesia. This variation is unique in terms of geo-politics: language is spoken only in the community, but it is not taught at school. Instead, the community is taught Sundanese language, which is dominated in West Java Province in general.
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->

<!--[Not provided]
## Demographic information
The dataset includes the following distribution of age and gender.
[Not provided]-->
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->
<!--[Not provided]
### Gender
Self-declared gender information, frequency refers to the number of clips annotated with this gender.
[Not provided]-->
<!-- {{GENDER_TABLE}} -->
<!-- @ AUTOMATICALLY GENERATED @ -->
<!-- | Gender | Frequency |
|--------|-----------|
| male, masculine | ? |
| undeclared | ? |
| female, feminine | ? | -->

<!--[Not provided]
### Age
Self-declared age information, frequency refers to the number of clips annotated with this age band.
[Not provided]-->
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
 | Split | Count |
|-|-|
| Train | 977 |
| Dev | 223 |
<!-- @ AUTOMATICALLY GENERATED @ -->

## Transcriptions
The transcription system uses general Latin script, but involves allophone variants of three /e/, these are /é/, /è/, and /e/.

* Prompts: `199`
* Duration: `39396960[ms]`
* Avg. Transcription Len: `292`
* Avg. Duration: `28.28[s]`
* Valid Duration: `36776.84[s]`
* Total hours: `10.94[h]`
* Valid hours: `10.22[h]`
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

<!--[Not provided]
#### Extralinguistic tags
[Not provided]-->

### Samples

#### Questions
There follows a randomly selected sample of questions used in the corpus.
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

### Fields
Each row of a `tsv` file represents a single audio clip, and contains the following information:

* `client_id` - hashed UUID of a given user
* `audio_id` - numeric id for audio file
* `audio_file` - audio file name
* `duration_ms` - duration of audio in milliseconds
* `prompt_id` - numeric id for prompt
* `prompt` - question for user
* `transcription` - transcription of the audio response
* `votes` - number of people that who approved a given transcript
* `age` - age of the speaker[^1]
* `gender` - gender of the speaker[^1]
* `language` - language name
* `split` - for data modelling, which subset of the data does this clip pertain to
* `char_per_sec` - how many characters of transcription per second of audio
* `quality_tags` - some automated assessment of the transcription--audio pair, separated by `|`
   * `transcription-length` - character per second under 3 characters per second
   * `speech-rate` - characters per second over 30 characters per second
   * `short-audio` - audio length under 2 seconds
   * `long-audio` - audio length over 30 seconds

#### 
[^1]: For a full list of age, gender, and accent options, see the
[demograpics
spec](https://github.com/common-voice/common-voice/blob/main/web/src/stores/demographics.ts). These
will only be reported if the speaker opted in to provide that
information.

## Get involved!

### Community links
* https://referensi.data.kemendikdasmen.go.id/budayakita/wbtb/objek/AA000491  
* https://petabahasa.kemdikbud.go.id/  (Web of peta bahasa does not consider Betawi language is part of Indonesia, particularly in Jakarta and West Jawa Province.
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/bew/common-voice/contributors/)
<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->

<!--[Not provided]
### Discussions
[Not provided]-->
<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->


### Contribute
* [Contribute questions](https://commonvoice.mozilla.org/spontaneous-speech/beta/question)
* [Validate questions](https://commonvoice.mozilla.org/spontaneous-speech/beta/validate)
* [Answer questions](https://commonvoice.mozilla.org/spontaneous-speech/beta/prompts)
* [Transcribe recordings](https://commonvoice.mozilla.org/spontaneous-speech/beta/transcribe)
* [Validate transcriptions](https://commonvoice.mozilla.org/spontaneous-speech/beta/check-transcript)
<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->

## Acknowledgements

### Datasheet authors
* Yacub Fahmilda &lt;yacub.fahmilda@gmail.com&gt;
* Riska Legistari Febri &lt;riskalegistari25@gmail.com&gt;
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name &lt;email@email.com&gt; -->

<!--[Not provided]
### Citation guidelines
[Not provided]-->
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
