# *[Bahasa Malay]* &mdash; Bahasa Malay (`ms-MY`)
This datasheet is for version 23.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Bahasa Malay (`ms-MY`). The dataset contains 7 hours of recorded
speech (6 hours validated) from 22 speakers.

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

## Transcriptions

* Prompts: `119`
* Clips: `1144`
* Duration: `22271760[ms]`
* Avg. Transcription Len: `199`
* Avg. Duration: `19.468321678321676[s]`
* Valid Duration: `20287.044[s]`
* Total hours: `6.1866[h]`
* Valid hours: `5.63529[h]`

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
Apakah sebab utama orang dalam komuniti anda berhijrah ke tempat lain?
Bagaimanakah anda menambah nilai, menambah kredit atau membayar untuk telefon bimbit anda
Apakah jenis haiwan peliharaan yang biasa dalam komuniti anda?
Adakah cuaca di negara anda telah mengalami perubahan sepanjang 10 tahun yang lalu?
Apakah jenis dokumen yang anda perlukan untuk membuat perjalanan di dalam negara anda, atau ke negara jiran?
```

<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
There follows a randomly selected sample of transcribed responses from the corpus.

```
Detik pada hidup saya yang sangat gembira adalah semasa saya mencuba memanjat Gunung Kinabalu. Tetapi malangnya tidak dapat mencapai puncaknya. <bunyi> Tetapi dapat melihat puncak adalah sangat gembira.
Ya, buat masa ini saya memandu kereta saya, di mana di- saya selalunya akan menaiki kereta dan membawa kereta saya ke pejabat saya tiap-tiap hari dan juga pada hari minggu.
Dalam budaya saya, kebiasaannya waris-waris terdekat seperti anak-anak ataupun adik-beradik yang akan bergilir-gilir menjaga seseorang yang sedang berada di penghujung nyawanya.
Saya sentiasa memanjatkan doa untuk anak-anak saya dan saya- mereka bebas untuk memilih jalan hidup sendiri.
Saya memandu sebuah kenderaan kereta berjenama Axia.
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

#### 
[^1]: For a full list of age, gender, and accent options, see the
[demograpics
spec](https://github.com/common-voice/common-voice/blob/main/web/src/stores/demographics.ts). These
will only be reported if the speaker opted in to provide that
information.

## Get involved!

### Community links

* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/ms-MY/common-voice/contributors/)

<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->

### Discussions
<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->

### Contribute

* [Speak](https://commonvoice.mozilla.org/ms-MY/speak)
* [Write](https://commonvoice.mozilla.org/ms-MY/write)
* [Listen](https://commonvoice.mozilla.org/ms-MY/listen)
* [Review](https://commonvoice.mozilla.org/ms-MY/review)
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