# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 Bahasa Indonesia · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 [繁體中文](README.zh-TW.md)

Panduan pengguna untuk panel [3x-ui](https://github.com/MHSanaei/3x-ui) — panduan pengguna lengkap yang ditulis untuk panel **v3.4.2**.

> **Mirror hanya-baca.** Repositori GitHub ini adalah mirror satu arah — sumber manual berada di GitLab pribadi dan didorong ke sini secara otomatis, sehingga selalu mutakhir. Menemukan kesalahan atau ketidaktepatan? Silakan [buka Isu](https://github.com/yukh975/3X-UI-Manual/issues). **Pull request tidak diterima** (ditutup secara otomatis) — perbaikan dilakukan di sumber.

## Daftar Isi

| Berkas | Bahasa | Format |
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

## Apa yang Baru di 3.4.2

Versi 3.4.2 adalah pembaruan besar: WireGuard dialihkan ke model multi-klien, REALITY mendapat pemindai target langsung, balancer memperoleh tab Observatory/Burst Observatory, dan ditambahkan konfirmasi pengaturan sensitif dengan kode 2FA. Berikut adalah perubahan dibandingkan 3.4.1, dikelompokkan berdasarkan bagian panduan.

### Perubahan di bagian 1 — Pendahuluan, Persyaratan, dan Instalasi

- Di menu samping (dan di laci geser pada perangkat seluler) muncul tombol **«Dokumentasi»** (ikon buku) — membuka dokumentasi resmi `https://docs.sanaei.dev/`.
- Versi Xray minimum yang dapat diperbarui oleh panel dinaikkan menjadi **26.6.27** (inti Xray 26.6.27 sudah disertakan).

### Perubahan di bagian 2 — Login Panel dan Keamanan Akses

- Saat 2FA diaktifkan, mengganti login/password administrator dan menonaktifkan 2FA kini memerlukan **memasukkan kode saat ini** dari aplikasi autentikator (konfirmasi perubahan sensitif).
- LDAP: sakelar baru **«Lewati verifikasi sertifikat TLS»** (`ldapInsecureSkipVerify`) — menonaktifkan verifikasi sertifikat saat LDAPS; hanya tersedia jika «Gunakan TLS (LDAPS)» diaktifkan.

### Perubahan di bagian 3 — Ikhtisar / Dashboard

- Tombol versi panel kini selalu membuka jendela pembaruan (lihat bagian 16 — saluran dev).
- Peningkatan **aksesibilitas** secara menyeluruh: label aria untuk ikon dan aktivasi elemen dengan Enter/Space (untuk pembaca layar dan navigasi keyboard).

### Perubahan di bagian 4 — Inbounds: pembuatan dan parameter umum

- Tindakan **«Ekspor semua tautan»** kini membentuk tautan melalui mesin langganan — menerapkan template remark ke setiap klien dan memilih endpoint Host terkelola (sebelumnya remark tetap `inbound-email`).

### Perubahan di bagian 5 — Protokol

- **WireGuard dialihkan ke model multi-klien.** Peer kini menjadi klien biasa (dengan penetapan alamat tunnel otomatis, dukungan langganan, batas lalu lintas/masa berlaku, dan grup); daftar inline «Peer» dari formulir inbound dihapus.
- Pada inbound WireGuard ditambahkan field **DNS** yang dapat dikonfigurasi (default `1.1.1.1, 1.0.0.1`) dan **kartu konfigurasi klien** — salin/unduh/QR `.conf` lengkap serta tautan `wireguard://`/`wg://`.

### Perubahan di bagian 6 — Transport (Stream Settings)

- Pada XHTTP untuk inbound baru, parameter `maxConnections` di **xmux** kini default-nya **6** (sebelumnya `0` — tanpa batas). Inbound yang sudah ada mempertahankan nilainya.

### Perubahan di bagian 7 — Keamanan Koneksi: TLS, XTLS, dan REALITY

- Ditambahkan **pemindai target REALITY langsung**: tombol **«Pindai»** (memeriksa target saat ini «secara langsung») dan **«Cari target»** (memindai domain atau rentang **IP/CIDR** dan memilih target yang cocok berdasarkan sertifikatnya). Field «Target» dan SNI kini kosong saat REALITY pertama kali dipilih.

### Perubahan di bagian 8 — Klien

- Perpanjangan masa berlaku/kuota melalui `bulkAdjust` kini **secara otomatis mengaktifkan** klien yang dinonaktifkan hanya karena habis (masa berlaku berakhir atau kuota terlampaui), jika perpanjangan mengembalikannya ke dalam batas. Klien yang dinonaktifkan secara manual atau yang masih habis tetap nonaktif.

### Perubahan di bagian 9 — Grup Klien

- **«Reset Traffic»** pada grup kini hanya menol-kan **penghitung grup itu sendiri**; penghitung, kuota, dan status masing-masing klien tidak terpengaruh, dan restart Xray tidak diperlukan. Ini adalah perubahan dari perilaku sebelumnya (sebelumnya lalu lintas semua klien grup direset).

### Perubahan di bagian 10 — Langganan (Subscription)

- Pada **host terkelola**, field **VLESS route** didefinisikan ulang: kini berupa satu nilai `0-65535` (bukan daftar port), dan nilai itu benar-benar «ditanamkan» ke UUID setiap langganan (raw/JSON/Clash).
- Variabel `{{EMAIL}}` (dan sinonimnya `{{USERNAME}}`) di template remark kini hanya ditampilkan pada **tautan pertama** klien — sama seperti blok lalu lintas/masa berlaku.

### Perubahan di bagian 11 — Xray: Routing, Outbounds, DNS, dan Ekstensi

- **Balancer**: halaman dibagi menjadi tab **«Pengaturan balancer»** dan **«Observatory»**; alih-alih JSON mentah — formulir Observatory dan Burst Observatory (pada Burst ditambahkan field **«Metode HTTP»**). Balancer Random/Round-robin dengan `fallbackTag` kini otomatis membuat Burst Observatory.
- Saat menghapus outbound atau balancer, panel secara otomatis membersihkan tautan terkait di routing dan menampilkan **pratinjau dampak** di dialog konfirmasi.
- Dalam aturan routing, kriteria jaringan **L4** ditulis ke config dalam huruf kecil (`tcp`/`udp`), tetapi ditampilkan dalam huruf kapital di tabel.
- Kesalahan pada formulir penambahan/pengeditan balancer kini ditangguhkan hingga field pertama disentuh atau penyimpanan dicoba.

### Perubahan di bagian 12 — Node (multipanel, master/slave)

- Notifikasi «disimpan secara lokal, node offline — akan disinkronkan nanti» kini hanya ditampilkan ketika node benar-benar offline atau dimatikan (sebelumnya — pada setiap penyimpanan ke node online).

### Perubahan di bagian 16 — Operasional: Cadangan, Log, Pembaruan, CLI

- Nama file cadangan kini menyertakan alamat server dan **tanggal-waktu**: `{host}_YYYY-MM-DD_HHMMSS.db` (`.dump` untuk PostgreSQL), misalnya `panel.example.com_2026-06-27_000000.db` — baik saat diunduh dari panel maupun pada cadangan yang dikirim bot Telegram.
- Saluran **dev** pembaruan kini dapat diaktifkan dari build stabil: tombol versi selalu membuka jendela pembaruan, dan muncul sakelar **«Saluran Dev»** dengan peringatan tentang ketidakstabilan dan tidak adanya rollback otomatis.

---

Dibuat berdasarkan analisis file sumber panel. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._
