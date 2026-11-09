# aymati.com.tr — çalışma notları

Aymati Proje Mühendislik'in statik web sitesi. Derleme adımı yok; `site/` klasörü olduğu gibi yayına alınır (Cloudflare Pages, çıktı dizini `site`). `main` dalına giren her değişiklik otomatik yayınlanır.

## Kurallar

- Site Türkçedir. Metinler sade, net ve teknik olarak doğru olmalı; uydurma mevzuat maddesi, sınır değer veya rakam yazma. Emin olmadığın bilgiyi yazma ya da genel ifade et.
- Sitede yıl vurgusu yapılmaz: görünür metinde "2026" gibi yıl yazma (Google verisindeki `datePublished` hariç).
- Fiyat yazılmaz. Tek istisna: site sahibinin talebiyle Faraday kafesi sayfasında (faraday-kafesi-hesaplama.html) yazan İstanbul içi keşif ücreti (500 € + KDV; İstanbul dışı ayrıca bildirilir). Hesap aracı yalnızca tahmini malzeme miktarı verir, fiyat vermez; fiyatlandırma keşif sonrası yapılır.
- Elektrik grubu projeleri "EMO kayıtlı S.M.M. elektrik mühendisi", mekanik grubu projeler ve statik analizler "MMO kayıtlı makina mühendisi" tarafından imzalanır.
- Hizmet adları baş harfleri büyük yazılır (ör. "Topraklama Ölçümü").
- Adresler .html'siz kullanılır: site içi bağlantılar `href="topraklama-olcumu"`, canonical/og:url/sitemap/JSON-LD `https://www.aymati.com.tr/topraklama-olcumu`. Cloudflare Pages `.html` adreslerini .html'siz adrese yönlendirir; yönlenen adrese canonical verilmez. Dosya adları yine `site/<sayfa>.html`dir.
- Her sayfanın başında özgün bir teknik çizim (`site/img/<sayfa>.svg`) ve paylaşım görseli (`site/img/og/<sayfa>.jpg`) olur. Yeni sayfa için `python3 tools/gorsel/gorsel.py <sayfa> <motif> "<başlık>" "<üst etiket>"` çalıştır; motifler `tools/gorsel/motifs.py`, sayfa→motif kaydı `tools/gorsel/sayfalar.json`. `new_post.py` blog görselini kendisi üretir. Gerçek fotoğraf gelirse `site/img/foto/` altına eklenir.
- Mobil ekranda alttaki Ara / WhatsApp / Teklif Al çubuğu (`.mcta`) her sayfada bulunur; yeni sayfada korunur.
- `main` dalına doğrudan yazma. Her değişiklik ayrı bir dalda hazırlanır ve pull request olarak açılır. Site sahibi genel izin verdi (5 Kasım): PR, kurallara uygunluğu ve kırık bağlantı olmadığı kontrol edildikten sonra REST API ile (squash) birleştirilebilir; site sahibine onay için soru sorulmaz, yapılan iş sonradan özetlenir. Hesap açma, şifre/ödeme bilgisi girme, reklam harcaması başlatma ve sosyal medyada paylaşım yine site sahibine aittir.

## Yeni blog yazısı (iki haftada bir)

1. `tools/takvim.json` içinde `"durum": "bekliyor"` olan ilk konuyu seç.
2. Yazıyı yaz: 700-1000 kelime; `<p>`, `<h2>`, `<h3>`, `<ul>`, `<ol>`, `<b>` kullan. Mevcut `site/blog-*.html` yazılarının tonuna uy: kısa paragraflar, işletme sahibine ve İSG uzmanına hitap eden pratik bilgi, sonda Aymati Proje'nin bu konudaki hizmetine bir cümlelik atıf. İlgili hizmet sayfalarına metin içinde `<a href="sayfa-adi">` ile (.html yazmadan) bağlantı ver. Bilgileri resmî kaynaklardan (Resmî Gazete, ÇSGB, TSE, EMO, MMO) doğrula.
3. `tools/yazilar/<slug>.json` dosyasını oluştur (alanlar `tools/new_post.py` başında açıklanmıştır; `related` için takvimdeki `ilgili` listesini kullan).
4. `python3 tools/new_post.py tools/yazilar/<slug>.json` çalıştır.
5. Takvimde konunun durumunu `"taslak"` yap ve PR bağlantısını `"pr"` alanına yaz.
6. `blog/<slug>` dalına commit et, push et ve `gh api repos/sadohozmen-droid/aymati-site/pulls -f title=... -f head=blog/<slug> -f base=main -f body=...` ile pull request aç. PR açıklamasında yazının özetini ve sayfa adını ver. (GraphQL çalışmaz; yalnızca REST.)
7. PR'ı kontrol edip birleştir; takvimde durumu `"yayında"` yap. Önceki bir blog PR'ı açık ve birleştirilemiyorsa (çakışma vb.) önce onu çöz.

Takvimdeki konular bittiğinde, hizmet sayfalarıyla ilişkili ve işletmelerin Google'da sorduğu sorulardan yeni konular öner ve takvime ekle.
