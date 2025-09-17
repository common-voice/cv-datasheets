# *Адыгабзэ* &mdash; Adyghe (West Circassian) (`ady`)
This datasheet is for version 23.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Adyghe (West Circassian) (`ady`). The dataset contains 799 clips representing 6 hours of recorded
speech (6 hours validated) from 22 speakers.

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->

## Demographic information
We are working on adding demographic information to the Spontaneous Speech datasets. For the moment this information
is not available.



<!--
The dataset includes the following distribution of age and gender.
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->

### Gender
Self-declared gender information, frequency refers to the number of clips annotated with this gender.
-->



<!--
<!-- {{GENDER_TABLE}} -->
<!-- @ AUTOMATICALLY GENERATED @ -->
<!-- | Gender | Frequency |
|--------|-----------|
| male, masculine | ? |
| undeclared | ? |
| female, feminine | ? | -->

### Age
Self-declared age information, frequency refers to the number of clips annotated with this age band.
-->
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
| Train | 186 |
| Test | 358 |
| Dev | 255 |

<!-- @ AUTOMATICALLY GENERATED @ -->

## Transcriptions

* Prompts: `127`
* Duration: `20277000[ms]`
* Avg. Transcription Len: `189`
* Avg. Duration: `25.38[s]`
* Valid Duration: `16706.66[s]`
* Total hours: `5.63[h]`
* Valid hours: `4.64[h]`

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
"""Непэ программэу ӏэрышӏ акъылыр зылъапсэм удэгущыӏэныр цӏыфхэмкӏэ шэпхъэ уцугъэу олъыта? [Nêpe programmeu 'erış' akhılır zılhapsem vudeguşı'enır ts'ıfxemç'e şşepxhe vutsuğeu volhıta?]"""
"""Тиныдэлъфыбзэу адыгабзэр мыкӏодыжьынымкӏэ тыпэшӏуекӏонэу сыд тшӏэмэ хъущт, сыд уигупшысэр? [Tinıdelhfıbzeu adıgabzer mık'odıjınımç'e tıpeş'uêk'oneu sıd tş'eme xhuşt, sıd vuigupşşıser?]"""
"""Гукъыдэчъ къыозытыгъэ цӀыф горэ е хъугъэ-шӀэгъэ горэ уищыӀэныгъэкӀэ щыӀа? [Gukhıdeçç khıozıtığe ts'ıf gore yê xhuğe-ş'eğe gore vuişı'enığeç'e şı'a?]"""
"""Сыд фэдэ тхылъхэм уяджэныр уикӏаса? [Sıd fede txılhxem vuyacenır vuiç'asa?]"","
"""Уисабыигъом тыдэ шъущыпсэугъ? Сыд фэда джэгухэр шъуджэгущтыгъа? [Vuisabıiğom tıde şsuşıpseuğ? Sıd feda ceguxer şsuceguştığa?]"""
```

<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.

```
Жъыгъырыб, зае, зэндалэ, къужъы, къыпцӏэ, къыцэ, [noise] чэрэз - мыхэр.
Сисабыигъом байрам мафэхэр янахь тикӏасэщтыгъ.  Джэнакӏэу тянэ къытфидыгъэхэ тщыгъэу, цокъакӏэхэр зыщытлъэу, зыдгъэкӏэракӏэу, къуажьэми тыкӏуагъэу тиныбжьэгъухэм тадэджэгумэ - джары янахь тызщытхъэщтыгъэ лъэхъаныр.
Нахь бэрэм уахътэ сизакъоу згъэкӏонэу сыгу рехьы. Ау загъорэ цӏыфэу шӏу слъэгъухэрэм садигъусэу уахътэ згъэкӏонэуи сыфае мэхъу, сафэзэщы мэ.


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

* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/ady/common-voice/contributors/)

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

This dataset was partially funded by the *Open Multilingual Speech Fund* managed by Mozilla Common Voice.
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.