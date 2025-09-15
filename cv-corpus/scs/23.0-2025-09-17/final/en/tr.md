# _Türkçe_ &mdash; Turkish (`tr`)

This datasheet is for version 23.0 of the the Mozilla Common Voice _Scripted Speech_ dataset
for Turkish (`tr`). The dataset contains 134 hours of recorded
speech (129 hours validated) from 1790 speakers.

## Language

<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->

[Turkish](https://en.wikipedia.org/wiki/Turkish_language) is the most widely spoken language among Turkic languages and has around 100 million L1 speakers, which makes it the 18th most spoken language.
It is the national language of Turkey and one of two official languages of Cyprus, and secondary languages of some neighboring countries.
Many smaller groups in other countries exist, through migrations or communities from Ottoman era.
These smaller groups should usually be categorized as a variant.

### Variants

<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->

There are currently no variants defined for Common Voice Turkish dataset.
It is worth noting that, until now, this dataset focused on literary Turkish, often called "Turkish of Turkey".
There are also some L2 voices, mostly from immigrants coming into the country, but these can be categorized as "foreign accents".

## Demographic information

<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->

The dataset includes the following distribution of age and gender.
The demographics coverage based on clips metadata reaches `75%`, but when individual voices are taken into account, we can see that only `30%` of contributors provided the information.
Below, we give the automatically calculated values from the current dataset version, and unique-voice distributions from one previous version.
More statistics on demographic information calculated from previous version of the dataset [can be found here](https://analyzer.cv-toolbox.web.tr/examine/tr/22.0),
and change of major values throughout versions are [visualized here](https://metadata.cv-toolbox.web.tr/).
Note that:

- The secondary tables below are calculated using the `client_id` field and therefore cannot be exact.
- We are giving the gender bins as old categorization which was needed for cross-dataset comparisons.
- The difference between the two tables shows us that few female contributors, and people with higher age recorded more sentences than other groups.
- Currently the female/male voice ratio in the clips metadata is `0.76`.
  Therefore we keep our focus on gaining more female voices for the sake of diversity, as we previously did in the 2021-2022 campaign.

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

When we get the statistics from individual voices in validated set of the [previous version](https://analyzer.cv-toolbox.web.tr/examine/tr/22.0):

| Gender  | Frequency |
| ------- | --------: |
| male    |   25.18 % |
| female  |    5.20 % |
| other   |    0.00 % |
| no data |   69.61 % |

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

When we get the statistics from individual voices in validated set of the [previous version](https://analyzer.cv-toolbox.web.tr/examine/tr/22.0):

| Age band  | Frequency |
| --------- | --------: |
| teens     |    3.02 % |
| twenties  |   15.78 % |
| thirties  |    8.62 % |
| fourties  |    3.13 % |
| fifties   |    1.57 % |
| sixties   |    0.56 % |
| seventies |    0.11 % |
| eighties  |    0.11 % |
| nineties  |    0.00 % |

## Text corpus

<!-- {{TEXT_CORPUS_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- An overview of the text corpus, with information such as average length (in characters and words) of validated sentences. -->

Actual values of text corpus from the [previous version](https://analyzer.cv-toolbox.web.tr/examine/tr/22.0) (please check the text corpus tab) show that:

- Average `Characters/Sentence` of the whole corpus is `62.25`, but validated set average is `35.915`. Median values are `61` and `27` respectively.
- Average `Words/Sentence` of the whole corpus is `8.379`, but validated set average is `5.096`. Median values are `8` and `4` respectively.
- Shorter sentences in the older text corpus resulted in shorter recording durations, which is `3.8` seconds on the average (in the previous dataset).
  This value is increasing with each version, and we aim to reach `5 sec`, which is the ideal minimum of most SotA model architectures.

### Writing system

<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

Turkish uses an extended Latin alphabet.

#### Symbol table

<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->

Official Alphabet:

- Lowercase: `a b c ç d e f g ğ h ı i j k l m n o ö p r s ş t u ü v y z`
- Uppercase: `A B C Ç D E F G Ğ H I İ J K L M N O Ö P R S Ş T U Ü V Y Z`

Auxilary Characters (Arabic/Farsi loanwords): `â î û` `Â Î Û`

### Sample

There follows a randomly selected sample of five sentences from the corpus.

<!-- {{SENTENCES_SAMPLE}} -->

Note that this random selection might mostly be descriptive sentences coming from Wikipedia, because of their abundancy in the text-corpus.

### Sources

<!-- {{SOURCES_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- A list of sentence sources, can be curated to the top-N -->

The whole history of the text-corpora added throughout the years can be found [in this forum post (Turkish)](https://discourse.mozilla.org/t/turkce-kulliyat-cumleler/85899).
They mainly consist of:

- Pre 2021: [SETimes](https://en.wikipedia.org/wiki/Southeast_European_Times) => ~5k sentences (only these are recorded multiple times between 2018-2021, ~30h audio)
- 2021/10: Turkish proverbs => ~2.5k
- 2021-2022: Extracted sentences from books of Sabahattin Ali => ~18-19k sentences
- 2021-2024: Community generated conversational sentences => ~33k sentences
- 2023/11: Wikipedia random selection through [cv-sentence-extractor](https://github.com/common-voice/cv-sentence-extractor/pull/185) => 348.5k

Please note that:

- Not all of these sentences are recorded. The validated set only includes ~63k unique sentences.
- Until inclusion of Wikipedia sentences, we did not put a minimum limit to the sentence length.
  Especially after adding short conversational sentences, the average recording duration dropped.
  For this reason, although they are descriptive statements, we put a 3 word/20 char minimum limit to Wikipedia sentences.
- We currently have ~110k sentences extracted from public works of deceased authors, and 20k community generated sentences, waiting to be cross checked.

### Text domains

<!-- {{TEXT_DOMAIN_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What text domains are represented in the corpus? -->

Until this version, we did not work on specialized sentence domains, except entries coming from individuals and ~300 numbers we added.

### Processing

<!-- {{PROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- How has the text data been processed -->

Except entries coming from individuals, we followed the following procedure for bulk additions to the text-corpus:

- Extraction using Common Voice rules (e.g. 14 words)
- Using Google Sheets to create conversational sentences in volunteer groups
- Every entry has been check twice by the datasheet author, then at least one person checked it again, fully.
- Wikipedia data extracted using the [cv-sentence-extractor](https://github.com/common-voice/cv-sentence-extractor) has been done through a [long and carefull process](https://github.com/common-voice/cv-sentence-extractor/pull/185) to keep the corpus quality high. We don't expect more than 2.5% error rate in these sentences, and most will be based on the bad grammer in originals, which we could not correct at that time due to the random nature of the algorithm.

Please note that Turkish in Common Voice does not have a special language based validator, it uses the defaults.

### Recommended post-processing

<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What should people do before they use the data, for example Unicode normalisation -->

- Because there has been no sentence validation, there are some non-alphabet characters in the text corpus, especially coming from the [SETimes](https://en.wikipedia.org/wiki/Southeast_European_Times) corpus via proper names.
  You may like to remove these.
- Don't normalize extra characters used for Arabic/Farsi loanwords (â, î, û), normalizing them to a/ı/u will change the meaning and intonation.
- There are some proper names containing x and w, there are few and can be removed. We usually keep them because they are also used in minority languages of Turkey and in some proper names.

## Get involved

### Community links

<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->

Main Channels:

- [Telegram (IM / Support)](https://bit.ly/3basUbX)
- [Discourse (Documents)](https://discourse.mozilla.org/c/voice/tr/610)

Social media channels used during campaigns:

- [Facebook (Community & Support & Guides)](https://bit.ly/3C6oOgQ)
- [Youtube (Video Guides)](https://bit.ly/3FYsJi1)
- [X/Twitter](https://bit.ly/3jmq08a)
- [Instagram](https://bit.ly/3G0RUAB)
- [LinkedIn Page](https://bit.ly/3G0RUAB)

### Discussions

<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->

Most info can be found in Turkish language in the [Discourse Turkish sub-forum](https://discourse.mozilla.org/c/voice/tr/610).
Other discussions are in [Discourse main forum](https://discourse.mozilla.org/c/voice/239) in English. Current discussions are on the [Telegram group](https://bit.ly/3basUbX).

### Contribute

<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->

"How to contribute?", "What to avoid?", and similar topics for the newcomers can be found in the following forum post in Turkish:<br />
[The process, rights & wrongs and dataset improvement](https://discourse.mozilla.org/t/surec-dogrular-yanlislar-ve-veri-kumesinin-iyilestirilmesi/85938)

If you want to contribute, please first join the [Telegram group](https://bit.ly/3basUbX).

Our future plans include:

- Adding more conversational sentences, validating extracted 110k sentences, adding longer sentences.
- Providing domain based text-corpora
- Adding pre-defined variants and accents
- Adding validators
- Prepare a global campaign

You can find more information about how to participate in the Common Voice Project on the following page:  
[Community Participation Guidelines](https://github.com/common-voice/common-voice/blob/main/docs/COMMUNITIES.md)

## Acknowledgements

We extend our thanks to all contributors, without them there won't be any dataset.
We would also like to thank the Common Voice team for their help over the years.

### Datasheet authors

<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->

Bülent Özden <bulentozden2007@gmail.com>

<!-- ### Citation guidelines -->

<!-- {{CITATION_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you published a paper and would like people to cite it, you can include the BiBTeX here -->

<!-- ### Funding -->

<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->

## Licence

This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.
