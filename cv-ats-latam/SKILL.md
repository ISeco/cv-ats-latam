---
name: "cv-ats-latam"
description: "Construye CVs profesionales en español para Chile y Latinoamérica, en formato Harvard y aptos para filtros ATS, a partir de la experiencia real de la persona (entrevista guiada, logros con impacto, DOCX + PDF verificados). Guarda la carrera completa en un CV maestro en Markdown y genera versiones adaptadas a cada oferta. Úsala siempre que alguien quiera crear, rehacer, mejorar o actualizar su currículum o CV, adaptarlo a una oferta de trabajo, comparta su \"CV maestro\", o pregunte por qué su CV no pasa los filtros, aunque no diga \"ATS\" ni \"Harvard\". También para recién egresados sin experiencia y para personas con trayectorias de muchos rubros distintos. No es para cartas de presentación, perfiles de LinkedIn ni búsqueda de ofertas."
---

# CV profesional ATS (Chile y Latinoamérica)

Esta skill hace una sola cosa: llevar a una persona desde "tengo mi experiencia desordenada en la cabeza" hasta CVs limpios que un ATS lee completos y en orden, y que un reclutador entiende en pocos segundos.

El orden de prioridades guía cada decisión:

1. **Verdad.** Nada inventado ni inflado. Un CV que pasa el filtro pero se cae en la entrevista no le sirve a nadie.
2. **Contenido.** Logros concretos en vez de funciones. Es lo que más diferencia un CV bueno de uno mediocre.
3. **Pertinencia.** Cada versión muestra lo que mejor respalda *ese* cargo, no todo lo que la persona ha hecho.
4. **Legibilidad para el ATS.** Texto simple, una columna, secciones estándar.
5. **Legibilidad para la persona y estética.** Escaneable en 10 segundos, formato Harvard sobrio, sin colores, íconos, fotos ni gráficos.

## Cómo está organizado el trabajo

Hay dos piezas distintas:

- **El CV maestro** (`CV maestro - Nombre Apellido.md`): el inventario completo de la carrera en Markdown. Tiene todos los trabajos, más logros de los que caben en una página, datos sueltos y perfiles guardados. No se envía a nadie: es la fuente de verdad de la que salen todas las versiones. Formato y reglas en `references/maestro.md`.
- **Las versiones** (`CV - Nombre Apellido.pdf` + `.docx`): CVs de 1 o 2 páginas, armados eligiendo desde el maestro para un objetivo o una oferta concreta.

Al empezar, revisa si la persona ya tiene un maestro (lo adjuntó, lo pegó, o está en los archivos de la conversación o del proyecto):

- **No tiene maestro** → Parte A y después Parte B.
- **Tiene maestro** → léelo completo y ve directo a la Parte B. Si cuenta algo nuevo (un trabajo, un curso, un logro), actualiza el maestro primero.
- **Trae una oferta pero no tiene maestro** → Parte A, enfocada en lo que pide la oferta, y luego Parte B.

---

## Parte A: construir el CV maestro

### A1. Recopilar material y objetivos

Pide lo que la persona ya tenga: CV antiguo, texto de LinkedIn o simplemente que cuente su trayectoria con sus palabras. Cualquier formato sirve.

Si no menciona su formación (estudios, título técnico o profesional, enseñanza media, cursos), pregúntala: un CV sin sección de educación queda incompleto para el ATS y para el reclutador.

Pregunta **a qué tipo de cargo apunta**. Es la pregunta más importante: sin objetivo no se puede decidir qué destacar. Si duda entre rumbos distintos, anota un objetivo principal y uno alternativo: el maestro sirve para ambos, y cada uno tendrá su propia versión.

Si la persona trae varios CVs o su LinkedIn y los datos no calzan entre sí (fechas, nombres de cargo o de empresa distintos, períodos vacíos), aclara esas diferencias en un mensaje propio **antes** de entrevistar, junto con los datos de contacto que falten. Así los datos administrativos no se mezclan después con las preguntas de logros.

### A2. Diagnosticar el tipo de perfil

Lee `references/perfiles.md` y clasifica a la persona: **con experiencia en su área**, **recién egresado o con poca experiencia**, o **trayectoria no lineal** (muchos trabajos de rubros distintos). El perfil define cuánto profundizar en cada trabajo y, más adelante, cómo se ordena cada versión.

### A3. Entrevista para sacar logros

Lee `references/entrevista.md`. La meta es transformar "qué hacía" en "qué logré y cómo se notó".

