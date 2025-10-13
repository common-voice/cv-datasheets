# *català* &mdash; Catalan (`ca`)

This datasheet is for version 1.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Catalan (`ca`). The dataset contains 137 clips representing 1 hours of recorded
speech (1 hours validated) from 11 speakers.

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->
Catalan is a Romance language spoken by about 9 million people, mainly on the Mediterranean coast of the Iberian Peninsula. 

It is an official language, along with Spanish or Castilian, in Catalonia, the Balearic Islands and the Valencian Community (where it
is also called Valencian), while it is the only official language of the Principality of Andorra. 
It is also spoken, and has some administrative recognition, without reaching official status,
in the eastern part of the autonomous community of Aragon, in the French department of Pyrénées-Orientales (Eastern Pyrenees) and in the city of Alghero, on the island of Sardinia (Italy).

### Variants
The main variants of Catalan are:
* Central [ca-central]: It is the variant with the most speakers, as it encompasses the metropolitan area of Barcelona, extending to the region of Girona and the eastern half of Tarragona
* Balearic [ca-balear]: The variant used in the Balearic Islands
* Nord-Occidental [ca-nwestern]: Spoken in Andorra, Lleida and the western half of Tarragona in Catalonia, and the eastern part of Aragon
* Septentrional [ca-northern]: Corresponds to the area of Roussillon and the northern part of Girona
* Valencian: Spoken in the Valencian comunity, where it's also known as "Valencian"
  * Valencià meridional [ca-valencia-southern]
  * Alacantí [ca-valencia-alacant]
  * Valencià septentrional [ca-valencia-northern]
  * Tortosí [ca-valencia-tortosi]
  * Valencià central [ca-valencia-central]
* Alguerese [ca-algueres]: Spoken in the city of Alghero, in Sardinia


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
* Prompts: `57`
* Duration: `2101320[ms]`
* Avg. Transcription Len: `74`
* Avg. Duration: `15.34[s]`
* Valid Duration: `605.95[s]`
* Total hours: `0.58[h]`
* Valid hours: `0.17[h]`
<!-- {{TRANSCRIPTIONS_DESCRIPTION}} -->
<!-- A description of the transcription system used -->

### Writing system
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->
Catalan is written using the Latin alphabet (abcdefghijklmnopqrstuvwxyz), with the special characters *ç* and *l·l*. In addition, vowels can be accented (à, è, é, í, ò, ó, ú, ü, ï). The characters *-* (hyphen) and *'* (apostrophe) are also part of Catalan orthography.

#### Symbol table
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->
```a b c ç d e f g h i j k l m n o p q r s t u v w x y z à è é í ò ó ú ï ü```


#### Extralinguistic tags

### Samples

#### Questions
There follows a randomly selected sample of questions used in the corpus.

```
Tʼinformes de lʼactualitat sense fer servir televisió convencional? Com?
Quin és el teu plat preferit?
Explica alguna tradició de Sant Jordi que trobis especial.
Què significa lʼèxit per a tu?
Què creus que és important per a un bon barri?
```
<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.

```

Els avenços que s'han fet en el camp de la diabetis, eh... on te... cada vegada hi ha sensors per me... mesurar la glucosa en sang, i bombes per a... administrar la insulina, diferents tecnologies que... la veritat és que...  ajuden molt al, al dia a dia del... dels pacients i... i que fa un temps enrere no els ah tenien i és un camp qualitatiu molt gran.
Doncs en els últims anys, la veritat és que viatjo molt menys, perquè trobo que tot s'ha encarit moltíssim, tant l'allotjament com els vols o la gasolina pel cotxe, etcètera. La qual cosa fa que, francament, viatgi potser la meitat del que acostumava a viatjar abans.
Per seguir l'actualitat, normalment utilitzo l'aplicació del 324. De 3cat.

```
<!-- {{TRANSCRIPTIONS_SAMPLE}} -->

### Recommended post-processing
<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What should people do before they use the data, for example Unicode normalisation or normalisation of extralinguistic tags -->
It is recommended to normalize instances of the geminate L, which can take the equivalent forms of l·l or ŀl.

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
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/ca/common-voice/contributors/)
* [Original language request on GitHub](https://github.com/common-voice/common-voice/issues/4911)
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

* Carme Armentano <carme.armentano@bsc.es>

### Funding
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.
