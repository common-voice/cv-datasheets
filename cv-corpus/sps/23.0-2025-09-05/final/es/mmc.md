# *Jñatjo* &mdash; Michoacán Mazahua (`mmc`)
Esta ficha técnica corresponde a la versión 1.0 del conjunto de datos *Spontaneous Speech* (habla espontánea) de Mozilla Common Voice 
para Michoacán Mazahua (`mmc`). El conjunto de datos contiene 876 representando 12 horas de grabaciones 
(12 horas validadas) de 12 hablantes.

## Idioma
La variante de Michoacán de mazahua o ‘Jñatjo’ es hablada en el norte Michoacán, México.  Las tenencias donde se habla esta variante son Crescencio Morales, Boca de la Cañada, Rincón de San Mateo, El Tigre, La Barranca, La Dieta, La Fundición, Macho de Agua y Río de Guadalupe. Pertenece a la familia lingüística otomangue, subrama otopameana-central.
Los datos obtenidos para este corpus de datos provienen de la tenencia de Crescencio Morales, ubicado en el municipio de Zitácuaro.
<!-- {{LANGUAGE_DESCRIPTION}} -->
<!-- Proporciona una breve descripción (1-2 párrafos) de tu lengua -->

<!--[No proporcionado]
## Información demográfica
El conjunto de datos incluye la siguiente distribución de edad y género.
[No proporcionado]-->
<!-- Puedes obtener gran parte de la información de esta sección desde [https://analyzer.cv-toolbox.web.tr/browse](https://analyzer.cv-toolbox.web.tr/browse) -->

<!--[No proporcionado]
### Género
Información de género autodeclarada; la frecuencia se refiere al número de fragmentos anotados con este género.
[No proporcionado]-->
<!-- {{GENDER_TABLE}} -->
<!-- @ GENERADO AUTOMÁTICAMENTE @ -->
<!-- | Género              | Frecuencia |
|---------------------|------------|
| masculino           | ? |
| no declarado        | ? |
| femenino            | ? |
-->

<!--[No proporcionado]
### Edad
Información de edad autodeclarada; la frecuencia se refiere al número de fragmentos anotados con esta franja etaria.
[No proporcionado]-->
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
| Train | 429 |
| Dev | 270 |
<!-- @ GENERADO AUTOMÁTICAMENTE @ -->

## Transcripciones
* Prompts: `195`
* Duration: `40574520[ms]`
* Avg. Transcription Len: `330`
* Avg. Duration: `46.32[s]`
* Valid Duration: `40574.52[s]`
* Total hours: `11.27[h]`
* Valid hours: `11.27[h]`
<!-- {{TRANSCRIPTIONS_DESCRIPTION}} -->
<!-- Una descripción del sistema de transcripción utilizado -->

### Sistema de escritura
El Mazahua de Michoacán se escribe utilizando alfabeto latino.
Ha habido múltiples propuestas de alfabeto para el Mazahua y sus dos variantes, la del Estado de México (Jñajtro) y la de Michoacán (Jñatjo), las cuales no toman en cuenta los tonos de las palabras habiendo mucha confusión durante la escritura, los tonos de la lengua son sistémicos ya que pueden contrastar funciones gramaticales (posesión, demostrativos, definitud, tiempo, aspecto y modo) y determinar el significado de las palabras 

Por ejemplo: 	
* ‘kjǚjnü’ metate – ‘kjǜjnü’ maíz 
* ‘‘ë̀dyi’ llevar animales – ‘ ‘ë̂dyi’ medir
<!-- {{WRITING_SYSTEM_DESCRIPTION}} -->
<!-- @ OPCIONAL @ -->
<!-- Una descripción del sistema (o sistemas) de escritura usado en el corpus de texto -->

#### Tabla de símbolos
Para esta propuesta de alfabeto, se retomará el sugerido por la Universidad Intercultural del Estado de México expuesto en la tesis de Gloria Vargas Bernal (2013). Se tiene la visión de hacerlo más específico en el caso de los tonos.


##### Consonantes
El Mazahua de Michoacán posee un inventario consonántico de 51 segmentos fonológicos. Hay oclusivas, implosivas, fricativas, africadas, nasales, aproximantes, laterales, vibrantes y glotales. También en estos segmentos hay realización de articulaciones secundarias como: glotalización, preaspiración, aspiración, labialización, prenasalización.
En la propuesta de alfabeto para esta variante, los sonidos labializados [w] se consideran como una realización de la vocal cerrada [u], obteniendo 47 grafías.

###### Consonantes simples
b, m, t, s, z, ts, ch, n, l, r, rr, x, zh, ñ, y, k, g, j, ‘ (salto glotal)

###### Articulaciones secundarias
- Glotalización: b’, p’, t’, d’, s’, ts’, ch’, s’, dy, k’

- Preaspiración: jm, jn, jñ, jdy

- Aspiración : pj, tj, sj, tsj, chj, kj 

- Labialización: En esta articulación secundaria, se hace énfasis en el uso de la consonante seguido de una vocal cerrada ‘u’. 
ku, ngu

- Prenasalización: mb, nd, ndz, ndzh, ng, ngu

##### Vocales
El mazahua tiene inventario de 15 vocales: 9 orales y 6 nasales.

###### Vocales orales
Se usa diéresis en la vocal para indicar la abertura. Los símbolos en corchetes corresponden a los sonidos presentes en Alfabeto Fonético Internacional (AFI).
- a = [a]
- ä = [ə]
- e = [e]
- ë = [ɛ]
- i = [i]
- o = [o]
- ö = [ɔ]
- u = [u]
- ü = [ɨ]

###### Vocales nasales
Se usa diacrítico macron en la vocal para indicar nasalidad.

- ā = [ã]
- ē = [ẽ]
- ī = [ ĩ ]
- ō = [õ]
- ū = [ũ]
- ǖ = [ ɨ̃ ] 

En Unicode, “ǖ” tiene código 01D6 en minúscula y 01D5 en mayúscula.

##### Tonos (diacríticos en Unicode)
El mazahua posee cuatro tonos: alto, bajo, ascendente y descendente. Los diacríticos se escriben encima de la primera vocal. 

* Tono alto: [ ́ ], 02CB 
* Tono bajo: [ ̀ ], 02CB
* Tono descendente: [ ̂  ], 02C6
* Tono ascendente: [ ̌  ], 02C6

Ejemplo: 
* *ndzíncho* – nueve
* *jmū̀ru* – huevo 
* *pjâd'ül* – caballo  
* *jyö̌rga* – lagartija  

<!-- {{ALPHABET_TABLE}} -->
<!-- @ OPCIONAL @ -->
<!-- Si el sistema de escritura es alfabético, puedes incluir aquí el alfabeto válido -->

<!--[No proporcionado]
#### Etiquetas extralingüísticas
[No proporcionado]-->

### Ejemplos

#### Preguntas
1) *Pjéko gí kjâ'a nú ts'índajme k'a gí sôdya?* - "¿Qué haces en tu tiempo libre?"
2) *Jânge gá dyä̀tji nú sopa k'âraxü?* - "¿Cómo se hace la sopa de trigo verde?"
3) *Pjéko má 'úb'i kuâjtp'ü 'ó ngéjo añimále?* - "¿Qué animales ponen en los bordados?"
4) *Jânge gá dyä̀t'äji nú b'ë̌'ë?* - "¿Cómo hacen el tejido?"
5) *Pjéko má jñôna dyà mí né'e má kjâ'a mí ts'íjke?* - "¿Qué comida no te gustaba cuando eras niño/niña?"

