"""Generates the SVG figures used in the compendium."""
from __future__ import annotations

import os
from svgkit import Fig

OUT = os.path.join(os.path.dirname(__file__), "..", "kompendium", "figury")
os.makedirs(OUT, exist_ok=True)

STYLE = """<style>
.wi{stroke:#1f2937;fill:none;stroke-linecap:round}
.sym{stroke:#1f2937;fill:none;stroke-width:1.5}
.bx{stroke:#1f2937;fill:#fff;stroke-width:1.5}
.nd{fill:#1f2937}
.lb{fill:#111827;font-family:'Segoe UI',Arial,sans-serif}
.qa{stroke:#b91c1c;fill:none;stroke-width:1.2;color:#b91c1c}
.ttl{fill:#1f2937;font-family:'Segoe UI',Arial,sans-serif;font-weight:600}
</style>"""


def save(name: str, fig: Fig):
    svg = fig.render()
    with open(os.path.join(OUT, name), "w") as f:
        f.write(svg)
    return name


# ---------------------------------------------------------------- 1. konwencje
def f_konwencje():
    f = Fig(430, 175)
    # odbiornik
    f.wire((20, 30), (20, 120), (150, 120))
    f.res(150, 120, 150, 30, "R")
    f.wire((150, 30), (20, 30))
    f.arrow(20, 30, 20, 120, "")
    f.txt(34, 78, "i", "start", 13)
    f.arrow(150, 120, 150, 30, "")
    f.txt(140, 70, "u", "end", 13)
    f.txt(85, 150, "odbiornik: p = u·i > 0", "middle", 12)
    f.txt(85, 165, "strzałki zgodne", "middle", 11, italic=True)

    # źródło
    f.wire((270, 30), (270, 120), (400, 120))
    f.items.append(f'<circle cx="335" cy="30" r="11" class="sym"/>')
    f.wire((270, 30), (324, 30))
    f.wire((346, 30), (400, 30))
    f.txt(329, 34, "–", "middle", 12)
    f.txt(341, 34, "+", "middle", 12)
    f.arrow(270, 30, 270, 120, "")
    f.txt(258, 78, "i", "end", 13)
    f.arrow(335, 120, 335, 41, "")
    f.txt(345, 80, "u", "start", 13)
    f.txt(335, 150, "źródło: p = u·i < 0", "middle", 12)
    f.txt(335, 165, "strzałki przeciwne", "middle", 11, italic=True)
    return save("konwencje.svg", f)


# ------------------------------------------------- 2. szeregowo / równolegle
def f_szereg_rown():
    f = Fig(520, 175)
    # --- szeregowe
    f.wire((45, 45), (60, 45))
    f.res(60, 45, 130, 45, "R", "1", side=-1)
    f.wire((130, 45), (145, 45))
    f.res(145, 45, 215, 45, "R", "2", side=-1)
    f.wire((215, 45), (235, 45), (235, 130), (20, 130), (45, 45)) if False else None
    f.wire((215, 45), (235, 45), (235, 130), (20, 130), (20, 45), (45, 45))
    f.node(20, 45)
    f.node(20, 130)
    f.arrow(20, 130, 20, 45, "U")
    f.txt(130, 20, "szeregowo", "middle", 12, italic=True)
    f.txt(130, 158, "R = R₁ + R₂   I = const,  U dzieli się", "middle", 11)

    # --- równoległe
    f.wire((310, 45), (310, 130))
    f.wire((310, 45), (490, 45))
    f.wire((310, 130), (490, 130))
    f.node(310, 45)
    f.node(310, 130)
    f.arrow(310, 130, 310, 45, "")
    f.txt(296, 92, "U", "end", 13)
    f.res(370, 45, 370, 130, "R", "1", side=1)
    f.res(440, 45, 440, 130, "R", "2", side=1)
    f.node(370, 45)
    f.node(370, 130)
    f.txt(400, 20, "równolegle", "middle", 12, italic=True)
    f.txt(400, 158, "1/R = 1/R₁ + 1/R₂   U = const,  I dzieli się", "middle", 11)
    return save("szeregowo_rownolegle.svg", f)

