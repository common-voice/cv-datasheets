# *Punu qhichwa* &mdash; Puno Quechua (`qxp`)
This datasheet is for version 1.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Puno Quechua (`qxp`). The dataset contains 1075 clips representing 6 hours of recorded
speech (6 hours validated) from 11 speakers.

## Language
Puno Quechua, identified by the ISO 639-3: [qxp](https://iso639-3.sil.org/code/qxp), belongs to the Quechua II group. The [2017 National Census in Peru](https://www.gob.pe/en/535-check-results-of-the-2017-national-census) estimates approximately 474203 speaker of Puno Quechua, predominantly in the Puno region of Peru.
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
| Train | 173 |
| Test | 422 |
| Dev | 480 |
<!-- @ AUTOMATICALLY GENERATED @ -->

## Transcriptions
* Prompts: `150`
* Duration: `18708156[ms]`
* Avg. Transcription Len: `158`
* Avg. Duration: `17.4[s]`
* Valid Duration: `18708.16[s]`
* Total hours: `5.2[h]`
* Valid hours: `5.2[h]`
<!-- {{TRANSCRIPTIONS_DESCRIPTION}} -->
<!-- A description of the transcription system used -->

### Writing system
The writting system for the Puno Quechua language is not formaly described, however there are some resources that can be mentioned. Linguistic resources for Puno Quechua, as cataloged by Glottolog [puno1238](https://glottolog.org/resource/languoid/id/puno1238), are predominantly from the 1963–1993 period, with limited publications post-2005. These materials offer critical insights into the Puno Quechua language's grammatical framework. Like all Quechua languages, Puno Quechua forms words by sequentially adding suffixes to a root and follows a Subject-Object-Verb (SOV) word order.
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

### Samples

#### Questions
The following is a curated selection of questions used in the corpus.
```
*Huñullachu icha sapallaykichu llank'ayta munawaq? Imarayku?*
*Pipas wañupuqtin hinaqa, imatataq ruwankichis llaqtaykipi?*
*Aylluykipi, imaynatataq qullqita waqaychayta yachankichis?*
```

There follows a randomly selected sample of questions used in the corpus.
```
Imaraykutaq hanaqpacha anqas kanman?
Aylluykipi, musqhuykuna imatataq niyta munanku?
Chaqrapi tarpuy pachamanta rimariy.
Ancha suwakuna kapun, imaraykutaq chay?
Imatan ruwayta munanki minchha p'unchay?
```
<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
The following is a curated selection of transcribed responses from the corpus.
```
Masiykunawan tupani hinaqa asikuspallaykun puriyku, chaymanta mikhuspapis lumata purispapis, takiqpis riyku ima. Aqnatan.
Llaqtaman urayuyku hinaqa chaqramanta huqarisqakunata qhatuyku qhatuna wasipi, runa mink'akuqpis puriyku, utaq ayllumasiykuta watukuq riyku, anchaymi llaqtapi p'unchaykunaqa.
Nuqaqa llank'ani sapallay, nuqataq warmi kani nuqataq qhari kani, hina chaqra ruwayñiykunata. Waq amikuykunapis kallantaq anchiykunatapis ayutallawantaq hina, chaykunata llank'ani: papata, kinuwata, qañiwa siwarata, todo agricultura.
```

There follows a randomly selected sample of transcribed responses from the corpus.
```
Riqsini puka, q'illu, anqas, q'umir, yana, yuraq, qulli llimphikunata. Chay llimp'ikunatan p'achaykupi, lliqllaykupi qhawanki.
Llaqtaypiqa musqhuykunataqa chaninchaykun. Taytamamaykunaqa ninku musqhuykunaqa willakuymi, imapas paqarin minchha pasananmanta. Wawakunaymanpas willariq kani, amaruwan musqhuspaqa allinmi, qullqi kanqa; waqrawan musqhuspataq maqanakuymi kanqa, nispa.
Aylluypiqa ima sasachakuypis kan hina, nuqanchismantarayku qayllanakuyku ima atisqaykupi yanapakuykunapaq. Wakinqa uywata michin, wakin chaqrawan yanapakun, wakintaq huq chhiqasmanta huq chhiqaqman apanakuyku.
Q'ala phuyukuna pichakapunku hina, qasallanpuni, chiwraq kapun hina qasa pasaqtaraq chayamun, lumakunatapis yuraqtaraq saqirqapun qhipa p'unchaypaq.
Wawa unquq warmikunataqa hampina wasipi qhawarinku, chaypin hampiq, unquq yanapaq, hampi kamachiq ima llamk'anku.
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
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/qxp/common-voice/contributors/)
* [QuechuaBase telegram group](https://t.me/QuechuaBase)
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
* Elwin Huaman &lt;elwin.huaman@hotmail.com&gt;
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name &lt;email@email.com&gt; -->

### Citation guidelines
If you use this dataset in your research, please cite the following publication:

```bibtex
    @inproceedings{HuamanHHQ25,
    author       = {Elwin Huaman and
                    Jorge Luis Huaman and
                    Wendi Huaman and
                    Ninfa Quispe},
    title        = {Quechua Speech Datasets in Common Voice: The Case of Puno Quechua},
    booktitle    = {Information Management and Big Data - 12th Annual International Conference, SIMBig 2025, Lima, Peru, October 29-31, 2025, Proceedings},
    series       = {Communications in Computer and Information Science},  
    publisher    = {Springer},
    year         = {2025},
    }
```
<!-- {{CITATION_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you published a paper and would like people to cite it, you can include the BiBTeX here -->
<!-- Submitted to SIMBig 2025 (Needs confirmation). -->

### Funding
This dataset was partially funded by the *Open Multilingual Speech Fund* managed by Mozilla Common Voice.
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.
