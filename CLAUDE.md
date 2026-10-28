# aymati.com.tr — çalışma notları

Aymati Proje Mühendislik'in statik web sitesi. Derleme adımı yok; `site/` klasörü olduğu gibi yayına alınır (Cloudflare Pages, çıktı dizini `site`). `main` dalına giren her değişiklik otomatik yayınlanır.

## Kurallar

- Site Türkçedir. Metinler sade, net ve teknik olarak doğru olmalı; uydurma mevzuat maddesi, sınır değer veya rakam yazma. Emin olmadığın bilgiyi yazma ya da genel ifade et.
- Sitede yıl vurgusu yapılmaz: görünür metinde "2026" gibi yıl yazma (Google verisindeki `datePublished` hariç).
- Fiyat yazılmaz.
- Elektrik grubu projeleri "EMO kayıtlı S.M.M. elektrik mühendisi", mekanik grubu projeler ve statik analizler "MMO kayıtlı makina mühendisi" tarafından imzalanır.
- Hizmet adları baş harfleri büyük yazılır (ör. "Topraklama Ölçümü").
- `main` dalına doğrudan yazma. Her değişiklik ayrı bir dalda hazırlanır ve pull request olarak açılır; site sahibi onaylayınca birleştirilir.

## Yeni blog yazısı (iki haftada bir)

1. `tools/takvim.json` içinde `"durum": "bekliyor"` olan ilk konuyu seç.
2. Yazıyı yaz: 700-1000 kelime; `<p>`, `<h2>`, `<h3>`, `<ul>`, `<ol>`, `<b>` kullan. Mevcut `site/blog-*.html` yazılarının tonuna uy: kısa paragraflar, işletme sahibine ve İSG uzmanına hitap eden pratik bilgi, sonda Aymati Proje'nin bu konudaki hizmetine bir cümlelik atıf. İlgili hizmet sayfalarına metin içinde `<a href="...html">` ile bağlantı ver. Bilgileri resmî kaynaklardan (Resmî Gazete, ÇSGB, TSE, EMO, MMO) doğrula.
3. `tools/yazilar/<slug>.json` dosyasını oluştur (alanlar `tools/new_post.py` başında açıklanmıştır; `related` için takvimdeki `ilgili` listesini kullan).
4. `python3 tools/new_post.py tools/yazilar/<slug>.json` çalıştır.
5. Takvimde konunun durumunu `"taslak"` yap ve PR bağlantısını `"pr"` alanına yaz.
6. `blog/<slug>` dalına commit et, push et ve `gh api repos/sadohozmen-droid/aymati-site/pulls -f title=... -f head=blog/<slug> -f base=main -f body=...` ile pull request aç. PR açıklamasında yazının özetini ve sayfa adını ver. (GraphQL çalışmaz; yalnızca REST.)
7. Önceki taslak PR'lar hâlâ açıksa yeni yazı yazma; bunun yerine açık PR'ları hatırlatan kısa bir not bırak.

Takvimdeki konular bittiğinde, hizmet sayfalarıyla ilişkili ve işletmelerin Google'da sorduğu sorulardan yeni konular öner ve takvime ekle.
