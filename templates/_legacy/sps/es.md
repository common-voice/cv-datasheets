# *{{NATIVE_NAME}}* &mdash; {{ENGLISH_NAME}} (`{{LOCALE}}`)

Esta ficha técnica corresponde a la versión {{VERSION}} del conjunto de datos *Spontaneous Speech* (habla espontánea) de Mozilla Common Voice 
para {{ENGLISH_NAME}} (`{{LOCALE}}`). El conjunto de datos contiene {{CLIPS}} representando {{HOURS_RECORDED}} horas de grabaciones 
({{HOURS_VALIDATED}} horas validadas) de {{SPEAKERS}} hablantes.

## Idioma

<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Proporciona una breve descripción (1-2 párrafos) de tu lengua -->

## Información demográfica

Por el momento no está disponible la información demográfica para habla espontánea. Estamos trabajando en ello y esperamos que sea 
disponible en el próximo lanzamiento.

<!-- Puedes obtener gran parte de la información de esta sección desde [https://analyzer.cv-toolbox.web.tr/browse](https://analyzer.cv-toolbox.web.tr/browse) -->
<!--
El conjunto de datos incluye la siguiente distribución de edad y género.

### Género

Información de género autodeclarada; la frecuencia se refiere al número de fragmentos anotados con este género.
-->
<!-- {{GENDER_TABLE}} -->
<!-- @ GENERADO AUTOMÁTICAMENTE @ -->
<!-- 
| Género              | Frecuencia |
|---------------------|------------|
| masculino           | ? |
| no declarado        | ? |
| femenino            | ? |
-->
<!--
### Edad

Información de edad autodeclarada; la frecuencia se refiere al número de fragmentos anotados con esta franja etaria.
-->
<!-- {{AGE_TABLE}} -->
<!-- @ GENERADO AUTOMÁTICAMENTE @ -->
<!-- 
| Franja etaria  | Frecuencia |
|----------------|------------|
| adolescencia   | ? |
| veintes        | ? |
| treintas       | ? |
| cuarentas      | ? |
| cincuentas     | ? |
   ...si en tus datos aparecen otros rangos de edad, añade filas...
-->

## Partición de datos para modelado

<!-- @ GENERADO AUTOMÁTICAMENTE @ -->

## Transcripciones

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

<!-- {{QUESTIONS_SAMPLE}} -->

#### Respuestas

A continuación se muestra una selección aleatoria de respuestas transcritas del corpus.

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

<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPCIONAL @ -->
<!-- Enlaces a chats o foros comunitarios -->

### Discusiones

<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPCIONAL @ -->
<!-- Aquí se pueden incluir enlaces a discusiones, por ejemplo en Discourse u otros foros o blogs -->

### Contribuir

<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Aquí puedes incluir enlaces sobre cómo contribuir al conjunto de datos -->

* [Contribuye con preguntas](https://commonvoice.mozilla.org/spontaneous-speech/beta/question)
* [Valida preguntas](https://commonvoice.mozilla.org/spontaneous-speech/beta/validate)
* [Responde preguntas](https://commonvoice.mozilla.org/spontaneous-speech/beta/prompts)
* [Transcribe grabaciones](https://commonvoice.mozilla.org/spontaneous-speech/beta/transcribe)
* [Valida transcripciones](https://commonvoice.mozilla.org/spontaneous-speech/beta/check-transcript)

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
