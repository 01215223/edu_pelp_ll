#!/usr/bin/env python3
"""Rysunki do „Komentarza do wykładów 1–5” (katalog wyklady/figury).

Każdy rysunek powstaje jako SVG (wersja HTML) i PNG 2× (wersja PDF — MuPDF
Story nie rysuje SVG przez <img>). Rasteryzacja: build/svg2png.js
(wymaga @resvg/resvg-js, tak jak w kompendium).

Użycie:
    python3 figures_wyklady.py          # SVG + PNG
    python3 figures_wyklady.py --svg    # tylko SVG
"""
from __future__ import annotations

import math
import os
import shutil
import subprocess
import sys

from svgkit import Fig

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "wyklady", "figury")
OUT_PNG = os.path.join(OUT, "png")
os.makedirs(OUT, exist_ok=True)
os.makedirs(OUT_PNG, exist_ok=True)

# dodatkowe klasy rysunkowe (svgkit zna tylko podstawowe symbole); muszą być
# w Fig.CLS, bo render() zamienia je na atrybuty inline — rysunki wstawiamy
# przez <img>, więc zewnętrzny CSS by nie działał
Fig.CLS.update({
    "sy": 'stroke="#1f2937" fill="none" stroke-width="1.6"',
    "tan": 'stroke="#b45309" fill="none" stroke-width="1.2" stroke-dasharray="4 3"',
    "sec": 'stroke="#0e7c86" fill="none" stroke-width="1.2"',
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
        shutil.move("/tmp/" + name[:-4] + ".png", os.path.join(OUT_PNG, name[:-4] + ".png"))
    return name


def axes(f: Fig, x0, y0, w, h, xlab, ylab):
    """Osie wykresu: (x0, y0) = lewy dolny róg."""
    f.items.append(f'<polyline points="{x0},{y0} {x0},{y0-h}" class="sy" marker-end="url(#ak)"/>')
    f.items.append(f'<polyline points="{x0},{y0} {x0+w},{y0}" class="sy" marker-end="url(#ak)"/>')
    f.txt(x0 + w - 4, y0 + 16, xlab, "end", 11)
    f.txt(x0 + 8, y0 - h - 4, ylab, "start", 11)
    return f


# ------------------------------------------------------------------ 1. obwód
def f_obwod():
    f = Fig(360, 250)
    T, B = 40, 210
    XL, XM, XR = 70, 180, 300
    f.wire((XL, T), (XR, T))
    f.wire((XL, B), (XR, B))
    f.vsrc(XL, T, XL, 100, "E1", "", side=-1, plus=-1)
    f.res(XL, 100, XL, B, "R1", "", side=-1)
    f.res(XM, T, XM, B, "R2", "", side=-1)
    f.res(XR, T, XR, 115, "R3", "", side=1)
    f.vsrc(XR, 115, XR, B, "E2", "", side=1, plus=-1)
    for x in (XL, XM, XR):
        f.node(x, T).node(x, B)
    f.txt(XM, T - 10, "A", "middle", 13)
    f.ground(XM, B)
    f.txt(XM - 12, B + 4, "B", "end", 12)
    f.arrow(XL + 16, B - 26, XL + 16, 116, "")
    f.txt(XL + 20, B - 52, "I1", "start", 12)
    f.arrow(XM - 14, T + 34, XM - 14, 146, "")
    f.txt(XM - 18, T + 30, "I2", "end", 12)
    f.arrow(XR - 14, B - 34, XR - 14, 140, "")
    f.txt(XR - 18, B - 38, "I3", "end", 12)
    return save("obwod.svg", f)


# --------------------------------------------------------- 2. superpozycja
def _mini(f, ox, oy, kind, title, note=""):
    T, B = oy + 34, oy + 164
    XL, XM, XR = ox + 34, ox + 114, ox + 194
    f.txt(XM, oy + 12, title, "middle", 11.5, cls="ttl")
    f.wire((XL, T), (XR, T))
    f.wire((XL, B), (XR, B))
    if kind in ("full", "E1"):
        f.vsrc(XL, T, XL, oy + 96, "E1", "", side=-1, plus=-1)
    else:
        f.wire((XL, T), (XL, oy + 96))
        f.txt(XL - 8, oy + 96, "zw.", "end", 9.5, cls="gry")
    f.res(XL, oy + 96, XL, B, "R1", "", side=-1)
    f.res(XM, T, XM, B, "R2", "", side=-1)
    f.res(XR, T, XR, oy + 110, "R3", "", side=1)
    if kind in ("full", "E2"):
        f.vsrc(XR, oy + 110, XR, B, "E2", "", side=1, plus=-1)
    else:
        f.wire((XR, oy + 110), (XR, B))
        f.txt(XR + 8, oy + 106, "zw.", "start", 9.5, cls="gry")
    for x in (XL, XM, XR):
        f.node(x, T).node(x, B)
    f.txt(XM, T - 8, "A", "middle", 11)
    f.ground(XM, B)
    if note:
        f.txt(XM, B + 26, note, "middle", 9.5, cls="gry")


def f_superpozycja():
    f = Fig(730, 224)
    _mini(f, 14, 4, "full", "1° obwód pełny")
    _mini(f, 254, 4, "E1", "2° tylko E1", "E2 zwarte (E2 = 0)")
    _mini(f, 494, 4, "E2", "3° tylko E2", "E1 zwarte (E1 = 0)")
    return save("superpozycja.svg", f)


# ----------------------------------------------------------- 3. Thévenin
def f_thevenin():
    f = Fig(540, 250)
    T, B = 48, 196

    def two_pole(ox, out_label):
        XL, XR = ox + 40, ox + 170
        f.wire((XL, T), (XR, T))
        f.wire((XL, B), (XR, B))
        f.wire((XL, T), (XL - 26, T))            # zacisk A
        f.wire((XL, B), (XL - 26, B))            # zacisk B
        f.vsrc(XL, T, XL, 110, "E1", "", side=-1, plus=-1)
        f.res(XL, 110, XL, B, "R1", "", side=-1)
        f.res(XR, T, XR, 120, "R3", "", side=1)
        f.vsrc(XR, 120, XR, B, "E2", "", side=1, plus=-1)
        for x in (XL, XR):
            f.node(x, T).node(x, B)
        f.node(XL - 26, T).node(XL - 26, B)
        f.txt(XL - 26, T - 10, "A", "middle", 12)
        f.txt(XL - 26, B + 16, "B", "middle", 12)
        f.txt(ox + 105, 18, out_label, "middle", 11.5, cls="ttl")

    two_pole(20, "dwójnik oryginalny (widziany z A–B)")
    f.txt(276, 130, "≡", "middle", 26, cls="ttl")

    # równoważnik: Eth + Rt w jednej gałęzi, obciążenie R2 w drugiej
    ox = 300
    XL, XR = ox + 40, ox + 150
    f.txt(ox + 95, 18, "źródło Thévenina + obciążenie", "middle", 11.5, cls="ttl")
    f.wire((XL, T), (XR, T))
    f.wire((XL, B), (XR, B))
    f.wire((XL, T), (XL - 26, T))
    f.wire((XL, B), (XL - 26, B))
    f.vsrc(XL, T, XL, 110, "Eth", "", side=-1, plus=-1)
    f.res(XL, 110, XL, B, "Rt", "", side=-1)
    f.res(XR, T, XR, B, "R2", "", side=1)
    for x in (XL, XR):
        f.node(x, T).node(x, B)
    f.node(XL - 26, T).node(XL - 26, B)
    f.txt(XL - 26, T - 10, "A", "middle", 12)
    f.txt(XL - 26, B + 16, "B", "middle", 12)
    f.txt(270, 236, "Eth = 8 V, Rt = 1 Ω  →  I = Et/(Rt+R2) = 2 A", "middle", 10, cls="gry")
    return save("thevenin.svg", f)


# ------------------------------------------------------------ 4. dzielniki
def f_dzielniki():
    f = Fig(540, 210)
    T, B = 44, 168
    # --- dzielnik napięciowy
    XL, XR = 46, 150
    f.txt(100, 20, "dzielnik napięciowy", "middle", 11.5, cls="ttl")
    f.wire((XL, T), (XR, T))
    f.wire((XL, B), (XR + 60, B))
    f.vsrc(XL, T, XL, B, "U", "", side=-1, plus=-1)
    f.res(XR, T, XR, 106, "R1", "", side=-1)
    f.res(XR, 106, XR, B, "R2", "", side=-1)
    f.node(XR, T).node(XR, 106)
    f.node(XL, T).node(XL, B)
    f.wire((XR, 106), (XR + 60, 106))
    f.node(XR + 60, 106).node(XR + 60, B)
    f.arrow(XR + 44, B - 4, XR + 44, 102, "")
    f.txt(XR + 50, 146, "U1", "start", 11)
    f.txt(100, 202, "U1 = U·R1/(R1+R2)", "middle", 10, cls="gry")

    # --- dzielnik prądowy
    XL2, XR2 = 300, 500
    f.txt(400, 20, "dzielnik prądowy", "middle", 11.5, cls="ttl")
    f.wire((XL2, T), (XR2, T))
    f.wire((XL2, B), (XR2, B))
    f.isrc(XL2, T, XL2, B, "I", "", side=-1)
    XA, XB = XL2 + 55, XL2 + 130
    f.res(XA, T, XA, B, "R1", "", side=1)
    f.res(XB, T, XB, B, "R2", "", side=1)
    for x in (XL2, XA, XB):
        f.node(x, T).node(x, B)
    f.arrow(XA - 10, T + 22, XA - 10, B - 26, "")
    f.txt(XA - 14, T + 18, "I1", "end", 11)
    f.txt(400, 202, "I1 = I·G1/(G1+G2) = I·R2/(R1+R2)", "middle", 10, cls="gry")
    return save("dzielniki.svg", f)


# ---------------------------------------------------------------- 5. mostek
def f_mostek():
    f = Fig(340, 250)
    A, Bn = (170, 30), (170, 225)
    C, D = (70, 130), (270, 130)
    f.res(*A, *C, "R1", "", side=-1)
    f.res(*A, *D, "R2", "", side=1)
    f.res(*C, *Bn, "R3", "", side=-1)
    f.res(*D, *Bn, "R4", "", side=1)
    f.res(*C, *D, "R5", "", side=-1)
    for p in (A, Bn, C, D):
        f.node(*p)
    f.txt(A[0], A[1] - 12, "A", "middle", 13)
    f.txt(Bn[0] + 14, Bn[1] + 2, "B", "start", 13)
    f.txt(C[0] - 14, C[1] + 4, "C", "end", 12)
    f.txt(D[0] + 14, D[1] + 4, "D", "start", 12)
    f.txt(170, 246, "R1 = 10 Ω, R2 = 20 Ω, R3 = 30 Ω, R4 = 40 Ω, R5 = 50 Ω",
          "middle", 9.5, cls="gry")
    return save("mostek.svg", f)


# ------------------------------------------------------------- 6. delta-Y
def f_delta_y():
    f = Fig(440, 220)
    P1, P2, P3 = (60, 50), (60, 175), (170, 112)
    f.txt(110, 26, "trójkąt (Δ)", "middle", 11.5, cls="ttl")
    f.res(*P1, *P2, "Rxy", "", side=-1)
    f.res(*P2, *P3, "Ryz", "", side=1)
    f.res(*P3, *P1, "Rzx", "", side=1)
    for p in (P1, P2, P3):
        f.node(*p)
    f.txt(P1[0] - 12, P1[1] + 2, "x", "end", 11)
    f.txt(P2[0] - 12, P2[1] + 4, "y", "end", 11)
    f.txt(P3[0] + 10, P3[1] + 14, "z", "start", 11)
    f.txt(220, 115, "⇄", "middle", 22, cls="ttl")

    cx, cy = 340, 118
    Q1, Q2, Q3 = (cx, 56), (cx - 58, 182), (cx + 58, 182)
    f.txt(cx, 26, "gwiazda (Y)", "middle", 11.5, cls="ttl")
    f.res(*Q1, cx, cy, "Rx", "", side=1)
    f.res(cx, cy, *Q2, "Ry", "", side=-1)
    f.res(cx, cy, *Q3, "Rz", "", side=1)
    for p in (Q1, Q2, Q3, (cx, cy)):
        f.node(*p)
    f.txt(Q1[0], Q1[1] - 8, "x", "middle", 11)
    f.txt(Q2[0] - 6, Q2[1] + 14, "y", "middle", 11)
    f.txt(Q3[0] + 6, Q3[1] + 14, "z", "middle", 11)
    return save("delta_y.svg", f)


# ------------------------------------------------------- 7. wzmacniacz WO
def f_wo():
    f = Fig(560, 300)

    def body(ox, oy):
        f.items.append(
            f'<polygon points="{ox+66},{oy+34} {ox+66},{oy+126} {ox+156},{oy+80} z" class="symf"/>'
        )
        f.txt(ox + 76, oy + 56, "−", "middle", 13)
        f.txt(ox + 76, oy + 112, "+", "middle", 13)
        f.wire((ox + 40, oy + 52), (ox + 66, oy + 52))
        f.wire((ox + 40, oy + 108), (ox + 66, oy + 108))
        f.wire((ox + 156, oy + 80), (ox + 176, oy + 80))
        f.node(ox + 176, oy + 80)
        f.txt(ox + 180, oy + 74, "u2", "start", 11)

    def feedback(ox, oy):
        f.node(ox + 40, oy + 52)
        f.wire((ox + 40, oy + 52), (ox + 40, oy + 8), (ox + 176, oy + 8), (ox + 176, oy + 80))
        f.res(ox + 78, oy + 8, ox + 132, oy + 8, "R2", "", side=0)

    # ------------------------------------------------ odwracający
    ox, oy = 6, 34
    body(ox, oy)
    feedback(ox, oy)
    f.vsrc(ox + 4, oy + 52, ox + 4, oy + 112, "ui", "", side=-1, plus=-1)
    f.res(ox + 4, oy + 52, ox + 40, oy + 52, "R1", "", side=1)
    f.wire((ox + 4, oy + 112), (ox + 18, oy + 112))
    f.ground(ox + 18, oy + 112)
    f.node(ox + 4, oy + 52)
    f.wire((ox + 40, oy + 108), (ox + 40, oy + 138))
    f.ground(ox + 40, oy + 138)
    f.txt(ox + 116, oy + 252, "odwracający:  u2 = −(R2/R1)·ui", "middle", 11, cls="ttl")

    # ------------------------------------------------ nieodwracający
    ox, oy = 306, 34
    body(ox, oy)
    feedback(ox, oy)
    f.wire((ox + 40, oy + 52), (ox + 22, oy + 52))
    f.res(ox + 22, oy + 52, ox + 22, oy + 104, "R1", "", side=-1)
    f.ground(ox + 22, oy + 104)
    f.vsrc(ox + 4, oy + 140, ox + 4, oy + 184, "ui", "", side=-1, plus=-1)
    f.wire((ox + 4, oy + 140), (ox + 52, oy + 140), (ox + 52, oy + 108), (ox + 66, oy + 108))
    f.wire((ox + 4, oy + 184), (ox + 26, oy + 184))
    f.ground(ox + 26, oy + 184)
    f.node(ox + 4, oy + 140)
    f.txt(ox + 116, oy + 252, "nieodwracający:  u2 = (1 + R2/R1)·ui", "middle", 11, cls="ttl")
    return save("wo.svg", f)


# -------------------------------------------------- 8. element nieliniowy
def f_nieliniowy():
    f = Fig(560, 260)
    # (a) charakterystyka + Rs, Rd
    x0, y0 = 56, 200
    axes(f, x0, y0, 180, 150, "u", "i")
    f.txt(146, 24, "opór nieliniowy: Rs i Rd", "middle", 11.5, cls="ttl")
    pts = [(0, 0), (30, 12), (60, 30), (90, 58), (120, 100), (150, 148)]
    d = " ".join(f"{x0+3+px},{y0-py}" for px, py in pts)
    f.items.append(f'<polyline points="{d}" class="sy"/>')
    px, py = 60, 30
    f.items.append(f'<line x1="{x0+3+px}" y1="{y0}" x2="{x0+3+px}" y2="{y0-py}" class="sec" stroke-dasharray="3 3"/>')
    f.items.append(f'<line x1="{x0}" y1="{y0-py}" x2="{x0+3+px}" y2="{y0-py}" class="sec" stroke-dasharray="3 3"/>')
    f.node(x0 + 3 + px, y0 - py)
    f.txt(x0 + 3 + px + 8, y0 - py - 10, "P(U0, I0)", "start", 10)
    f.items.append(f'<polyline points="{x0+3+16},{y0-4} {x0+3+126},{y0-102}" class="tan"/>')
    f.txt(x0 + 136, y0 - 98, "Rd: styczna", "start", 9.5)
    f.items.append(f'<line x1="{x0}" y1="{y0}" x2="{x0+3+px}" y2="{y0-py}" class="sec"/>')
    f.txt(x0 + 30, y0 - 30, "Rs: sieczna", "start", 9.5)

    # (b) prosta oporu
    x0, y0 = 340, 200
    axes(f, x0, y0, 180, 150, "u", "i")
    f.txt(430, 24, "punkt pracy z prostą oporu", "middle", 11.5, cls="ttl")
    pts = [(0, 0), (25, 10), (50, 26), (75, 50), (100, 82), (125, 120), (152, 148)]
    d = " ".join(f"{x0+3+px},{y0-py}" for px, py in pts)
    f.items.append(f'<polyline points="{d}" class="sy"/>')
    ET, IT = 150, 148
    f.items.append(f'<line x1="{x0}" y1="{y0-IT}" x2="{x0+ET}" y2="{y0}" class="sec"/>')

    ix, iy = 3 + 79, 56
    f.node(x0 + ix, y0 - iy)
    f.txt(x0 + ix + 8, y0 - iy - 10, "punkt pracy", "start", 10)
    f.txt(430, 236, "prosta: i = ET/Rt − u/Rt  ·  przecięcie z charakterystyką",
          "middle", 9.5, cls="gry")
    return save("nieliniowy.svg", f)


# ------------------------------------------------------- 9. sygnały okresowe
def f_sygnaly():
    f = Fig(540, 452)
    panels = [(76, "prostokątny"), (222, "trójkątny"), (368, "sinusoidalny")]
    for yy, nm in panels:
        x0 = 60
        f.txt(x0 + 118, yy - 48, nm, "middle", 11, cls="ttl")
        f.items.append(f'<polyline points="{x0},{yy+44} {x0+250},{yy+44}" class="sy" marker-end="url(#ak)"/>')
        f.items.append(f'<polyline points="{x0},{yy+44} {x0},{yy-34}" class="sy"/>')
        f.items.append(f'<line x1="{x0}" y1="{yy}" x2="{x0+250}" y2="{yy}" class="gry" stroke-dasharray="3 3"/>')
        f.txt(x0 - 6, yy + 4, "X0", "end", 9.5)
        if nm == "prostokątny":
            d = f'M {x0} {yy-22} H {x0+62} V {yy+22} H {x0+188} V {yy-22} H {x0+250}'
            f.items.append(f'<path d="{d}" class="sy"/>')
            f.txt(x0 + 31, yy - 28, "+Xm", "middle", 9.5)
            f.txt(x0 + 125, yy + 34, "−Xm", "middle", 9.5)
            f.wire((x0, yy + 54), (x0 + 62, yy + 54), w=0.8)
            f.txt(x0 + 31, yy + 66, "t1 = δT", "middle", 9)
            f.wire((x0 + 62, yy + 54), (x0 + 188, yy + 54), w=0.8)
            f.txt(x0 + 125, yy + 66, "t0 = (1−δ)T", "middle", 9)
            f.wire((x0 + 188, yy + 54), (x0 + 250, yy + 54), w=0.8)
        elif nm == "trójkątny":
            d = (f'M {x0} {yy} L {x0+31} {yy-22} L {x0+94} {yy+22} L {x0+156} {yy-22} '
                 f'L {x0+219} {yy+22} L {x0+250} {yy-6}')
            f.items.append(f'<path d="{d}" class="sy"/>')
            f.txt(x0 + 31, yy - 28, "+Xm", "middle", 9.5)
            f.txt(x0 + 94, yy + 34, "−Xm", "middle", 9.5)
        else:
            pts = []
            for k in range(0, 251, 2):
                ang = 2 * math.pi * k / 125.0
                pts.append(f"{x0+k},{yy - 22*math.sin(ang)}")
            f.items.append(f'<polyline points="{" ".join(pts)}" class="sy"/>')
            f.txt(x0 + 31, yy - 28, "+Xm", "middle", 9.5)
            f.txt(x0 + 94, yy + 34, "−Xm", "middle", 9.5)
            f.wire((x0, yy + 54), (x0 + 125, yy + 54), w=0.8)
            f.wire((x0 + 125, yy + 54), (x0 + 250, yy + 54), w=0.8)
            f.txt(x0 + 62, yy + 66, "T", "middle", 9)
    return save("sygnaly.svg", f)


# --------------------------------------------------------- 10. dopasowanie
def f_dopasowanie():
    f = Fig(440, 250)
    x0, y0 = 70, 196
    axes(f, x0, y0, 330, 150, "R0 / Rt", "P / Pdysp")
    f.txt(232, 26, "moc w obciążeniu a rezystancja obciążenia", "middle", 11.5, cls="ttl")
    pts = []
    for k in range(2, 400):
        x = k / 100.0
        p = 4 * x / (1 + x) ** 2
        pts.append(f"{x0 + x*70},{y0 - p*110}")
    f.items.append(f'<polyline points="{" ".join(pts)}" class="sy"/>')
    f.items.append(f'<line x1="{x0+70}" y1="{y0}" x2="{x0+70}" y2="{y0-110}" class="gry" stroke-dasharray="3 3"/>')
    f.items.append(f'<line x1="{x0}" y1="{y0-110}" x2="{x0+70}" y2="{y0-110}" class="gry" stroke-dasharray="3 3"/>')
    f.txt(x0 + 70, y0 + 16, "R0 = Rt", "middle", 10)
    f.txt(x0 - 8, y0 - 106, "1", "end", 10)
    f.txt(x0 + 76, y0 - 116, "Pmax = Pdysp", "start", 10)
    for xx, lab in ((0.33, "1/3"), (3, "3")):
        f.txt(x0 + xx * 70, y0 + 16, lab, "middle", 9)
        f.items.append(f'<line x1="{x0+xx*70}" y1="{y0}" x2="{x0+xx*70}" y2="{y0-3}" class="sy"/>')
    return save("dopasowanie.svg", f)


# --------------------------------------------- 11. przesunięcie źródła
def f_przesuniecie():
    f = Fig(560, 230)
    T, B = 56, 180

    def panel(ox, title, src_branch):
        XL, XR = ox + 40, ox + 150
        f.txt(ox + 100, 22, title, "middle", 11, cls="ttl")
        f.wire((XL, T), (XR, T))
        f.wire((XL, B), (XR, B))
        f.wire((XL, T), (XL - 24, T))
        f.wire((XL, B), (XL - 24, B))
        for x in (XL, XR):
            f.node(x, T).node(x, B)
        if src_branch == 1:
            # E w gałęzi 1, „+” zwrócony do węzła A
            f.vsrc(XL, T, XL, 106, "E", "", side=-1, plus=-1)
            f.res(XL, 106, XL, B, "R1", "", side=-1)
            f.res(XR, T, XR, B, "R2", "", side=1)
        else:
            # E przeniesione do gałęzi 2 — ze zwrotem odwróconym względem A
            f.res(XL, T, XL, B, "R1", "", side=-1)
            f.res(XR, T, XR, 100, "R2", "", side=1)
            f.vsrc(XR, 100, XR, B, "E", "", side=1, plus=1)
        f.txt(XL - 24, T - 8, "A", "middle", 11)
        f.txt(XL - 24, B + 14, "B", "middle", 11)

    panel(20, "przed: E w gałęzi 1", 1)
    f.txt(270, 122, "≡", "middle", 22, cls="ttl")
    panel(310, "po: E przeniesione do gałęzi 2", 2)
    return save("przesuniecie.svg", f)


def main() -> int:
    global PNG_ENABLED
    PNG_ENABLED = "--svg" not in sys.argv
    for fn in (f_obwod, f_superpozycja, f_thevenin, f_dzielniki, f_mostek,
               f_delta_y, f_wo, f_nieliniowy, f_sygnaly, f_dopasowanie,
               f_przesuniecie):
        print("OK", fn())
    return 0


if __name__ == "__main__":
    sys.exit(main())
