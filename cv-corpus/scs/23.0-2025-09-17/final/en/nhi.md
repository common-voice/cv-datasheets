# *Maseualtlahtol* &mdash; Western Sierra Puebla Nahuatl (`nhi`)

This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Western Sierra Puebla Nahuatl (`nhi`). The dataset contains 0.6 hours of recorded
speech (0.1 hours validated) from 6 speakers.

## Language

<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->
Western Sierra Puebla Nahuatl, alternatively Zacatlán-Ahuacatlán-Tepetzintla Nahuatl, is a 
variety of Nahuatl spoken in the Northwestern region of Puebla's Sierra Norte. A 2009 report
from Mexico's National Institute of Indigenous Languages estimates approximately 17,000 speakers.

The language code is `nhi`. There is quite a bit of variation within the nhi variant, varying between
municipalities and communities. For example, some towns, near San Miguel Tenango, use "inverted prefixes" compared
to the rest of the Nahuatl-speaking area, (e.g. *in-nihnimi* instead of *ni-nihnimi*, "I walk").
The sentences in this corpus come from the `nhi` Universal Dependencies treebank, which is made up of samples 
from all three municipalities, and a set of dictionary-style example sentences written by a speaker from the 
Tepetzintla municipality.

### Variants 

<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->
There are currently no variants defined for Western Sierra Puebla Nahuatl.

## Demographic information
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->
The dataset includes the following distribution of age and gender.

### Gender

Self-declared gender information, frequency refers to the number of clips annotated with this gender.

<!-- {{GENDER_TABLE}} -->
<!-- @ AUTOMATICALLY GENERATED @ -->
<!-- 
| Gender | Frequency |
|--------|-----------|
| male, masculine | ? |
| undeclared | ? |
| female, feminine | ? |
-->
### Age

Self-declared age information, frequency refers to the number of clips annotated with this age band.

<!-- {{AGE_TABLE}} -->
<!-- @ AUTOMATICALLY GENERATED @ -->
<!-- 
| Age band | Frequency |
|----------|-----------|
| teens | ? |
| twenties | ? |
| thirties | ? |
| fourties | ? |
| fifties | ? |
   ...if other age ranges are present in your data, add rows...
-->

## Text corpus

<!-- {{TEXT_CORPUS_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- An overview of the text corpus, with information such as average length (in characters and words) of validated sentences. -->

The average length of validated sentences is 5.5 words (34 characters). The corpus contains numerous Spanish loanwords, calques, and code-switching. For example, the following sentence from the corpus contains the Spanish conjunction *pero* "but", Spanish preposition *de* "of", the subordinator *hasta* "until", a morphologically-adapted loanword *oniquestudiaro* (from *estudiar* "to study"), and a morphologically-adapted number, *ocho* "eight" (*tiochoque* "we are eight"). Due to long-standing language contact and bilingualism, Nahuatl commonly incorporates elements of Spanish, and this is well-represented in the text corpus.

> *Pero de nochten tlen tiochoque sa ye neh oniquestudiaro hasta cuando onipiyaya dieciocho años.*
> 
> "But of all of us eight I was the only one who studied until when I was eighteen years old."

### Writing system

<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

Western Sierra Puebla Nahuatl is written in the Latin script. Specifically, the Common Voice corpus uses an orthographic 
norm defined by the Summer Institute of Linguistics in collaboration with the nhi-speaking community in San Miguel Tenango, 
Zacatlán, Puebla. See this [Description of the nhi alphabet](https://www.sil.org/system/files/reapdata/53/94/82/53948241349464823321651210693778285566/nhi_17154_El_alfabeto_del_nahuatl_de_los_municipios_07_002.pdf) for more information.

In most cases, Spanish loans, even those with Nahuatl morphology, are written in standard Spanish orthography (the Nahuatl morphemes follow the Nahuatl orthography described here, though it is worth noting the similarities between the writing systems so that there are only rare cases where the orthography change is noticeable).

#### Symbol table

<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->

`a b c ch cu d e f g h i j k l m n ñ o p qu r s t tl tz u v w x y`

Note that of the alphabet listed above, `b d f g j k ñ r v w` are used for loanwords and some proper names only.

### Sample

There follows a randomly selected sample of five sentences from the corpus.

<!-- {{SENTENCES_SAMPLE}} -->
```
Uan quitzahtzilihtoc nirana mach canih cah.
Pero neh amo onimatiya tleno nicchiuas mox nimocauas o niyas.
Pero bueno, sa amo tlen sequichiua.
Iuah tiyas n Luis o aquin oc se?
Cualtzin uelic atzintlin
```

### Sources

<!-- {{SOURCES_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- A list of sentence sources, can be curated to the top-N -->

* [subset of UD corpus](https://github.com/UniversalDependencies/UD_Western_Sierra_Puebla_Nahuatl-ITML) (Public domain)
* Individual sentences submitted by users through the Mozilla Common Voice interface (Public domain)

### Text domains

<!-- {{TEXT_DOMAIN_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What text domains are represented in the corpus? -->
* General

### Processing

<!-- {{PROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- How has the text data been processed -->

The original sentences from the UD treebank are written in varying orthographic norms. Prior to their inclusion into the Common Voice corpus,
the orthgoraphy was converted to the SIL San Miguel Tenango orthography ("ilv") using a rule-based automatic converter from the [py-elotl Python package](https://aclanthology.org/2025.americasnlp-1.5/), followed by some manual verification.

### Recommended post-processing

<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What should people do before they use the data, for example Unicode normalisation -->
None

## Get involved!

### Community links

<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->

### Discussions

<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->

### Contribute

<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->

* [Contribute voice recordings](https://commonvoice.mozilla.org/nhi/speak)
* [Contribute sentences](https://commonvoice.mozilla.org/nhi/write)
* [Validate recordings](https://commonvoice.mozilla.org/nhi/listen)
* [Review sentences](https://commonvoice.mozilla.org/nhi/review)

## Acknowledgements

### Datasheet authors

<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->
* Robert A. Pugh <robertp@mozillafoundation.org>

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

