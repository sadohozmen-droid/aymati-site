# Pazarlama ajanları

Plan: Google aramasından (yerel SEO, blog, Google Ads) İstanbul batı yakası OSB'lerindeki fabrika, depo ve atölyelerden teklif talebi toplamak.

## Nasıl çalıştırılır

Depoda Claude Code'u açıp `/haftalik-pazarlama` yazın (veya haftalık zamanlanmış görevle aynı komutu çalıştırın).
Komut haftanın işlerini aşağıdaki ajanlara dağıtır; her çıktı ayrı bir PR olarak gelir, siz onaylamadan yayına girmez.

| Ajan / komut | Görevi | Çıktı | Sıklık |
| --- | --- | --- | --- |
| `/haftalik-pazarlama` | Koordinasyon, haftalık rapor | `pazarlama/raporlar/` | Haftalık |
| `icerik-yazari` | Takvimden blog yazısı | `site/blog-*.html` | Haftalık |
| `seo-denetcisi` | Teknik / içerik SEO denetimi | `pazarlama/seo/` + düzeltme PR'ı | Aylık |
| `bolge-sayfasi-yazari` | Yeni bölge sayfası | `site/bolge-*.html` | 2 ayda 1 |
| `sosyal-medya-editoru` | LinkedIn + Google İşletme metinleri | `pazarlama/sosyal/` | Haftalık |
| `reklam-uzmani` | Google Ads yapısı ve metinleri | `pazarlama/reklam/kampanya.md` | Aylık |

Ajanlar paylaşım yapmaz ve reklam harcamaz; sosyal medya ve reklam çıktıları kopyalanmaya hazır metindir.
`pazarlama/` klasörü `site/` dışında olduğu için yayına girmez.
