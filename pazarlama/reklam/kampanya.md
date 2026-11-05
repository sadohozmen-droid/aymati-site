# Google Ads Kampanya Yapısı — Aymati Proje

Bu dosya reklam uzmanı ajanı tarafından her ay güncellenir. Ajanın hesaba erişimi yoktur; aşağıdaki yapı Google Ads Editor'e veya Google Ads arayüzüne elle girilmek üzere hazırlanmıştır. Bu dosya `site/` dışında olduğu için yayına girmez.

Toplu yükleme dosyaları:

- `pazarlama/reklam/ads-editor-2026-11.csv`: anahtar kelimeler ve negatifler (Campaign, Ad group, Keyword, Match type)
- `pazarlama/reklam/ads-editor-reklamlar-2026-11.csv`: duyarlı arama reklamları (Campaign, Ad group, Headline 1–15, Description 1–4, Final URL, Path 1, Path 2)

## Bu ay değişenler (Kasım 2026, revizyon — 5 Kasım)

Site sahibinin talebi: *"Google reklamlarını planla; özellikle statik analiz, PKD ve projeler."* Yapı bu önceliğe göre baştan kuruldu. Bu revizyon, PR #15 ile aynı gün eklenen "2. aşama statik grupları" (eski bölüm 5) ve "bölge varyantları" (eski bölüm 6) bölümlerinin yerine geçer ve içeriklerini kapsar. 2. aşama grupları artık Statik Analiz kampanyasında; "dönüşüm ölçümü kurulmadan açılmaz" şartı tüm kampanyalar için bölüm 1'de geçerli.

