# Google Ads Kampanya Yapısı — Aymati Proje

Bu dosya reklam uzmanı ajanı tarafından her ay güncellenir. Ajanın hesaba erişimi yoktur; aşağıdaki yapı Google Ads Editor'e veya Google Ads arayüzüne elle girilmek üzere hazırlanmıştır. Bu dosya `site/` dışında olduğu için yayına girmez.

## Bu ay değişenler (Kasım 2026, 2. güncelleme — 5 Kasım)

- **Topraklama başlığı teyit edildi.** Site sahibi, topraklama ölçüm raporlarını EMO kayıtlı mühendisin imzaladığını teyit etti; 2.6 Topraklama Ölçümü grubundaki "EMO Kayıtlı Mühendis Raporu" başlığı olduğu gibi kullanılabilir (dosyada ayrıca bir teyit notu bulunmuyordu; değişiklik gerekmedi).
- **Yeni bölüm 5 — 2. aşama reklam grupları** (dönüşüm ölçümü kurulduktan sonra açılacak): 2.9 Vinç Statik Analizi, 2.10 Monoray / Vinç Yolu Statik Analizi, 2.11 Kaldırma Aparatı Statik Hesabı, 2.12 Fuar Standı Statik Analizi, 2.13 Sahne / Truss / Tribün Statik Analizi, 2.14 Tabela / Pilon Statik Hesabı. Her birinde 10–12 anahtar kelime, 15 başlık, 4 açıklama ve gruba özel negatifler var.
- **Yeni bölüm 6 — Bölge varyantları:** İkitelli OSB / Başakşehir, Hadımköy / Arnavutköy, Esenyurt / Beylikdüzü, Tuzla OSB için 5'er başlık ve 2'şer açıklama; mevcut gruplara ikinci RSA olarak eklenir. Hangi grubun bölge reklamının hangi sayfaya gideceği yönlendirme tablosunda.
- Tüm yeni başlık/açıklama karakter sayıları Python `len()` ile sayıldı (başlık ≤30, açıklama ≤90, görünen yol ≤15).
- Arama terimleri raporu (`sonuclar-2026-11.csv`) henüz yok; negatif/yeni anahtar kelime analizi yapılmadı. Bütçe rakamı yoktur.

### İlk sürüm (Kasım 2026)

- **İlk sürüm.** Daha önce kampanya ve arama terimleri raporu (`sonuclar-YYYY-AA.csv`) yok; bu nedenle negatif/yeni anahtar kelime analizi yapılmadı.
- 8 reklam grubu: istenen 6 hizmete ek olarak sitede bulunan statik analiz hizmet sayfalarından **Platform / Asma Kat Statik Analizi** ve **İskele Statik Analizi** ayrı grup yapıldı (her grup tek bir hizmet sayfasına gider).
- Diğer statik analiz sayfaları (fuar standı, sahne/truss/tribün, tabela/pilon, vinç, monoray vinç yolu, kaldırma aparatı) arama hacmi düşük ve dağınık olduğu için şimdilik reklam grubu yapılmadı; arama terimleri raporu geldikçe değerlendirilecek.
- Bütçe: **site sahibi belirleyecek.** Bu dosyada bütçe rakamı yoktur.

## 1. Kampanya ayarları

| Ayar | Öneri |
| --- | --- |
| Kampanya türü | Arama (Search). Hedef: Potansiyel müşteriler |
| Ağlar | **Yalnız Google Arama Ağı.** "Arama ağı iş ortakları" ve "Görüntülü Reklam Ağı" kutuları **kapalı** |
| Konum | İstanbul (il). İsteğe bağlı: Kocaeli, Tekirdağ (ayrı kampanya yerine aynı kampanyaya eklenip konum raporundan izlenebilir) |
| Konum seçenekleri | **"Varlık: Hedeflenen konumlarınızda bulunan veya buraları düzenli olarak ziyaret eden kişiler"** ("ilgilenen kişiler" seçeneği kapalı) |
| Dil | Türkçe |
| Reklam planlaması | Pazartesi–Cuma 08:00–18:30. Cumartesi-Pazar reklam yok |
| Bütçe | Site sahibi belirleyecek |
| Teklif stratejisi | Başlangıçta "Tıklamaları en üst düzeye çıkar" (TBM teklif sınırı ile) veya Manuel TBM; yeterli dönüşüm biriktikten sonra (yaklaşık 30 günde 15+ dönüşüm) "Dönüşümleri en üst düzeye çıkar"a geçiş önerilir |
| Otomatik oluşturulan öğeler / geniş eşleme | Kampanya düzeyinde "Geniş eşleme" **kapalı**; otomatik oluşturulan öğeler isteğe bağlı, fiyat/iddia üretmesine karşı ilk ay **kapalı** önerilir |
| Otomatik etiketleme | Açık (gclid) |
| Alan adı | https://www.aymati.com.tr |

### Dönüşümler

| Dönüşüm | Tetikleyici | Not |
| --- | --- | --- |
| Teklif formu gönderimi | `teklif.html` formunun başarılı gönderimi ("Talebiniz bize ulaştı" bildirimi) | Birincil dönüşüm |
| Telefon tıklaması | `tel:+905551428474` bağlantılarına tıklama | Birincil dönüşüm |
| WhatsApp tıklaması | `https://wa.me/905551428474` bağlantılarına tıklama | Birincil dönüşüm |
| (İsteğe bağlı) Reklamdan arama | Çağrı öğesindeki numaraya reklamdan arama, 30 sn+ | Google yönlendirme numarası Türkiye'de kullanılamıyorsa yalnız tıklama sayılır |

**Önemli:** Sitede şu an Google etiketi (gtag.js / Google Tag Manager) yok ve form başarılı gönderimde ayrı bir teşekkür sayfasına gitmiyor. Dönüşüm ölçümü için sitede ayrı bir değişiklik gerekir: tüm sayfalara Google etiketi eklenmesi ve form başarı anında, telefon ve WhatsApp tıklamalarında dönüşüm olaylarının gönderilmesi. Bu değişiklik ayrı bir PR olarak yapılmalı; Google Ads dönüşüm kimliği/etiketi site sahibinden alınmalıdır. Bu yapılmadan reklam açılırsa yalnız tıklama ölçülür.

### Hesap düzeyi öğeler (uzantılar)

- **Çağrı öğesi:** 0555 142 84 74 (yalnız reklam planlaması saatlerinde gösterilsin).
- **Site bağlantıları** (başlık ≤25, açıklama satırı ≤35 karakter):

| Başlık | Kr. | URL | Açıklama 1 | Kr. | Açıklama 2 | Kr. |
| --- | --- | --- | --- | --- | --- | --- |
| Teklif Alın | 11 | `teklif.html` | Formu doldurun, dönüş yapalım | 29 | Hizmet ve tesis bilgisi yeterli | 31 |
| Statik Analiz | 13 | `statik-analiz.html` | Raf, platform, iskele hesapları | 31 | MMO kayıtlı mühendis imzalı | 27 |
| Periyodik Muayene | 17 | `periyodik-muayene.html` | Forklift, vinç, kazan, tesisat | 30 | Yerinde kontrol ve rapor | 24 |
| Projelendirme | 13 | `projelendirme.html` | Elektrik ve mekanik projeler | 28 | EMO / MMO kayıtlı mühendis | 26 |
| Raf Statik Örnek Rapor | 22 | `raf-statik-analizi.html` | Örnek rapor sayfalarını görün | 29 | Raporda neler var inceleyin | 27 |
| Hizmet Bölgeleri | 16 | `hizmet-bolgeleri.html` | İkitelli, Hadımköy, Esenyurt | 28 | İstanbul batı yakası OSB'ler | 28 |

