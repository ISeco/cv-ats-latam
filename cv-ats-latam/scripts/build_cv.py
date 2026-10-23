#!/usr/bin/env python3
"""
Genera un CV en formato Harvard, apto para ATS, a partir de un archivo JSON.

Uso:
    python build_cv.py datos.json --out "CV - Nombre Apellido" [--pdf] [--no-lint]

Produce <out>.docx y, con --pdf, <out>.pdf (requiere LibreOffice).

Decisiones de diseño (por qué es así):
- Sin tablas, columnas, cuadros de texto, imágenes ni encabezados/pies de página.
  Muchos ATS leen las tablas celda por celda o ignoran encabezados y cuadros de
  texto, y entonces fechas, empresas y cargos quedan desordenados o se pierden.
- Fechas y ciudades alineadas a la derecha con una tabulación dentro del mismo
  párrafo: visualmente es idéntico a la plantilla Harvard clásica, pero el texto
  sale en orden ("Empresa ... Ciudad").
- Viñetas con numeración real de Word (no el carácter "•" escrito a mano).
- Una sola fuente estándar, en negro.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

try:
    from docx import Document
    from docx.enum.section import WD_SECTION
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_BREAK
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Pt, RGBColor
except ImportError:
    sys.exit("Falta python-docx. Instálalo con: pip install python-docx")

# ----------------------------------------------------------------------------
# Configuración de estilo (sobrescribible desde "estilo" en el JSON)
# ----------------------------------------------------------------------------
ESTILO_BASE = {
    "fuente": "Cambria",        # serif estándar; Word la trae. Alternativas: "Georgia", "Times New Roman", "Calibri"
    "tamano": 11,               # puntos del texto normal (10.5 a 11.5)
    "tamano_nombre": 22,
    "tamano_titulo": 12,
    "papel": "carta",           # "carta" (Chile/LatAm) o "a4"
    "margen_cm": 1.6,
}

TITULOS = {
    "perfil": "Perfil profesional",
    "experiencia": "Experiencia profesional",
    "otra_experiencia": "Otra experiencia laboral",
    "proyectos": "Proyectos",
    "educacion": "Educación",
    "certificaciones": "Cursos y certificaciones",
    "habilidades": "Habilidades",
    "idiomas": "Idiomas",
}

ORDEN_POR_DEFECTO = [
    "perfil", "experiencia", "otra_experiencia", "proyectos",
    "educacion", "certificaciones", "habilidades", "idiomas", "extra",
]


# ----------------------------------------------------------------------------
# Utilidades de bajo nivel
# ----------------------------------------------------------------------------
def fijar_fuente(rpr_owner, nombre):
    """Fija la fuente en todos los atributos y quita las referencias al tema
    (asciiTheme etc.), que si no tienen prioridad sobre el nombre de fuente."""
    rpr = rpr_owner.get_or_add_rPr() if hasattr(rpr_owner, "get_or_add_rPr") else rpr_owner
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for att in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
        if rfonts.get(qn(att)) is not None:
            del rfonts.attrib[qn(att)]
    for att in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rfonts.set(qn(att), nombre)


def fijar_idioma(style, codigo="es-CL"):
    rpr = style.element.get_or_add_rPr()
    lang = rpr.find(qn("w:lang"))
    if lang is None:
        lang = OxmlElement("w:lang")
        rpr.append(lang)
    lang.set(qn("w:val"), codigo)


def borde_inferior(paragraph, tamano=6, espacio=1):
    ppr = paragraph._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(tamano))
    bottom.set(qn("w:space"), str(espacio))
    bottom.set(qn("w:color"), "000000")
    pbdr.append(bottom)
    ppr.append(pbdr)


def crear_numeracion_vinetas(doc):
    """Crea una definición de viñetas propia (guion corto), con sangría francesa."""
    numbering = doc.part.numbering_part.numbering_definitions._numbering
    abstract_id = 90
    abstract = OxmlElement("w:abstractNum")
    abstract.set(qn("w:abstractNumId"), str(abstract_id))
    mlt = OxmlElement("w:multiLevelType")
    mlt.set(qn("w:val"), "singleLevel")
    abstract.append(mlt)
    lvl = OxmlElement("w:lvl")
    lvl.set(qn("w:ilvl"), "0")
    for tag, val in (("w:start", "1"), ("w:numFmt", "bullet"), ("w:lvlText", "•"), ("w:lvlJc", "left")):
        el = OxmlElement(tag)
        el.set(qn("w:val"), val)
        lvl.append(el)
    ppr = OxmlElement("w:pPr")
    ind = OxmlElement("w:ind")
    ind.set(qn("w:left"), "357")
    ind.set(qn("w:hanging"), "250")
    ppr.append(ind)
    lvl.append(ppr)
    abstract.append(lvl)
    # abstractNum debe ir antes que los w:num
    first_num = numbering.find(qn("w:num"))
    if first_num is not None:
        first_num.addprevious(abstract)
    else:
        numbering.append(abstract)
    num = OxmlElement("w:num")
    num_id = 90
    num.set(qn("w:numId"), str(num_id))
    an = OxmlElement("w:abstractNumId")
    an.set(qn("w:val"), str(abstract_id))
    num.append(an)
    numbering.append(num)
    return num_id


def aplicar_vineta(paragraph, num_id):
    ppr = paragraph._p.get_or_add_pPr()
    numpr = OxmlElement("w:numPr")
    ilvl = OxmlElement("w:ilvl")
    ilvl.set(qn("w:val"), "0")
    nid = OxmlElement("w:numId")
    nid.set(qn("w:val"), str(num_id))
    numpr.append(ilvl)
    numpr.append(nid)
    ppr.insert(0, numpr)


def limpiar(texto):
    """Normaliza espacios y reemplaza caracteres que algunos ATS leen mal."""
    if texto is None:
        return ""
    t = str(texto)
    t = t.replace(" ", " ").replace("\t", " ")
    t = t.replace("“", '"').replace("”", '"').replace("’", "'")
    return re.sub(r"\s+", " ", t).strip()


# ----------------------------------------------------------------------------
# Constructor del documento
# ----------------------------------------------------------------------------
class ConstructorCV:
    def __init__(self, datos):
        self.d = datos
        self.e = {**ESTILO_BASE, **(datos.get("estilo") or {})}
        self.doc = Document()
        self._configurar_documento()
        self.num_vinetas = crear_numeracion_vinetas(self.doc)

    # -- configuración general -------------------------------------------------
    def _configurar_documento(self):
        e = self.e
        sec = self.doc.sections[0]
        if e["papel"] == "a4":
            sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
        else:
            sec.page_width, sec.page_height = Cm(21.59), Cm(27.94)
        m = Cm(e["margen_cm"])
        sec.left_margin = sec.right_margin = m
        sec.top_margin = Cm(max(e["margen_cm"] - 0.3, 1.0))
        sec.bottom_margin = m
        self.ancho_util = sec.page_width - sec.left_margin - sec.right_margin

        normal = self.doc.styles["Normal"]
        normal.font.size = Pt(e["tamano"])
        normal.font.color.rgb = RGBColor(0, 0, 0)
        fijar_fuente(normal.element, e["fuente"])
        fijar_idioma(normal)
        pf = normal.paragraph_format
        pf.space_before = Pt(0)
        pf.space_after = Pt(0)
        pf.line_spacing = 1.0

        # Los títulos de sección usan "Heading 1" para que Word y los ATS
        # reconozcan la estructura; se reestiliza para que se vea Harvard.
        h1 = self.doc.styles["Heading 1"]
        h1.font.size = Pt(e["tamano_titulo"])
        h1.font.bold = True
        h1.font.italic = False
        h1.font.all_caps = True
        h1.font.color.rgb = RGBColor(0, 0, 0)
        fijar_fuente(h1.element, e["fuente"])
        h1pf = h1.paragraph_format
        h1pf.space_before = Pt(10)
        h1pf.space_after = Pt(4)
        h1pf.keep_with_next = True
        h1pf.line_spacing = 1.0

        props = self.doc.core_properties
        nombre = limpiar(self.d.get("nombre"))
        props.title = f"CV {nombre}".strip()
        props.author = nombre
        props.subject = limpiar(self.d.get("titular"))
        props.language = "es-CL"

    # -- piezas reutilizables ----------------------------------------------------
    def _parrafo(self, alineacion=None, antes=0, despues=0, mantener=False):
        p = self.doc.add_paragraph()
        if alineacion is not None:
            p.alignment = alineacion
        p.paragraph_format.space_before = Pt(antes)
        p.paragraph_format.space_after = Pt(despues)
        p.paragraph_format.keep_with_next = mantener
        return p

    def _run(self, p, texto, negrita=False, cursiva=False, tamano=None):
        r = p.add_run(texto)
        r.bold = negrita
        r.italic = cursiva
        if tamano:
            r.font.size = Pt(tamano)
        return r

    def _linea_doble(self, izq, der, negrita_izq=False, cursiva_izq=False,
                     cursiva_der=False, antes=0, mantener=True):
        """Texto a la izquierda y texto alineado a la derecha en el MISMO párrafo."""
        p = self._parrafo(antes=antes, mantener=mantener)
        p.paragraph_format.tab_stops.add_tab_stop(self.ancho_util, WD_TAB_ALIGNMENT.RIGHT)
        self._run(p, limpiar(izq), negrita=negrita_izq, cursiva=cursiva_izq)
        if der:
            self._run(p, "\t")
            self._run(p, limpiar(der), cursiva=cursiva_der)
        return p

    def _vineta(self, texto, mantener=False):
        p = self._parrafo(despues=1, mantener=mantener)
        aplicar_vineta(p, self.num_vinetas)
        self._partes_con_negrita(p, limpiar(texto))
        return p

    def _partes_con_negrita(self, p, texto):
        """Permite **negrita** puntual dentro de un logro (úsese con moderación)."""
        partes = re.split(r"(\*\*[^*]+\*\*)", texto)
        for parte in partes:
            if parte.startswith("**") and parte.endswith("**"):
                self._run(p, parte[2:-2], negrita=True)
            elif parte:
                self._run(p, parte)

    def _titulo(self, clave, texto=None):
        p = self.doc.add_paragraph(style="Heading 1")
        p.add_run(texto or TITULOS.get(clave, clave))
        borde_inferior(p)
        return p

    @staticmethod
    def _fechas(item):
        ini, fin = limpiar(item.get("inicio")), limpiar(item.get("fin"))
        if ini and fin:
            return f"{ini} – {fin}"
        return ini or fin

    # -- secciones -------------------------------------------------------------
    def encabezado(self):
        d = self.d
        p = self._parrafo(WD_ALIGN_PARAGRAPH.CENTER)
        self._run(p, limpiar(d["nombre"]), negrita=True, tamano=self.e["tamano_nombre"])
        if d.get("titular"):
            p = self._parrafo(WD_ALIGN_PARAGRAPH.CENTER, antes=1)
            self._run(p, limpiar(d["titular"]), tamano=self.e["tamano"] + 1)
        c = d.get("contacto") or {}
        partes = [c.get(k) for k in ("ciudad", "telefono", "email", "linkedin", "web", "rut")]
        partes += c.get("otros") or []
        partes = [limpiar(x) for x in partes if x]
        if partes:
            p = self._parrafo(WD_ALIGN_PARAGRAPH.CENTER, antes=3)
            self._run(p, " • ".join(partes))

    def perfil(self):
        if not self.d.get("perfil"):
            return
        self._titulo("perfil", self.d.get("titulo_perfil"))
        p = self._parrafo()
        self._partes_con_negrita(p, limpiar(self.d["perfil"]))

    def experiencia(self, clave="experiencia"):
        items = self.d.get(clave) or []
        if not items:
            return
        self._titulo(clave, self.d.get(f"titulo_{clave}"))
        for i, it in enumerate(items):
            antes = 0 if i == 0 else 6
            self._linea_doble(it.get("empresa"), it.get("ubicacion"), negrita_izq=True, antes=antes)
            self._linea_doble(it.get("cargo"), self._fechas(it), cursiva_izq=True,
                              mantener=bool(it.get("contexto") or it.get("logros")))
            if it.get("contexto"):
                p = self._parrafo(mantener=bool(it.get("logros")))
                self._run(p, limpiar(it["contexto"]), cursiva=False)
            logros = it.get("logros") or []
            for j, logro in enumerate(logros):
                self._vineta(logro, mantener=(j == 0 and len(logros) > 1))

    def otra_experiencia(self):
        """Formato compacto: una línea por trabajo. Pensado para trayectorias no
        lineales: muestra continuidad laboral sin quitar espacio a lo relevante."""
        items = self.d.get("otra_experiencia") or []
        if not items:
            return
        self._titulo("otra_experiencia", self.d.get("titulo_otra_experiencia"))
        for it in items:
            izq = limpiar(it.get("cargo"))
            if it.get("empresa"):
                izq += f", {limpiar(it['empresa'])}"
            if it.get("resumen"):
                izq += f". {limpiar(it['resumen'])}"
            p = self._parrafo(despues=2, mantener=False)
            p.paragraph_format.tab_stops.add_tab_stop(self.ancho_util, WD_TAB_ALIGNMENT.RIGHT)
            cargo = limpiar(it.get("cargo"))
            self._run(p, cargo, negrita=True)
            resto = izq[len(cargo):]
            if resto:
                self._run(p, resto)
            fechas = self._fechas(it)
            if fechas:
                self._run(p, "\t" + fechas)

    def proyectos(self):
        items = self.d.get("proyectos") or []
        if not items:
            return
        self._titulo("proyectos", self.d.get("titulo_proyectos"))
        for i, it in enumerate(items):
            antes = 0 if i == 0 else 6
            titulo = limpiar(it.get("nombre"))
            self._linea_doble(titulo, self._fechas(it), negrita_izq=True, antes=antes)
            if it.get("rol") or it.get("tecnologias"):
                sub = limpiar(it.get("rol"))
                if it.get("tecnologias"):
                    tec = ", ".join(limpiar(t) for t in it["tecnologias"])
                    sub = f"{sub} | {tec}" if sub else tec
                p = self._parrafo(mantener=True)
                self._run(p, sub, cursiva=True)
            if it.get("descripcion"):
                p = self._parrafo(mantener=bool(it.get("logros")))
                self._run(p, limpiar(it["descripcion"]))
            for logro in it.get("logros") or []:
                self._vineta(logro)

    def educacion(self):
        items = self.d.get("educacion") or []
        if not items:
            return
        self._titulo("educacion", self.d.get("titulo_educacion"))
        for i, it in enumerate(items):
            antes = 0 if i == 0 else 5
            self._linea_doble(it.get("institucion"), it.get("ubicacion"), negrita_izq=True, antes=antes)
            self._linea_doble(it.get("titulo"), self._fechas(it), cursiva_izq=True,
                              mantener=bool(it.get("detalle")))
            detalles = it.get("detalle") or []
            if isinstance(detalles, str):
                detalles = [detalles]
            for det in detalles:
                self._vineta(det)

    def certificaciones(self):
        items = self.d.get("certificaciones") or []
        if not items:
            return
        self._titulo("certificaciones", self.d.get("titulo_certificaciones"))
        for it in items:
            if isinstance(it, str):
                self._vineta(it)
                continue
            izq = limpiar(it.get("nombre"))
            if it.get("emisor"):
                izq += f", {limpiar(it['emisor'])}"
            p = self._parrafo(despues=1)
            p.paragraph_format.tab_stops.add_tab_stop(self.ancho_util, WD_TAB_ALIGNMENT.RIGHT)
            aplicar_vineta(p, self.num_vinetas)
            self._run(p, izq)
            if it.get("fecha"):
                self._run(p, "\t" + limpiar(it["fecha"]))

    def habilidades(self):
        grupos = self.d.get("habilidades") or []
        if not grupos:
            return
        self._titulo("habilidades", self.d.get("titulo_habilidades"))
        for g in grupos:
            p = self._parrafo(despues=2)
            if isinstance(g, str):
                self._run(p, limpiar(g))
                continue
            self._run(p, f"{limpiar(g.get('categoria'))}: ", negrita=True)
            self._run(p, ", ".join(limpiar(x) for x in g.get("items") or []))

    def idiomas(self):
        items = self.d.get("idiomas") or []
        if not items:
            return
        self._titulo("idiomas", self.d.get("titulo_idiomas"))
        partes = []
        for it in items:
            if isinstance(it, str):
                partes.append(limpiar(it))
            else:
                partes.append(f"{limpiar(it.get('idioma'))} ({limpiar(it.get('nivel'))})"
                              if it.get("nivel") else limpiar(it.get("idioma")))
        p = self._parrafo()
        self._run(p, " • ".join(partes))

    def extra(self):
        """Secciones adicionales libres: voluntariado, publicaciones, logros, etc."""
        for sec in self.d.get("secciones_extra") or []:
            self._titulo("extra", sec.get("titulo"))
            for item in sec.get("items") or []:
                self._vineta(item)

    # -- ensamblado --------------------------------------------------------------
    def construir(self):
        self.encabezado()
        orden = self.d.get("orden") or ORDEN_POR_DEFECTO
        for clave in orden:
            metodo = getattr(self, clave, None)
            if metodo is None:
                print(f"Aviso: sección desconocida en 'orden': {clave}", file=sys.stderr)
                continue
            metodo()
        # quitar el párrafo vacío inicial que python-docx deja
        cuerpo = self.doc.element.body
        primero = cuerpo[0]
        if primero.tag == qn("w:p") and not "".join(primero.itertext()).strip():
            cuerpo.remove(primero)
        return self.doc


# ----------------------------------------------------------------------------
# Revisión de contenido (avisos, no errores)
# ----------------------------------------------------------------------------
INICIOS_DEBILES = [
    "responsable de", "encargado de", "encargada de", "a cargo de", "apoyo en",
    "apoyar ", "ayudar ", "ayudé", "participación en",
    "tareas de", "funciones de", "realización de", "colaboración en",
    "trabajé en", "me encargaba", "estuve a cargo",
]


def revisar_contenido(d):
    avisos = []
    if not d.get("nombre"):
        avisos.append("ERROR: falta 'nombre'.")
    c = d.get("contacto") or {}
    if not c.get("email"):
        avisos.append("Falta el correo en 'contacto'. Es lo primero que busca un reclutador.")
    if not c.get("telefono"):
        avisos.append("Falta el teléfono en 'contacto'.")
    perfil = limpiar(d.get("perfil"))
    if len(perfil) > 600:
        avisos.append(f"El perfil tiene {len(perfil)} caracteres; apunta a 3-4 líneas (~350-500).")

    logros = []
    for clave in ("experiencia", "proyectos"):
        for it in d.get(clave) or []:
            for l in it.get("logros") or []:
                logros.append((it.get("cargo") or it.get("nombre") or "", limpiar(l)))
    sin_cifra = 0
    primeras = {}
    for cargo, l in logros:
        low = l.lower()
        for ini in INICIOS_DEBILES:
            if low.startswith(ini):
                avisos.append(f"Inicio débil ('{ini.strip()}…') en «{l[:60]}». Empieza por el verbo del logro.")
                break
        if len(l) > 240:
            avisos.append(f"Logro muy largo ({len(l)} caracteres): «{l[:60]}…». Máximo ~2 líneas.")
        if not re.search(r"\d", l):
            sin_cifra += 1
        palabra = re.sub(r"[^\wáéíóúñü]", "", low.split(" ")[0]) if low else ""
        if palabra:
            primeras[palabra] = primeras.get(palabra, 0) + 1
        if re.search(r"\byo\b", low):
            avisos.append(f"Evita 'yo' en «{l[:60]}».")
    if logros and sin_cifra / len(logros) > 0.6:
        avisos.append(f"{sin_cifra} de {len(logros)} logros no tienen ninguna cifra. "
                      "Revisa si existe alguna medida real (volumen, frecuencia, tamaño de equipo, tiempo); "
                      "si no existe, está bien: no inventes números.")
    for palabra, n in primeras.items():
        if n >= 3:
            avisos.append(f"El verbo '{palabra}' abre {n} logros; varía los verbos.")
    for it in d.get("experiencia") or []:
        n = len(it.get("logros") or [])
        if n > 6:
            avisos.append(f"'{it.get('cargo')}' tiene {n} logros; deja los 3-5 más fuertes.")
    # líneas con texto a la izquierda y ciudad/fecha a la derecha
    for clave, izq_der in (("experiencia", (("empresa", "ubicacion"), ("cargo", None))),
                           ("educacion", (("institucion", "ubicacion"), ("titulo", None)))):
        for it in d.get(clave) or []:
            fechas = " – ".join(x for x in (it.get("inicio"), it.get("fin")) if x)
            for izq, der in izq_der:
                largo = len(limpiar(it.get(izq))) + len(limpiar(it.get(der)) if der else fechas)
                if largo > 80:
                    avisos.append(f"La línea de «{limpiar(it.get(izq))[:40]}» es muy larga ({largo} caracteres "
                                  "con su ciudad/fecha). Acórtala o mueve la descripción a 'contexto'.")
    return avisos


# ----------------------------------------------------------------------------
# Conversión a PDF
# ----------------------------------------------------------------------------
def a_pdf(ruta_docx):
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        print("No se encontró LibreOffice: se generó solo el DOCX. "
              "Puedes exportarlo a PDF desde Word o Google Docs (Archivo → Descargar → PDF).")
        return None
    salida = os.path.dirname(os.path.abspath(ruta_docx))
    perfil = tempfile.mkdtemp(prefix="lo_cv_")
    cmd = [soffice, f"-env:UserInstallation=file://{perfil}", "--headless",
           "--convert-to", "pdf", "--outdir", salida, ruta_docx]
    try:
        subprocess.run(cmd, check=True, capture_output=True, timeout=180)
    except Exception as exc:  # noqa: BLE001
        print(f"No se pudo convertir a PDF ({exc}). Entrega el DOCX y exporta a PDF desde Word/Google Docs.")
        return None
    finally:
        shutil.rmtree(perfil, ignore_errors=True)
    pdf = os.path.splitext(ruta_docx)[0] + ".pdf"
    return pdf if os.path.exists(pdf) else None


def main():
    ap = argparse.ArgumentParser(description="Genera un CV Harvard apto para ATS desde JSON.")
    ap.add_argument("json", help="Archivo JSON con los datos del CV")
    ap.add_argument("--out", required=True, help="Ruta de salida sin extensión, p. ej. 'CV - Ana Pérez'")
    ap.add_argument("--pdf", action="store_true", help="También generar PDF (requiere LibreOffice)")
    ap.add_argument("--no-lint", action="store_true", help="No mostrar avisos de contenido")
    args = ap.parse_args()

    with open(args.json, encoding="utf-8") as f:
        datos = json.load(f)

    if not args.no_lint:
        avisos = revisar_contenido(datos)
        if avisos:
            print("Avisos de contenido:")
            for a in avisos:
                print(f"  - {a}")
            if any(a.startswith("ERROR") for a in avisos):
                sys.exit(1)

    doc = ConstructorCV(datos).construir()
    ruta_docx = args.out + ".docx"
    os.makedirs(os.path.dirname(os.path.abspath(ruta_docx)), exist_ok=True)
    doc.save(ruta_docx)
    print(f"DOCX: {ruta_docx}")
    if args.pdf:
        pdf = a_pdf(ruta_docx)
        if pdf:
            print(f"PDF:  {pdf}")


if __name__ == "__main__":
    main()