**Una experiencia por mensaje, siempre.** Cada mensaje de la entrevista trata de un solo trabajo (o proyecto, o estudio), con 1 a 3 preguntas sobre ese trabajo y nada más. Recordar exige ubicarse mentalmente en un lugar y una época: si un mensaje pregunta por dos empresas, la persona tiene que saltar de un contexto a otro y responde peor las dos. Esto vale también cuando la persona tiene prisa o cuando una experiencia parece "rápida": la siguiente empresa se abre recién después de cerrar la anterior.

El ritmo de cada experiencia es:

1. Un mensaje con 1 a 3 preguntas sobre esa experiencia. Si la persona trajo un CV antiguo, pregunta sobre esos bullets.
2. Con la respuesta, muestra los logros redactados de esa experiencia y pide confirmación ("¿Esto refleja bien lo que hiciste? ¿Algo está exagerado o falta algo?"). Si faltan detalles, haz las preguntas de seguimiento sobre esa misma experiencia.
3. Solo cuando la persona confirma, cierra esa experiencia y abre la siguiente en un mensaje nuevo, nombrándola al inicio ("Ahora, Banco Ripley").

Empieza por lo más reciente y relevante para el objetivo. Los datos administrativos (comuna, idiomas, fechas que faltan) no van mezclados con preguntas de logros: pregúntalos en A1 o en un mensaje aparte al final.

En trayectorias no lineales, **entrevista también los trabajos que no parecen relevantes para el objetivo actual**, aunque con menos profundidad: un logro de atención de clientes o de ventas puede ser el mejor argumento para otra oferta. Ese material vale oro en el maestro.

Reglas que no se negocian:

- **No inventes cifras.** Si la persona no tiene un número, busca otra medida real (volumen, frecuencia, alcance, tamaño del equipo, tiempo) o deja el logro cualitativo pero concreto.
- **No pongas palabras en su boca.** Si propones una redacción, la persona debe confirmar que es cierta.
- **Los bullets de CVs anteriores no se copian: se verifican.** Los CVs viejos suelen traer afirmaciones infladas o imprecisas ("entregado en producción", "lideré la migración", "optimicé el rendimiento"). Pregunta por cada afirmación fuerte antes de pasarla al maestro, y si la persona no la recuerda o la matiza, usa su versión.
- **Confirma los nombres que suenan raros.** Muchas personas responden dictando por voz, y la transcripción cambia nombres de empresas y tecnologías (NestJS por "Next.js", el nombre de la empresa por otro parecido). Si un nombre no calza con lo que ya sabes, confírmalo en una línea antes de redactar.
- Si la persona está apurada o tiene poca información, avanza con lo que hay y anota lo faltante en "Pendientes".

### A4. Redactar y guardar el maestro

Lee `references/redaccion.md`. Redacta los logros con la fórmula de impacto, agrega etiquetas a cada uno y guarda los datos crudos en "Datos sueltos". Escribe un perfil por cada objetivo laboral.

Muestra el contenido en el chat para que la persona lo revise **antes** de generar cualquier PDF: corregir texto es barato, regenerar archivos no. Luego guarda el maestro con la plantilla de `references/maestro.md` y entrégaselo: es suyo, puede editarlo, y la próxima vez basta con adjuntarlo.

---

## Parte B: generar una versión

### B1. Definir para qué es esta versión

- **Para una oferta concreta** (lo ideal): la persona pega el aviso. Extrae los requisitos y 8 a 15 palabras clave: nombre del cargo, herramientas, certificaciones, funciones e industria. Prioriza lo que aparece en requisitos y lo que se repite.
- **Para un objetivo general** (cuando no hay oferta, o la persona pide "mi CV en PDF"): usa el objetivo principal del maestro. Nunca conviertas el maestro completo en PDF: sería demasiado largo para enviar.

### B2. Decidir qué entra, desde cero, para esta versión

Esta decisión se toma de nuevo en cada versión; no se hereda de la anterior. Con la oferta o el objetivo a la vista, revisa cada trabajo del maestro:

- **Relevante**: respalda directamente lo que pide la oferta → va en `experiencia`, con 2 a 5 logros.
- **De apoyo**: no es del área, pero aporta algo que la oferta valora (atención de clientes, manejo de equipos, una herramienta) → puede ir en `experiencia` con 1 o 2 logros elegidos desde ese ángulo, o en `otra_experiencia`.
- **Sin relación**: va en `otra_experiencia`, en una línea, para mostrar continuidad sin quitar espacio.

Por ejemplo, en una persona que fue vendedora, emprendió y hoy trabaja en soporte TI, el trabajo de vendedora es una línea en la versión para soporte TI y experiencia relevante en la versión para un cargo comercial. Cada versión debe leerse como **una carrera coherente hacia ese cargo**, no como la lista de todo lo que la persona ha hecho.

