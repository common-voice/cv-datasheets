# cv-datasheets

## Community contribution

* First clone this repository, or select your language code draft from [the drafts directory](https://github.com/common-voice/cv-datasheets/tree/main/cv-corpus-23.0-2025-09-17/draft/en).
* Then edit the draft to include all the information, there are some pointers and description in the comments 
* Either submit the editted `.md` file via a pull request or email the completed datasheet to commonvoice@mozilla.com

## Internal process

* The draft datasheets are generated from a template + the language metadata
* The draft datasheets are then given to community members to edit and adapt
* The editted datasheets that we receive back are added to the repository in the final/ directory 

# Scripts

**Usage:**

Generate the draft datasheets:

*Scripted:*
 
```
python3 generate-datasheet.py metadata/scs/metadata.json templates/scs/en.md cv-corpus/scs/23.0-2025-09-17/draft/en 
```

*Spontaneous:*

```
python3 generate-datasheet.py metadata/sps/metadata.json templates/sps/en.md cv-corpus/sps/23.0-2025-09-17/draft/en 
```