- **Açıklama metni öğeleri** (≤25 karakter):

| Metin | Kr. |
| --- | --- |
| EMO/MMO Kayıtlı Mühendis | 24 |
| Yerinde Rölöve ve Ölçüm | 23 |
| Fabrika, Depo ve Atölye | 23 |
| İstanbul Batı Yakası OSB | 24 |
| Teklif Formu ve WhatsApp | 24 |
| WhatsApp ile Ulaşın | 19 |

- **Yapılandırılmış snippet** (Başlık: Hizmetler): Elektrik Projesi, Raf Statik Analizi, PKD, Topraklama Ölçümü, Forklift Kontrolü, İş Hijyeni Ölçümü (her değer ≤25 karakter).

## 2. Reklam grupları

Her grupta bir **Duyarlı Arama Reklamı (RSA)**: 15 başlık (≤30 karakter), 4 açıklama (≤90 karakter). Karakter sayıları Python `len()` ile sayılmıştır (Türkçe harfler tek karakter). Anahtar kelimelerde `[...]` = tam eşleme, `"..."` = sıralı eşleme. Başlık sabitleme (pin) önerisi: 1. başlık konumuna grubun hizmet adı sabitlenebilir; diğerleri serbest bırakılmalı.

| # | Reklam grubu | Nihai URL | Görünen yol | Anahtar kelime |
| --- | --- | --- | --- | --- |
| 1 | Elektrik Projesi / Rölöve | https://www.aymati.com.tr/elektrik-ic-tesisat-projesi.html | /Elektrik-Proje/Rolove | 16 |
| 2 | Raf Statik Analizi | https://www.aymati.com.tr/raf-statik-analizi.html | /Raf-Statik/Analiz | 16 |
| 3 | Platform / Asma Kat Statik Analizi | https://www.aymati.com.tr/platform-statik-analizi.html | /Platform-Statik/Asma-Kat | 13 |
| 4 | İskele Statik Analizi | https://www.aymati.com.tr/iskele-statik-analizi.html | /Iskele-Statik/Rapor | 11 |
| 5 | Patlamadan Korunma Dokümanı | https://www.aymati.com.tr/patlamadan-korunma-dokumani.html | /PKD/ATEX | 14 |
| 6 | Topraklama Ölçümü | https://www.aymati.com.tr/topraklama-olcumu.html | /Topraklama/Olcum | 14 |
| 7 | Forklift Periyodik Kontrolü | https://www.aymati.com.tr/forklift-periyodik-kontrolu.html | /Forklift/Periyodik | 14 |
| 8 | İş Hijyeni Ölçümleri | https://www.aymati.com.tr/is-hijyeni-olcumleri.html | /Is-Hijyeni/Olcum | 16 |

### 2.1 Elektrik Projesi / Rölöve

- **Nihai URL:** https://www.aymati.com.tr/elektrik-ic-tesisat-projesi.html
- **Görünen yol:** www.aymati.com.tr/Elektrik-Proje/Rolove (14 / 6 karakter, sınır 15)

**Anahtar kelimeler (16)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[elektrik projesi]` | Tam |
| `[elektrik iç tesisat projesi]` | Tam |
| `[elektrik tesisat projesi]` | Tam |
| `[elektrik rölöve projesi]` | Tam |
| `[elektrik rölövesi]` | Tam |
| `[fabrika elektrik projesi]` | Tam |
| `[iş yeri elektrik projesi]` | Tam |
| `[elektrik projesi çizimi]` | Tam |
| `"elektrik projesi çizdirmek"` | Sıralı |
| `"elektrik iç tesisat projesi"` | Sıralı |
| `"elektrik rölöve"` | Sıralı |
| `"elektrik projesi istanbul"` | Sıralı |
| `"tek hat şeması çizimi"` | Sıralı |
| `"kısa devre hesabı"` | Sıralı |
| `"gerilim düşümü hesabı"` | Sıralı |
| `"kablo kesit hesabı"` | Sıralı |

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Elektrik İç Tesisat Projesi | 27 |
| 2 | Yerinde Rölöve ile Proje | 24 |
| 3 | EMO Kayıtlı Mühendis İmzalı | 27 |
| 4 | Elektrik Projesi İstanbul | 25 |
| 5 | Fabrika ve Depo Elektrik | 24 |
| 6 | Mevcut Tesise Rölöve Projesi | 28 |
| 7 | Kısa Devre ve Kesit Hesabı | 26 |
| 8 | Tek Hat ve Kolon Şeması | 23 |
| 9 | Gerilim Düşümü Hesapları | 24 |
| 10 | Kompanzasyon Hesabı Dahil | 25 |
| 11 | S.M.M. İmzalı Elektrik Proje | 28 |
| 12 | İşletmeniz İçin Teklif Alın | 27 |
| 13 | Batı Yakası OSB'lerine Hizmet | 29 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Mevcut tesisinizde yerinde rölöve alıyor, elektrik iç tesisat projesini hazırlıyoruz. | 85 |
| 2 | Kısa devre, gerilim düşümü, kablo kesit ve topraklama hesapları; tek hat şeması dahil. | 86 |
| 3 | Projeler EMO kayıtlı S.M.M. elektrik mühendisi tarafından hazırlanır ve imzalanır. | 82 |
| 4 | Fabrika, depo ve atölyeler için elektrik projesi. Formu doldurun, size dönüş yapalım. | 85 |

### 2.2 Raf Statik Analizi

- **Nihai URL:** https://www.aymati.com.tr/raf-statik-analizi.html
- **Görünen yol:** www.aymati.com.tr/Raf-Statik/Analiz (10 / 6 karakter, sınır 15)

**Anahtar kelimeler (16)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[raf statik analizi]` | Tam |
| `[raf statik hesabı]` | Tam |
| `[raf statik raporu]` | Tam |
| `[raf statik analiz raporu]` | Tam |
| `[depo raf statik hesabı]` | Tam |
| `[palet rafı statik hesabı]` | Tam |
| `[raf yük kapasite etiketi]` | Tam |
| `[raf taşıma kapasitesi hesabı]` | Tam |
| `[raf deprem hesabı]` | Tam |
| `"raf statik"` | Sıralı |
| `"raf statik hesap"` | Sıralı |
| `"depo raf statik"` | Sıralı |
| `"raf yük etiketi"` | Sıralı |
| `"palet raf statik"` | Sıralı |
| `"en 15512 raf hesabı"` | Sıralı |
| `"raf ankraj hesabı"` | Sıralı |

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Raf Statik Analizi | 18 |
| 2 | Raf Statik Hesabı ve Raporu | 27 |
| 3 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 4 | Raflar Yerinde Ölçülür | 22 |
| 5 | Depo Rafı Statik Raporu | 23 |
| 6 | Palet Rafı Taşıma Kapasitesi | 28 |
| 7 | Raf Yük Kapasite Etiketi | 24 |
| 8 | TS EN 15512'ye Göre Hesap | 25 |
| 9 | Deprem Hesabı ve Ankraj | 23 |
| 10 | Örnek Raporu İnceleyin | 22 |
| 11 | İSG Denetimi İçin Raf Raporu | 28 |
| 12 | Raf Statik Teklifi Alın | 23 |
| 13 | İstanbul Depolarına Hizmet | 26 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Depo ve palet rafları için statik hesap ve rapor. MMO kayıtlı makina mühendisi imzalı. | 86 |
| 2 | Raf ölçüleri, göz ve kat düzeni, ankraj ve zemin yerinde incelenir, ardından modellenir. | 88 |
| 3 | TS EN 15512, TS EN 15635 ve TBDY 2018 deprem hesabı; yük kapasite etiketi bilgileri. | 84 |
| 4 | Sitemizdeki örnek raporu inceleyin, raf bilgilerinizi gönderin, size dönüş yapalım. | 83 |