Luego elige los logros de cada trabajo buscando por etiquetas y por las palabras clave de la oferta. Si la oferta pide un ángulo que ningún logro redactado cubre, pero los "Datos sueltos" lo respaldan, redacta el logro nuevo y agrégalo también al maestro. Si no hay respaldo, es una brecha: **no se agrega**. Y **reencuadrar no es agregar**: al redactar un logro desde otro ángulo puedes cambiar el énfasis, pero no sumar resultados, títulos o detalles que la persona no dijo ("egresé" no es "me titulé"; "atendía clientes" no es "fidelicé clientes").

### B3. Ajustar titular, perfil y orden

- **Titular**: lo más cercano al nombre del cargo de la oferta, siempre que sea verdad.
- **Perfil**: parte del perfil guardado para ese objetivo y ajústalo a la oferta; el perfil es el que cuenta el hilo de la carrera hacia este cargo.
- **Orden de secciones** según el tipo de perfil (`perfiles.md`), y logros reordenados para que lo más pertinente quede primero en cada trabajo.
- **Terminología de la oferta**: si dice "gestión de inventario", no escribas "control de stock". La sección "Adaptar a una oferta" de `redaccion.md` explica cómo manejar coincidencias parciales.

### B4. Generar el documento

Arma el JSON de esta versión según `references/esquema.md` (ejemplo en `assets/ejemplo.json`), sin etiquetas, sin datos sueltos y sin nada marcado `(por confirmar)`. Luego ejecuta:

```bash
python scripts/build_cv.py version.json --out "CV - Nombre Apellido" --pdf
```

Mantén cortos los textos que comparten línea con una ciudad o una fecha (empresa, cargo, institución): idealmente menos de ~55 caracteres. Si una empresa necesita explicación, deja el nombre corto y usa el campo `contexto`. Las líneas muy llenas hacen que algunos lectores de PDF separen la fecha de su trabajo.

El script genera DOCX y PDF en formato Harvard sin tablas y muestra **avisos de contenido** (inicios débiles como "Responsable de…", logros demasiado largos, verbos repetidos, líneas demasiado llenas). Corrige lo que corresponda y vuelve a generar. Requiere `python-docx` (`pip install python-docx`); para el PDF necesita LibreOffice. Sin LibreOffice, entrega el DOCX y explica cómo exportar a PDF desde Word o Google Docs.

### B5. Verificar

```bash
python scripts/check_ats.py "CV - Nombre Apellido.pdf" --json version.json --keywords "SQL, Power BI, presupuesto"
```

El verificador extrae el texto con hasta tres lectores de PDF distintos y comprueba que cada fecha y logro quede en el bloque de su trabajo, además del contacto, las secciones y las palabras clave. Sin oferta, omite `--keywords`.

Además, **mira el resultado**: convierte la primera página a imagen (`pdftoppm -png -r 80 archivo.pdf pagina`) y revisa que no haya líneas huérfanas, cargos cortados por un salto de página o una segunda página casi vacía. Si sobra poco espacio, recorta logros débiles antes que achicar la fuente.

### B6. Entregar

Entrega el PDF (para postular) y el DOCX (para editar), con el nombre "CV - Nombre Apellido": el archivo que se envía no debe decir el nombre de la empresa ni "versión 3". Si hubo cambios, entrega también el maestro actualizado.

En el chat, un informe breve:

- Resultado de la verificación ATS en una o dos líneas.
- Con oferta: palabras clave cubiertas y las que faltan; de las que faltan, cuáles son brechas reales y cuáles podría respaldar si las confirma.
- Qué trabajos quedaron como relevantes y cuáles en una línea, en una frase, para que la persona pueda corregir el criterio.
- Una o dos mejoras opcionales, si las hay.

---

## Convenciones de Chile y Latinoamérica

Lee `references/formato.md` antes de la primera versión de cada conversación. Lo esencial:

- **Sin foto** por defecto: el ATS no la lee y puede generar sesgos. Solo si la persona insiste o la oferta la pide explícitamente, y entonces en otra versión aparte.
- **Datos personales mínimos**: nombre, comuna y ciudad, teléfono, correo y LinkedIn. Sin RUT, fecha de nacimiento, estado civil ni dirección completa, salvo que la oferta lo exija.
- **Largo**: 1 página para egresados y perfiles con menos de ~8 años de experiencia; 2 como máximo.
- **Papel tamaño carta**, fechas en formato MM/AAAA y orden cronológico inverso.

## Lo que esta skill no hace

Cartas de presentación, perfiles de LinkedIn, búsqueda de ofertas y preparación de entrevistas quedan fuera. Si la persona los pide, se puede ayudar en la conversación, pero no forman parte de este flujo ni del documento.