A continuación se muestra una selección aleatoria de las preguntas usadas en el corpus.
```
Pjéko má manualidad gí néʼe rí dyä̀tʼä?
Jângé gí juǎjnuji nú ngálo para nú áñima? Jânge jéʼe gá kjâʼa jênge kʼo rá sóʼo ná juǎjnuji?
Pjéko gi ka ká ri mběñe kó má sí porta ts'i?
B'ǘb'ü ná jñâtjo o náñyakímü gí né'e pjéko gi ñé'e?
Jânge ga jóküji nú níts'imi mà sǔ'p'a?
```
<!-- {{QUESTIONS_SAMPLE}} -->

#### Respuestas
1) Má rá tûguro rí né'e rá, rá resucitágö k'a nú cuerpo de ná pjántëjë - "Quiero resucitar en el cuerpo de un venado"
2) Má dyá gó áñima m'a 'í sump'a 'ä̀tjä yó tjö́mech'i k'o ngéjo ts'áka të́'ë, xíji tjö́mech'i kjuá'a - "En Día de Muertos, nosotros hacemos pan con forma de persona, también pan de conejo"
3) À jñíñi mí b'ǚb'ü ná, ná ndíxu ñe ná b'ë̌zo yá mí xîrabi mí sìpji ná xútǐ'i - "En el pueblo, había una mujer y un hombre que tenían una niña pequeña"
4) Rá, rá, rí né'egö rá kjâ'a nú pjántëjë - "A mí me gustaría ser un venado"
5) Nú ndíxu mí kjë́jmé à k'a ngǔm'ü mí 'ä̀t'ä jñôna mí pà'a k'a ndáreje pa pédye b'íjtu - "La mujer salió de la casa, antes de calentar la comida y fue al río a lavar la ropa"

