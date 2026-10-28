# aymati.com.tr

Aymati Proje Mühendislik web sitesi (statik HTML, derleme adımı yok).

- `site/` — yayına alınan dosyalar (Cloudflare Pages çıktı dizini)
- `tools/new_post.py` — yeni blog yazısı sayfası üretir
- `tools/takvim.json` — blog içerik takvimi
- `tools/yazilar/` — yazıların kaynak dosyaları

Yeni yazılar `blog/...` dallarında pull request olarak hazırlanır; onaylanıp `main` dalına birleştirildiğinde yayına girer.
