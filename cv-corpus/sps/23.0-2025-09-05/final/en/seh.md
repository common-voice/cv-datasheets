# *[Sena]* &mdash; Sena (`seh`)
> This datasheet has been generated automatically, we would love to include more information, if you would like to help out, [get in touch](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)!

 This datasheet is for version 23.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Sena (`seh`). The dataset contains 21 clips representing 1 hours of recorded
speech (0 hours validated) from 1 speakers.

## Language
<!-- {{LANGUAGE_DESCRIPTION}} --> The Sena language (hereinafter Cisena, N 44 in the Guthrie classification, 1967-71), is a language originally belonging to the Congo-Kordophonian (Niger-Congo) family of the Bantu group. In Mozambique the Sena language is spoken predominantly in the provinces of lower Zambezi, namely Sofala, Zambezia, Tete and Manica and in the far south of the Republic of Malawi.
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

## Transcriptions
* Prompts: `21`
* Duration: `830124[ms]`
* Avg. Transcription Len: `66`
* Avg. Duration: `39.53[s]`
* Valid Duration: `0.0[s]`
* Total hours: `0.23[h]`
* Valid hours: `0.0[h]`
<!-- {{TRANSCRIPTIONS_DESCRIPTION}} --> 
<!-- A description of the transcription system used --> The transcription system uses Latin script in general, but with some combinations of consonants that serve to represent the specific sounds of the language as ny, dz, jh, pf, bz, ng', ps, sv, ts, dh and bh.

### Writing system
<!-- {{WRITING_SYSTEM_DESCRIPTION}} --> The writing system uses the Latin script in general, but with some combinations of consonants that serve to represent the specific sounds of the language as ny, dz, jh, pf, bz, ng', ps, sv, ts, dh and bh.
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus --> In the corpus was used the latin writing system, but with some combinations of consonants that serve to represent the specific sounds of the language as ny, dz, jh, pf, bz, ng', ps, sv, ts, dh and bh.
#### Symbol table
<!-- {{ALPHABET_TABLE}} --> 
Sena	IPA		Sena	IPA
a	a	    	n	n
b	ɓ		    ng'	ŋ
bh	b	   	ny	ɲ
c	c	    	o	ɔ
d	ɗ	    	p	p
dh	d	   	r	ɾ
jh	dʒ  		s	s
j 	dj 	 	dz	dz
e	ɛ		    t	t
f	f	   	th	ʄ
g	g		   u	u
h	h	   	v	v
i	i	   	w	w
k	k	   	x	ʃ
l	l		   y	j
m	m	   	z	Z

<!-- @ OPTIONAL @ --> 

#### Extralinguistic tags

### Samples

#### Questions
There follows a randomly selected sample of questions used in the corpus.

```
Samora Machel ndi mbani penu akhali yani?
Thangweranji pasakhondeswa anapiyana kuyenda kumaliro?
Maputo ndi cigawo comwe cisagumanika kupi?
Imwe mucisa mwanu muna pifuwo pipi?
Musafuna kudyanji makamaka mucisa mwanu?
```
<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.
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
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/seh/common-voice/contributors/)
* [Original language request on GitHub](https://github.com/common-voice/common-voice/issues/5024)
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
