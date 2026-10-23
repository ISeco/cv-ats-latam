# Esquema del JSON para `build_cv.py`

Ejemplo completo en `assets/ejemplo.json`. Solo `nombre` es obligatorio; las secciones vacías u omitidas no se imprimen.

```json
{
  "nombre": "Nombre Apellido Apellido",
  "titular": "Cargo objetivo | Especialidad",
  "contacto": {
    "ciudad": "Comuna, Ciudad",
    "telefono": "+56 9 1234 5678",
    "email": "nombre.apellido@gmail.com",
    "linkedin": "linkedin.com/in/usuario",
    "web": "github.com/usuario",
    "otros": ["Licencia de conducir clase B"]
  },

  "perfil": "3 a 4 líneas.",

  "experiencia": [
    {
      "empresa": "Empresa S.A.",
      "ubicacion": "Santiago, Chile",
      "cargo": "Cargo",
      "inicio": "03/2021",
      "fin": "Actualidad",
      "contexto": "Opcional: una línea sobre la empresa si no es conocida (rubro, tamaño).",
      "logros": ["Verbo + qué + resultado.", "..."]
    }
  ],

  "otra_experiencia": [
    {"cargo": "Vendedor", "empresa": "Falabella", "inicio": "2016", "fin": "2018",
     "resumen": "Opcional: una frase."}
  ],

  "proyectos": [
    {"nombre": "Nombre del proyecto", "rol": "Proyecto de título", "tecnologias": ["Python", "SQL"],
     "inicio": "2024", "fin": "2025", "descripcion": "Opcional: una línea.", "logros": ["..."]}
  ],

  "educacion": [
    {"institucion": "Universidad", "ubicacion": "Santiago, Chile",
     "titulo": "Título o carrera", "inicio": "2015", "fin": "2020",
     "detalle": ["Opcional: memoria de título, mención, ranking, ramos clave."]}
  ],

  "certificaciones": [
    {"nombre": "Curso o certificación", "emisor": "Institución", "fecha": "2023"}
  ],

  "habilidades": [
    {"categoria": "Herramientas", "items": ["Excel avanzado", "SAP MM"]}
  ],

  "idiomas": [
    {"idioma": "Español", "nivel": "nativo"},
    {"idioma": "Inglés", "nivel": "intermedio (B1)"}
  ],

  "secciones_extra": [
    {"titulo": "Voluntariado", "items": ["Texto de cada línea."]}
  ],

  "orden": ["perfil", "experiencia", "otra_experiencia", "proyectos", "educacion",
            "certificaciones", "habilidades", "idiomas", "extra"],

  "estilo": {"fuente": "Cambria", "tamano": 11, "papel": "carta", "margen_cm": 1.6}
}
```

## Notas por campo

- **contacto**: se imprime en una línea, en el orden ciudad • teléfono • email • linkedin • web • rut • otros. `rut` existe pero no se usa salvo que la oferta lo pida (ver `formato.md`).
- **fechas**: texto libre, pero mantén un formato único en todo el CV: `MM/AAAA` para experiencia; solo el año en educación y certificaciones está bien. El cargo vigente lleva `"fin": "Actualidad"`.
- **ubicacion**: "Ciudad, País". Para remoto: "Remoto" o "Santiago, Chile (remoto)". Puede omitirse.
- **logros**: admite `**negrita**` puntual. Sin viñetas manuales ("•", "-") al inicio: el script las pone.
- **otra_experiencia**: una línea por trabajo (cargo en negrita, empresa, frase opcional y fechas a la derecha). Pensada para trayectorias no lineales y trabajos antiguos.
- **certificaciones**: también acepta una lista de textos simples.
- **habilidades**: también acepta una lista de textos simples (una línea cada uno).
- **títulos de sección**: se cambian con `"titulo_<seccion>"`, por ejemplo `"titulo_experiencia": "Experiencia relevante"` o `"titulo_educacion": "Formación académica"`. Usa siempre nombres reconocibles.
- **orden**: lista de secciones a imprimir y su orden. Para recién egresados, `educacion` va antes de `experiencia` (ver `perfiles.md`). Una sección que no está en `orden` no se imprime.
- **estilo.fuente**: por defecto Cambria (serif estándar, viene con Word y Office). Alternativas seguras: "Georgia", "Times New Roman", "Calibri", "Arial". Evita fuentes descargadas o decorativas.
- **estilo.papel**: "carta" (por defecto) o "a4".
