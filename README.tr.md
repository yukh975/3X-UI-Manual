# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 Türkçe · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 [繁體中文](README.zh-TW.md)

Panel [3x-ui](https://github.com/MHSanaei/3x-ui) için kullanım kılavuzu — panel **v3.4.2** için yazılmış kapsamlı bir kullanıcı rehberi.

> **Salt okunur yansıma.** Bu GitHub deposu tek yönlü bir yansımadır — kılavuzun kaynağı özel bir GitLab'da bulunur ve buraya otomatik olarak aktarılır; bu nedenle her zaman günceldir. Bir hata veya yanlışlık mı buldunuz? Lütfen [bir Sorun bildirin](https://github.com/yukh975/3X-UI-Manual/issues). **Pull request kabul edilmez** (otomatik olarak kapatılır) — düzeltmeler kaynakta yapılır.

## İçindekiler

| Dosya | Dil | Biçim |
| --- | --- | --- |
| **[3X-UI-MANUAL.ar.md](3X-UI-MANUAL.ar.md)** · [PDF](pdf/3X-UI-MANUAL.ar.pdf) | 🇸🇦 العربية | Markdown + PDF |
| **[3X-UI-MANUAL.en.md](3X-UI-MANUAL.en.md)** · [PDF](pdf/3X-UI-MANUAL.en.pdf) | 🇬🇧 English | Markdown + PDF |
| **[3X-UI-MANUAL.es.md](3X-UI-MANUAL.es.md)** · [PDF](pdf/3X-UI-MANUAL.es.pdf) | 🇪🇸 Español | Markdown + PDF |
| **[3X-UI-MANUAL.fa.md](3X-UI-MANUAL.fa.md)** · [PDF](pdf/3X-UI-MANUAL.fa.pdf) | 🇮🇷 فارسی | Markdown + PDF |
| **[3X-UI-MANUAL.id.md](3X-UI-MANUAL.id.md)** · [PDF](pdf/3X-UI-MANUAL.id.pdf) | 🇮🇩 Bahasa Indonesia | Markdown + PDF |
| **[3X-UI-MANUAL.ja.md](3X-UI-MANUAL.ja.md)** · [PDF](pdf/3X-UI-MANUAL.ja.pdf) | 🇯🇵 日本語 | Markdown + PDF |
| **[3X-UI-MANUAL.pt.md](3X-UI-MANUAL.pt.md)** · [PDF](pdf/3X-UI-MANUAL.pt.pdf) | 🇧🇷 Português | Markdown + PDF |
| **[3X-UI-MANUAL.ru.md](3X-UI-MANUAL.ru.md)** · [PDF](pdf/3X-UI-MANUAL.ru.pdf) | 🇷🇺 Русский | Markdown + PDF |
| **[3X-UI-MANUAL.tr.md](3X-UI-MANUAL.tr.md)** · [PDF](pdf/3X-UI-MANUAL.tr.pdf) | 🇹🇷 Türkçe | Markdown + PDF |
| **[3X-UI-MANUAL.uk.md](3X-UI-MANUAL.uk.md)** · [PDF](pdf/3X-UI-MANUAL.uk.pdf) | 🇺🇦 Українська | Markdown + PDF |
| **[3X-UI-MANUAL.vi.md](3X-UI-MANUAL.vi.md)** · [PDF](pdf/3X-UI-MANUAL.vi.pdf) | 🇻🇳 Tiếng Việt | Markdown + PDF |
| **[3X-UI-MANUAL.zh-CN.md](3X-UI-MANUAL.zh-CN.md)** · [PDF](pdf/3X-UI-MANUAL.zh-CN.pdf) | 🇨🇳 简体中文 | Markdown + PDF |
| **[3X-UI-MANUAL.zh-TW.md](3X-UI-MANUAL.zh-TW.md)** · [PDF](pdf/3X-UI-MANUAL.zh-TW.pdf) | 🇹🇼 繁體中文 | Markdown + PDF |

## 3.4.2'deki Yenilikler

3.4.2 sürümü büyük bir güncellemedir: WireGuard çok istemcili modele geçirildi, REALITY'ye canlı bir hedef tarayıcısı eklendi, yük dengeleyiciler Observatory / Burst Observatory sekmelerine kavuştu ve hassas ayarların 2FA koduyla onaylanması eklendi. Aşağıda, 3.4.1'e göre değişiklikler kılavuz bölümlerine göre gruplandırılmıştır.

### Bölüm 1 değişiklikleri — Giriş, Gereksinimler ve Kurulum

- Kenar çubuğu menüsünde (ve mobil çekmecede) artık **«Belgeler»** düğmesi (kitap simgesi) bulunuyor — `https://docs.sanaei.dev/` adresindeki resmi belgeleri açar.
- Panelin güncellediği minimum Xray sürümü **26.6.27**'ye yükseltildi (pakette Xray çekirdeği 26.6.27 gelir).

### Bölüm 2 değişiklikleri — Panele Giriş ve Erişim Güvenliği

- 2FA etkinken yönetici kullanıcı adı/parolasını değiştirmek ve 2FA'yı devre dışı bırakmak artık kimlik doğrulayıcı uygulamadaki **mevcut kodun girilmesini** gerektiriyor (hassas değişikliklerin onayı).
- LDAP: yeni **«TLS sertifikası doğrulamasını atla»** (`ldapInsecureSkipVerify`) geçişi — LDAPS'te sertifika doğrulamasını kapatır; yalnızca «TLS Kullan (LDAPS)» etkinken kullanılabilir.

### Bölüm 3 değişiklikleri — Genel Bakış / Gösterge Paneli

- Panel sürüm düğmesi artık her zaman güncelleme penceresini açıyor (bkz. bölüm 16 — dev kanalı).
- Genel bir **erişilebilirlik** iyileştirmesi: simgeler için aria etiketleri ve öğelerin Enter/Space ile etkinleştirilmesi (ekran okuyucular ve klavye gezintisi için).

### Bölüm 4 değişiklikleri — Inbounds: oluşturma ve genel parametreler

- **«Tüm bağlantıları dışa aktar»** eylemi artık bağlantıları abonelik motoru aracılığıyla oluşturuyor — her istemciye açıklama şablonunu uygular ve yönetilen Host uç noktalarını tercih eder (önceden sabit `inbound-email` açıklaması vardı).

### Bölüm 5 değişiklikleri — Protokoller

- **WireGuard çok istemcili modele geçirildi.** Peer'lar artık sıradan istemcilerdir (tünelde otomatik adres atama, abonelik desteği, trafik/süre limitleri ve gruplarla); inbound formundaki satır içi «Peer'lar» listesi kaldırıldı.
- WireGuard inbound'a yapılandırılabilir bir **DNS** alanı (varsayılan `1.1.1.1, 1.0.0.1`) ve bir **istemci yapılandırma kartı** eklendi — tam `.conf` ve `wireguard://`/`wg://` bağlantısı için kopyala/indir/QR.

### Bölüm 6 değişiklikleri — Aktarım (Stream Settings)

- XHTTP'de yeni inbound'lar için **xmux** içindeki `maxConnections` parametresi artık varsayılan olarak **6**'dır (önceden `0` — sınırsız). Mevcut inbound'lar kendi değerlerini korur.

### Bölüm 7 değişiklikleri — Bağlantı Güvenliği: TLS, XTLS ve REALITY

- **Canlı REALITY hedef tarayıcısı** eklendi: **«Tara»** (mevcut hedefi «canlı» kontrol et) ve **«Hedef bul»** (bir alan adını veya **IP/CIDR** aralığını tarayıp sertifikalarına göre uygun hedefleri seç) düğmeleri. REALITY ilk seçildiğinde «Hedef» ve SNI alanları artık boştur.

### Bölüm 8 değişiklikleri — İstemciler

- Süreyi/kotayı `bulkAdjust` ile uzatmak artık **yalnızca tükenme nedeniyle** (süresi dolmuş veya kotası aşılmış) devre dışı bırakılan istemciyi, uzatma onu limitlere geri döndürürse **otomatik olarak etkinleştiriyor**. Elle devre dışı bırakılanlar veya hâlâ tükenmiş olanlar kapalı kalır.

### Bölüm 9 değişiklikleri — İstemci Grupları

- Bir grupta **«Trafiği Sıfırla»** artık **yalnızca grubun kendi sayacını** sıfırlıyor; tek tek istemcilerin sayaçları, kotaları ve durumu etkilenmez, Xray'i yeniden başlatma gerekmez. Bu, önceki davranışa göre bir değişikliktir (önceden grubun tüm istemcilerinin trafiği sıfırlanıyordu).

### Bölüm 10 değişiklikleri — Abonelikler (Subscription)

- **Yönetilen hostlarda** **VLESS route** alanı yeniden tanımlandı: artık tek bir `0-65535` değeridir (port listesi değil) ve gerçekten her aboneliğin UUID'sine «gömülür» (raw/JSON/Clash).
- Açıklama şablonundaki `{{EMAIL}}` değişkeni (ve eş anlamlısı `{{USERNAME}}`) artık yalnızca istemcinin **ilk bağlantısında** gösteriliyor — tıpkı trafik/süre bloğu gibi.

### Bölüm 11 değişiklikleri — Xray: Yönlendirme, outbounds, DNS ve Uzantılar

- **Yük dengeleyiciler**: sayfa **«Yük dengeleyici ayarları»** ve **«Observatory»** sekmelerine ayrıldı; ham JSON yerine Observatory ve Burst Observatory formları geldi (Burst'e bir **«HTTP yöntemi»** alanı eklendi). `fallbackTag` içeren Random/Round-robin yük dengeleyici artık otomatik olarak bir Burst Observatory oluşturuyor.
- Bir outbound veya yük dengeleyici silinirken panel, yönlendirmedeki ilgili referansları kendisi temizliyor ve onay diyaloğunda bir **sonuç önizlemesi** gösteriyor.
- Yönlendirme kurallarında **L4** ağ ölçütü yapılandırmaya küçük harfle (`tcp`/`udp`) yazılırken tabloda büyük harfle gösteriliyor.
- Yük dengeleyici ekleme/düzenleme formundaki hatalar artık ilk alan dokunuşuna veya kaydetme girişimine kadar ertelenir.

### Bölüm 12 değişiklikleri — Düğümler (Çok Panelli, master/slave)

- «yerel olarak kaydedildi, düğüm çevrimdışı — sonra senkronize edilecek» bildirimi artık yalnızca düğüm gerçekten çevrimdışı veya kapalıyken gösteriliyor (önceden — çevrimiçi bir düğüme her kaydetmede).

### Bölüm 16 değişiklikleri — İşletim: Yedeklemeler, Günlükler, Güncelleme, CLI

- Yedek dosyası adları artık sunucu adresini ve **tarih-saati** içeriyor: `{host}_YYYY-AA-GG_SSDDSS.db` (PostgreSQL için `.dump`), örneğin `panel.example.com_2026-06-27_000000.db` — hem panelden indirirken hem de Telegram botunun gönderdiği yedeklerde.
- Kararlı bir derlemeden güncellemelerde **dev kanalı** etkinleştirilebilir: sürüm düğmesi her zaman güncelleme penceresini açar, kararsızlık ve otomatik geri alma olmadığı uyarısıyla birlikte bir **«Dev kanalı»** geçişi eklendi.

---

Panel kaynak dosyalarının analizinden oluşturulmuştur. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._
