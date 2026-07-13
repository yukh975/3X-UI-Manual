# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 Türkçe · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 [繁體中文](README.zh-TW.md)

Panel [3x-ui](https://github.com/MHSanaei/3x-ui) için kullanım kılavuzu — panel **v3.5.0** için yazılmış kapsamlı bir kullanıcı rehberi.

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

## 3.5.0'daki Yenilikler

3.5.0 sürümü büyük bir sürümdür: MTProto çok istemcili modele geçirildi (mtg-multi motoru, kişisel gizli anahtarlar, kotalar ve ad-tag), yönetilen hostlar grup haline geldi (tek kayıtta birden fazla inbound ve adres), PostgreSQL panelindeki geri yükleme artık SQLite yedeklerini kabul ediyor, outbound'lara «Target Strategy», «Real delay» testi ve Egress/Country sütunları eklendi, yük dengeleyici başka bir yük dengeleyiciyi fallback (yedek) olarak kullanabiliyor. Pakette Xray çekirdeği 26.7.11 gelir. Aşağıda, 3.4.2'ye göre değişiklikler kılavuz bölümlerine göre verilmiştir.

### Bölüm 1 değişiklikleri — Giriş, Gereksinimler ve Kurulum

- Xray çekirdeği **26.7.11**'e güncellendi. Beraberinde gelen otomatik geçişler: Shadowsocks `none`/`plain` ve VMess `none`/`zero` şifreleri çekirdekten kaldırıldı (kayıtlı yapılandırmalar otomatik olarak yeniden yazılır), genel bir adrese giden şifrelenmemiş VLESS/Trojan outbound kaydetme sırasında reddedilir.
- Yeni **`x-ui pgclient [sürüm]`** komutu ve PostgreSQL menüsünde **10. Install/Upgrade client tools (pg_dump/pg_restore)** öğesi — PostgreSQL istemci araçlarının kurulumu/güncellenmesi.
- Betik düzeltmeleri: RHEL ailesinde PostgreSQL ve fail2ban kurulumu (EPEL), Arch'ta tam `pacman -Syu` çalıştırılmıyor, 32 bit ARM'de doğru Xray ikili dosya adı (`xray-linux-arm32`), IP sertifikası verilmeden önce otomatik algılanan IPv4'ün onaylanması, varsayılan ACME portu seçimindeki yanlış «Your input is invalid» düzeltildi.

### Bölüm 2 değişiklikleri — Panele Giriş ve Erişim Güvenliği

- IP limiti: «ölü» bağlantı artık her 10 saniyelik taramada değil, **bir kez** banlanıyor — fail2ban sayaçları artık şişmiyor, `maxretry` değerini yükseltmeye gerek yok.

### Bölüm 4 değişiklikleri — Inbounds: oluşturma ve genel parametreler

- inbound listesine **arama** eklendi (açıklamaya, porta ve protokole göre); düğüm açılır listeleri («Şuraya Dağıt», «Düğümler» filtresi) aranabilir hale geldi.

### Bölüm 5 değişiklikleri — Protokoller

- **MTProto çok istemcili modele geçirildi** (mtg-multi motoru): MTProto kullanıcıları artık kendi gizli anahtarı, kotası, süresi, ad-tag'i ve kişisel `tg://proxy` bağlantısı olan sıradan istemcilerdir. inbound düzeyindeki «Secret» alanı kaldırıldı (mevcut inbound'lar otomatik dönüştürülür), «FakeTLS domain» yeni gizli anahtarlar için varsayılan alan adı oldu. Yeni inbound alanları: **Max connections** (bağlantı sınırı), **Public IPv4/IPv6** (ad-tag middle proxy için). İstemci değişiklikleri, başkalarının Telegram oturumlarını düşürmeden «anında» uygulanır.
- WireGuard: inbound menüsü eksiksiz istemci işlemleri setine kavuştu (Export All URLs, bağlama/bağlantı kesme, gruplar), dışa aktarma **Config** ve **Links** sekmelerine ayrıldı, **«WireGuard izin verilen IP'ler» alanı düzenlenebilir oldu** (virgülle ayrılmış birden fazla kayıt), düğümdeki inbound'un istemci yapılandırmasında `Endpoint` artık düğümün adresini gösteriyor.