- **Tek kampanya yerine 4 kampanya**, her birinin ayrı bütçesi var: **Statik Analiz** (%40), **Projelendirme** (%30), **PKD** (%20) öncelikli; **Muayene ve İş Hijyeni** (%10) ikincil. Gerekçe bölüm 2'de.
- **Statik Analiz kampanyası, 10 reklam grubu:** genel "statik analiz raporu / statik hesap" aramaları için `statik-analiz.html`, ayrıca raf, platform/asma kat, iskele, fuar standı, vinç, kaldırma aparatı, monoray/vinç yolu, sahne/truss/tribün ve tabela/pilon. Fuar standı ile vinç / kaldırma aparatı site sahibinin isteğiyle ayrı gruplar. Düşük hacimli gruplar **birleştirilmedi**. Her grup kendi sayfasına gidiyor; birleştirmek, aramayı başka bir hizmeti anlatan sayfaya göndermek anlamına gelirdi ve reklam alaka düzeyini düşürürdü. Tam ve sıralı eşlemede hacmi düşük bir grup bütçe harcamaz, yalnızca gösterim almaz. Bu nedenle ayrı tutmanın bir maliyeti yok. 4 hafta sonunda hiç gösterim almayan grup duraklatılır (bölüm 10).
- **PKD kampanyası, 3 reklam grubu:** PKD Genel, ATEX / Tehlikeli Bölge Sınıflandırması, Toz Patlaması ve Sektörel PKD. Sitede ATEX veya toz patlaması için ayrı sayfa olmadığından üçü de `patlamadan-korunma-dokumani.html` sayfasına gider; gruplar yalnızca reklam metnini aramaya yaklaştırmak için ayrıldı. PKD metinlerinde mühendis odası iddiası yoktur.
- **Projelendirme kampanyası, 9 reklam grubu:** elektrik projesi / rölöve, "periyodik kontrolde elektrik projesi eksik" niyeti (aynı sayfa, ayrı metin), pano tek hat şeması, yangın algılama, yıldırımdan korunma / paratoner, **Faraday kafesi hesaplama**, sulu söndürme / sprinkler, acil durum tahliye planı, havalandırma.
- **Faraday kafesi:** Hesaplama aracı (PR #6) bu revizyon hazırlanırken main'e girdi. "Faraday kafesi hesabı / hesaplama / maliyeti" aramaları `faraday-kafesi-hesaplama.html` sayfasına, "faraday kafesi projesi" aramaları ise yıldırımdan korunma proje sayfasına gider. Araç sayfası dolar bazında ön bütçe gösteriyor, ancak reklam metninde tutar ya da para birimi yok.
- **Muayene ve İş Hijyeni (ikincil):** Topraklama, Forklift ve İş Hijyeni grupları korundu. Doğrulanamayan iki başlık düzeltildi: Topraklama'daki "EMO Kayıtlı Mühendis Raporu" yerine "Mühendis Tarafından Ölçüm", Forklift'teki "Makina Mühendisi Kontrolü" yerine "Mühendis Tarafından Kontrol" yazıldı. İki sayfada da bu imza bilgisi yazmıyor. PR #15 bu başlığı, site sahibinin teyidine dayanarak geri almıştı; ancak teyit yazılı olarak depoda yok ve `topraklama-olcumu.html` sayfasında EMO ifadesi hâlâ geçmiyor. Teyit doğruysa önce `topraklama-olcumu.html` sayfasına eklenmeli; ardından başlık geri alınabilir, çünkü reklamdaki iddia açılış sayfasında da görünmeli.
- **PR #15'ten alınanlar:** Vinç, monoray, kaldırma aparatı, fuar, sahne ve tabela gruplarındaki ek anahtar kelimeler (ör. `[vinç ayak yükü hesabı]`, `"caraskal rayı hesabı"`, `[çift katlı fuar standı statik]`, `[konser sahnesi statik]`, `"belediye tabela statik rapor"`) ve grup negatifleri (`"operatörlü"`, `"ikinci el"`, `"montajı"`, `"zincir"`, `"halat"`, `"stand yapımı"`, `"ses sistemi"`, `"tabela modelleri"`). Bölge anahtar kelimeleri de ilgili gruplara sıralı eşlemeyle eklendi: İkitelli, Başakşehir, Esenyurt, Beylikdüzü, Hadımköy, Arnavutköy, Tuzla.
- **PR #15'ten alınmayanlar:** Bölge sayfalarına giden ikinci RSA'lar. Her reklam grubunun tek bir hizmet sayfasına gitmesi kuralına aykırılar. Ayrıca konum hedefi tüm İstanbul olduğundan bölge adlı başlıklar o bölgede olmayan kullanıcılara da gösterilir. Bölge anahtar kelimeleri dönüşüm getirirse bölge reklamları sonraki ay ayrı bir kampanya olarak değerlendirilecek. PR #15'teki "Bu kelimeler `stand firmaları` / `tabelacı` negatifleri müşteriyi keser" uyarısına uyuldu; bu ikisi negatif yapılmadı.
- **Negatifler yeniden düzenlendi:** ortak liste, kampanya listeleri ve grup listeleri ayrıldı. "Nedir" kararı kampanya bazında verildi: Statik, Proje ve Muayene'de negatif; PKD'de ilk 4 hafta açık (bölüm 8.2). Statik kampanyasına yazılım (SAP2000, ANSYS, SolidWorks vb.), ders ve bina/betonarme statiği negatifleri, PKD kampanyasına "PKD = polikistik böbrek hastalığı" ve ATEX ürün negatifleri eklendi.
- **Yeni bölümler:** yayına almadan önce yapılacaklar (bölüm 1), teklif formunun WhatsApp'a göre güncellenmiş dönüşüm tanımları (bölüm 3.2), teklif stratejisi (bölüm 3.3), ilk 4 hafta için haftalık kontrol listesi (bölüm 10), Ads Editor CSV dosyaları.
- Tüm başlık, açıklama, görünen yol, site bağlantısı ve snippet karakter sayıları Python `len()` ile sayıldı (Türkçe harfler tek karakter). Betik ayrıca yasaklı ifadeleri (fiyat, garanti, %100, en ucuz, hemen, aynı gün, yıl), imza kuralını (EMO yalnızca elektrik projelerinde, MMO yalnızca statik ve mekanik projelerde, PKD'de hiçbiri), tekrarlı anahtar kelimeleri, negatiflerin anahtar kelimeleri engelleyip engellemediğini ve her nihai URL'nin `site/` içinde var olduğunu denetledi.
- Arama terimleri raporu (`sonuclar-2026-11.csv`) henüz yok; negatif ve yeni anahtar kelime analizi yapılmadı. Bütçe rakamı yok.

### Önceki değişiklikler

- **Kasım 2026, 2. güncelleme (PR #15):** Topraklama EMO başlığı geri alındı; 2. aşama statik grupları (vinç, monoray, kaldırma aparatı, fuar, sahne, tabela) ve bölge varyantları eklendi. Bu revizyonda yukarıdaki gibi kapsandı.
- **Kasım 2026, ilk sürüm:** Tek kampanya, 8 reklam grubu (Elektrik Projesi, Raf, Platform, İskele, PKD, Topraklama, Forklift, İş Hijyeni). Bu grupların metinleri yeni yapıda ilgili kampanyalara taşındı.

## 1. Yayına almadan önce yapılması gerekenler (site sahibi)

Hesap açma, ödeme bilgisi girme ve harcamayı başlatma site sahibine aittir.

1. **Google Ads hesabı:** ads.google.com adresinde şirketin Google hesabıyla (ör. info@aymati.com.tr) hesap açın. Kurulum sihirbazı "Akıllı kampanya" önerirse **"Uzman moduna geç"** seçeneğiyle kampanya oluşturmadan hesabı tamamlayın. Ülke: Türkiye, saat dilimi: (GMT+03:00) İstanbul, para birimi: TRY. **Saat dilimi ve para birimi sonradan değiştirilemez.**
2. **Faturalama:** Ödeme profili türü "Kuruluş". Ticari ünvanı, adresi, vergi dairesini ve vergi numarasını girin; ödeme yöntemini (kart) ekleyin. Faturalar ve belgeler Faturalama > Belgeler bölümünden indirilir. Google reklamveren doğrulaması (kimlik / kuruluş bilgisi) isteyebilir; vergi levhası ve ticaret sicil bilgisini hazır tutun.
3. **Dönüşüm işlemlerini oluşturun** (Hedefler > Dönüşümler > Yeni dönüşüm işlemi > Web sitesi > manuel kurulum). Bölüm 3.2'deki üç dönüşümü oluşturun; Google'ın vereceği **dönüşüm kimliği (AW-…) ve üç dönüşüm etiketini** bu depoya not olarak iletin.
4. **Sitede Google etiketi yok.** Dönüşüm kimliği gelince ayrı bir PR'da tüm sayfalara Google etiketi (gtag.js) ve bölüm 3.2'deki olaylar eklenecek. **Bu yapılmadan reklam açılmamalı**, çünkü yalnızca tıklama ölçülür ve teklif stratejisi öğrenemez.
5. **Çerez / KVKK:** Google etiketi çerez kullanır. `kvkk.html` ve aydınlatma metnine reklam ölçüm çerezleri eklenmeli; açık rıza (çerez onay bandı) gerekip gerekmediğini hukuk danışmanınızla netleştirin. Etiket PR'ı bu karara göre hazırlanacak.
6. **Test:** Etiket PR'ı yayına girdikten sonra Google Etiket Asistanı (tagassistant.google.com) ile teklif formunu (WhatsApp'a aktarım), bir telefon bağlantısını ve bir WhatsApp bağlantısını deneyin. Dönüşümler Google Ads'te 24 saat içinde "Kayıt yapılıyor" durumuna geçmeli.
7. **Google Ads Editor** programını kurun, hesabı indirin ve bölüm 9'daki gibi iki CSV dosyasını içe aktarın. Kampanyaları **duraklatılmış** olarak yükleyin, ayarları (bölüm 3) kontrol edip yayınlayın.
8. Kampanya bütçelerini bölüm 2'deki yüzdelere göre girin ve kampanyaları etkinleştirin.

## 2. Kampanya yapısı ve bütçe dağılımı

Dört ayrı kampanya; her birinin **ayrı günlük bütçesi** olur (paylaşılan bütçe kullanmayın). Tutarları site sahibi belirler; aşağıdaki yüzdeler toplam reklam bütçesinin kampanyalara bölünmesi içindir.

| Kampanya | Öncelik | Bütçe payı | Reklam grubu | Anahtar kelime |
| --- | --- | --- | --- | --- |
| Statik Analiz | Öncelikli | %40 | 10 | 162 |
| PKD | Öncelikli | %20 | 3 | 48 |
| Projelendirme | Öncelikli | %30 | 9 | 135 |
| Muayene ve İş Hijyeni | İkincil | %10 | 3 | 51 |
| **Toplam** | | **%100** | **25** | **396** |

**Gerekçe:**

- **Statik Analiz (%40):** Site sahibinin ilk önceliği. En fazla grup (10) ve en geniş arama yelpazesi bu kampanyada. "Raporu fuar merkezi, belediye veya periyodik kontrol kuruluşu istedi" niyeti güçlü ve teslim tarihli; arama yapan kişi doğrudan hizmet arıyor. "MMO kayıtlı makina mühendisi imzalı" ifadesi gerçek bir farklılık.
- **Projelendirme (%30):** 9 grup. Periyodik kontrolde "proje eksik" uygunsuzluğu düzenli talep yaratıyor. Elektrik projesi aramaları hacimli ama öğrenci ve konut karışık; negatiflerle daraltıldı. Statikten düşük tutulmasının nedeni, aramaların daha rekabetçi ve bilgi amaçlı olması.
- **PKD (%20):** Tek hizmet, yüksek değerli iş, ama arama hacmi sınırlı. Daha yüksek pay büyük olasılıkla harcanamaz. PKD kampanyası 2 hafta üst üste günlük bütçesinin belirgin altında harcıyorsa artan pay Statik'e aktarılır.
- **Muayene ve İş Hijyeni (%10, ikincil):** Periyodik muayene pazarında çok sayıda firma var, teklifler yüksek ve iş başına değer projelere göre düşük. Kampanya açık kalır ama bütçe sınırlı. İlk ay dönüşüm maliyeti öncelikli kampanyalardan iyiyse pay artırılabilir.
- Kampanyalardan biri "bütçe nedeniyle sınırlı" uyarısı alıp dönüşüm getiriyorsa, payı en düşük dönüşüm getiren kampanyadan alınarak artırılır. Toplam bütçe değişmez.

### Reklam grubu → açılış sayfası

| Kampanya | # | Reklam grubu | Nihai URL | Görünen yol | Anahtar kelime |
| --- | --- | --- | --- | --- | --- |
| Statik Analiz | 4.1 | Statik Analiz Raporu (genel) | `statik-analiz.html` | /Statik-Analiz/Rapor | 15 |
| Statik Analiz | 4.2 | Raf Statik Analizi | `raf-statik-analizi.html` | /Raf-Statik/Analiz | 18 |
| Statik Analiz | 4.3 | Platform / Asma Kat Statik Analizi | `platform-statik-analizi.html` | /Platform-Statik/Asma-Kat | 14 |
| Statik Analiz | 4.4 | İskele Statik Analizi | `iskele-statik-analizi.html` | /Iskele-Statik/Rapor | 11 |
| Statik Analiz | 4.5 | Fuar Standı Statik Analizi | `fuar-standi-statik-analizi.html` | /Fuar-Standi/Statik | 17 |
| Statik Analiz | 4.6 | Vinç Statik Analizi | `vinc-statik-analizi.html` | /Vinc-Statik/Temel | 17 |
| Statik Analiz | 4.7 | Kaldırma Aparatı Statik Hesabı | `kaldirma-aparati-statik-hesabi.html` | /Kaldirma-Aparat/WLL | 16 |
| Statik Analiz | 4.8 | Monoray / Vinç Yolu Statik Analizi | `monoray-vinc-yolu-statik-analizi.html` | /Monoray/Vinc-Yolu | 18 |
| Statik Analiz | 4.9 | Sahne / Truss / Tribün Statik Analizi | `sahne-truss-tribun-statik-analizi.html` | /Sahne-Truss/Statik | 19 |
| Statik Analiz | 4.10 | Tabela / Pilon Statik Hesabı | `tabela-pilon-statik-hesabi.html` | /Tabela-Pilon/Statik | 17 |
| PKD | 5.1 | PKD Genel | `patlamadan-korunma-dokumani.html` | /PKD/Hazirlama | 17 |
| PKD | 5.2 | ATEX / Tehlikeli Bölge Sınıflandırması | `patlamadan-korunma-dokumani.html` | /ATEX/Zone | 15 |
| PKD | 5.3 | Toz Patlaması ve Sektörel PKD | `patlamadan-korunma-dokumani.html` | /PKD/Toz-Patlamasi | 16 |
| Projelendirme | 6.1 | Elektrik Projesi / Rölöve | `elektrik-ic-tesisat-projesi.html` | /Elektrik-Proje/Rolove | 20 |
| Projelendirme | 6.2 | Elektrik Projesi Eksik (Periyodik Kontrol) | `elektrik-ic-tesisat-projesi.html` | /Elektrik-Proje/Eksik | 15 |
| Projelendirme | 6.3 | Pano Tek Hat Şeması | `pano-tek-hat-semasi-projesi.html` | /Tek-Hat/Pano | 14 |
| Projelendirme | 6.4 | Yangın Algılama ve İhbar Projesi | `yangin-algilama-ve-ihbar-sistemleri-projesi.html` | /Yangin-Algilama/Proje | 14 |
| Projelendirme | 6.5 | Yıldırımdan Korunma / Paratoner / Faraday | `yildirimdan-korunma-tesisati-projesi.html` | /Paratoner/Proje | 14 |
| Projelendirme | 6.6 | Faraday Kafesi Hesaplama | `faraday-kafesi-hesaplama.html` | /Faraday-Kafesi/Hesaplama | 12 |
| Projelendirme | 6.7 | Sulu Söndürme / Sprinkler Projesi | `sulu-sondurme-yangin-tesisat-projesi.html` | /Sprinkler/Proje | 16 |
| Projelendirme | 6.8 | Acil Durum Tahliye Planı | `acil-durum-tahliye-plani-projesi.html` | /Tahliye-Plani/Cizim | 15 |
| Projelendirme | 6.9 | Havalandırma Tesisat Projesi | `havalandirma-tesisat-projesi.html` | /Havalandirma/Proje | 15 |
| Muayene ve İş Hijyeni | 7.1 | Topraklama Ölçümü | `topraklama-olcumu.html` | /Topraklama/Olcum | 17 |
| Muayene ve İş Hijyeni | 7.2 | Forklift Periyodik Kontrolü | `forklift-periyodik-kontrolu.html` | /Forklift/Periyodik | 15 |
| Muayene ve İş Hijyeni | 7.3 | İş Hijyeni Ölçümleri | `is-hijyeni-olcumleri.html` | /Is-Hijyeni/Olcum | 19 |

## 3. Kampanya ayarları (dört kampanyada aynı)

### 3.1 Genel ayarlar

| Ayar | Öneri |
| --- | --- |
| Kampanya türü | Arama (Search). Hedef: Potansiyel müşteriler |
| Ağlar | **Yalnız Google Arama Ağı.** "Arama ağı iş ortakları" ve "Görüntülü Reklam Ağı" kutuları **kapalı** |
| Konum | İstanbul (il). İsteğe bağlı: Kocaeli, Tekirdağ (ayrı kampanya açmadan aynı kampanyaya eklenip konum raporundan izlenebilir) |
| Konum seçenekleri | **"Varlık: Hedeflenen konumlarınızda bulunan veya buraları düzenli olarak ziyaret eden kişiler"** ("ilgilenen kişiler" seçeneği kapalı) |
| Dil | Türkçe |
| Reklam planlaması | Pazartesi–Cuma 08:00–18:30. Cumartesi-Pazar reklam yok |
| Bütçe | Site sahibi belirleyecek; dağılım bölüm 2'de |
| Teklif stratejisi | Bölüm 3.3 |
| Geniş eşleme | Kampanya düzeyinde **kapalı** (yalnız tam ve sıralı eşleme) |
| Otomatik oluşturulan öğeler | İlk ay **kapalı** (fiyat veya doğrulanamayan iddia üretmesine karşı) |
| Otomatik etiketleme | Açık (gclid) |
| Reklam rotasyonu | Optimize et (varsayılan) |
| Alan adı | https://www.aymati.com.tr |

Not: Fuar standı ve sahne/truss aramaları İstanbul dışındaki stand ve organizasyon firmalarından da gelebilir. Konum hedefi değiştirilmedi; konum raporuna göre sonraki ay değerlendirilecek.

### 3.2 Dönüşümler

`site/teklif.html` incelendi (PR #12 sonrası): Formda `FORM_ENDPOINT` boş. Doğrulamadan geçen talep, ziyaretçinin WhatsApp'ında hazır mesaj olarak açılıyor (`sendFallback` → `https://wa.me/905551428474?text=...`). Ayrı bir teşekkür sayfası yok, bu yüzden URL tabanlı dönüşüm kullanılamaz; dönüşümler kod içinden olay olarak gönderilmeli.

| Dönüşüm adı | Tetikleyici (etiket PR'ında uygulanacak) | Kategori | Sayım | Tür |
| --- | --- | --- | --- | --- |
| Teklif formu (WhatsApp'a aktarıldı) | `teklif.html` formunda tüm alanlar ve KVKK onayı doğrulandıktan sonra, `sendFallback(body)` çağrılmadan **hemen önce**. Sayfa WhatsApp'a yönlendiği için olay `transport_type: 'beacon'` ile gönderilmeli. Teklif türü (`proje` / `muayene`) parametre olarak eklenir. İleride `FORM_ENDPOINT` doldurulursa aynı olay, "Talebiniz bize ulaştı" başarı anında da gönderilir | Potansiyel müşteri formu gönderme | Bir | **Birincil** |
| WhatsApp tıklaması | Sitedeki `https://wa.me/` ile başlayan bağlantılara tıklama | İletişim | Bir | **Birincil** |
| Telefon tıklaması | `tel:+905551428474` bağlantılarına tıklama | Telefon görüşmesi | Bir | **Birincil** |
| (İsteğe bağlı) Reklamdan arama | Çağrı öğesindeki numaraya reklamdan arama, 30 sn+ | Telefon görüşmesi | Bir | İkincil |

Dikkat edilecekler:

- Form dönüşümü WhatsApp'ın **açıldığı** anı ölçer. Ziyaretçinin mesajı gerçekten gönderip göndermediği ölçülemez, bu yüzden sayı gerçek talepten fazla görünebilir. Site sahibi ilk 4 hafta, gelen WhatsApp teklif mesajlarının sayısını Google Ads'teki form dönüşümüyle haftalık karşılaştırmalı (bölüm 10).
- Form, WhatsApp'a `location.href` ile yönlendirdiğinden "WhatsApp tıklaması" olayı ayrıca tetiklenmez; çift sayım olmaz.
- Google yönlendirme numarası Türkiye'de kullanılamıyorsa "Reklamdan arama" dönüşümü kurulamaz; o durumda yalnızca sitedeki telefon tıklaması sayılır.

### 3.3 Teklif stratejisi

| Dönem | Strateji | Not |
| --- | --- | --- |
| Hafta 1–4 (dönüşüm verisi yok) | **"Tıklamaları en üst düzeye çıkar" + maksimum TBM teklif sınırı** | Sınırı, her kampanya için Anahtar Kelime Planlayıcı'daki "sayfanın üstü teklifi (yüksek aralık)" değerlerine göre site sahibi belirler. Az grubun çok harcaması engellenir. Bu dosyada tutar yok |
| Bir kampanya son 30 günde yaklaşık 15+ dönüşüme ulaşınca | **"Dönüşümleri en üst düzeye çıkar"** (önce hedef EBM'siz) | Geçiş kampanya bazında yapılır. Geçişten sonraki 2 hafta ayar değiştirilmez (öğrenme dönemi) |
| Yeterli dönüşüm biriktiğinde (aylar içinde) | Hedef EBM'li "Dönüşümleri en üst düzeye çıkar" | Hedef, gerçekleşen ortalama EBM'ye göre belirlenir |

PKD ve Muayene kampanyaları dönüşüm eşiğine geç ulaşabilir; bu kampanyalarda manuel TBM sınırlı strateji daha uzun süre kalabilir.

### 3.4 Öğeler (uzantılar)

- **Çağrı öğesi** (hesap düzeyi): 0555 142 84 74, yalnız reklam planlaması saatlerinde.
- **Açıklama metni öğeleri** (hesap düzeyi, ≤25 karakter):

| Metin | Kr. |
| --- | --- |
| EMO/MMO Kayıtlı Mühendis | 24 |
| Yerinde Rölöve ve Ölçüm | 23 |
| Fabrika, Depo ve Atölye | 23 |
| İstanbul Batı Yakası OSB | 24 |
| Teklif Formu ve WhatsApp | 24 |
| E-İmzalı PDF Rapor | 18 |

- **Site bağlantıları** (kampanya düzeyi; başlık ≤25, açıklama satırı ≤35):

**Statik Analiz**

| Başlık | Kr. | URL | Açıklama 1 | Kr. | Açıklama 2 | Kr. |
| --- | --- | --- | --- | --- | --- | --- |
| Fuar Standı Statik | 18 | `fuar-standi-statik-analizi.html` | Çift katlı stand statik raporu | 30 | Teknik ofis formatına uygun | 27 |
| Vinç Statik Analizi | 19 | `vinc-statik-analizi.html` | Kule vinç temeli, ayak yükü | 27 | Zemin basıncı ve altlık | 23 |
| Raf Statik Örnek Rapor | 22 | `raf-statik-analizi.html` | Örnek rapor sayfalarını görün | 29 | Raporda neler var inceleyin | 27 |
| Tüm Statik Hizmetler | 20 | `statik-analiz.html` | Raf, platform, iskele, tabela | 29 | MMO kayıtlı mühendis imzalı | 27 |
| Teklif Alın | 11 | `teklif.html` | Formu doldurun, dönüş yapalım | 29 | WhatsApp ile iletilir | 21 |

**PKD**

| Başlık | Kr. | URL | Açıklama 1 | Kr. | Açıklama 2 | Kr. |
| --- | --- | --- | --- | --- | --- | --- |
| Teklif Alın | 11 | `teklif.html` | Formu doldurun, dönüş yapalım | 29 | WhatsApp ile iletilir | 21 |
| Paratoner Projesi | 17 | `yildirimdan-korunma-tesisati-projesi.html` | Yıldırım risk analizi | 21 | Koruma alanı hesabı | 19 |
| Topraklama Ölçümü | 17 | `topraklama-olcumu.html` | Topraklama ölçüm raporu | 23 | Yerinde ölçüm ve test | 21 |
| Sık Sorulanlar | 14 | `sss.html` | Hizmetlerle ilgili sorular | 26 | Kapsam ve teslim bilgisi | 24 |

**Projelendirme**

| Başlık | Kr. | URL | Açıklama 1 | Kr. | Açıklama 2 | Kr. |
| --- | --- | --- | --- | --- | --- | --- |
| Elektrik İç Tesisat | 19 | `elektrik-ic-tesisat-projesi.html` | Yerinde rölöve ile proje | 24 | EMO kayıtlı S.M.M. imzalı | 25 |
| Tek Hat Şeması | 14 | `pano-tek-hat-semasi-projesi.html` | Panolar yerinde incelenir | 25 | Her pano için ayrı pafta | 24 |
| Tahliye Planı | 13 | `acil-durum-tahliye-plani-projesi.html` | ISO 23601 kaçış planı | 21 | A3 laminasyonlu baskı | 21 |
| Tüm Projeler | 12 | `projelendirme.html` | Elektrik ve mekanik projeler | 28 | EMO / MMO kayıtlı mühendis | 26 |
| Teklif Alın | 11 | `teklif.html` | Formu doldurun, dönüş yapalım | 29 | WhatsApp ile iletilir | 21 |

**Muayene ve İş Hijyeni**

| Başlık | Kr. | URL | Açıklama 1 | Kr. | Açıklama 2 | Kr. |
| --- | --- | --- | --- | --- | --- | --- |
| Periyodik Muayene | 17 | `periyodik-muayene.html` | Forklift, vinç, kazan, tesisat | 30 | Yerinde kontrol ve rapor | 24 |
| İş Hijyeni | 10 | `is-hijyeni-olcumleri.html` | Gürültü, toz, VOC ölçümleri | 27 | Kişisel ve ortam ölçümleri | 26 |
| Hizmet Bölgeleri | 16 | `hizmet-bolgeleri.html` | İkitelli, Hadımköy, Esenyurt | 28 | İstanbul batı yakası OSB'ler | 28 |
| Teklif Alın | 11 | `teklif.html` | Formu doldurun, dönüş yapalım | 29 | WhatsApp ile iletilir | 21 |

- **Yapılandırılmış snippet** (kampanya düzeyi, her değer ≤25):

| Kampanya | Başlık | Değerler |
| --- | --- | --- |
| Statik Analiz | Türler | Raf (3), Platform / Asma Kat (19), İskele (6), Fuar Standı (11), Kule Vinç Temeli (16), Kaldırma Aparatı (16), Monoray / Vinç Yolu (19), Tabela ve Pilon (15) |
| PKD | Hizmetler | Bölge Sınıflandırması (21), Patlama Riski Analizi (21), Bölge Haritaları (16), Ex Ekipman Kontrolü (19), Eylem Planı (11) |
| Projelendirme | Hizmetler | Elektrik İç Tesisat (19), Tek Hat Şeması (14), Yangın Algılama (15), Paratoner (9), Sprinkler (9), Tahliye Planı (13), Havalandırma (12) |
| Muayene ve İş Hijyeni | Hizmetler | Topraklama Ölçümü (17), Forklift Kontrolü (17), Gürültü Ölçümü (14), Toz Ölçümü (10), VOC Ölçümü (10) |

## 4. Kampanya: Statik Analiz

Bütçe payı **%40**. Tüm metinlerde imza ifadesi "MMO kayıtlı makina mühendisi". Kampanya negatifleri bina/betonarme statiğini (inşaat mühendisliği işi), yazılımları ve ders/öğrenci aramalarını dışarıda bırakır. Başlık sabitleme (pin) önerisi: 1. konuma grubun hizmet adı (1. başlık) sabitlenebilir; diğerleri serbest.

### 4.1 Statik Analiz Raporu (genel)

- **Nihai URL:** https://www.aymati.com.tr/statik-analiz.html
- **Görünen yol:** www.aymati.com.tr/Statik-Analiz/Rapor (13 / 5 karakter, sınır 15)
- **Not:** Genel aramalar. Yapı türü belli olan aramalar alt gruplara gitsin diye bu gruptaki sıralı anahtar kelimeler alt grupların terimlerini içermez.

**Anahtar kelimeler (15)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[statik analiz raporu]` | Tam |
| `[statik hesap raporu]` | Tam |
| `[statik analiz hizmeti]` | Tam |
| `[statik hesap hizmeti]` | Tam |
| `[statik hesap raporu hazırlama]` | Tam |
| `[statik analiz yaptırma]` | Tam |
| `[statik hesap yaptırmak]` | Tam |
| `[statik analiz firması]` | Tam |
| `[mmo statik rapor]` | Tam |
| `"statik analiz raporu"` | Sıralı |
| `"statik hesap raporu"` | Sıralı |
| `"imzalı statik rapor"` | Sıralı |
| `"statik hesap istanbul"` | Sıralı |
| `"makina mühendisi statik hesap"` | Sıralı |
| `"statik rapor hazırlayan"` | Sıralı |

**Grup negatifleri (sıralı):** `"bina statik"` (Bina/betonarme statik projesi verilmiyor (inşaat mühendisliği))

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Statik Analiz Raporu | 20 |
| 2 | Statik Hesap Raporu | 19 |
| 3 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 4 | Makina Mühendisi İmzalı Rapor | 29 |
| 5 | Raf, Platform, İskele, Vinç | 27 |
| 6 | Fuar Standı ve Tabela Hesabı | 28 |
| 7 | Kaldırma Aparatı ve Monoray | 27 |
| 8 | Yük, Rüzgâr ve Deprem Etkisi | 28 |
| 9 | Eleman ve Bağlantı Kontrolü | 27 |
| 10 | E-İmzalı PDF Rapor | 18 |
| 11 | Gerekirse Güçlendirme Önerisi | 29 |
| 12 | Statik Rapor Teklifi Alın | 25 |
| 13 | İstanbul İşletmelerine Hizmet | 29 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Raf, platform, iskele, vinç, fuar standı ve tabela için imzalı statik hesap raporu. | 83 |
| 2 | Statik analizlerimizi MMO kayıtlı makina mühendislerimiz hazırlar ve imzalar. | 77 |
| 3 | Rapor; yükleri, hesap modelini, eleman ve bağlantı kontrollerini ve sonucu içerir. | 82 |
| 4 | Yapının türünü, ölçülerini ve raporu isteyen kurumu yazın, kapsamı birlikte belirleyelim. | 89 |

### 4.2 Raf Statik Analizi

- **Nihai URL:** https://www.aymati.com.tr/raf-statik-analizi.html
- **Görünen yol:** www.aymati.com.tr/Raf-Statik/Analiz (10 / 6 karakter, sınır 15)

**Anahtar kelimeler (18)**

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
| `"hadımköy raf statik"` | Sıralı |
| `"arnavutköy raf statik"` | Sıralı |

**Grup negatifleri (sıralı):** `"ikea"` (Ev mobilyası), `"kitaplık"` (Ev mobilyası), `"duvar rafı"` (Ev mobilyası), `"market rafı"` (Raf satın alma), `"satılık"` (Raf satın alma), `"sahibinden"` (Raf satın alma)

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
| 3 | TS EN 15512, TS EN 15635 ve deprem yönetmeliğine göre hesap; yük kapasite etiketi bilgisi. | 90 |
| 4 | Sitemizdeki örnek raporu inceleyin, raf bilgilerinizi gönderin, size dönüş yapalım. | 83 |

### 4.3 Platform / Asma Kat Statik Analizi

- **Nihai URL:** https://www.aymati.com.tr/platform-statik-analizi.html
- **Görünen yol:** www.aymati.com.tr/Platform-Statik/Asma-Kat (15 / 8 karakter, sınır 15)

**Anahtar kelimeler (14)**

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
| `"hadımköy asma kat statik"` | Sıralı |

**Grup negatifleri (sıralı):** `"web"` (Yazılım platformu), `"yazılım"` (Yazılım platformu), `"oyun"` (Alakasız)

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

### 4.4 İskele Statik Analizi

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

**Grup negatifleri (sıralı):** `"kiralama"` (İskele kiralama), `"kiralık"` (İskele kiralama), `"satılık"` (İskele satın alma), `"tekne"` (Deniz iskelesi), `"liman"` (Deniz iskelesi)

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

### 4.5 Fuar Standı Statik Analizi

- **Nihai URL:** https://www.aymati.com.tr/fuar-standi-statik-analizi.html
- **Görünen yol:** www.aymati.com.tr/Fuar-Standi/Statik (11 / 6 karakter, sınır 15)
- **Not:** Site sahibinin isteğiyle ayrı grup. Bazı fuar şartnameleri çift katlı stand için inşaat mühendisi (SİM) onayı ister; reklamda "fuar onayı", "onaylı rapor" gibi ifade yoktur. 3. açıklama bu konuyu teklif aşamasına bırakır (sayfadaki SSS ile aynı).

**Anahtar kelimeler (17)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[fuar standı statik analizi]` | Tam |
| `[fuar standı statik hesabı]` | Tam |
| `[fuar standı statik raporu]` | Tam |
| `[fuar standı statik proje]` | Tam |
| `[çift katlı stand statik]` | Tam |
| `[çift katlı stand statik hesabı]` | Tam |
| `[çift katlı stand statik raporu]` | Tam |
| `[stand statik raporu]` | Tam |
| `[stand statik hesabı]` | Tam |
| `"fuar standı statik"` | Sıralı |
| `"çift katlı stand statik"` | Sıralı |
| `"stand statik rapor"` | Sıralı |
| `[çift katlı fuar standı statik]` | Tam |
| `"fuar statik rapor"` | Sıralı |
| `"stand statik hesap"` | Sıralı |
| `"iki katlı stand statik"` | Sıralı |
| `"fuar standı statik proje"` | Sıralı |

**Grup negatifleri (sıralı):** `"tasarım"` (Stand tasarımı arayan), `"tasarımı"` (Stand tasarımı arayan), `"kiralama"` (Stand kiralama), `"kiralık"` (Stand kiralama), `"fuar takvimi"` (Ziyaretçi), `"bilet"` (Ziyaretçi), `"hostes"` (İş arayan), `"stand yapımı"` (Stand imalatı arayan)

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Fuar Standı Statik Analizi | 26 |
| 2 | Çift Katlı Stand Statik Rapor | 29 |
| 3 | Fuar Standı Statik Hesabı | 25 |
| 4 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 5 | Fuar Teknik Ofisi İçin Rapor | 28 |
| 6 | Kurulum Öncesi Statik Rapor | 27 |
| 7 | Asma Kat, Merdiven, Korkuluk | 28 |
| 8 | Çelik ve Alüminyum Standlar | 27 |
| 9 | Teknik Ofis Formatına Uygun | 27 |
| 10 | E-İmzalı PDF Rapor | 18 |
| 11 | Stand Tasarımcıları İçin | 24 |
| 12 | Taslak Planla Teklif Alın | 25 |
| 13 | İstanbul Fuarları İçin Rapor | 28 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Çift katlı ve yüksek fuar standları için taşıyıcı sistem hesabı ve imzalı statik rapor. | 87 |
| 2 | Kolon, kiriş, ikinci kat döşemesi, merdiven ve korkuluklar yüklere göre kontrol edilir. | 87 |
| 3 | MMO kayıtlı makina mühendisi imzalı. Şartnamedeki imza şartını teklifte birlikte bakarız. | 89 |
| 4 | Stand planı ve kesitleri (taslak da olur), yükseklik ve fuar adını gönderin, dönelim. | 85 |

### 4.6 Vinç Statik Analizi

- **Nihai URL:** https://www.aymati.com.tr/vinc-statik-analizi.html
- **Görünen yol:** www.aymati.com.tr/Vinc-Statik/Temel (11 / 5 karakter, sınır 15)
- **Not:** Site sahibinin isteğiyle Kaldırma Aparatı grubundan ayrı tutuldu.

**Anahtar kelimeler (17)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[vinç statik analizi]` | Tam |
| `[vinç statik hesabı]` | Tam |
| `[kule vinç temel hesabı]` | Tam |
| `[kule vinç temeli statik]` | Tam |
| `[kule vinç temel projesi]` | Tam |
| `[mobil vinç ayak yükü]` | Tam |
| `[mobil vinç ayak yükü hesabı]` | Tam |
| `[vinç zemin basıncı hesabı]` | Tam |
| `[vinç ayak altı plaka hesabı]` | Tam |
| `[vinç zemin hesabı]` | Tam |
| `[vinç ayak yükü hesabı]` | Tam |
| `"kule vinç temel hesabı"` | Sıralı |
| `"kule vinç temeli"` | Sıralı |
| `"mobil vinç ayak"` | Sıralı |
| `"vinç statik"` | Sıralı |
| `"vinç zemin hesabı"` | Sıralı |
| `"vinç ayak basıncı"` | Sıralı |

**Grup negatifleri (sıralı):** `"kiralama"` (Vinç kiralama), `"kiralık"` (Vinç kiralama), `"operatör"` (Operatör/iş arayan), `"operatörlüğü"` (Operatör belgesi), `"satılık"` (Vinç satın alma), `"sahibinden"` (Vinç satın alma), `"operatörlü"` (Operatörlü kiralama), `"ikinci el"` (Vinç satın alma), `"oyuncak"` (Alakasız)

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Vinç Statik Analizi | 19 |
| 2 | Kule Vinç Temel Hesabı | 22 |
| 3 | Mobil Vinç Ayak Yükü Hesabı | 27 |
| 4 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 5 | Zemin Basıncı ve Altlık Ölçüsü | 30 |
| 6 | Kurulum Öncesi Vinç Raporu | 26 |
| 7 | Temel, Ankraj ve Ayak Yükü | 26 |
| 8 | Döşeme ve Bodrum Üstü Kurulum | 29 |
| 9 | Üretici Yük Tablolarıyla | 24 |
| 10 | E-İmzalı PDF Teslim | 19 |
| 11 | Şantiyeler İçin Statik Rapor | 28 |
| 12 | Vinç Statik Teklifi Alın | 24 |
| 13 | İstanbul Şantiyelerine Hizmet | 29 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Kule vinç temeli, mobil vinç ayak yükü ve zemin basıncı hesabı; imzalı statik rapor. | 84 |
| 2 | Üretici yük tabloları, kaldırma planı ve zemin bilgileriyle kritik durum hesaplanır. | 84 |
| 3 | Rapor MMO kayıtlı makina mühendisi imzalı, e-imzalı PDF olarak teslim edilir. | 77 |
| 4 | Vinç modeli, en ağır yük, çalışma yarıçapı ve kurulum yerinin fotoğrafını gönderin. | 83 |

### 4.7 Kaldırma Aparatı Statik Hesabı

- **Nihai URL:** https://www.aymati.com.tr/kaldirma-aparati-statik-hesabi.html
- **Görünen yol:** www.aymati.com.tr/Kaldirma-Aparat/WLL (15 / 3 karakter, sınır 15)
- **Not:** Site sahibinin isteğiyle Vinç grubundan ayrı tutuldu. "Travers" demiryolu traversiyle karışır; grup negatifleri bunun için.

**Anahtar kelimeler (16)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[kaldırma aparatı statik hesabı]` | Tam |
| `[kaldırma aparatı hesabı]` | Tam |
| `[travers statik hesabı]` | Tam |
| `[kaldırma kirişi hesabı]` | Tam |
| `[kaldırma traversi hesabı]` | Tam |
| `[kaldırma kulağı hesabı]` | Tam |
| `[kaldırma kulağı statik hesabı]` | Tam |
| `[lifting beam hesabı]` | Tam |
| `[spreader beam hesabı]` | Tam |
| `[wll hesabı]` | Tam |
| `[travers hesabı]` | Tam |
| `"kaldırma aparatı statik"` | Sıralı |
| `"kaldırma aparatı hesap"` | Sıralı |
| `"travers hesabı"` | Sıralı |
| `"kaldırma kulağı hesap"` | Sıralı |
| `"kaldırma aparatı belgesi"` | Sıralı |

**Grup negatifleri (sıralı):** `"demiryolu"` (Demiryolu traversi), `"beton travers"` (Demiryolu traversi), `"ray traversi"` (Demiryolu traversi), `"satılık"` (Ürün satın alma), `"satış"` (Ürün satın alma), `"sahibinden"` (Ürün satın alma), `"zincir"` (Zincir/halat ürünü), `"halat"` (Zincir/halat ürünü)

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Kaldırma Aparatı Statik Hesabı | 30 |
| 2 | Travers ve Kaldırma Kirişi | 26 |
| 3 | Kaldırma Kulağı Hesabı | 22 |
| 4 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 5 | Çalışma Yük Sınırı (WLL) | 24 |
| 6 | WLL Etiket Bilgileri Dahil | 26 |
| 7 | Atölye İmalatı Aparatlar İçin | 29 |
| 8 | Kaynak, Pim ve Delik Kontrolü | 29 |
| 9 | Periyodik Kontrol Eksiği İçin | 29 |
| 10 | Gerekirse Güçlendirme Önerisi | 29 |
| 11 | E-İmzalı PDF Rapor | 18 |
| 12 | TS EN 13155 Esas Alınır | 23 |
| 13 | Aparat Hesabı Teklifi Alın | 26 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Atölyede imal edilen travers, kaldırma kirişi ve kulakları için statik hesap ve WLL. | 84 |
| 2 | Gövde, kaynak, pim ve delik bölgeleri ile sapan bağlantı noktaları kontrol edilir. | 82 |
| 3 | MMO kayıtlı makina mühendisi imzalı rapor; aparata yazılacak etiket bilgileri dahil. | 84 |
| 4 | Aparatın fotoğrafını, ana ölçülerini ve kaldırılacak yükü gönderin, dönüş yapalım. | 82 |

### 4.8 Monoray / Vinç Yolu Statik Analizi

- **Nihai URL:** https://www.aymati.com.tr/monoray-vinc-yolu-statik-analizi.html
- **Görünen yol:** www.aymati.com.tr/Monoray/Vinc-Yolu (7 / 9 karakter, sınır 15)

**Anahtar kelimeler (18)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[monoray statik hesabı]` | Tam |
| `[monoray statik analizi]` | Tam |
| `[monoray ray hesabı]` | Tam |
| `[vinç yolu statik hesabı]` | Tam |
| `[vinç yolu kirişi hesabı]` | Tam |
| `[vinç yolu hesabı]` | Tam |
| `[köprülü vinç yolu hesabı]` | Tam |
| `[gezer vinç yolu hesabı]` | Tam |
| `[konsol vinç statik hesabı]` | Tam |
| `[pergel vinç statik hesabı]` | Tam |
| `"monoray statik"` | Sıralı |
| `"vinç yolu statik"` | Sıralı |
| `[vinç yolu statik analizi]` | Tam |
| `[monoray hesabı]` | Tam |
| `"vinç yolu kirişi"` | Sıralı |
| `"monoray hesap"` | Sıralı |
| `"vinç yolu hesap"` | Sıralı |
| `"caraskal rayı hesabı"` | Sıralı |

**Grup negatifleri (sıralı):** `"tren"` (Monoray toplu taşıma), `"metro"` (Monoray toplu taşıma), `"raylı sistem"` (Toplu taşıma), `"istasyon"` (Toplu taşıma), `"imalatı"` (İmalatçı arayan), `"montajı"` (Montajcı arayan), `"satılık"` (Ürün satın alma), `"ikinci el"` (Ürün satın alma)

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Monoray Statik Analizi | 22 |
| 2 | Vinç Yolu Kirişi Hesabı | 23 |
| 3 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 4 | Köprülü ve Konsol Vinç Yolu | 27 |
| 5 | Sahada Ölçüm ve Modelleme | 25 |
| 6 | Tekerlek ve Fren Yükleri | 24 |
| 7 | Sehim ve Bağlantı Kontrolü | 26 |
| 8 | Kapasite Artırımı Öncesi | 24 |
| 9 | Periyodik Kontrol Eksiği İçin | 29 |
| 10 | Fabrikalar İçin Statik Rapor | 28 |
| 11 | E-İmzalı PDF Rapor | 18 |
| 12 | Vinç Yolu Teklifi Alın | 22 |
| 13 | İstanbul Fabrikalarına Hizmet | 29 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Monoray rayı, köprülü vinç yolu kirişi ve konsol vinç taşıyıcı sistemi için statik rapor. | 89 |
| 2 | Kirişler, kolonlar ve bağlantılar sahada ölçülür; tekerlek ve fren yükleri hesaplanır. | 86 |
| 3 | Rapor MMO kayıtlı makina mühendisi tarafından hazırlanır ve imzalanır. | 70 |
| 4 | Vinç kapasitesi artırılacaksa veya ikinci vinç eklenecekse mevcut yapıyı kontrol ederiz. | 88 |

### 4.9 Sahne / Truss / Tribün Statik Analizi

- **Nihai URL:** https://www.aymati.com.tr/sahne-truss-tribun-statik-analizi.html
- **Görünen yol:** www.aymati.com.tr/Sahne-Truss/Statik (11 / 6 karakter, sınır 15)

**Anahtar kelimeler (19)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[sahne statik hesabı]` | Tam |
| `[sahne statik raporu]` | Tam |
| `[sahne statik analizi]` | Tam |
| `[truss statik hesabı]` | Tam |
| `[truss statik raporu]` | Tam |
| `[tribün statik hesabı]` | Tam |
| `[geçici tribün statik raporu]` | Tam |
| `[led ekran kulesi statik]` | Tam |
| `[truss çatı statik hesabı]` | Tam |
| `[etkinlik sahnesi statik rapor]` | Tam |
| `[tribün statik analizi]` | Tam |
| `[geçici tribün statik]` | Tam |
| `[konser sahnesi statik]` | Tam |
| `"sahne statik"` | Sıralı |
| `"truss statik"` | Sıralı |
| `"tribün statik"` | Sıralı |
| `"rigging hesabı"` | Sıralı |
| `"led ekran statik"` | Sıralı |
| `"etkinlik statik rapor"` | Sıralı |

**Grup negatifleri (sıralı):** `"kiralama"` (Ekipman kiralama), `"kiralık"` (Ekipman kiralama), `"bilet"` (Seyirci), `"satılık"` (Ürün satın alma), `"sahibinden"` (Ürün satın alma), `"ses sistemi"` (Ekipman)

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Sahne ve Truss Statik Analizi | 29 |
| 2 | Tribün Statik Hesabı | 20 |
| 3 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 4 | Etkinlik Öncesi Statik Rapor | 28 |
| 5 | Asma Yük (Rigging) Hesabı | 25 |
| 6 | Rüzgâr Yükü ve Balast Hesabı | 28 |
| 7 | LED Ekran Kulesi Hesabı | 23 |
| 8 | Truss Çatı Statik Raporu | 24 |
| 9 | Geçici Tribün Seyirci Yükü | 26 |
| 10 | Belediye ve Organizatör İçin | 28 |
| 11 | E-İmzalı PDF Rapor | 18 |
| 12 | Sahne Statik Teklifi Alın | 25 |
| 13 | Organizasyon Firmaları İçin | 27 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Konser sahnesi, truss çatı, LED ekran kulesi ve geçici tribünler için imzalı statik rapor. | 90 |
| 2 | Asılan ses, ışık ve ekran yükleri, rüzgâr ve seyirci yükü hesaplanır; balast belirlenir. | 88 |
| 3 | Truss üreticisinin yük tabloları ve ekipman listesiyle sistemi modelleyip kontrol ederiz. | 89 |
| 4 | Statik analizleri MMO kayıtlı makina mühendisi hazırlar ve imzalar. Teklif alın. | 80 |

### 4.10 Tabela / Pilon Statik Hesabı

- **Nihai URL:** https://www.aymati.com.tr/tabela-pilon-statik-hesabi.html
- **Görünen yol:** www.aymati.com.tr/Tabela-Pilon/Statik (12 / 6 karakter, sınır 15)

**Anahtar kelimeler (17)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[tabela statik hesabı]` | Tam |
| `[tabela statik raporu]` | Tam |
| `[çatı tabelası statik hesabı]` | Tam |
| `[çatı tabelası statik rapor]` | Tam |
| `[pilon statik hesabı]` | Tam |
| `[totem statik hesabı]` | Tam |
| `[reklam panosu statik hesabı]` | Tam |
| `[tabela rüzgar hesabı]` | Tam |
| `[tabela statik proje]` | Tam |
| `[pilon temel hesabı]` | Tam |
| `"tabela statik"` | Sıralı |
| `"pilon statik"` | Sıralı |
| `"totem statik"` | Sıralı |
| `"çatı tabelası statik"` | Sıralı |
| `"reklam panosu statik"` | Sıralı |
| `"tabela izni statik"` | Sıralı |
| `"belediye tabela statik rapor"` | Sıralı |

**Grup negatifleri (sıralı):** `"tasarım"` (Tabela tasarımı), `"logo"` (Tabela tasarımı), `"neon"` (Tabela imalatı), `"harf"` (Tabela imalatı), `"tabela modelleri"` (Tabela imalatı)

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Tabela Statik Hesabı | 20 |
| 2 | Pilon ve Totem Statik Hesabı | 28 |
| 3 | Çatı Tabelası Statik Raporu | 27 |
| 4 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 5 | Belediye Başvurusu İçin Rapor | 29 |
| 6 | Rüzgâr Yükü Hesabı | 18 |
| 7 | Konstrüksiyon ve Ankraj | 23 |
| 8 | Pilon Temeli ve Devrilme | 24 |
| 9 | Reklam Panosu Statik Hesap | 26 |
| 10 | Taşıyıcı Sistem Çizimi Dahil | 28 |
| 11 | E-İmzalı PDF Rapor | 18 |
| 12 | Tabela Statik Teklifi Alın | 26 |
| 13 | Tabela Firmaları İçin Hesap | 27 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Çatı ve cephe tabelası, reklam panosu ve pilonlar için rüzgâr yükü ve statik hesap. | 83 |
| 2 | Taşıyıcı profiller, bağlantılar, ankraj cıvataları ve pilon temeli kontrol edilir. | 82 |
| 3 | Belediye başvurusu için taşıyıcı sistem çizimi ve MMO kayıtlı mühendis imzalı rapor. | 84 |
| 4 | Belediyenin istediği belgeleri birlikte teyit edelim. Tabela ölçülerini gönderin. | 81 |

## 5. Kampanya: PKD

Bütçe payı **%20**. Üç grup da `patlamadan-korunma-dokumani.html` sayfasına gider (sitede ATEX veya toz patlaması için ayrı sayfa yok). Metinlerde mühendis veya meslek odası iddiası **yok**. Kampanya negatifleri "PKD" kısaltmasının tıp anlamını (polikistik böbrek hastalığı), ATEX ürün ve ekipman alımını ve şablon arayanları dışarıda bırakır.

### 5.1 PKD Genel

- **Nihai URL:** https://www.aymati.com.tr/patlamadan-korunma-dokumani.html
- **Görünen yol:** www.aymati.com.tr/PKD/Hazirlama (3 / 9 karakter, sınır 15)

**Anahtar kelimeler (17)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[patlamadan korunma dokümanı]` | Tam |
| `[patlamadan korunma dökümanı]` | Tam |
| `[patlamadan korunma dokümanı hazırlama]` | Tam |
| `[patlamadan korunma dokümanı hazırlayan firmalar]` | Tam |
| `[patlamadan korunma dokümanı güncelleme]` | Tam |
| `[patlamadan korunma dokümanı zorunlu mu]` | Tam |
| `[pkd hazırlama]` | Tam |
| `[pkd raporu]` | Tam |
| `[pkd hazırlatmak]` | Tam |
| `[pkd güncelleme]` | Tam |
| `"patlamadan korunma dokümanı"` | Sıralı |
| `"patlamadan korunma dökümanı"` | Sıralı |
| `"pkd hazırlayan firma"` | Sıralı |
| `"pkd hazırlama"` | Sıralı |
| `"patlamadan korunma dokümanı istanbul"` | Sıralı |
| `"tuzla patlamadan korunma dokümanı"` | Sıralı |
| `"tuzla osb pkd"` | Sıralı |

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Patlamadan Korunma Dokümanı | 27 |
| 2 | PKD Hazırlama | 13 |
| 3 | Tesisiniz Yerinde İncelenir | 27 |
| 4 | ATEX Bölge Sınıflandırması | 26 |
| 5 | Patlama Riski Değerlendirmesi | 29 |
| 6 | Bölge Haritaları Dahil | 22 |
| 7 | Tutuşturucu Kaynak Analizi | 26 |
| 8 | Ex Ekipman Uygunluk Kontrolü | 28 |
| 9 | Uygunsuzluk ve Eylem Planı | 26 |
| 10 | Yönetmeliğe Uygun PKD | 21 |
| 11 | PKD Güncelleme | 14 |
| 12 | Tadilat Sonrası Güncelleme | 26 |
| 13 | PKD İçin Teklif Alın | 20 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Patlamadan korunma dokümanı: ATEX bölge sınıflandırması ve patlama riski değerlendirmesi. | 89 |
| 2 | Prosesleri, depolama alanlarını, havalandırmayı ve ekipmanları yerinde inceliyoruz. | 83 |
| 3 | Tutuşturucu kaynak analizi, Ex ekipman uygunluğu, bölge haritaları ve önlem önerileri. | 86 |
| 4 | PKD işe başlamadan önce hazırlanır, önemli değişikliklerde güncellenir. Teklif alın. | 84 |

### 5.2 ATEX / Tehlikeli Bölge Sınıflandırması

- **Nihai URL:** https://www.aymati.com.tr/patlamadan-korunma-dokumani.html
- **Görünen yol:** www.aymati.com.tr/ATEX/Zone (4 / 4 karakter, sınır 15)
- **Not:** ATEX ürün aramaları (Ex motor, armatür, sertifikalı ekipman) kampanya negatifleriyle dışarıda bırakılır.

**Anahtar kelimeler (15)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[atex bölge sınıflandırması]` | Tam |
| `[tehlikeli bölge sınıflandırması]` | Tam |
| `[atex zone sınıflandırması]` | Tam |
| `[ex bölge sınıflandırması]` | Tam |
| `[patlayıcı ortam bölge sınıflandırması]` | Tam |
| `[atex risk analizi]` | Tam |
| `[atex risk değerlendirmesi]` | Tam |
| `[patlama riski değerlendirmesi]` | Tam |
| `[patlayıcı ortam risk değerlendirmesi]` | Tam |
| `[atex bölge haritası]` | Tam |
| `"atex bölge sınıflandırması"` | Sıralı |
| `"tehlikeli bölge sınıflandırması"` | Sıralı |
| `"atex risk analizi"` | Sıralı |
| `"ex zone sınıflandırması"` | Sıralı |
| `"patlama riski değerlendirmesi"` | Sıralı |

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | ATEX Bölge Sınıflandırması | 26 |
| 2 | Tehlikeli Bölge Sınıflandırma | 29 |
| 3 | Zone 0, 1, 2 ve 20, 21, 22 | 26 |
| 4 | Gaz, Buhar ve Toz Bölgeleri | 27 |
| 5 | Bölge Haritaları Plan Üzerinde | 30 |
| 6 | Patlama Riski Değerlendirmesi | 29 |
| 7 | Ex Ekipman Kategori Kontrolü | 28 |
| 8 | Tutuşturucu Kaynak Analizi | 26 |
| 9 | Patlamadan Korunma Dokümanı | 27 |
| 10 | Tesisiniz Yerinde İncelenir | 27 |
| 11 | Teknik ve Organizasyonel Önlem | 30 |
| 12 | Boyahane, Kimya, LPG Alanları | 29 |
| 13 | ATEX Çalışması İçin Teklif | 26 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Gaz ve buhar için Zone 0, 1, 2; yanıcı toz için Zone 20, 21, 22 bölgelerini belirliyoruz. | 89 |
| 2 | Tehlikeli bölgeler kat planları üzerinde sınırları ve uzaklıklarıyla haritalanır. | 81 |
| 3 | Bölgelerdeki elektrikli ve mekanik ekipmanın uygun Ex kategorisinde olduğu kontrol edilir. | 90 |
| 4 | Sınıflandırma, patlamadan korunma dokümanının parçası olarak eylem planıyla teslim edilir. | 90 |

### 5.3 Toz Patlaması ve Sektörel PKD

- **Nihai URL:** https://www.aymati.com.tr/patlamadan-korunma-dokumani.html
- **Görünen yol:** www.aymati.com.tr/PKD/Toz-Patlamasi (3 / 13 karakter, sınır 15)
- **Not:** Hacmi düşük; sektör aramalarında reklam metnini sektöre yaklaştırmak için ayrı tutuldu. 4 hafta sonunda gösterim yoksa PKD Genel ile birleştirilebilir.

**Anahtar kelimeler (16)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[toz patlaması risk değerlendirmesi]` | Tam |
| `[yanıcı toz patlama riski]` | Tam |
| `[un fabrikası patlamadan korunma dokümanı]` | Tam |
| `[boyahane patlamadan korunma dokümanı]` | Tam |
| `[boya kabini atex]` | Tam |
| `[akü şarj odası atex]` | Tam |
| `[akü şarj odası patlamadan korunma]` | Tam |
| `[lpg tankı patlamadan korunma dokümanı]` | Tam |
| `[akaryakıt istasyonu patlamadan korunma dokümanı]` | Tam |
| `[ahşap tozu patlama riski]` | Tam |
| `"toz patlaması risk"` | Sıralı |
| `"boyahane patlamadan korunma"` | Sıralı |
| `"akü şarj odası atex"` | Sıralı |
| `"akaryakıt istasyonu pkd"` | Sıralı |
| `"mobilya atölyesi pkd"` | Sıralı |
| `"toz patlaması atex"` | Sıralı |

**Grup negatifleri (sıralı):** `"haber"` (Kaza haberi), `"haberleri"` (Kaza haberi), `"son dakika"` (Kaza haberi)

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Toz Patlaması Risk Analizi | 26 |
| 2 | Yanıcı Toz İçin Zone 20-22 | 26 |
| 3 | Boyahane ve Solvent Alanları | 28 |
| 4 | Akü Şarj Odası (Hidrojen) | 25 |
| 5 | Un, Yem ve Tahıl Tesisleri | 26 |
| 6 | Ahşap ve Mobilya Atölyeleri | 27 |
| 7 | LPG ve Akaryakıt Tesisleri | 26 |
| 8 | Metal Tozu ve Taşlama Alanı | 27 |
| 9 | Patlamadan Korunma Dokümanı | 27 |
| 10 | Tesisiniz Yerinde İncelenir | 27 |
| 11 | Toz Birikimi Değerlendirilir | 28 |
| 12 | Bölge Haritaları Dahil | 22 |
| 13 | Sektörünüze Göre PKD | 20 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Un, yem, ahşap, metal tozu ve boya alanlarında patlayıcı ortam riskini değerlendiriyoruz. | 89 |
| 2 | Yığılmış veya katmanlaşmış yanıcı toz da patlayıcı ortam kaynağı olarak ele alınır. | 83 |
| 3 | Boyahane, akü şarj odası, LPG ve akaryakıt alanları için bölge sınıflandırması ve PKD. | 86 |
| 4 | Tesisinizdeki yanıcı maddeleri ve prosesleri yazın, kapsamı birlikte belirleyelim. | 82 |

## 6. Kampanya: Projelendirme

Bütçe payı **%30**. İmza ifadeleri sayfalarla uyumlu: elektrik grubu (elektrik projesi, tek hat şeması, yangın algılama, yıldırımdan korunma) "EMO kayıtlı S.M.M. elektrik mühendisi"; mekanik grubu (sprinkler, havalandırma, tahliye planı) "MMO kayıtlı makina mühendisi". Faraday kafesi hesaplama grubunda imza iddiası yok. `otomatik-gazli-yangin-sondurme-fm-200-projesi.html` sayfası da var ama hacmi çok düşük olduğu için ilk ay grup açılmadı.

### 6.1 Elektrik Projesi / Rölöve

- **Nihai URL:** https://www.aymati.com.tr/elektrik-ic-tesisat-projesi.html
- **Görünen yol:** www.aymati.com.tr/Elektrik-Proje/Rolove (14 / 6 karakter, sınır 15)

**Anahtar kelimeler (20)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[elektrik projesi]` | Tam |
| `[elektrik iç tesisat projesi]` | Tam |
| `[elektrik tesisat projesi]` | Tam |
| `[elektrik rölöve projesi]` | Tam |
| `[elektrik rölövesi]` | Tam |
| `[fabrika elektrik projesi]` | Tam |
| `[iş yeri elektrik projesi]` | Tam |
| `[işyeri elektrik projesi]` | Tam |
| `[mevcut bina elektrik projesi]` | Tam |
| `[elektrik projesi çizimi]` | Tam |
| `[elektrik proje firması]` | Tam |
| `"elektrik projesi çizdirmek"` | Sıralı |
| `"elektrik iç tesisat projesi"` | Sıralı |
| `"elektrik rölöve"` | Sıralı |
| `"elektrik projesi istanbul"` | Sıralı |
| `"fabrika elektrik projesi"` | Sıralı |
| `"ikitelli elektrik projesi"` | Sıralı |
| `"başakşehir elektrik projesi"` | Sıralı |
| `"esenyurt elektrik projesi"` | Sıralı |
| `"beylikdüzü elektrik projesi"` | Sıralı |

**Grup negatifleri (sıralı):** `"arduino"` (Hobi/öğrenci), `"lise"` (Öğrenci), `"deney"` (Öğrenci)

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
| 10 | Kuvvetli ve Zayıf Akım Projesi | 30 |
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

### 6.2 Elektrik Projesi Eksik (Periyodik Kontrol)

- **Nihai URL:** https://www.aymati.com.tr/elektrik-ic-tesisat-projesi.html
- **Görünen yol:** www.aymati.com.tr/Elektrik-Proje/Eksik (14 / 5 karakter, sınır 15)
- **Not:** Aynı sayfaya giden ikinci grup: "periyodik kontrolde proje eksik" niyetine özel reklam metni. Hacmi düşükse 4. haftada Elektrik Projesi / Rölöve grubuyla birleştirilebilir.

**Anahtar kelimeler (15)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[elektrik projesi yok]` | Tam |
| `[elektrik projesi eksik]` | Tam |
| `[periyodik kontrol elektrik projesi]` | Tam |
| `[periyodik kontrol için elektrik projesi]` | Tam |
| `[elektrik projesi olmayan bina]` | Tam |
| `[elektrik iç tesisat projesi yok]` | Tam |
| `[elektrik projesi istendi]` | Tam |
| `[eski bina elektrik projesi]` | Tam |
| `[elektrik projesi kayıp]` | Tam |
| `[elektrik projesi güncelleme]` | Tam |
| `"elektrik projesi yok"` | Sıralı |
| `"elektrik projesi eksik"` | Sıralı |
| `"periyodik kontrol elektrik projesi"` | Sıralı |
| `"elektrik projesi güncelleme"` | Sıralı |
| `"proje eksik uygunsuzluk"` | Sıralı |

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Elektrik Projesi Eksik mi? | 26 |
| 2 | Kontrolde Proje Eksik Çıktıysa | 30 |
| 3 | Yerinde Rölöve ile Proje | 24 |
| 4 | EMO Kayıtlı Mühendis İmzalı | 27 |
| 5 | Mevcut Tesise Rölöve Projesi | 28 |
| 6 | Bugünkü Duruma Göre Çizim | 25 |
| 7 | Uygunsuzluk Kapatmak İçin | 25 |
| 8 | Eski Binalar İçin Elektrik | 26 |
| 9 | Tek Hat ve Kolon Şeması | 23 |
| 10 | Kısa Devre ve Kesit Hesabı | 26 |
| 11 | S.M.M. İmzalı Elektrik Proje | 28 |
| 12 | Ozalit Baskı Teslim | 19 |
| 13 | Rölöve Projesi Teklifi Alın | 27 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Periyodik kontrolde elektrik projesi eksik mi çıktı? Tesisinizde yerinde rölöve alıyoruz. | 89 |
| 2 | Proje, sahadaki gerçek tesisata göre çizilir; tek hat şeması ve hesaplar dahildir. | 82 |
| 3 | Projeler EMO kayıtlı S.M.M. elektrik mühendisi tarafından hazırlanır ve imzalanır. | 82 |
| 4 | Raporda yazan uygunsuzluğu ve tesis bilgilerinizi gönderin, kapsamı birlikte belirleyelim. | 90 |

### 6.3 Pano Tek Hat Şeması

- **Nihai URL:** https://www.aymati.com.tr/pano-tek-hat-semasi-projesi.html
- **Görünen yol:** www.aymati.com.tr/Tek-Hat/Pano (7 / 4 karakter, sınır 15)

**Anahtar kelimeler (14)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[pano tek hat şeması]` | Tam |
| `[tek hat şeması çizimi]` | Tam |
| `[tek hat şeması çizdirme]` | Tam |
| `[pano tek hat şeması çizimi]` | Tam |
| `[elektrik panosu tek hat şeması]` | Tam |
| `[tek hat şeması yok]` | Tam |
| `[pano şeması çizimi]` | Tam |
| `[tek hat şeması projesi]` | Tam |
| `[ana dağıtım panosu tek hat şeması]` | Tam |
| `[pano rölövesi]` | Tam |
| `"tek hat şeması çizimi"` | Sıralı |
| `"pano tek hat şeması"` | Sıralı |
| `"tek hat şeması çizen"` | Sıralı |
| `"pano şeması çizdirmek"` | Sıralı |

**Grup negatifleri (sıralı):** `"nasıl okunur"` (Bilgi amaçlı), `"eplan"` (Yazılım)

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Pano Tek Hat Şeması | 19 |
| 2 | Tek Hat Şeması Çizimi | 21 |
| 3 | EMO Kayıtlı Mühendis İmzalı | 27 |
| 4 | Panolar Yerinde İncelenir | 25 |
| 5 | Sahadaki Koruma Elemanlarıyla | 29 |
| 6 | Her Pano İçin Ayrı Pafta | 24 |
| 7 | Kaçak Akım Röleleri Dahil | 25 |
| 8 | Uygunsuzluk Notları Dahil | 25 |
| 9 | Tek Hat Şeması Eksikse | 22 |
| 10 | Ana ve Tali Dağıtım Panoları | 28 |
| 11 | E-İmzalı PDF Teslim | 19 |
| 12 | Tek Hat Şeması Teklifi Alın | 27 |
| 13 | Batı Yakası OSB'lerine Hizmet | 29 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Panolarınızı sahada tek tek inceliyor, tek hat şemasını bugünkü duruma göre çiziyoruz. | 86 |
| 2 | Her koruma elemanının akım değeri, kutup sayısı ve kesme kapasitesi yerinde okunur. | 83 |
| 3 | Şemalar EMO kayıtlı S.M.M. elektrik mühendisi imzalıdır; her pano için ayrı pafta. | 82 |
| 4 | Periyodik kontrolde tek hat şeması eksik mi yazıldı? Pano sayınızı gönderin, dönelim. | 85 |

### 6.4 Yangın Algılama ve İhbar Projesi

- **Nihai URL:** https://www.aymati.com.tr/yangin-algilama-ve-ihbar-sistemleri-projesi.html
- **Görünen yol:** www.aymati.com.tr/Yangin-Algilama/Proje (15 / 5 karakter, sınır 15)

**Anahtar kelimeler (14)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[yangın algılama projesi]` | Tam |
| `[yangın algılama sistemi projesi]` | Tam |
| `[yangın ihbar projesi]` | Tam |
| `[yangın algılama ve ihbar projesi]` | Tam |
| `[yangın alarm projesi]` | Tam |
| `[yangın algılama proje çizimi]` | Tam |
| `[yangın algılama rölöve projesi]` | Tam |
| `[dedektör yerleşim projesi]` | Tam |
| `[yangın algılama projesi itfaiye]` | Tam |
| `[zayıf akım yangın projesi]` | Tam |
| `"yangın algılama projesi"` | Sıralı |
| `"yangın alarm projesi"` | Sıralı |
| `"yangın ihbar projesi"` | Sıralı |
| `"yangın algılama sistemi projesi"` | Sıralı |

**Grup negatifleri (sıralı):** `"ev tipi"` (Konut ürünü)

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Yangın Algılama Projesi | 23 |
| 2 | Yangın İhbar Sistemi Projesi | 28 |
| 3 | EMO Kayıtlı Mühendis İmzalı | 27 |
| 4 | Dedektör, Buton, Siren, Panel | 29 |
| 5 | Mevcut Sisteme Rölöve Projesi | 29 |
| 6 | İtfaiye ve İskân İçin Proje | 27 |
| 7 | Kablolama ve Adresleme | 22 |
| 8 | TS CEN/TS 54-14'e Uygun | 23 |
| 9 | Mahale Göre Dedektör Seçimi | 27 |
| 10 | Periyodik Kontrol Eksiği İçin | 29 |
| 11 | Sigorta Dokümantasyonu İçin | 27 |
| 12 | Ozalit Baskı Teslim | 19 |
| 13 | Yangın Projesi Teklifi Alın | 27 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Duman ve ısı dedektörü, ihbar butonu, siren ve panel yerleşimi; kablolama ve adresleme. | 87 |
| 2 | Mevcut sistemi sahada tespit ediyor, kapsama alanını kontrol ederek projeyi çiziyoruz. | 86 |
| 3 | Proje EMO kayıtlı S.M.M. elektrik mühendisi tarafından çizilir ve imzalanır. | 76 |
| 4 | İtfaiye, iskân, periyodik kontrol veya sigorta için proje mi istendi? Teklif alın. | 82 |

### 6.5 Yıldırımdan Korunma / Paratoner / Faraday

- **Nihai URL:** https://www.aymati.com.tr/yildirimdan-korunma-tesisati-projesi.html
- **Görünen yol:** www.aymati.com.tr/Paratoner/Proje (9 / 5 karakter, sınır 15)
- **Not:** "Faraday kafesi projesi" aramaları bu grupta kalır; hesap/hesaplama/maliyet aramaları PR #6 ile yayına giren hesaplama aracına giden ayrı gruptadır.

**Anahtar kelimeler (14)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[paratoner projesi]` | Tam |
| `[yıldırımdan korunma projesi]` | Tam |
| `[yıldırımdan korunma tesisatı projesi]` | Tam |
| `[yıldırım risk analizi]` | Tam |
| `[yıldırım risk analizi raporu]` | Tam |
| `[paratoner risk analizi]` | Tam |
| `[faraday kafesi projesi]` | Tam |
| `[paratoner koruma alanı hesabı]` | Tam |
| `[ts en 62305 risk analizi]` | Tam |
| `"paratoner projesi"` | Sıralı |
| `"yıldırımdan korunma projesi"` | Sıralı |
| `"yıldırım risk analizi"` | Sıralı |
| `"faraday kafesi projesi"` | Sıralı |
| `"paratoner projesi istanbul"` | Sıralı |

**Grup negatifleri (sıralı):** `"deney"` (Fizik deneyi), `"fizik"` (Fizik dersi), `"araba"` (Araçta Faraday etkisi), `"araç"` (Araçta Faraday etkisi), `"nasıl çalışır"` (Bilgi amaçlı), `"telefon"` (Alakasız)

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Yıldırımdan Korunma Projesi | 27 |
| 2 | Paratoner Projesi | 17 |
| 3 | Yıldırım Risk Analizi | 21 |
| 4 | EMO Kayıtlı Mühendis İmzalı | 27 |
| 5 | Faraday Kafesi Projesi | 22 |
| 6 | TS EN 62305-2 Risk Analizi | 26 |
| 7 | Koruma Alanı Hesabı | 19 |
| 8 | Yakalama Ucu ve İniş İletkeni | 29 |
| 9 | Ölçekli Plan ve Kesit Çizimi | 28 |
| 10 | Parafudr (SPD) Seçimi | 21 |
| 11 | Güneş Paneli Eklendiyse | 23 |
| 12 | Periyodik Kontrol Eksiği İçin | 29 |
| 13 | Paratoner Projesi Teklifi | 25 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | TS EN 62305-2'ye göre yıldırım risk analizi yapıp gerekli koruma seviyesini belirliyoruz. | 89 |
| 2 | Yakalama uçları veya Faraday kafesi, iniş iletkenleri ve topraklama bağlantısı çizilir. | 87 |
| 3 | Koruma alanını binanın gerçek ölçülerine göre hesaplayıp ölçekli çizimle gösteriyoruz. | 86 |
| 4 | EMO kayıtlı S.M.M. elektrik mühendisi imzalı. Periyodik kontrolde eksik çıktıysa yazın. | 87 |

### 6.6 Faraday Kafesi Hesaplama

- **Nihai URL:** https://www.aymati.com.tr/faraday-kafesi-hesaplama.html
- **Görünen yol:** www.aymati.com.tr/Faraday-Kafesi/Hesaplama (14 / 9 karakter, sınır 15)
- **Not:** Hesaplama aracı sayfası (PR #6 ile yayında). Sayfada dolar bazında ön bütçe gösterilir; reklam metninde fiyat, tutar veya para birimi yazılmaz. Grupta mühendis odası iddiası yok (araç sayfası imzalı belge sunmaz).

**Anahtar kelimeler (12)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[faraday kafesi hesabı]` | Tam |
| `[faraday kafesi hesaplama]` | Tam |
| `[faraday kafesi maliyeti]` | Tam |
| `[faraday kafesi göz aralığı]` | Tam |
| `[faraday kafesi malzeme hesabı]` | Tam |
| `[faraday kafesi iniş iletkeni]` | Tam |
| `[çatı faraday kafesi]` | Tam |
| `"faraday kafesi hesabı"` | Sıralı |
| `"faraday kafesi hesaplama"` | Sıralı |
| `"faraday kafesi maliyet"` | Sıralı |
| `"faraday kafesi göz aralığı"` | Sıralı |
| `"faraday kafesi malzeme"` | Sıralı |

**Grup negatifleri (sıralı):** `"deney"` (Fizik deneyi), `"fizik"` (Fizik dersi), `"araba"` (Araçta Faraday etkisi), `"araç"` (Araçta Faraday etkisi), `"nasıl çalışır"` (Bilgi amaçlı), `"telefon"` (Alakasız), `"çanta"` (Faraday çantası ürünü)

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Faraday Kafesi Hesaplama | 24 |
| 2 | Çatı m² ile Faraday Hesabı | 26 |
| 3 | Göz Aralığı ve İniş İletkeni | 28 |
| 4 | TS EN 62305-3 Ağ Yöntemi | 24 |
| 5 | Topraklama Uzunluğu Hesabı | 26 |
| 6 | Yerleşim Çizimi Ekranda | 23 |
| 7 | Malzeme Listesi ve Ön Bütçe | 27 |
| 8 | Koruma Sınıfı I-IV Seçimi | 25 |
| 9 | Galvaniz veya Bakır İletken | 27 |
| 10 | Kesin Teklif Keşif Sonrası | 26 |
| 11 | Faraday Kafesi Projesi | 22 |
| 12 | Yıldırım Risk Analizi | 21 |
| 13 | Çatınız İçin Teklif Alın | 24 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Çatı alanını girin; göz aralığı, iniş iletkeni sayısı ve topraklama uzunluğunu görün. | 85 |
| 2 | Hesap TS EN 62305-3 ağ (göz) yöntemine göredir; koruma sınıfını siz seçersiniz. | 79 |
| 3 | Araç ön bütçe içindir; kesin teklif çatı tipi ve keşiften sonra verilir. | 72 |
| 4 | Kesin koruma sınıfı TS EN 62305-2 risk analiziyle belirlenir; projesini de hazırlıyoruz. | 88 |

### 6.7 Sulu Söndürme / Sprinkler Projesi

- **Nihai URL:** https://www.aymati.com.tr/sulu-sondurme-yangin-tesisat-projesi.html
- **Görünen yol:** www.aymati.com.tr/Sprinkler/Proje (9 / 5 karakter, sınır 15)

**Anahtar kelimeler (16)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[sprinkler projesi]` | Tam |
| `[yangın sprinkler projesi]` | Tam |
| `[sulu söndürme projesi]` | Tam |
| `[yangın tesisatı projesi]` | Tam |
| `[yangın tesisat projesi]` | Tam |
| `[sprinkler hidrolik hesap]` | Tam |
| `[sprinkler hidrolik hesabı]` | Tam |
| `[yangın dolabı projesi]` | Tam |
| `[hidrant projesi]` | Tam |
| `[yangın pompası hesabı]` | Tam |
| `[yangın suyu deposu hesabı]` | Tam |
| `"sprinkler projesi"` | Sıralı |
| `"yangın tesisat projesi"` | Sıralı |
| `"sulu söndürme projesi"` | Sıralı |
| `"sprinkler hidrolik hesap"` | Sıralı |
| `"yangın dolabı projesi"` | Sıralı |

**Grup negatifleri (sıralı):** `"bahçe"` (Bahçe sulama), `"çim"` (Bahçe sulama), `"sulama"` (Bahçe sulama)

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Sprinkler Projesi | 17 |
| 2 | Sulu Söndürme Tesisat Projesi | 29 |
| 3 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 4 | Hidrolik Hesap Raporu Dahil | 27 |
| 5 | Yangın Dolabı ve Hidrant | 24 |
| 6 | Pompa ve Depo Hesapları | 23 |
| 7 | Hatlar Sahada İzlenir | 21 |
| 8 | Mevcut Tesisata Göre Hesap | 26 |
| 9 | İtfaiye ve Sigorta İçin Proje | 29 |
| 10 | Raf Yüksekliği Değiştiyse | 25 |
| 11 | Depo ve Fabrikalar İçin | 23 |
| 12 | Ozalit Baskı Teslim | 19 |
| 13 | Sprinkler Projesi Teklifi | 25 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Sprinkler, yangın dolabı, hidrant, pompa istasyonu ve yangın suyu deposu projesi. | 81 |
| 2 | En elverişsiz noktadan pompaya kadar debi ve basınç hidrolik hesapla gösterilir. | 80 |
| 3 | Hatları sahada izleyip ölçüyor, hesapları bugünkü tesisata göre yapıyoruz. | 74 |
| 4 | Proje MMO kayıtlı makina mühendisi imzalı teslim edilir. Tesis bilgilerinizi gönderin. | 86 |

### 6.8 Acil Durum Tahliye Planı

- **Nihai URL:** https://www.aymati.com.tr/acil-durum-tahliye-plani-projesi.html
- **Görünen yol:** www.aymati.com.tr/Tahliye-Plani/Cizim (13 / 5 karakter, sınır 15)

**Anahtar kelimeler (15)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[tahliye planı çizimi]` | Tam |
| `[acil durum tahliye planı]` | Tam |
| `[acil durum tahliye planı çizimi]` | Tam |
| `[kaçış planı çizimi]` | Tam |
| `[yangın tahliye planı]` | Tam |
| `[tahliye krokisi]` | Tam |
| `[acil çıkış krokisi]` | Tam |
| `[iso 23601 tahliye planı]` | Tam |
| `[tahliye planı hazırlama]` | Tam |
| `[tahliye planı çizdirmek]` | Tam |
| `"tahliye planı çizimi"` | Sıralı |
| `"acil durum tahliye planı"` | Sıralı |
| `"kaçış planı"` | Sıralı |
| `"tahliye krokisi"` | Sıralı |
| `"yangın tahliye planı"` | Sıralı |

**Grup negatifleri (sıralı):** `"kiracı"` (Kira tahliyesi), `"taahhütname"` (Kira tahliyesi), `"ihtarname"` (Kira tahliyesi), `"film"` (Alakasız), `"dizi"` (Alakasız), `"oyun"` (Alakasız)

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Acil Durum Tahliye Planı | 24 |
| 2 | Tahliye Planı Çizimi | 20 |
| 3 | ISO 23601 Kaçış Planı | 21 |
| 4 | ISO 7010 Sembolleriyle | 22 |
| 5 | Her Kat İçin Ayrı Plan | 22 |
| 6 | A3 Laminasyonlu Baskı + PDF | 27 |
| 7 | Çıkışlar Yerinde Tespit | 23 |
| 8 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 9 | Duvara Asılmaya Hazır Plan | 26 |
| 10 | Toplanma Yeri ve Ekipmanlar | 27 |
| 11 | İSG ve İtfaiye Kontrolü İçin | 28 |
| 12 | Fabrika, Depo ve Ofisler İçin | 29 |
| 13 | Tahliye Planı Teklifi Alın | 26 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Her kat ve asılma noktası için ayrı çizilen, ISO 7010 sembollü acil durum tahliye planı. | 88 |
| 2 | Çıkışları, söndürücüleri ve riskli alanları yerinde tespit edip kat planına işliyoruz. | 86 |
| 3 | Planlar A3 laminasyonlu baskı ve PDF olarak, duvara asılmaya hazır teslim edilir. | 81 |
| 4 | Bina yerleşimi değiştiyse planınızı güncelleyelim. Kat sayısını ve alanı yazın. | 79 |

### 6.9 Havalandırma Tesisat Projesi

- **Nihai URL:** https://www.aymati.com.tr/havalandirma-tesisat-projesi.html
- **Görünen yol:** www.aymati.com.tr/Havalandirma/Proje (12 / 5 karakter, sınır 15)

**Anahtar kelimeler (15)**

| Anahtar kelime | Eşleme |
| --- | --- |
| `[havalandırma projesi]` | Tam |
| `[havalandırma tesisat projesi]` | Tam |
| `[havalandırma tesisatı projesi]` | Tam |
| `[hava debisi hesabı]` | Tam |
| `[havalandırma hesabı]` | Tam |
| `[fabrika havalandırma projesi]` | Tam |
| `[atölye havalandırma projesi]` | Tam |
| `[otopark havalandırma projesi]` | Tam |
| `[duman tahliye projesi]` | Tam |
| `[havalandırma rölöve projesi]` | Tam |
| `"havalandırma projesi"` | Sıralı |
| `"havalandırma tesisat projesi"` | Sıralı |
| `"hava debisi hesabı"` | Sıralı |
| `"fabrika havalandırma projesi"` | Sıralı |
| `"otopark havalandırma projesi"` | Sıralı |

**Grup negatifleri (sıralı):** `"banyo"` (Konut), `"mutfak"` (Konut), `"davlumbaz"` (Konut), `"kanal temizliği"` (Temizlik hizmeti)

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Havalandırma Tesisat Projesi | 28 |
| 2 | Hava Debisi Hesabı | 18 |
| 3 | MMO Kayıtlı Mühendis İmzalı | 27 |
| 4 | Ünite ve Kanallar Yerinde | 25 |
| 5 | Fabrika ve Atölyeler İçin | 25 |
| 6 | Kaynak, Boya, Kimyasal Alanı | 28 |
| 7 | Otopark ve Kazan Dairesi | 24 |
| 8 | Duman Tahliyesi Kontrolü | 24 |
| 9 | Mevcut Sistem Yeterli mi? | 25 |
| 10 | Öneriler Rapora Eklenir | 23 |
| 11 | İSG Denetimi İçin Proje | 23 |
| 12 | Ozalit Baskı Teslim | 19 |
| 13 | Havalandırma Teklifi Alın | 25 |
| 14 | Aymati Proje Mühendislik | 24 |
| 15 | Arayın veya WhatsApp Yazın | 26 |

**Açıklamalar (4, sınır 90)**

| # | Açıklama | Kr. |
| --- | --- | --- |
| 1 | Aspiratör, fan, klima santrali ve kanalların yerini, kapasitesini gösteren mekanik proje. | 89 |
| 2 | Mahal hacmine ve kullanımına göre gerekli hava değişimi ve debi hesaplanır. | 75 |
| 3 | Yetersiz kalan alanlar için önerilerimizi rapora ekliyoruz. MMO kayıtlı mühendis imzalı. | 88 |
| 4 | Periyodik kontrol veya İSG denetiminde havalandırma projesi mi istendi? Teklif alın. | 84 |

## 7. Kampanya: Muayene ve İş Hijyeni (ikincil)

Bütçe payı **%10** (ikincil). İlk sürümdeki üç grup korundu; yalnızca doğrulanamayan iki başlık düzeltildi ve PR #15'teki bölge anahtar kelimeleri eklendi. Kampanya negatifi `"projesi"`, proje niyetli aramaları Projelendirme kampanyasına bırakır.

### 7.1 Topraklama Ölçümü

- **Nihai URL:** https://www.aymati.com.tr/topraklama-olcumu.html
- **Görünen yol:** www.aymati.com.tr/Topraklama/Olcum (10 / 5 karakter, sınır 15)

**Anahtar kelimeler (17)**

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
| `"topraklama ölçümü istanbul"` | Sıralı |
| `"çevrim empedansı ölçümü"` | Sıralı |
| `"süreklilik ölçümü"` | Sıralı |
| `"topraklama kontrolü"` | Sıralı |
| `"ikitelli topraklama ölçümü"` | Sıralı |
| `"esenyurt topraklama ölçümü"` | Sıralı |
| `"beylikdüzü osb topraklama"` | Sıralı |

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Topraklama Ölçümü | 17 |
| 2 | Topraklama Ölçüm Raporu | 23 |
| 3 | Mühendis Tarafından Ölçüm | 25 |
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

### 7.2 Forklift Periyodik Kontrolü

- **Nihai URL:** https://www.aymati.com.tr/forklift-periyodik-kontrolu.html
- **Görünen yol:** www.aymati.com.tr/Forklift/Periyodik (8 / 9 karakter, sınır 15)

**Anahtar kelimeler (15)**

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
| `"hadımköy forklift kontrolü"` | Sıralı |

**Grup negatifleri (sıralı):** `"operatör"` (Operatör belgesi), `"ehliyet"` (Operatör belgesi), `"satılık"` (Forklift satın alma), `"kiralık"` (Forklift kiralama), `"kiralama"` (Forklift kiralama), `"ikinci el"` (Forklift satın alma), `"sahibinden"` (Forklift satın alma)

**Başlıklar (15, sınır 30)**

| # | Başlık | Kr. |
| --- | --- | --- |
| 1 | Forklift Periyodik Kontrolü | 27 |
| 2 | Forklift Muayene Raporu | 23 |
| 3 | Mühendis Tarafından Kontrol | 27 |
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

### 7.3 İş Hijyeni Ölçümleri

- **Nihai URL:** https://www.aymati.com.tr/is-hijyeni-olcumleri.html
- **Görünen yol:** www.aymati.com.tr/Is-Hijyeni/Olcum (10 / 5 karakter, sınır 15)

**Anahtar kelimeler (19)**

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
| `"işyeri gürültü ölçümü"` | Sıralı |
| `"işyeri toz ölçümü"` | Sıralı |
| `"isg ortam ölçümleri"` | Sıralı |
| `"ikitelli osb iş hijyeni"` | Sıralı |
| `"tuzla iş hijyeni ölçümü"` | Sıralı |
| `"tuzla voc ölçümü"` | Sıralı |

**Grup negatifleri (sıralı):** `"uygulaması"` (Telefon uygulaması), `"telefon"` (Telefon uygulaması), `"desibel ölçer"` (Cihaz satın alma), `"cihazı"` (Cihaz satın alma), `"lux metre"` (Cihaz satın alma)

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

## 8. Negatif anahtar kelimeler

Tümü **sıralı eşleme**. Ortak liste hesap düzeyinde paylaşılan liste ("Aymati ortak negatifler") olarak oluşturulup dört kampanyaya bağlanabilir; Ads Editor CSV'sinde kolaylık için her kampanyaya kampanya negatifi olarak da yazılmıştır (ikisini birden yapmayın).

### 8.1 Ortak negatifler (41)

| Negatif | Gerekçe |
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
| `"sertifika programı"` | Eğitim arayanlar |
| `"belgesi nasıl alınır"` | Yetki belgesi arayan |
| `"ders"` | Öğrenci |
| `"ders notları"` | Öğrenci |
| `"sınav"` | Öğrenci |
| `"sınav soruları"` | Öğrenci |
| `"ödev"` | Öğrenci |
| `"tez"` | Akademik |
| `"proje ödevi"` | Öğrenci |
| `"bitirme projesi"` | Öğrenci |
| `"pdf"` | Doküman arayanlar |
| `"pdf indir"` | Doküman arayanlar |
| `"nasıl yapılır pdf"` | Kendin-yap / doküman |
| `"ppt"` | Doküman arayanlar |
| `"sunum"` | Doküman arayanlar |
| `"indir"` | Doküman/yazılım arayanlar |
| `"program indir"` | Yazılım arayanlar |
| `"excel"` | Hesap şablonu arayanlar |
| `"dwg"` | Çizim dosyası arayanlar |
| `"autocad"` | Çizim/yazılım arayanlar |
| `"ücretsiz"` | Ücretsiz hizmet arayanlar |
| `"bedava"` | Ücretsiz hizmet arayanlar |
| `"yönetmelik pdf"` | Mevzuat metni arayanlar |
| `"ekşi"` | Bilgi/forum |
| `"yorumları"` | Bilgi/forum |
| `"wikipedia"` | Bilgi amaçlı |
| `"youtube"` | Video arayanlar |
| `"video"` | Video arayanlar |
| `"hobi"` | Alakasız |

Not: Önceki sürümdeki genel `"sertifika"` / `"sertifikası"` negatifleri ortak listeden çıkarıldı (kaldırma aparatı ve ATEX aramalarında anlamı farklı); yalnız ilgili kampanyalarda kullanılıyor.

### 8.2 "Nedir" ve bilgi amaçlı aramalar: kampanya bazında karar

| Kampanya | Karar |
| --- | --- |
| Statik Analiz | Negatif. Statik aramalarında "nedir / nasıl hesaplanır" çoğunlukla öğrenci ve mühendis; bu trafik blog yazılarına (organik) bırakılır. |
| PKD | Negatif DEĞİL (ilk 4 hafta). PKD'yi araştıran kişi çoğunlukla işyerinin İSG uzmanı veya işvereni, yani karar verici; "pkd nedir", "zorunlu mu" aramaları alıcıya yakın. Şablon/örnek/word aramaları negatif. 4. haftada dönüşümsüz "nedir" tıklamaları çoksa negatife alınır. |
| Projelendirme | Negatif. "Elektrik projesi nedir" gibi aramalarda konut sahibi ve öğrenci oranı yüksek. |
| Muayene ve İş Hijyeni | Negatif (ikincil kampanya, bütçe dar). |

### 8.3 Statik Analiz kampanya negatifleri (40)

| Negatif | Gerekçe |
| --- | --- |
| `"nedir"` | Bilgi amaçlı: statik aramalarında öğrenci/mühendis oranı yüksek (blog trafiğine bırakılır) |
| `"ne demek"` | Bilgi amaçlı |
| `"nasıl yapılır"` | Kendin-yap |
| `"nasıl hesaplanır"` | Kendin-yap |
| `"formül"` | Öğrenci/kendin-yap |
| `"formülleri"` | Öğrenci/kendin-yap |
| `"çözümlü"` | Öğrenci |
| `"soru"` | Öğrenci |
| `"sorular"` | Öğrenci |
| `"mukavemet"` | Öğrenci |
| `"statik analiz programı"` | Yazılım |
| `"programı"` | Yazılım |
| `"programları"` | Yazılım |
| `"sap2000"` | Yazılım |
| `"ansys"` | Yazılım |
| `"solidworks"` | Yazılım |
| `"etabs"` | Yazılım |
| `"idecad"` | Yazılım |
| `"sta4cad"` | Yazılım |
| `"probina"` | Yazılım |
| `"abaqus"` | Yazılım |
| `"robot structural"` | Yazılım |
| `"tekla"` | Yazılım |
| `"statik elektrik"` | Farklı konu |
| `"statik ip"` | Farklı konu |
| `"statik site"` | Farklı konu |
| `"bina"` | Bina statiği verilmiyor (inşaat mühendisliği) |
| `"binası"` | Bina statiği |
| `"binanın"` | Bina statiği |
| `"apartman"` | Bina statiği |
| `"konut"` | Bina statiği |
| `"ev"` | Bina statiği |
| `"villa"` | Bina statiği |
| `"betonarme"` | Bina statiği |
| `"riskli yapı"` | Deprem/kentsel dönüşüm |
| `"kentsel dönüşüm"` | Deprem/kentsel dönüşüm |
| `"deprem performans"` | Bina deprem analizi |
| `"karot"` | Bina deprem analizi |
| `"yapı denetim"` | Bina |
| `"inşaat mühendisi"` | SİM imzası arayan / iş arayan |

### 8.4 PKD kampanya negatifleri (25)

| Negatif | Gerekçe |
| --- | --- |
| `"böbrek"` | PKD = polikistik böbrek hastalığı |
| `"hastalık"` | Sağlık |
| `"hastalığı"` | Sağlık |
| `"kist"` | Sağlık |
| `"tedavi"` | Sağlık |
| `"belirtileri"` | Sağlık |
| `"örnek"` | Kendin-yap şablon |
| `"örneği"` | Kendin-yap şablon |
| `"şablon"` | Kendin-yap şablon |
| `"word"` | Kendin-yap şablon |
| `"motor"` | ATEX ürün alımı |
| `"fan"` | ATEX ürün alımı |
| `"armatür"` | ATEX ürün alımı |
| `"lamba"` | ATEX ürün alımı |
| `"aydınlatma"` | ATEX ürün alımı |
| `"telefon"` | ATEX ürün alımı |
| `"el feneri"` | ATEX ürün alımı |
| `"kamera"` | ATEX ürün alımı |
| `"buat"` | ATEX ürün alımı |
| `"rakor"` | ATEX ürün alımı |
| `"sertifikası"` | Ürün sertifikasyonu |
| `"sertifikalı"` | Ürün alımı |
| `"patlayıcı madde"` | Patlayıcı maddeler |
| `"havai fişek"` | Alakasız |
| `"maden"` | Madencilik |

### 8.5 Projelendirme kampanya negatifleri (18)

| Negatif | Gerekçe |
| --- | --- |
| `"nedir"` | Bilgi amaçlı (blog trafiğine bırakılır) |
| `"ne demek"` | Bilgi amaçlı |
| `"nasıl çizilir"` | Kendin-yap |
| `"nasıl yapılır"` | Kendin-yap |
| `"sembolleri"` | Öğrenci/çizimci |
| `"semboller"` | Öğrenci/çizimci |
| `"örnek"` | Şablon arayan |
| `"örneği"` | Şablon arayan |
| `"programı"` | Yazılım |
| `"ev"` | Konut (hedef: işletme) |
| `"daire"` | Konut |
| `"villa"` | Konut |
| `"apartman"` | Konut |
| `"montaj"` | Uygulama/montaj işi (verilmiyor) |
| `"montajı"` | Uygulama/montaj işi |
| `"kurulum"` | Uygulama/montaj işi |
| `"satış"` | Ürün alımı |
| `"bakım"` | Bakım hizmeti |

### 8.6 Muayene ve İş Hijyeni kampanya negatifleri (8)

| Negatif | Gerekçe |
| --- | --- |
| `"nedir"` | Bilgi amaçlı |
| `"ev"` | Konut |
| `"daire"` | Konut |
| `"apartman"` | Konut |
| `"villa"` | Konut |
| `"sertifika"` | Operatör/kişi belgesi |
| `"sertifikası"` | Operatör/kişi belgesi |
| `"projesi"` | Proje niyeti Projelendirme kampanyasına |

Betik kontrolü: hiçbir ortak, kampanya veya grup negatifi aynı kampanyadaki bir anahtar kelimeyi engellemiyor (tam kelime eşleşmesiyle denetlendi). Rakip firma adları anahtar kelime yapılmadı; arama terimleri raporunda görülürse negatife eklenmesi değerlendirilecek.

## 9. Google Ads Editor'e toplu yükleme

Dosyalar UTF-8 (BOM'suz), virgülle ayrılmış. Excel'de çift tıklayarak açarsanız Türkçe karakterler bozuk görünebilir; düzenlemek gerekirse Excel'de Veri > Metinden/CSV'den > "65001: Unicode (UTF-8)" ile açın.

1. Ads Editor > Hesap > İçe aktar > **Dosyadan** > `ads-editor-2026-11.csv`. Kampanyalar ve reklam grupları yoksa Ads Editor bunları oluşturmayı önerir. Kampanyaların **Duraklatıldı** durumunda olduğunu kontrol edin ve ayarları bölüm 3'e göre girin (ağlar, konum, planlama, bütçe, teklif).
   - `Match type` sütunu: `Exact` = tam, `Phrase` = sıralı, `Negative Phrase` = grup negatifi, `Campaign Negative Phrase` = kampanya negatifi (Ad group boş). Ads Editor sütunu otomatik eşleştirmezse "Match type" sütununu **"Criterion Type"** alanına eşleyin.
   - Ortak negatifler bu dosyada her kampanyaya kampanya negatifi olarak yazılmıştır. Paylaşılan negatif liste kullanmak isterseniz bu satırları silip listeyi Paylaşılan kitaplık'ta oluşturun.
2. Hesap > İçe aktar > Dosyadan > `ads-editor-reklamlar-2026-11.csv`. Her satır bir duyarlı arama reklamıdır (15 başlık, 4 açıklama, nihai URL, görünen yol). Ads Editor reklam türünü sormazsa "Responsive search ad" olarak kabul eder; sorarsa bu türü seçin.
3. Hesap düzeyi öğeleri (çağrı, açıklama metni) ile kampanya düzeyindeki site bağlantılarını ve snippet'leri bölüm 3'teki tablolardan elle girin.
4. "Değişiklikleri kontrol et" deyip hataları giderin, ardından "Yayınla" deyin. Kampanyalar duraklatılmış olarak gider; bölüm 1 tamamlanınca etkinleştirin.

## 10. İlk 4 hafta: haftalık kontrol listesi

**Hafta 1 (ilk 2–3 gün dahil)**

- [ ] Reklamlar "Uygun" durumda mı? Reddedilen reklam varsa nedenini not edin (ör. "telefon numarası metinde", "büyük harf kullanımı").
- [ ] Dönüşümler "Kayıt yapılıyor" durumunda mı? Teklif formunu, telefon ve WhatsApp bağlantısını kendiniz bir kez deneyip (ofis dışı bir cihazdan) dönüşümün 24 saat içinde göründüğünü kontrol edin; test dönüşümlerini not edin.
- [ ] **Arama terimleri** raporunu ilk 3 gün her gün açın. Alakasız terimleri (bina statiği, yazılım, iş ilanı, ürün alımı) hemen negatife ekleyin.
- [ ] Her kampanya bütçesini harcıyor mu? Hiç harcamayan kampanyada anahtar kelime durumlarını ("Düşük arama hacmi") kontrol edin.

**Hafta 2**

- [ ] Arama terimleri raporu: dönüşümsüz ve alakasız terimleri negatife alın; alakalı ve tıklama alan yeni terimleri not edin (ay sonunda anahtar kelime olur).
- [ ] Gösterim payı ve "bütçe nedeniyle kaybedilen gösterim payı": bir kampanya bütçe yüzünden kısılıyorsa ve dönüşüm getiriyorsa payını artırmayı değerlendirin (bölüm 2).
- [ ] Maksimum TBM sınırı: "sayfanın üstü" gösterim oranı çok düşükse sınırı kademeli artırın.
- [ ] WhatsApp'a gelen teklif mesajlarını Google Ads'teki form dönüşümüyle karşılaştırın.

**Hafta 3**

- [ ] Reklam öğesi raporu (başlık/açıklama performansı): "Düşük" etiketi alan başlıkları not edin; değişiklik bir sonraki aylık güncellemede yapılacak.
- [ ] Konum raporu: Kocaeli/Tekirdağ eklendiyse tıklama ve dönüşüm durumunu kontrol edin.
- [ ] Saat/gün raporu: 08:00–18:30 dışında talep gelmiyorsa planlama korunur.
- [ ] PKD kampanyası: "nedir / zorunlu mu" aramaları tıklama alıp dönüşüm getirmiyorsa `"nedir"` negatifini ekleyin.

**Hafta 4**

- [ ] Arama terimleri raporunu CSV olarak indirip `pazarlama/reklam/sonuclar-2026-11.csv` adıyla depoya ekleyin (bölüm 11).
- [ ] 4 hafta boyunca hiç gösterim almayan reklam grubunu duraklatın (silmeyin).
- [ ] Dönüşüm sayısı yaklaşık 15/30 günü geçen kampanyada "Dönüşümleri en üst düzeye çıkar" stratejisine geçin (bölüm 3.3).
- [ ] Kampanya bazında dönüşüm başına maliyeti karşılaştırın ve bütçe yüzdelerini gerekirse güncelleyin.

## 11. Arama terimleri raporu ile aylık güncelleme

Google Ads > Anahtar kelimeler > Arama terimleri raporunu (son 30 gün) CSV olarak indirip `pazarlama/reklam/sonuclar-YYYY-AA.csv` adıyla depoya ekleyin (ör. `sonuclar-2026-11.csv`). Sütunlar: arama terimi, kampanya, reklam grubu, gösterim, tıklama, maliyet, dönüşüm. Bir sonraki aylık güncellemede:

- Tıklama alıp dönüşüm getirmeyen ve alakasız terimler negatif listesine önerilir.
- Dönüşüm getiren terimler ilgili gruba yeni anahtar kelime olarak eklenir.
- Değişiklikler bu dosyanın en üstündeki "Bu ay değişenler" bölümüne yazılır, Ads Editor CSV'leri yeni ay adıyla yeniden üretilir.

## Reklam metni kuralları (kontrol listesi)

- Fiyat, tutar, para birimi, "en ucuz", "garanti", "%100", "hemen", "aynı gün" gibi doğrulanamayan iddialar yok (betikle denetlendi).
- Rakip marka adı yok.
- Telefon numarası reklam metnine yazılmadı (Google politikası); numara çağrı öğesinde.
- İmza ifadeleri: statik analizler ve mekanik projeler "MMO kayıtlı makina mühendisi", elektrik projeleri "EMO kayıtlı S.M.M. elektrik mühendisi". PKD, Faraday hesaplama aracı ve muayene/iş hijyeni gruplarında oda iddiası yok.
- Fuar standı: "fuar onayı", "onaylı rapor" gibi ifade yok. Bazı fuar şartnameleri çift katlı stand için inşaat mühendisi (SİM) onayı ister; imza şartı teklif aşamasında kontrol edilir (sayfadaki SSS ile aynı).
- Reklamdaki her iddia açılış sayfasında da yazıyor (sayfa metinleriyle karşılaştırıldı).
- Görünür metinde yıl yok.
