# *Адыгэбзэ (Къэбэрдей)* &mdash; Kabardian (East Circassian) (`kbd`)
This datasheet is for version 23.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Kabardian (East Circassian) (`kbd`). The dataset contains 669 clips representing 8 hours of recorded
speech (6 hours validated) from 25 speakers.

## Language
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

## Data splits for modelling



 | Split | Count |
|-|-|
| Train | 381 |
| Test | 166 |
| Dev | 122 |


## Transcriptions

* Prompts: `154`
* Duration: `25347204[ms]`
* Avg. Transcription Len: `297`
* Avg. Duration: `37.89[s]`
* Valid Duration: `18827.35[s]`
* Total hours: `7.04[h]`
* Valid hours: `5.23[h]`

<!-- {{TRANSCRIPTIONS_DESCRIPTION}} -->
<!-- A description of the transcription system used -->

### Writing system
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

#### Symbol table
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->

#### Extralinguistic tags

### Samples

#### Questions
There follows a randomly selected sample of questions used in the corpus.

```
Ущыцӏыкӏум сыт хуэдэ джэгукӏэ узэрыджэгуар? [Vuşıts'ık'um sıt xuede ceguç'e vuzerıceguar?]
Уи сабийр и ныбжьэгъухэм езауэмэ сыт пщӏэнур? [Vui sabiyr yi nıbjeğuxem yêzaueme sıt pş'enur?]
Щхьэхуитыныгъэр дауэ къызэрыбгурыӏуэр? [Şhexuitınığer daue khızerıbgurı'uer?]
Узэреплъымкӏэ псы ежэххэр къабзэу къызэтенэн папщӏэ сыт тщӏэн хуейр? [Vuzerêplhımç'e psı yêjjexxer khabzeu khızetênen papş'e sıt tş'en xuêyr?]
Фи щӏэнгъасэ ӏуэхум дауэ уеплърэ? [Fi ş'enğase 'uexum daue vuêplhre?]
```

<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.

```
Си лъэпкъ хабзэр куэдчӏэ къащхьэщочӏ адрей лъэпкъхэм. Сэ си хабзэр дахэщ, икъучӏэ губзыгъагъэ хьэлщэн дахэхьэр хэлъщ.[noise]

Нтӏэ, ищӏащ. Цӏыхум убгъэдэту ущепсалъэм дей зыгуэрчӏэ и жагъуэ пщӏыуэ щытмэ е зыгуэр жепӏэу щытмэ игу иримыхьу,[disfluency] абыи зыгуэр къуищӏэнчӏэри хъунущ, ӏей дыдэу и жагъуэ пщӏыуэ щытмэ. Интернетым апхуэдэу зы щӏыпӏэ [disfluency] комментарий жоуэ уихьэу зыгуэр птхыуэ е зыгуэрым уедауэу зыгуэрк1э и жагъуэ пщӏыуэ щытмэ, зыри къуищӏэну [disfluency] къару иӏэнукъымэ.
Си щэхухэр зыхуэсӏуатэр си анэращ. Си анэр анэм хуэдэуи, шыпхъу нэхъыжьым хуэдэуи, ныбжьэгъуфӏым хуэдэуи къысхущытщ. Абы хуэду си дзыхь зыми есхьэлӏэӏым, абы хуэдэуи зыми сыкъигъэпэжыну си фӏэщ хъуркъым.
Пщӏэ яхуэпщӏын хуейщ.
```

<!-- {{TRANSCRIPTIONS_SAMPLE}} -->

### Recommended post-processing
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
   *  `transcription-length` - character per second under 3 characters per second
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

* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/kbd/common-voice/contributors/)

<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->

### Discussions
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
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->

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