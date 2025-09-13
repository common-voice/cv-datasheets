# *[Central Puebla Nahuatl]* &mdash; Central Puebla Nahuatl (ncx)
Esta ficha técnica corresponde a la versión 23.0 del conjunto de datos de voz guiada de Mozilla Common Voice 
para Central Puebla Nahuatl (ncx). El conjunto de datos contiene 12 horas de grabaciones (11 horas
validadas) de 41 hablantes.

## Idioma
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Proporcione una breve descripción (1-2 párrafos) de su idioma -->

### Variantes
<!-- {{VARIANT_DESCRIPTION}} -->
<!-- @ OPCIONAL @ -->
<!-- Describa las variantes (variantes MCV) de su idioma -->

## Información demográfica
El conjunto de datos incluye la siguiente distribución de edad y género.
<!-- puede obtener gran parte de la información en esta sección desde https://analyzer.cv-toolbox.web.tr/browse -->

### Género
Información de género autodeclarada, frecuencia se refiere al número de clips anotados con este género.
| Género | Frecuencia |
|-|-|
|  | 0.61 |
| Male Masculine | 0.01 |
| Female Feminine | 0.38 |
| Transgender | 0 |
| Non-Binary | 0 |
| Do Not Wish To Say | 0 |

<!-- {{GENDER_TABLE}} -->
<!-- @ GENERADO AUTOMÁTICAMENTE @ -->
<!-- | Género              | Frecuencia |
|---------------------|------------|
| masculino           | ? |
| no declarado        | ? |
| femenino            | ? | -->

### Edad
Información de edad autodeclarada, frecuencia se refiere al número de clips anotados con este rango de edad.
| Rango de edad | Frecuencia |
|-|-|
|  | 0.04 |
| Twenties | 0.15 |
| Thirties | 0.63 |
| Teens | 0 |
| Fourties | 0.17 |
| Fifties | 0 |
| Sixties | 0 |
| Seventies | 0 |
| Eighties | 0 |
| Nineties | 0 |

<!-- {{AGE_TABLE}} -->
<!-- @ GENERADO AUTOMÁTICAMENTE @ -->
<!-- | Rango de edad | Frecuencia |
|---------------|------------|
| adolescentes  | ? |
| veintes       | ? |
| treintas      | ? |
| cuarentas     | ? |
| cincuentas    | ? |
   ...si hay otros rangos de edad presentes en sus datos, añádalos como filas... -->

## Corpus de texto

* Reported sentences: `2`
* Validated sentences: `1518`
* Unvalidated sentences: `5`
* Clips: `9509`
* Users: `41`
* Avg duration: `4.457[s]`
* Valid duration: `38508.643[s]`
* Total hours: `11.77`
* Valid hours: `10.69`

<!-- {{TEXT_CORPUS_DESCRIPTION}} -->
<!-- @ OPCIONAL @ -->
<!-- Una descripción general del corpus de texto, con información como la longitud media (en caracteres y palabras) de las oraciones validadas. -->

### Sistema de escritura
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPCIONAL @ -->
<!-- Una descripción del sistema de escritura (o sistemas de escritura) utilizado en el corpus de texto -->

#### Tabla de símbolos
<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPCIONAL @ -->
<!-- Si el sistema de escritura es alfabético, puede incluir aquí el alfabeto válido -->

### Muestra
A continuación se muestran cinco oraciones seleccionadas aleatoriamente del corpus.

```
Kuali, momauitsotsin
Panpa ne amo nechyolkokoa nimotemakas mopatka.
¿Tikmati tiajkuis?
¿Nin chikiuitl non moaxka?
¿Kanin mochan?
```

<!-- {{SENTENCES_SAMPLE}} -->

### Fuentes
<!-- {{SOURCES_LIST}} -->
<!-- @ OPCIONAL @ -->
<!-- Una lista de las fuentes de las oraciones, se puede limitar a las N principales -->

### Dominios textuales

| Dominio | Cuenta |
|-|-|
|  | 2832 |
| Agriculture Food | 0 |
| Automotive Transport | 0 |
| Finance | 212 |
| Service Retail | 0 |
| General | 0 |
| Healthcare | 212 |
| History Law Government | 0 |
| Language Fundamentals | 2047 |
| Media Entertainment | 4700 |
| Nature Environment | 0 |
| News Current Affairs | 0 |
| Technology Robotics | 0 |

<!-- {{TEXT_DOMAIN_DESCRIPTION}} -->
<!-- @ OPCIONAL @ -->
<!-- ¿Qué dominios textuales están representados en el corpus? -->

### Procesamiento
<!-- {{PROCESSING_DESCRIPTION}} -->
<!-- @ OPCIONAL @ -->
<!-- Cómo se ha procesado la información textual -->

### Postprocesamiento recomendado
<!-- {{RECOMMENDED_POSTPROCESSING_DESCRIPTION}} -->
<!-- @ OPCIONAL @ -->
<!-- Qué debería hacerse antes de usar los datos, por ejemplo normalización de Unicode -->

### Campos
Cada fila de un archivo `tsv` representa un solo clip de audio, y contiene la siguiente información:

* `client_id` - UUID hasheado de cierto usuario
* `path` - ruta relativa al archivo de audio
* `text` - presunta transcripción del audio
* `up_votes` - número de personas que dijeron que el audio concordaba con el texto
* `down_votes` - número de personas que dijeron que el audio no concordaba con el texto
* `age` - edad de los hablantes[^1]
* `gender` - genero de los hablantes[^1]
* `accent` - acénto de los hablantes[^1]
* `segment` - si la oración pertenece a una porción personalizada de un dataset, será listada aquí

#### 
[^1]: Para una lista completa de opciones de edades, generos, y acéntos, ver la [especificación demográfica](https://github.com/common-voice/common-voice/blob/main/web/src/stores/demographics.ts). Esta será reportada únicamente si el hablante aceptó proporcionar dicha información.

## ¡Involúcrate!

### Enlaces comunitarios

* [Traductores de Common Voice en Pontoon](https://pontoon.mozilla.org/ncx/common-voice/contributors/)

<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPCIONAL @ -->
<!-- Enlaces a chats / foros de la comunidad -->

### Discusiones
<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPCIONAL @ -->
<!-- Puede incluirse cualquier enlace a discusiones, por ejemplo en Discourse, foros u otros blogs -->

### Contribuir

* [Hablar](https://commonvoice.mozilla.org/ncx/speak)
* [Escribir](https://commonvoice.mozilla.org/ncx/write)
* [Escuchar](https://commonvoice.mozilla.org/ncx/listen)
* [Revisar](https://commonvoice.mozilla.org/ncx/review)
<!-- {{CONTRIBUTE_LINKS_LIST}} -->
<!-- Aquí puede incluir enlaces sobre cómo contribuir al conjunto de datos -->

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