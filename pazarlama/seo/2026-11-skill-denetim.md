# Skill tabanlı derin SEO denetimi: Kasım 2026 (2026-11-23)

**KRİTİK: teklif formu e-posta programına düşüyor.** `site/teklif.html:495` içinde `const FORM_ENDPOINT='';` hâlâ boş (2026-11 denetiminin 1. maddesi, hâlâ açık). Bu denetimin konusu değil, ama sitenin tek dönüşüm noktası olduğu için en üstte tekrar ediliyor.

Yöntem: `.claude/product-marketing.md` bağlamıyla `seo-audit` (yerel SEO başvuruları dahil), `schema`, `ai-seo` (agent-readiness, platform-ranking-factors) ve `site-architecture` skill'leri kullanıldı. `site/` altındaki 102 sayfa betikle tarandı: JSON-LD tipleri, NAP, iç bağlantı grafiği, tıklama derinliği, küme yapısı, ilk paragraf ve llms.txt kapsamı. Kasım genel denetiminde (`2026-11.md`, `2026-11-meta.md`) ele alınan başlık, açıklama, H1 ve canonical konuları tekrarlanmadı.

**Ölçülemeyenler:** Canlı siteye (`www.aymati.com.tr`) bu ortamdan erişilemedi; ajan vekil sunucusu bağlantıyı reddetti (403). Bu yüzden Cloudflare'in yapay zekâ botlarına verdiği gerçek yanıt, Rich Results Test ve Search Console verisi **ölçülmedi**. Bu konular "geçti" sayılmamalı (bkz. B2).

## Bu dalda yapılan düzeltmeler (mekanik, görünür metin değişmedi)

| # | Düzeltme | Dosya |
|---|---|---|
| D1 | Bağlantı metniyle hedefi uyuşmayan 6 iç bağlantı düzeltildi. Metin belirli bir hizmeti söylüyor, bağlantı ise genel bir dizin sayfasına gidiyordu. "Topraklama Ölçümü" → `topraklama-olcumu` (2 yerde), "Anlık Gaz Ölçümü" → `anlik-gaz-olcumu`, "Ortam VOC Ölçümü" → `ortam-voc-olcumu`, "Endüstriyel Raf Kontrolü" → `endustriyel-raf-kontrolu`, "Forklift Periyodik Kontrolü" → `forklift-periyodik-kontrolu` | `site/elektrik-ic-tesisat-projesi.html:483`, `site/patlamadan-korunma-dokumani.html:510`, `site/raf-statik-analizi.html:571` |
| D2 | Ana işletme şeması (ProfessionalService) zenginleştirildi: `@id` (`https://www.aymati.com.tr/#isletme`), `logo` (`img/gbp/logo-kare.png`, 720×720), `image` (`og-image.png`) ve sayfada görünen "Hafta içi 08:30 – 18:00" bilgisiyle eşleşen `openingHoursSpecification` eklendi. `description` alanı Statik Analiz'i içermiyordu; ana sayfanın mevcut meta açıklamasıyla eşitlendi (yeni metin yazılmadı) | `site/index.html:329`, `site/iletisim.html:325` |
| D3 | Ana sayfaya `WebSite` şeması eklendi (`name`, `url`, `inLanguage`, `publisher` → `#isletme`). Google'ın sonuçlarda site adını göstermek için kullandığı tip budur | `site/index.html:330` |
| D4 | 6 bölge sayfasındaki ProfessionalService'te telefon, e-posta ve çalışma saati yoktu. Ana kayıtla aynı NAP değerleri ve `@id` eklendi | `site/bolge-*.html:325` |
| D5 | Faraday sayfasındaki iki `provider` düğümüne aynı `@id` eklendi (fiyat/Offer alanlarına dokunulmadı) | `site/faraday-kafesi-hesaplama.html:325-326` |
| D6 | `robots.txt` tek grupta toplandı. Eski dosyada her bot ayrı `User-agent` grubundaydı; adı yazılan grup `*` kurallarını devralmadığı için `Disallow: /404` bu botlara uygulanmıyordu. Erişim izni değişmedi: tüm arama, alıntı ve eğitim botları yine izinli. `Claude-User`, `Perplexity-User` ve `meta-webindexer` niyeti belgelemek için listeye eklendi. `urllib.robotparser` ile doğrulandı | `site/robots.txt` |
| D7 | `llms.txt` site haritasındaki 8 adresi içermiyordu: blog dizini ile son 7 yazı (PKD güncelleme, pano tek hat şeması, monoray, işin durdurulması, ağır sanayi, hafif/ağır kusur, kalorifer kazanı). Sayfaların kendi başlık ve açıklamalarıyla eklendi. Artık site haritası ile llms.txt birebir eşleşiyor | `site/llms.txt` (Blog bölümü) |

