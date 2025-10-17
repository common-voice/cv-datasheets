# *Saʼban* &mdash; Sa'ban (`snv`)

This datasheet is for version 1.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Sa'ban (`snv`). The dataset contains 2038 clips representing 11 hours of recorded
speech (1 hours validated) from 30 speakers.

## Language
Saʼban is an Austronesian language in the Apo Duat subgroup. It is spoken by the Saʼban people and is indigenous to Sarawak, Malaysia and North Kalimantan, Indonesia.
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
| Train | 1407 |
| Test | 337 |
| Dev | 294 |
<!-- @ AUTOMATICALLY GENERATED @ -->

## Transcriptions
* Prompts: `120`
* Duration: `37757736[ms]`
* Avg. Transcription Len: `72`
* Avg. Duration: `18.53[s]`
* Valid Duration: `87.88[s]`
* Total hours: `10.49[h]`
* Valid hours: `0.02[h]`
<!-- {{TRANSCRIPTIONS_DESCRIPTION}} -->
<!-- A description of the transcription system used -->


### Writing system
The Saʼban writing system is based on the Latin alphabet.
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

<!--[Not provided]
#### Symbol table
[Not provided]-->
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
Papah dut lun aweng parap nolong lun nok lah’ wan anok?
Kan nan acala ngan irau sinah nok nan lem tak bongma’ ceh mai? 
Um minot ceek mai pei’
Madei’ lem ayo’ atol papu’ duktun dong negala ceh
Kedutpah sawai ceh lem ayo’ langoi? Papah?
```
<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.
```
Lem nnau eek aa.. papah duet lem sieu hnai maa ee..teknologi  ee… yeh nah menye… menyebar aa..pesanan nok wei yeh nah lem ee… teknologi
mayak budaya tam lem aweng memang err nan err siu siu nok rah on lun err kira pa nan lun papuk err kudut irau krismas ka tahun baru ka err memang err mung lun lem aweng apalagi keluarga memang mei mayak lun mei ngan lun err lem masa nok nonoh dudut ai

Kai sik lem lun nok arok anok malak lem'rang ceh weik arai mrai padeik nok weik ndeh supaya deh weik lek hleu nok on deh malak jadi hleu

```
<!-- {{TRANSCRIPTIONS_SAMPLE}} -->

### Recommended post-processing
The questions use the ’ character, while the responses use the ' character instead. These characters should be treated as equivalent.
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
[demographics
spec](https://github.com/common-voice/common-voice/blob/main/web/src/stores/demographics.ts). These
will only be reported if the speaker opted in to provide that
information.

## Get involved!

### Community links
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/snv/common-voice/contributors/)
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

<!--[Not provided]
### Datasheet authors
[Not provided]-->
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
