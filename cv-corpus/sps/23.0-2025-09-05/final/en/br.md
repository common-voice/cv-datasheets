# *Brezhoneg* &mdash; Breton (`br`)

This datasheet is for version 1.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Breton (`br`). The dataset contains 28 clips representing 1 hours of recorded
speech (1 hours validated) from 5 speakers.

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->
Breton (Brezhoneg) is the only Celtic language spoken on the continent. It belongs to the Brittonic branch of the Celtic languages, like Welsh and Cornish. Breton is classified as "severely endangered" by the UNESCO Atlas of the World's Languages in Danger. The language declined from more than one million speakers around 1950 to less than 200 000 in 2024. After a period of intense protest that began in the 1960s, Breton gradually regained a place in schools, on road signs, then in the media, public life in general, and more recently in digital technology. With the creation of the first bilingual schools at the end of the 1970s, young people were once again speaking Breton, and a change in the way people viewed the language and its use began. Approximately 20 000 pupils attend Breton bilingual classes, either in the Diwan network (immersive teaching) or in bilingual classes in public and catholic school systems. In addition to evening breton classes for adults (~4 000), long-term courses (6 to 9 months) are offered to adults, with approximately 350 places available annually and online courses too (more than 15 000 learners).

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
* Prompts: `22`
* Duration: `342828[ms]`
* Avg. Transcription Len: `92`
* Avg. Duration: `12.24[s]`
* Valid Duration: `35.03[s]`
* Total hours: `0.1[h]`
* Valid hours: `0.01[h]`
<!-- {{TRANSCRIPTIONS_DESCRIPTION}} -->
<!-- A description of the transcription system used -->
The transcription system uses general Latin script, including some diacritics and considering ch and c'h like unique letters. c, q, x may appear in loanwords or foreign language words.

Hesitations in the answers are marked in square brackets (e.g. [euu])

### Writing system
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->
The writing system in this dataset uses general Latin script. The diacritics à, è and é may appear in the transcription of Gwenedeg variant.

#### Symbol table
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->
```a â b ch c'h d e ê f g h i j k l m n ñ o ô p r s t u ù û ü v w y z```

```à è é``` (for gwenedeg variant) 

```c q x``` (foreign, loanwords)

#### Extralinguistic tags

### Samples

#### Questions
There follows a randomly selected sample of questions used in the corpus.

```
Petra a vefe evidocʼh gwellañ micher ar bed ?
Petra a rit da vare Nedeleg?
Plijout a ra deocʼh labourat ?
Ha plijet ocʼh gant ar rouedad treuzdougen boutin e Breizh ?
Gant petra e vezit hegazet ?
```
<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.

```
War meur a enezenn vreizhat on bet : ar Gerveur, Enez-Houad, Enez-Edig, Enez-Groe, [euu],  Enez-Sun, Enez-Vaz, Enez-Eusa, Molenez, Enez-Vriad.
Ar wech kentañ eo din en ober, [euu] lâran ket eo plijus met ma servij d'unan bennak [euu] ret eo ober gantañ.
Spot a anavezan, ya. Ur c'hi bihan eo a vez kavet e-barzh levrioù evit ar vugale ha pa oa bihan va re din-me pet gwech n'on eus ket lennet levrioù Spot 'lec'h ma veze klasket Spot dindan ar gwele, peotramant barzh an armel peotramant el lec'hioù iskisañ 'lec'h ma'z ae da guzh.

ya plijout a rin labourat kar me a labour e bed ar brezhoneg [eeeuu] o stourmiñ evit ma vo komzet brezhoneg a bep seurt livioù e pep lec'h e Breizh.
```
<!-- {{TRANSCRIPTIONS_SAMPLE}} -->

### Recommended post-processing
<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What should people do before they use the data, for example Unicode normalisation or normalisation of extralinguistic tags -->
In Breton, c'h is considered to be a letter. To avoid confusion with the final apostrophe (U+2019 RIGHT SINGLE QUOTATION MARK), you can use the character U+02BC MODIFIER LETTER APOSTROPHE for natural language processing purposes.

c'h : U+0063 LATIN SMALL LETTER C  U+02BC MODIFIER LETTER APOSTROPHE  U+0068 LATIN SMALL LETTER H

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
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/br/common-voice/contributors/)
* [Original language request on GitHub](https://github.com/common-voice/common-voice/issues/4910)
<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->
* [Ofis Publik ar Brezhoneg](https://www.brezhoneg.bzh/)  (public institution in charge of promoting and developing the teaching and use of the Breton language in everyday life)

* [Porched niverel ar brezhoneg](https://niverel.brezhoneg.bzh/br/home/) (portal gathering various digital tools relating to the Breton language)

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
Contact us via  https://www.fr.brezhoneg.bzh/171-contact.htm


### Funding
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.
