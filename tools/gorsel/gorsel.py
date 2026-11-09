#!/usr/bin/env python3
"""Sayfa görseli üretir: site/img/<slug>.svg (sayfa başı çizimi) ve site/img/og/<slug>.jpg (paylaşım görseli).

Kullanım:
  python3 tools/gorsel/gorsel.py <slug> <motif> "<başlık>" "<üst etiket>" ["<alt metin>"] [motif argümanı...]
Örnek:
  python3 tools/gorsel/gorsel.py blog-raf-yuk-etiketi raf "Raf Yük Etiketi Nasıl Okunur?" "Blog · Statik Analiz"

Motif adları: tools/gorsel/motifs.py içindeki MOTIFS (raf, platform, iskele, stand, sahne, kulevinc,
travers, monoray, tabela, paratoner, pano, topraklama, olcum, termal, trafo, aku, forklift, kopruvinc,
kazan, yangin, fan, tahliye, atex, gurultu, toz, gaz, voc, isik, titresim, manyetik, termalkonfor,
agirmetal, makasli, jenerator, kompanzasyon, katodik, enerji, ark, zincir, caraskal, harita, cizim,
kontrol, kiris, soru). JPG için Node + Playwright gerekir; yoksa yalnız SVG üretilir.
"""
import sys, os, json, html, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import motifs as M
SITE = os.path.join(HERE, '..', '..', 'site')
GRID = '<defs><pattern id="g" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="#ffffff" stroke-opacity=".06"/></pattern></defs>'

def body(motif, args, uid):
    return M.MOTIFS[motif](*args).replace('id="hot"', f'id="hot-{uid}"').replace('url(#hot)', f'url(#hot-{uid})')

def hero_svg(motif, args, alt, uid='x'):
    a = html.escape(alt)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 440" width="640" height="440" role="img" aria-label="{a}"><title>{a}</title>'
            f'{GRID}<rect width="640" height="440" fill="#0d2547"/><rect width="640" height="440" fill="url(#g)"/>{body(motif, args, uid)}</svg>')

def _lines(s, n=22):
    out, cur = [], ''
    for w in s.split():
        if len(cur) + len(w) + 1 > n and cur: out.append(cur); cur = w
        else: cur = (cur + ' ' + w).strip()
    return (out + [cur])[:3]

def tr_upper(s): return s.replace('i', 'İ').replace('ı', 'I').upper()

def og_svg(motif, args, title, eyebrow, uid='x'):
    ls = _lines(title)
    tx = ''.join(f'<text x="64" y="{230 + i*62}" font-size="52" font-weight="800" fill="#ffffff" font-family="Poppins,\'DejaVu Sans\',Arial,sans-serif">{html.escape(l)}</text>' for i, l in enumerate(ls))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">{GRID}<rect width="1200" height="630" fill="#0d2547"/><rect width="1200" height="630" fill="url(#g)"/>'
            f'<text x="64" y="150" font-size="22" fill="#d3a467" font-family="\'DejaVu Sans Mono\',monospace" letter-spacing=".12em">{html.escape(tr_upper(eyebrow))}</text>{tx}'
            f'<rect x="64" y="{250 + len(ls)*62}" width="120" height="6" fill="#48c9c6"/>'
            f'<text x="64" y="560" font-size="30" font-weight="700" fill="#ffffff" font-family="Poppins,\'DejaVu Sans\',Arial,sans-serif">AYMATİ <tspan fill="#d3a467" font-weight="400">PROJE</tspan></text>'
            f'<text x="64" y="594" font-size="20" fill="#9aa9be" font-family="\'DejaVu Sans Mono\',monospace">www.aymati.com.tr · 0555 142 84 74</text>'
            f'<g transform="translate(600,110) scale(0.88)">{body(motif, args, uid)}</g></svg>')

JS = r"""const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:630}});
await p.setContent('<html><body style="margin:0">'+fs.readFileSync(process.argv[2],'utf8')+'</body></html>');await p.screenshot({path:process.argv[3],type:'jpeg',quality:82});await b.close()})();"""

def make(slug, motif, title, eyebrow, alt=None, args=()):
    alt = alt or f'{title} — teknik çizim'
    os.makedirs(os.path.join(SITE, 'img', 'og'), exist_ok=True)
    open(os.path.join(SITE, 'img', slug + '.svg'), 'w', encoding='utf-8').write(hero_svg(motif, args, alt, slug[:8]))
    with tempfile.TemporaryDirectory() as d:
        sp = os.path.join(d, 'og.svg'); jp = os.path.join(d, 'r.js')
        open(sp, 'w', encoding='utf-8').write(og_svg(motif, args, title, eyebrow, slug[:8])); open(jp, 'w').write(JS)
        try:
            subprocess.run(['node', jp, sp, os.path.join(SITE, 'img', 'og', slug + '.jpg')], check=True, capture_output=True, timeout=120)
            return True
        except Exception as e:
            print('JPG üretilemedi (Node/Playwright yok?):', e); return False

if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) < 4: print(__doc__); sys.exit(1)
    ok = make(a[0], a[1], a[2], a[3], a[4] if len(a) > 4 else None, tuple(a[5:]))
    print('site/img/' + a[0] + '.svg' + (' ve site/img/og/' + a[0] + '.jpg' if ok else ''))
