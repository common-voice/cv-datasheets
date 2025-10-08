# *Cymraeg* &mdash; Welsh (`cy`)
> This datasheet has been generated automatically, we would love to include more information, if you would like to help out, [get in touch](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)!

 This datasheet is for version 23.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Welsh (`cy`). The dataset contains 8 clips representing 1 hours of recorded
speech (0 hours validated) from 1 speakers.

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->
The Welsh language (Cymraeg - /kəmˈraːiɡ/) belongs to the Celtic language family, specifically the Brythonic branch of Insular Celtic. Welsh evolved in the 6th century, alongside Breton and Cornish, from Common Brittonic, the common language previously spoken throughout Great Britain during the Iron Age and Roman period. The language has experienced contact with English since medieval times, leading to extensive lexical borrowing and gradual language shift intensified by socioeconomic factors and educational policies. It's resilience however stems from concentrated communities, intergenerational transmission, cultural traditions like the Eisteddfod, and religious revival movements. Strategic activism by speakers from the 1960s onwards has transformed Welsh from a declining minority language into one with official legal status. The most recent census shows 538,300 speakers (17.8% of Wales' population), though other surveys suggest higher figures of up to 862,700 speakers. Legislation by the Senedd (Welsh Parliament) supports revitalization through education and technology, with the goal of achieving one million speakers and doubled daily usage by 2050.

Welsh language speech varies significantly across proficiency levels (from native speakers and learners to passive understanders), regional dialects (mainly northern and southern, plus Patagonian Welsh), and registers (formal literary Welsh versus more informal colloquial spoken forms that sometimes incorporates code-switching). Speaker competence ranges widely, with some demonstrating full fluency across all domains while others show more limited or context-specific abilities.


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
* Prompts: `8`
* Duration: `621036[ms]`
* Avg. Transcription Len: `0`
* Avg. Duration: `77.63[s]`
* Valid Duration: `0.0[s]`
* Total hours: `0.17[h]`
* Valid hours: `0.0[h]`
<!-- {{TRANSCRIPTIONS_DESCRIPTION}} -->
<!-- A description of the transcription system used -->

### Writing system
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->
Welsh employs a Latin alphabet of 29 letters, including eight digraphs (ch, dd, ff, ng, ll, ph, rh, th) treated as single letters for alphabetization, and treats "w" and "y" as vowels. The orthography is largely phonetic with predictable sound-letter correspondences. Loanwords, especially from English, are occasionally adapted to Welsh spelling conventions.

#### Symbol table
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->
The 29 letters used for alphabetization in Welsh are:

```a b c ch d dd e f ff g ng h i j l ll m n o p ph r rh s t th u w y```

The letter j is borrowed from English to represent the borrowed /dʒ/ consonant phoneme. 

Welsh also uses diacritical marks on vowels (considered variants of their base letters, not separate letters for alphabetization):

With circumflex ('to bach'): ```â ê î ô û ŵ ŷ```

With acute accent: ```á é í ó ú ẃ ý```

With grave accent: ```à è ì ò ù ẁ ỳ```

With diaeresis: ```ä ë ï ö ü ẅ ÿ```

The traditional system lacks letters k, q, v, x, z, although these can appear in proper nouns and technical terms. 


#### Extralinguistic tags

### Samples

#### Questions
There follows a randomly selected sample of questions used in the corpus.

```
Beth yw dy hoff bryd bwyd iʼw goginio gartref?
Beth ywʼr peth gorau am fyw yng Nghymru?
Oes gen ti unrhyw hobi neu ddiddordeb arbennig?
Beth wyt tiʼn hoffi ei wneud ar y penwythnos?
Beth wyt tiʼn ei hoffi fwyaf am dy swydd?
```
<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.
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
[demograpics
spec](https://github.com/common-voice/common-voice/blob/main/web/src/stores/demographics.ts). These
will only be reported if the speaker opted in to provide that
information.

## Get involved!

### Community links
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/cy/common-voice/contributors/)
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

* Dewi Bryn Jones (https://github.com/DewiBrynJones)
* Gareth Watkins (https://github.com/grw20blt)


### Funding
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.
