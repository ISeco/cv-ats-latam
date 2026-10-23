# cv-ats-latam

Skill de Claude que construye CVs profesionales en español para Chile y Latinoamérica: formato Harvard, aptos para filtros ATS y basados en la experiencia real de la persona.

## Qué hace

1. **Entrevista guiada** para convertir funciones en logros con impacto, una experiencia a la vez.
2. **CV maestro en Markdown**: el inventario completo de la carrera (logros etiquetados, datos sueltos y perfiles por objetivo). Es la fuente de verdad y no se envía a nadie.
3. **Versiones por oferta**: CVs de 1 o 2 páginas en PDF y DOCX, armados desde el maestro para cada cargo.
4. **Verificación ATS**: extrae el texto con hasta tres lectores de PDF y comprueba contacto, secciones, el orden de cada bloque y las palabras clave de la oferta.

Sirve para profesionales con experiencia, recién egresados y personas con trayectorias en rubros distintos. No hace cartas de presentación, perfiles de LinkedIn ni búsqueda de ofertas.

## Estructura

```
cv-ats-latam/
├── SKILL.md              # Flujo principal (Parte A: maestro, Parte B: versiones)
├── references/           # Entrevista, redacción, perfiles, formato, maestro y esquema JSON
├── scripts/
│   ├── build_cv.py       # JSON → DOCX + PDF en formato Harvard, sin tablas
│   └── check_ats.py      # Verificación ATS del PDF generado
└── assets/               # Ejemplos: CV maestro y JSON de una versión
```

## Instalación en Claude

Comprime la carpeta `cv-ats-latam` (la carpeta, no su contenido) en un ZIP y súbela en la sección de Skills de la configuración de Claude.

## Requisitos de los scripts

- Python 3 con `python-docx` (`pip install python-docx`)
- LibreOffice, para exportar a PDF
- `pdftotext` / `pdftoppm` (poppler), para la verificación
