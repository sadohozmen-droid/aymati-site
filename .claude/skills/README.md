# Dış kaynaklı skill'ler

Bu klasördeki skill'ler, GitHub'daki iki açık kaynak koleksiyondan seçilip olduğu gibi kopyalandı. Ajanlar bunları **yöntem rehberi** olarak okur. Önce `CLAUDE.md`, `yonetim/README.md` ve `.claude/product-marketing.md` kuralları gelir; skill ile kural çelişirse kural kazanır. Örnekler İngilizce ve çoğu SaaS içindir; çıktılar her zaman Türkçe ve Aymati'ye uyarlanmış olmalıdır.

| Kaynak | Lisans | Sürüm | Alınan skill'ler |
| --- | --- | --- | --- |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT (`_lisanslar/marketingskills-MIT.txt`) | `8fd2fca` | seo-audit, ai-seo, schema, site-architecture, programmatic-seo, content-strategy, copywriting, copy-editing, cro, ads, competitors, sales-enablement |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Apache 2.0 (`_lisanslar/knowledge-work-plugins-Apache-2.0.txt`) | `2baf6d1` | sales: handle-objection, call-prep, win-loss-review · small-business: speed-to-lead, proposal-builder, review-reputation (ortak dosyalar `.claude/shared/`) |

`evals/` klasörleri çıkarıldı; başka değişiklik yapılmadı. Eklenmeden önce tarandı: zararlı komut, gizli karakter veya gömülü talimat bulunmadı. Bazı SEO başvuru dosyaları `npx`/`curl` ile yapılabilecek kontrollerden söz eder; ajanlar bunları yalnızca site sahibine öneri olarak yazar, kendileri araç kurmaz.

## Hangi ajan neyi kullanır

| Ajan | Skill'ler |
| --- | --- |
| seo-denetcisi | seo-audit, schema, ai-seo, site-architecture |
| icerik-yazari | content-strategy, copywriting, copy-editing, ai-seo |
| bolge-sayfasi-yazari | programmatic-seo, copywriting |
| reklam-uzmani | ads, copywriting |
| sosyal-medya-yoneticisi / editörü | content-strategy, copywriting |
| satis-temsilcisi | speed-to-lead, proposal-builder, handle-objection, call-prep, sales-enablement, win-loss-review, cro |
| Genel Müdür | competitors, review-reputation, cro (aylık) |

## Güncelleme

Yeni sürüm almak için kaynak depoyu indirip aynı klasörleri yeniden kopyalayın, değişiklikleri okuyun (yeni talimat, komut veya bağlantı var mı) ve tablodaki sürümü güncelleyin. Tanımadığınız bir depodan skill eklemeden önce içeriğini okuyun.