Kontroller: 102 sayfanın tüm JSON-LD blokları ayrıştırılabiliyor, kırık iç bağlantı yok, `.html`'li iç bağlantı yok. Alt metni eksik tek görsel bilinen büyütme penceresi (`raf-statik-analizi.html:737`, JS ile dolduruluyor).

Not: D2-D5 görünmeyen şema değişiklikleridir ama 9 sayfaya dokunur. CLAUDE.md'deki "birçok sayfayı birden etkileyen değişiklik" ölçütüne girip girmediğine PR'ı açan karar versin.

---

## A. Yüksek öncelik (öneri, site sahibi kararı gerekir)

### A1. Ana sayfa kardeş siteyle aynı sorgulara oynuyor; öncelikli hizmetler başlıkta yok
- **Kanıt:** `site/index.html:9`: `<title>Projelendirme, Periyodik Muayene, İş Hijyeni | Aymati Proje</title>`. `index.html:551` H2'si "Projelendirme, periyodik muayene ve iş hijyeni", `index.html:633` "Tek ofis, üç hizmet". `site/hakkimizda.html:405` lead'i şirketi "projelendirme, periyodik kontrol ve çalışma ortamı ölçümleri" diye tanımlıyor. `llms.txt` giriş özeti de periyodik muayene ve iş hijyenini öncelikli hizmetlerle aynı düzeyde sayıyor.
- **Etki:** Yüksek. Sitenin en güçlü sayfası, teknikisg.com'un sahip olduğu sorgulara (periyodik muayene, iş hijyeni) oynuyor. Öncelikli Statik Analiz ve PKD ise başlıkta yok. Yapay zekâ asistanları şirketi tanımlarken ilk olarak ana sayfanın ve Hakkımızda'nın lead'ini kullanıyor; şu an çıkan tanım "periyodik muayene firması".
- **Öneri:** Ana sayfa başlığı ve "Hizmetlerimiz" H2'si öncelikli kümeleri öne alsın. Örnek kalıp: "Projelendirme, Statik Analiz ve PKD | Aymati Proje". Periyodik muayene ve iş hijyeni sayfaları kalır, ama ana sayfa ve Hakkımızda tanımında ikinci sıraya iner. `llms.txt` girişi de aynı sırayla güncellenir. Bu, metin ve konumlandırma kararıdır, site sahibinin onayını gerektirir.

