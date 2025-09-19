# *català* &mdash; Catalan (`ca`)
This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Catalan (`ca`). The dataset contains 2658094 clips representing 3403 hours of recorded
speech (2883 hours validated) from 36898 speakers.

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->
Catalan is a Romance language spoken by about 9 milion people mainly on the Mediterranean coast of the Iberian Peninsula. 

It is an official language, along with Spanish or Castilian, in Catalonia, the Balearic Islands and the Valencian Community (where it
is also called Valencian), while it is the only official language of the Principality of Andorra. It is also spoken, and has some administrative recognition, without reaching official status,
in the eastern part of the autonomous community of Aragon, in the French department Pyrénées-Orientales (Eastern
Pyrenees) and in the city of Alghero, on the island of Sardinia (Italy).

The language evolved from Vulgar Latin in the Middle Ages.

### Variants
<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->
The main variants of Catalan are:
* Central: It is the variant with the most speakers, as it encompasses the metropolitan area of Barcelona, extending to the region of Girona and the eastern half of Tarragona
* Nord-western: Spoken in Andorra, Lleida and the western half of Tarragona in Catalonia, and the eastern part of Aragon
* Valencian: Spoken in the Valencian comunity, where it's also known as "Valencian"
* Northern: Corresponds to the area of Roussillon and the northern part of Girona
* Balearic: The variant used in the Balearic Islands
* Alguerese: Spoken in the city of Alghero, in Sardinia

## Demographic information
The dataset includes the following distribution of age and gender.
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->

### Gender
Self-declared gender information, percentage refers to the number of clips annotated with this gender.
| Gender | Pertentage |
|-|-|
| Undefined | 27.0% |
| Male Masculine | 52.0% |
| Female Feminine | 20.0% |

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
| Undefined | 27.0% |
| Twenties | 4.0% |
| Thirties | 5.0% |
| Teens | 1.0% |
| Fourties | 12.0% |
| Fifties | 19.0% |
| Sixties | 29.0% |
| Seventies | 4.0% |

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

The official data splits for modelling this language are as follows. Of the validated clips, 54.59% are included in the splits.

 | Split | Count |
|-|-|
| Train | 1212809 |
| Test | 16415 |
| Dev | 16415 |


## Text corpus

The text corpus contains `1307340` sentences, of which `1302505` are validated, `4835` are invalidated and `8864` are reported.
<!-- {{TEXT_CORPUS_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- An overview of the text corpus, with information such as average length (in characters and words) of validated sentences. -->

### Writing system
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

Catalan is written using the Latin alphabet (abcdefghijklmnopqrstuvwxyz), with the special characters *ç* and *l·l*. In addition, vowels can be accented (à, è, é, í, ò, ó, ú, ü, ï). The characters *-* (hyphen) and *'* (apostrophe) are also part of Catalan orthography.

#### Symbol table
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->
```a b c ç d e f g h i j k l m n o p q r s t u v w x y z à è é í ò ó ú ï ü```

### Sample
There follows a randomly selected sample of five sentences from the corpus.

```
Després d'algunes mudes es transformen en pupa.
Va ser Director General en diferents governs de Jordi Pujol.
Va ser un altre avatar de Devi Laxmi.
El de Sanchi tenia una execució menys refinada, i estava en pitjors condicions. 
Res ni ningú guanyar ni doblegarà les nostres ànsies de llibertat, va escriure.
```

<!-- {{SENTENCES_SAMPLE}} -->


### Text domains

| Domain | Count |
|-|-|
| Undefined | 2657032 |
| Agriculture Food | 44 |
| Automotive Transport | 27 |
| Finance | 4 |
| Service Retail | 63 |
| General | 618 |
| Healthcare | 34 |
| History Law Government | 65 |
| Language Fundamentals | 32 |
| Media Entertainment | 33 |
| Nature Environment | 114 |
| News Current Affairs | 32 |
| Technology Robotics | 21 |

<!-- {{TEXT_DOMAIN_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What text domains are represented in the corpus? -->

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

* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/ca/common-voice/contributors/)

<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->


### Contribute

* [Speak](https://commonvoice.mozilla.org/ca/speak)
* [Write](https://commonvoice.mozilla.org/ca/write)
* [Listen](https://commonvoice.mozilla.org/ca/listen)
* [Review](https://commonvoice.mozilla.org/ca/review)
<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->

## Acknowledgements

### Datasheet authors
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->

Common Voice Community

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.
