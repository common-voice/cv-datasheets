# cv-datasheets

## Community contribution

### Via a form

Scripted/Read Speech:

* (`en`) [MCV Datasheet: Scripted speech](https://docs.google.com/forms/d/e/1FAIpQLSc5QnmXd7MrfPd375RZ2YFh-Z3I_BGAf7e2cTD2h5xtWV8klQ/viewform?usp=dialog)
* (`es`) [MCV Datasheet: Habla leída](https://docs.google.com/forms/d/e/1FAIpQLSdk1IITzjpjrXKKLyHhzb5d0VoGvNNbscBywqJZf1BnBcf7Pw/viewform?usp=dialog)

Spontaneous Speech:

* (`en`) [MCV Datasheet: Spontaneous speech](https://docs.google.com/forms/d/e/1FAIpQLSfYI6CXK97boZ951gb3l2ysl77Hnyyi8qeSagXAlB1v32adqQ/viewform?usp=dialog)
* (`es`) [MCV Datasheet: Habla espontánea](https://docs.google.com/forms/d/e/1FAIpQLSdhHHYqgj1x6Cki8OYCHjVr3l3KmahBfcWvOgF70B6gV1jfbw/viewform?usp=dialog)

Submitting in a different language: If you would like to submit your datasheet in a language that is not English or Spanish, please feel free to get in contact with us [on Matrix](https://app.element.io/#/room/#common-voice:mozilla.org) (`#common-voice:mozilla.org`) to request a new template.
  
### Directly on GitHub

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
