
# Mozilla Common Voice: Kyrgyz (ky)

This document is a datasheet for the Mozilla Common Voice (MCV) dataset for the
Kyrgyz language, version `22.0-2025-06-25`.

The Kyrgyz language is a Turkic language and one of the two official languages
of Kyrgyzstan, the other being Russian. It is spoken by about 5 million people,
primarily in Kyrgyzstan, with smaller communities of speakers in neighboring
countries like China, Afghanistan, Kazakhstan, and Uzbekistan. Kyrgyz is a
member of the Kipchak branch of the Turkic language family and is written in a
Cyrillic alphabet.

## Clip & Sentence Statistics

This dataset contains a total of **38.12 validated hours** of speech from
**269** unique contributors.

| Type                | Count | Hours  |
| ------------------- | ----: | -----: |
| Validated Clips     | 30,670 |   38.12 |
| Invalidated Clips   | 5,677 |   7.64 |
| **Total Clips**     | 37,841 |   45.76 |

| Type                  |   Count |
| --------------------- | ------: |
| Validated Sentences   |   5,045 |
| Invalidated Sentences |     242 |
| **Total Sentences**   |     5,287 |

## Demographic Information

Demographic information is self-reported by contributors and may not be
representative of the entire speaker population.

### Age

| Age Group | Validated Clip Count |
| --------- | -------------------: |
| Twenties  |               20,747 |
| Teens     |                4,681 |
| Thirties  |                2,781 |
| Fourties  |                  341 |
| Fifties   |                    5 |
| **Total** |               28,555 |

### Gender

| Gender          | Validated Clip Count |
| --------------- | -------------------: |
| Male/Masculine  |               15,798 |
| Female/Feminine |               11,285 |
| **Total**       |               27,083 |

### Accent

The following accents were reported by contributors.

| Accent  | Count |
| ------- | ----: |
| Native  |    32 |
| Кандай  |     8 |
| Чүй     |     5 |

#### English Translation of Accents

| Reported Accent | Best-Effort English Translation/Explanation      |
| --------------- | -------------------------------------------------- |
| Native          | "Native"                                           |
| Кандай          | "How?" or "What kind?" (a Kyrgyz question word)    |
| Чүй             | Chüy / Chui (a region in northern Kyrgyzstan)      |

## Contributor Statistics

This table shows the distribution of clips recorded per contributor.

| Clips Recorded | Number of Contributors |
| -------------- | ---------------------: |
| 1-10           |                    133 |
| 11-50          |                     59 |
| 51-100         |                     16 |
| 101-500        |                     41 |
| >500           |                     20 |
| **Total**      |                    269 |

## Text Corpus

The text corpus is the collection of sentences used for recordings.

- **Total validated sentences:** 5,045
- **Sentences without a recording yet:** 19
- **Average clips per validated sentence:** 7.95
- **Average sentence length (tokens):** 6.7
- **Average sentence length (characters):** 46.7

### Corpus Sources

The sentences in this corpus were sourced from the following places:

| Source                                     | Description                                                |
| ------------------------------------------ | ---------------------------------------------------------- |
| My own, My own sentences, me                 | Sentences submitted directly by individual contributors.   |
| https://kaktus.kg/                         | Kaktus.media, a popular news website in Kyrgyzstan.        |
| https://new.bizdin.kg/.../makaldar.pdf      | A PDF document containing Kyrgyz proverbs (`makaldar`).    |
| https://www.azattyk.org/...                | Azattyk Media, the Kyrgyz service of RFE/RL.               |
| kloop                                      | Kloop, an independent media outlet in Kyrgyzstan.          |
| sentence-collector                         | Sentences from the Mozilla Common Voice Sentence Collector.|
| singleword-benchmark                       | A collection of single words for testing or benchmarking.  |
| Гугл                                       | "Google" (Cyrillic). Sourced via Google Search/Translate.  |
| Сүйло                                      | "Speak" (Kyrgyz). Likely a custom project name.            |

### Alphabet

The following characters are used in the text corpus:

```
  ! , - . ? А Б В Г Д Е Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Ы Э Ю Я а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я ё ң Ү ү ӊ Ө ө – — ” ⅛
```

### Sample Sentences

- Аянт ар кандай күч түзүмдөрүнүн кордондору менен тосмолонгон.
- Эми кыргызстандык эркектерден да сурашы мүмкүн.
- Мамкурулуш жеке өзү компанияны тандаган эмес, — деп билдирди ал.
- Анын айтымында, бул шайлоонун жыйынтыгына таасир эткен.
- Бизде аны багуу үчүн тиешелүү шарттар жок.

## Community Links

- **Common Voice Page:** `https://commonvoice.mozilla.org/ky`

> **Note:** This language is in **need of new sentences**. With only 19
> sentences left to record and an average of 7.95 clips per sentence, the
> dataset lacks the textual variety needed to train robust speech models. Please
> consider adding new public domain sentences via the Common Voice's [Write
> page](https://commonvoice.mozilla.org/ky/write)

## Fun Fact

The Kyrgyz language is the vehicle for the Epic of Manas, one of the world's
longest epic poems. Traditional storytellers, known as *manaschi*, can recite
vast portions of the poem from memory, with some versions exceeding half a
million lines. This oral tradition is a cornerstone of Kyrgyz culture and has
been recognized by UNESCO as an Intangible Cultural Heritage of Humanity.

Source: [UNESCO](https://ich.unesco.org/en/RL/kyrgyz-epic-trilogy-manas-semetey-seytek-00876)

## Datasheet Authors

This datasheet was semi-automatically generated by Ilnar Salimzianov <mdc.ilnar@gmail.com> based on corpus statistics.

***

Thank you for your interest in the Kyrgyz Common Voice dataset. To help this
dataset grow, please consider contributing to it today.

*   **Speak:** Record new voice clips from the sentence bank.
*   **Listen:** Help us validate the recordings of other contributors.
*   **Write:** Add new, public domain sentences to the text corpus.
*   **Review:** Help review the sentences that others have submitted.

**Visit [commonvoice.mozilla.org](https://commonvoice.mozilla.org/ky) to get
started!**
