# *[Dameli]* &mdash; Dameli (`dml`)
This datasheet is for version 23.0 of the the Mozilla Common Voice *Scripted Speech* dataset 
for Dameli (`dml`). The dataset contains 11 hours of recorded
speech (11 hours validated) from 5 speakers.

## Language
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Provide a brief (1-2 paragraph) description of your language -->

Dameli is one of the most vulnerable languages of Pakistan. The language is spoken in a few remote villages, Asper, Dondidari, Ponagram and Shintari and the surrounding hamlets in the side valley called Damel in northern mountainous area of district Chitral of Khyber Pakhtunkhwa province. This vulnerability becomes more critical because of the community’s fewer numbers of speakers (about 6500 in total) In UNESCO’S  Atlas of the world languages in Danger, Dameli is listed as “Severely endangered” (Elnazarov, 2010).The entry on Dameli was contributed by Hakim Elnazarov, and was based on information in Decker (1992). 

<!-- ### Variants -->
<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- Describe the variants (MCV variants) of your language -->

<!-- Original Answer: -->
<!-- The dataset represents a wide range of Dameli language usage across different domains. The collected material includes sentences and expressions from:  Economic life, Social interactions, Education, Agriculture and farming, Poetry and oral traditions, History and culture. These varieties ensure that the dataset captures the richness of the Dameli language, reflecting not only everyday communication but also specialized fields and traditional knowledge. -->

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

The corpus consists of 5,670 sentences in the Dameli language. The data was collected from multiple sources, including published books in Dameli, community-written materials, and newly created sentences designed to reflect everyday use of the language. The aim of compiling this corpus is to represent a wide range of topics such as social life, education, agriculture, economy, poetry, farming, and history. This balanced collection provides a valuable resource for linguistic analysis, documentation, and language technology development.

### Writing system
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- A description of the writing system (or writing systems) used in the text corpus -->

The Dameli corpus is written using the Arabic script (Perso-Arabic style), which is commonly used for many regional languages in Pakistan. The writing system has been adapted to represent Dameli sounds, with some additional diacritics and letters used where necessary to capture specific phonetic distinctions.

#### Symbol table
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPTIONAL @ -->
<!-- If the writing system is alphabetic, you can include the valid alphabet here -->

``` آ ا ب پ ت ٹ ث ج چ ڇ څ ح خ د ڈ ذ ر ڑ ز ڙ ژ س ش ݜ ص ض ط ظ ع غ ف ق ک گ ل م ن ݨ و ہ ھ ء ی ے```

### Sample
<!-- {{SENTENCES_SAMPLE}} -->
There follows a randomly selected sample of sentences from the corpus.
```
 ماں نم حیات درو ماں گرم ساں نم نعیلہ درو ائی دامن ایک مس آݜنتہ ینُم ما کُل آسپرہ درو دامن لے شُباں درو 
```

### Sources
<!-- {{SOURCES_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- A list of sentence sources, can be curated to the top-N -->

The text corpus was compiled from the following sources:  
* Published books in the Dameli language 
* Unpublished community manuscripts and notes 
* Folk stories, oral traditions, and poetry transcribed into written form 
* Newly created sentences for grammar and vocabulary coverage 
* Educational and social materials produced by local speakers  

### Text domains
<!-- {{TEXT_DOMAIN_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What text domains are represented in the corpus? -->

General, Agriculture and Food, Finance, Service and Retail, Healthcare, History, Law and Governmant, Media and Entertainment, Nature and Environment, Language Fundamentals (e.g. Digits, Letters, Money)

### Processing
<!-- {{PROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- How has the text data been processed -->

The collected texts were first gathered from books, manuscripts, and community contributions. Additional sentences were created to cover gaps in vocabulary and grammar. All materials were transcribed into a consistent format using the Arabic (Perso-Arabic) script adapted for Dameli. The data was then carefully reviewed and proofread to remove errors and ensure accuracy. Finally, the sentences were digitized, standardized, and compiled into a single corpus of 5,670 sentences for use in research and language development.

### Recommended post-processing
<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- What should people do before they use the data, for example Unicode normalisation -->

Users of this dataset may consider the following post-processing steps depending on their research goals:  
* Normalization: Ensure consistent spelling, especially where multiple variants of the same word exist. 
* Tokenization: Segment the text into words or morphemes for computational use. 
* POS tagging / annotation: Add part-of-speech or grammatical tags if the dataset will be used for linguistic or NLP applications. 
* Transliteration:  Convert the Arabic script into Latin script if required for cross-linguistic comparison. 
* Alignment: If paired with translations, align Dameli sentences with their equivalents in other languages for bilingual analysis.  

## Get involved!


### Community links
<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Links to community chats / fora -->

As internet access is limited in the Dameli Valley, most local communication takes place through community gatherings, cultural events, and village meeting. However, Dameli people living in cities and outside the valley stay connected online. They maintain a WhatsApp group called “Anjuman Taraqi Damyan Basha”, where members share poetry, cultural materials, news, and language-related resources. In this way, both offline and online platforms help keep the community connected and engaged in language preservation.

### Discussions
<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPTIONAL @ -->
<!-- Any links to discussions, for example on Discourse or other fora or blogs can be included here -->

There are no formal online forums or blogs for discussions related to the dataset. Instead, most of the discussion and coordination took place in the WhatsApp group “Anjuman Taraqi Damyan Basha”, where community members exchanged ideas, shared poetry, cultural materials, and contributed to decisions during the dataset creation process.

### Contribute
<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Here you can include links for how to contribute to the dataset -->



## Acknowledgements


### Datasheet authors
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- A list in the format of: Your Name <email@email.com> -->

Common Voice Community

### Funding
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPTIONAL @ -->
<!-- If you received any funding, you can include the acknowledgement here -->

This project was funded by the Common Voice Foundation, and we are deeply grateful for their support. These materials were then converted into individual sentences by Mr. Meesum Alam, whose guidance and leadership were instrumental in successfully completing the project. We extend our heartfelt thanks to the Common Voice Foundation for making this work possible, and special appreciation to Mr. Meesum Alam for his invaluable guidance and dedication throughout the project. 

## Licence
This dataset is released under the [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/) licence. By downloading this data
you agree to not determine the identity of speakers in the dataset.