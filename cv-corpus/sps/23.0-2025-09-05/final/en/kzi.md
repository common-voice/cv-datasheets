# *Kelabit* &mdash; Kelabit (`kzi`)

This datasheet is for version 1.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Kelabit (`kzi`). The dataset contains 1741 clips representing 10 hours of recorded
speech (1 hours validated) from 21 speakers.

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->
Kelabit is an Austronesian language in the Apo Duat subgroup. It is spoken by the Kelabit people and is indigenous to Sarawak, Malaysia and North Kalimantan, Indonesia.

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
| Train | 1112 |
| Test | 296 |
| Dev | 333 |

## Transcriptions
* Prompts: `120`
* Duration: `34662672[ms]`
* Avg. Transcription Len: `190`
* Avg. Duration: `19.91[s]`
* Valid Duration: `812.34[s]`
* Total hours: `9.63[h]`
* Valid hours: `0.23[h]`
<!-- {{TRANSCRIPTIONS_DESCRIPTION}} -->
<!-- A description of the transcription system used -->

### Writing system
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

The Kelabit writing system is based on the Latin alphabet.

#### Symbol table
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->

```
a e i o u
aa ee ii oo uu
b bp c d dt g gk h j k l m n ng p r s t w y ʼ
```

#### Extralinguistic tags

### Samples

#### Questions
There follows a randomly selected sample of questions used in the corpus.

```
Nun naru lun muyuh bubuh me’ ngi bawang beken? / Kadi ngudah lun muyuh bubuh me’ ngi bawang beken?
Enun program radio lem bawang nuk iko doo pian?
Ken inan bajet senaru/senulis muyuh dengeruyung? / Ken naru muyuh dengeruyung bajet?
Iko seritah lawe iko nier wayang ngi ruma wayang lem bawang muyuh?
Kapeh ayu edto ngi nuk inan iko mudeng?
```
<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.

```
Mo raut ebol, raut ebol, raut volley ball, raut gaing nideh ngilad, raut pepana' nideh, raut guli nideh ngilad.
Manid na'an teh pakaian doo' piyan tauh lemulun eh. Maya' lawey mudeng ngi ruma' beto' narih keh pakai nuk buyur neh narih. La' mey lati' beto' narih keh pakai nuk senang koh mey lati' nikoh. La' mey kerja ngi upis beto' koh keh la' pakai gaun neh narih. Maya' kerja nuk tu'en narih teh sapa' nuk doo' piyan pakai narih.
Teknologi nuk inan uih rapang  i h ineh inan ibal lemulun ngidih nuk merey  karuh, merey talk leh. Bisnes. Kinih-kinih kedeh , kinih-kinih kedeh nuru'  arih masuk bisnes bah. Err... ta'ut narih .  Mula' lem...lem  pengeh uih ni'er ibal lemulun deh masuk bisnes neh keyh. Mileh' usin deh raruh bah. 'di keduih rapang ngelinuh lemulun nuk nasihat tauh mala kinih-kinih-kinih tauh. Beng, beng, raut beng kinih usin pakai tauh kedeh ko'. Masuk nideh beng, masuk nideh na'...inan na' nideh pa... inan peruyung lah gen bisnes-bisnes. Mileh raruh teh usin dedih bah. Kadi' keduih  taut lah, kadi' keduih rapang masuk nuk tad-tad ineh neh bah. 'Ey' neto keduih nekinih masuk naru' sineh neto'.
Na'em ngadan getu'en keli' keduih. Na'em men lun merar mala ngadan getu'en malam, mala idih getu'en tupu tideh nuk mudeng liyang langit nangey  senaru' Tuhan Alla, neh tupu nidih, erang gawa' ngih. Mo.
[noise] Moq kanap so karu'uih naruh bajet, [a..]lam [dat..] daih kamih[a..] lam kamih ngaruyung, masti narih inan bajet dih tah do, naam narih pakai usin mu'oh mu'oh, dih tah narih mi'lah gi'rah usin, ripun idih man...
```
<!-- {{TRANSCRIPTIONS_SAMPLE}} -->

### Recommended post-processing
<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What should people do before they use the data, for example Unicode normalisation or normalisation of extralinguistic tags -->

The questions use the ’ character, while the responses use the ' character instead. These characters should be treated as equivalent.

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
[demographics
spec](https://github.com/common-voice/common-voice/blob/main/web/src/stores/demographics.ts). These
will only be reported if the speaker opted in to provide that
information.

## Get involved!

### Community links
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/kzi/common-voice/contributors/)
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
<!-- A list in the format of: Your Name &lt;email@email.com&gt; -->

### Citation guidelines
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