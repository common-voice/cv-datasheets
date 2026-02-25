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
