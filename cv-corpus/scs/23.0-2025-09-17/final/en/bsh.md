# *کتہ وری* &mdash; Kateviri (`bsh`)
This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Kateviri (`bsh`). The dataset contains 11 hours of recorded
speech (11 hours validated) from 14 speakers.

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->

Kateviri is spoken in Afghanistan's province Noristan and in a few regions in Pakistan (Bumburait, Rumbur, Gobor). The number of speakers of Kateviri is around 40,000.

<!-- ### Variants -->
<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->

<!-- Original Answer: -->
<!-- The dataset primarily includes (kamveri)  kati as the main variety with limited samples from ashkun and prasun dialects these varieties are mutually  intelligible to some extent but have differences in pronunciation. -->

## Demographic information
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->
The dataset includes the following distribution of age and gender.

### Gender
<!-- {{GENDER_TABLE}} -->
<!-- @ AUTOMATICALLY GENERATED @ -->
<!-- | Gender | Frequency |
|--------|-----------|
| male, masculine | ? |
| undeclared | ? |
| female, feminine | ? | -->
Self-declared gender information, frequency refers to the number of clips annotated with this gender.

### Age
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
Self-declared age information, frequency refers to the number of clips annotated with this age band.

## Text corpus
<!-- {{TEXT_CORPUS_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- An overview of the text corpus, with information such as average length (in characters and words) of validated sentences. -->

The text corpus consists of transcriptions of spontaneous speech recorded from native Noristani speakers in natural conversations. The content includes everyday topics such as family, culture, daily routines, and local traditions. The dataset contains approximately 3000 to 5000  sentences and was collected primarily from speakers in  and Bumburet, Rumbur, and Gabor valleys (Pakistan).

### Writing system
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

Parso Arabic 

#### Symbol table
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->

```ا آ ب پ ت ٹ ث ج چ ڄ ح خ څ د ڈ ر ڑ ز ژ ڗ س ش ݜ ص ض ط ظ ع غ ف ق ک گ ݣ ل م ن ݨ ں ݩ و ہ ھ ٴ ی ے  ```

### Sample
<!-- {{SENTENCES_SAMPLE}} -->
There follows a randomly selected sample of sentences from the corpus.
```
 شلماچ پشول گوسہ تیو کور اسیش وݜ مع اسیشا پموکچی ائ  ایمو تہ کائ نہ ائ
```

### Sources
<!-- {{SOURCES_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- A list of sentence sources, can be curated to the top-N -->

Recorded spontaneous conversations

### Text domains
<!-- {{TEXT_DOMAIN_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What text domains are represented in the corpus? -->

General, Agriculture and Food, Media and Entertainment, Nature and Environment, Language Fundamentals (e.g. Digits, Letters, Money)

### Processing
<!-- {{PROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- How has the text data been processed -->

The recordings were collected from native kate  speakers, then manually transcribed. Background noise and silence were removed, and irrelevant parts were excluded. The text was checked for accuracy and aligned with the corresponding audio segments

### Recommended post-processing
<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What should people do before they use the data, for example Unicode normalisation -->

Yes. It is recommended to apply additional noise reduction, normalize audio levels, and perform a manual review of transcriptions for consistency. For advanced use, forced alignment and phonetic labeling can also improve the dataset quality

## Get involved!


### Community links
<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->

* [Facebook group](https://www.facebook.com/share/g/1Fw7UnLrtN/)

### Contribute
<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->


## Acknowledgements


### Datasheet authors
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->

* Nasir Mansoor <nasirmansorch@gmail.com>

### Citation guidelines
<!-- {{CITATION_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you published a paper and would like people to cite it, you can include the BiBTeX here -->

```bibtex
   @misc{noristani_dataset_2025,
   title        ={Noristani Spontaneous Speech Dataset},
   author       ={Arshad Nasir},
   year         ={2025},
   howpublished ={\url{https://commonvoice.mozilla.org}},
   note         ={Noristani language corpus for spontaneous speech}} 
```

### Funding
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->

Meesum Alam: meesum.alam12@gmail.com

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.