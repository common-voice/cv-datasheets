# *Galego* &mdash; Galician (`gl`)
> This datasheet has been generated automatically, we would love to include more information, if you would like to help out, [get in touch](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)!

 This datasheet is for version 23.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Galician (`gl`). The dataset contains 211 clips representing 2 hours of recorded
speech (1 hours validated) from 13 speakers.

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->
Galician is the language of Galicia (Spain). In addition to being a language of use in this territory, it is spoken in other bordering areas, although without official status (Asturias, León, Zamora). It belongs to the Indo-European language family, specifically the Romance languages, along with Spanish, Portuguese and Catalan. It also has a close relationship with Portuguese since they share historical origins, but today they constitute two separate languages with each one having its own respective standard. The state of vitality of the language is “Institutional” according to Ethnologue https://www.ethnologue.com/language/glg/, that is, the language is developed, has a standard variety, is taught at all stages of the Galician educational system and has institutional support. However, from the point of view of sociolinguistics, both the autonomous community of Galicia and the other territories that speak the Galician language present typical features of a situation of linguistic conflict (diglossia), resulting from a historical process of replacement of Galician (a minority language) by Spanish. 

The Galician language is a rich and diverse reality, and its linguistic variation is manifested in spontaneous speech. Thus, aspects such as age, geography, sociocultural level or communicative context also influence linguistic uses. At the dialectal level, Galician presents differentiating features between the eastern and western areas, as well as between the north and the south: phonetic changes (such as the use of gheada or seseo), lexical variations (different words to designate the same object) or even small morpho-syntactic differences. 

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
* Prompts: `153`
* Duration: `3821976[ms]`
* Avg. Transcription Len: `15`
* Avg. Duration: `18.11[s]`
* Valid Duration: `227.48[s]`
* Total hours: `1.06[h]`
* Valid hours: `0.06[h]`
<!-- {{TRANSCRIPTIONS_DESCRIPTION}} -->
<!-- A description of the transcription system used -->

### Writing system
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

The writing system of Galician is based on the Latin alphabet, like other Romance languages (Spanish, Portuguese or French). Its orthography is regulated by the corresponding regional institutions that establish the official rules of use (NOMIG).

Galician uses the 23 letters of the basic Latin alphabet: 5 vowels and 18 consonants. In addition, the letters Ç, J, K, W and Y are supported in foreign words, proper names, abbreviations and international acronyms. The Galician alphabet also has numerous digraphs: combinations of two letters that represent a single sound: "ch", "gu", "ll", "nh", "qu", "rr".

#### Symbol table
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->

a, á, b, c, d, e, é, f, g, h, i, í, ï, l, m, n, o, ó, p, q, r, s, t, u, ú, ü, v, x, z

#### Extralinguistic tags

### Samples

#### Questions
There follows a randomly selected sample of questions used in the corpus.

```
Estendes a roupa nun tendal ou métela nunha secadora?
Que almorzas un día normal?
Que é o máis estresante do teu traballo ou dos teus estudos?
Que se facía antes na Semana Santa?
Describe algunha decoración que teñas na casa.
```
<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.
<!-- {{TRANSCRIPTIONS_SAMPLE}} -->

Pois, en xeral, levántome sobre as oito e media, máis ou menos, pero agora no verán teño que me levantar antes porque teño, eeh... horario de verán.
Como son un señor, as actividades físicas favoritas para min son as de andar, se cadra andar tamén na bicicleta e tomar un pouco o fresco.
Verde por fóra, branca por dentro... mmm (risas) é que non me lembro
Para traballar e para me entreter
Escoitar un pouco ó corpo, eee, comer de todo un pouco, eee, non restrinxir ningún alimento...

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
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/gl/common-voice/contributors/)
* [Original language request on GitHub](https://github.com/common-voice/common-voice/issues/4913)
* [Doar a miña voz] (https://doagalego.nos.gal/)
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
Adina Ioana Vladu
María Pérez Lago 

### Citation guidelines
<!-- {{CITATION_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you published a paper and would like people to cite it, you can include the BiBTeX here -->

### Funding
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->
This dataset was fully funded by the Instituto da Lingua Galega.

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.
