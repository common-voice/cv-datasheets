# *Basaa* &mdash; Basaa (`bas`)
> This datasheet has been generated automatically, we would love to include more information, if you would like to help out, [get in touch](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)!

 This datasheet is for version 23.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Basaa (`bas`). The dataset contains 773 clips representing 6 hours of recorded
speech (6 hours validated) from 11 speakers.

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
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
| Split | Count |
|-|-|
| Train | 291 |
| Test | 220 |
| Dev | 262 |

## Transcriptions
* Prompts: `74`
* Duration: `19354320[ms]`
* Avg. Transcription Len: `282`
* Avg. Duration: `25.04[s]`
* Valid Duration: `18232.45[s]`
* Total hours: `5.38[h]`
* Valid hours: `5.06[h]`
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
Lelaa Batada ba bé léglana manwin nwaa le ngobi-hop i bakana i nlo?
Imbee tison i nlôôha lémél we ikédé loñ Kamerun ? Inyukii ini tison i nlémle we ?
"Ngén basaa yada i nkal le, ""ibale he jôm bé, ki ngôs i tehe bé ñoñ"". Ini ngén i nkobla le kii ?"
Bôt ba nyo maok ma maén, ndi jôga li nyi bé hee ma nlôl. Ti le bés ndoñol i bôlô i lisee maok ma maén.
Mambee masak di gwéé i Mbog yés ?
```
<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.

```
Batada ba bé leglana manwin ni hikuu.
Masak ma yé ngandak i Mbog yés. Ndi ma tôbôtôbô di nla añ nna, ma yé ; ngôla-m'be, hijingô, bôlbô, m'baye, hôngô, hisigô, makune, koo, mauñ, ike i bisu.
Me nkal le ba nsébél Um Nyobe le Mpôdôl  inyu le ingeñ ntida u bakana i binay, le loñ yés i n'nay ni ndutu, i béda naano le yak bés di pam i minkôm, di kôs kunde, Um Nyobe nyen a bé'é a nke i pôdôl loñ, i kodba i matén. Jon ba nsébél nye le Mpôdôl.
Bikila bi Mbog yés. Mut a nlalna bé ñôô ; mut a nsol bé to bép bagwal bé ; mut a nje bé nuga i Mbog kiki bo mbom, bo péé, nyetama ; bikila, mut a nyan bé loñ ; mut a nyan bé Bambombog.
Mbog yés i Mbog yés, di nje ngond minténmintén. Di nla je yo nkônô u ngond ; di nla je yo euh nsagle-ngond ; di nla je yo masas ma ngond.
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
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/bas/common-voice/contributors/)
* [Original language request on GitHub](https://github.com/common-voice/common-voice/issues/4983)
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