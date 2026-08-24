#!/usr/bin/env python3
"""BIMI SVG Tiny PS validator.

Checks a logo SVG against the BIMI SVG Tiny 1.2 Portable/Secure profile
without network access or third-party dependencies.

Usage:  python3 bimi_check.py logo.svg [more.svg ...]
Exit:   0 = no errors, 1 = at least one error
"""

import re
import sys
import xml.etree.ElementTree as ET

SVG_NS = "http://www.w3.org/2000/svg"
XLINK_NS = "http://www.w3.org/1999/xlink"
SIZE_LIMIT = 32 * 1024

# Explicitly forbidden by the BIMI profile: scripting, external loads, animation.
FORBIDDEN = {
    "script": "Skripting ist verboten",
    "image": "eingebettete Rasterbilder sind verboten",
    "foreignObject": "foreignObject ist verboten",
    "a": "Links sind verboten",
    "animate": "Animation ist verboten",
    "animateColor": "Animation ist verboten",
    "animateMotion": "Animation ist verboten",
    "animateTransform": "Animation ist verboten",
    "set": "Animation ist verboten",
    "discard": "Animation ist verboten",
    "audio": "Medienelemente sind verboten",
    "video": "Medienelemente sind verboten",
    "handler": "Event-Handler sind verboten",
    "listener": "Event-Handler sind verboten",
    "style": "Stylesheets gibt es in SVG Tiny nicht - Praesentationsattribute nutzen",
}

# Valid SVG 1.1, but outside the SVG Tiny 1.2 element set.
NOT_IN_TINY = {
    "clipPath": "clipPath",
    "mask": "mask",
    "filter": "filter",
    "pattern": "pattern",
    "marker": "marker",
    "symbol": "symbol",
}

# In Tiny 1.2, but risky or discouraged for BIMI.
DISCOURAGED = {
    "use": "use referenziert andere Knoten - manche Validatoren stolpern darueber",
    "switch": "switch wird von Mailclients uneinheitlich behandelt",
    "text": "Text wird ohne die passende Schrift falsch gerendert - in Pfade umwandeln",
    "tspan": "Text wird ohne die passende Schrift falsch gerendert - in Pfade umwandeln",
}


def local(tag):
    return tag.split("}", 1)[1] if "}" in tag else tag


def numbers(value):
    return [float(n) for n in re.split(r"[\s,]+", value.strip()) if n]


