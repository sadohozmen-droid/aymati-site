#!/usr/bin/env python3
"""Yeni blog yazısı sayfası üretir ve siteyi günceller.

Kullanım:  python3 tools/new_post.py tools/yazilar/<slug>.json

JSON alanları:
  slug      : URL parçası (ör. "topraklama-olcumu-kac-yilda-bir-yapilir")
  cat       : "mevzuat" | "isg" | "saha"
  date      : "YYYY-MM-DD" (sayfada görünmez, yalnızca Google verisinde)
  title     : sayfadaki başlık (H1)
  seo       : <title> etiketi (60-65 karakter civarı)
  desc      : meta açıklama (150-160 karakter)
  summary   : kart ve giriş metni (1 cümle)
  related   : ilgili hizmet sayfalarının dosya adları, .html olmadan (2-4 adet)
  body      : yazının HTML gövdesi (<p>, <h2>, <h3>, <ul>, <ol>, <b>)

Yapılanlar: site/blog-<slug>.html oluşturulur; blog.html listesinin başına kart,
index.html "Son yazılar" bölümüne kart (en yeni 3) eklenir; tüm yazılardaki
"Diğer yazılar" listesi ve sitemap.xml güncellenir.
"""
import json, re, sys, glob, os, html

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site')
BASE = 'https://www.aymati.com.tr/'
CATS = {'mevzuat': 'Mevzuat ve Bakanlık', 'isg': 'İSG gelişmeleri', 'saha': 'Sahadan uygunsuzluklar'}

def rd(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def wr(p, t): open(os.path.join(ROOT, p), 'w', encoding='utf-8').write(t)
def esc(s): return html.escape(s, quote=True)

def service_name(slug):
    t = rd(slug + '.html')
    m = re.search(r'"@type": "Service", "name": "([^"]+)"', t)
    if m: return m.group(1)
    m = re.search(r'<h1>(.*?)</h1>', t, re.S)
    return re.sub(r'<[^>]+>', '', m.group(1)).strip()

def posts():
    out = []
    for f in glob.glob(os.path.join(ROOT, 'blog-*.html')):
        t = open(f, encoding='utf-8').read()
        d = re.search(r'"datePublished": "([^"]+)"', t).group(1)
        h = re.search(r'<h1>(.*?)</h1>', t, re.S).group(1)
        out.append((d, os.path.basename(f), h))
    return sorted(out, reverse=True)

def main(path):
    x = json.load(open(path, encoding='utf-8'))
    assert x['cat'] in CATS, 'cat: mevzuat | isg | saha'
    for r in x['related']:
        assert os.path.exists(os.path.join(ROOT, r + '.html')), 'ilgili sayfa yok: ' + r
    catname = CATS[x['cat']]
    fn = 'blog-' + x['slug'] + '.html'; url = BASE + fn
    tpl_file = sorted(glob.glob(os.path.join(ROOT, 'blog-*.html')))[0]
    t = open(tpl_file, encoding='utf-8').read()

    t = re.sub(r'<title>.*?</title>', f'<title>{esc(x["seo"])} | Aymati Proje</title>', t, count=1, flags=re.S)
    t = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(x["desc"])}">', t, count=1)
    t = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{esc(x["seo"])} | Aymati Proje">', t, count=1)
    t = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{esc(x["desc"])}">', t, count=1)
    t = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', t, count=1)
    t = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', t, count=1)
    ld = [{"@context": "https://schema.org", "@type": "BlogPosting", "headline": x['title'], "description": x['desc'],
           "datePublished": x['date'], "dateModified": x['date'], "inLanguage": "tr", "mainEntityOfPage": url,
           "author": {"@type": "Organization", "name": "Aymati Proje", "url": BASE},
           "publisher": {"@type": "Organization", "name": "Aymati Proje", "logo": {"@type": "ImageObject", "url": BASE + "og-image.png"}},
           "image": BASE + "og-image.png"},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Ana sayfa", "item": BASE},
              {"@type": "ListItem", "position": 2, "name": "Blog", "item": BASE + "blog.html"},
              {"@type": "ListItem", "position": 3, "name": x['title'], "item": url}]}]
    t = re.sub(r'(<script type="application/ld\+json">.*?</script>\n?)+',
               ''.join(f'<script type="application/ld+json">{json.dumps(l, ensure_ascii=False)}</script>\n' for l in ld), t, count=1, flags=re.S)
    t = re.sub(r'(<a href="blog.html">Blog</a> / )[^<]*(</nav>)', lambda m: m.group(1) + catname + m.group(2), t, count=1)
    t = re.sub(r'<h1>.*?</h1>', f'<h1>{x["title"]}</h1>', t, count=1, flags=re.S)
    t = re.sub(r'(<section class="dhero".*?<p class="lead">).*?(</p>)', lambda m: m.group(1) + x['summary'] + m.group(2), t, count=1, flags=re.S)
    t = re.sub(r'<div class="ameta"><span>[^<]*</span>', f'<div class="ameta"><span>{catname}</span>', t, count=1)
    t = re.sub(r'<article class="art">.*?</article>', lambda m: f'<article class="art">{x["body"]}</article>', t, count=1, flags=re.S)
    rel = ''.join(f'<a href="{r}.html">{service_name(r)}<span aria-hidden="true">→</span></a>' for r in x['related'])
    t = re.sub(r'<div class="relgrid">.*?</div></section>', lambda m: f'<div class="relgrid">{rel}</div></section>', t, count=1, flags=re.S)
    t = re.sub(r'(<button type="button" class="btn teal quote" data-svc=")[^"]*(")', lambda m: m.group(1) + service_name(x['related'][0]) + m.group(2), t, count=1)
    wr(fn, t)

    card = (f'<article class="post" data-cat="{x["cat"]}"><span class="tag t-{x["cat"]}">{catname}</span>'
            f'<h3><a href="{fn}">{x["title"]}</a></h3><p>{x["summary"]}</p></article>')
    b = rd('blog.html')
    if f'href="{fn}"' not in b:
        b = b.replace('<div class="posts" id="posts">', '<div class="posts" id="posts">' + card, 1)
        wr('blog.html', b)
    i = rd('index.html')
    m = re.search(r'(<section id="blog-ozet".*?<div class="posts">)(.*?)(</div>\s*<p)', i, re.S)
    if m and f'href="{fn}"' not in m.group(2):
        cards = re.findall(r'<article class="post".*?</article>', m.group(2), re.S)
        new = card + ''.join(cards[:2])
        i = i[:m.start(2)] + new + i[m.end(2):]
        wr('index.html', i)

    allp = posts()
    for d, f, h in allp:
        pt = rd(f)
        lst = ''.join(f'<li><a href="{f2}">{h2}</a></li>' for d2, f2, h2 in allp if f2 != f)
        pt = re.sub(r'<ul class="morep">.*?</ul>', lambda m: f'<ul class="morep">{lst}</ul>', pt, count=1, flags=re.S)
        wr(f, pt)

    sm = rd('sitemap.xml')
    if url not in sm:
        sm = sm.replace('</urlset>', f'  <url><loc>{url}</loc><lastmod>{x["date"]}</lastmod></url>\n</urlset>')
        wr('sitemap.xml', sm)
    print('Oluşturuldu:', fn)

if __name__ == '__main__':
    main(sys.argv[1])
