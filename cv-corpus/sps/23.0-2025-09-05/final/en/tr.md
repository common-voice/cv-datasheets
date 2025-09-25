# *Türkçe* &mdash; Turkish (`tr`)
> This datasheet has been generated automatically, we would love to include more information, if you would like to help out, [get in touch](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)!

 This datasheet is for version 23.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Turkish (`tr`). The dataset contains 25 clips representing 1 hours of recorded
speech (1 hours validated) from 8 speakers.

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

## Transcriptions
* Prompts: `25`
* Duration: `556632[ms]`
* Avg. Transcription Len: `219`
* Avg. Duration: `22.27[s]`
* Valid Duration: `284.08[s]`
* Total hours: `0.15[h]`
* Valid hours: `0.08[h]`
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
Yabancı dille eğitim yapılması konusunda ne düşünüyorsun?
Arkadaşlarınla vakit geçirdiğinde en çok ne yapmaktan hoşlanırsın?
En sevdiğin mevsim hangisi?
Sabahları enerjik olmanı sağlayan şey nedir?
Dünyanın bir yerinde yaşamak istesen neresi olurdu?
```
<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.

```
Çocukluğumda en sevdiğim oyun yakan toptu. İki grup halinde oynanıyordu. Ee, gruplardaki kişiler topa yakalanmamaya çalışıyorlardı, burada bir bireysellik vardı. Yakalanan grup arkadaşlarını da kurtarmaya da çalışıyorlardı, burada da grup oyunu da vardı. Bu ikisini de birleştirdiği için, aynı zamanda iki takım halinde olduğundan dolayı rekabet de vardı. Bu yüzden çok seviyordum o oyunu.
Abimin mimar olmasının da etkisi var sanırım, mimar olmak isterdim hep. Olmadı... Herhalde yeniden dünyaya gelsem, mimar olmak isterdim...
En sevdiğim mevsim ilkbahardır. İlkbahar, ee, doğanın uyanışını simgelediği için, ee, diğer mevsimlere göre bende ayrı bir yerdedir.
Bana göre özel ve paralı okullar olmamalı. Fırsat eşitliğini bozuyor, öncelikle. Eee, özel ve paralı okullarda altyapı daha iyi olabilir, ama aslında bütün okullar devlet tarafından finanse edilmeli, aynı sağlık gibi, ve bütün okullar eşit yüksek kalitede olmalı, çünkü eğitim en önemli şeyimiz.
Ortalama bir günümde, sürekli bilgisayar başındayım, yani günde böyle 12, 16 saat falan, ee, sürekli bir şeyler üretiyorum, bir şeyler öğreniyorum. Ee, tabii normal sosyal yaşam da var, ama gün geçtikçe azalıyor bu, daha çok eve kapalı yaşamayı tercih ediyorum. Özellikle ee, zaman daha hızlı geçiyor gibi geliyor bana yaş ilerledikçe.
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
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/tr/common-voice/contributors/)
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