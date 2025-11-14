# *[Toba Qom]* &mdash; Toba Qom (`tob`)
This datasheet is for version 1.0 of the the Mozilla Common Voice *Spontaneous Speech* dataset 
for Toba Qom (`tob`). The dataset contains 1611 clips representing 11 hours of recorded
speech (11 hours validated) from 25 speakers.

## Language
The Toba Qom language is an endangered language spoken in Gran Chaco, a region spanned over Argentina, Paraguay and Bolivia. As per the official demographic data provided by the Argentinian state, the population of Qom individuals is estimated at 80,000, of which approximately 49% are speakers of the oral form of the language. The term "qom" describes a population that has traditionally been arranged into multiple extended families or groups. Language and sociocultural traits that are essential to qom culture are shared by these groups, which are traditionally hunter-gatherer. 

The contributors to this corpus originate from Chaco and Formosa provinces in Argentina. This area encompasses four ethnodialectal subregions with distinct self-identification terms (Messineo, 1991) [^3].

| Area        | Province               | Locations                                                    | Variant (self-identification) |
| ----------- | ---------------------- | ------------------------------------------------------------ | ----------------------------- |
| Northwest   | Chaco                  | El Colchwón, El Espinillo and the Bermejo river’s surroundings | *dapigemlʔek*                 |
| Northcenter | Chaco                  | Pampa del Indio                                              | *noʔolgaGanaq*                |
| Southcenter | Chaco                  | Sáenz Peña, Machahay, Quitilipi                              | *lʔañaGashek*                 |
| Southeast   | Chaco, Eastern Formosa | Las Palmas, Clorinda                                         | *takshek*                     |

For further information, see [^2] [^3] [^4]. 
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->

## Composition
This corpus consists of 1350 utterances approximately, totalling 10hs of transcribed speech. The dataset does not focus on any particular domain or topics. The question set consists of 150 instances, covering a wide range of general topics about lifestyles and culture (hobbies, education, traditions, nature, food, society, technology, relationships, art, etc). Speakers responded to each question based on their personal belief, experiences, and knowledge, mainly to describe their culture or share their personal opinion about how they interact within the society (e.g. how they would find a lawyer, how they make a medical appointment, etc).

The dataset does not contain any data that might be considered sensitive for others, to the best of the author's knowledge. 

## Demographic information
The corpus includes utterances from 6 speakers (2 female and 4 males). Their languages variants correspond to the speaker locations:

- Chaco: 
  - Quitilipi
  - El Colchón
- Formosa:
  - Clorinda 

The dataset includes the following distribution of age and gender.
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->

### Gender
<!-- Self-declared gender information, frequency refers to the number of clips annotated with this gender. -->
The following ratios represent the amount of utterances from female/male speakers.

Female: 0.2
Male: 0.8
<!-- {{GENDER_TABLE}} -->
<!-- @ AUTOMATICALLY GENERATED @ -->
<!-- | Gender | Frequency |
|--------|-----------|
| male, masculine | ? |
| undeclared | ? |
| female, feminine | ? | -->

### Age
<!-- Self-declared age information, frequency refers to the number of clips annotated with this age band. -->

| Age      | #Speakers |
| -------- | --------- |
| 30-39    | 2         |
| 40-49]   | 0         |
| 50-59    | 3         |
| 60-69    | 1         |
| 70-above | 0         |
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
| Train | 1189 |
| Dev | 210 |

## Data Collection
The data collection involved a coordinator (a PhD student), a linguist known by the Qom contributors (researcher), and three field-work assistants (linguists). The data was collected mainly by the Qom contributors using their own phones at home, after receiving technical training. A small proportion of data was recorded in an academic setting (e.g. research institute) during the training phase. 

## Transcriptions
* Prompts: `136`
* Duration: `37258920[ms]`
* Avg. Transcription Len: `128`
* Avg. Duration: `23.13[s]`
* Valid Duration: `36076.25[s]`
* Total hours: `10.35[h]`
* Valid hours: `10.02[h]`
<!-- {{TRANSCRIPTIONS_DESCRIPTION}} -->
<!-- A description of the transcription system used -->

### Writing system
The transcriptions follows the orthographic systems proposed by Buckwalter (2001) [^2] 
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

#### Symbol table
```a c ch d e g hu i j l ll m n ñ o p q qu r s sh t u v x y ỹ ’```
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->

<!--[Not provided]
#### Extralinguistic tags
[Not provided]-->

### Samples

#### Questions
The following is a curated selection of questions in the corpus.
```
Q1: ’Auachigoxota’aguelo’ naua 'adaqtaqa ’auotaqtapoiguilo’? 
In English, how did you learn the languages you speak?

Q2: ’Eetec da ’auolo’ogue na ’ad’oguiaxac? 
In Spanish, “¿Cómo cuidás (mirás por) tu cuerpo?”

Q3: ’Eetec da qaica ca machaqcoom qataq yayamaqchiguiñi da ’antounaxac?
In Spanish, “Cómo te relajás (que esté todo bien) y tener bien tu mente (pensamiento)”
```