### A2. Görünür fiyat ana sayfada da var (CLAUDE.md istisnası yalnız Faraday sayfası için)
- **Kanıt:** `site/index.html:472` (slayt lead'i: "İstanbul içi keşif 500 € + KDV") ve `site/index.html:538` ("Fiyatlandırma keşif sonrası: İstanbul içi keşif 500 € + KDV"). Bunlar #36 ile eklendi. Ayrıca `site/llms.txt:21`'de de geçiyor.
- **Etki:** Kural çelişkisi. CLAUDE.md'ye göre tek istisna `faraday-kafesi-hesaplama.html`.
- **Öneri:** Site sahibi ana sayfada da fiyatı istiyorsa CLAUDE.md'deki istisna metni genişletilsin. İstemiyorsa iki cümle "keşif ücreti için Faraday sayfasına bakın" biçimine çekilsin. Ajanların bu tutarsızlığı her ay yeniden raporlamaması için karar yazılı olmalı. Değiştirilmedi.

### A3. Google İşletme Profili ile site birbirine bağlı değil (yerel SEO, NAP)
- **Kanıt:** NAP sitede tutarlı: telefon 316 yerde "0555 142 84 74", `tel:`/`wa.me` biçimleri tek tip, adres 109 yerde aynı. Ama hiçbir sayfada Google Haritalar veya İşletme Profili bağlantısı yok, şemada `sameAs`/`hasMap` yok. Sosyal medya planlarına göre (`pazarlama/sosyal/2026-49.md:64`) profil mevcut. Şemada `postalCode` ve `geo` da yok.
- **Etki:** Yüksek (yerel paket). Google'ın siteyi ve profili aynı varlık olarak eşlemesi zorlaşıyor. Yapay zekâ asistanlarının yerel öneri yaparken kullandığı kaynak çoğunlukla profil.
- **Site sahibinden istenenler:** (1) İşletme Profili'nin paylaşım bağlantısı (maps.app.goo.gl/… veya CID). (2) Varsa LinkedIn şirket sayfası. (3) Posta kodu. (4) Profildeki saatlerin sitedeki "Hafta içi 08:30 – 18:00" ile aynı olduğunun teyidi. Gelince: `iletisim` sayfasına "Haritada görün" bağlantısı, şemaya `sameAs` + `hasMap` + `postalCode`. Koordinat uydurulmayacak; yalnız profilden alınacak.
- **Ayrıca:** Profildeki işletme adı ve kategori "Mühendislik hizmetleri" olmalı. Adda anahtar kelime olmamalı. Hizmet bölgesi gerçek kapsamla sınırlı tutulmalı (`local-seo-profile-and-citations.md`).

### A4. PKD kümesinde hub, yazılarına bağlantı vermiyor; küme tek sayfa
- **Kanıt:** `site/patlamadan-korunma-dokumani.html` hiçbir blog yazısına bağlantı vermiyor. Konuya ait iki yazı var: `blog-patlamadan-korunma-dokumani-ne-zaman-guncellenir`, `blog-agir-sanayide-patlama-ve-buyuk-kaza-riskine-karsi-temel-kontroller`. İkisi hub'a bağlantı veriyor; bağlantı tek yönlü. Kümede PKD'ye ait ikinci bir hizmet sayfası yok.
- **Öneri:**
  1. PKD sayfasının yan sütununa, statik analiz sayfasındaki gibi bir "İlgili yazı" kartı eklensin (bu biçim 2026-11-meta'da onaylandı).
  2. Takvimdeki PKD konuları (#26 tehlikeli bölge sınıflandırması, #4 hangi işyerlerine zorunlu, #30 kim hazırlar, #19 Ex ekipman) periyodik muayene konularından önce yazılsın. Her biri hub'a ve hub da onlara bağlantı versin.

### A5. Statik Analiz ve Projelendirme hub'larında hub'dan yazıya bağlantı eksik
- **Kanıt:**
  - `statik-analiz.html` kümenin 5 yazısından yalnız `blog-statik-analiz-raporu-nedir-kimler-ister`'e bağlantı veriyor. `blog-fuar-standi-…`, `blog-vinc-ayak-yuku-…`, `blog-monoray-…`, `blog-raf-etiketi-…` hub'dan bağlantı almıyor.
  - `monoray-vinc-yolu-statik-analizi.html` kendi yazısı `blog-monoray-ve-vinc-yolu-statik-hesabi-nedir`'e bağlantı vermiyor.
  - `raf-statik-analizi.html` de `blog-raf-etiketi-olmayan-depolar`'a bağlantı vermiyor.
  - `blog-monoray-…` ve `blog-raf-etiketi-…` gövde metninde hub'a (`statik-analiz`) bağlantı vermiyor; yalnız menüde var.
  - `projelendirme.html` hiçbir yazıya bağlantı vermiyor (`blog-pano-tek-hat-semasi-…`, `blog-acil-durum-tahliye-plani-…`). `acil-durum-tahliye-plani-projesi.html` kendi yazısına bağlantı vermiyor.
- **Öneri:** `site-architecture` hub-and-spoke kuralı gereği hub tüm yazılarına, her hizmet sayfası kendi yazısına bağlantı vermeli. Bunun için "İlgili yazılar" kartları gerekir; görünür içerik değiştiği için yapılmadı.
- **Not:** Bütün öncelikli sayfalar ana sayfadan 1 tıklamada; tıklama derinliği sorunu yok. Sorun bağlantının yönü ve bağlam.

## B. Orta öncelik

### B1. Faraday kümesi: araç sayfası güçlü, destek içeriği yok
- **Kanıt:** `faraday-kafesi-hesaplama` her sayfadaki üst şeritten bağlantı alıyor. Gövde metninden ise yalnız 3 sayfa bağlantı veriyor: `index`, `yildirimdan-korunma-tesisati-projesi`, `yildirimdan-korunma-tesisati-paratoner-olcumu`. Faraday veya aktif paratoner üzerine hiç yazı yok. Takvimde #32 (Faraday mı paratoner mi) ve #29 (TS EN 62305-2 risk analizi) "bekliyor".
- **Öneri:** #32 ve #29 öne alınsın. `topraklama-olcumu` ve `elektrik-ic-tesisat-projesi` "İlgili hizmetler" listelerine Faraday aracı eklensin (öneri). Faraday sayfasının ilk paragrafı alıntılanmaya uygun bir doğrudan cevapla başlıyor; korunmalı.

### B2. Cloudflare bot ayarı doğrulanmalı (ölçülmedi)
- `robots.txt` her şeye izin veriyor. Ama `ai-seo/references/agent-readiness.md`'ye göre asıl kapı CDN/WAF: Cloudflare'in "Block AI bots", "AI Crawl Control" ve "Managed robots.txt" ayarları, robots.txt ne derse desin 403 döndürebilir veya dosyanın başına kendi kurallarını ekleyebilir.
- **Site sahibinden:** Cloudflare panelinde Security → Bots ekranının ve AI Crawl Control sayfasının görüntüsü. İzin veriliyorsa canlı `https://www.aymati.com.tr/robots.txt` çıktısının depodaki dosyayla aynı olduğu da kontrol edilmeli.
- **Eğitim botları:** `GPTBot`, `ClaudeBot`, `Google-Extended`, `Applebot-Extended` şu an izinli. Bu bir tercih; kapatmak alıntılanmayı engellemez. Karar site sahibinin.

### B3. Yapay zekâ alıntısı: ilk paragraflar
`ai-seo` "Content Extractability" kontrolü 12 öncelikli sayfaya uygulandı:
- **İyi (doğrudan tanımla başlıyor):** `statik-analiz`, `raf-statik-analizi`, `fuar-standi-statik-analizi`, `patlamadan-korunma-dokumani`, `pano-tek-hat-semasi-projesi`, `yildirimdan-korunma-tesisati-projesi`, `faraday-kafesi-hesaplama`. PKD sayfası yönetmelik dayanağını ilk paragrafta veriyor.
- **Geliştirilebilir:**
  - `vinc-statik-analizi` ve `tabela-pilon-statik-hesabi`'nin ilk cümlesi tanım değil, risk anlatısı; tanım ikinci cümlede. Önerilen ilk cümle kalıbı: "X statik hesabı, … gösteren imzalı mühendislik raporudur; Y ister, MMO kayıtlı makina mühendisi imzalar."
  - `index.html:441` H1'i ("Periyodik kontrolden projeniz yok diye mi geçemediniz?") şirketin ne olduğunu söylemiyor (A1 ile birlikte ele alınmalı).
- **Teknik engel:** "Rölöve" açıklama kutusu (`<span class="tip" hidden>`) cümlenin içinde duruyor. CSS çalıştırmayan ajanlar ve metin dönüştürücüler cümleyi "rölövesiniRölöve (Fransızca relevé): … alır ve" diye okuyor; ilk paragraf bozuluyor. Konumlar: `index.html:442`, `projelendirme.html:416`, `elektrik-ic-tesisat-projesi.html:454`. Öneri: açıklama kutusunu cümlenin dışına taşımak, örneğin paragraf sonuna `<dfn>` notu ya da `title` özniteliği. Tasarım değişikliği olduğu için yapılmadı.
- **İmza bilgisi:** "Kim imzalar" sorusu (EMO/MMO) hizmet sayfalarında var ve ayırt edici. Ancak mühendis adları ve sicil numaraları hâlâ yer tutucu (`hakkimizda.html:425`: "Ad Soyad" ×3, "SİCİL NO: ______" ×2). Hem E-E-A-T hem yapay zekâ alıntısı için bu en değerli eksik. Bilgi gelince Hakkımızda'ya `Person` şeması eklenebilir (`jobTitle`, `memberOf` EMO/MMO, `worksFor` → `#isletme`). Uydurma bilgi girilmeyecek.

### B4. Bölge sayfaları: içerik derinliği dengesiz (doorway riski)
- **Kanıt:** Ana içerik uzunluğu sayfadan sayfaya çok farklı. `bolge-dudullu-osb-umraniye` 716 kelime, `bolge-tuzla-osb-tuzla` 659 kelime. Eski dört sayfa ise kısa: `ikitelli` 347, `gaziosmanpasa` 307, `hadimkoy` 298, `esenyurt` 272. Sayfalar arası metin benzerliği düşük (≤0,33), yani şablon kopyası değiller. Ama kısa olanlar `local-seo-pages-and-measurement.md`'deki "anlamlı yerel bilgi" ölçütünün sınırında.
- **Öneri:** Dört eski sayfa Dudullu/Tuzla düzeyine getirilsin: bölgedeki sektörler, sık istenen belgeler, bölgeye özgü SSS. Sayfalar, ofisin Gaziosmanpaşa'da olduğunu ve bunun bir hizmet bölgesi olduğunu açıkça söylemeye devam etmeli. Şemada bölge sayfaları için yeni adres uydurulmadı; `areaServed` doğru kullanılıyor.

### B5. Şemada hizmet bölgesi görünür metinle uyuşmuyor
- **Kanıt:** 69 hizmet sayfasında ve ana kayıtta `areaServed: Country "Türkiye"`. Görünür metin ve `llms.txt` "İstanbul ve çevresi" diyor. Faraday sayfası "İstanbul dışı ayrıca bildirilir" diyor (`City: İstanbul`).
- **Öneri:** Site sahibi gerçek kapsamı söylesin (yalnız İstanbul mu, Marmara mı, Türkiye geneli mi?). Gelen cevaba göre `areaServed` tek seferde güncellenir: örneğin `[{"@type":"City","name":"İstanbul"},{"@type":"Country","name":"Türkiye"}]`. Hizmet sayfalarındaki `provider` düğümlerine de `"@id": "https://www.aymati.com.tr/#isletme"` eklenebilir. Bu 70 sayfayı etkiler; ayrı PR ve onayla yapılmalı.

## C. Düşük öncelik / bilgi

- **FAQPage:** 75 sayfada FAQPage var. `schema` skill'ine göre Google FAQ zengin sonucunu 7 Mayıs 2026'da kaldırdı; işaretleme zararlı değil, görünür SSS ile eşleşiyor, **kaldırılmadı**. Search Console'da FAQ raporunun kaybolması hata değil. Bundan sonra yeni sayfalara FAQPage eklemek zorunlu değil; görünür SSS bölümü yapay zekâ alıntısı için değerini koruyor.
- **BlogPosting:** 18 yazıda `datePublished`, `dateModified`, `image`, `author`, `publisher` tam. `publisher.logo` 1200×630 `og-image.png`'yi gösteriyor; kare logo (`img/gbp/logo-kare.png`) daha uygun olur (18 sayfa, toplu değişiklik, öneri). `author` kurum; mühendis adları gelince `Person` yazar eklenebilir.
- **`WebApplication` (Faraday aracı):** Uygun tip. `Offer.availability: InStock` hizmet için anlamsız ama zararsız; dokunulmadı.
- **Hakkımızda şeması:** Yalnız BreadcrumbList var. Yer tutucular giderilince `AboutPage` (`about` → `#isletme`) ve `Person` eklenmeli.
- **llms.txt keşfi:** Hiçbir sayfa `llms.txt`'ye bağlantı vermiyor. `agent-readiness.md`'ye göre ajanlar bu dosyaya çoğunlukla bir bağlantı üzerinden ulaşıyor. Öneri: alt bilgiye küçük bir "llms.txt" bağlantısı. Tüm sayfaları etkileyen bir şablon değişikliği olduğu için yapılmadı. İsteğe bağlı: `llms-full.txt`.
- **Yapay zekâ trafiği ölçümü:** GTM kurulu (`index.html:5`), telefon ve WhatsApp tıklamaları olay olarak gidiyor. GA4'te chatgpt.com, perplexity.ai, claude.ai, copilot.microsoft.com, gemini.google.com yönlendirmeleri için ayrı bir kanal grubu tanımlanırsa yapay zekâdan gelen teklif talepleri ayrıca görülebilir (site sahibi / GA4 yöneticisi).
- **Takvim dengesi:** "Bekliyor" durumundaki konuların bir kısmı periyodik muayene/iş hijyeni alanında (#20, #16, #15, #12, #6, #10), yani teknikisg.com'un alanında. Öncelikli kümelere (Statik #33, #34, #24, #23, #22; PKD #26, #4, #30, #19; Faraday #32, #29; Projelendirme #27, #28, #31, #9) öncelik verilmesi önerilir. Yeni konu önerilmedi.
- **PKD sayfasında bölüm numaraları** (`gno`) sırasız: 01, 02, 10, Ex, 04, 05 (`patlamadan-korunma-dokumani.html:478-495`). "10" yönetmelik maddesine gönderme olabilir; tasarım kararı, bilgi için.

## Site sahibinden beklenenler (özet)

1. Teklif formu uç noktası (KRİTİK, önceki denetimden açık).
2. Google İşletme Profili bağlantısı, varsa LinkedIn, posta kodu; profildeki saatlerin teyidi (A3).
3. Mühendis adları, EMO/MMO sicil numaraları, belge sınıfı (B3).
4. Ana sayfa başlık ve konumlandırma kararı (A1) ile ana sayfadaki keşif ücretinin durumu (A2).
5. Gerçek hizmet bölgesi kapsamı (B5).
6. Cloudflare Bots / AI Crawl Control ekran görüntüsü (B2).
7. Onay gerektiren içerik işleri: hub "İlgili yazılar" kartları (A4, A5), bölge sayfası genişletmeleri (B4), Rölöve kutusunun taşınması (B3).
