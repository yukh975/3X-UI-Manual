# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 Bahasa Indonesia · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 [繁體中文](README.zh-TW.md)

Panduan pengguna untuk panel [3x-ui](https://github.com/MHSanaei/3x-ui) — panduan pengguna lengkap yang ditulis untuk panel **v3.5.0**.

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

## Apa yang Baru di 3.5.0

Versi 3.5.0 adalah rilis besar: MTProto dialihkan ke model multi-klien (mesin mtg-multi, secret personal, kuota, dan ad-tag), host terkelola menjadi grup (beberapa inbound dan alamat dalam satu entri), pemulihan pada panel PostgreSQL menerima backup SQLite, outbound mendapat «Target Strategy», uji «Real delay», dan kolom Egress/Country, serta balancer dapat menggunakan balancer lain sebagai fallback. Inti Xray 26.7.11 sudah disertakan. Berikut adalah perubahan dibandingkan 3.4.2, dikelompokkan berdasarkan bagian panduan.

### Perubahan di bagian 1 — Pendahuluan, Persyaratan, dan Instalasi

- Inti Xray diperbarui ke **26.7.11**. Migrasi otomatis penyerta: cipher Shadowsocks `none`/`plain` dan VMess `none`/`zero` dihapus dari inti (konfigurasi tersimpan ditulis ulang otomatis), dan outbound VLESS/Trojan tanpa enkripsi ke alamat publik ditolak saat penyimpanan.
- Perintah baru **`x-ui pgclient [versi]`** dan item **10. Install/Upgrade client tools (pg_dump/pg_restore)** di menu PostgreSQL — instalasi/pembaruan alat klien PostgreSQL.
- Perbaikan skrip: instalasi PostgreSQL dan fail2ban pada keluarga RHEL (EPEL), Arch tanpa `pacman -Syu` penuh, nama biner Xray yang benar pada ARM 32-bit (`xray-linux-arm32`), konfirmasi IPv4 yang terdeteksi otomatis sebelum penerbitan sertifikat IP, serta perbaikan pesan keliru «Your input is invalid» saat memilih port ACME default.

### Perubahan di bagian 2 — Login Panel dan Keamanan Akses

- Batas IP: koneksi «mati» kini diblokir **satu kali saja**, bukan pada setiap pemindaian 10 detik — penghitung fail2ban tidak lagi terus bertambah, dan `maxretry` tidak perlu dinaikkan berlebihan.

### Perubahan di bagian 4 — Inbounds: pembuatan dan parameter umum

- Daftar inbound kini memiliki **kolom pencarian** (berdasarkan catatan, port, dan protokol), dan daftar dropdown node («Deploy ke», filter «Node») kini mendukung pencarian.

### Perubahan di bagian 5 — Protokol

- **MTProto dialihkan ke model multi-klien** (mesin mtg-multi): pengguna MTProto kini menjadi klien biasa dengan secret, kuota, masa berlaku, ad-tag, dan tautan `tg://proxy` personal masing-masing. Field «Secret» di tingkat inbound dihapus (inbound yang ada dikonversi otomatis), dan «FakeTLS domain» menjadi domain default untuk secret baru. Field inbound baru: **Max connections** (pembatasan koneksi) dan **Public IPv4/IPv6** (untuk ad-tag middle proxy). Perubahan klien diterapkan «on the fly» tanpa memutus sesi Telegram pengguna lain.
- WireGuard: menu inbound mendapat rangkaian lengkap tindakan klien (Export All URLs, penautan/pelepasan, grup), ekspor dibagi menjadi tab **Config** dan **Links**, field **«IP yang diizinkan WireGuard» kini dapat diedit** (beberapa entri dipisahkan koma), dan pada konfigurasi klien untuk inbound yang berjalan di node, `Endpoint` kini menunjuk ke alamat node.

### Perubahan di bagian 7 — Keamanan Koneksi: TLS, XTLS, dan REALITY

- Kombinasi **Finalmask + REALITY ditolak** saat penyimpanan (kombinasi ini menyebabkan Xray-core crash pada koneksi pertama); placeholder minClientVer diperbarui menjadi 26.3.27.
- Tipe mask TCP Finalmask baru — **XMC (Minecraft)**: menyamarkan aliran sebagai trafik Minecraft (Hostname, Usernames, dan Password wajib dengan pembuatan otomatis).

### Perubahan di bagian 8 — Klien

- Kolom baru **«Kecepatan»** — kecepatan langsung setiap klien (↑/↓, rata-rata bergerak ~5 detik).
- Pencarian klien kembali dapat menemukan berdasarkan **Telegram ID**; di formulir klien, inbound yang dinonaktifkan disembunyikan dari daftar penautan; penumpukan duplikat di jendela «Lepas Tautan» diperbaiki.
- Klien MTProto memiliki field tersendiri: **«MTProto secret»** (dengan tombol pembuatan ulang) dan **«Ad-tag (kanal sponsor)»** (32 karakter hex); kuota dan masa berlaku kini benar-benar diterapkan pada MTProto.

### Perubahan di bagian 9 — Grup Klien

- Jendela informasi klien kini menampilkan **grup** klien tersebut.

### Perubahan di bagian 10 — Langganan (Subscription)

- **Host terkelola menjadi grup**: satu entri mencakup **beberapa inbound** (multi-pilih) dan **beberapa alamat** (input tag, setiap entri dapat memiliki `:port` sendiri; pelengkapan otomatis alamat; kosong — mewarisi alamat inbound). Kolom daftar menampilkan chip alamat dan inbound (dengan «+N»), tindakan dan API bekerja dengan grup (`groupId`), dan tersedia endpoint massal `POST /panel/api/hosts/bulk/add`. Pengurutan host kini global (berdasarkan urutan, lalu berdasarkan remark).
- Teks **pengumuman** (`subAnnounce`) kini ditampilkan sebagai banner di halaman info langganan; variabel `announce` tersedia untuk template kustom.
- Halaman info di browser kini juga terbuka melalui **tautan JSON/Clash** (bukan hanya tautan utama).
- Pengaturan host **Final Mask** dan **Allow insecure** kini juga berlaku masing-masing di tautan raw (`fm=`) dan untuk **Hysteria2** (`insecure=1` / `skip-cert-verify: true`).
- Rentang «Interval pembaruan langganan» (`subUpdates`) diperbaiki menjadi **0–525600** (batas UI lama 168 memblokir penyimpanan pengaturan setelah upgrade dari 2.x).
- Klien **WireGuard native kini masuk ke langganan Clash dan JSON** (sebelumnya hanya ke raw).

### Perubahan di bagian 11 — Xray: Routing, Outbounds, DNS, dan Ekstensi

- Editor outbound: field baru **«Target Strategy»** (11 nilai dari `AsIs` hingga `ForceIPv4`), mode uji **«Real delay»** (waktu penuh termasuk pembentukan tunnel; mode HTTP kini diukur pada koneksi «hangat»), serta kolom **Egress** (IP keluar di balik ikon «mata») dan **Country** (bendera + negara, label WARP) setelah uji HTTP/Real.
- **Fallback balancer dapat menunjuk ke balancer lain**: panel sendiri membangun objek loopback tersembunyi (`_bl_…`), melindungi dari siklus dan dari penghapusan balancer yang sedang digunakan; prefiks `_bl_` dicadangkan.
- Tab «Routing dasar» mendapat selektor **«Default Outbound»** — outbound mana yang menangani trafik yang tidak cocok dengan aturan mana pun (outbound yang dipilih dipindahkan ke posisi pertama).
- Server DNS pada IP privat tidak lagi diblokir oleh aturan `geoip:private` — panel sendiri memelihara aturan allow terkelola.
- Happy Eyeballs di pengaturan dial (sockopt) kini benar-benar aktif; «Try delay» kini default 250 md, nilai `0` eksplisit tetap disimpan.
- Impor langganan outbound: port pada tautan `ss://` dengan `?plugin=`/`/` di akhir kini diurai dengan benar.

### Perubahan di bagian 12 — Node (multipanel, master/slave)

- Paket perbaikan: menyimpan klien tanpa perubahan tidak lagi merusak trafik aktif inbound node; penggantian Host dari node diterima ke master pada penerimaan pertama; perpanjangan otomatis membuka jendela kuota yang baru; penghapusan klien di master menghapusnya sepenuhnya di node; inbound node tidak lagi disapu sebelum penerimaan pertama; satu inbound yang tidak valid tidak menghentikan sinkronisasi trafik node; pemeriksaan konflik port dibatasi pada node itu sendiri.

### Perubahan di bagian 14 — Bot Telegram

- Menu perintah bot mendapat tambahan **`/usage`**, **`/inbound`**, **`/restart`**, dan perintah admin baru **`/clearall`** (reset trafik semua klien, dengan konfirmasi).
- Daftar klien online kini diberi label `email - remark inbound`; pesan backup dan log ban menyertakan nama host; pencarian berdasarkan Telegram ID berfungsi terlepas dari pemformatan pengaturan.

### Perubahan di bagian 16 — Operasional: Cadangan, Log, Pembaruan, CLI

- **Pemulihan pada panel PostgreSQL menerima file SQLite**: backup biasa `.db` atau dump migrasi `.dump` diimpor langsung ke PostgreSQL (dalam satu transaksi, dengan pemeriksaan sebelum Xray dihentikan). Dialog pemilihan file menerima `.dump,.db` di kedua DBMS; «Unduh file migrasi» kini hanya tersedia di panel PostgreSQL.
- Sebelum memulihkan arsip `pg_dump`, panel memeriksa keterbacaan dump dan, jika versi tidak cocok, menyarankan perintah persisnya `x-ui pgclient <versi>`.
- Perbaikan otomatis saat startup: penghitung trafik yang meluap dijepit dan dipulihkan; batasan UNIQUE usang pada port inbound dihapus (menghambat multi-node).
- Log Xray: tugas baru setiap 10 menit memangkas log access dan error saat melebihi **64 MiB**; pembersihan harian kini membersihkan keduanya.
- Docker: perpanjangan otomatis sertifikat diperbaiki (crond dijalankan, status acme.sh disimpan dalam volume).

---

Dibuat berdasarkan analisis file sumber panel. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._
