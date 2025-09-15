# *[Sindhi]* &mdash; Sindhi (`sd`)
This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Sindhi (`sd`). The dataset contains 35 hours of recorded
speech (0.4 hours validated) from 25 speakers.

## Language
Sindhi (سنڌي) is an Indo-Aryan language spoken mainly in Sindh, Pakistan, and also in India. It has millions of speakers, a rich literary history, and is written in both Perso-Arabic and Devanagari scripts.
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->
<!-- ### Variants -->
<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->
<!-- Original Answer: -->
<!-- Sindhi has several dialects, including Siroli (spoken in upper Sindh), Lari (spoken in lower Sindh), Thari (spoken in Tharparkar), and Kutchi (spoken in Kutch, India). The standard variety is based on the central Sindh dialect. -->

## Demographic information
The dataset includes the following distribution of age and gender.
<!-- You can get a lot of the information in this section from https://analyzer.cv-toolbox.web.tr/browse -->

### Gender
Self-declared gender information, percentage refers to the number of clips annotated with this gender.
| Gender | Pertentage |
|-|-|
| Undefined | 87.0% |
| Male Masculine | 13.0% |
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
| Undefined | 2.0% |
| Thirties | 13.0% |
| Fourties | 85.0% |
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
The Sindhi corpus consists of collected texts from newspapers, and social media. It contains more then one lacs sentences. The texts cover different domains, including literature, news, education, and everyday communication.
<!-- {{TEXT_CORPUS_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- An overview of the text corpus, with information such as average length (in characters and words) of validated sentences. -->

### Writing system
The Sindhi corpus is written in the Perso-Arabic script, which is the standard script used by Sindhi newspapers in Pakistan. It includes additional letters that represent Sindhi-specific sounds not found in standard Arabic.
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

#### Symbol table
The Sindhi Perso-Arabic script (used in newspapers) has 52 letters. Here is the full alphabet list separated by spaces:
```ا ب ٻ ڀ پ ت ٿ ٽ ٺ ث ج جه ڄ چ ڇ ح خ د ڌ ڏ ڊ ڍ ذ ر ڙ ڍ ز س ش ص ض ط ظ ع غ ف ڦ ق ڪ گ ڳ گه ڱ ل ڻ ن ڃ م و ء ه ة ي ئ```
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->

### Sample
There follows a randomly selected sample of sentences from the corpus.

```
ڳوٺ محمد ابراهيم سومرو ۾ پورهيت چاڪر سومرو جي گهر کي باهه لڳي وئي عوامي تحريڪ ضلعي صدر ايڊووڪيٽ نياز بھراڻي  قتل ٿيل امجد علي لاشاري جي والد عرس لاشاري احتجاج ڪيو ايس ايس پي سنگهار ملڪ جي وڪيل جي پونيئرن سان تعزيت قوم سميت واٽر ڪارپوريشن جي سمورن آفيسرن ۽ ملازمن کي مبارڪون
```

*Automatic random samples*

```
اهي هاڻي اسلام آباد سان ڇا ڪندا؟
هن پوڊ ڪاسٽ ذريعي
ڪيترين روايتن موجب علي جي مٿي مان وهندڙ رت سندس ڏاڙهيءَ جو رنگ ڪري رهيو هو
مسٽر هيئن پڻ جارجيا پئسفڪ جي ڊرامائي ڦيرڦار جو بندوبست ڪيو
رسول الله ﷺ جن کي هن طرح بيان ڪيو آهي
```
<!-- {{SENTENCES_SAMPLE}} -->

### Text domains
General, Media and Entertainment, News and Current Affairs
<!-- {{TEXT_DOMAIN_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What text domains are represented in the corpus? -->

### Processing
The corpus was created by collecting texts from different Sindhi newspapers. The articles were gathered, cleaned to remove formatting issues, and then organized into a structured dataset for analysis.
<!-- {{PROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- How has the text data been processed -->

### Recommended post-processing
It is recommended to clean the text for duplicate articles, normalize spellings, and remove unwanted symbols or formatting. Tokenization and sentence segmentation may also be useful for better analysis.
<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What should people do before they use the data, for example Unicode normalisation -->

## Get involved!

### Community links
* [Common Voice translators on Pontoon](https://pontoon.mozilla.org/sd/common-voice/contributors/)

### Contribute
<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->

## Acknowledgements

### Datasheet authors
Common Voice Community
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->

### Funding
This dataset was created with funding support from Mozilla. Special acknowledgments to Meesam Alam (meesum.alam12@gmail.com) for contributions and support.
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.