A continuación se muestra una selección aleatoria de respuestas transcritas del corpus.
```
Yó të́'ë kja íjñíni mí pèdyeji mí jíngua porque mí 'ṑjtjo pjéko k'o rá sîji, m'ájmí b'ëpjü mbèpji ná jó'o dyá mi kjṑtji'i ná jó'o y pus... angezi mí jö̌rü tòpjü para que rá juîñiji yó ndíxuji, yó tǐji, yó nána, yó tá'a ngéko ó têndzagö yó b'ëzo ngéko nú mbèdyeji primero para que rá mí pòji à Bṓndo para que rá jö̌rüji mbépji k'a jângo rá tôji ná jó'o para que sô'o rá 'íjñíji ná jó'o k'o yú pjamilia para que rá tjômaji'i nú bíjtu yó mbójkuaji k'a mí kjèzheji
Rí né'e rá xôrügö k'o dyá rí pâ'a rá mâb'ügö kjo rá jíts'i rá xôrü. rá xôrü ná ndé rá jíts'i k'o nú téxe ná mbǘb'ü ngéko rá xôrü nú májyâra juéch'i rá 'ät' m'á rá jìts'ibi 'ä́rä mí mbéjkue nú m'á dyá rá xôrgü m'a ó rí né'e ra xôrgü ts'ak'a k'o dyá rí pâra eh... rá... rá xôrü ts'ák'a m'á pjéko rí mā̀'mā m'a rí jë́ts'i k'o pára angezi k'o dyá í pjë́ch'k'o b'ü m'á rá xôrü ná pǔnk'ü
Àjníni k'a índzǔmü rí síji ngôñi, ñejo ndë̌chü go k'âra ñéjo ch'édyo
Ná pá'a má yá mêzhe, mí b'ǚb'ü dyä̀jä tǐ'i k'o mí b'ǚb'ü ó jä̀tja, nájnú jä̀'tja dyà mí kjâ'a ná jó'o míjmi sä... sä̀t'ä, mí 'ä̀mbä k'o yó kjä̀tji rá gó sâgü ná pá'a o mé'b'i, gó mé'b'i ndízik'o xípji, xí k'a o ndzhôji. Nú k'a rí sā̂ch'ok'ü má... rí má m'á s'í' nú... nú este... nú kúch'i k'a b'ǚb'ü kja mū̀'ū gá s'ídyi mbé rá... rá pô'b'ü rá má jânk'o rá tö̌mbe kja s'íb'i, nújka kjâ'a kja nú tǐ'i kja gú ndzhûgü yá 'ä̀rä ná jó'o gó zǘtü kja nú ngǔm'ü k'a gó ts'á'a gó má... gó má... ts'ǘkjü  ngûxt'i ndízik'o kja nú ndù... kja ná ndùjme rú mé'b'i, rú mé'b'i, k'a të́jë má yá gó xôm'a kja ná má mé'b'i pjéko rá kjâbi yá... ngó rá 'ö́b'übi es... b'ǚb'ü ná pǔnk'ü este... 'ùb'i yó ná só'o gá kja, kja të̌jë rá zàgübi, yá rá jókò ná rí kjâbi, rä́k'ä nú ts'ábi gó... gó ndú... gó ndú né'e ná má'a gá jês'e kja ró zà'a yá nú ngúxti kja tùnüjnubi gó ñó'o yó nú b'íjtu má yá gó kö̌gü tá xûm'a ró zä̀t'ä este... k'o mbé k'o mí ndzhôd'ü kja të̌jë Kjo rú zä̀tä o yá gó míjmi nú kjâ'a, kja nú nguá'a nú zá'a gó mí b'ǚb'ü, nú k'a gó ts'á gó k'ǘ'ü nú tujm'ü kja mí b'ǚb'ü kja mí tùjpjübi nú ngûxti kja ná ndôge, ná ndôge gá má hùmü nú k'o yó mbé k'o 'íxchimi pǘnü ná, ná pǔnk'ü mério kja pa yó jñíñi gó sǔb'i gó b'ǚ... b'ǚb'ü angezeji yá má gú tsǜri kja hùm'ü gú b'ǚb'ü k'o yó mbé 'ùnü pjéko mí bûnk'o b'ǚb'übi chôtübi ná pǔnk'ü yó... k'o yó sǔmpjü yó mbé'e, kja nú ndzhúgübi à kja nú ngǔm'ü ngéko angezebi dyá, dyá b'ǚbi ná jó'o ya í síji ná pǔnk'ü tòpjü k'o gó, k'o gó sôpk'uji k'o yó mbék'o gó b'ǚb'ü, ngéko angezebi kja ná jó'o núkja nú jä̀t'ä k'a yó, dyä̀jkja 'é'e kjo xíji dyá
Rí m'ângó ná té k'a jízhi pjéko pë́jch'i, este... ts'ómbeñe gá té dyàndéjo té yó m'ârá k'o ó p'âra, mê'erá jízhi ngéko rá mbàra koyáji yó té porque m'â'rá 'ö́jtk'ä kja ró té m'adyàrá jízhi pues si rá ndézhi para dyákja rá xôrü má'a ño'té. Mí na ts'ómbeñe ngéko gü ná jízhikö k'o pá'a
```
<!-- {{TRANSCRIPTIONS_SAMPLE}} -->

