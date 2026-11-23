# Keşif kontrol listesi — Elektrik İç Tesisat Projesi / Rölöve

Site sayfası: `site/elektrik-ic-tesisat-projesi.html` (https://www.aymati.com.tr/elektrik-ic-tesisat-projesi)

Bu liste saha ekibinin elektrik iç tesisat projesi veya mevcut tesisat rölövesi için gereken veriyi tek keşifte toplaması içindir. Kısa devre, gerilim düşümü, kablo kesiti, topraklama ve koruma hesapları ile proje kararları mühendise aittir; bu listede hesap ya da sonuç alanı yoktur. Proje EMO kayıtlı S.M.M. elektrik mühendisi tarafından çizilir ve imzalanır.

Kişisel veri ve müşteri bilgisi bu dosyaya yazılmaz. Gerçek bir işte listeyi kopyalayıp ayrı (depo dışı) dosyada doldurun.

---

## 1. Keşif öncesi müşteriden istenecekler

- [ ] Yapının ilçesi, kullanım amacı (fabrika, depo, atölye, ofis, karma vb.) ve yapı tipi
- [ ] Toplam inşaat alanı (m²) ve kat sayısı
- [ ] İşin türü: yeni proje, mevcut tesisat rölövesi, tadilat / ilave, kapasite artışı
- [ ] Talebin nedeni: dağıtım şirketi başvurusu, iskân / ruhsat, denetim, sigorta, kiracı değişikliği, yeni makine
- [ ] Mimari plan (tercihen DWG; yoksa PDF veya ölçekli kroki), kesit ve vaziyet planı
- [ ] Varsa mevcut elektrik projesi (onaylı ise onay bilgisi), tek hat şeması, kolon şeması
- [ ] Enerji giriş şekli: AG abone (kofra / sayaç) mi, kendi trafosu (OG) mu
- [ ] Bağlantı gücü / sözleşme gücü (fatura veya bağlantı anlaşmasından)
- [ ] Trafo varsa gücü ve trafo etiket bilgisi
- [ ] Makine ve ekipman listesi (güç, gerilim, faz); planlanan yeni yükler
- [ ] Jeneratör, UPS, kompanzasyon panosu var mı
- [ ] Zayıf akım ihtiyacı: data, telefon, kamera, anons, diafon, yangın algılama (yangın algılama ayrı proje olarak da istenebilir)
- [ ] Varsa topraklama ölçüm raporu ve paratoner / Faraday kafesi bilgisi
- [ ] Panolara ve elektrik odasına erişim için yetkili / bakım sorumlusunun keşifte bulunması

## 2. Sahada ölçülecekler, kaydedilecekler

### Enerji girişi
- [ ] Enerji giriş noktası, kofra / sayaç panosu yeri
- [ ] Sayaç tipi ve sayaç etiket bilgileri (güç ve akım değerleri)
- [ ] Ana şalter tipi ve anma akımı (etiketten)
- [ ] Trafo varsa: gücü, OG hücreleri, trafo ile ana pano arası mesafe ve kablo
- [ ] Jeneratör / UPS / ATS: gücü, yeri, beslediği panolar

### Pano listesi
Her pano için ayrı satır açın:

| Pano adı / no | Yeri (mahal, kat) | Besleyen pano | Giriş şalteri (tip, anma akımı) | Besleme kablosu (tip, kesit, yaklaşık uzunluk) | Çıkış sayısı | Kaçak akım rölesi var mı | Notlar |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

- [ ] Her panonun çıkışları: linye adı, koruma elemanı (tip, anma akımı), kablo kesiti, beslediği yük
- [ ] Pano içi etiketleme var mı
- [ ] Panolar arası kablo güzergâhı (tava, kanal, şaft) ve yaklaşık uzunluklar

### Yükler
- [ ] Makine / motor listesi: güç, faz, etiket bilgisi (etiket fotoğrafı)
- [ ] Aydınlatma: mahal bazında armatür tipi ve sayısı
- [ ] Priz ve kuvvet prizleri: mahal bazında sayısı
- [ ] Klima, ısıtma, kompresör, asansör, pompa gibi büyük yükler
- [ ] Acil aydınlatma ve yönlendirme armatürleri var mı, yerleri

### Mahaller ve mimari
- [ ] Mimari planı sahayla karşılaştırma: duvar, bölme, kapı farkları
- [ ] Plan yoksa mahal ölçüleri ve kat yüksekliği (rölöve krokisi)
- [ ] Elektrik odası, şaft ve kablo geçiş yerleri
- [ ] Özel mahaller: ıslak hacim, depo, tozlu / nemli alan, yanıcı madde bulunan alan (varsa PKD ile ilişki notu)

### Topraklama ve koruma
- [ ] Topraklama tesisatının görünen kısımları: topraklama barası, ana eş potansiyel bara, iletkenler
- [ ] Şebeke tipi hakkında bilgi (TN / TT; müşteriden veya mevcut projeden; sahada kesin karar mühendisindir)
- [ ] Parafudr (aşırı gerilim koruma) var mı, hangi panoda
- [ ] Paratoner / Faraday kafesi var mı; iniş iletkenleri ve test klemensleri görülüyor mu

### Zayıf akım
- [ ] Data kabineti yeri, data prizleri
- [ ] Kamera, kayıt cihazı, alarm paneli yerleri
- [ ] Anons / seslendirme, diafon
- [ ] Yangın algılama paneli ve dedektörler (varsa)

## 3. Fotoğraflanacaklar

- [ ] Enerji girişi, kofra ve sayaç panosu
- [ ] Trafo etiketi, jeneratör / UPS etiketi (varsa)
- [ ] Her pano: kapalı görünüş, kapak açık iç görünüş (yetkili açar), giriş şalteri etiketi
- [ ] Makine etiketleri
- [ ] Kablo tavaları ve şaftlar
- [ ] Topraklama barası, eş potansiyel bara
- [ ] Parafudr ve kaçak akım röleleri
- [ ] Acil aydınlatma armatürleri
- [ ] Zayıf akım kabinet ve panelleri

Pano kapağı yalnızca yetkili kişi tarafından açılır; gerilim altındaki tesisatta ölçüm ve müdahale bu listenin kapsamında değildir. Fotoğraf adlarını pano numarasıyla eşleştirin (ör. `P02-ic-gorunus.jpg`).

## 4. Sık görülen eksiklikler

- Mimari plan yok ya da güncel değil; rölöve krokisi sahada çıkarılmak zorunda
- Mevcut tek hat şeması yok veya panolardaki gerçek durumu yansıtmıyor
- Pano ve linye etiketlemesi yok; hangi çıkışın neyi beslediği bilinmiyor
- Bağlantı gücü / sözleşme gücü belgesi elde değil
- Makine listesi eksik; büyük yükler (kompresör, fırın, kaynak makinesi) bildirilmemiş
- Sonradan eklenen panolar projede yok
- Kaçak akım rölesi bazı hatlarda yok
- Topraklama ölçüm raporu yok veya eski
- Zayıf akım ve yangın algılama kapsamı teklif aşamasında netleştirilmemiş
- Acil aydınlatma ve yönlendirme eksik

## 5. Müşteriden istenecek belgeler (özet)

- Mimari plan (DWG tercih), kesit, vaziyet planı
- Varsa mevcut elektrik projesi, tek hat ve kolon şeması
- Bağlantı / sözleşme gücü bilgisi (fatura veya bağlantı anlaşması)
- Makine ve ekipman listesi (güç, faz)
- Varsa trafo, jeneratör, UPS bilgileri
- Varsa topraklama ölçüm raporu

## 6. Satış ekibine not (teklif için kritik 3 bilgi)

1. **Yapı ve alan:** ilçe, toplam alan (m²), kat sayısı ve yapı tipi / kullanım amacı (site sayfasındaki teklif bilgisiyle aynı).
2. **İşin türü:** yeni proje mi, mevcut tesisat rölövesi mi, tadilat / ilave mi; mimari plan ve mevcut proje var mı.
3. **Güç ve kapsam:** enerji giriş şekli (AG abone / kendi trafosu), yaklaşık kurulu güç ve zayıf akım / yangın algılama projesinin kapsama girip girmediği.

## 7. Keşif kaydı

| Alan | Değer |
| --- | --- |
| Keşif tarihi | |
| Keşfi yapan | |
| Pano sayısı | |
| Fotoğraf sayısı / klasör | |
| Eksik kalan bilgi | |

Mühendis kontrolü ve imza:

Ad Soyad: ______________________
EMO sicil no / S.M.M. belge no: ______________________
İmza: ______________________
Tarih: ______________________

---

### Kaynak ve dayanak notu

- Yönetmelik ve standart adları site sayfasıyla aynıdır: Elektrik İç Tesisleri Yönetmeliği, Elektrik Kuvvetli Akım Tesisleri Yönetmeliği, Elektrik Tesislerinde Topraklamalar Yönetmeliği, TS HD 60364 serisi, TS EN 60909-0, TS EN 12464-1, TS EN 62305, TS EN 50522. Bu listede yönetmeliklerden sınır değer veya madde numarası aktarılmamıştır.
- Yönetmeliklerin Resmî Gazete tarih–sayı bilgisi ve güncel metinleri mevzuat.gov.tr'den kontrol edilip buraya eklenecek: `[DOĞRULANACAK]`.
- Gerilim düşümü sınırları ve topraklama hedef değerleri keşif konusu değildir; proje aşamasında mühendis güncel yönetmelik metninden uygular. Site sayfasındaki gerilim düşümü yüzdeleri için kaynak teyidi: `[DOĞRULANACAK]`.
- Projenin onay süreci (dağıtım şirketi / belediye) ve istenen ek belgeler bölgeye göre değişebilir: `[DOĞRULANACAK]`.