# ------------------------------------------------------------- 3. dzielniki
def f_dzielniki():
    f = Fig(520, 215)
    f.vsrc(50, 10, 50, 40, "E")
    f.wire((50, 40), (50, 55))
    f.res(50, 55, 50, 110, "R", "1", side=-1)
    f.node(50, 110)
    f.res(50, 110, 50, 170, "R", "2", side=1)
    f.wire((50, 170), (50, 195), (50, 10))
    f.wire((50, 110), (150, 110))
    f.node(50, 110)
    f.txt(158, 105, "U₂ = E·R₂/(R₁+R₂)", "start", 12)
    f.txt(50, 212, "dzielnik napięcia", "middle", 11, italic=True)

    # dzielnik prądu
    f.items.append('<circle cx="300" cy="100" r="10" class="symf"/>')
    f.items.append('<line x1="300" y1="106" x2="300" y2="94" class="sym"/>')
    f.items.append('<polyline points="297,97 300,93 303,97" class="sym"/>')
    f.txt(300, 128, "J", "middle", 12)
    f.wire((300, 90), (300, 45))
    f.wire((300, 110), (300, 165))
    f.wire((300, 45), (480, 45))
    f.wire((300, 165), (480, 165))
    f.node(300, 45)
    f.node(300, 165)
    f.res(380, 45, 380, 165, "R", "1", side=-1)
    f.res(450, 45, 450, 165, "R", "2", side=1)
    f.node(380, 45)
    f.node(380, 165)
    f.txt(390, 30, "I₁ = J·R₂/(R₁+R₂)", "start", 12)
    f.txt(380, 212, "dzielnik prądu", "middle", 11, italic=True)
    return save("dzielniki.svg", f)

# ------------------------------------- 4. dwójnik ze źródłem sterowanym (NIC)
def f_dwojnik_ster():
    f = Fig(520, 215)
    f.txt(40, 40, "A", "middle", 13)
    f.txt(40, 190, "B", "middle", 13)
    f.node(55, 40)
    f.node(55, 190)
    f.wire((55, 40), (160, 40))
    f.wire((55, 190), (160, 190))
    f.node(160, 40)
    f.node(160, 190)
    f.wire((160, 40), (160, 62))
    f.res(160, 62, 160, 120, "R", "", side=-1)
    f.wire((160, 120), (160, 190))
    f.wire((160, 40), (285, 40))
    f.wire((285, 40), (285, 62))
    f.dsrc(285, 62, 285, 120, "", "", side=1, kind="I")
    f.wire((285, 120), (285, 190))
    f.wire((285, 190), (160, 190))
    f.node(285, 40)
    f.arrow(160, 26, 285, 26, "")
    f.txt(222, 18, "u", "middle", 12)
    f.txt(298, 95, "g·u", "start", 12)
    f.txt(330, 70, "R_z = u/i = 1/(G − g)", "start", 13)
    f.txt(330, 92, "G = 1/R,  g — transkonduktancja", "start", 11)
    f.txt(330, 120, "g > G  ⇒  R_z < 0", "start", 12)
    f.txt(330, 150, "dwójnik aktywny (NIC)", "start", 11, italic=True)
    f.txt(160, 210, "dwójnik ze źródłem sterowanym", "middle", 11, italic=True)
    return save("dwojnik_sterowany.svg", f)