There follows a randomly selected sample of questions used in the corpus.
```
¿Chalcata naxa da’au’a que’eca nataxannaxanaq can ’am cocho’olec?
¿Negue’t na no’onatac nam ỹaguec da qai’ot yi ’adma’?
¿Negue’t aca lede lmalate ihuen ca ’oonolec da coleetac qataq da taỹa ca l-lla alhua?
¿Tashe ’au’axat da lataxac na ’adhuodeuapi yi ’adma’?
Eetec na napo yi arma?
```
<!-- {{QUESTIONS_SAMPLE}} -->

#### Responses
The following is a curated selection of responses in the corpus.
```
A1: Ayem naua ya’aqtaqa nagui sachegoxoto’oto soua yapiyilpi qataq so iquedoxonapi qom l'aqtaqa. 
In Spanish, “yo el idioma que hoy hablo aprendí de mis abuelitos y de mis ancianas, el idioma qom”

A2: Ayem da selotague' dam yio'ocyaxac saishet da choche ñi so'otañi so'oshiguem sequeuoiapigui'. 
In Spanish, “para cuidar mi cuerpo no solo me quedo sentado, sino me levanto y camino.”

A3: Ayem da selotague’ dam yio’ocyaxac saishet da choche ñi so’otañi so’oshiguem sequeuoiapigui’. 
In Spanish, “para cuidar mi cuerpo no solo me quedo sentado, sino me levanto y camino.”
```

There follows a randomly selected sample of transcribed responses from the corpus.
```
Naua na'aqtaqa sacheta'ape lalamaxat na qom qaq ra le'enaxat qom la'aqtaqa 
Yi imaa heq na shiaxauapi tahiaa' ca lya alua' l'lia cha aye ilotaque eca lonatac
Ra huo'o ca'aca sano'on ye ima'   qaiaxaneuga ca'aca lnotaxaqui ne'ena dalolaxaicpi nache ra pasa'aguet nache nataqaen pasa' ivira ca'aca ivireua' ca'aca huetaigui na nata'  huetaigui na natannanaxanaxatpi ca qanmit qataq ra qailalec cam eca lalolaxa nache qoiami' que'eca lata' cam ecaeso qarqaia ra sano'on
Ana'ana nmejna huetaigui na lqui'ipi na ashaxaicpi qataq na onaxanaxaicpi nache huo'o naxa da ñimeten na potoro l'oli da qaichaxan
Ra ñishitaique qataq sañalo'oguet da io'onaxanaxac lamaic aiem sacona aso ivique nache so'onaxatac qaq ra so'onaxatac  nache no'oita naqaen aiem era ra so'ot aiem
```
<!-- {{TRANSCRIPTIONS_SAMPLE}} -->

### Recommended post-processing
To be updated in the next release. Contact the author for details. 
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
[^1]: For a full list of age, gender, and accent options, see the [demographics spec](https://github.com/common-voice/common-voice/blob/main/web/src/stores/demographics.ts). These will only be reported if the speaker opted in to provide that information.
[^2]: Buckwalter, Alberto. 2001 [1980]). Vocabulario toba. Formosa / Indiana: Equipo Menonita / Mennonite Board of Missions. Ed. Revisada.
[^3]: Messineo, Cristina. 1991. Variantes dialectales del complejo lingüístico toba. Hacia una nueva carta étnica del Gran Chaco II: 12-22. Las Lomitas: Centro del Hombre Antiguo Chaqueño.
[^4]: Messineo, Cristina. 2003. Lengua Toba (guaycurú). Aspectos gramaticales y discursivos. Lincom Studies in Native American Linguistics 48. Münich: Lincom Europa.

## Get involved!

### Community links
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/tob/common-voice/contributors/)
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

## Acknowledgements

### Datasheet authors
* Belu Ticona
* Paola Cúneo
* Antonios Anastasopoulos
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name &lt;email@email.com&gt; -->

### Citation guidelines
B. Ticona, P. Cuneo. A. Anastasopoulos. “Datasheet of Spontaneous Speech Corpus for Qom - Mozilla Common Voice”. Revised on Aug 29th, 2025. [Publication Date].
<!-- {{CITATION_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you published a paper and would like people to cite it, you can include the BiBTeX here -->

### Funding
This dataset was partially funded by the *Open Multilingual Speech Fund* managed by Mozilla Common Voice.

The speaker collaborators were funded by Mozilla Common Voice. The project coordinator was partially funded by the US NSF grants 2346334 and 2439202.
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.