### 2.3 Platform / Asma Kat Statik Analizi

- **Nihai URL:** https://www.aymati.com.tr/platform-statik-analizi.html
- **Görünen yol:** www.aymati.com.tr/Platform-Statik/Asma-Kat (15 / 8 karakter, sınır 15)

**Anahtar kelimeler (13)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[platform statik analizi]` | Tam |
| `[platform statik hesabı]` | Tam |
| `[asma kat statik hesabı]` | Tam |
| `[asma kat statik raporu]` | Tam |
| `[mezanin statik hesabı]` | Tam |
| `[çelik platform statik hesabı]` | Tam |
| `[çelik asma kat statik]` | Tam |
| `[mezanin kat statik raporu]` | Tam |
| `"asma kat statik"` | Sıralı |
| `"mezanin statik"` | Sıralı |
| `"çelik platform statik"` | Sıralı |
| `"asma kat taşıma kapasitesi"` | Sıralı |
| `"platform taşıma kapasitesi"` | Sıralı |

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Platform Statik Analizi | 23 |
| 2 | Asma Kat Statik Hesabı | 22 |
| 3 | Mezanin Kat Statik Raporu | 25 |
| 4 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 5 | Çelik Platform Taşıma Hesabı | 28 |
| 6 | Asma Kat Yük Kapasitesi | 23 |
| 7 | Yük, Gerilme, Deformasyon | 25 |
| 8 | Eurocode 3'e Göre Hesap | 23 |
| 9 | Mevcut Asma Katlar İçin | 23 |
| 10 | İSG Denetimi İçin Rapor | 23 |
| 11 | E-İmzalı PDF Rapor | 18 |
| 12 | Statik Rapor Teklifi Alın | 25 |
| 13 | İstanbul Tesislerine Hizmet | 27 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Çelik platform, asma kat ve mezaninler için taşıma kapasitesi hesabı ve statik rapor. | 85 |
| 2 | Yük, gerilme ve deformasyon analizi Eurocode 3 ve TS 498'e göre yapılır. | 72 |
| 3 | Rapor MMO kayıtlı makina mühendisi tarafından hazırlanır ve e-imzalı PDF teslim edilir. | 87 |
| 4 | Mevcut asma katınızın bilgilerini gönderin, kapsamı birlikte belirleyip dönüş yapalım. | 86 |

### 2.4 İskele Statik Analizi

- **Nihai URL:** https://www.aymati.com.tr/iskele-statik-analizi.html
- **Görünen yol:** www.aymati.com.tr/Iskele-Statik/Rapor (13 / 5 karakter, sınır 15)

**Anahtar kelimeler (11)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[iskele statik hesabı]` | Tam |
| `[iskele statik raporu]` | Tam |
| `[iskele statik analizi]` | Tam |
| `[cephe iskelesi statik hesabı]` | Tam |
| `[iş iskelesi statik hesabı]` | Tam |
| `[iskele statik proje]` | Tam |
| `[iskele rüzgar hesabı]` | Tam |
| `"iskele statik"` | Sıralı |
| `"cephe iskelesi statik"` | Sıralı |
| `"iskele statik rapor"` | Sıralı |
| `"iskele stabilite hesabı"` | Sıralı |

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | İskele Statik Hesabı | 20 |
| 2 | İskele Statik Raporu | 20 |
| 3 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 4 | Cephe İskelesi Statik Hesap | 27 |
| 5 | İş İskelesi Statik Raporu | 25 |
| 6 | Yük ve Rüzgâr Hesabı | 20 |
| 7 | Stabilite Kontrolü Dahil | 24 |
| 8 | Eurocode ve TS 498'e Göre | 25 |
| 9 | Şantiye ve Tesisler İçin | 24 |
| 10 | E-İmzalı PDF Rapor | 18 |
| 11 | İskele Statik Teklifi Alın | 26 |
| 12 | İstanbul Şantiyelerine Hizmet | 29 |
| 13 | İskele Statik Hesap İstanbul | 28 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Cephe ve iş iskeleleri için yük, rüzgâr ve stabilite hesabı içeren iskele statik raporu. | 88 |
| 2 | Hesaplar Eurocode ve TS 498'e göre yapılır; rapor MMO kayıtlı mühendis imzalıdır. | 81 |
| 3 | İskele tipi, yükseklik ve bağlantı bilgilerini gönderin, kapsamı birlikte belirleyelim. | 87 |
| 4 | Şantiye ve tesisler için iskele statik raporu. Formu doldurun ya da bizi arayın. | 80 |

### 2.5 Patlamadan Korunma Dokümanı

- **Nihai URL:** https://www.aymati.com.tr/patlamadan-korunma-dokumani.html
- **Görünen yol:** www.aymati.com.tr/PKD/ATEX (3 / 4 karakter, sınır 15)

**Anahtar kelimeler (14)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[patlamadan korunma dokümanı]` | Tam |
| `[patlamadan korunma dökümanı]` | Tam |
| `[pkd hazırlama]` | Tam |
| `[patlamadan korunma dokümanı hazırlama]` | Tam |
| `[atex bölge sınıflandırması]` | Tam |
| `[tehlikeli bölge sınıflandırması]` | Tam |
| `[patlama riski değerlendirmesi]` | Tam |
| `[pkd raporu]` | Tam |
| `"patlamadan korunma dokümanı"` | Sıralı |
| `"patlamadan korunma dökümanı"` | Sıralı |
| `"pkd hazırlayan firma"` | Sıralı |
| `"atex zone sınıflandırması"` | Sıralı |
| `"patlayıcı ortam risk değerlendirmesi"` | Sıralı |
| `"patlamadan korunma" istanbul` | Sıralı |

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Patlamadan Korunma Dokümanı | 27 |
| 2 | PKD Hazırlama | 13 |
| 3 | ATEX Bölge Sınıflandırması | 26 |
| 4 | Zone 0, 1, 2, 20, 21, 22 | 24 |
| 5 | Patlama Riski Değerlendirmesi | 29 |
| 6 | Tesisiniz Yerinde İncelenir | 27 |
| 7 | Tutuşturucu Kaynak Analizi | 26 |
| 8 | Ex Ekipman Uygunluğu | 20 |
| 9 | Bölge Haritaları Dahil | 22 |
| 10 | Uygunsuzluk ve Önlem Listesi | 28 |
| 11 | Boya, Toz, Solvent, LPG Alanı | 29 |
| 12 | PKD İçin Teklif Alın | 20 |
| 13 | İstanbul Tesislerine Hizmet | 27 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Patlamadan korunma dokümanı: ATEX bölge sınıflandırması ve patlama riski değerlendirmesi. | 89 |
| 2 | Prosesleri, depolama alanlarını, havalandırmayı ve ekipmanları yerinde inceliyoruz. | 83 |
| 3 | Tutuşturucu kaynak analizi, Ex ekipman uygunluğu, bölge haritaları ve önlem önerileri. | 86 |
| 4 | PKD işe başlamadan önce hazırlanır, önemli değişikliklerde güncellenir. Teklif alın. | 84 |

### 2.6 Topraklama Ölçümü

- **Nihai URL:** https://www.aymati.com.tr/topraklama-olcumu.html
- **Görünen yol:** www.aymati.com.tr/Topraklama/Olcum (10 / 5 karakter, sınır 15)

**Anahtar kelimeler (14)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[topraklama ölçümü]` | Tam |
| `[topraklama ölçüm raporu]` | Tam |
| `[topraklama raporu]` | Tam |
| `[topraklama direnci ölçümü]` | Tam |
| `[topraklama ölçümü yaptırmak]` | Tam |
| `[topraklama periyodik kontrol]` | Tam |
| `[topraklama tesisatı ölçümü]` | Tam |
| `[fabrika topraklama ölçümü]` | Tam |
| `"topraklama ölçümü"` | Sıralı |
| `"topraklama raporu"` | Sıralı |
| `"topraklama ölçüm" istanbul` | Sıralı |
| `"çevrim empedansı ölçümü"` | Sıralı |
| `"süreklilik ölçümü"` | Sıralı |
| `"topraklama kontrolü"` | Sıralı |

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Topraklama Ölçümü | 17 |
| 2 | Topraklama Ölçüm Raporu | 23 |
| 3 | EMO Kayıtlı Mühendis Raporu | 27 |
| 4 | Yerinde Ölçüm ve Test | 21 |
| 5 | Topraklama Direnci Ölçümü | 25 |
| 6 | Çevrim Empedansı Ölçümü | 23 |
| 7 | Süreklilik Ölçümü Dahil | 23 |
| 8 | Kalibrasyonlu Cihazlarla | 24 |
| 9 | Yıllık Periyodik Kontrol | 24 |
| 10 | Fabrika ve Depolar İçin | 23 |
| 11 | İSG Denetimi İçin Rapor | 23 |
| 12 | Ölçüm İçin Teklif Alın | 22 |
| 13 | Batı Yakası OSB'lerine Hizmet | 29 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Topraklama direnci, çevrim empedansı ve süreklilik ölçümü; yönetmeliğe uygun rapor. | 83 |
| 2 | Mühendislerimiz tesisinizde yerinde ölçer, test eder ve topraklama raporunu hazırlar. | 85 |
| 3 | Raporda kullanılan kalibrasyonlu ölçüm cihazlarının bilgileri yer alır. | 71 |
| 4 | Topraklama ölçümü yılda bir yapılması gereken periyodik kontroldür. Teklif alın. | 80 |

