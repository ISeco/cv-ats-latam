# Estrategias por tipo de perfil

El mismo formato Harvard sirve para todos, pero el orden de las secciones y el peso de cada una cambian según la historia de la persona. Elige uno de los tres perfiles; si alguien está entre dos, elige según lo que más le conviene mostrar para su objetivo.

En todos los casos se usa orden **cronológico inverso** (lo más reciente primero). El CV "funcional" (solo habilidades, sin fechas por empleador) queda descartado: los ATS necesitan empresa + cargo + fechas para leer la experiencia, y los reclutadores lo asocian a querer ocultar algo.

---

## 1. Profesional con experiencia en su área

**Señal:** dos o más años trabajando en el mismo tipo de función a la que postula.

**Orden de secciones** (el orden por defecto de `build_cv.py`):
Perfil → Experiencia profesional → Educación → Cursos y certificaciones → Habilidades → Idiomas

**Cómo distribuir el espacio:**
- Últimos 10 a 15 años con detalle. Lo anterior, condensado: 1 logro por cargo o directamente en "Otra experiencia laboral".
- 3 a 5 logros en los cargos recientes; 1 o 2 en los antiguos.
- Si tuvo varios cargos en una misma empresa (ascensos), sepáralos como entradas distintas con la misma empresa: un ascenso es un logro en sí mismo.
- Educación breve: institución, título y año. Sin notas, salvo que sean muy destacables y la persona tenga menos de 3 años de experiencia.
- Más de ~8 años de experiencia relevante: 2 páginas está bien. Menos: 1 página.

**Error típico a evitar:** listar todas las funciones del cargo. El reclutador ya sabe qué hace un "Analista de Control de Gestión"; lo que no sabe es qué logró esta persona en particular.

---

## 2. Recién egresado o con poca experiencia

**Señal:** egresado hace menos de ~2 años, o con experiencia laboral escasa o no relacionada con lo que estudió.

**Orden de secciones:**
Perfil → Educación → Experiencia (prácticas incluidas) → Proyectos → Cursos y certificaciones → Habilidades → Idiomas

Usa `"orden": ["perfil", "educacion", "experiencia", "proyectos", "certificaciones", "habilidades", "idiomas", "extra"]` en el JSON.

**Qué cuenta como experiencia (y la persona suele olvidarlo):**
- Prácticas profesionales y prácticas de verano.
- Ayudantías de cátedra o investigación.
- Memoria o tesis de título, sobre todo si se hizo con una empresa.
- Proyectos académicos con un resultado concreto, proyectos personales y hackatones.
- Trabajos part-time o de temporada (vendedor, garzón, repartidor, call center). No están relacionados con la carrera, pero muestran responsabilidad, trato con clientes y manejo de presión; se redactan con logros igual que cualquier otro trabajo.
- Voluntariados, centros de alumnos y emprendimientos pequeños.

**Cómo distribuir el espacio:**
- 1 página, siempre.
- Educación con más detalle: mención, ranking o promedio si es bueno, ramos o proyectos clave relacionados con el cargo, memoria de título.
- El perfil se centra en qué sabe hacer y qué busca, no en "persona proactiva con ganas de aprender" (eso lo dice todo el mundo).
- La sección Proyectos puede pesar tanto como la experiencia. Cada proyecto: nombre, qué se construyó o resolvió, con qué herramientas, y el resultado.

**Error típico a evitar:** dejar el CV casi vacío por pensar que "no tiene experiencia". Casi siempre hay material; hay que preguntarlo.

---

## 3. Trayectoria no lineal (muchos trabajos de rubros distintos)

**Señal:** varios trabajos en áreas que no se conectan a simple vista (por ejemplo: vendedor de retail, luego administrativo, luego emprendimiento propio, luego soporte técnico), o un cambio de carrera.

Esta persona tiene un problema real: si lista todo con el mismo peso, el CV parece disperso y el reclutador no ve un hilo. Si omite trabajos, quedan vacíos de años que generan desconfianza. La solución es separar **relevancia** de **continuidad**.

**Orden de secciones:**
Perfil → Experiencia profesional (solo lo relevante, con logros) → Otra experiencia laboral (compacta) → Educación → Cursos y certificaciones → Habilidades → Idiomas

**Cómo armarlo:**
1. **Parte del objetivo.** Con el cargo objetivo claro, revisa cada trabajo y pregunta: ¿qué de esto sirve para ese cargo? Muchas veces hay habilidades transferibles escondidas (manejo de clientes, caja, inventario, coordinación de equipos, uso de sistemas, resolución de problemas, ventas).
2. **"Experiencia profesional"** lleva los trabajos que más respaldan el objetivo, con 2 a 4 logros redactados desde la óptica del cargo al que postula. Puede titularse "Experiencia relevante" con `"titulo_experiencia": "Experiencia relevante"`.
3. **"Otra experiencia laboral"** (campo `otra_experiencia`) lleva el resto: una línea por trabajo con cargo, empresa y fechas, más una frase opcional. Así demuestra continuidad sin quitarle espacio a lo importante.
4. **El perfil hace el trabajo de dar coherencia.** Es donde se cuenta el hilo en una frase: "Profesional con 8 años en atención a clientes y operaciones comerciales en retail y servicios, hoy enfocado en soporte TI…". El perfil convierte la variedad en una fortaleza (adaptabilidad, visión de distintas áreas) en vez de un problema.
5. **Habilidades** agrupa lo transferible con nombres concretos ("Atención de público", "Manejo de caja y cuadratura", "Excel", "Sistema SAP"), no adjetivos.

**Vacíos laborales:** si hay un período sin trabajo formal de más de ~6 meses, se puede incluir una línea honesta en "Otra experiencia laboral" ("Emprendimiento propio: venta de…", "Formación en desarrollo web", "Período dedicado al cuidado familiar") solo si la persona quiere. No hay que justificar cada mes; vacíos cortos no necesitan explicación.

**Emprendimientos propios:** cuentan como experiencia formal. Cargo: "Fundador/a" o "Dueño/a"; empresa: el nombre del negocio o una descripción ("Emprendimiento de repostería"). Se redactan con logros como cualquier trabajo (clientes, ventas, canales, gestión).

**La clasificación cambia con cada oferta.** Qué trabajo es "relevante" y cuál va en una línea no es una propiedad del trabajo, sino de la relación entre el trabajo y el cargo al que se postula. Por eso en el CV maestro se guardan los logros de *todos* los trabajos, y en cada versión se decide de nuevo (Parte B2 del SKILL.md). Así, la misma persona puede tener una versión que se lee como una carrera técnica y otra que se lee como una carrera comercial, ambas verdaderas.

**Error típico a evitar:** intentar que todo parezca relacionado forzando la redacción. Si un trabajo no aporta al objetivo, va compacto en "Otra experiencia laboral" y no pasa nada.
