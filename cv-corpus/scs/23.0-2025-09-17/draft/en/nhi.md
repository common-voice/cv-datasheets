# *[Western Sierra Puebla Nahuatl]* &mdash; Western Sierra Puebla Nahuatl (`nhi`)
This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Western Sierra Puebla Nahuatl (`nhi`). The dataset contains 0.6 hours of recorded
speech (0.1 hours validated) from 6 speakers.

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->

### Variants
<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->

## Demographic information
The dataset includes the following distribution of age and gender.
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->

### Gender
Self-declared gender information, frequency refers to the number of clips annotated with this gender.
| Gender | Frequency |
|-|-|
|  | 0.19 |
| Male Masculine | 0.08 |
| Female Feminine | 0.73 |
| Transgender | 0 |
| Non-Binary | 0 |
| Do Not Wish To Say | 0 |

<!-- {{GENDER_TABLE}} -->
<!-- @ AUTOMATICALLY GENERATED @ -->
<!-- | Gender | Frequency |
|--------|-----------|
| male, masculine | ? |
| undeclared | ? |
| female, feminine | ? | -->

### Age
Self-declared age information, frequency refers to the number of clips annotated with this age band.
| Age Band | Frequency |
|-|-|
|  | 0.19 |
| Twenties | 0.73 |
| Thirties | 0.08 |
| Teens | 0 |
| Fourties | 0 |
| Fifties | 0 |
| Sixties | 0 |
| Seventies | 0 |
| Eighties | 0 |
| Nineties | 0 |

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

## Text corpus

* Reported sentences: `0`
* Validated sentences: `758`
* Unvalidated sentences: `11`
* Clips: `427`
* Users: `6`
* Avg duration: `5.081[s]`
* Valid duration: `203.239[s]`
* Total hours: `0.6`
* Valid hours: `0.05`

<!-- {{TEXT_CORPUS_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- An overview of the text corpus, with information such as average length (in characters and words) of validated sentences. -->

### Writing system
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

#### Symbol table
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->

### Sample
There follows a randomly selected sample of five sentences from the corpus.

```
Isqui aquin yoquinpaleuito.
Uan niquihlnamiqui a veses oquiyouiya.
Ich n quince tlamis niluitl.
Tlen milauac ne yonimomohteh
Nin se libro itoca mach "rana, can ticah?" quimotlahtlania se telpucatl.
```

<!-- {{SENTENCES_SAMPLE}} -->

### Sources
<!-- {{SOURCES_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- A list of sentence sources, can be curated to the top-N -->

### Text domains

| Domain | Count |
|-|-|
|  | 427 |
| Agriculture Food | 0 |
| Automotive Transport | 0 |
| Finance | 0 |
| Service Retail | 0 |
| General | 0 |
| Healthcare | 0 |
| History Law Government | 0 |
| Language Fundamentals | 0 |
| Media Entertainment | 0 |
| Nature Environment | 0 |
| News Current Affairs | 0 |
| Technology Robotics | 0 |

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

* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/nhi/common-voice/contributors/)
* [Original language request on GitHub](https://github.com/common-voice/common-voice/issues/3889)
<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->

### Discussions
<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->

### Contribute

* [Speak](https://commonvoice.mozilla.org/nhi/speak)
* [Write](https://commonvoice.mozilla.org/nhi/write)
* [Listen](https://commonvoice.mozilla.org/nhi/listen)
* [Review](https://commonvoice.mozilla.org/nhi/review)
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