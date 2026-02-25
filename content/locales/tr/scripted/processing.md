Except entries coming from individuals, we followed the following procedure for bulk additions to the text-corpus:

- Extraction using Common Voice rules (e.g. 14 words)
- Using Google Sheets to create conversational sentences in volunteer groups
- Every entry has been check twice by the datasheet author, then at least one person checked it again, fully.
- Wikipedia data extracted using the [cv-sentence-extractor](https://github.com/common-voice/cv-sentence-extractor) has been done through a [long and carefull process](https://github.com/common-voice/cv-sentence-extractor/pull/185) to keep the corpus quality high. We don't expect more than 2.5% error rate in these sentences, and most will be based on the bad grammer in originals, which we could not correct at that time due to the random nature of the algorithm.

Please note that Turkish in Common Voice does not have a special language based validator, it uses the defaults.
