# *Norsk Nynorsk* &mdash; Norwegian Nynorsk (`nn-NO`)
This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Norwegian Nynorsk (`nn-NO`). The dataset contains 1.7 hours of recorded
speech (1.5 hours validated) from 40 speakers.

## Language
Norwegian Nynorsk is a written standard of Norwegian. The standard is the preferred written 
standard of around 10-15% of the Norwegian population and is largely based on the Norwegian dialects
of the West of Norway.

The language code is `nn` and the locale is `nn-NO` (Nynorsk as written in Norway). Note that this 
locale includes the region code for historical reasons relating to the localisation platform. The dataset
contains Norwegian as spoken anywhere and as written in the Nynorsk standard.
<!-- ### Variants -->
<!-- Original Answer: -->
<!-- There are currently no variants defined for Norwegian Nynorsk. -->

## Demographic information
The dataset includes the following distribution of age and gender.

### Gender
Self-declared gender information, percentage refers to the number of clips annotated with this gender.
| Gender | Pertentage |
|-|-|
| Undefined | 29.0% |
| Male Masculine | 58.0% |
| Female Feminine | 13.0% |

### Age
Self-declared age information, percentage refers to the number of clips annotated with this age band.
| Age Band | Percentage |
|-|-|
| Undefined | 26.0% |
| Twenties | 28.0% |
| Thirties | 40.0% |
| Teens | 2.0% |
| Fourties | 3.0% |
| Fifties | 1.0% |

## Text corpus
The average length of sentences is 7 tokens (42 characters).

### Writing system
Norwegian is written in the Latin script. The text corpus also contains a limited amount of punctuation.

#### Symbol table
|Symbol|
|---|
| a | 
| å | 
| æ | 
| b | 
| c | 
| d | 
| e | 
| é | 
| è | 
| f | 
| g | 
| h | 
| i | 
| j | 
| k | 
| l | 
| m | 
| n | 
| o | 
| ò | 
| ø | 
| p | 
| q | 
| r | 
| s | 
| t | 
| u | 
| v | 
| w | 
| x | 
| y | 
| z | 
| ! | 
| - | 
| . | 
| ? |

### Sample
There follows a randomly selected sample of five sentences from the corpus.

```
Dette med følg boka skjønte eg heller ikkje heilt vitsen med.
Eg har ikkje mykje om kap.
Ei rettssak er i grunnen ein fin måte å stille ting i relieff på.
Kva er forklaringa på at regjeringa enno ikkje har følgt dette opp?
Eg gler meg også til å lesa.
```

*Automatic random samples*

```
Har vurdert å laga eit slektskart!
Derfor bruker eg ikkje å setje om sitat frå andre språk enn norsk.
Ein av dei fremste språkpedagogane i Norden er Viljo Kohonen.
Les ho gjerne!
Eg seier ofte at eg ikkje likar krim.
```

### Sources
* [Korpus med bokomtalar frå Bokelskere.no](https://www.nb.no/sprakbanken/en/resource-catalogue/oai-nb-no-sbr-53/) (Public domain)
* [Stortingskorpuset 1.1](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-58/) (Public domain)
* Individual sentences submitted by users through the Mozilla Common Voice interface (Public domain)

### Text domains
The corpus was initially seeded with sentences from
* Book reviews and book discussions (from the web community bokelskere.no)
* Transcribed and manually checked discussions from the Norwegian Parliament (Stortinget), from 2017 to 2018

Later, several individual users have contributed sentences in various
domains through Mozilla's web interface.

### Processing
Both sources include sentences in both Norwegian Nynorsk and Norwegian Bokmål.

Norwegian Nynorsk candidate sentences were extracted by both excluding Bokmål-only words and including 
Nynorsk-only words:

| Only       | Words   |
|------------|------------|
| Bokmål |  *ikke*, *jeg*, *en*, *et*, *fra*, *hun*, *noen*, *være*, *mer*, *ble*, *mye*, *bare*, *boken*, *kommer*, *flere*, *dem*  |
| Nynorsk |  *eg*, *ikkje*, *ein*, *me*, *vere*, *meir*, *fleire*, *berre*, *ho*, *eit*, *blei*, *vart*  | 

These candidate sentences were then checked by two writers of Nynorsk to ensure that they were indeed written
in Nynorsk before inclusion into the corpus.

## Get involved!
To get more information about this dataset and find out how you can contribute, please 
take a look at the following links.

### Community links
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/nn-NO/common-voice/contributors/)

### Discussions
* [Merging Norwegian Nynorsk and Norwegian Bokmål](https://discourse.mozilla.org/t/merging-norwegian-nynorsk-and-norwegian-bokmal/130474) (2024)
* [Norwegian speech and its dialect and sentence problem](https://discourse.mozilla.org/t/norwegian-speech-and-its-dialect-and-sentence-problems/30568) (2018)

### Contribute
* [Contribute voice recordings](https://commonvoice.mozilla.org/nn-NO/speak)
* [Contribute sentences](https://commonvoice.mozilla.org/nn-NO/write)
* [Validate recordings](https://commonvoice.mozilla.org/nn-NO/listen)
* [Review sentences](https://commonvoice.mozilla.org/nn-NO/review)

## Acknowledgements

### Datasheet authors
* Francis M. Tyers <ftyers@iu.edu>
* Kevin B. Unhammer <unhammer@fsfe.org>

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.