### 2.7 Forklift Periyodik Kontrolü

- **Nihai URL:** https://www.aymati.com.tr/forklift-periyodik-kontrolu.html
- **Görünen yol:** www.aymati.com.tr/Forklift/Periyodik (8 / 9 karakter, sınır 15)

**Anahtar kelimeler (14)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[forklift periyodik kontrolü]` | Tam |
| `[forklift periyodik kontrol]` | Tam |
| `[forklift periyodik muayene]` | Tam |
| `[forklift muayene raporu]` | Tam |
| `[forklift kontrol raporu]` | Tam |
| `[forklift periyodik kontrol raporu]` | Tam |
| `[forklift yıllık kontrol]` | Tam |
| `[akülü forklift periyodik kontrol]` | Tam |
| `[dizel forklift periyodik kontrol]` | Tam |
| `"forklift periyodik"` | Sıralı |
| `"forklift muayene"` | Sıralı |
| `"forklift kontrol raporu"` | Sıralı |
| `"forklift yük testi"` | Sıralı |
| `"istif makinesi periyodik kontrol"` | Sıralı |

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Forklift Periyodik Kontrolü | 27 |
| 2 | Forklift Muayene Raporu | 23 |
| 3 | Makina Mühendisi Kontrolü | 25 |
| 4 | Yerinde Kontrol ve Yük Testi | 28 |
| 5 | Akülü, Dizel ve LPG Forklift | 28 |
| 6 | Fren, Direksiyon, Hidrolik | 26 |
| 7 | Direk, Zincir ve Çatal | 22 |
| 8 | İş Ekipmanları Yönetmeliği | 26 |
| 9 | Forklift Kontrolü İstanbul | 26 |
| 10 | Depo ve Fabrikalar İçin | 23 |
| 11 | İSG Denetimi İçin Rapor | 23 |
| 12 | Forklift Kontrol Teklifi | 24 |
| 13 | Batı Yakası OSB'lerine Hizmet | 29 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Akülü, dizel ve LPG forkliftlerin periyodik kontrolü ve forklift kontrol raporu. | 80 |
| 2 | Fren, direksiyon, direk ve zincir, çatal aşınması, hidrolik, ikazlar ve yük testi. | 82 |
| 3 | Mühendislerimiz forkliftleri işletmenizde yerinde kontrol eder, test eder ve raporlar. | 86 |
| 4 | İş Ekipmanları Yönetmeliği'ne uygun rapor. Forklift sayınızı yazın, teklif gönderelim. | 86 |

### 2.8 İş Hijyeni Ölçümleri

- **Nihai URL:** https://www.aymati.com.tr/is-hijyeni-olcumleri.html
- **Görünen yol:** www.aymati.com.tr/Is-Hijyeni/Olcum (10 / 5 karakter, sınır 15)

**Anahtar kelimeler (16)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[iş hijyeni ölçümleri]` | Tam |
| `[iş hijyeni ölçümü]` | Tam |
| `[gürültü ölçümü]` | Tam |
| `[kişisel gürültü ölçümü]` | Tam |
| `[ortam gürültü ölçümü]` | Tam |
| `[toz ölçümü]` | Tam |
| `[kişisel toz ölçümü]` | Tam |
| `[voc ölçümü]` | Tam |
| `[titreşim ölçümü]` | Tam |
| `[aydınlatma ölçümü]` | Tam |
| `[termal konfor ölçümü]` | Tam |
| `"iş hijyeni ölçüm"` | Sıralı |
| `"işyeri ortam ölçümü"` | Sıralı |
| `"gürültü ölçümü" işyeri` | Sıralı |
| `"toz ölçümü" işyeri` | Sıralı |
| `"ortam ölçümleri" isg` | Sıralı |

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | İş Hijyeni Ölçümleri | 20 |
| 2 | Gürültü ve Toz Ölçümü | 21 |
| 3 | Kişisel ve Ortam Ölçümleri | 26 |
| 4 | VOC ve Gaz Ölçümü | 17 |
| 5 | Titreşim Ölçümü | 15 |
| 6 | Aydınlatma ve Termal Konfor | 27 |
| 7 | Manyetik Alan Ölçümü | 20 |
| 8 | Ağır Metal Ölçümü | 17 |
| 9 | Risk Değerlendirmesi İçin | 25 |
| 10 | İSG Uzmanları İçin Ölçüm | 24 |
| 11 | Fabrika ve Atölyeler İçin | 25 |
| 12 | Ölçüm Planı ve Teklif | 21 |
| 13 | İstanbul Tesislerine Hizmet | 27 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Kişisel ve ortam gürültü, toz, VOC ve gaz ölçümleri ile titreşim ölçümü. | 72 |
| 2 | Manyetik alan, ağır metal, termal konfor ve aydınlatma ölçümleri de yapılır. | 76 |
| 3 | Risk değerlendirmenize dayanak olacak ölçümleri işyerinizdeki işlere göre planlıyoruz. | 86 |
| 4 | Hangi ölçümlere ihtiyacınız olduğunu yazın, kapsamı birlikte belirleyip dönüş yapalım. | 86 |

## 3. Ortak negatif anahtar kelimeler

Hesap düzeyinde bir negatif anahtar kelime listesi (ör. "Aymati ortak negatifler") oluşturup kampanyaya bağlayın. Tümü **sıralı eşleme** önerilir.

