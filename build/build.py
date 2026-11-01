#!/usr/bin/env python3
"""Buduje kompendium: Markdown -> pojedynczy, samodzielny plik HTML.

Cechy:
  * ochrona wzorów $...$ / $$...$$ przed przetwarzaniem przez Markdown,
  * bloki ::: nazwa Tytuł ... :::  -> kolorowe ramki (definicja, wzór, pułapka...),
  * ::: figura plik | podpis :::   -> rysunek z podpisem,
  * spis treści generowany z nagłówków,
  * automatycznie generowany aneks z bankiem 252 pytań z kluczy PDF.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys

import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
KOMP = os.path.join(ROOT, "kompendium")
SRC = os.path.join(KOMP, "kompendium.md")
OUT = os.path.join(KOMP, "index.html")
KATEX_SRC = "/home/user/buildtools/node_modules/katex/dist"
KATEX_DST = os.path.join(KOMP, "katex")

# --------------------------------------------------------------------- tematy
# etykieta z ekstrakcji pytań -> (numer sekcji, nazwa rozdziału w kompendium)
TOPICS = {
    "Opór zastępczy dwójnika (ze źródłami sterowanymi)": ("1.6", "Rezystancja zastępcza i dwójniki ze źródłami sterowanymi"),
    "Punkt pracy elementu nieliniowego (Rs, Rd)": ("4.1", "Element nieliniowy: opór statyczny i dynamiczny"),
    "Charakterystyka dwójnika z diodą idealną": ("4.3", "Dioda idealna i dwójniki z diodą"),
    "Moc maksymalna wydzielana w R (dopasowanie)": ("3.4", "Dopasowanie odbiornika i moc dysponowana"),
    "Moc dysponowana dwójnika": ("3.4", "Dopasowanie odbiornika i moc dysponowana"),
    "Równoważnik Thévenina / Nortona": ("3.3", "Twierdzenie Thévenina i Nortona"),
    "Zasada superpozycji": ("3.1", "Zasada superpozycji"),
    "Napięcie w obwodzie (obliczenia)": ("2.2", "Metody analizy obwodów"),
    "Napięcie/prąd źródła – wpływ parametrów": ("2.2", "Metody analizy obwodów"),
    "Rozpoznawanie połączeń (szeregowo/równolegle, gwiazda/trójkąt)": ("1.6", "Rezystancja zastępcza i dwójniki ze źródłami sterowanymi"),
    "Prądowe prawo Kirchhoffa": ("2.1", "Prawa Kirchhoffa w praktyce"),
    "Równania Kirchhoffa (węzeł / oczko)": ("2.1", "Prawa Kirchhoffa w praktyce"),
    "Elementy skupione – założenia": ("1.2", "Model elementu skupionego"),
    "Charakterystyki napięciowo-prądowe": ("4.1", "Element nieliniowy: opór statyczny i dynamiczny"),
    "Czwórnik": ("5.2", "Czwórniki"),
    "Zasada Tellegena": ("3.2", "Zasada Tellegena"),
    "Łączenie źródeł idealnych": ("2.3", "Źródła rzeczywiste i łączenie źródeł"),
    "Dwójnik bezźródłowy / źródłowy": ("5.1", "Klasyfikacja dwójników"),
    "Moc w połączeniach szereg./równol.": ("1.6", "Rezystancja zastępcza i dwójniki ze źródłami sterowanymi"),
    "Zaokrąglanie wyniku pomiaru": ("6.4", "Zaokrąglanie wyniku i zapis niepewności"),
    "Wykresy niepewności przyrządu cyfrowego": ("7.2", "Przyrządy cyfrowe"),
    "Niepewność złożona – rachunek": ("6.3", "Niepewność złożona — rachunek"),
    "Dobór przyrządu i zakresu": ("7.3", "Dobór przyrządu i zakresu"),
    "Statystyka serii pomiarów": ("6.5", "Opracowanie serii pomiarów"),
    "Oscyloskop – budowa, tryby, ADC": ("9", "Oscyloskop"),
    "Mostek Wheatstone’a": ("8.2", "Mostek Wheatstone’a"),
    "Metoda techniczna i błąd metody": ("8.1", "Metoda techniczna pomiaru rezystancji"),
    "Pojęcia: niepewność i błąd": ("6.1", "Błąd i niepewność — pojęcia podstawowe"),
    "Własności niepewności przyrządów cyfrowych": ("7.2", "Przyrządy cyfrowe"),
    "Rodzaje i metody pomiaru": ("6.2", "Metody pomiarowe"),
    "INNE": ("2.1", "Prawa Kirchhoffa w praktyce"),
    # uzupełnienia z ręcznej klasyfikacji
    "Oscyloskop": ("9", "Oscyloskop"),
    "Obciążenie przyrządem (błąd metody)": ("8.1", "Metoda techniczna pomiaru rezystancji"),
}


# ---------------------------------------------------------------- preprocesor
MATH_RE = re.compile(r"(\$\$.+?\$\$|(?<!\\)\$.+?(?<!\\)\$)", re.S)
BOX_OPEN = re.compile(r"^:::\s*(\w+)(?:\s+(.*))?$")


PL_MAP = str.maketrans(
    "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ", "acelnoszzACELNOSZZ"
)


def slugify(value, separator="-"):
    value = str(value).translate(PL_MAP)
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    return re.sub(r"[-\s]+", separator, value)


def protect_math(text: str):
    store: list[str] = []

    def repl(m):
        store.append(m.group(0))
        return f"\x00MATH{len(store)-1}\x00"

    return MATH_RE.sub(repl, text), store


def render_math(store: list[str], mode: str = "katex") -> list[str]:
    """Renderuje wzory statycznie (bez JS w przeglądarce).

    mode="katex" — HTML+CSS KaTeX-a (wersja do przeglądarki),
    mode="img"   — PNG przez matplotlib mathtext (wersja do PDF).
    """
    src, dst = "/tmp/_math_in.json", "/tmp/_math_out.json"
    with open(src, "w") as f:
        json.dump(store, f, ensure_ascii=False)
    if mode == "katex":
        subprocess.run(["node", os.path.join(HERE, "katex_render.js"), src, dst], check=True)
    else:
        subprocess.run([sys.executable, os.path.join(HERE, "mathpng.py"), src, dst], check=True)
    return json.load(open(dst))


def restore_math(html: str, rendered: list[str]) -> str:
    for i, s in enumerate(rendered):
        html = html.replace(f"\x00MATH{i}\x00", s)
    return html


ICI = {
    "def": ("Definicja", "def"),
    "wzor": ("Wzór", "wzor"),
    "uwaga": ("Uwaga", "uwaga"),
    "pulapka": ("Pułapka", "pulapka"),
    "przyklad": ("Przykład", "przyklad"),
    "metoda": ("Metoda", "metoda"),
    "zapamietaj": ("Zapamiętaj", "zapamietaj"),
    "ciekawostka": ("Kontekst", "ciekawostka"),
    "klucz": ("Klucz odpowiedzi", "klucz"),
}


def md_inline(text: str) -> str:
    """Minimalna obsługa **pogrubień** w tytułach ramek."""
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)


def boxes_and_figures(text: str) -> str:
    out = []
    stack = []
    for line in text.split("\n"):
        m = BOX_OPEN.match(line.strip())
        if m and m.group(1) in ICI:
            kind, title = m.group(1), (m.group(2) or "").strip()
            label, cls = ICI[kind]
            head = title or label
            out.append(f'<div class="box {cls}" markdown="1">')
            out.append(f'<p class="box-title">{md_inline(head)}</p>')
            out.append("")
            stack.append(kind)
            continue
        if m and m.group(1) == "figura":
            spec = (m.group(2) or "").strip()
            spec = re.sub(r"\s*:::\s*$", "", spec)
            path, _, cap = spec.partition("|")
            path, cap = path.strip(), cap.strip()
            alt = re.sub(r"\$[^$]*\$", "", cap)  # alt bez LaTeX-a
            alt = re.sub(r"\s{2,}", " ", alt).replace('"', "&quot;").strip()
            out.append(
                f'<figure><img src="{path}" alt="{alt}" loading="lazy">'
                f"<figcaption>{cap}</figcaption></figure>"
            )
            continue
        if line.strip() == ":::":
            if stack:
                stack.pop()
                out.append("</div>")
            continue
        # listy i cytaty muszą zaczynać się od pustej linii, inaczej Markdown
        # wciąga je do poprzedniego akapitu (widoczne jako literalne "* ")
        if re.match(r"^(\s*)([*+-]|\d+\.)\s", line):
            prev = next((x for x in reversed(out) if x.strip()), "")
            if prev and not re.match(r"^(\s*)([*+-]|\d+\.)\s", prev) and not prev.startswith(("|", "<")):
                out.append("")
        out.append(line)
    assert not stack, f"niedomknięte ramki: {stack}"
    return "\n".join(out)


# ------------------------------------------------------------------- aneks
def build_bank_html() -> str:
    rows = json.load(open(os.path.join(HERE, "bank.json")))
    # rows: [{file, hdr, l, a, stem, lab}]
    tests: dict[str, list] = {}
    for r in rows:
        tests.setdefault(r["hdr"], []).append(r)

    def sort_key(name):
        m = re.search(r"(\d{4})", name)
        return (0 if "Test 1" in name else 1, m.group(1) if m else "", name)

    parts = ['<div class="bank">']
    parts.append(
        '<div class="bank-bar"><input id="qfilter" type="search" '
        'placeholder="Filtruj pytania po słowie (np. Wheatstone, dopasowanie, niepewność)…">'
        '<select id="topicfilter"><option value="">— wszystkie tematy —</option>'
    )
    labs = sorted({r["lab"] for r in rows})
    for lab in labs:
        parts.append(f'<option value="{lab}">{lab}</option>')
    parts.append("</select>")
    parts.append(
        f'<span class="bank-count" id="bankcount">{len(rows)} pytań</span></div>'
    )

    for name in sorted(tests, key=sort_key):
        rows_t = tests[name]
        total = sum(1 for _ in rows_t)
        parts.append(
            f'<details class="testcard"><summary>{name} '
            f'<span class="mini">{total} pytań</span></summary><table class="banktable">'
            "<thead><tr><th>Pyt.</th><th>Pkt</th><th>Temat w kompendium</th>"
            "<th>Odp.</th></tr></thead><tbody>"
        )
        for r in rows_t:
            sec, title = TOPICS.get(r["lab"], TOPICS["INNE"])
            ans = ", ".join(str(x) for x in r["a"])
            parts.append(
                f'<tr data-lab="{r["lab"]}" data-sec="{sec}">'
                f'<td class="c">{r["l"]}</td><td class="c">{"2" if "2p" in r["stem"][:4] else "1"}</td>'
                f'<td><span class="badge">§{sec}</span> {title}'
                f'<div class="tiny">{r["lab"]}</div></td>'
                f'<td class="c"><b>{ans}</b></td></tr>'
            )
        parts.append("</tbody></table></details>")

    parts.append("</div>")
    return "\n".join(parts)


def build_topic_map() -> str:
    rows = json.load(open(os.path.join(HERE, "bank.json")))
    from collections import Counter

    c = Counter(r["lab"] for r in rows)
    parts = [
        '<table class="map"><thead><tr><th>Temat</th><th>Liczba pytań</th>'
        "<th>Gdzie w kompendium</th></tr></thead><tbody>"
    ]
    for lab, n in c.most_common():
        sec, title = TOPICS.get(lab, TOPICS["INNE"])
        bar = int(round(100 * n / max(c.values())))
        parts.append(
            f'<tr><td>{lab}</td><td class="c"><span class="minibar" '
            f'style="width:{bar}%"></span>{n}</td>'
            f'<td><span class="badge">§{sec}</span> {title}</td></tr>'
        )
    parts.append("</tbody></table>")
    return "\n".join(parts)


# ---------------------------------------------------------------------- TOC
def build_toc(html: str, toc_tokens: dict) -> str:
    items = toc_tokens.get("toc", [])
    if not items:
        return ""
    return markdown.markdown(
        toc_tokens["toc_tokens"] and "" or "", extensions=["extra"]
    ) or _toc_from_tokens(toc_tokens["toc_tokens"])


def _toc_from_tokens(tokens) -> str:
    if not tokens:
        return ""
    out = ['<ul class="toc">']
    for t in tokens:
        out.append(
            f'<li><a href="#{t["id"]}" class="lvl{t["level"]}">{t["name"]}</a>'
        )
        if t.get("children"):
            out.append(_toc_from_tokens(t["children"]))
        out.append("</li>")
    out.append("</ul>")
    return "".join(out)


# --------------------------------------------------------------------- main
TEMPLATE = """<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kompendium PELP1 — Podstawy elektroniki i teoria obwodów</title>
<link rel="stylesheet" href="katex/katex.min.css">
<style>
:root{
  --ink:#16202c; --ink-soft:#4a5a6a; --muted:#7b8794;
  --line:#e2e8ee; --bg:#ffffff; --bg-soft:#f6f8fa; --bg-side:#fbfcfd;
  --accent:#0b5fa5; --accent-2:#0e7c86; --warn:#b45309; --danger:#b91c1c;
  --ok:#15803d; --violet:#6d28d9;
  --radius:10px;
  --mono:"SFMono-Regular",ui-monospace,Menlo,Consolas,monospace;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0; background:var(--bg); color:var(--ink);
  font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  -webkit-font-smoothing:antialiased;
}
.layout{display:grid; grid-template-columns:310px minmax(0,1fr); max-width:1500px; margin:0 auto}
/* ---------------- sidebar ---------------- */
nav.side{
  position:sticky; top:0; align-self:start; height:100vh; overflow-y:auto;
  background:var(--bg-side); border-right:1px solid var(--line); padding:22px 18px 60px;
  font-size:13.5px;
}
nav.side h1{font-size:15px; margin:0 0 2px; letter-spacing:.01em}
nav.side .sub{color:var(--muted); font-size:11.5px; margin-bottom:16px; line-height:1.4}
nav.side .toc, nav.side .toc ul{list-style:none; margin:0; padding:0}
nav.side .toc ul{margin-left:10px; border-left:1px solid var(--line); padding-left:8px}
nav.side a{display:block; color:var(--ink-soft); text-decoration:none; padding:3px 6px; border-radius:6px; line-height:1.35}
nav.side a:hover{background:#eef4fa; color:var(--accent)}
nav.side a.lvl2{font-weight:650; color:var(--ink); margin-top:6px}
nav.side a.lvl3{font-size:12.8px}
nav.side a.lvl4{font-size:12.2px; color:var(--muted)}
nav.side a.active{background:#e6f0fa; color:var(--accent); font-weight:600}
/* ---------------- content ---------------- */
main{padding:38px 54px 100px; max-width:1000px}
h1,h2,h3,h4{line-height:1.25; color:var(--ink); scroll-margin-top:18px}
h1{font-size:31px; margin:0 0 6px; letter-spacing:-.015em}
h2{font-size:24px; margin:52px 0 14px; padding-bottom:8px; border-bottom:2px solid var(--line)}
h3{font-size:18.5px; margin:34px 0 10px; color:var(--accent)}
h4{font-size:15.5px; margin:24px 0 8px; color:var(--ink-soft)}
p{margin:.6em 0}
a{color:var(--accent)}
hr{border:0; border-top:1px solid var(--line); margin:36px 0}
small,.tiny{color:var(--muted); font-size:12px}
ul,ol{padding-left:22px; margin:.55em 0}
li{margin:.22em 0}
strong{font-weight:650}
code{font-family:var(--mono); font-size:.88em; background:#f1f4f7; padding:1px 5px; border-radius:4px}
table{border-collapse:collapse; width:100%; margin:14px 0; font-size:14.2px}
th,td{border:1px solid var(--line); padding:7px 9px; text-align:left; vertical-align:top}
th{background:var(--bg-soft); font-weight:650; font-size:13.4px}
tbody tr:nth-child(even){background:#fcfdfe}
td.c,th.c{text-align:center; white-space:nowrap}
/* ---------------- figures ---------------- */
figure{margin:20px 0; padding:14px 14px 6px; border:1px solid var(--line); border-radius:var(--radius);
       background:linear-gradient(180deg,#fdfefe,#f8fafc); text-align:center}
figure img{width:100%; max-width:620px; height:auto}
figcaption{color:var(--muted); font-size:12.8px; margin-top:8px; text-align:center}
/* ---------------- boxes ---------------- */
.box{border-radius:var(--radius); padding:12px 16px 12px 16px; margin:18px 0; border:1px solid var(--line);
     background:var(--bg-soft); border-left:4px solid var(--muted)}
.box p{margin:.45em 0}
.box-title{margin:0 0 6px !important; font-size:11.6px; font-weight:750; letter-spacing:.09em;
           text-transform:uppercase; color:var(--muted)}
.box.def{background:#f2f8fd; border-color:#cfe4f3; border-left-color:#2979b8}
.box.def .box-title{color:#1a6098}
.box.wzor{background:#f7f5ff; border-color:#e0d9fb; border-left-color:#6d28d9}
.box.wzor .box-title{color:#5b21b6}
.box.uwaga{background:#fffbeb; border-color:#f6e6b4; border-left-color:#c98a06}
.box.uwaga .box-title{color:#8a5a00}
.box.pulapka{background:#fdf2f2; border-color:#f6d3d3; border-left-color:#c0392b}
.box.pulapka .box-title{color:#a72b1f}
.box.przyklad{background:#f4faf6; border-color:#cfe8d8; border-left-color:#157f4b}
.box.przyklad .box-title{color:#116b40}
.box.metoda{background:#f2fbfb; border-color:#cceceb; border-left-color:#0e7c86}
.box.metoda .box-title{color:#0a6b73}
.box.zapamietaj{background:#f5f7ff; border-color:#d9def5; border-left-color:#3b4fbe}
.box.zapamietaj .box-title{color:#33429e}
.box.ciekawostka{background:#fafafa; border-color:#e8e8e8; border-left-color:#8b8b8b}
.box.klucz{background:#f0f7f4; border-color:#cfe8dd; border-left-color:#0f766e}
.box.klucz .box-title{color:#0b5f59}
.box.przyklad h4{margin-top:.2em}
/* ---------------- katex ---------------- */
.katex{font-size:1.04em}
.katex-mathml{display:none}
.katex-html{white-space:nowrap}
.katex-display{margin:.85em 0; overflow-x:auto; overflow-y:hidden; padding:2px 0}
/* ---------------- badge / appendix ---------------- */
.badge{display:inline-block; background:#e8f0f8; color:#0b5fa5; border-radius:20px;
       padding:0 7px; font-size:11.5px; font-weight:650; line-height:1.7; white-space:nowrap}
.bank-bar{display:flex; gap:10px; align-items:center; margin:16px 0; flex-wrap:wrap;
          position:sticky; top:0; background:#fff; padding:8px 0; z-index:5; border-bottom:1px solid var(--line)}
.bank-bar input[type=search]{flex:1 1 320px; padding:9px 12px; border:1px solid var(--line);
       border-radius:8px; font-size:14px; font-family:inherit}
.bank-bar select{padding:9px 10px; border:1px solid var(--line); border-radius:8px; font-size:13.5px; font-family:inherit}
.bank-count{color:var(--muted); font-size:12.5px; white-space:nowrap}
details.testcard{border:1px solid var(--line); border-radius:var(--radius); margin:10px 0; background:#fff}
details.testcard>summary{cursor:pointer; padding:10px 14px; font-weight:600; font-size:14px; list-style:none}
details.testcard>summary::-webkit-details-marker{display:none}
details.testcard>summary::before{content:"▸"; color:var(--muted); margin-right:8px; display:inline-block; transition:.15s}
details.testcard[open]>summary::before{transform:rotate(90deg)}
details.testcard[open]>summary{border-bottom:1px solid var(--line); background:var(--bg-soft); border-radius:var(--radius) var(--radius) 0 0}
details.testcard .mini{color:var(--muted); font-weight:400; font-size:12px}
.banktable{margin:0; font-size:13.6px; border:0}
.banktable th{border-left:0; border-right:0}
.banktable td{border-left:0; border-right:0}
table.map td.c{min-width:130px}
.minibar{display:inline-block; height:9px; background:#cfe4f3; border-radius:5px; margin-right:8px; vertical-align:middle}
h2#aneks-klucze ~ .bank, .bank{margin-top:8px}
/* ---------------- misc ---------------- */
.hero{border:1px solid var(--line); border-radius:14px; padding:26px 30px; background:
       radial-gradient(1200px 200px at 10% -30%, #eaf3fb 0%, transparent 70%), #fbfdff; margin-bottom:26px}
.hero .kicker{color:var(--accent); font-size:12px; font-weight:750; letter-spacing:.14em; text-transform:uppercase}
.hero h1{margin-top:6px}
.hero p{color:var(--ink-soft); max-width:74ch}
.meta{display:flex; gap:22px; flex-wrap:wrap; margin-top:14px; font-size:13px; color:var(--muted)}
.meta b{color:var(--ink); font-weight:650}
.lead{font-size:17px; color:var(--ink-soft)}
@media (max-width:1000px){
  .layout{grid-template-columns:1fr}
  nav.side{position:static; height:auto; border-right:0; border-bottom:1px solid var(--line)}
  main{padding:24px 20px 80px}
}
.totop{position:fixed; right:18px; bottom:18px; width:40px; height:40px; border-radius:50%;
  border:1px solid var(--line); background:#fff; color:var(--ink-soft); font-size:17px; cursor:pointer;
  box-shadow:0 2px 10px rgba(16,36,58,.12); opacity:0; pointer-events:none; transition:.2s; z-index:20}
.totop.show{opacity:1; pointer-events:auto}
.totop:hover{color:var(--accent); border-color:#bcd6ea}
@page{size:A4; margin:17mm 15mm}
@media print{
  nav.side{display:none}
  .totop{display:none}
  .layout{grid-template-columns:1fr}
  main{max-width:none; padding:0}
  .box,figure,table,details{break-inside:avoid}
  h2{break-after:avoid}
  a{color:inherit; text-decoration:none}
  .bank-bar{display:none}
  details.testcard>summary{background:#fff !important}
  .hero{background:#fff}
}
</style>
</head>
<body>
<div class="layout">
<nav class="side">
  <h1>Kompendium PELP1</h1>
  <div class="sub">Podstawy elektroniki i teoria obwodów<br>
  na podstawie 35 kluczy kolokwiów (2019–2026)</div>
  __TOC__
  <div class="sub" style="margin-top:18px">Skróty: <b>Ctrl/⌘+F</b> szuka w tekście,
  <b>Ctrl/⌘+P</b> drukuje do PDF.</div>
</nav>
<main>
__BODY__
</main>
</div>
<button class="totop" id="totop" title="Do góry" aria-label="Do góry">↑</button>
<script>
document.addEventListener('DOMContentLoaded', function(){
  // --- podświetlanie aktywnej pozycji spisu treści
  var links = Array.prototype.slice.call(document.querySelectorAll('nav.side a'));
  var map = {};
  links.forEach(function(a){
    var id = decodeURIComponent(a.getAttribute('href').slice(1));
    var el = document.getElementById(id);
    if (el) map[id] = a;
  });
  var obs = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if (e.isIntersecting) {
        links.forEach(function(l){l.classList.remove('active')});
        var a = map[e.target.id]; if (a) a.classList.add('active');
      }
    });
  }, {rootMargin:'-10% 0px -80% 0px'});
  Object.keys(map).forEach(function(id){ obs.observe(document.getElementById(id)) });

  // --- filtr banku pytań
  var q = document.getElementById('qfilter');
  var sel = document.getElementById('topicfilter');
  var count = document.getElementById('bankcount');
  function apply(){
    var needle = (q && q.value || '').toLowerCase().trim();
    var topic = sel && sel.value || '';
    var shown = 0;
    document.querySelectorAll('details.testcard').forEach(function(card){
      var rows = card.querySelectorAll('tbody tr');
      var vis = 0;
      rows.forEach(function(tr){
        var ok = (!topic || tr.dataset.lab === topic) &&
                 (!needle || tr.textContent.toLowerCase().indexOf(needle) >= 0);
        tr.style.display = ok ? '' : 'none';
        if (ok) vis++;
      });
      card.style.display = vis ? '' : 'none';
      if (needle || topic) card.open = vis > 0; else card.open = false;
      shown += vis;
    });
    if (count) count.textContent = shown + ' pytań';
  }
  var tt = document.getElementById('totop');
  if (tt) {
    tt.addEventListener('click', function(){ window.scrollTo({top:0, behavior:'smooth'}); });
    window.addEventListener('scroll', function(){
      tt.classList.toggle('show', window.scrollY > 700);
    });
  }
  if (q) q.addEventListener('input', apply);
  if (sel) sel.addEventListener('change', apply);
});
</script>
</body>
</html>
"""


def build(mode: str, out_path: str) -> str:
    text = open(SRC, encoding="utf-8").read()

    # wklejenie automatycznych aneksów
    text = text.replace("<!--BANK-->", build_bank_html())
    text = text.replace("<!--TOPICMAP-->", build_topic_map())

    text = boxes_and_figures(text)
    text, store = protect_math(text)

    md = markdown.Markdown(
        extensions=[
            "extra",
            "sane_lists",
            "toc",
            "md_in_html",
            "footnotes",
            "admonition",
        ],
        extension_configs={
            "toc": {"permalink": False, "toc_depth": "2-3", "slugify": slugify},
        },
    )
    html = md.convert(text)
    html = restore_math(html, render_math(store, mode))

    # hero section: first h1 -> hero block
    m = re.search(r"<h1[^>]*>(.*?)</h1>(.*?)(?=<h2)", html, re.S)
    if m:
        title, rest = m.group(1), m.group(2)
        # wyciągnij pierwszy akapit jako lead
        hero = (
            f'<div class="hero"><div class="kicker">PELP1 · kompendium</div>'
            f"<h1>{title}</h1>{rest}</div>"
        )
        html = html[: m.start()] + hero + html[m.end():]

    toc = _toc_from_tokens(md.toc_tokens)
    page = TEMPLATE.replace("__TOC__", toc).replace("__BODY__", html)

    os.makedirs(KATEX_DST, exist_ok=True)
    shutil.copy(os.path.join(KATEX_SRC, "katex.min.css"), os.path.join(KATEX_DST, "katex.min.css"))
    fdir = os.path.join(KATEX_DST, "fonts")
    os.makedirs(fdir, exist_ok=True)
    for f in os.listdir(os.path.join(KATEX_SRC, "fonts")):
        if f.endswith(".woff2"):
            shutil.copy(os.path.join(KATEX_SRC, "fonts", f), os.path.join(fdir, f))

    if mode == "img":
        # MuPDF Story nie rysuje SVG przez <img> — podmieniamy na PNG 2x
        png_dir = os.path.join(KOMP, "figury", "png")
        os.makedirs(png_dir, exist_ok=True)
        for name in os.listdir(os.path.join(KOMP, "figury")):
            if name.endswith(".svg"):
                out_png = os.path.join(png_dir, name[:-4] + ".png")
                subprocess.run(
                    ["node", "/home/user/buildtools/svg2png.js",
                     os.path.join(KOMP, "figury", name)], check=True,
                    stdout=subprocess.DEVNULL)
                shutil.move("/tmp/" + name[:-4] + ".png", out_png)
        page = page.replace('src="figury/', 'src="figury/png/')
        page = page.replace('.svg"', '.png"')
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"OK -> {out_path}  ({len(page)/1024:.0f} kB)")
    return page


def main():
    build("katex", OUT)
    if "--pdf-src" in sys.argv:
        build("img", os.path.join(KOMP, "_pdf_source.html"))


if __name__ == "__main__":
    main()
