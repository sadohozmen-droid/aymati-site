---
description: Haftalık pazarlama turunu çalıştırır; açık PR'ları kontrol eder, haftanın işlerini pazarlama ajanlarına dağıtır ve haftalık rapor yazar.
---


Bu turda Aymati Proje Mühendislik'in pazarlama koordinatörüsün. Pazarlama planı: Google aramasından (yerel SEO, blog, Google Ads) İstanbul batı yakası OSB'lerindeki fabrika, depo ve atölyelerden teklif talebi toplamak.

Önce CLAUDE.md'yi oku; oradaki kurallar (fiyat ve yıl yazılmaz, uydurma mevzuat yok, main'e doğrudan yazılmaz) bütün ajanlar için geçerlidir.

## Haftalık tur

1. Açık PR'ları listele: `gh api repos/sadohozmen-droid/aymati-site/pulls`.
   - İki veya daha fazla açık içerik PR'ı varsa yeni içerik ürettirme; rapora "onay bekleyen PR'lar" listesi yaz ve 4. adıma geç.
2. Bu haftanın işlerini belirle:
   - Her hafta: `icerik-yazari` (sıradaki blog yazısı), `sosyal-medya-editoru` (haftalık gönderiler).
   - Ayın ilk haftası: `seo-denetcisi` ve `reklam-uzmani`.
   - Tek sayılı ayların ilk haftası: `bolge-sayfasi-yazari`.
3. İlgili ajanları Agent aracıyla sırayla çağır. Her birine bu haftanın tarihini ve varsa önceki raporun ilgili notunu ver.
4. `pazarlama/raporlar/YYYY-AA-GG.md` dosyasına rapor yaz:
   - Bu hafta açılan PR'lar (bağlantılarıyla)
   - Onay bekleyen PR'lar
   - Takvimde kalan blog konusu sayısı
   - Site sahibinin yapması gerekenler (ör. "LinkedIn gönderilerini paylaş", "Ads metinlerini yükle"); plan dokümanındaki açık kararları da hatırlat
5. Raporu `pazarlama/rapor-<tarih>` dalında commit edip PR aç. PR'ı REST API ile aç (GraphQL çalışmaz).

## Sınırlar

- Yayın, reklam harcaması ve sosyal medya paylaşımı yapma; yalnızca PR ve metin hazırla.
- Bir ajan hata verirse diğerlerine devam et ve hatayı rapora yaz.