| Negatif kelime | Gerekçe |
| --- | --- |
| `"iş ilanı"` | İş arayanlar |
| `"iş ilanları"` | İş arayanlar |
| `"eleman"` | İş arayanlar |
| `"eleman arıyor"` | İş arayanlar |
| `"kariyer"` | İş arayanlar |
| `"maaş"` | İş arayanlar |
| `"maaşları"` | İş arayanlar |
| `"staj"` | Öğrenci |
| `"stajyer"` | Öğrenci |
| `"kurs"` | Eğitim arayanlar |
| `"eğitimi"` | Eğitim arayanlar |
| `"sertifika eğitimi"` | Eğitim arayanlar |
| `"sertifika"` | Eğitim/belge arayanlar |
| `"sertifikası"` | Eğitim/belge arayanlar |
| `"belgesi nasıl alınır"` | Yetki belgesi arayan mühendis/teknisyen |
| `"ders"` | Öğrenci |
| `"ders notları"` | Öğrenci |
| `"sınav"` | Öğrenci |
| `"sınav soruları"` | Öğrenci |
| `"nasıl yapılır pdf"` | Kendin-yap / doküman arayanlar |
| `"pdf"` | Doküman arayanlar |
| `"ppt"` | Doküman arayanlar |
| `"sunum"` | Doküman arayanlar |
| `"örnek pdf"` | Doküman arayanlar |
| `"indir"` | Doküman/yazılım arayanlar |
| `"excel"` | Hesap şablonu arayanlar |
| `"ücretsiz"` | Ücretsiz hizmet arayanlar |
| `"bedava"` | Ücretsiz hizmet arayanlar |
| `"yönetmelik pdf"` | Mevzuat metni arayanlar |
| `"tez"` | Akademik |
| `"ödev"` | Öğrenci |
| `"ekşi"` | Bilgi/forum |
| `"yorumları"` | Bilgi/forum |
| `"hobi"` | Alakasız |
| `"ev"` | Konut (hedef: sanayi) |
| `"daire"` | Konut (hedef: sanayi) |
| `"apartman"` | Konut (hedef: sanayi) |
| `"villa"` | Konut (hedef: sanayi) |
| `"program indir"` | Yazılım arayanlar |
| `"dwg"` | Çizim dosyası arayanlar |
| `"autocad"` | Çizim/yazılım arayanlar |
| `"youtube"` | Video arayanlar |
| `"video"` | Video arayanlar |
| `"nedir"` | Bilgi amaçlı (blog trafiğine bırakılır); ilk ay izlenip gerekirse kaldırılır |

Not: "nedir" ve "ev" negatifleri dikkatle izlenmeli; "ev" kelimesi tam kelime olarak eşleşir ("elektrik projesi ev" gibi aramaları keser, "evrak" gibi kelimeleri kesmez). Rakip firma adları anahtar kelime yapılmamıştır; arama terimleri raporunda görülürse negatife eklenmesi değerlendirilecektir.

## 4. Arama terimleri raporu ile aylık güncelleme

Google Ads > Anahtar kelimeler > Arama terimleri raporunu (son 30 gün) CSV olarak indirip `pazarlama/reklam/sonuclar-YYYY-AA.csv` adıyla depoya ekleyin (ör. `sonuclar-2026-11.csv`). Sütunlar: arama terimi, reklam grubu, gösterim, tıklama, maliyet, dönüşüm. Bir sonraki ayki güncellemede:

- Tıklama alıp dönüşüm getirmeyen ve alakasız terimler negatif listesine önerilir.
- Dönüşüm getiren terimler ilgili gruba yeni anahtar kelime olarak eklenir.
- Değişiklikler bu dosyanın en üstündeki "Bu ay değişenler" bölümüne yazılır.

## 5. 2. aşama (dönüşüm ölçümü kurulduktan sonra açılacak)

Bu gruplar ilk sürümde dışarıda bırakılan statik analiz sayfaları içindir. **Dönüşüm ölçümü (Google etiketi + form / telefon / WhatsApp olayları) sitede çalışır hale gelmeden açılmamalıdır**; arama hacimleri düşük ve dağınık olduğundan hangi grubun teklif getirdiği ancak dönüşüm verisiyle görülebilir. Açıldıklarında aynı kampanyaya (aynı ayarlar, aynı negatif liste) eklenir; her grup tek bir hizmet sayfasına gider. Tüm sayfaların `site/` içinde bulunduğu kontrol edildi. Raporlar sitede belirtildiği gibi MMO kayıtlı makina mühendisi imzalıdır.

Not: Fuar standı ve sahne/truss/tribün aramaları İstanbul dışından (stand ve organizasyon firmaları) da gelebilir; konum hedefi değiştirilmedi, arama terimleri ve konum raporuna göre değerlendirilecek.

| # | Reklam grubu | Nihai URL | Görünen yol | Anahtar kelime |
| --- | --- | --- | --- | --- |
| 2.9 | Vinç Statik Analizi | https://www.aymati.com.tr/vinc-statik-analizi.html | /Vinc-Statik/Zemin-Hesabi | 11 |
| 2.10 | Monoray / Vinç Yolu Statik Analizi | https://www.aymati.com.tr/monoray-vinc-yolu-statik-analizi.html | /Monoray/Vinc-Yolu | 10 |
| 2.11 | Kaldırma Aparatı Statik Hesabı | https://www.aymati.com.tr/kaldirma-aparati-statik-hesabi.html | /Kaldirma-Aparat/Statik-Hesap | 11 |
| 2.12 | Fuar Standı Statik Analizi | https://www.aymati.com.tr/fuar-standi-statik-analizi.html | /Fuar-Standi/Statik-Rapor | 10 |
| 2.13 | Sahne / Truss / Tribün Statik Analizi | https://www.aymati.com.tr/sahne-truss-tribun-statik-analizi.html | /Sahne-Truss/Tribun | 12 |
| 2.14 | Tabela / Pilon Statik Hesabı | https://www.aymati.com.tr/tabela-pilon-statik-hesabi.html | /Tabela-Pilon/Statik-Hesap | 11 |

### 2.9 Vinç Statik Analizi

- **Nihai URL:** https://www.aymati.com.tr/vinc-statik-analizi.html
- **Görünen yol:** www.aymati.com.tr/Vinc-Statik/Zemin-Hesabi (11 / 12 karakter, sınır 15)