# ---------------------------------------------------- 5. Thévenin / Norton
def f_thevenin():
    f = Fig(520, 200)
    f.txt(30, 55, "A", "middle", 13)
    f.txt(30, 160, "B", "middle", 13)
    f.node(45, 55)
    f.node(45, 160)
    f.wire((45, 55), (110, 55))
    f.wire((45, 160), (110, 160))
    f.res(110, 55, 110, 105, "R", "w", side=-1)
    f.vsrc(110, 105, 110, 160, "E", "", side=-1, plus=1)
    f.txt(78, 190, "dwójnik liniowy", "middle", 11, italic=True)
    f.txt(215, 100, "≡", "middle", 20)

    f.txt(250, 55, "A", "middle", 13)
    f.txt(250, 160, "B", "middle", 13)
    f.node(265, 55)
    f.node(265, 160)
    f.wire((265, 55), (330, 55))
    f.wire((265, 160), (330, 160))
    f.res(330, 55, 330, 105, "R", "T", side=1)
    f.vsrc(330, 105, 330, 160, "E", "T", side=1, plus=1)
    f.txt(300, 190, "Thévenin", "middle", 11, italic=True)

    f.txt(400, 55, "A", "middle", 13)
    f.txt(400, 160, "B", "middle", 13)
    f.node(415, 55)
    f.node(415, 160)
    f.wire((415, 55), (495, 55))
    f.wire((415, 160), (495, 160))
    f.res(480, 55, 480, 105, "R", "T", side=-1)
    f.isrc(480, 105, 480, 160, "", "", side=1)
    f.txt(452, 130, "J", "end", 13)
    f.txt(455, 190, "Norton", "middle", 11, italic=True)
    f.txt(260, 30, "E_T = J_N·R_T", "middle", 12)
    return save("thevenin_norton.svg", f)

# ------------------------------------------------ 6. punkt pracy nieliniowego
def f_nieliniowy():
    f = Fig(430, 230)
    # axes
    x0, y0 = 60, 190
    f.arrow(x0, y0, 220, y0, "")
    f.arrow(x0, y0, x0, 20, "")
    f.txt(215, 208, "u", "middle", 12, italic=True)
    f.txt(48, 30, "i", "middle", 12, italic=True)
    # nonlinear characteristic (monotonic, saturating-ish)
    f.items.append(
        '<path d="M60,190 C 90,186 105,150 130,90 C 142,62 150,52 175,44" '
        'class="sym" stroke-width="2"/>'
    )
    # load line: i = (E - u)/Rw
    f.items.append('<line x1="60" y1="70" x2="185" y2="190" class="sym" stroke-dasharray="5 4"/>')
    f.node(130, 90, 3.4)
    f.txt(140, 84, "P", "start", 12)
    # asymptote (dynamic resistance tangent)
    f.items.append('<line x1="98" y1="112" x2="175" y2="84" class="symr" stroke-width="1.1"/>')
    f.txt(178, 100, "styczna: R_d", "start", 11)
    f.items.append('<line x1="60" y1="90" x2="130" y2="90" class="sym" stroke-dasharray="3 3" stroke-width="0.9"/>')
    f.items.append('<line x1="130" y1="90" x2="130" y2="190" class="sym" stroke-dasharray="3 3" stroke-width="0.9"/>')
    f.txt(52, 94, "I", "end", 12, italic=True)
    f.txt(130, 205, "U", "middle", 12, italic=True)
    f.txt(60, 60, "E/R_w", "start", 11)
    # right: definitions
    f.txt(250, 50, "opór statyczny", "start", 12)
    f.txt(250, 68, "R_s = U / I", "start", 13)
    f.txt(250, 100, "opór dynamiczny", "start", 12)
    f.txt(250, 118, "R_d = du / di  w P", "start", 13)
    f.txt(250, 150, "prosta obciążenia:", "start", 12)
    f.txt(250, 168, "i = (E − u) / R_w", "start", 13)
    f.txt(250, 200, "przecięcie ⇒ punkt pracy P", "start", 11, italic=True)
    return save("nieliniowy.svg", f)


# ------------------------------------------------------------- 7. mostek
def f_mostek():
    f = Fig(520, 240)
    A, Bp, L, R = (260, 30), (260, 190), (90, 110), (430, 110)
    f.txt(260, 20, "A", "middle", 13)
    f.txt(260, 212, "B", "middle", 13)
    f.res(L[0], L[1], A[0], A[1], "R", "1", side=-1)
    f.res(A[0], A[1], R[0], R[1], "R", "2", side=-1)
    f.res(L[0], L[1], Bp[0], Bp[1], "R", "0", side=1)
    f.res(R[0], R[1], Bp[0], Bp[1], "R", "x", side=1)
    for p in (L, R, A, Bp):
        f.node(*p)
    f.items.append('<line x1="90" y1="110" x2="430" y2="110" class="sym" stroke-dasharray="4 4" stroke-width="1"/>')
    f.items.append('<circle cx="260" cy="110" r="12" class="symf"/>')
    f.txt(260, 115, "G", "middle", 11)
    f.txt(260, 138, "galwanometr", "middle", 10, italic=True)
    f.txt(260, 160, "U_AB zasila mostek", "middle", 10, italic=True)
    f.txt(260, 235, "równowaga (I_G = 0):  R₁·R_x = R₂·R₀   ⇒   R_x = R₀·R₂/R₁", "middle", 12)
    return save("mostek.svg", f)

