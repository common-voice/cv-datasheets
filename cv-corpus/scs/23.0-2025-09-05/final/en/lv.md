# *Latviešu* &mdash; Latvian (`lv`)
This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Latvian (`lv`). The dataset contains 229955 clips representing 311 hours of recorded
speech (263 hours validated) from 6508 speakers.

## Language
Latvian is an Baltic language belonging to the Indo-European language family. It is spoken in the Baltic region,
and is the official language of Latvia as well as one of the official languages of the European Union.
There are about 1.5 million native Latvian speakers in Latvia and 100,000 abroad. 
It uses the Latin alphabet with additional diacritical marks to represent specific sounds.
<!-- Provide a brief (1-2 paragraph) description of your language -->

### Variants
There are slight stylistic speach variations among different regions of Latvia, but they do not affect mutual 
intelligibility. Latgale region has more significant differences with main Latvian language. It is sometimes 
considered a dialect, but Latgalian (`ltg`) speech is collected as a separate language in Common Voice.
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->

## Demographic information
The dataset includes the following distribution of age and gender.
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->

### Gender
Self-declared gender information, percentage refers to the number of clips annotated with this gender.
| Gender | Pertentage |
|-|-|
| Undefined | 45.0% |
| Male Masculine | 25.0% |
| Female Feminine | 30.0% |
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
| Undefined | 44.0% |
| Twenties | 6.0% |
| Thirties | 29.0% |
| Teens | 1.0% |
| Fourties | 9.0% |
| Fifties | 8.0% |
| Sixties | 2.0% |
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
The official data splits for modelling this language are as follows. Of the validated clips, 15.17% are included in the splits.

 | Split | Count |
|-|-|
| Train | 14432 |
| Test | 7728 |
| Dev | 7728 |

## Text corpus
The text corpus contains `99526` sentences, of which `34448` are validated, `65078` are invalidated and `3143` are reported.
<!-- {{TEXT_CORPUS_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- An overview of the text corpus, with information such as average length (in characters and words) of validated sentences. -->

### Writing system
Latvian alphabet is based on the Latin script and consists of 33 letters, including special characters with
diacritical marks such as ā, č, ē, ģ, ī, ķ, ļ, ņ, š, ū, and ž.

Historic texts also used letter /ŗ/, but use of it has been officially discontinued since 1946. 
This letter is equivalent to letter /r/ in modern Latvian orthography.

Letter /o/ can represent three different sounds [ua̯], [ɔ], [ɔː].

Letter /e/ can represent two different sounds [e], [æ].

<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

#### Symbol table
```
a ā b c č d e ē f g ģ h i ī j k ķ l ļ m n ņ o p r s š t u ū v z ž
```
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->

### Sample
There follows a randomly selected sample of five sentences from the corpus.

```
Uzzinājis par kureliešu atbruņošanu, leitnants Rubenis pavēlēja bataljonam doties pārgājienā.
Mācījās Napoleona Asmusa privātskolā, vēlāk bija māceklis sava tēva koktirdzniecības uzņēmumā.
"Jo manai "sapņu princesei" vajadzētu māju, automašīnu un daudz skaistu tērpu."
Alus brūvēšanu, šņabja sagādi, malkas sagādi lokmobīlei.
Karavīri uzdāvināja frontes paciņu, kurā atradās saldumi un šokolādes tāfelīte.
```
<!-- {{SENTENCES_SAMPLE}} -->

### Sources
Text sources in the dataset consists of user added content as well as balanced sets of samples from Wikipedia,
European parliament transcripts, out of copyright books and other sources.
<!-- @ OPTIONAL @ -->
<!-- A list of sentence sources, can be curated to the top-N -->

### Text domains
| Domain | Count |
|-|-|
| Undefined | 229120 |
| Agriculture Food | 8 |
| Automotive Transport | 3 |
| Finance | 4 |
| Service Retail | 16 |
| General | 694 |
| Healthcare | 36 |
| History Law Government | 8 |
| Language Fundamentals | 9 |
| Media Entertainment | 16 |
| Nature Environment | 40 |
| News Current Affairs | 5 |
| Technology Robotics | 13 |
<!-- {{TEXT_DOMAIN_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What text domains are represented in the corpus? -->

### Processing
<!-- {{PROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- How has the text data been processed -->

### Recommended post-processing
* Filter out clips with /ŗ/
* Filter out clips with characters not in the Latvian alphabet
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
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/lv/common-voice/contributors/)
* [Balsu talka](https://balsutalka.lv/)
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->

### Discussions
<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->

### Contribute
* [Speak](https://commonvoice.mozilla.org/lv/speak)
* [Write](https://commonvoice.mozilla.org/lv/write)
* [Listen](https://commonvoice.mozilla.org/lv/listen)
* [Review](https://commonvoice.mozilla.org/lv/review)
<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->

## Acknowledgements

### Datasheet authors
Raivis Dejus <orvils@gmail.com>
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