**Anahtar kelimeler (11)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[vinç statik analizi]` | Tam |
| `[vinç statik hesabı]` | Tam |
| `[kule vinç temel hesabı]` | Tam |
| `[kule vinç temeli statik]` | Tam |
| `[mobil vinç ayak yükü]` | Tam |
| `[vinç ayak yükü hesabı]` | Tam |
| `[vinç zemin hesabı]` | Tam |
| `"vinç statik rapor"` | Sıralı |
| `"kule vinç temel hesabı"` | Sıralı |
| `"vinç ayak basıncı"` | Sıralı |
| `"vinç zemin basıncı hesabı"` | Sıralı |

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Vinç Statik Analizi | 19 |
| 2 | Kule Vinç Temel Hesabı | 22 |
| 3 | Mobil Vinç Ayak Yükü Hesabı | 27 |
| 4 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 5 | Vinç Zemin Basıncı Hesabı | 25 |
| 6 | Ankraj ve Temel Kontrolü | 24 |
| 7 | Kurulum Öncesi Statik Rapor | 27 |
| 8 | Döşeme Üzerine Vinç Kontrolü | 28 |
| 9 | Üretici Yük Tablolarıyla | 24 |
| 10 | Şantiye İçin Statik Rapor | 25 |
| 11 | Altlık Plakası Ölçüsü Hesabı | 28 |
| 12 | Vinç Hesabı İçin Teklif Alın | 28 |
| 13 | Batı Yakası OSB'lerine Hizmet | 29 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Kule vinç temeli, ankraj, mobil vinç ayak yükü ve zemin basıncını hesaplıyoruz. | 79 |
| 2 | Vinç kurulmadan önce MMO kayıtlı makina mühendisi imzalı statik hesap raporu hazırlanır. | 88 |
| 3 | Döşeme, rampa veya bodrum üzerine kurulacak vinçte yapının taşıma kapasitesi kontrolü. | 86 |
| 4 | Vinç modeli, kaldırma planı ve zemin bilgisini gönderin, kapsamı belirleyip dönüş yapalım. | 90 |

### 2.10 Monoray / Vinç Yolu Statik Analizi

- **Nihai URL:** https://www.aymati.com.tr/monoray-vinc-yolu-statik-analizi.html
- **Görünen yol:** www.aymati.com.tr/Monoray/Vinc-Yolu (7 / 9 karakter, sınır 15)

**Anahtar kelimeler (10)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[monoray statik hesabı]` | Tam |
| `[monoray statik analizi]` | Tam |
| `[vinç yolu statik hesabı]` | Tam |
| `[vinç yolu kirişi hesabı]` | Tam |
| `[vinç yolu statik analizi]` | Tam |
| `[köprülü vinç yolu hesabı]` | Tam |
| `[monoray hesabı]` | Tam |
| `"monoray statik"` | Sıralı |
| `"vinç yolu kirişi" hesap` | Sıralı |
| `"caraskal rayı hesabı"` | Sıralı |

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Monoray Statik Analizi | 22 |
| 2 | Vinç Yolu Kirişi Hesabı | 23 |
| 3 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 4 | Yerinde Ölçüm ile Statik Hesap | 30 |
| 5 | Köprülü Vinç Yolu Kontrolü | 26 |
| 6 | Monoray Rayı Statik Raporu | 26 |
| 7 | Sehim ve Bağlantı Kontrolü | 26 |
| 8 | Kapasite Artırımı Hesabı | 24 |
| 9 | Konsol Vinç Taşıyıcı Hesabı | 27 |
| 10 | Fabrika ve Atölyeler İçin | 25 |
| 11 | Tekerlek ve Fren Yükleriyle | 27 |
| 12 | Statik Rapor İçin Teklif Alın | 29 |
| 13 | Batı Yakası OSB'lerine Hizmet | 29 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Monoray rayı, vinç yolu kirişi ve konsol vinç taşıyıcısını sahada ölçüp hesaplıyoruz. | 85 |
| 2 | Tekerlek yükleri, fren kuvvetleri, sehim ve ray bağlantıları raporda kontrol edilir. | 84 |
| 3 | Raporlar MMO kayıtlı makina mühendisi tarafından hazırlanır ve imzalanır. | 73 |
| 4 | Yeni vinç veya kapasite artırımı planlıyorsanız mevcut yapıyı birlikte değerlendirelim. | 87 |

### 2.11 Kaldırma Aparatı Statik Hesabı

- **Nihai URL:** https://www.aymati.com.tr/kaldirma-aparati-statik-hesabi.html
- **Görünen yol:** www.aymati.com.tr/Kaldirma-Aparat/Statik-Hesap (15 / 12 karakter, sınır 15)

**Anahtar kelimeler (11)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[kaldırma aparatı statik hesabı]` | Tam |
| `[travers statik hesabı]` | Tam |
| `[kaldırma kirişi hesabı]` | Tam |
| `[kaldırma kulağı hesabı]` | Tam |
| `[kaldırma aparatı hesabı]` | Tam |
| `[spreader beam hesabı]` | Tam |
| `[travers hesabı]` | Tam |
| `"kaldırma aparatı" statik` | Sıralı |
| `"travers" statik rapor` | Sıralı |
| `"kaldırma kulağı" hesap` | Sıralı |
| `"wll hesabı"` | Sıralı |

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Kaldırma Aparatı Statik Hesabı | 30 |
| 2 | Travers ve Kaldırma Kirişi | 26 |
| 3 | Kaldırma Kulağı Hesabı | 22 |
| 4 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 5 | Çalışma Yük Sınırı (WLL) | 24 |
| 6 | Atölye İmalatı Aparatlara | 25 |
| 7 | Etiket Bilgisi Raporda | 22 |
| 8 | Kaynak ve Pim Kontrolü | 22 |
| 9 | Yerinde Ölçüm ile Hesap | 23 |
| 10 | Periyodik Kontrol Eksiğine | 26 |
| 11 | Güçlendirme Önerisi Dahil | 25 |
| 12 | Aparat İçin Teklif Alın | 23 |
| 13 | Batı Yakası OSB'lerine Hizmet | 29 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Travers, kaldırma kirişi, kaldırma kulağı ve özel aparatların taşıma kapasitesi hesabı. | 87 |
| 2 | Aparatın üzerine yazılacak çalışma yük sınırı (WLL) ve etiket bilgileri raporda yer alır. | 89 |
| 3 | Gövde, kaynak, pim ve delik bölgeleri kontrol edilir; MMO kayıtlı mühendis imzalı rapor. | 88 |
| 4 | Aparatı sahada ölçüyor veya imalat çiziminden hesaplıyoruz. Formu doldurun, dönüş yapalım. | 90 |

### 2.12 Fuar Standı Statik Analizi

- **Nihai URL:** https://www.aymati.com.tr/fuar-standi-statik-analizi.html
- **Görünen yol:** www.aymati.com.tr/Fuar-Standi/Statik-Rapor (11 / 12 karakter, sınır 15)

**Anahtar kelimeler (10)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[fuar standı statik analizi]` | Tam |
| `[fuar standı statik rapor]` | Tam |
| `[fuar standı statik hesabı]` | Tam |
| `[çift katlı stand statik]` | Tam |
| `[çift katlı fuar standı statik]` | Tam |
| `[stand statik raporu]` | Tam |
| `[fuar standı statik proje]` | Tam |
| `"fuar standı statik"` | Sıralı |
| `"çift katlı stand" statik` | Sıralı |
| `"stand statik hesap"` | Sıralı |

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Fuar Standı Statik Analizi | 26 |
| 2 | Çift Katlı Stand Statik Rapor | 29 |
| 3 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 4 | Teknik Ofise Sunulacak Rapor | 28 |
| 5 | Kurulumdan Önce Statik Rapor | 28 |
| 6 | Yüksek Stand Statik Hesabı | 26 |
| 7 | Asma Kat ve Merdiven Kontrolü | 29 |
| 8 | Korkuluk Yeterlilik Hesabı | 26 |
| 9 | Çelik ve Alüminyum Stand | 24 |
| 10 | Stand Firmalarına Hizmet | 24 |
| 11 | Fuar Şartnamesine Uygun Rapor | 29 |
| 12 | Stand Projeniz İçin Teklif | 26 |
| 13 | İstanbul Fuarları İçin | 22 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Fuar merkezi çift katlı veya yüksek standınız için statik rapor mu istedi? Hesaplıyoruz. | 88 |
| 2 | Kolon, kiriş, ikinci kat döşemesi, merdiven ve korkuluklar ziyaretçi yüküne göre kontrol. | 89 |
| 3 | Teknik ofise sunulacak rapor MMO kayıtlı makina mühendisi tarafından imzalanır. | 79 |
| 4 | Stand planı, kesit ve malzeme bilgisini gönderin; fuar takvimine göre planlayalım. | 82 |