# ------------------------------------------- 8. metoda techniczna (2 układy)
def f_metoda_techniczna():
    f = Fig(520, 215)
    # a) poprawny pomiar napięcia
    f.txt(20, 22, "a) poprawny pomiar napięcia", "start", 11, italic=True)
    f.wire((30, 45), (30, 175), (75, 175), (75, 45), (40, 45))
    f.items.append('<circle cx="52" cy="45" r="11" class="symf"/>')
    f.txt(52, 50, "A", "middle", 11)
    f.wire((63, 45), (110, 45))
    f.res(110, 45, 110, 100, "R", "x", side=1)
    f.wire((110, 100), (110, 140))
    f.wire((110, 140), (75, 140)) if False else None
    f.node(30, 110)
    f.node(110, 110)
    f.wire((30, 110), (60, 110))
    f.items.append('<circle cx="78" cy="110" r="11" class="symf"/>')
    f.txt(78, 115, "V", "middle", 11)
    f.wire((89, 110), (110, 110))
    f.txt(20, 200, "R = U/I — woltomierz mierzy U na R_x,", "start", 10)
    f.txt(20, 213, "amperomierz mierzy I przez R_x.", "start", 10)

    # b) poprawny pomiar prądu
    f.txt(255, 22, "b) poprawny pomiar prądu", "start", 11, italic=True)
    f.wire((265, 60), (285, 60))
    f.items.append('<circle cx="305" cy="60" r="11" class="symf"/>')
    f.txt(305, 65, "A", "middle", 11)
    f.wire((316, 60), (345, 60))
    f.res(345, 60, 345, 130, "R", "x", side=-1)
    f.wire((345, 130), (345, 160), (265, 160), (265, 60))
    f.node(335, 60)
    f.node(335, 130)
    f.items.append('<circle cx="400" cy="95" r="11" class="symf"/>')
    f.txt(400, 100, "V", "middle", 11)
    f.wire((335, 60), (385, 60), (385, 95))
    f.wire((411, 95), (430, 95), (430, 60), (345, 60)) if False else None
    f.wire((411, 95), (430, 95), (430, 130), (345, 130))
    f.node(345, 130) if False else None
    f.txt(255, 200, "R = U/I — woltomierz mierzy U na (R_x + R_A),", "start", 10)
    f.txt(255, 213, "amperomierz mierzy tylko I przez R_x.", "start", 10)
    return save("metoda_techniczna.svg", f)

# ---------------------------------------- 9. niepewność przyrządu cyfrowego
def f_niepewnosc():
    f = Fig(430, 210)
    ax_y = 170
    # panel 1: Δg(x)
    f.arrow(50, ax_y, 195, ax_y, "")
    f.arrow(50, ax_y, 50, 30, "")
    f.txt(190, 188, "|x|", "middle", 11, italic=True)
    f.txt(38, 34, "Δg", "middle", 11, italic=True)
    f.items.append('<line x1="50" y1="150" x2="180" y2="90" class="sym" stroke-width="2"/>')
    f.items.append('<line x1="50" y1="150" x2="50" y2="90" class="sym" stroke-width="2" opacity="0"/>')
    f.txt(115, 205, "Δg rośnie z |x|", "middle", 10)

    # panel 2: δg(x)
    f.arrow(265, ax_y, 410, ax_y, "")
    f.arrow(265, ax_y, 265, 30, "")
    f.txt(405, 188, "|x|", "middle", 11, italic=True)
    f.txt(250, 34, "δg", "middle", 11, italic=True)
    f.items.append('<path d="M285,45 C 320,140 350,158 395,163" class="sym" stroke-width="2"/>')
    f.items.append('<line x1="285" y1="163" x2="395" y2="163" class="sym" stroke-dasharray="4 3" stroke-width="1"/>')
    f.txt(392, 156, "a", "end", 10)
    f.txt(330, 205, "δg maleje z |x|, dąży do a", "middle", 10)
    return save("niepewnosc_wykresy.svg", f)


