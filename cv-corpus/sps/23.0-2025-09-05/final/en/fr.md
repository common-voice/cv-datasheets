# *Français* &mdash; French (`fr`)

 This datasheet is for version 23.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for French (`fr`). The dataset contains 133 clips representing 1 hours of recorded
speech (1 hours validated) from 14 speakers.

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->

French is a Romance language. It is the official language of 26 countries and is spoken across around 50 countries. 

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
* Prompts: `81`
* Duration: `2142792[ms]`
* Avg. Transcription Len: `98`
* Avg. Duration: `16.11[s]`
* Valid Duration: `983.77[s]`
* Total hours: `0.6[h]`
* Valid hours: `0.27[h]`
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

```! " ' ( ) , - . 0 3 4 : ; ? A B C D E F G H I J L M N O P Q S T U V Y ] a b c d e f g h i k l m  o p q r s t u v w x y z À à â ç è é ê î ï ô ù û œ ’```

#### Extralinguistic tags

### Samples

#### Questions
There follows a randomly selected sample of questions used in the corpus.

```
Pouvez-vous décrire l'un de vos hobbies et nous expliquer en quoi il consiste ?
Les gens de différents âges utilisent-ils la technologie de manière différente ?
Est-ce que vous trouvez le temps de lire ?
Comment vous détendez-vous et gardez-vous votre esprit en santé ?
Quelle est votre fête préférée et pourquoi ?
```
<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.

```
On tourne en boucle, j'ai déjà répondu à cette question, sauf que maintenant c'est au pluriel, je reste sur l'anglais, c'est ma matière préférée, c'était l'anglais et pourquoi, parce que j'aimais ça.

Oui !
Je suis pas sûr de comprendre la question mais j'ai l'impression qu'oui, après c'est, c'est très difficile l'apprentissage des langues en français en général, parce que c'est, ouais, c'est plutôt la merde en général.
Oui, mais avec le gouvernement Bayrou de moins en moins et il y a toujours une attaque sur la question sociale qui est faite ; heureusement il y a les syndicats, hum, derrière mais c'est... Il y a une attaque en règle en tout cas sur la protection sociale en France.
```
<!-- {{TRANSCRIPTIONS_SAMPLE}} -->

### Recommended post-processing
<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What should people do before they use the data, for example Unicode normalisation or normalisation of extralinguistic tags -->

The transcripts contain two different quotations, ’ and ', which should be normalized.

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
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/fr/common-voice/contributors/)
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

### Funding
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.