### 2.13 Sahne / Truss / Tribün Statik Analizi

- **Nihai URL:** https://www.aymati.com.tr/sahne-truss-tribun-statik-analizi.html
- **Görünen yol:** www.aymati.com.tr/Sahne-Truss/Tribun (11 / 6 karakter, sınır 15)

**Anahtar kelimeler (12)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[sahne statik analizi]` | Tam |
| `[sahne statik raporu]` | Tam |
| `[truss statik hesabı]` | Tam |
| `[truss statik rapor]` | Tam |
| `[tribün statik analizi]` | Tam |
| `[geçici tribün statik]` | Tam |
| `[led ekran kulesi statik]` | Tam |
| `[konser sahnesi statik]` | Tam |
| `"sahne statik"` | Sıralı |
| `"truss statik"` | Sıralı |
| `"tribün statik"` | Sıralı |
| `"etkinlik statik rapor"` | Sıralı |

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Sahne ve Truss Statik Analizi | 29 |
| 2 | Geçici Tribün Statik Raporu | 27 |
| 3 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 4 | Truss Çatı Statik Hesabı | 24 |
| 5 | LED Ekran Kulesi Hesabı | 23 |
| 6 | Rüzgâr ve Asma Yük Kontrolü | 27 |
| 7 | Etkinlik Öncesi Statik Rapor | 28 |
| 8 | Seyirci Yükü Hesabı | 19 |
| 9 | Balast İhtiyacı Hesaplanır | 26 |
| 10 | Belediye ve Sigorta İçin | 24 |
| 11 | Organizasyon Firmalarına | 24 |
| 12 | Etkinliğiniz İçin Teklif Alın | 29 |
| 13 | İstanbul Etkinlikleri İçin | 26 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Konser sahnesi, truss çatı, LED ekran kulesi ve geçici tribünler için statik analiz. | 84 |
| 2 | Ses, ışık ve ekran gibi asılan yükler, rüzgâr ve seyirci yükü hesaba katılır. | 77 |
| 3 | Truss, kule, ayak ve balast ihtiyacı hesaplanır; MMO kayıtlı mühendis imzalı rapor. | 83 |
| 4 | Etkinlik tarihini ve ekipman listesini gönderin, kapsamı belirleyip size dönüş yapalım. | 87 |

### 2.14 Tabela / Pilon Statik Hesabı

- **Nihai URL:** https://www.aymati.com.tr/tabela-pilon-statik-hesabi.html
- **Görünen yol:** www.aymati.com.tr/Tabela-Pilon/Statik-Hesap (12 / 12 karakter, sınır 15)

**Anahtar kelimeler (11)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[tabela statik hesabı]` | Tam |
| `[tabela statik raporu]` | Tam |
| `[pilon statik hesabı]` | Tam |
| `[totem statik hesabı]` | Tam |
| `[reklam panosu statik hesabı]` | Tam |
| `[çatı tabelası statik rapor]` | Tam |
| `[tabela statik proje]` | Tam |
| `"tabela statik"` | Sıralı |
| `"pilon statik"` | Sıralı |
| `"totem statik"` | Sıralı |
| `"belediye tabela" statik rapor` | Sıralı |

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Tabela Statik Hesabı | 20 |
| 2 | Pilon ve Totem Statik Hesabı | 28 |
| 3 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 4 | Belediye İçin Statik Rapor | 26 |
| 5 | Çatı Tabelası Statik Rapor | 26 |
| 6 | Rüzgâr Yükü Hesabı | 18 |
| 7 | Ankraj ve Temel Kontrolü | 24 |
| 8 | Reklam Panosu Statik Hesap | 26 |
| 9 | Cephe Tabelası Hesabı | 21 |
| 10 | Tabela Firmalarına Hizmet | 25 |
| 11 | Taşıyıcı Konstrüksiyon | 22 |
| 12 | Tabelanız İçin Teklif Alın | 26 |
| 13 | İstanbul Geneline Hizmet | 24 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Çatı tabelası, cephe tabelası, reklam panosu ve pilon için statik hesap raporu. | 79 |
| 2 | Rüzgâr yükü, taşıyıcı profiller, bağlantılar, ankraj cıvataları ve temel hesaplanır. | 84 |
| 3 | Belediye başvurusu için MMO kayıtlı makina mühendisi imzalı statik rapor hazırlanır. | 84 |
| 4 | Tabela ölçüsü, yüksekliği ve konumunu gönderin; kapsamı belirleyip dönüş yapalım. | 81 |

### 2. aşama grup düzeyi negatifler

Bu gruplarda hizmet yerine ekipman kiralama / imalat arayan aramalar beklenir. Ortak listeye değil, yalnız ilgili gruba sıralı eşleme ile eklenir:

| Grup | Negatif kelimeler |
| --- | --- |
| 2.9 Vinç Statik Analizi | `"kiralama"`, `"kiralık"`, `"operatör"`, `"operatörlü"`, `"satılık"`, `"ikinci el"` |
| 2.10 Monoray / Vinç Yolu | `"satılık"`, `"ikinci el"`, `"imalatı"`, `"montajı"` |
| 2.11 Kaldırma Aparatı | `"satılık"`, `"satış"`, `"sapan"`, `"zincir"`, `"halat"` |
| 2.12 Fuar Standı | `"tasarım"`, `"stand yapımı"`, `"kiralama"`, `"stand firmaları"` |
| 2.13 Sahne / Truss / Tribün | `"kiralama"`, `"kiralık"`, `"satılık"`, `"ses sistemi"` |
| 2.14 Tabela / Pilon | `"tabela yapımı"`, `"tabela modelleri"`, `"tabelacı"`, `"led tabela"` |

Not: "tasarım", "stand yapımı", "tabela yapımı" gibi aramalar stand/tabela firmalarından da gelebilir (bu firmalar statik rapor müşterisidir). Bu negatifler arama terimleri raporunda dönüşüm getiren terimler görülürse kaldırılır.

## 6. Bölge varyantları

Bölge adını içeren başlıklar, mevcut gruplara **ikinci bir duyarlı arama reklamı (RSA)** olarak eklenir. Google'da nihai URL başlık bazında değil reklam bazında seçildiği için bölge başlıkları ana reklama karıştırılmaz: bölge reklamı ya ilgili bölge sayfasına ya da grubun hizmet sayfasına gider (aşağıdaki tablo). Bölge reklamında 15 başlığı tamamlamak için bu 5 bölge başlığına grubun kendi başlıklarından 10 tanesi eklenir; 4 açıklamanın 2'si aşağıdaki bölge açıklamaları, 2'si grubun açıklamalarıdır.

Kampanyanın konumu İstanbul'un tamamı olduğu için bölge başlıkları o bölgede olmayan kullanıcılara da gösterilebilir. Bunu sınırlamak için bölge başlıklarından biri 1. konuma sabitlenmez; bunun yerine gruba aşağıdaki bölge anahtar kelimeleri (sıralı eşleme) eklenir ve bölge reklamının performansı ana reklamla karşılaştırılır. Bir ay sonra bölge reklamı daha düşük tıklama oranı veya dönüşüm getiriyorsa duraklatılır.

### Yönlendirme tablosu

