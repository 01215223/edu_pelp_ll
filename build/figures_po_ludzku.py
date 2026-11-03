#!/usr/bin/env python3
"""Rysunki do „Obwody po ludzku” (katalog po-ludzku/figury).

Każdy rysunek powstaje jako SVG (wersja HTML) i PNG 2× (wersja PDF —
MuPDF Story nie rysuje SVG przez <img>). Rasteryzacja: build/svg2png.js
(wymaga @resvg/resvg-js, tak jak w kompendium).

Użycie:
    python3 figures_po_ludzku.py          # SVG + PNG
    python3 figures_po_ludzku.py --svg    # tylko SVG
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys

from svgkit import Fig

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "po-ludzku", "figury")
OUT_PNG = os.path.join(OUT, "png")
os.makedirs(OUT, exist_ok=True)
os.makedirs(OUT_PNG, exist_ok=True)

Fig.CLS.update({
    "sy": 'stroke="#1f2937" fill="none" stroke-width="1.6"',
    "tan": 'stroke="#b45309" fill="none" stroke-width="1.2" stroke-dasharray="4 3"',
    "sec": 'stroke="#0e7c86" fill="none" stroke-width="1.2"',
    "blu": 'stroke="#2563eb" fill="none" stroke-width="2.2"',
    "gry": 'fill="#6b7280" font-family="Arial,Helvetica,sans-serif"',
})

AK_MARKER = (
    '<marker id="ak" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" '
    'markerHeight="7" orient="auto-start-reverse">'
    '<path d="M0,0 L8,4 L0,8 z" fill="#1f2937"/></marker>'
)

PNG_ENABLED = True


def save(name: str, fig: Fig, png: bool | None = None) -> str:
    if png is None:
        png = PNG_ENABLED
    path = os.path.join(OUT, name)
    svg = fig.render().replace("<defs>", "<defs>" + AK_MARKER, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    if png:
        subprocess.run(["node", os.path.join(HERE, "svg2png.js"), path],
                       check=True, stdout=subprocess.DEVNULL)
        shutil.move("/tmp/" + name[:-4] + ".png",
                    os.path.join(OUT_PNG, name[:-4] + ".png"))
    return name


def axes(f: Fig, x0, y0, w, h, xlab, ylab):
    f.items.append(f'<polyline points="{x0},{y0} {x0},{y0-h}" class="sy" marker-end="url(#ak)"/>')
    f.items.append(f'<polyline points="{x0},{y0} {x0+w},{y0}" class="sy" marker-end="url(#ak)"/>')
    f.txt(x0 + w - 4, y0 + 16, xlab, "end", 11)
    f.txt(x0 + 8, y0 - h - 4, ylab, "start", 11)
    return f


# ---------------------------------------------------------------- 1. analogia
def f_analogia():
    f = Fig(640, 250)
    # --- pętla wodna (lewa)
    f.txt(160, 24, "WODA — podpowiedź", "middle", 12, cls="ttl")
    XL, XR, T, B = 60, 260, 55, 185
    f.items.append(f'<polyline points="{XL},{T} {XR},{T} {XR},{B} {XL},{B} {XL},{T}" class="blu"/>')
    # pompa na dole
    cx = 160
    f.items.append(f'<circle cx="{cx}" cy="{B}" r="16" stroke="#2563eb" fill="#ffffff" stroke-width="2"/>')
    f.txt(cx, B + 5, "P", "middle", 14, cls="ttl")
    f.txt(cx, B + 38, "pompa", "middle", 10, cls="gry")
    # zwężka na górze
    f.items.append(f'<polyline points="{cx-34},{T-10} {cx-8},{T} {cx+8},{T} {cx+34},{T-10}" class="blu"/>')
    f.items.append(f'<polyline points="{cx-34},{T+10} {cx-8},{T} {cx+8},{T} {cx+34},{T+10}" class="blu"/>')
    f.txt(cx, T - 16, "zwężka", "middle", 10, cls="gry")
    # przepływ
    f.arrow(XR - 6, T + 30, XR - 6, B - 34, "")
    f.txt(XR - 12, 124, "przepływ", "end", 10)

    f.txt(320, 128, "≈", "middle", 28, cls="ttl")

    # --- pętla elektryczna (prawa)
    f.txt(480, 24, "PRĄD — oryginał", "middle", 12, cls="ttl")
    XL2, XR2 = 380, 580
    f.wire((XL2, T), (XR2, T))
    f.wire((XL2, B), (XR2, B))
    f.wire((XR2, T), (XR2, B))
    f.vsrc(XL2, T, XL2, B, "E", "", side=-1, plus=-1)
    f.res(430, T, 530, T, "R", "", side=-1)
    for x in (XL2, XR2):
        f.node(x, T).node(x, B)
    f.arrow(XR2 - 14, T + 24, XR2 - 14, B - 30, "")
    f.txt(XR2 + 4, 124, "i", "start", 12)
    f.txt(480, B + 38, "źródło", "middle", 10, cls="gry")
    return save("analogia.svg", f)


# ---------------------------------------------------------------- 2. obwód-hero
def f_hero():
    f = Fig(400, 262)
    T, B = 42, 208
    XL, XM, XR = 72, 200, 322
    f.wire((XL, T), (XR, T))
    f.wire((XL, B), (XR, B))
    f.vsrc(XL, T, XL, 102, "E1", "", side=-1, plus=-1)
    f.res(XL, 102, XL, B, "R1", "", side=-1)
    f.res(XM, T, XM, B, "R2", "", side=-1)
    f.res(XR, T, XR, 116, "R3", "", side=1)
    f.vsrc(XR, 116, XR, B, "E2", "", side=1, plus=-1)
    for x in (XL, XM, XR):
        f.node(x, T).node(x, B)
    f.txt(XM, T - 12, "A", "middle", 14, cls="ttl")
    f.ground(XM, B)
    f.txt(XM - 22, B + 4, "B", "end", 12, cls="ttl")
    # prądy: I1 i I3 w górę (dostarczają), I2 w dół (odbiera)
    f.arrow(XL + 16, B - 26, XL + 16, 118, "")
    f.txt(XL + 20, B - 52, "I1", "start", 12)
    f.arrow(XM - 14, T + 34, XM - 14, 148, "")
    f.txt(XM - 18, T + 30, "I2", "end", 12)
    f.arrow(XR - 14, B - 34, XR - 14, 142, "")
    f.txt(XR - 18, B - 40, "I3", "end", 12)
    f.txt(200, 256, "E1 = 9 V,  E2 = 6 V,  R1 = R2 = R3 = 2 Ω",
          "middle", 10.5, cls="gry")
    return save("hero.svg", f)


# ------------------------------------------------------- 3. charakterystyki
def f_charakterystyki():
    f = Fig(760, 238)
    titles = ["źródło napięciowe\nidealne", "źródło prądowe\nidealne",
              "opór liniowy", "źródło napięciowe\nrzeczywiste"]
    for k in range(4):
        x0 = 55 + k * 185
        y0 = 190
        axes(f, x0, y0, 130, 118, "u", "i")
        for j, line in enumerate(titles[k].split("\n")):
            f.txt(x0 + 65, 22 + j * 14, line, "middle", 10.5, cls="ttl")
        if k == 0:      # u = E — pion
            f.items.append(f'<line x1="{x0+82}" y1="{y0-112}" x2="{x0+82}" y2="{y0}" class="sy"/>')
            f.txt(x0 + 82, y0 + 16, "E", "middle", 10)
            f.txt(x0 + 65, 224, "u = E, i — dowolne", "middle", 9, cls="gry")
        elif k == 1:    # i = J — poziom
            f.items.append(f'<line x1="{x0}" y1="{y0-76}" x2="{x0+124}" y2="{y0-76}" class="sy"/>')
            f.txt(x0 - 8, y0 - 72, "J", "end", 10)
            f.txt(x0 + 65, 224, "i = J, u — dowolne", "middle", 9, cls="gry")
        elif k == 2:    # opór — prosta przez początek
            f.items.append(f'<line x1="{x0}" y1="{y0}" x2="{x0+122}" y2="{y0-106}" class="sy"/>')
            f.txt(x0 + 65, 224, "u = Ri (przez zero!)", "middle", 9, cls="gry")
        else:           # rzeczywiste — opadająca
            f.items.append(f'<line x1="{x0}" y1="{y0-104}" x2="{x0+104}" y2="{y0}" class="sy"/>')
            f.txt(x0 + 104, y0 + 16, "E", "middle", 10)
            f.txt(x0 - 8, y0 - 100, "E/Rw", "end", 9)
            f.txt(x0 + 65, 224, "u = E − Rw·i (i — oddawany)", "middle", 9, cls="gry")
    return save("charakterystyki.svg", f)


# ---------------------------------------------------------------- 4. dzielniki
def f_dzielniki():
    f = Fig(600, 228)
    T, B = 48, 176
    # --- napięciowy
    XL, XR = 50, 160
    f.txt(125, 22, "dzielnik napięciowy", "middle", 11.5, cls="ttl")
    f.wire((XL, T), (XR, T))
    f.wire((XL, B), (XR + 62, B))
    f.vsrc(XL, T, XL, B, "U", "", side=-1, plus=-1)
    f.res(XR, T, XR, 112, "R1", "", side=-1)
    f.res(XR, 112, XR, B, "R2", "", side=-1)
    f.node(XR, T).node(XR, 112).node(XL, T).node(XL, B)
    f.wire((XR, 112), (XR + 62, 112))
    f.node(XR + 62, 112).node(XR + 62, B)
    f.arrow(XR + 44, B - 4, XR + 44, 108, "")
    f.txt(XR + 50, 150, "U2", "start", 11)
    f.txt(125, 214, "U2 = U · R2/(R1+R2)  —  „swój opór na górze”",
          "middle", 9.5, cls="gry")
    # --- prądowy
    XL2 = 330
    f.txt(450, 22, "dzielnik prądowy", "middle", 11.5, cls="ttl")
    XA, XB = XL2 + 70, XL2 + 170
    f.wire((XL2, T), (XB, T))
    f.wire((XL2, B), (XB, B))
    f.isrc(XL2, B, XL2, T, "I", "", side=-1)
    f.res(XA, T, XA, B, "R1", "", side=1)
    f.res(XB, T, XB, B, "R2", "", side=1)
    for x in (XL2, XA, XB):
        f.node(x, T).node(x, B)
    f.arrow(XA - 12, T + 22, XA - 12, B - 26, "")
    f.txt(XA - 16, T + 18, "I1", "end", 11)
    f.arrow(XB - 12, T + 22, XB - 12, B - 26, "")
    f.txt(XB - 16, T + 18, "I2", "end", 11)
    f.txt(450, 214, "I1 = I · R2/(R1+R2)  —  „na górze ten DRUGI”",
          "middle", 9.5, cls="gry")
    return save("dzielniki.svg", f)


# ------------------------------------------------------------ 5. superpozycja
def _mini(f, ox, oy, kind, title, note=""):
    T, B = oy + 36, oy + 166
    XL, XM, XR = ox + 36, ox + 116, ox + 196
    f.txt(XM, oy + 12, title, "middle", 11.5, cls="ttl")
    f.wire((XL, T), (XR, T))
    f.wire((XL, B), (XR, B))
    if kind in ("full", "E1"):
        f.vsrc(XL, T, XL, oy + 98, "E1", "", side=-1, plus=-1)
    else:
        f.wire((XL, T), (XL, oy + 98))
        f.txt(XL - 8, oy + 96, "zw.", "end", 9.5, cls="gry")
    f.res(XL, oy + 98, XL, B, "R1", "", side=-1)
    f.res(XM, T, XM, B, "R2", "", side=-1)
    f.res(XR, T, XR, oy + 112, "R3", "", side=1)
    if kind in ("full", "E2"):
        f.vsrc(XR, oy + 112, XR, B, "E2", "", side=1, plus=-1)
    else:
        f.wire((XR, oy + 112), (XR, B))
        f.txt(XR + 8, oy + 108, "zw.", "start", 9.5, cls="gry")
    for x in (XL, XM, XR):
        f.node(x, T).node(x, B)
    f.txt(XM, T - 8, "A", "middle", 11)
    f.ground(XM, B)
    if note:
        f.txt(XM, B + 28, note, "middle", 10, cls="gry")


def f_superpozycja():
    f = Fig(740, 236)
    _mini(f, 10, 4, "full", "1° obwód pełny", "UA = ?")
    _mini(f, 252, 4, "E1", "2° tylko E1 = 9 V", "U'A = 3 V")
    _mini(f, 494, 4, "E2", "3° tylko E2 = 6 V", "U''A = 2 V")
    return save("superpozycja.svg", f)


# --------------------------------------------------------------- 6. Thévenin
def f_thevenin():
    f = Fig(620, 258)
    T, B = 52, 198
    # dwójnik oryginalny bez R2
    f.txt(140, 22, "dwójnik widziany z A–B", "middle", 11.5, cls="ttl")
    XL, XR = 60, 220
    f.wire((XL, T), (XR, T))
    f.wire((XL, B), (XR, B))
    f.vsrc(XL, T, XL, 112, "E1", "", side=-1, plus=-1)
    f.res(XL, 112, XL, B, "R1", "", side=-1)
    f.res(XR, T, XR, 122, "R3", "", side=1)
    f.vsrc(XR, 122, XR, B, "E2", "", side=1, plus=-1)
    for x in (XL, XR):
        f.node(x, T).node(x, B)
    # zaciski na środku górnej szyny
    f.node(140, T).node(140, B)
    f.txt(140, T - 12, "A", "middle", 13, cls="ttl")
    f.txt(140, B + 18, "B", "middle", 13, cls="ttl")
    f.txt(310, 130, "≡", "middle", 26, cls="ttl")
    # równoważnik + obciążenie
    f.txt(470, 22, "źródło Thévenina + obciążenie R2", "middle", 11.5, cls="ttl")
    XL2, XR2 = 390, 550
    f.wire((XL2, T), (XR2, T))
    f.wire((XL2, B), (XR2, B))
    f.vsrc(XL2, T, XL2, 112, "ET", "", side=-1, plus=-1)
    f.res(XL2, 112, XL2, B, "RW", "", side=-1)
    f.res(XR2, T, XR2, B, "R2", "", side=1)
    for x in (XL2, XR2):
        f.node(x, T).node(x, B)
    f.node(470, T).node(470, B)
    f.txt(470, T - 12, "A", "middle", 13, cls="ttl")
    f.txt(470, B + 18, "B", "middle", 13, cls="ttl")
    f.txt(310, 244, "ET = 7,5 V,  RW = 1 Ω  →  I2 = 7,5/(1+2) = 2,5 A,  UA = 5 V",
          "middle", 10.5, cls="gry")
    return save("thevenin.svg", f)


# ------------------------------------------------------------ 7. gwiazda–trójkąt
def f_gwiazda():
    f = Fig(470, 226)
    P1, P2, P3 = (64, 52), (64, 176), (176, 114)
    f.txt(114, 26, "trójkąt (Δ): po 9 Ω", "middle", 11.5, cls="ttl")
    f.res(*P1, *P2, "Rxy", "", side=-1)
    f.res(*P2, *P3, "Ryz", "", side=1)
    f.res(*P3, *P1, "Rzx", "", side=1)
    for p in (P1, P2, P3):
        f.node(*p)
    f.txt(P1[0] - 12, P1[1] + 2, "x", "end", 11)
    f.txt(P2[0] - 12, P2[1] + 4, "y", "end", 11)
    f.txt(P3[0] + 10, P3[1] + 14, "z", "start", 11)
    f.txt(228, 120, "⇄", "middle", 22, cls="ttl")
    cx, cy = 356, 120
    Q1, Q2, Q3 = (cx, 58), (cx - 58, 184), (cx + 58, 184)
    f.txt(cx, 26, "gwiazda (Y): po 3 Ω", "middle", 11.5, cls="ttl")
    f.res(*Q1, cx, cy, "Rx", "", side=1)
    f.res(cx, cy, *Q2, "Ry", "", side=-1)
    f.res(cx, cy, *Q3, "Rz", "", side=1)
    for p in (Q1, Q2, Q3, (cx, cy)):
        f.node(*p)
    f.txt(Q1[0], Q1[1] - 8, "x", "middle", 11)
    f.txt(Q2[0] - 6, Q2[1] + 14, "y", "middle", 11)
    f.txt(Q3[0] + 6, Q3[1] + 14, "z", "middle", 11)
    f.txt(235, 218, "układ symetryczny:  RΔ = 3 · RY", "middle", 10, cls="gry")
    return save("gwiazda.svg", f)


# ------------------------------------------------------ 8. wzmacniacz operacyjny
def f_wo():
    f = Fig(600, 290)
    oy = 40
    # trójkąt WO
    ox = 300
    f.items.append(f'<polygon points="{ox},{oy+30} {ox},{oy+140} {ox+110},{oy+85} z" class="symf"/>')
    f.txt(ox + 14, oy + 62, "−", "middle", 15)
    f.txt(ox + 14, oy + 118, "+", "middle", 15)
    # wejścia
    f.wire((ox - 34, oy + 56), (ox, oy + 56))
    f.wire((ox - 34, oy + 114), (ox, oy + 114))
    # wejście + do masy
    f.wire((ox - 34, oy + 114), (ox - 34, oy + 150))
    f.ground(ox - 34, oy + 150)
    # wyjście
    f.wire((ox + 110, oy + 85), (ox + 200, oy + 85))
    f.node(ox + 200, oy + 85)
    f.txt(ox + 206, oy + 78, "uwy", "start", 12)
    # sprzężenie zwrotne Rf
    f.node(ox - 34, oy + 56)
    f.wire((ox - 34, oy + 56), (ox - 34, oy + 8), (ox + 200, oy + 8), (ox + 200, oy + 85))
    f.res(ox + 30, oy + 8, ox + 130, oy + 8, "Rf", "", side=-1)
    # gałąź wejściowa R1 + źródło
    f.res(120, oy + 56, ox - 34, oy + 56, "R1", "", side=-1)
    f.node(120, oy + 56)
    f.vsrc(90, oy + 56, 90, oy + 150, "uwe", "", side=-1, plus=-1)
    f.wire((90, oy + 56), (120, oy + 56))
    f.wire((90, oy + 150), (120, oy + 150))
    f.ground(120, oy + 150)
    # adnotacje
    f.txt(ox - 52, oy + 46, "0 V", "end", 11, cls="ttl")
    f.txt(300, oy + 210, "wirtualna masa: węzeł „−” trzyma 0 V, choć żaden przewód go nie zwiera",
          "middle", 10, cls="gry")
    f.txt(300, oy + 232, "uwy = −(Rf/R1)·uwe", "middle", 12, cls="ttl")
    return save("wo.svg", f)


# ---------------------------------------------------------- 9. prosta oporu
def f_prosta():
    f = Fig(520, 280)
    x0, y0 = 66, 224
    SX, SY = 50.0, 36.0          # px na 1 V, px na 1 A
    axes(f, x0, y0, int(8.6 * SX), int(5.2 * SY), "u [V]", "i [A]")
    f.txt(x0 + 170, 24, "punkt pracy: przecięcie dwóch wymagań", "middle", 11.5, cls="ttl")

    def P(u, i):
        return x0 + u * SX, y0 - i * SY

    # charakterystyka elementu i = u^2/8
    pts = []
    u = 0.0
    while u <= 7.2:
        pts.append("{:.1f},{:.1f}".format(*P(u, u * u / 8.0)))
        u += 0.2
    f.items.append(f'<polyline points="{" ".join(pts)}" class="sy"/>')
    f.txt(*[v + d for v, d in zip(P(6.7, 4.5), (6, 0))], "element: i = u²/8", "start", 10)
    # prosta oporu: od (0,4) do (8,0)
    a, b = P(0, 4), P(8, 0)
    f.items.append(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" class="sec"/>')
    f.txt(a[0] - 8, a[1] + 4, "4", "end", 10)
    f.txt(b[0], b[1] - 8, "8", "middle", 10)
    f.txt(*[v + d for v, d in zip(P(6.2, 0.9), (8, -4))], "prosta oporu", "start", 10)
    # punkt Q
    q = P(4, 2)
    f.node(*q)
    f.items.append(f'<line x1="{q[0]}" y1="{y0}" x2="{q[0]}" y2="{q[1]}" class="gry" stroke-dasharray="3 3"/>')
    f.items.append(f'<line x1="{x0}" y1="{q[1]}" x2="{q[0]}" y2="{q[1]}" class="gry" stroke-dasharray="3 3"/>')
    f.txt(q[0], y0 + 16, "4", "middle", 10)
    f.txt(x0 - 8, q[1] + 4, "2", "end", 10)
    f.txt(q[0] + 10, q[1] - 12, "Q (4 V, 2 A)", "start", 11, cls="ttl")
    # sieczna (Rs) i styczna (Rd)
    o = P(0, 0)
    f.items.append(f'<line x1="{o[0]}" y1="{o[1]}" x2="{q[0]}" y2="{q[1]}" class="tan"/>')
    t1, t2 = P(2, 0), P(6, 4)
    f.items.append(f'<line x1="{t1[0]}" y1="{t1[1]}" x2="{t2[0]}" y2="{t2[1]}" class="tan"/>')
    f.txt(*[v + d for v, d in zip(P(1.7, 0.7), (-4, 0))], "Rs: sieczna", "end", 9.5)
    f.txt(*[v + d for v, d in zip(P(5.9, 3.9), (6, 0))], "Rd: styczna", "start", 9.5)
    return save("prosta.svg", f)


# ------------------------------------------------------------- 10. dioda
def f_dioda():
    f = Fig(560, 250)
    # charakterystyka
    cx, cy = 150, 150
    f.txt(150, 24, "dioda idealna — charakterystyka", "middle", 11.5, cls="ttl")
    f.items.append(f'<polyline points="{cx-110},{cy} {cx+130},{cy}" class="sy" marker-end="url(#ak)"/>')
    f.items.append(f'<polyline points="{cx},{cy+58} {cx},{cy-96}" class="sy" marker-end="url(#ak)"/>')
    f.txt(cx + 122, cy + 18, "u", "end", 11)
    f.txt(cx + 10, cy - 92, "i", "start", 11)
    # kształt „L”: rozwarcie dla u<0, zwarcie dla i>0
    f.items.append(f'<polyline points="{cx-104},{cy} {cx},{cy} {cx},{cy-88}" class="blu"/>')
    f.txt(cx - 62, cy - 12, "rozwarcie", "middle", 10)
    f.txt(cx - 62, cy + 20, "i = 0, u < 0", "middle", 9, cls="gry")
    f.txt(cx + 12, cy - 58, "zwarcie", "start", 10)
    f.txt(cx + 12, cy - 40, "u = 0, i > 0", "start", 9, cls="gry")
    # obwód testowy
    f.txt(420, 24, "obwód testowy", "middle", 11.5, cls="ttl")
    XL, XR, T, B = 340, 500, 60, 190
    f.wire((XL, T), (XR, T))
    f.wire((XL, B), (XR, B))
    f.vsrc(XL, T, XL, B, "E", "", side=-1, plus=-1)
    f.res(370, T, 450, T, "R", "", side=-1)
    f.diode(XR, T, XR, B, "D", "", side=1)
    for x in (XL, XR):
        f.node(x, T).node(x, B)
    f.arrow(XR - 16, T + 26, XR - 16, B - 34, "")
    f.txt(XR - 20, T + 22, "i", "end", 11)
    f.txt(420, 232, "E = 5 V, R = 1 kΩ  →  zgadnij stan i sprawdź znak",
          "middle", 9.5, cls="gry")
    return save("dioda.svg", f)


# -------------------------------------------------------- 11. dopasowanie
def f_dopasowanie():
    f = Fig(500, 272)
    x0, y0 = 66, 218
    SX, SY = 72.0, 11.0          # px na 1 Ω, px na 1 W
    axes(f, x0, y0, int(5.4 * SX), int(16 * SY), "R0 [Ω]", "P [W]")
    f.txt(x0 + 190, 24, "moc w obciążeniu: ET = 7,5 V, RW = 1 Ω", "middle", 11.5, cls="ttl")
    pts = []
    r = 0.02
    while r <= 5.2:
        p = (7.5 / (1.0 + r)) ** 2 * r
        pts.append(f"{x0 + r*SX:.1f},{y0 - p*SY:.1f}")
        r += 0.04
    f.items.append(f'<polyline points="{" ".join(pts)}" class="sy"/>')
    for r0, lab in ((0.25, "9 W"), (1.0, "14,06 W"), (2.0, "12,5 W"), (4.0, "9 W")):
        p = (7.5 / (1.0 + r0)) ** 2 * r0
        x, y = x0 + r0 * SX, y0 - p * SY
        f.node(x, y, r=3.2)
        f.txt(x, y0 + 16, str(r0).replace(".", ","), "middle", 9.5)
        f.txt(x, y - 10, lab, "middle", 9.5)
    xp = x0 + SX
    f.items.append(f'<line x1="{xp}" y1="{y0}" x2="{xp}" y2="{y0 - 14.0625*SY}" class="gry" stroke-dasharray="3 3"/>')
    f.txt(xp, y0 + 32, "R0 = RW — szczyt", "middle", 10, cls="ttl")
    return save("dopasowanie.svg", f)


def main() -> int:
    global PNG_ENABLED
    PNG_ENABLED = "--svg" not in sys.argv
    for fn in (f_analogia, f_hero, f_charakterystyki, f_dzielniki,
               f_superpozycja, f_thevenin, f_gwiazda, f_wo, f_prosta,
               f_dioda, f_dopasowanie):
        print("OK", fn())
    return 0


if __name__ == "__main__":
    sys.exit(main())