### Bölüm 7 değişiklikleri — Bağlantı Güvenliği: TLS, XTLS ve REALITY

- **Finalmask + REALITY kombinasyonu** kaydetme sırasında **reddediliyor** (ilk bağlantıda Xray-core'un çökmesine yol açıyordu); minClientVer yer tutucusu 26.3.27'ye güncellendi.
- Yeni Finalmask TCP maskesi türü — **XMC (Minecraft)**: akışın Minecraft trafiği gibi maskelenmesi (Hostname, Usernames, otomatik oluşturmalı zorunlu Password).

### Bölüm 8 değişiklikleri — İstemciler

- Yeni **«Hız»** sütunu — her istemcinin canlı hızı (↑/↓, ~5 saniyelik kayan ortalama).
- İstemci araması yeniden **Telegram ID** ile bulabiliyor; istemci formunda devre dışı inbound'lar bağlama listesinden gizleniyor; «Bağlantıyı Kes» penceresindeki kopya kayıt birikimi düzeltildi.
- MTProto istemcilerinin kendi alanları var: **«MTProto secret»** (yeniden oluşturmalı) ve **«Ad-tag (sponsorlu kanal)»** (32 hex karakter); kota ve süre artık MTProto'ya gerçekten uygulanıyor.

### Bölüm 9 değişiklikleri — İstemci Grupları

- İstemci bilgi penceresinde artık istemcinin **grubu** gösteriliyor.

### Bölüm 10 değişiklikleri — Abonelikler (Subscription)

- **Yönetilen hostlar grup haline geldi**: tek kayıt **birden fazla inbound** (çoklu seçim) ve **birden fazla adres** (etiketler; her kaydın kendi `:port`'u olabilir; adres otomatik tamamlama; boş — inbound adresi devralınır) kapsıyor. Liste sütunları adres ve inbound çiplerini gösteriyor («+N» ile), işlemler ve API gruplarla çalışıyor (`groupId`), toplu `POST /panel/api/hosts/bulk/add` eklendi. Host sıralaması artık geneldir (sıraya, ardından açıklamaya göre).
- **Duyuru** metni (`subAnnounce`) artık abonelik bilgi sayfasında bir afiş olarak gösteriliyor; özel şablonlarda `announce` değişkeni kullanılabilir.
- Bilgi sayfası tarayıcıda artık **JSON/Clash bağlantılarıyla** da açılıyor (yalnızca ana bağlantıyla değil).
- Host ayarları **Final Mask** ve **Allow insecure** artık sırasıyla raw bağlantılarda (`fm=`) ve **Hysteria2** için de (`insecure=1` / `skip-cert-verify: true`) geçerli.
- «Güncelleme aralıkları» (`subUpdates`) aralığı **0–525600** olarak düzeltildi (önceki 168 arayüz sınırı, 2.x'ten yükseltme sonrasında ayarların kaydedilmesini engelliyordu).
- Yerel **WireGuard istemcileri artık Clash ve JSON aboneliklerine giriyor** (önceden yalnızca raw'a).

### Bölüm 11 değişiklikleri — Xray: Yönlendirme, outbounds, DNS ve Uzantılar

- Outbound düzenleyicisi: yeni **«Target Strategy»** alanı (`AsIs`'ten `ForceIPv4`'e 11 değer), **«Real delay»** test modu (tünel kurulumu dahil tam süre; HTTP modu artık «ısınmış» bağlantı üzerinden ölçülüyor), HTTP/Real testinden sonra **Egress** («göz» arkasında çıkış IP'si) ve **Country** (bayrak + ülke, WARP etiketi) sütunları.
- **Yük dengeleyicinin fallback'i başka bir yük dengeleyiciyi gösterebilir**: panel gizli loopback nesnesini (`_bl_…`) kendisi kurar, döngülere ve kullanılan yük dengeleyicinin silinmesine karşı korur; `_bl_` öneki ayrılmıştır.
- «Temel Yönlendirme» sekmesine **«Default Outbound»** seçicisi eklendi — hiçbir kurala girmeyen trafiği hangi outbound'un işleyeceği (seçilen, ilk konuma taşınır).
- Özel IP'lerdeki DNS sunucuları artık `geoip:private` kuralıyla engellenmiyor — panel yönetilen bir izin kuralını kendisi sürdürüyor.
- dial (sockopt) ayarlarındaki Happy Eyeballs artık gerçekten etkinleşiyor; «Try delay» varsayılanı 250 ms, açıkça girilen 0 korunuyor.
- outbound abonelik içe aktarması: `?plugin=`/sondaki `/` içeren `ss://` bağlantılarında port doğru ayrıştırılıyor.

### Bölüm 12 değişiklikleri — Düğümler (Çok Panelli, master/slave)

- Düzeltme paketi: istemciyi değişiklik yapmadan kaydetmek artık düğüm inbound'larının canlı trafiğini bozmuyor; düğümün Host geçersiz kılmaları ilk kabulde master'a alınıyor; otomatik yenileme yeni bir kota penceresi açıyor; istemcinin master'da silinmesi onu düğümlerde tamamen siliyor; düğümün inbound'ları ilk kabulden önce süpürülmüyor; tek bir hatalı inbound düğümün trafik senkronizasyonunu durdurmuyor; port çakışması denetimi kendi düğümüyle sınırlandırıldı.

### Bölüm 14 değişiklikleri — Telegram Botu

- Bot komut menüsüne **`/usage`**, **`/inbound`**, **`/restart`** ve yeni yönetici komutu **`/clearall`** (tüm istemcilerin trafiğini sıfırlama, onaylı) eklendi.
- Çevrimiçi istemci listesi `email - inbound açıklaması` olarak etiketleniyor; yedek ve ban günlüğü mesajları ana bilgisayar adını içeriyor; Telegram ID araması, ayarların biçimlendirmesinden bağımsız çalışıyor.

### Bölüm 16 değişiklikleri — İşletim: Yedeklemeler, Günlükler, Güncelleme, CLI

- **PostgreSQL panelinde geri yükleme SQLite dosyalarını kabul ediyor**: normal `.db` yedeği veya geçiş `.dump` dosyası doğrudan PostgreSQL'e aktarılıyor (tek işlemle, Xray durdurulmadan önce denetimlerle). Dosya seçim iletişim kutusu her iki DBMS'te de `.dump,.db` kabul ediyor; «Geçiş Dosyasını İndir» yalnızca PostgreSQL panellerinde kaldı.
- Bir `pg_dump` arşivini geri yüklemeden önce panel dökümün okunabilirliğini denetliyor ve sürüm uyuşmazlığında tam `x-ui pgclient <sürüm>` komutunu öneriyor.
- Başlangıçta otomatik onarımlar: taşan trafik sayaçları sınırlandırılıp kurtarılıyor; inbound portundaki eski UNIQUE kısıtlaması kaldırılıyor (multi-node'u engelliyordu).
- Xray günlükleri: yeni görev, access ve error günlüğü **64 MiB**'ı aştığında her 10 dakikada bir kırpıyor; günlük temizleme artık her ikisini de temizliyor.
- Docker: sertifikaların otomatik yenilenmesi onarıldı (crond başlatılıyor, acme.sh durumu bir volume'de saklanıyor).

---

Panel kaynak dosyalarının analizinden oluşturulmuştur. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._