class Report:
    def __init__(self, path):
        self.path = path
        self.errors = []
        self.warnings = []
        self.notes = []

    def error(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    def note(self, msg):
        self.notes.append(msg)

    def show(self):
        print(f"\n=== {self.path} ===")
        for m in self.errors:
            print(f"  [FEHLER ] {m}")
        for m in self.warnings:
            print(f"  [WARNUNG] {m}")
        for m in self.notes:
            print(f"  [HINWEIS] {m}")
        if not (self.errors or self.warnings or self.notes):
            print("  Keine Beanstandungen.")
        verdict = "BESTANDEN" if not self.errors else "DURCHGEFALLEN"
        print(f"  -> {verdict}: {len(self.errors)} Fehler, {len(self.warnings)} Warnungen")


def check_root(root, rep):
    if local(root.tag) != "svg" or not root.tag.startswith("{" + SVG_NS + "}"):
        rep.error("Wurzelelement ist kein <svg> im SVG-Namensraum")
        return None

    if root.get("version") != "1.2":
        rep.error(f'version muss "1.2" sein (ist: {root.get("version") or "fehlt"})')
    if root.get("baseProfile") != "tiny-ps":
        rep.error(f'baseProfile muss "tiny-ps" sein (ist: {root.get("baseProfile") or "fehlt"})')

    for attr in ("width", "height", "x", "y"):
        if root.get(attr) is not None:
            rep.error(f"Wurzel-<svg> darf kein {attr}-Attribut haben (ist: {root.get(attr)})")

    box = root.get("viewBox")
    if not box:
        rep.error("viewBox fehlt am Wurzel-<svg>")
        return None

    try:
        vb = numbers(box)
    except ValueError:
        rep.error(f"viewBox ist nicht lesbar: {box}")
        return None

    if len(vb) != 4:
        rep.error(f"viewBox braucht genau 4 Werte (hat {len(vb)}): {box}")
        return None
    if abs(vb[2] - vb[3]) > 0.01:
        rep.error(f"viewBox muss quadratisch sein - Breite {vb[2]} != Hoehe {vb[3]}")
    return vb


def check_title(root, rep):
    children = list(root)
    if not children:
        rep.error("<svg> hat keine Kindelemente")
        return
    first = children[0]
    if local(first.tag) != "title":
        rep.error(f"Erstes Kindelement muss <title> sein (ist: <{local(first.tag)}>)")
        return
    if not (first.text or "").strip():
        rep.error("<title> ist leer - hier gehoert der Markenname hin")


def check_elements(root, rep):
    for el in root.iter():
        name = local(el.tag)
        if name in FORBIDDEN:
            rep.error(f"<{name}> gefunden: {FORBIDDEN[name]}")
        elif name in NOT_IN_TINY:
            rep.error(f"<{name}> gehoert nicht zum SVG-Tiny-1.2-Elementsatz")
        elif name in DISCOURAGED:
            rep.warn(f"<{name}>: {DISCOURAGED[name]}")

        for attr, value in el.attrib.items():
            aname = local(attr)
            if aname.startswith("on"):
                rep.error(f"Event-Attribut {aname} an <{name}>")
            if aname == "href" or attr == f"{{{XLINK_NS}}}href":
                if not value.startswith("#"):
                    rep.error(f"Externe Referenz an <{name}>: {value[:60]}")
            if aname == "role" or aname.startswith("aria-"):
                rep.warn(f"{aname} an <{name}> - ARIA gehoert nicht zu SVG Tiny, <title> uebernimmt das")
            if aname == "class":
                rep.warn(f"class-Attribut an <{name}> - SVG Tiny kennt keine CSS-Klassen")
            if aname == "style":
                rep.warn(f"style-Attribut an <{name}> - Praesentationsattribute nutzen")


def check_background(root, vb, rep):
    if not vb:
        return
    min_x, min_y, w, h = vb
    for el in root.iter():
        name = local(el.tag)
        try:
            if name == "rect":
                rw = float(el.get("width", 0))
                rh = float(el.get("height", 0))
                rx = float(el.get("x", 0))
                ry = float(el.get("y", 0))
                if rw >= w * 0.99 and rh >= h * 0.99 and rx <= min_x + 0.01 and ry <= min_y + 0.01:
                    return
            elif name == "circle":
                if float(el.get("r", 0)) >= (w / 2) * 0.97:
                    return
            elif name == "ellipse":
                if float(el.get("rx", 0)) >= (w / 2) * 0.97 and float(el.get("ry", 0)) >= (h / 2) * 0.97:
                    return
        except (TypeError, ValueError):
            continue
    rep.note(
        "Kein flaechendeckender Hintergrund erkannt. Gmail und Apple Mail "
        "beschneiden das Logo zu einem Kreis - ohne deckende Flaeche wirkt es abgeschnitten."
    )


def check_raw(raw, rep):
    if len(raw) > SIZE_LIMIT:
        rep.error(f"Datei ist {len(raw)} Bytes - das Limit liegt bei {SIZE_LIMIT} Bytes (32 KB)")
    elif len(raw) > SIZE_LIMIT * 0.8:
        rep.warn(f"Datei ist {len(raw)} Bytes - nahe am 32-KB-Limit")

    text = raw.decode("utf-8", errors="replace")
    if "<!DOCTYPE" in text:
        rep.error("DOCTYPE-Deklaration gefunden - nicht erlaubt")
    if "<!ENTITY" in text:
        rep.error("Entity-Deklaration gefunden - nicht erlaubt")
    if "<?xml-stylesheet" in text:
        rep.error("xml-stylesheet-Verarbeitungsanweisung gefunden - nicht erlaubt")
    if "data:" in text:
        rep.error("data:-URI gefunden - eingebettete Binaerdaten sind verboten")


def validate(path):
    rep = Report(path)
    try:
        with open(path, "rb") as fh:
            raw = fh.read()
    except OSError as exc:
        rep.error(f"Datei nicht lesbar: {exc}")
        rep.show()
        return False

    check_raw(raw, rep)

    try:
        root = ET.fromstring(raw)
    except ET.ParseError as exc:
        rep.error(f"Kein wohlgeformtes XML: {exc}")
        rep.show()
        return False

    vb = check_root(root, rep)
    check_title(root, rep)
    check_elements(root, rep)
    check_background(root, vb, rep)
    rep.show()
    return not rep.errors


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    results = [validate(p) for p in argv]
    print()
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
