# *[Eastern Min]* &mdash; Eastern Min (`cdo`)
This datasheet is for version 23.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Eastern Min (`cdo`). The dataset contains 1045 clips representing 10 hours of recorded
speech (1 hours validated) from 31 speakers.

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
| Train | 683 |
| Test | 239 |
| Dev | 123 |


## Transcriptions

* Prompts: `119`
* Duration: `35655192[ms]`
* Avg. Transcription Len: `91`
* Avg. Duration: `34.12[s]`
* Valid Duration: `3380.94[s]`
* Total hours: `9.9[h]`
* Valid hours: `0.94[h]`

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
社會如何幫助需要協助的人？
你對使用科技的好處和風險有什麼看法？
你希望你的社區能有更多哪些類型的商家？
你最常用科技做什麼？
你對長時間步行有什麼看法？為什麼？
```

<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.

```
我喜欢的音乐节叻就是贝多芬贝多芬他的镨啊曲啊哇都是很很生动的嗯表演出来
我做小孩子的时候那时候想的是要做scientist 不然就是做警察做宾士到后来大的时候最近scientist 就是engineer 咯那个土木工程咯读土木工程咯
我们国家这边叻有很多种的病啊大多数叻有糖尿病血压还有呃毒瘤还有胆固醇高呃大多数病都是较好命的人才会中到这样的病然后叻较平常的叻应该也有呃会咳嗽啊
这个社会有很多坎苦的人。他们生活非常困难。这种人需要政府在赚钱方向帮助他们。用他们可以在这个社会生活。
药叻我们很多都是吃西药中药要吃较少不过有时候会吃参参拿泡下然后当水喝喝了有体力身体会较好六
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

* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/cdo/common-voice/contributors/)

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