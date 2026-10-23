# Formato ATS y convenciones de Chile y Latinoamérica

## Qué es un ATS y qué hace realmente

Un ATS (Applicant Tracking System) es el software donde las empresas reciben y ordenan postulaciones. En Chile se usan, entre otros, plataformas locales de gestión de personas y selección (como Buk o Talana), portales con ATS integrado (Laborum, Trabajando.com, Computrabajo) y sistemas internacionales en empresas grandes (Workday, SuccessFactors, Greenhouse, Teamtailor).

Lo que hacen, en la práctica:
1. **Extraen el texto** del CV e intentan separarlo en campos: nombre, contacto, experiencias (empresa, cargo, fechas), educación, habilidades.
2. **Permiten al reclutador filtrar y buscar** por palabras clave, años de experiencia, títulos, etc. Algunos además ordenan a los candidatos según cuánto calzan con la oferta.

Por eso un CV "pasa el filtro" cuando cumple dos cosas: **se extrae completo y en orden**, y **contiene las palabras que el reclutador va a buscar**. No existe un "puntaje ATS" universal; las herramientas que dan "95/100" usan criterios propios. Esta skill verifica cosas comprobables en vez de prometer un puntaje.

## Reglas de formato (y por qué)

| Regla | Por qué |
|---|---|
| Una sola columna | Las columnas laterales se leen mezcladas con el cuerpo o al final, desordenando todo. |
| Sin tablas | Muchos ATS leen celda por celda: fechas y ciudades terminan separadas de su empresa y cargo. |
| Sin cuadros de texto | Su contenido suele perderse completo. |
| Nada en encabezado ni pie de página | Varios ATS los ignoran; si ahí está el contacto, la persona queda sin teléfono ni correo. |
| Sin foto, íconos, gráficos, barras de nivel ni logos | No se leen; los íconos de teléfono o correo pueden convertirse en caracteres basura. |
| Títulos de sección estándar | "Experiencia profesional", "Educación", "Habilidades": los nombres creativos ("Mi camino", "Lo que sé hacer") no se reconocen. |
| Fechas consistentes MM/AAAA | Formato que cualquier ATS interpreta, en cualquier idioma, para calcular años de experiencia. "Actualidad" para el cargo vigente. |
| Fuente estándar, 10,5 a 11,5 pt | Fuentes decorativas pueden extraerse con caracteres raros; menos de 10 pt cansa al lector humano. |
| Texto en negro, sin colores de fondo | Contraste máximo para lectura y para impresión. |
| PDF generado desde texto (no escaneado ni exportado como imagen) | Un PDF imagen se ve bien pero el ATS lo lee vacío. |
| Entregar PDF y DOCX | El PDF mantiene el diseño; algunos portales piden Word. Ambos los genera el script. |

El script `build_cv.py` ya cumple todo esto. Si la persona trae su propia plantilla, el verificador `check_ats.py` sobre el DOCX detecta tablas, cuadros de texto, imágenes y texto en encabezados.

## Formato Harvard

Es el formato que replica el script: nombre centrado y destacado, contacto en una línea separado por "•", títulos de sección en mayúsculas con una línea debajo, empresa en negrita y cargo en cursiva a la izquierda, ciudad y fechas alineadas a la derecha, logros en viñetas.

No funciona bien con los ATS por llamarse "Harvard", sino porque es texto simple en una columna. Muchas plantillas "Harvard" que circulan en internet arman ese diseño con **tablas invisibles** y fallan justamente en lo que prometen. El script logra el mismo diseño con tabulaciones dentro del mismo párrafo.

## Convenciones de Chile y Latinoamérica

**Datos de contacto** (en este orden, en una línea):
- Comuna y ciudad (por ejemplo "Ñuñoa, Santiago"). Sin dirección exacta.
- Teléfono con código de país: "+56 9 1234 5678".
- Correo profesional: nombre y apellido, sin apodos ni números al azar. Si el correo actual es poco serio, sugiere crear uno nuevo.
- LinkedIn sin "https://www.": "linkedin.com/in/nombre". Portafolio o GitHub solo si aporta al cargo.

**Lo que no va, salvo que la oferta lo exija expresamente:**
- **Foto.** No es obligatoria en Chile; el ATS no la lee y puede abrir la puerta a sesgos por edad o apariencia. Si la persona insiste o la oferta la pide, hazlo en una versión aparte y explica el costo.
- **RUT.** Es común verlo, pero no es necesario en esta etapa y expone un dato sensible en un documento que circula. Se entrega cuando la empresa lo pide en el proceso.
- **Fecha de nacimiento o edad, estado civil, hijos, nacionalidad, religión.** No aportan a la evaluación y pueden generar discriminación. Excepción razonable: si la persona es extranjera y tiene permiso de trabajo vigente, puede indicarlo si la oferta lo pregunta; eso lo decide ella.
- **Pretensión de renta.** Se entrega solo cuando la oferta la pide, normalmente en un campo del formulario, no en el CV.
- **Referencias.** No hace falta "Referencias a disposición": se dan cuando las piden.

**Largo:**
- 1 página: recién egresados y perfiles con menos de ~8 años de experiencia.
- 2 páginas: experiencia más larga o muy relevante. Nunca más de 2.
- Si se pasa por poco, recorta los logros más débiles o condensa trabajos antiguos antes de achicar la fuente o los márgenes.

**Papel:** tamaño carta (lo habitual en Chile y la mayoría de Latinoamérica). Para España u otros mercados con A4, usa `"estilo": {"papel": "a4"}`.

**Idioma:** español neutro y profesional, evitando chilenismos ("pega", "cachar") y siglas internas de la empresa que nadie fuera entiende. Las herramientas se escriben con su nombre oficial aunque sea en inglés (Power BI, Salesforce, Google Cloud).

**Nombre del archivo:** "CV - Nombre Apellido.pdf". Nunca "CV final v3.pdf" ni "curriculum.pdf".
