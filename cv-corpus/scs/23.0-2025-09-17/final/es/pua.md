# *[Western Highland Purepecha]* &mdash; Western Highland Purepecha (pua)
Esta ficha técnica corresponde a la versión 23.0 del conjunto de datos de voz guiada de Mozilla Common Voice 
para Western Highland Purepecha (pua). El conjunto de datos contiene 8180 clips reprentando 12 horas de grabaciones (11 horas
validadas) de 9 hablantes.

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
Información de género autodeclarada, el porcentaje se refiere al número de clips anotados con este género.
| Género | Porcentaje |
|-|-|
| Undefined | 72.0% |
| Female Feminine | 28.0% |
<!-- {{GENDER_TABLE}} -->
<!-- @ GENERADO AUTOMÁTICAMENTE @ -->
<!-- | Género              | Frecuencia |
|---------------------|------------|
| masculino           | ? |
| no declarado        | ? |
| femenino            | ? | -->

### Edad
Información de edad autodeclarada, el porcentaje se refiere al número de clips anotados con este rango de edad.
| Rango de edad | Porcentaje |
|-|-|
| Undefined | 14.0% |
| Twenties | 55.0% |
| Thirties | 31.0% |
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

## Partición de datos para modelado
Las particiones de datos oficiales para el modelado de esta lengua son las siguientes. De los clips validados, 29.13% están incluidos en las particiones.

 | Partición | Cuenta |
|-|-|
| Train | 1153 |
| Test | 547 |
| Dev | 495 |

## Corpus de texto
El corpus textual contiene `2200` oraciones, de las cuales `2201` están validadas, `-1` están invalidadas y `1` son reportadas.
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
Juchiti pirentsï nirasti kʼeri iretarhu miyuni.
¿Chiini ampe xani jorhentperanhasïni?
Ima chʼawaka énka Pedru pʼikuka xarakata pʼikunhasïnti.
Xarhinichani kanekwa tsʼïrakwarhisïnti.
Énka warhiti ma ikiani jawaka no jarhasti para itsukwa intskuni charhaku jempani.
```

*Muestras automáticas aleatorias*

```
Juchiti pirentsï nirasti kʼeri iretarhu miyuni.
¿Chiini ampe xani jorhentperanhasïni?
Ima chʼawaka énka Pedru pʼikuka xarakata pʼikunhasïnti.
Xarhinichani kanekwa tsʼïrakwarhisïnti.
Énka warhiti ma ikiani jawaka no jarhasti para itsukwa intskuni charhaku jempani.
```

*Muestras automáticas aleatorias*

```
Juchiti pirentsï nirasti kʼeri iretarhu miyuni.
¿Chiini ampe xani jorhentperanhasïni?
Ima chʼawaka énka Pedru pʼikuka xarakata pʼikunhasïnti.
Xarhinichani kanekwa tsʼïrakwarhisïnti.
Énka warhiti ma ikiani jawaka no jarhasti para itsukwa intskuni charhaku jempani.
```

*Muestras automáticas aleatorias*

```
Juchiti pirentsï nirasti kʼeri iretarhu miyuni.
¿Chiini ampe xani jorhentperanhasïni?
Ima chʼawaka énka Pedru pʼikuka xarakata pʼikunhasïnti.
Xarhinichani kanekwa tsʼïrakwarhisïnti.
Énka warhiti ma ikiani jawaka no jarhasti para itsukwa intskuni charhaku jempani.
```
<!-- {{SENTENCES_SAMPLE}} -->

### Fuentes
<!-- {{SOURCES_LIST}} -->
<!-- @ OPCIONAL @ -->
<!-- Una lista de las fuentes de las oraciones, se puede limitar a las N principales -->

### Dominios textuales
| Dominio | Cuenta |
|-|-|
| Undefined | 8180 |
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
* [Traductores de Common Voice en Pontoon](https://pontoon.mozilla.org/pua/common-voice/contributors/)
<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPCIONAL @ -->
<!-- Enlaces a chats / foros de la comunidad -->

### Discusiones
<!-- {{DISCUSSION_LINKS_LIST}} -->
<!-- @ OPCIONAL @ -->
<!-- Puede incluirse cualquier enlace a discusiones, por ejemplo en Discourse, foros u otros blogs -->

### Contribuir
* [Hablar](https://commonvoice.mozilla.org/pua/speak)
* [Escribir](https://commonvoice.mozilla.org/pua/write)
* [Escuchar](https://commonvoice.mozilla.org/pua/listen)
* [Revisar](https://commonvoice.mozilla.org/pua/review)
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