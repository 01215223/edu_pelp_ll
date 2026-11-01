const katex = require('/home/user/buildtools/node_modules/katex');
const fs = require('fs');
const src = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const out = src.map(t => {
  const display = t.startsWith('$$');
  const tex = display ? t.slice(2, -2) : t.slice(1, -1);
  try {
    return katex.renderToString(tex, {displayMode: display, throwOnError: false, strict: false});
  } catch (e) {
    return '<span class="math-error">' + tex.replace(/</g, '&lt;') + '</span>';
  }
});
fs.writeFileSync(process.argv[3], JSON.stringify(out));