# ------------------------------------------ 10. sprzężenie wejścia oscyloskopu
def f_sprzezenie():
    import math
    f = Fig(520, 230)
    f.arrow(30, 150, 250, 150, "")
    f.arrow(30, 150, 30, 30, "")
    f.wire((30, 150), (30, 55), (250, 55)) if False else None
    pts = []
    for k in range(0, 221):
        x = 30 + k
        y = 95 - 7 * math.sin(x / 7.0)
        pts.append(f"{x},{y:.1f}")
    f.items.append(f'<polyline points="{" ".join(pts)}" class="sym" stroke-width="1.6"/>')
    f.items.append('<line x1="30" y1="95" x2="250" y2="95" class="sym" stroke-dasharray="4 3" stroke-width="1"/>')
    f.txt(240, 40, "u(t)", "middle", 11, italic=True)
    f.txt(18, 60, "5 V", "end", 10)
    f.txt(18, 100, "0", "end", 10)
    f.txt(138, 185, "duża składowa stała + mała składowa zmienna", "middle", 10, italic=True)

    f.wire((300, 95), (340, 95))
    f.cap(340, 95, 380, 95, "", "")
    f.wire((380, 95), (430, 95))
    f.txt(360, 78, "C", "middle", 11)
    f.txt(300, 70, "AC", "middle", 10)
    f.txt(430, 140, "wejście oscyloskopu", "middle", 10)
    f.txt(20, 205, "AC: składowa stała odcięta → widać małą składową zmienną w pełnej skali", "start", 10)
    f.txt(20, 222, "DC: widoczne obie składowe;  GND: wejście na masę (poziom odniesienia)", "start", 10)
    return save("sprzezenie.svg", f)

# --------------------------------------------------- 11. łączenie źródeł
def f_zrodla():
    f = Fig(520, 200)
    f.txt(95, 18, "a) szeregowo:  E = E₁ + E₂", "middle", 10, italic=True)
    f.wire((30, 40), (40, 40))
    f.items.append('<circle cx="52" cy="40" r="11" class="symf"/>')
    f.txt(52, 45, "E₁", "middle", 9)
    f.wire((63, 40), (80, 40))
    f.items.append('<circle cx="92" cy="40" r="11" class="symf"/>')
    f.txt(92, 45, "E₂", "middle", 9)
    f.wire((103, 40), (120, 40), (120, 105), (30, 105), (30, 40))

    f.txt(390, 18, "b) równolegle:  J = J₁ + J₂", "middle", 10, italic=True)
    f.wire((330, 40), (450, 40))
    f.wire((330, 105), (450, 105))
    for x in (350, 430):
        f.items.append(f'<circle cx="{x}" cy="72" r="11" class="symf"/>')
        f.items.append(f'<line x1="{x}" y1="78" x2="{x}" y2="66" class="sym"/>')
        f.items.append(f'<polyline points="{x-3},{69} {x},{65} {x+3},{69}" class="sym"/>')
        f.wire((x, 40), (x, 61))
        f.wire((x, 83), (x, 105))
    f.txt(340, 32, "J₁", "start", 9)
    f.txt(440, 32, "J₂", "start", 9)

    f.txt(20, 145, "Niedozwolone: dwa idealne źródła napięciowe równolegle (sprzeczność z NPK),", "start", 10)
    f.txt(20, 160, "dwa idealne źródła prądowe szeregowo (sprzeczność z PPK).", "start", 10)
    f.txt(20, 182, "Rzeczywiste źródła łączyć można — mają opór/przewodność wewnętrzną.", "start", 10, italic=True)
    return save("zrodla_laczenie.svg", f)

