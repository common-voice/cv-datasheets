# cv-datasheets

## Community contribution

* First clone this repository, or select your language code draft from the Spontaneous Speech (`sps`) or Scripted Speech (`scs`) directories:
  * [scs](https://github.com/common-voice/cv-datasheets/tree/main/cv-corpus/scs/23.0-2025-09-17/draft/).
  * [sps](https://github.com/common-voice/cv-datasheets/tree/main/cv-corpus/sps/23.0-2025-09-17/draft/).
* Then edit the draft to include all the information, there are some pointers and description in the comments 
* Either submit the editted `.md` file via a pull request or email the completed datasheet to commonvoice@mozilla.com

## Internal process

* The draft datasheets are generated from a template + the language metadata
* The draft datasheets are then given to community members to edit and adapt
* The editted datasheets that we receive back are added to the repository in the final/ directory 

# Scripts

**Usage:**

Generate the draft datasheets:

```
python3 generate-datasheet.py metadata/metadata.tsv metadata/datasheet-languages.tsv 23.0-2025-09-17 cv-corpus 
```
