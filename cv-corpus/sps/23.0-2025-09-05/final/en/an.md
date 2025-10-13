# *Aragonés* &mdash; Aragonese (`an`)

This datasheet is for version 1.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Aragonese (`an`). The dataset contains 19 clips representing 1 hours of recorded
speech (1 hours validated) from 1 speakers.

## Language
Aragonese is a Romance language spoken in several dialects by about 8,000&mdash;12,000 people in the northern areas of Aragon, Spain, primarily in the counties of Chacetania, Alto Galligo, Sobrarbe and Ribagorza. The language vitality status is Endangered according to https://www.ethnologue.com/language/arg/. At the moment, Spanish influences the native speakers, which may cause code mixing in a spontaneous speech. 

<!-- ### Variants -->
<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->
<!-- Original Answer: -->
<!-- There are currently no variants defined for Aragonese. -->
<!-- ### Accents -->
<!-- #### Predefined -->
<!-- There are currently no pre-defined accents. -->

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

## Transcriptions
* Prompts: `19`
* Duration: `395352[ms]`
* Avg. Transcription Len: `233`
* Avg. Duration: `20.81[s]`
* Valid Duration: `395.35[s]`
* Total hours: `0.11[h]`
* Valid hours: `0.11[h]`
<!-- {{TRANSCRIPTIONS_DESCRIPTION}} -->
<!-- A description of the transcription system used -->

### Writing system
In 2023, the [Academia Aragonesa de la Lengua](https://academiaaragonesadelalengua.org), a public institution created as language regulatory body, established the [Orthography of Aragonese](https://https://academiaaragonesadelalengua.org/sites/default/files/ficheros-pdf/ortografia-aragones.pdf) as the official spelling for the language. The spelling system is flexible enough to allow writing all Aragonese varieties. All the transcriptions have been done using the official orthography (using Spanish spelling when words of this language were intercalated in the speech).

#### Symbol table
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->

#### Extralinguistic tags

### Samples

#### Questions
There follows a randomly selected sample of questions used in the corpus.

```
Cuál d'os quefers de casa t'agrada menos?
Qué remedios emplegas cuan yes resfriau?
Ta dó te faría goyo d'ir de viache?
Qué tecnolochía te preocupa mas?
Qué querrías fer pa trobar-te millor?
```
<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.

```
Como vivimos en un lugar chicorrón y no bi ha pescadería, lo pescau que mas se mincha ye la merluza conchelada. Fresco, lo que mas goyo nos fa ye la dorada, la lubina, y lo millor d'el mundo ye lo abadeixo salau.
Pa trobar-me millor, m'aganaría caminar más y estar menos andalosa, no meter la carga debant de los machos siempre.
En lo nuestro lugar las casas antis mas se feban de solo piedra, con parets muit recias d'hasta ochenta centimetros y tasament heban cimientos, asinas que... las parets yeran parets de carga... Los pisos s'aposentaban en buenas bigas trabes de madera, tamién lo tellau. Y las las tellas yeran de charco marrón, no yeran pizarra, yeran feitas de charco marrón y cocidas y lo monyo... pa sojetar-las s'apoyaba en las latas. Las latas yeran listonez finos que se clavaban d'una trabeta a l'atra. 
Tasament me refrío pero si lo i so, beber muita agua y tomar bel paracetamol.
L'orache en lo mío lugar habría que estar como l'orache de lo mont en lo Pirineu: muito frío y muita nieu en himbierno; primaveras, bien de agua, aire, y verdes; veranos de muito calor de manyanas y fresco cuando se caye lo sol, y frío de noches y de madrugada; y las santmigaladas, con muita airera... pero ixas estacions ya se'n son perdidas.
```
<!-- {{TRANSCRIPTIONS_SAMPLE}} -->

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
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/an/common-voice/contributors/)
<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->


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
* Juan Pablo Martínez <juanpabl@gmail.com>


### Funding
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->
This dataset was partially funded by the Open Multilingual Speech Fund.

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.
