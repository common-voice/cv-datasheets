# *Татар* &mdash; Tatar (`tt`)
This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Tatar (`tt`). The dataset contains 30895 clips representing 33 hours of recorded
speech (32 hours validated) from 285 speakers.

## Language
Tatar (татар теле, tatar tele) is a Turkic language spoken by an estimated 5–7 million people,
primarily in the Republic of Tatarstan (within the Russian Federation), as well as in neighboring
regions of Russia, Central Asia, Turkey, China, Finland, and Western Europe.  

It belongs to the Kipchak (Northwestern) branch of the Turkic family, closely related to Bashkir,
Nogai, and Kazakh. The standard form, based on the **Kazan dialect**, is used in education, media,
publishing, and administration in Tatarstan. Other dialects include **Mishar Tatar** (spoken in
western areas) and **Siberian Tatar** (spoken in Siberia).  

Historically, Tatar has been written in several scripts:  
* **Arabic script** — used for centuries until the 1920s.  
* **Latin script (Yanalif)** — introduced in 1928 during language reforms in the Soviet Union.  
* **Cyrillic script** — adopted in 1939 and remains the official script today in Russia.  

Despite Cyrillic remaining the official standard, recent decades have seen **revival efforts to promote a Latin-based orthography**, especially in digital communication, education projects, and diaspora communities. The Latin script is viewed as more internationally accessible and closer to other Turkic languages such as Turkish, Uzbek, and Azerbaijani.

### Variants
There are three main dialect groups of Tatar:  
* **Kazan (Central) Tatar** – the literary standard and most widely spoken.  
* **Mishar Tatar** – spoken in western regions; differs in phonetics and vocabulary.  
* **Siberian Tatar** – spoken in smaller communities in Siberia; more divergent. 
The Common Voice dataset predominantly reflects **Kazan Tatar** due to its dominance in education and media.

## Demographic information
The dataset includes the following distribution of age and gender.
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->

### Gender
Self-declared gender information, percentage refers to the number of clips annotated with this gender.
| Gender | Pertentage |
|-|-|
| Undefined | 21.0% |
| Male Masculine | 76.0% |
| Female Feminine | 3.0% |

<!-- {{GENDER_TABLE}} -->
<!-- @ AUTOMATICALLY GENERATED @ -->
<!-- | Gender | Frequency |
|--------|-----------|
| male, masculine | ? |
| undeclared | ? |
| female, feminine | ? | -->

### Age
Self-declared age information, percentage refers to the number of clips annotated with this age band.
| Age Band | Percentage |
|-|-|
| Undefined | 21.0% |
| Twenties | 5.0% |
| Thirties | 71.0% |
| Fifties | 1.0% |
| Sixties | 1.0% |
| Seventies | 1.0% |

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

The official data splits for modelling this language are as follows. Of the validated clips, 60.30% are included in the splits.

 | Split | Count |
|-|-|
| Train | 8813 |
| Test | 5156 |
| Dev | 4009 |


## Text corpus

The text corpus contains `18083` sentences, of which `18051` are validated, `32` are invalidated and `6` are reported.
<!-- {{TEXT_CORPUS_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- An overview of the text corpus, with information such as average length (in characters and words) of validated sentences. -->

### Writing system
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->
The corpus uses the **Cyrillic alphabet**, the official script for Tatar in Russia. Tatar Cyrillic consists of the standard Russian alphabet plus six additional letters: `Ә` `ә`, `Ө` `ө`, `Ү` `ү`, `Җ` `җ`, `Ң` `ң`, `Һ` `һ`.

#### Symbol table
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->
Valid alphabet characters include:  
А а, Ә ә, Б б, В в, Г г, Д д,
Е е, Ё ё, Ж ж, Җ җ, З з, И и,
Й й, К к, Л л, М м, Н н, Ң ң,
О о, Ө ө, П п, Р р, С с, Т т,
У у, Ү ү, Ф ф, Х х, Һ һ, Ц ц,
Ч ч, Ш ш, Щ щ, Ъ ъ, Ы ы, Ь ь,
Э э, Ю ю, Я я

### Sample
There follows a randomly selected sample of five sentences from the corpus.

```
Аларда художестволы камиллеккә, пөхтәлеккә омтылыш, югары зәвыкка исәп тотып язу көчле иде.
Аның бу дәрте ике нәрсәдән туа.
Аякка бастыру.
Алыштыргысыз кешеләр юк.
Беренче вариант.
```

<!-- {{SENTENCES_SAMPLE}} -->

### Sources
<!-- {{SOURCES_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- A list of sentence sources, can be curated to the top-N -->

### Text domains

| Domain | Count |
|-|-|
| Undefined | 30883 |
| General | 12 |

<!-- {{TEXT_DOMAIN_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What text domains are represented in the corpus? -->

### Processing
<!-- {{PROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- How has the text data been processed -->

### Recommended post-processing
<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What should people do before they use the data, for example Unicode normalisation -->
Users may consider:  
* Unicode normalization (NFC)  
* Removal of extraneous punctuation and symbols  
* Script conversion (e.g. Cyrillic → Latin) for multilingual training

### Fields
Each row of a `tsv` file represents a single audio clip, and contains the following information:

* `client_id` - hashed UUID of a given user
* `path` - relative path of the audio file
* `text` - supposed transcription of the audio
* `up_votes` - number of people who said audio matches the text
* `down_votes` - number of people who said audio does not match text
* `age` - age of the speaker[^1]
* `gender` - gender of the speaker[^1]
* `accent` - accent of the speaker[^1]
* `segment` - if sentence belongs to a custom dataset segment, it will be listed here

#### 
[^1]: For a full list of age, gender, and accent options, see the
[demograpics
spec](https://github.com/common-voice/common-voice/blob/main/web/src/stores/demographics.ts). These
will only be reported if the speaker opted in to provide that
information.

## Get involved!

### Community links

* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/tt/common-voice/contributors/)

<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->

### Discussions
<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->

### Contribute

* [Speak](https://commonvoice.mozilla.org/tt/speak)
* [Write](https://commonvoice.mozilla.org/tt/write)
* [Listen](https://commonvoice.mozilla.org/tt/listen)
* [Review](https://commonvoice.mozilla.org/tt/review)
<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->

## Acknowledgements

### Datasheet authors
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->
Rinat Kharisov <rkharisov.tt@gmail.com> — member of **Yasalma**, a non-profit collective of Tatar language activists and volunteers

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