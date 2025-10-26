# *Gegnisht* &mdash; Gheg Albanian (`aln`)
This datasheet is for version 1.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Gheg Albanian (`aln`). The dataset contains 1655 clips representing 11 hours of recorded
speech (11 hours validated) from 14 speakers.

## Language
Gheg Albanian (/ɡɛɡ/) is an Albanian dialect group spoken in northern and central Albania, Kosovo, northwestern North Macedonia, southeastern Montenegro, southern Serbia and southwestern Croatia. Identified by the ISO 639-3 code aln, it belongs to the Indo-European language family. There are estimated to be around four million speakers. There is no widely accepted writing system.
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
| Train | 1115 |
| Dev | 287 |
<!-- @ AUTOMATICALLY GENERATED @ -->
   
## Transcriptions
The transcription of the entire dataset was done by a single individual, using the following guidelines:

In general, the standard Albanian writing system was used, with the following exceptions:

* `&lt;Ε&gt;` was used in place of standard Albanian &lt;ë&gt; /ǝ/
* `&lt;C&gt;` was used in place of standard Albanian &lt;ç&gt; /tš/
* `&lt;gh&gt;` was used to represent /γ/
* `&lt;hj&gt;` was used to represent /ç/

* Prompts: `144`
* Duration: `39113172[ms]`
* Avg. Transcription Len: `198`
* Avg. Duration: `23.63[s]`
* Valid Duration: `37793.74[s]`
* Total hours: `10.86[h]`
* Valid hours: `10.5[h]`
<!-- {{TRANSCRIPTIONS_DESCRIPTION}} -->
<!-- A description of the transcription system used -->

<!--[Not provided]
### Writing system
[Not provided]-->
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

<!--[Not provided]
### Samples
[Not provided]-->

#### Questions
The following is a manually curated sample of questions in the corpus.
```
Çar shifni ju n’ televizor?
Çar lloj lojrash ju pëlqejshin me lujt kalamajve kur ishin t’ vegjël?
Kur ke marr telefon për her t’ par?
```

There follows a randomly selected sample of questions used in the corpus.
```
Masi ke ba familje ça ke ba?
Cilat të mira besoni ju që jan të rëndsishme për venin ku rrini?
A din nonj nofk në shqip?
Sa lloj lulesh dhe bim ke pa kët jav?
Çfar kafshësh ka atje afër ku rrin ti?
```
<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.
```
Me fillu njw pun t re n vendin twnd duet me pas shum lek edhe pranaj gjwrat vwshtirsohen sepse nuk munesh me hap diCka, ose njw pun ose diCka me pak lek, duhet direkt me fillu me shum, sepse atje ka dy shtresa, njw shum t varfwr, njw shum t pasur, edhe t han pastaj. 
Z di me lujt letra se z di me gwnjy, e m mashtrojn tjerwt, ka ma shanse me m mashtru  t tjerwt, se me mashtru un, z di me lujt letra se m ka la ftyra, i ftyr mw shkoi i ftyr m vje...
me nenj ke shpia m pwlqen, nuk asht se kam problem me nenj n shpi, po dhe me dal ajroset robi, merr njw ndryshim tjetwr, shef njw diCa, funksionon truni, funksionon Cdo gja. ma mir me dal kanjhere se pwrdit nuk delet, nuk delet pwrdit, nuk a se na ... mir asht edhe me dal edhe ke shpia mir a.
pwr zotin t tana gjanat jan t mira ku rrim, po, malet, fushat, po male kena ma shum na na pwr shembull, kena male, mojat e malit fiiiiuu ... a ju thash ku jan malet atje... llogarite pwr me dal n maj t malit do njwzet minuta n komb me dal n maj t malit, tu ec dath jo kshu, pwrpara kena ec dhe dath
E Ca shofim na n televizor? Po na nonjer telenovela, lajme, thjesht sa me marr vesh Ca bahet n kwt an, e, nanj film ose siC thash telenovela, muzik, emisione pwr fmij qw ka qef me pa fmija me pas koh shofim dhe na bashk me fmin, kshtu shkon puna, Ca don fmija e kena pa edhe na, kuklla, kuklla, 
```
<!-- {{TRANSCRIPTIONS_SAMPLE}} -->

<!--[Not provided]
### Recommended post-processing
[Not provided]-->
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
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/aln/common-voice/contributors/)
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
* [Contribute Questions](https://commonvoice.mozilla.org/spontaneous-speech/beta/question)
* [Validate Questions](https://commonvoice.mozilla.org/spontaneous-speech/beta/validate)
* [Answer Spontaneous Questions](https://commonvoice.mozilla.org/spontaneous-speech/beta/prompts)
* [Transcribe Recordings](https://commonvoice.mozilla.org/spontaneous-speech/beta/transcribe)
* [Validate Transcriptions](https://commonvoice.mozilla.org/spontaneous-speech/beta/check-transcript)
<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->

## Acknowledgements

### Datasheet authors
* Antonios Dimakis &lt;a.dimakis@athenarc.gr&gt;
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
