// Rasteryzacja SVG -> PNG przez resvg (Node), wynik w /tmp/<nazwa>.png
const fs = require('fs');
const path = require('path');
// moduł może leżeć globalnie (npm i -g) albo w katalogu roboczym
const candidates = [
  '@resvg/resvg-js',
  '/home/user/buildtools/node_modules/@resvg/resvg-js',
  path.join(process.cwd(), 'node_modules/@resvg/resvg-js'),
];
let Resvg = null;
for (const c of candidates) {
  try { Resvg = require(c).Resvg; break; } catch (e) { /* następny */ }
}
if (!Resvg) {
  console.error('Brak modułu @resvg/resvg-js — uruchom: npm install @resvg/resvg-js');
  process.exit(1);
}

const src = process.argv[2];
const scale = Number(process.argv[3] || 2);
const svg = fs.readFileSync(src, 'utf8');
const r = new Resvg(svg, { fitTo: { mode: 'zoom', value: scale }, background: 'white' });
const png = r.render().asPng();
const out = path.join('/tmp', path.basename(src).replace(/\.svg$/i, '.png'));
fs.writeFileSync(out, png);
console.log(out);
