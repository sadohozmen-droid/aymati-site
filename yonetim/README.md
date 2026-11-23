# Aymati Proje — ajan ekibi

Site sahibinin kararı (23 Kasım): Aymati'nin günlük işleri, bir Genel Müdür (CEO) ajanının yönettiği bir ajan ekibine devredildi. Bu dosya ekibin yapısını, kimin neye yetkili olduğunu ve neyin her zaman site sahibinde kaldığını anlatır.

## Strateji (değişmez çerçeve)

- **Hedef:** Google aramasından (yerel SEO, blog, Google Ads) İstanbul'daki fabrika, depo, atölye ve OSB işletmelerinden teklif talebi toplamak; gelen talebi hızlı ve düzgün bir teklife çevirmek.
- **Öncelikli hizmet kümeleri:** Statik Analiz (raf, iskele, fuar standı, sahne/truss, vinç temeli, kaldırma aparatı, monoray/vinç yolu, tabela/pilon), Patlamadan Korunma Dokümanı (PKD/ATEX), Projelendirme (elektrik, yangın, mekanik), Faraday Kafesi / paratoner.
- **Kardeş site:** Periyodik muayene ve iş hijyeni sorguları teknikisg.com'un alanıdır. Aymati bu kümelerde yeni sayfa açmaz, mevcut sayfaları korur; iki site aynı sorgu için yarışmaz.

## Örgüt şeması

```
Site sahibi (yönetim kurulu: para, imza, hesaplar, paylaşım)
└── Genel Müdür ajanı  ·  /genel-mudur  ·  haftalık (pazartesi) + aylık hedef
    ├── Pazarlama Müdürü  ·  /haftalik-pazarlama
    │   ├── icerik-yazari          blog ve gündem yazıları
    │   ├── seo-denetcisi          aylık teknik/içerik SEO
    │   ├── reklam-uzmani          Google Ads yapısı ve metinleri
    │   └── bolge-sayfasi-yazari   ilçe/OSB sayfaları
    ├── Sosyal Medya Yöneticisi  ·  sosyal-medya-yoneticisi  (aylık plan)
    │   └── sosyal-medya-editoru   haftalık gönderi metinleri
    ├── Satış Temsilcisi  ·  satis-temsilcisi
    │   talep karşılama, teklif yazısı taslağı, takip mesajları
    └── Teknik Operasyon  ·  teknik-operasyon
        keşif hazırlığı, rapor şablonları, mevzuat ve standart takibi
```

Zaten çalışan zamanlanmış görevler (Genel Müdür bunları yeniden yapmaz, raporlarını okur):

| Görev | Sıklık | Çıktı |
| --- | --- | --- |
| Aymati Günlük SEO Raporu | Her gün | `pazarlama/raporlar/gunluk/` |
| Aymati Gündem ve Blog Ajanı | Salı, perşembe | Blog yazısı PR'ı |
| Portföy Haftalık Özet (4 site) | Pazar | Mesaj |
| **Aymati Genel Müdür** (yeni) | Pazartesi | `yonetim/raporlar/` + mesaj |

## Yetki matrisi

| İş | Kim karar verir |
| --- | --- |
| Site içeriği, sayfa, tasarım, site yapısı, SEO düzeltmeleri | **Genel Müdür** (tam yetki; site sahibine sonradan özetlenir) |
| Blog, sosyal medya metni, reklam metni hazırlama | İlgili ajan, Genel Müdür denetler |
| Teklif yazısı ve müşteri mesajı **taslağı** | Satış Temsilcisi hazırlar, **gönderen site sahibidir** |
| Fiyat, indirim, ödeme koşulu | **Site sahibi** |
| Proje/rapor imzası | **EMO kayıtlı S.M.M. elektrik mühendisi** (elektrik), **MMO kayıtlı makina mühendisi** (mekanik ve statik) |
| Keşif, ölçüm, saha işi | **Mühendis / saha ekibi** (insan) |
| Hesap açma, şifre, ödeme, reklam bütçesi, sosyal medyada paylaşım, e-posta/WhatsApp gönderme | **Site sahibi** |

## Kişisel veri (KVKK)

Bu depo site koduyla birlikte durur. Müşteri adı, firma adı, telefon, e-posta, adres ve teklif tutarı **depoya yazılmaz**: ne rapora, ne şablona, ne commit mesajına. Satış ajanı gerçek bir talep üzerinde çalışırken çıktısını yalnızca sohbette verir. Depoda yalnızca kişisel veri içermeyen şablonlar ve sayısal özetler (ör. "bu hafta 3 talep, 2'si statik analiz") durur.

## Site sahibinden beklenen girdiler

Genel Müdür her raporda bunların durumunu sorar; gelmeyen bilgiyi uydurmaz.

1. Haftalık talep özeti: kaç talep geldi, hangi hizmet, hangi kanal (telefon / WhatsApp / e-posta / form), kaçı teklife, kaçı işe döndü. Kişi bilgisi olmadan, tek satır yeter.
2. Teklif formu için form servisi (`site/teklif.html` içindeki `FORM_ENDPOINT` boş; form şu an ziyaretçinin e-posta programını açıyor).
3. Hakkımızda: mühendis adları, EMO/MMO sicil numaraları, saha fotoğrafları, izinli referanslar.
4. Satış şablonları için fiyatlandırma ilkeleri (site dışı, yalnızca sizin teklifleriniz için) ve standart ödeme/teslim koşulları.
5. İsterseniz Gmail bağlantısı: bağlanırsa Satış Temsilcisi gelen talepleri okuyup cevap taslağı hazırlayabilir (yine göndermez).

## Klasörler

- `yonetim/` — Genel Müdür raporları ve aylık hedefler
- `pazarlama/` — pazarlama ve sosyal medya çıktıları
- `satis/sablonlar/` — teklif yazısı, takip ve cevap şablonları (kişisel veri yok)
- `operasyon/` — keşif kontrol listeleri, rapor şablonları, mevzuat takibi

Bu klasörler `site/` dışında olduğu için yayına girmez.