# ------------------------------------------------------ 12. gwiazda/trójkąt
def f_gwiazda():
    f = Fig(520, 215)
    A, B, C = (120, 35), (60, 165), (180, 165)
    f.txt(120, 25, "A", "middle", 12)
    f.txt(46, 178, "B", "middle", 12)
    f.txt(194, 178, "C", "middle", 12)
    f.res(A[0], A[1], B[0], B[1], "R", "AB", side=-1)
    f.res(B[0], B[1], C[0], C[1], "R", "BC", side=1)
    f.res(C[0], C[1], A[0], A[1], "R", "CA", side=1)
    f.txt(120, 205, "trójkąt (Δ)", "middle", 10, italic=True)
    f.txt(260, 105, "≡", "middle", 22)

    A2, B2, C2 = (390, 35), (330, 165), (450, 165)
    S = (390, 120)
    f.txt(390, 25, "A", "middle", 12)
    f.txt(316, 178, "B", "middle", 12)
    f.txt(464, 178, "C", "middle", 12)
    f.txt(400, 128, "S", "start", 11)
    f.wire(A2, S)
    f.wire(B2, (S[0]-0, S[1])) if False else None
    f.wire((S[0], S[1]), (S[0]-30, S[1]+22))
    f.wire((S[0], S[1]), (S[0]+30, S[1]+22))
    f.wire((S[0]-30, S[1]+22), B2)
    f.wire((S[0]+30, S[1]+22), C2)
    f.res(B2[0]+30, B2[1]-12, S[0]-30, S[1]+10, "R", "B", side=-1)
    f.res(S[0]+30, S[1]+10, C2[0]-30, C2[1]-12, "R", "C", side=1)
    f.res(A2[0], A2[1]+12, S[0], S[1]-12, "R", "A", side=1)
    f.node(*S)
    f.txt(390, 205, "gwiazda (Y)", "middle", 10, italic=True)
    f.txt(390, 190, "R_A R_B R_C  ⇄  R_AB R_BC R_CA", "middle", 9)
    return save("gwiazda_trojkat.svg", f)

# ------------------------------------------------------------- 13. dioda
def f_dioda():
    f = Fig(430, 200)
    # characteristic of ideal diode
    f.arrow(50, 150, 190, 150, "")
    f.arrow(110, 150, 110, 30, "")
    f.txt(185, 168, "u", "middle", 11, italic=True)
    f.txt(96, 34, "i", "middle", 11, italic=True)
    f.items.append('<line x1="110" y1="150" x2="110" y2="45" class="sym" stroke-width="2.2"/>')
    f.items.append('<line x1="110" y1="150" x2="180" y2="150" class="sym" stroke-width="2.2"/>')
    f.txt(120, 62, "przewodzi (zwarcie)", "start", 10)
    f.txt(150, 165, "zaporowo (rozwar cie)", "start", 10)
    f.txt(105, 190, "dioda idealna zwarciowo-rozwarciowa", "middle", 10, italic=True)

    # circuit with diode
    f.txt(250, 40, "D w gałęzi ⇒ dwa przypadki:", "start", 11, italic=True)
    f.txt(250, 62, "1) D przewodzi  →  zwarcie,", "start", 10)
    f.txt(250, 78, "   sprawdź i_D > 0,", "start", 10)
    f.txt(250, 100, "2) D zaporowa  →  rozwarcie,", "start", 10)
    f.txt(250, 116, "   sprawdź u_D < 0.", "start", 10)
    f.txt(250, 146, "Charakterystyka dwójnika =", "start", 10)
    f.txt(250, 162, "złożenie obu przypadków", "start", 10)
    return save("dioda.svg", f)


if __name__ == "__main__":
    print(f_konwencje())
    print(f_szereg_rown())
    print(f_dzielniki())
    print(f_dwojnik_ster())
    print(f_thevenin())
    print(f_nieliniowy())
    print(f_mostek())
    print(f_metoda_techniczna())
    print(f_niepewnosc())
    print(f_sprzezenie())
    print(f_zrodla())
    print(f_gwiazda())
    print(f_dioda())