| Bölge | Eklendiği reklam grupları | Bölge reklamının nihai URL'si | Not |
| --- | --- | --- | --- |
| İkitelli OSB / Başakşehir | 2.1 Elektrik Projesi / Rölöve, 2.6 Topraklama Ölçümü, 2.8 İş Hijyeni Ölçümleri | https://www.aymati.com.tr/bolge-ikitelli-osb-basaksehir.html | Bölge sayfası elektrik projesi, topraklama ve iş hijyeni hizmetlerine bağlantı veriyor |
| Hadımköy / Arnavutköy | 2.2 Raf Statik Analizi, 2.3 Platform / Asma Kat Statik Analizi, 2.7 Forklift Periyodik Kontrolü | https://www.aymati.com.tr/bolge-hadimkoy-arnavutkoy.html | Bölge sayfası raf statik, raf kontrolü ve forklift kontrolüne bağlantı veriyor. Platform / asma kat grubu için nihai URL hizmet sayfası (`platform-statik-analizi.html`) kalsın |
| Esenyurt / Beylikdüzü | 2.1 Elektrik Projesi / Rölöve, 2.6 Topraklama Ölçümü | https://www.aymati.com.tr/bolge-esenyurt-beylikduzu.html | Bölge sayfası elektrik projesine bağlantı veriyor. Topraklama grubu için nihai URL hizmet sayfası (`topraklama-olcumu.html`) kalsın |
| Tuzla OSB | 2.5 Patlamadan Korunma Dokümanı, 2.8 İş Hijyeni Ölçümleri | https://www.aymati.com.tr/bolge-tuzla-osb-tuzla.html | Bölge sayfası PKD ve iş hijyeni (VOC) konularını anlatıyor |

Kural: Bölge sayfası grubun hizmetini anlatıyor ve hizmet sayfasına bağlantı veriyorsa bölge sayfası kullanılır; anlatmıyorsa bölge reklamı grubun hizmet sayfasına gider. Bölge sayfalarına giden reklamlarda dönüşüm oranı hizmet sayfasından belirgin biçimde düşükse nihai URL hizmet sayfasına çevrilir.

### İkitelli OSB / Başakşehir

- **Nihai URL:** https://www.aymati.com.tr/bolge-ikitelli-osb-basaksehir.html
- **Gruplar:** 2.1 Elektrik Projesi / Rölöve, 2.6 Topraklama Ölçümü, 2.8 İş Hijyeni Ölçümleri
- **Bölge anahtar kelimeleri (sıralı eşleme, ilgili gruba):** `"ikitelli" elektrik projesi`, `"ikitelli" topraklama ölçümü`, `"başakşehir" elektrik projesi`, `"ikitelli osb" iş hijyeni`

| # | Bölge başlığı | Kr. |
| --- | --- | --- |
| 1 | İkitelli OSB Elektrik Projesi | 29 |
| 2 | İkitelli OSB'de Yerinde Rölöve | 30 |
| 3 | İkitelli Topraklama Ölçümü | 26 |
| 4 | Başakşehir Elektrik Projesi | 27 |
| 5 | İkitelli OSB İş Hijyeni Ölçümü | 30 |

| # | Bölge açıklaması | Kr. |
| --- | --- | --- |
| 1 | İkitelli OSB ve Başakşehir'deki atölye ve fabrikalarda yerinde rölöve ve elektrik projesi. | 90 |
| 2 | İkitelli OSB'de EMO kayıtlı mühendis imzalı topraklama ölçümü ve iş hijyeni ölçümleri. | 86 |

### Hadımköy / Arnavutköy

- **Nihai URL:** https://www.aymati.com.tr/bolge-hadimkoy-arnavutkoy.html
- **Gruplar:** 2.2 Raf Statik Analizi, 2.3 Platform / Asma Kat Statik Analizi, 2.7 Forklift Periyodik Kontrolü
- **Bölge anahtar kelimeleri (sıralı eşleme, ilgili gruba):** `"hadımköy" raf statik`, `"arnavutköy" raf statik`, `"hadımköy" forklift kontrolü`, `"hadımköy" asma kat statik`

| # | Bölge başlığı | Kr. |
| --- | --- | --- |
| 1 | Hadımköy Raf Statik Analizi | 27 |
| 2 | Arnavutköy Raf Statik Analizi | 29 |
| 3 | Hadımköy Forklift Kontrolü | 26 |
| 4 | Hadımköy Depolarına Hizmet | 26 |
| 5 | Hadımköy Asma Kat Statik | 24 |

| # | Bölge açıklaması | Kr. |
| --- | --- | --- |
| 1 | Hadımköy ve Arnavutköy depolarında raf statik analizi; MMO kayıtlı mühendis imzalı. | 83 |
| 2 | Hadımköy'deki depo ve tesislerde forklift periyodik kontrolü ve asma kat statik analizi. | 88 |

### Esenyurt / Beylikdüzü

- **Nihai URL:** https://www.aymati.com.tr/bolge-esenyurt-beylikduzu.html
- **Gruplar:** 2.1 Elektrik Projesi / Rölöve, 2.6 Topraklama Ölçümü
- **Bölge anahtar kelimeleri (sıralı eşleme, ilgili gruba):** `"esenyurt" elektrik projesi`, `"beylikdüzü" elektrik projesi`, `"beylikdüzü osb" topraklama`, `"esenyurt" topraklama ölçümü`

| # | Bölge başlığı | Kr. |
| --- | --- | --- |
| 1 | Esenyurt Elektrik Projesi | 25 |
| 2 | Beylikdüzü Elektrik Projesi | 27 |
| 3 | Beylikdüzü OSB'ye Hizmet | 24 |
| 4 | Esenyurt Topraklama Ölçümü | 26 |
| 5 | Beylikdüzü Topraklama Ölçümü | 28 |

| # | Bölge açıklaması | Kr. |
| --- | --- | --- |
| 1 | Esenyurt ve Beylikdüzü'ndeki fabrika ve depolarda yerinde rölöve ile elektrik projesi. | 86 |
| 2 | Beylikdüzü OSB ve Esenyurt'ta topraklama ölçümü; EMO kayıtlı mühendis imzalı rapor. | 83 |

### Tuzla OSB

- **Nihai URL:** https://www.aymati.com.tr/bolge-tuzla-osb-tuzla.html
- **Gruplar:** 2.5 Patlamadan Korunma Dokümanı, 2.8 İş Hijyeni Ölçümleri
- **Bölge anahtar kelimeleri (sıralı eşleme, ilgili gruba):** `"tuzla" patlamadan korunma dokümanı`, `"tuzla" iş hijyeni ölçümü`, `"tuzla osb" pkd`, `"tuzla" voc ölçümü`

| # | Bölge başlığı | Kr. |
| --- | --- | --- |
| 1 | Tuzla OSB Patlamadan Korunma | 28 |
| 2 | Tuzla'da PKD Hazırlanır | 23 |
| 3 | Tuzla OSB İş Hijyeni Ölçümü | 27 |
| 4 | Tuzla Kimya Tesislerine PKD | 27 |
| 5 | Tuzla'da VOC ve Gaz Ölçümü | 26 |

| # | Bölge açıklaması | Kr. |
| --- | --- | --- |
| 1 | Tuzla OSB'deki kimya, boya ve solvent tesisleri için patlamadan korunma dokümanı. | 81 |
| 2 | Tuzla'daki tesislerde kişisel ve ortam VOC, toz ve gürültü ölçümleri yerinde yapılır. | 85 |

## Reklam metni kuralları (kontrol listesi)

- Fiyat, "en ucuz", "garanti", "%100", süre vaadi gibi doğrulanamayan iddia yok.
- Rakip marka adı yok.
- Telefon numarası reklam metnine yazılmadı (Google politikası); numara çağrı öğesinde.
- "EMO / MMO kayıtlı mühendis imzalı" ve "yerinde rölöve / yerinde ölçüm" ifadeleri yalnız sitede bu iddiayı taşıyan hizmetlerde kullanıldı.
- Görünür metinde yıl yok.
