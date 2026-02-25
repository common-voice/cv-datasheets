# *English* &mdash; English (`en`)

This datasheet is for version 1.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for English (`en`). The dataset contains 0 clips representing 9 hours of recorded
speech (2 hours validated) from 148 speakers.

## Language
English is a West Germanic language with origins in England. There are an estimated 1.5 billion English speakers, making it the most widely spoken language in the world. English is commonly learned as a second language in many countries.
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

<!--[Not provided]
## Data splits for modelling
[Not provided]-->
<!-- @ AUTOMATICALLY GENERATED @ -->

<!--[Not provided]
## Transcriptions
[Not provided]-->
<!-- {{TRANSCRIPTIONS_DESCRIPTION}} -->
<!-- A description of the transcription system used -->

### Writing system
The English writing system is based off of the latin alphabet.
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

#### Symbol table
`a b c d e f g h i j k l m n o p q r s t u v w x y z`
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->

<!--[Not provided]
#### Extralinguistic tags
[Not provided]-->

<!--[Not provided]
### Samples
[Not provided]-->

<!--[Not provided]
#### Questions
There follows a randomly selected sample of questions used in the corpus.
[Not provided]-->
<!-- {{QUESTIONS_SAMPLE}} -->

<!--[Not provided]
#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.
[Not provided]-->
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
* `quality_tags` - some automated assessment of the transcription--audio pair, separated by |
   * `transcription-length` - character per second under 3 characters per second
   * `speech-rate` - characters per second over 30 characters per second
   * `short-audio` - audio length under 2 seconds
   * `long-audio` - audio length over 30 seconds
   * `non-allowed-script` - Tag for transcriptions containing a writing system non associated with the language.
   * `mixed-script-words` - ag for transcriptions containing multiple writing systems at the word/token level.
   * `mixed-script-transcription` - Tag for transcriptions containing multiple writing systems, but each word/token consistently uses a single script
   * `dataset-language-audio-mismatch` - Tag for audio where the spoken language could not be verified that it is in the expected dataset language with high confidence by an ASR model.

#### 
[^1]: For a full list of age, gender, and accent options, see the
[demographics
spec](https://github.com/common-voice/common-voice/blob/main/web/src/stores/demographics.ts). These
will only be reported if the speaker opted in to provide that
information.

## Get involved!

<!--[Not provided]
### Community links
[Not provided]-->
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
* [Contribute questions](https://commonvoice.mozilla.org/spontaneous-speech/beta/question)
* [Validate questions](https://commonvoice.mozilla.org/spontaneous-speech/beta/validate)
* [Answer questions](https://commonvoice.mozilla.org/spontaneous-speech/beta/prompts)
* [Transcribe recordings](https://commonvoice.mozilla.org/spontaneous-speech/beta/transcribe)
* [Validate transcriptions](https://commonvoice.mozilla.org/spontaneous-speech/beta/check-transcript)
<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->

<!--[Not provided]
## Acknowledgements
[Not provided]-->

<!--[Not provided]
### Datasheet authors
[Not provided]-->
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name &lt;email@email.com&gt; -->

<!--[Not provided]
### Citation guidelines
[Not provided]-->
<!-- {{CITATION_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you published a paper and would like people to cite it, you can include the BiBTeX here -->

<!--[Not provided]
### Funding
[Not provided]-->
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.
