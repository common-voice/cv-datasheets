# *Mixteco Yucuhiti* &mdash; Southwestern Tlaxiaco Mixtec (`meh`)
Esta ficha técnica corresponde a la versión 23.0 del conjunto de datos *Spontaneous Speech* (habla espontánea) de Mozilla Common Voice 
para Southwestern Tlaxiaco Mixtec (`meh`). El conjunto de datos contiene 1057 representando 11 horas de grabaciones 
(11 horas validadas) de 16 hablantes.

## Idioma
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Proporciona una breve descripción (1-2 párrafos) de tu lengua -->

## Información demográfica
El conjunto de datos incluye la siguiente distribución de edad y género.
<!-- Puedes obtener gran parte de la información de esta sección desde [https://analyzer.cv-toolbox.web.tr/browse](https://analyzer.cv-toolbox.web.tr/browse) -->

### Género
Información de género autodeclarada; la frecuencia se refiere al número de fragmentos anotados con este género.
<!-- {{GENDER_TABLE}} -->
<!-- @ GENERADO AUTOMÁTICAMENTE @ -->
<!-- | Género              | Frecuencia |
|---------------------|------------|
| masculino           | ? |
| no declarado        | ? |
| femenino            | ? | -->

### Edad
Información de edad autodeclarada; la frecuencia se refiere al número de fragmentos anotados con esta franja etaria.
<!-- {{AGE_TABLE}} -->
<!-- @ GENERADO AUTOMÁTICAMENTE @ -->
<!-- | Franja etaria  | Frecuencia |
|----------------|------------|
| adolescencia   | ? |
| veintes        | ? |
| treintas       | ? |
| cuarentas      | ? |
| cincuentas     | ? |
   ...si en tus datos aparecen otros rangos de edad, añade filas... -->

## Partición de datos para modelado



 | Partición | Cuenta |
|-|-|
| Train | 679 |
| Dev | 163 |


## Transcripciones

* Prompts: `120`
* Duration: `36567144[ms]`
* Avg. Transcription Len: `314`
* Avg. Duration: `34.59521665089877[s]`
* Valid Duration: `36197.496[s]`
* Total hours: `10.15754[h]`
* Valid hours: `10.05486[h]`

<!-- {{TRANSCRIPTIONS_DESCRIPTION}} -->
<!-- Una descripción del sistema de transcripción utilizado -->

### Sistema de escritura
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPCIONAL @ -->
<!-- Una descripción del sistema (o sistemas) de escritura usado en el corpus de texto -->

#### Tabla de símbolos
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPCIONAL @ -->
<!-- Si el sistema de escritura es alfabético, puedes incluir aquí el alfabeto válido -->

#### Etiquetas extralingüísticas

### Ejemplos

#### Preguntas
A continuación se muestra una selección aleatoria de las preguntas usadas en el corpus.

```
Á a nè’yá nú pelíkúlà, pelíkúlà kuítɨ́ axín nà inka kàa a kéne nùù televìsión’ tù’un maá nú
Nénú’ kúvi nùù né’ya nú pelíkúlà jin na inkà da à kéne nùù kàa?
Néiin kúvi à màá va’á nùù nú nùù súkuá’a nú?
Né neyu kúvi à víjí túní’ sà’a
Nàsa koo jiñú’ú danú nùù ñɨvɨ’ ñá’nú ñuu’ nú?
```

<!-- {{QUESTIONS_SAMPLE}} -->

#### Respuestas
A continuación se muestra una selección aleatoria de respuestas transcritas del corpus.

```
u... a maa xinañu'u vi tyi tyityi'yo ñe'e o uh ve de tun tyi'yo ñe'e o jen... ɨjɨn... nee niko jen nakoo o na'a o da vi a sa'a o xita jia'an nuu kata vi ñe'e. Yukuan kene kuli ji je sa sa'a o xita. 
A katie'e daja vi yaa a katyi'i xini jie'e, ka'an majan.
Iyo yuku kue'i sa'a nu ñuu ni ya'a. Ñivɨ ña'nu jen nkatyi daja nuu dani a iin xeen sa'a da yuku yukuan jen suu ntuvi ke'i dani majan a saa naa axin axin ntuvi jityi. Ke'i dani majan de sikitɨ dani majan jen kutyi dani majan, ko'o dani majan, tyi kue'i da yuku kua ita tunaa, tanaa, ita na'nu jen ntuvi nkuvi nani sa'a o jin. Iyo inka ka ita, ka'an daja ita nikɨn ka'an daja majan, suni kue'i, suni nsakuvi sikɨ majan. Iyo inka ka'an dani tyi'lo yuku suu suni a, xeen yuku yukuan va ntuvi a nani sa'a dani jin da yuku yukuan tyi, kumi naskuita ni sa va. Ntuvi nano'o dani. Iyo jo suni detun a tyiji yuku ko'on jen iyo i'yo jen da i'yɨ yukuan jen suni iyo i'yɨ sa kasun on tyi suni sa'a xeen jin yo axin ka'ni jin yo, suvi ni vi da yuku ini ni a iyo nuu nee dani ya'a a xeen jen.
Sa nkiji iin ñu'un taan maa ni'i jen ñu'vi kuatee ni nsa'a tyi ntia'an kuni ni na kuvi a taan jen ntaan ma xinañu'un nini ni jen iin taan.
Suu a kuvi ni nuvi va'a nuu ñuu ni vi, da ityi jika jia'a Niji Nuu tyiyo tuni iyo jen... na'a kuatee ñu'un on ityi tyi iyo tuni ɨjɨn, nkuvi tyi ñakɨn daja... nsa'a kaji daja nuu ñu'un soma tan ña'a kivɨ jen ntuvi iyo vii ka ityi i... ntu sa'a va'a to'o majan jen vitan jen no'o dani jin jin ityi tyi... ɨjɨn... tikua'yɨ kuatee jen no'o da kaa, sa numii ki da axin sa iyo ki ñɨvɨ. Jia'an ki Nijnuu jen no'o tuni daja. Jika tyiyo sava nee kuvi u'vi yo a ñu'un ityi a ne'i iyo ityi yukuan.
```

<!-- {{TRANSCRIPTIONS_SAMPLE}} -->

### Posprocesamiento recomendado
<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPCIONAL @ -->
<!-- Qué deberían hacer los usuarios antes de emplear los datos, por ejemplo normalización Unicode o normalización de etiquetas extralingüísticas -->

### Campos
Cada fila de un archivo `tsv` representa un solo clip de audio, y contiene la siguiente información:

* `client_id` - UUID hasheado de cierto usuario
* `audio_id` - id numérico para archivo de audio
* `audio_file` - nombre del archivo de audio
* `duration_ms` - duración del audio en milisegundo
* `prompt_id` - id numérico para el prompt
* `prompt` - pregunta para el usuario
* `transcription` - transcripción de la respuesta al audio
* `votes` - número de personas quiene aprobaron cierta transcripción
* `age` - edad de los hablantes[^1]
* `gender` - genero de los hablantes[^1]
* `language` - nombre de la lengua
* `split` - para el modelado de datos, indica a qué subconjunto de datos pertenece este clip
* `char_per_sec` - cuántos caracteres de transcripción por segundo de audio.
* `quality_tags` - una evaluación automatizada del par transcripción-audio, separadas por `|`
   * `transcription-length` -  caracteres por segundo inferior a 3 caracteres por segundo
   * `speech-rate` - tasa de caracteres por segundo superior a 30 caracteres por segundo
   * `short-audio` - duración del audio inferior a 2 segundos
   * `long-audio` - duración del audio superior a 30 segundos

#### 
[^1]: Para una lista completa de opciones de edades, generos, y acéntos, ver la [especificación demográfica](https://github.com/common-voice/common-voice/blob/main/web/src/stores/demographics.ts). Esta será reportada únicamente si el hablante aceptó proporcionar dicha información.

## ¡Participa!

### Enlaces comunitarios

* [Traductores de Common Voice en Pontoon](https://pontoon.mozilla.org/meh/common-voice/contributors/)

<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPCIONAL @ -->
<!-- Enlaces a chats o foros comunitarios -->

### Discusiones
<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPCIONAL @ -->
<!-- Aquí se pueden incluir enlaces a discusiones, por ejemplo en Discourse u otros foros o blogs -->

### Contribuir
* [Contribuye con preguntas](https://commonvoice.mozilla.org/spontaneous-speech/beta/question)
* [Valida preguntas](https://commonvoice.mozilla.org/spontaneous-speech/beta/validate)
* [Responde preguntas](https://commonvoice.mozilla.org/spontaneous-speech/beta/prompts)
* [Transcribe grabaciones](https://commonvoice.mozilla.org/spontaneous-speech/beta/transcribe)
* [Valida transcripciones](https://commonvoice.mozilla.org/spontaneous-speech/beta/check-transcript)
<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Aquí puedes incluir enlaces sobre cómo contribuir al conjunto de datos -->

## Agradecimientos

### Autores de la ficha técnica
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- Una lista en el formato: Su Nombre <email@email.com> -->

### Criterios de citación
<!-- {{CITATION_DESCRIPTION}} -->
<!-- @ OPCIONAL @ -->
<!-- Si publicó un artículo y desea que lo citen, puede incluir el BiBTeX aquí -->

### Financiamiento
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPCIONAL @ -->
<!-- Si recibió financiamiento, puede incluir el reconocimiento aquí -->

## Licencia
Este conjunto de datos se publica bajo la licencia [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/). Al descargar estos datos
usted acepta no determinar la identidad de los hablantes en el conjunto de datos.