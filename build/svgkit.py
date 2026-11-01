"""Minimal SVG schematic toolkit for the PELP1 compendium.

European (IEC) symbols: resistor = rectangle, capacitor = two parallel lines,
inductor = arcs, ideal voltage source = circle with +/-, ideal current source =
circle with arrow, dependent source = diamond, diode = triangle + bar.

All coordinates are user units (1 unit = 1 px in the viewBox).
"""

from __future__ import annotations


def esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


class Fig:
    def __init__(self, w: int, h: int, cls: str = "sch"):
        self.w, self.h = w, h
        self.cls = cls
        self.items: list[str] = []

    # ------------------------------------------------------------------ wires
    def wire(self, *pts, w: float = 1.4):
        d = " ".join(f"{x},{y}" for x, y in pts)
        self.items.append(
            f'<polyline points="{d}" class="wi" stroke-width="{w}"/>'
        )
        return self

    def node(self, x, y, r=3.0):
        self.items.append(f'<circle cx="{x}" cy="{y}" r="{r}" class="nd"/>')
        return self

    # ------------------------------------------------------------ two-terminals
    def _leads(self, x1, y1, x2, y2, half):
        """wire stubs from the terminals to the symbol body, return body centre"""
        import math

        L = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
        a = (cx - ux * half, cy - uy * half)
        b = (cx + ux * half, cy + uy * half)
        self.wire((x1, y1), a)
        self.wire(b, (x2, y2))
        return cx, cy, ux, uy, L

    def res(self, x1, y1, x2, y2, label="", sub="", side=1, half=13, box=9):
        cx, cy, ux, uy, L = self._leads(x1, y1, x2, y2, half)
        horiz = abs(uy) < abs(ux)
        if horiz:
            self.items.append(
                f'<rect x="{cx-half}" y="{cy-box/2}" width="{2*half}" '
                f'height="{box}" class="bx"/>'
            )
        else:
            self.items.append(
                f'<rect x="{cx-box/2}" y="{cy-half}" width="{box}" '
                f'height="{2*half}" class="bx"/>'
            )
        if label:
            self.label(cx, cy, label, sub, side, horiz, off=box / 2 + 15)
        return self

    def cap(self, x1, y1, x2, y2, label="", sub="", side=1, gap=5, plate=11):
        cx, cy, ux, uy, L = self._leads(x1, y1, x2, y2, gap)
        horiz = abs(uy) < abs(ux)
        if horiz:
            self.items.append(f'<line x1="{cx-gap}" y1="{cy-plate}" x2="{cx-gap}" y2="{cy+plate}" class="sym"/>')
            self.items.append(f'<line x1="{cx+gap}" y1="{cy-plate}" x2="{cx+gap}" y2="{cy+plate}" class="sym"/>')
        else:
            self.items.append(f'<line x1="{cx-plate}" y1="{cy-gap}" x2="{cx+plate}" y2="{cy-gap}" class="sym"/>')
            self.items.append(f'<line x1="{cx-plate}" y1="{cy+gap}" x2="{cx+plate}" y2="{cy+gap}" class="sym"/>')
        if label:
            self.label(cx, cy, label, sub, side, horiz, off=plate + 6)
        return self

    def ind(self, x1, y1, x2, y2, label="", sub="", side=1, half=15, n=4):
        import math

        cx, cy, ux, uy, L = self._leads(x1, y1, x2, y2, half)
        horiz = abs(uy) < abs(ux)
        r = half / n
        d = f"M {cx-half} {cy} "
        for k in range(n):
            x0 = cx - half + 2 * r * k
            if horiz:
                d += f"A {r} {r} 0 0 1 {x0+2*r} {cy} "
            else:
                pass
        if horiz:
            self.items.append(f'<path d="{d}" class="sym"/>')
        else:
            d = f"M {cx} {cy-half} "
            for k in range(n):
                y0 = cy - half + 2 * r * k
                d += f"A {r} {r} 0 0 1 {cx} {y0+2*r} "
            self.items.append(f'<path d="{d}" class="sym"/>')
        if label:
            self.label(cx, cy, label, sub, side, horiz, off=r + 8)
        return self

    def vsrc(self, x1, y1, x2, y2, label="", sub="", side=1, r=10, plus=None):
        cx, cy, ux, uy, L = self._leads(x1, y1, x2, y2, r)
        self.items.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" class="sym"/>')
        # polarity along the segment: plus toward (x2,y2) unless told otherwise
        s = 1 if plus is None else plus
        if abs(uy) < abs(ux):
            xm = cx + s * 4.2
            self.items.append(f'<line x1="{xm-3.5}" y1="{cy}" x2="{xm+3.5}" y2="{cy}" class="sym"/>')
            self.items.append(f'<line x1="{xm}" y1="{cy-3.5}" x2="{xm}" y2="{cy+3.5}" class="sym"/>')
            self.items.append(f'<line x1="{cx-s*4.2-3.5}" y1="{cy}" x2="{cx-s*4.2+3.5}" y2="{cy}" class="sym"/>')
        else:
            ym = cy + s * 4.2  # in svg y grows down
            self.items.append(f'<line x1="{cx-3.5}" y1="{ym}" x2="{cx+3.5}" y2="{ym}" class="sym"/>')
            self.items.append(f'<line x1="{cx}" y1="{ym-3.5}" x2="{cx}" y2="{ym+3.5}" class="sym"/>')
            self.items.append(f'<line x1="{cx-3.5}" y1="{cy-s*4.2}" x2="{cx+3.5}" y2="{cy-s*4.2}" class="sym"/>')
        if label:
            self.label(cx, cy, label, sub, side, abs(uy) < abs(ux), off=r + 6)
        return self

    def isrc(self, x1, y1, x2, y2, label="", sub="", side=1, r=10, up=True):
        cx, cy, ux, uy, L = self._leads(x1, y1, x2, y2, r)
        self.items.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" class="sym"/>')
        if abs(uy) < abs(ux):
            # arrow points up inside the circle (current direction convention: J upward)
            self.items.append(
                f'<line x1="{cx}" y1="{cy+5.5}" x2="{cx}" y2="{cy-5.5}" class="sym"/>'
                f'<polyline points="{cx-3},{cy-2.5} {cx},{cy-5.8} {cx+3},{cy-2.5}" class="sym"/>'
            )
        else:
            self.items.append(
                f'<line x1="{cx}" y1="{cy+5.5}" x2="{cx}" y2="{cy-5.5}" class="sym"/>'
                f'<polyline points="{cx-3},{cy-2.5} {cx},{cy-5.8} {cx+3},{cy-2.5}" class="sym"/>'
            )
        if label:
            self.label(cx, cy, label, sub, side, abs(uy) < abs(ux), off=r + 6)
        return self

    def dsrc(self, x1, y1, x2, y2, label="", sub="", side=1, r=13, kind="V"):
        """dependent source: diamond with +/-, or with arrow for current type"""
        cx, cy, ux, uy, L = self._leads(x1, y1, x2, y2, r)
        self.items.append(
            f'<polygon points="{cx},{cy-r} {cx+r},{cy} {cx},{cy+r} {cx-r},{cy}" class="symf"/>'
        )
        if kind == "V":
            self.items.append(f'<line x1="{cx-4}" y1="{cy}" x2="{cx+4}" y2="{cy}" class="sym"/>')
            self.items.append(f'<line x1="{cx}" y1="{cy-4}" x2="{cx}" y2="{cy+4}" class="sym"/>')
        else:
            self.items.append(
                f'<line x1="{cx}" y1="{cy+4.5}" x2="{cx}" y2="{cy-4.5}" class="sym"/>'
                f'<polyline points="{cx-2.6},{cy-2} {cx},{cy-5} {cx+2.6},{cy-2}" class="sym"/>'
            )
        if label:
            self.label(cx, cy, label, sub, side, abs(uy) < abs(ux), off=r + 6)
        return self

    def diode(self, x1, y1, x2, y2, label="", sub="", side=1, half=8):
        cx, cy, ux, uy, L = self._leads(x1, y1, x2, y2, half)
        # anode at (x1,y1), cathode toward (x2,y2)
        if abs(uy) < abs(ux):
            s = 1 if (x2 - x1) > 0 else -1
            self.items.append(
                f'<polygon points="{cx-s*half},{cy-7} {cx-s*half},{cy+7} {cx+s*half},{cy}" class="symf"/>'
            )
            self.items.append(f'<line x1="{cx+s*half}" y1="{cy-7}" x2="{cx+s*half}" y2="{cy+7}" class="sym"/>')
        else:
            s = 1 if (y2 - y1) > 0 else -1
            self.items.append(
                f'<polygon points="{cx-7},{cy-s*half} {cx+7},{cy-s*half} {cx},{cy+s*half}" class="symf"/>'
            )
            self.items.append(f'<line x1="{cx-7}" y1="{cy+s*half}" x2="{cx+7}" y2="{cy+s*half}" class="sym"/>')
        if label:
            self.label(cx, cy, label, sub, side, abs(uy) < abs(ux), off=half + 6)
        return self

    # ------------------------------------------------------------------ extras
    def ground(self, x, y):
        self.wire((x, y), (x, y + 6))
        for i, wdt in enumerate((12, 8, 4)):
            self.items.append(
                f'<line x1="{x-wdt/2}" y1="{y+6+i*4}" x2="{x+wdt/2}" y2="{y+6+i*4}" class="sym"/>'
            )
        return self

    def txt(self, x, y, s, anchor="middle", size=12, cls="lb", rot=None, italic=False, raw=False):
        if not raw:
            s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        s = "".join(c if ord(c) < 128 else f"&#{ord(c)};" for c in s)
        style = ' font-style="italic"' if italic else ""
        tr = f' transform="rotate({rot} {x} {y})"' if rot is not None else ""
        self.items.append(
            f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" '
            f'font-size="{size}"{style}{tr}>{s}</text>'
        )
        return self

    def label(self, cx, cy, main, sub, side, horiz, off):
        """main label with optional subscript placed beside the symbol"""
        html = esc(main)
        if sub:
            html += f'<tspan font-size="0.75em" dy="3">{esc(sub)}</tspan>'
        if horiz:
            y = cy - off if side <= 0 else cy + off + 4
            self.txt(cx, y, html, "middle", 13, raw=True)
        else:
            x = cx + off if side >= 0 else cx - off
            anchor = "start" if side >= 0 else "end"
            self.txt(x, cy + 4, html, anchor, 13, raw=True)
        return self

    def arrow(self, x1, y1, x2, y2, label="", sub="", at="mid", off=14, size=12):
        """dimension/quantity arrow (thin, with head)"""
        self.items.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="qa" '
            f'marker-end="url(#ah)"/>'
        )
        if label:
            if at == "mid":
                x, y = (x1 + x2) / 2, (y1 + y2) / 2
            else:
                x, y = x2, y2
            horiz = abs(y2 - y1) < abs(x2 - x1)
            if horiz:
                self.txt(x, y - 6 + (off - 14), label, "middle", size)
            else:
                self.txt(x + 10, y + 4, label, "start", size)
        return self

    def vlabel(self, x, y, s, anchor="start", size=12):
        return self.txt(x, y, s, anchor, size)

    CLS = {
        "wi": 'stroke="#1f2937" fill="none" stroke-linecap="round"',
        "sym": 'stroke="#1f2937" fill="none"',
        "symf": 'stroke="#1f2937" fill="#ffffff"',
        "symr": 'stroke="#b91c1c" fill="none"',
        "bx": 'stroke="#1f2937" fill="#ffffff" stroke-width="1.5"',
        "nd": 'fill="#1f2937"',
        "lb": 'fill="#111827" font-family="Arial,Helvetica,sans-serif"',
        "qa": 'stroke="#b91c1c" fill="none" stroke-width="1.2"',
        "ttl": 'fill="#1f2937" font-family="Arial,Helvetica,sans-serif" font-weight="600"',
    }

    def render(self) -> str:
        defs = (
            '<defs><marker id="ah" viewBox="0 0 8 8" refX="7" refY="4" '
            'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            '<path d="M0,0 L8,4 L0,8 z" fill="#b91c1c"/></marker></defs>'
        )
        body = "".join(self.items)
        for k, v in self.CLS.items():
            body = body.replace(f'class="{k}"', v)
        return (
            f'<svg viewBox="0 0 {self.w} {self.h}" '
            f'width="{self.w}" height="{self.h}" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">'
            f"{defs}{body}</svg>"
        )


def sub(prefix: str, idx) -> str:
    return f"{prefix}<tspan baseline-shift='sub' font-size='0.7em'>{idx}</tspan>"
