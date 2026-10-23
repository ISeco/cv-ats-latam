# El CV maestro (formato Markdown)

El CV maestro **no es un CV**: es el inventario completo de la carrera de la persona, del que se sacan las versiones que se envían. Por eso puede ser largo, tener más logros de los que caben en una página y guardar datos sueltos que hoy no se usan pero mañana sí.

Se guarda en Markdown porque:
- La persona lo puede leer y editar en cualquier editor (incluso en el celular, Notion u Obsidian) sin depender de Claude.
- Claude lo lee completo y sin ambigüedad en una conversación nueva.
- Es la fuente de verdad: cada CV en PDF se genera desde aquí, nunca al revés.

Nombre del archivo: `CV maestro - Nombre Apellido.md`. Hay un ejemplo completo en `assets/ejemplo-maestro.md` (una persona con trayectoria variada y dos objetivos laborales).

## Reglas

1. **Solo información confirmada por la persona.** Lo que falta confirmar se marca con `(por confirmar)` y nunca pasa a un PDF así.
2. **Más es mejor.** Guarda todos los logros que salgan en la entrevista, aunque no sean relevantes para el objetivo actual: un logro de un trabajo de ventas que hoy no sirve puede ser el mejor para una postulación comercial mañana.
3. **Los logros se escriben ya redactados** (fórmula de `redaccion.md`), para usarlos tal cual. Los datos crudos van en "Datos sueltos" del mismo trabajo: permiten redactar logros nuevos desde otro ángulo sin volver a entrevistar.
4. **Etiquetas por logro**, entre llaves al final: `{clientes, ventas}`. Sirven para encontrar rápido qué logros respaldan cada tipo de oferta. Nunca se copian al PDF.
5. **Se actualiza en cada conversación** en que aparezca información nueva (un logro, un curso, un trabajo nuevo), y se entrega de nuevo a la persona.

## Plantilla

```markdown
# CV maestro: Nombre Apellido Apellido

_Actualizado: 10/2026_

## Datos de contacto
- Ciudad: Comuna, Ciudad
- Teléfono: +56 9 1234 5678
- Email: nombre.apellido@gmail.com
- LinkedIn: linkedin.com/in/usuario
- Otros: Licencia de conducir clase B

## Objetivos laborales
- Principal: Cargo al que apunta hoy
- Alternativo: Otro tipo de cargo al que también postularía

## Perfiles guardados
### Para: Cargo principal
Texto de 3 a 4 líneas, ya aprobado por la persona.

### Para: Cargo alternativo
Texto de 3 a 4 líneas.

## Experiencia

### Cargo — Empresa
- Fechas: MM/AAAA – MM/AAAA (o Actualidad)
- Ubicación: Ciudad, País
- Contexto: una línea sobre la empresa, si no es conocida
- Logros:
  - Verbo + qué + resultado. {etiqueta, etiqueta}
  - Otro logro redactado. {etiqueta}
- Datos sueltos: cifras, herramientas, responsabilidades y anécdotas que contó la persona, sin redactar.

### Otro cargo — Otra empresa
...

## Educación

### Título o carrera — Institución
- Fechas: AAAA – AAAA
- Ubicación: Ciudad, País
- Detalle: memoria de título, mención, ranking, ramos clave

## Proyectos

### Nombre del proyecto
- Fechas: AAAA
- Rol: proyecto de título / personal / freelance
- Tecnologías: ...
- Logros:
  - ... {etiqueta}

## Cursos y certificaciones
- Nombre, Institución, AAAA

## Habilidades
- Herramientas: ...
- Técnicas: ...

## Idiomas
- Español: nativo
- Inglés: intermedio (B1)

## Pendientes
- Cosas por confirmar o averiguar que mejorarían el CV (por ejemplo, una cifra que la persona puede pedirle a su exjefe).
```

## De maestro a versión para una oferta

Cada versión se arma eligiendo desde el maestro, no copiándolo entero:

1. **Decide qué trabajos son relevantes para esta oferta.** No es una decisión fija: en una persona con trayectoria variada, el trabajo de vendedor puede ser "otra experiencia" para soporte TI y "experiencia relevante" para un cargo comercial. Los relevantes van en `experiencia` con logros; el resto, en `otra_experiencia` en una línea.
2. **Elige 2 a 5 logros por trabajo relevante**, buscando por etiquetas y por las palabras clave de la oferta. Si un logro no existe redactado desde el ángulo que pide la oferta pero los "Datos sueltos" lo respaldan, redáctalo y agrégalo también al maestro. **Reencuadrar no es agregar**: puedes cambiar el énfasis de un logro (destacar al cliente en vez de la técnica), pero no sumar resultados, títulos ni detalles que no estén en el maestro.
3. **Usa el perfil guardado** del objetivo que corresponda y ajústalo a la oferta. Si no hay uno adecuado, escríbelo y guárdalo en el maestro.
4. **Arma el JSON** de esa versión (`esquema.md`) sin etiquetas, sin "Datos sueltos" y sin nada marcado `(por confirmar)`.
5. Genera el PDF con `build_cv.py` y verifica con `check_ats.py`.

El JSON es un archivo de trabajo: se puede guardar junto al PDF para retocar esa versión, pero lo que se conserva a largo plazo es el maestro.

## Si la persona pide el maestro en PDF

Genera una versión general desde el maestro hacia su objetivo principal, con los mejores logros de cada trabajo y respetando el largo (1 o 2 páginas). El maestro completo no se convierte tal cual en PDF: sería un documento demasiado largo para enviar.