### Posprocesamiento recomendado
El sistema de escritura propuesto para esta variante de mazahua queda abierto a futuras modificaciones y comentarios.
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
* [Traductores de Common Voice en Pontoon](https://pontoon.mozilla.org/mmc/common-voice/contributors/)
<!-- {{COMMUNITY_LINKS_LIST}} -->
<!-- @ OPCIONAL @ -->
<!-- Enlaces a chats o foros comunitarios -->

<!--[No proporcionado]
### Discusiones
[No proporcionado]-->
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
- Colectivo 'Jñatjo Ndixu', Santa Martha del Sur, Coyoacán, Ciudad de México.
- Maestros Silverio Benítez García y Orlando Blanco y alumna María del Carmen de Jesús Guzmán, integrantes de Puntos de Innovación, Libertad, Arte, Educación y Saberes (PILARES), Ciudad de México.
- Coordinaciones de Posgrado y Licenciatura de la Universidad Autónoma Metropolitana, Unidad Iztapalapa. Gracias por todo el apoyo recibido y por habernos brindado el Laboratorio de Lingüística (D110) para llevar a cabo nuestras grabaciones.
- Mtro. Edgar Alberto Madrid Servin, coordinador y docente de la Licenciatura en Lingüística y Dr. Lucio Armando Mora-Bustos, docente e investigador de Lingüística, ambos de la Universidad Autónoma Metropolitana, Unidad Iztapalapa. Estamos totalmente agradecidos por su orientación y comentarios.

### Autores de la ficha técnica
* Rosario de Fátima Álvarez García &lt;fatimaalvarezgr96@gmail.com&gt;
* Juan Castro Gallardo &lt;jcgallardho@gmail.com&gt;
* Lorena Abigail Benítez Cruz &lt;abigailbenitez66@gmail.com&gt;
<!-- {{DATASHEET_AUTHORS_LIST}} -->
<!-- Una lista en el formato: Su Nombre <email@email.com> -->

<!--[No proporcionado]
### Criterios de citación
[No proporcionado]-->
<!-- {{CITATION_DESCRIPTION}} -->
<!-- @ OPCIONAL @ -->
<!-- Si publicó un artículo y desea que lo citen, puede incluir el BiBTeX aquí -->

### Financiamiento
Este proyecto recibió financiamiento del *Open Multilingual Speech Fund* gestionado por Mozilla Common Voice.
<!-- {{FUNDING_DESCRIPTION}} -->
<!-- @ OPCIONAL @ -->
<!-- Si recibió financiamiento, puede incluir el reconocimiento aquí -->

## Licencia
Este conjunto de datos se publica bajo la licencia [Creative Commons Zero (CC-0)](https://creativecommons.org/public-domain/cc0/). Al descargar estos datos
usted acepta no determinar la identidad de los hablantes en el conjunto de datos.
