# Panduan Pengguna Panel 3X-UI

🇸🇦 [العربية](3X-UI-MANUAL.ar.md) · 🇬🇧 [English](3X-UI-MANUAL.en.md) · 🇪🇸 [Español](3X-UI-MANUAL.es.md) · 🇮🇷 [فارسی](3X-UI-MANUAL.fa.md) · 🇮🇩 Bahasa Indonesia · 🇯🇵 [日本語](3X-UI-MANUAL.ja.md) · 🇷🇺 [Русский](3X-UI-MANUAL.ru.md) · 🇺🇦 [Українська](3X-UI-MANUAL.uk.md) · 🇨🇳 [简体中文](3X-UI-MANUAL.zh-CN.md) · 🇹🇼 [繁體中文](3X-UI-MANUAL.zh-TW.md)

**Versi 3X-UI: 3.4.0.** Panduan ini disusun berdasarkan versi ini dan berlaku untuk versi tersebut. Ringkasan perubahan 3.4.0 relatif terhadap 3.3.1 — di bagian [«Apa yang baru di 3.4.0»](#apa-yang-baru-di-340).

> Panduan lengkap berbahasa Indonesia untuk panel web **3X-UI** (pengelolaan
> Xray-core): fitur, konfigurasi, dan pengoperasian, dengan penjelasan setiap
> kolom dan sakelar di antarmuka.
>
> Nama dan label sesuai dengan antarmuka panel. Kata *inbound* / *outbound* tidak
> diterjemahkan.

## Daftar Isi

- [Apa yang baru di 3.4.0](#apa-yang-baru-di-340)
- [1. Pengantar, persyaratan, dan instalasi](#1-pengantar-persyaratan-dan-instalasi)
  - [1.1. Apa itu 3X-UI](#11-apa-itu-3x-ui)
  - [1.2. Sistem operasi dan arsitektur yang didukung](#12-sistem-operasi-dan-arsitektur-yang-didukung)
  - [1.3. Metode instalasi](#13-metode-instalasi)
  - [1.4. Peluncuran pertama dan kredensial default](#14-peluncuran-pertama-dan-kredensial-default)
  - [1.5. Lokasi file](#15-lokasi-file)
  - [1.6. Perintah manajemen `x-ui` (menu skrip)](#16-perintah-manajemen-x-ui-menu-skrip)
  - [1.7. Subperintah `x-ui` (tanpa menu interaktif)](#17-subperintah-x-ui-tanpa-menu-interaktif)
  - [1.8. Migrasi SQLite → PostgreSQL](#18-migrasi-sqlite--postgresql)
- [2. Masuk ke panel dan keamanan akses](#2-masuk-ke-panel-dan-keamanan-akses)
  - [2.1. Formulir login](#21-formulir-login)
  - [2.2. Autentikasi dua faktor (2FA / TOTP)](#22-autentikasi-dua-faktor-2fa--totp)
  - [2.3. Pembatasan percobaan login (login limiter / perlindungan brute-force)](#23-pembatasan-percobaan-login-login-limiter--perlindungan-brute-force)
  - [2.4. Mengubah nama pengguna dan kata sandi administrator](#24-mengubah-nama-pengguna-dan-kata-sandi-administrator)
  - [2.5. Path rahasia (URI path / webBasePath) dan port panel](#25-path-rahasia-uri-path--webbasepath-dan-port-panel)
  - [2.6. Masa aktif sesi (timeout)](#26-masa-aktif-sesi-timeout)
  - [2.7. LDAP (sinkronisasi dan autentikasi)](#27-ldap-sinkronisasi-dan-autentikasi)
- [3. Ikhtisar / Dashboard](#3-ikhtisar--dashboard)
  - [3.1. Prinsip umum pengumpulan data](#31-prinsip-umum-pengumpulan-data)
  - [3.2. CPU](#32-cpu)
  - [3.3. Memori (RAM)](#33-memori-ram)
  - [3.4. Swap](#34-swap)
  - [3.5. Disk (Storage)](#35-disk-storage)
  - [3.6. Waktu operasi sistem (Uptime)](#36-waktu-operasi-sistem-uptime)
  - [3.7. Beban sistem (Load average)](#37-beban-sistem-load-average)
  - [3.8. Jaringan: kecepatan dan total volume lalu lintas](#38-jaringan-kecepatan-dan-total-volume-lalu-lintas)
  - [3.9. Alamat IP server](#39-alamat-ip-server)
  - [3.10. Koneksi TCP/UDP](#310-koneksi-tcpudp)
  - [3.11. Status Xray dan manajemen proses](#311-status-xray-dan-manajemen-proses)
  - [3.12. Pembaruan panel (3X-UI)](#312-pembaruan-panel-3x-ui)
  - [3.13. Pembaruan file geo (GeoIP / GeoSite)](#313-pembaruan-file-geo-geoip--geosite)
  - [3.14. Pencadangan dan pemulihan basis data](#314-pencadangan-dan-pemulihan-basis-data)
  - [3.15. Elemen antarmuka tambahan](#315-elemen-antarmuka-tambahan)
- [4. Inbounds: pembuatan dan parameter umum](#4-inbounds-pembuatan-dan-parameter-umum)
  - [4.1. Kolom formulir umum](#41-kolom-formulir-umum)
  - [4.2. Sniffing](#42-sniffing)
  - [4.3. Allocate (strategi distribusi port)](#43-allocate-strategi-distribusi-port)
  - [4.4. External Proxy (Proksi eksternal)](#44-external-proxy-proksi-eksternal)
  - [4.5. Fallbacks](#45-fallbacks)
  - [4.6. Reset lalu lintas berkala](#46-reset-lalu-lintas-berkala)
  - [4.7. JSON inbound (advanced)](#47-json-inbound-advanced)
  - [4.8. Tindakan pada inbound: QR / Edit / Reset / Delete dan statistik](#48-tindakan-pada-inbound-qr--edit--reset--delete-dan-statistik)
- [5. Protokol](#5-protokol)
  - [5.1. Daftar protokol yang didukung](#51-daftar-protokol-yang-didukung)
  - [5.2. Protokol mana yang mendukung TLS / REALITY / transport](#52-protokol-mana-yang-mendukung-tls--reality--transport)
  - [5.3. VLESS](#53-vless)
  - [5.4. VMess](#54-vmess)
  - [5.5. Trojan](#55-trojan)
  - [5.6. Shadowsocks](#56-shadowsocks)
  - [5.7. Dokodemo-door / Tunnel (transparent forwarder)](#57-dokodemo-door--tunnel-transparent-forwarder)
  - [5.8. SOCKS / HTTP (protokol `mixed`)](#58-socks--http-protokol-mixed)
  - [5.9. WireGuard (inbound)](#59-wireguard-inbound)
  - [5.10. Hysteria (default v2)](#510-hysteria-default-v2)
  - [5.11. MTProto (proksi untuk Telegram)](#511-mtproto-proksi-untuk-telegram)
  - [5.12. Panduan singkat memilih protokol](#512-panduan-singkat-memilih-protokol)
- [6. Transport (Stream Settings)](#6-transport-stream-settings)
  - [6.1. Memilih jaringan transmisi](#61-memilih-jaringan-transmisi)
  - [6.2. RAW / TCP (`tcpSettings`)](#62-raw--tcp-tcpsettings)
  - [6.3. mKCP (`kcpSettings`)](#63-mkcp-kcpsettings)
  - [6.4. WebSocket (`wsSettings`)](#64-websocket-wssettings)
  - [6.5. gRPC (`grpcSettings`)](#65-grpc-grpcsettings)
  - [6.6. HTTPUpgrade (`httpupgradeSettings`)](#66-httpupgrade-httpupgradesettings)
  - [6.7. XHTTP / SplitHTTP (`xhttpSettings`)](#67-xhttp--splithttp-xhttpsettings)
  - [6.8. Transport Hysteria (`hysteriaSettings`)](#68-transport-hysteria-hysteriasettings)
  - [6.9. Parameter pendukung](#69-parameter-pendukung)
- [7. Keamanan koneksi: TLS, XTLS, dan REALITY](#7-keamanan-koneksi-tls-xtls-dan-reality)
  - [7.1. Perbedaan: TLS vs XTLS vs REALITY](#71-perbedaan-tls-vs-xtls-vs-reality)
  - [7.2. Mode «None» (`none`)](#72-mode-none-none)
  - [7.3. Mode TLS](#73-mode-tls)
  - [7.4. Mode REALITY](#74-mode-reality)
  - [7.5. Rekomendasi praktis konfigurasi](#75-rekomendasi-praktis-konfigurasi)
- [8. Klien](#8-klien)
  - [8.1. Kolom klien](#81-kolom-klien)
  - [8.2. Penautan ke inbound](#82-penautan-ke-inbound)
  - [8.3. Operasi pada klien](#83-operasi-pada-klien)
  - [8.4. Operasi massal](#84-operasi-massal)
  - [8.5. Pencarian, filter, dan pengurutan](#85-pencarian-filter-dan-pengurutan)
  - [8.6. Ikon dan status](#86-ikon-dan-status)
- [9. Grup klien](#9-grup-klien)
  - [9.1. Apa itu grup klien dan untuk apa](#91-apa-itu-grup-klien-dan-untuk-apa)
  - [9.2. Hubungan grup dengan klien, inbound, node, dan protokol](#92-hubungan-grup-dengan-klien-inbound-node-dan-protokol)
  - [9.3. Direktori grup dan grup «kosong»](#93-direktori-grup-dan-grup-kosong)
  - [9.4. Kolom dan bidang grup](#94-kolom-dan-bidang-grup)
  - [9.5. Membuat grup](#95-membuat-grup)
  - [9.6. Mengganti nama grup](#96-mengganti-nama-grup)
  - [9.7. Menambahkan klien ke grup](#97-menambahkan-klien-ke-grup)
  - [9.8. Menghapus klien dari grup (tanpa menghapus klien itu sendiri)](#98-menghapus-klien-dari-grup-tanpa-menghapus-klien-itu-sendiri)
  - [9.9. Reset lalu lintas grup](#99-reset-lalu-lintas-grup)
  - [9.10. Menghapus grup dan menghapus klien grup](#910-menghapus-grup-dan-menghapus-klien-grup)
  - [9.11. Hubungan dengan halaman «Klien»](#911-hubungan-dengan-halaman-klien)
  - [9.12. Ringkasan endpoint API](#912-ringkasan-endpoint-api)
  - [9.13. Lalu lintas per grup](#913-lalu-lintas-per-grup)
- [10. Langganan (Subscription)](#10-langganan-subscription)
  - [10.1. Apa itu subId dan bagaimana tautan dibentuk](#101-apa-itu-subid-dan-bagaimana-tautan-dibentuk)
  - [10.2. Pengaturan server langganan](#102-pengaturan-server-langganan)
  - [10.3. Format output](#103-format-output)
  - [10.4. Halaman informasi langganan dan kode QR](#104-halaman-informasi-langganan-dan-kode-qr)
  - [10.5. Template kustom halaman langganan](#105-template-kustom-halaman-langganan)
- [11. Xray: routing, outbounds, DNS, dan ekstensi](#11-xray-routing-outbounds-dns-dan-ekstensi)
  - [11.1. Struktur editor: tab/mode](#111-struktur-editor-tabmode)
  - [11.2. Pengaturan umum (General)](#112-pengaturan-umum-general)
  - [11.3. Aturan routing (routing)](#113-aturan-routing-routing)
  - [11.4. Outbounds (koneksi keluar)](#114-outbounds-koneksi-keluar)
  - [11.5. Balancer (Balancers)](#115-balancer-balancers)
  - [11.6. DNS](#116-dns)
  - [11.7. Fake DNS](#117-fake-dns)
  - [11.8. WireGuard / WARP / NordVPN](#118-wireguard--warp--nordvpn)
  - [11.9. Reverse proxy dan TUN](#119-reverse-proxy-dan-tun)
  - [11.10. Log dan statistik (Stats, metrics)](#1110-log-dan-statistik-stats-metrics)
  - [11.11. Penyimpanan, restart, dan transformasi otomatis](#1111-penyimpanan-restart-dan-transformasi-otomatis)
  - [11.12. Outbound dari langganan (dengan pembaruan otomatis)](#1112-outbound-dari-langganan-dengan-pembaruan-otomatis)
  - [11.13. Rotasi IP di WARP](#1113-rotasi-ip-di-warp)
- [12. Node (multipanel, master/slave)](#12-node-multipanel-masterslave)
  - [12.1. Ringkasan di bagian atas daftar](#121-ringkasan-di-bagian-atas-daftar)
  - [12.2. Menambahkan dan mengedit node](#122-menambahkan-dan-mengedit-node)
  - [12.3. Verifikasi TLS (untuk node https)](#123-verifikasi-tls-untuk-node-https)
  - [12.4. Informasi yang ditampilkan per node](#124-informasi-yang-ditampilkan-per-node)
  - [12.5. Tindakan pada node](#125-tindakan-pada-node)
  - [12.6. Riwayat metrik](#126-riwayat-metrik)
  - [12.7. Cara inbound dan klien disinkronkan](#127-cara-inbound-dan-klien-disinkronkan)
  - [12.8. Rantai node (sub-node / node transit)](#128-rantai-node-sub-node--node-transit)
  - [12.9. Node: yang baru di 3.3.0](#129-node-yang-baru-di-330)
- [13. Pengaturan panel](#13-pengaturan-panel)
  - [13.1. Menyimpan dan me-restart panel](#131-menyimpan-dan-me-restart-panel)
  - [13.2. Pengaturan umum (tab «Panel» / *General*)](#132-pengaturan-umum-tab-panel--general)
  - [13.3. Akses ke panel: IP, port, path, domain, sertifikat](#133-akses-ke-panel-ip-port-path-domain-sertifikat)
  - [13.4. Sesi, proksi panel, dan proksi tepercaya (tab «Proksi dan Server» / *Proxy and Server*)](#134-sesi-proksi-panel-dan-proksi-tepercaya-tab-proksi-dan-server--proxy-and-server)
  - [13.5. Bot Telegram (tab «Bot Telegram» / *Telegram Bot*)](#135-bot-telegram-tab-bot-telegram--telegram-bot)
  - [13.6. Tanggal dan waktu (tab «Tanggal dan Waktu» / *Date and Time*)](#136-tanggal-dan-waktu-tab-tanggal-dan-waktu--date-and-time)
  - [13.7. Lalu lintas eksternal dan perilaku Xray (tab «Lalu Lintas Eksternal» / *External Traffic*)](#137-lalu-lintas-eksternal-dan-perilaku-xray-tab-lalu-lintas-eksternal--external-traffic)
  - [13.8. Lainnya: template konfigurasi Xray dan URL verifikasi](#138-lainnya-template-konfigurasi-xray-dan-url-verifikasi)
  - [13.9. Akun administrator dan token API](#139-akun-administrator-dan-token-api)
  - [13.10. Perubahan API di 3.3.0 (penting untuk integrasi)](#1310-perubahan-api-di-330-penting-untuk-integrasi)
- [14. Bot Telegram](#14-bot-telegram)
  - [14.1. Mengaktifkan dan mengonfigurasi bot](#141-mengaktifkan-dan-mengonfigurasi-bot)
  - [14.2. Menu utama dan tombol](#142-menu-utama-dan-tombol)
  - [14.3. Perintah bot](#143-perintah-bot)
  - [14.4. Manajemen klien (khusus administrator)](#144-manajemen-klien-khusus-administrator)
  - [14.5. Notifikasi dan laporan](#145-notifikasi-dan-laporan)
  - [14.6. Cadangan dan log](#146-cadangan-dan-log)
  - [14.7. Fitur pengoperasian](#147-fitur-pengoperasian)
- [15. Basis geo (geoip / geosite dan kustom)](#15-basis-geo-geoip--geosite-dan-kustom)
  - [15.1. Apa itu geoip.dat dan geosite.dat](#151-apa-itu-geoipdat-dan-geositedat)
  - [15.2. File geo standar dan pembaruannya](#152-file-geo-standar-dan-pembaruannya)
  - [15.3. Sumber daya geo kustom (Custom GeoSite / GeoIP)](#153-sumber-daya-geo-kustom-custom-geosite--geoip)
  - [15.4. Validasi dan batasan](#154-validasi-dan-batasan)
  - [15.5. Pemeriksaan otomatis saat panel dimulai](#155-pemeriksaan-otomatis-saat-panel-dimulai)
  - [15.6. Penggunaan basis geo dalam aturan routing](#156-penggunaan-basis-geo-dalam-aturan-routing)
- [16. Pengoperasian: cadangan, log, pembaruan, CLI](#16-pengoperasian-cadangan-log-pembaruan-cli)
  - [16.1. Pencadangan dan pemulihan basis data](#161-pencadangan-dan-pemulihan-basis-data)
  - [16.2. Melihat log](#162-melihat-log)
  - [16.3. Tingkat dan konfigurasi logging Xray](#163-tingkat-dan-konfigurasi-logging-xray)
  - [16.4. Manajemen Xray: menghentikan dan me-restart](#164-manajemen-xray-menghentikan-dan-me-restart)
  - [16.5. Me-restart dan memperbarui panel](#165-me-restart-dan-memperbarui-panel)
  - [16.6. Tugas berkala (cron)](#166-tugas-berkala-cron)
  - [16.7. Menu konsol dan CLI (`x-ui`)](#167-menu-konsol-dan-cli-x-ui)
  - [16.8. Menghapus panel](#168-menghapus-panel)
  - [16.9. Perintah `x-ui migrateDB`](#169-perintah-x-ui-migratedb)

---

## Apa yang baru di 3.4.0

Bagian ini merangkum perubahan versi **3.4.0** dibandingkan 3.3.1 yang terlihat oleh pengguna panel, dikelompokkan berdasarkan bagian panduan. Detail setiap fitur ada di bagian yang sesuai di bawah.

### 3. Ikhtisar / Dashboard
- **Riwayat metrik sistem: interval agregasi baru 12h/24h/48h** — Di jendela riwayat metrik sistem, nilai 12h, 24h, dan 48h ditambahkan ke interval rata-rata — sekarang grafik (CPU, RAM, lalu lintas, paket, koneksi, disk, online, beban) dapat dilihat untuk periode hingga dua hari.

### 4. Inbounds: pembuatan dan parameter umum
- **Inbound: peringatan konflik dengan port Xray API yang dicadangkan** — Saat membuat atau mengubah inbound, panel kini tidak mengizinkan penggunaan port internal Xray API yang dicadangkan (default 62789 pada 127.0.0.1): TCP inbound lokal pada port tersebut di loopback ditolak dengan kesalahan konflik port. Pada node, pembatasan ini tidak berlaku — mereka memiliki Xray sendiri.
- **Tunnel/TProxy: menerima streamSettings tanpa kunci security** — Inbound tipe tunnel/TProxy yang streamSettings-nya tidak mengandung blok security kini dapat dibuka dan disimpan tanpa kesalahan validasi.
- **Inbounds: kolom Speed (kecepatan langsung) di daftar** — Di daftar inbounds, kolom Speed ditambahkan yang menampilkan kecepatan lalu lintas saat ini (upload/download) untuk setiap inbound.

### 5. Protokol
- **Shadowsocks-2022: regenerasi PSK klien saat metode dengan ukuran kunci berbeda diubah** — Untuk Shadowsocks-2022: saat metode enkripsi diubah ke metode dengan ukuran kunci yang berbeda (misalnya antara aes-256 dan aes-128), PSK klien sekarang diregenerasi otomatis sesuai panjang baru saat inbound disimpan. Akibatnya: klien yang terpengaruh perlu mendapatkan ulang langganan (tautan lama tidak akan berfungsi).
- **WireGuard: kolom workers dihapus** — Kolom workers dihapus dari formulir WireGuard (inbound dan outbound): xray-core v26.6.22 tidak lagi menggunakannya. Konfigurasi yang tersimpan sebelumnya tetap berfungsi — kolom ini cukup diabaikan.
- **VLESS+XHTTP: flow xtls-rprx-vision dalam tautan dan langganan** — Untuk VLESS melalui XHTTP, flow xtls-rprx-vision kini dengan benar disertakan dalam tautan dan langganan (termasuk untuk XHTTP+REALITY dan dalam format Clash/Mihomo). Sebelumnya panel menyimpan flow, tetapi klien menerima konfigurasi tanpa vision.

### 6. Transport (Stream Settings)
- **XHTTP: penggantian nama kolom sessionID + Session ID Table / Length** — Di transport XHTTP, kolom sesi diganti namanya: Session ID Placement dan Session ID Key (sebelumnya — Session Placement / Session Key). Dua parameter ditambahkan. Session ID Table — kumpulan karakter untuk menghasilkan pengenal sesi: dapat memilih yang sudah ditentukan (ALPHABET, Base62, hex, number, dll.) atau memasukkan string ASCII kustom; kosong — nilai default xray-core. Session ID Length — panjang atau rentang (misalnya 8-16) pengenal yang dihasilkan; hanya diperhitungkan ketika Session ID Table ditetapkan, minimum harus lebih besar dari 0. Inbound yang tersimpan sebelumnya dimigrasikan secara otomatis.
- **Inbound: preset Real client IP untuk menentukan IP nyata di balik CDN/relay** — Di pengaturan soket (sockopt) inbound, pemilihan Real client IP ditambahkan — preset untuk menentukan IP nyata pengunjung ketika lalu lintas datang melalui CDN atau relay (jika tidak, alamat perantara yang tercatat). Tersedia tiga opsi: Off / direct (tanpa pemrosesan), Cloudflare CDN (percayai X-Forwarded-For) dan L4 relay / Spectrum (PROXY) (terima header protokol PROXY). Preset saling eksklusif dan memperingatkan jika transport yang dipilih tidak mendukungnya. Kolom ini tidak pernah dikirim ke klien dalam langganan.
- **gRPC: header Trusted X-Forwarded-For sekarang diperhitungkan** — Header Trusted X-Forwarded-For sekarang diperhitungkan pada transport gRPC juga (sebelumnya — hanya WebSocket, HTTPUpgrade, dan XHTTP). Untuk inbound gRPC, panel tidak lagi menampilkan peringatan tentang header yang tidak didukung.

### 7. Keamanan koneksi: TLS, XTLS, dan REALITY
- **TLS: kolom baru Verify Peer Cert By Name, Curve Preferences, Master Key Log, ECH Sockopt** — Verify Peer Cert By Name — nama (dipisahkan koma) yang digunakan klien untuk memverifikasi sertifikat server alih-alih SNI; pengganti modern dari allowInsecure yang dihapus, disertakan dalam tautan dan langganan, tidak ditulis ke server. Curve Preferences — pembatasan dan urutan kurva pertukaran kunci TLS (misalnya X25519MLKEM768, X25519); kosong — nilai default. Master Key Log — path untuk menulis kunci TLS (format SSLKEYLOGFILE) untuk debugging di Wireshark; biarkan kosong di produksi. ECH Sockopt — parameter soket untuk mendapatkan konfigurasi ECH (dialerProxy, Domain Strategy, TCP Fast Open, Multipath TCP).
- **REALITY: pembatasan kecepatan fallback (Limit Fallback) dan Master Key Log** — Untuk setiap arah (Upload dan Download) ditetapkan: After Bytes — berapa byte yang dibiarkan lewat dengan kecepatan penuh sebelum pembatasan dimulai (0 — batasi dari byte pertama); Bytes Per Sec — batas atas kecepatan lalu lintas fallback agar probe tidak menggunakan server sebagai saluran gratis (0 — tanpa batas, menonaktifkan arah); Burst Bytes Per Sec — cadangan untuk lonjakan sementara. Kolom Master Key Log (path ke file SSLKEYLOGFILE untuk debugging) juga ditambahkan.
- **TLS: tombol pengisian Pinned Peer Cert SHA-256 dari sertifikat inbound dan berdasarkan SNI** — Di sebelah kolom Pinned Peer Cert SHA-256 sekarang ada dua tombol pengisian otomatis, menggantikan tombol hash acak sebelumnya. Tombol pertama memasukkan SHA-256 sertifikat inbound itu sendiri. Tombol kedua mendapatkan hash sertifikat server langsung dengan melakukan koneksi TLS ke SNI yang ditentukan (serverName harus diisi). Hash yang diperoleh ditambahkan ke kolom (dipisahkan koma) dan disertakan dalam tautan untuk penambatan sertifikat di klien.
- **TLS: OCSP-stapling dinonaktifkan secara default untuk sertifikat inbound baru** — Untuk inbound baru, OCSP stapling dinonaktifkan secara default (interval 0). Ini menghilangkan kesalahan di log xray untuk sertifikat tanpa OCSP responder (misalnya Let's Encrypt). Kolom tetap ada — dapat diaktifkan untuk sertifikat yang mendukung stapling.
- **REALITY: kompatibilitas dengan kolom dest (alias target)** — Jika inbound REALITY dibuat dengan kolom dest (oleh versi panel lama, melalui API atau alat eksternal), kini dimuat dengan benar: nilai dest dimasukkan ke kolom Target. Sebelumnya Target menjadi kosong, dan penyimpanan ulang merusak REALITY.

### 8. Klien
- **Tab «Links» di editor klien (tautan eksternal dan langganan)** — Di sana tombol **Add External Link** menambahkan tautan berbagi pihak ketiga (`vless://`, `vmess://`, `trojan://`, `ss://`, `hysteria2://`, `wireguard://`), dan tombol **Add External Subscription** — URL langganan jarak jauh. Semua ini dicampurkan ke dalam output langganan klien tersebut (format raw, JSON, dan Clash): tautan ditambahkan apa adanya, sedangkan langganan jarak jauh secara berkala diunduh panel dan konfigurasinya digabungkan dengan konfigurasi milik panel sendiri.
- **Kolom «IP Limit» sekarang dinonaktifkan tanpa Fail2ban** — Kolom **IP Limit** sekarang hanya berfungsi jika Fail2ban terpasang dan aktif. Jika Fail2ban tidak terpasang (atau sistem Windows, atau fitur dinonaktifkan di server), kolom editor klien diblokir, dan saat kursor diarahkan, tooltip ditampilkan menyarankan instalasi Fail2ban dari menu bash `x-ui`. Saat panel diperbarui, batas IP yang tersimpan pada klien di server tanpa Fail2ban akan diatur ulang ke nol, karena batas tersebut memang tidak diterapkan di sana.
- **Menghapus klien yang tidak terpaut, ekspor dan impor klien** — Di menu **Lainnya** pada halaman **Klien**, tiga operasi ditambahkan. **Ekspor klien** menampilkan daftar JSON semua klien (dalam format `{client, inboundIds}`) dengan tombol salin dan unduh (`clients-export.json`). **Impor klien** menerima JSON yang sama: klien dengan tautan dibuat ulang dan ditautkan ke inbound, klien tanpa tautan dipulihkan sebagai entri terpisah, dan email yang sudah ada tidak ditimpa (ditandai sebagai dilewati). **Hapus klien yang tidak terpaut** menghapus semua klien yang tidak terpaut ke inbound mana pun, beserta lalu lintas, log IP, dan tautan eksternalnya; tindakan ini tidak dapat dibatalkan.
- **Log IP klien: waktu koneksi dan nama node** — Di log IP klien (tombol lihat di sebelah kolom «IP Limit» dan di kartu «Informasi klien»), setiap entri sekarang berisi, selain IP itu sendiri, waktu akses terakhir dan label node (`@ nama_node`) tempat koneksi tercatat — dalam konfigurasi multipanel, terlihat melalui node mana klien terhubung.
- **Reset label grup pada klien di editor tunggal** — Sekarang jika di editor satu klien kolom **Grup** dikosongkan dan disimpan, label grup dihapus dengan benar — sebelumnya klien dapat terus ditampilkan di bawah grup lama hingga penyimpanan ulang berikutnya.
- **Daftar klien diperbarui otomatis (polling latar belakang)** — Daftar klien sekarang diperbarui secara otomatis: panel setiap beberapa detik mengambil halaman terkini, sehingga klien yang baru terhubung dan urutan pengurutan yang berubah muncul tanpa perlu refresh manual.

### 10. Langganan (Subscription)
- **Hosts yang dikelola: penggantian tautan langganan per host** — Di versi 3.4.0 ditambahkan bagian Hosts (item menu samping). Untuk setiap inbound dapat ditetapkan satu atau beberapa endpoint Host yang menggantikan alamat, port, dan parameter TLS inbound itu sendiri dalam tautan langganan — ini praktis untuk mendistribusikan lalu lintas melalui CDN atau relay. Host memiliki Remark dan deskripsi, tautan ke inbound, Address (kosong — mewarisi alamat inbound) dan Port (0 — mewarisi port inbound), parameter Security (same/tls/none/reality), serta Host header, Path, Mux, Sockopt, Final Mask, pengecualian dari format langganan (raw/json/clash), dan parameter untuk Clash/mihomo. Host diurutkan di dalam inbound dan mendukung operasi massal.
- **Remark Template menggantikan pembuat model remark; variabel {{VAR}}** — Pembuat nama profil sebelumnya (memilih Inbound/Email/External Proxy dan pemisah) digantikan oleh kolom «Remark Template». Di dalamnya Anda menulis format nama yang kustom, menyisipkan variabel dengan tombol: identifikasi klien ({{EMAIL}}, {{INBOUND}}, {{HOST}}, {{ID}}, {{SUB_ID}}, {{COMMENT}}, {{TELEGRAM_ID}}), lalu lintas ({{TRAFFIC_USED}}, {{TRAFFIC_LEFT}}, {{TRAFFIC_TOTAL}}, {{UP}}, {{DOWN}}, {{USAGE_PERCENTAGE}}) dan masa berlaku/status ({{DAYS_LEFT}}, {{TIME_LEFT}}, {{EXPIRE_DATE}}, {{JALALI_EXPIRE_DATE}}, {{STATUS}}, {{STATUS_EMOJI}}). Variabel disubstitusi secara individual untuk setiap klien saat langganan dibuat, tersedia pratinjau. Segmen yang dipisahkan simbol «|» dengan nilai tanpa batas disembunyikan secara otomatis, dan informasi penggunaan dan masa berlaku hanya ditampilkan pada tautan pertama klien. Jika kolom dibiarkan kosong, model remark lama digunakan.
- **Tautan eksternal dan langganan jarak jauh per klien (tab Links)** — Di sini untuk klien individual dapat dilampirkan tautan berbagi pihak ketiga (Add External Link) dan alamat langganan eksternal (Add External Subscription) — semuanya akan disertakan dalam langganan klien itu sendiri (format RAW, JSON, dan Clash). Langganan eksternal diunduh panel dan digabungkan dengan konfigurasi klien. Ini praktis untuk memberikan klien server tambahan di atas inbound Anda.
- **Happ: menyembunyikan pengaturan server di klien (Hide server settings)** — Di tab Happ pengaturan langganan ditambahkan sakelar «Hide server settings». Ketika diaktifkan, kemampuan untuk melihat dan mengubah parameter server disembunyikan di klien Happ. Opsi ini hanya berlaku untuk klien Happ.
- **Nama node tidak lagi ditambahkan ke nama profil dalam langganan** — Nama node tidak lagi ditambahkan ke nama profil dalam langganan. Dalam aplikasi klien hanya remark inbound yang ditetapkan administrator yang ditampilkan, tanpa sufiks internal seperti «@nama-node».
- **Label model remark diganti namanya Other → External Proxy (kemudian digantikan template)** — Tidak perlu didokumentasikan secara terpisah: penggantian nama item model remark «Other» menjadi «External Proxy» diserap oleh transisi ke kolom Remark Template baru, di mana pembuat model dari UI dihapus.
- **Ketepatan tautan langganan: SS2022, Shadowrocket, SIP002 obfs, XHTTP di Clash** — Kompatibilitas tautan langganan yang dihasilkan ditingkatkan: diperbaiki encoding SS2022, deep-link untuk Shadowrocket, output Shadowsocks+obfs dalam format SIP002 (plugin obfs-local) dan set lengkap kolom XHTTP dalam langganan Clash/Mihomo. Tidak ada pengaturan terpisah yang diperlukan — tautan cukup lebih tepat dikenali oleh klien.
- **Model remark langganan: item «Other» diganti namanya menjadi «External Proxy»** — Di pengaturan langganan dalam model remark, item **«Other»** diganti namanya menjadi **«External Proxy»** (sumber — remark proksi eksternal). Perilaku tidak berubah, pengaturan yang ada tetap kompatibel.
- **Langganan: pemilihan variabel remark dengan klik pada chip (Remark variable picker)** — Di sebelah kolom Remark Template tersedia kumpulan chip variabel yang dikelompokkan: mengklik variabel {{VAR}} menyisipkannya ke template, saat diarahkan kursor ditampilkan deskripsi. Dalam kolom remark dan nama host, penulisan sederhana dalam tanda kurung tunggal juga diperbolehkan — {DATA_LEFT}, {EXPIRE_DATE}, {PROTOCOL}, {TRANSPORT} dll.; panel secara otomatis mengonversinya ke format internal {{...}}.

### 11. Xray: routing, outbounds, DNS, dan ekstensi
- **Routing dan Outbounds dipindahkan ke item menu samping terpisah** — Mulai versi ini **«Outbounds»** dan **«Routing»** dipindahkan ke item menu samping terpisah (tepat di bawah «Hosts»), masing-masing dengan alamatnya sendiri — `/outbound` dan `/routing`. Sebelumnya routing dibuka di dalam submenu «Konfigurasi Xray», dan outbounds — sebagai tab halaman Xray. Di submenu «Konfigurasi Xray» sekarang hanya tersisa: Utama, Balancer, DNS, dan Template Lanjutan. Tautan langsung ke `/outbound` dan `/routing` serta pemuatan ulang halaman berfungsi seperti yang diharapkan.
- **Aturan routing dapat diaktifkan dan dinonaktifkan dengan sakelar** — Aturan routing individual sekarang dapat sementara **dinonaktifkan** dengan sakelar, tanpa menghapusnya. Di tabel aturan terdapat kolom **«Enable»** dengan sakelar, dalam formulir aturan kolom «Enable» juga merupakan sakelar. Aturan yang dinonaktifkan tidak masuk ke konfigurasi Xray akhir. Aturan layanan statistik (`api`) tidak dapat dinonaktifkan — sakelanya dikunci.
- **Ekspor aturan routing dan outbounds dibuka di jendela modal pratinjau** — Tombol **«Ekspor»** aturan routing dan outbounds sekarang tidak langsung mengunduh file, melainkan membuka jendela modal dengan pratinjau JSON dan tombol **«Salin»** dan **«Unduh»**. Di tab «Routing» «Impor» dan «Ekspor» dikumpulkan dalam menu dropdown **«lainnya»** (seperti di tab Outbounds).
- **Uji semua outbounds sekarang juga memeriksa outbounds dari langganan; direct/dns tidak lagi diuji** — Tombol **«Uji Semua»** di halaman «Outbounds» sekarang juga memeriksa outbounds yang diperoleh dari langganan (tabel «dari langganan») — baris mereka juga disorot dengan hasil. Dalam hal ini, outbounds `freedom` («direct») dan `dns` tidak lagi diuji dalam mode apa pun (ini bukan proksi): tombol uji pada mereka tidak tersedia, dan «Uji Semua» melewatinya.
- **FinalMask: array per-fragmen Lengths/Delays sebagai pengganti Length/Delay tunggal** — Dalam mask fragment (FinalMask), kolom tunggal Length dan Delay digantikan oleh daftar Lengths dan Delays: untuk setiap segmen dapat ditetapkan rentang panjang terpisah (misalnya 100-200) dan penundaan dalam milidetik (misalnya 10-20 atau 0). Baris dapat ditambahkan dan dihapus; nilai yang tersimpan sebelumnya dipindahkan secara otomatis.
- **Loopback outbound: blok Sniffing ditambahkan** — Outbound tipe loopback kini memiliki blok Sniffing dengan parameter yang sama seperti inbound: aktifkan, destOverride, Metadata Only, Route Only, dan daftar domain yang dikecualikan.
- **Hysteria2 / Salamander: mode Gecko (packetSize) dan TLS untuk mask Realm** — Dalam mask UDP (FinalMask) untuk Hysteria2, kemampuan diperluas. Mask Salamander mendapatkan selektor Mode: mode Gecko menambahkan padding paket acak dengan kolom Min/Max ukuran (dari 1 hingga 2048, default 512-1200) untuk perlindungan dari analisis panjang paket. Mask Realm mendapatkan blok TLS Config opsional: Server Name (SNI), ALPN (h3/h2/http/1.1), Fingerprint, dan Allow Insecure.
- **Impor tautan berbagi ke outbound menyimpan pengaturan xmux** — Saat mengimpor outbound dari tautan berbagi, pengaturan multipleksor **xmux** (XHTTP) sekarang disimpan: sebelumnya diam-diam hilang. Setelah impor, nilai dimasukkan ke sub-formulir XMUX.
- **Tag outbounds dari langganan mempertahankan karakter non-ASCII (Cyrillic)** — Tag outbounds yang diperoleh dari langganan sekarang mempertahankan karakter non-ASCII (misalnya, Cyrillic) dan tetap dapat dibaca, bukan hanya terdiri dari angka.

### 12. Node (multipanel, master/slave)
- **Node: mode verifikasi TLS baru — Mutual TLS (sertifikat klien)** — Dalam formulir node, mode verifikasi TLS sekarang memiliki empat opsi: Verify (CA sistem), Pin (penambatan sertifikat berdasarkan SHA-256), Skip (tanpa verifikasi) dan Mutual TLS baru (sertifikat klien). Dalam mode Mutual TLS, panel mengonfirmasi dirinya ke node dengan sertifikat klien yang diterbitkan oleh CA-nya sendiri; token API untuk node tersebut menjadi opsional. Untuk mengaktifkan mTLS: di node, atur mode Mutual TLS, salin CA panel kontrol dari bagian Node mTLS, tetapkan sebagai CA induk tepercaya di node, dan restart node.
- **Node: bagian «Node mTLS» — menyalin CA panel dan CA induk tepercaya** — Di halaman Node, bagian Node mTLS ditambahkan untuk mengonfigurasi mutual TLS antara panel. Tombol «Salin CA panel ini» menyalin sertifikat root panel ke clipboard — perlu diteruskan ke node yang akan dikelola yang akan memverifikasi sertifikat klien panel. Kolom «CA induk tepercaya» digunakan saat panel itu sendiri adalah node: tempel CA panel kontrol di sini untuk meminta sertifikat kliennya, dan restart panel. Mutual TLS diaktifkan secara opsional; jika kolom kosong, node bekerja sesuai skema sebelumnya — hanya dengan token API.
- **Routing koneksi keluar panel ke node (Connection outbound)** — Di formulir node, kolom **«Connection outbound»** (koneksi keluar) ditambahkan. Jika tag Xray-outbound dipilih di dalamnya, lalu lintas panel ke API node tersebut akan melewati outbound yang ditentukan (panel sendiri akan menambahkan bridge-inbound pada loopback ke konfigurasi yang berjalan dan menerapkannya tanpa restart). Nilai kosong = koneksi langsung. Dalam daftar, tag dikelompokkan menjadi «Outbounds» dan «Balancers», outbound blackhole disembunyikan.
- **Node: routing lalu lintas panel→node melalui outbound yang dipilih («Connection outbound»)** — Di formulir node, kolom «Connection outbound» ditambahkan: memungkinkan untuk mengarahkan lalu lintas permintaan panel ke node melalui Xray outbound yang dipilih (outbound biasa dan balancer tersedia). Panel secara otomatis menambahkan loopback-bridge inbound ke konfigurasi yang berjalan dan menerapkan perubahan tanpa restart. Biarkan kolom kosong untuk koneksi langsung.
- **Node: penghapusan node diblokir selama inbounds masih terpaut ke node tersebut** — Node hanya dapat dihapus setelah semua inbounds dilepaskan darinya. Jika setidaknya satu inbound masih terpaut ke node, panel akan menolak penghapusan dengan kesalahan — lepaskan atau hapus inbound tersebut terlebih dahulu, baru kemudian hapus node.
- **Node: kecepatan langsung inbounds yang ditempatkan di node ditampilkan di halaman node** — Di halaman Node, untuk inbounds yang ditempatkan di node, klien online, penghitung, dan kecepatan transfer saat ini sekarang ditampilkan. Chip «selesai» (ended) hanya menghitung klien yang kedaluwarsa dan yang telah habis lalu lintasnya (klien yang dinonaktifkan tidak lagi termasuk).

### 14. Bot Telegram
- **Notifikasi: bus acara baru dengan saluran Telegram dan Email (SMTP)** — Sistem notifikasi berbasis acara ditambahkan dengan dua saluran pengiriman — Telegram dan Email. Di tab notifikasi, acara dikelompokkan dalam kartu: Outbound (jatuh/pulih), Xray Core (penghentian darurat), Nodes (node tidak tersedia/pulih), System (beban CPU dan memori tinggi dengan ambang batas yang dapat dikonfigurasi dalam %), Security (percobaan login). Setiap grup memiliki sakelar master dan penghitung acara yang dipilih. Kumpulan acara yang diaktifkan dapat dikonfigurasi secara terpisah untuk Telegram dan Email; secara default «percobaan login» dan «beban CPU tinggi» diaktifkan.
- **Notifikasi: saluran Email/SMTP baru dan pengaturan server SMTP** — Saluran notifikasi baru melalui email menggunakan SMTP ditambahkan. Di tab pengaturan SMTP dikonfigurasi: aktifkan notifikasi email, host dan port SMTP (default 587), nama pengguna, kata sandi (disimpan tersembunyi), daftar penerima (dipisahkan koma) dan jenis enkripsi — none, STARTTLS (default) atau TLS. Tombol «Kirim email uji» memeriksa koneksi dan menunjukkan tahap mana (koneksi, autentikasi, pengiriman) yang mengalami kesalahan. Di tab kedua, acara yang akan dikirimkan pemberitahuan emailnya dipilih.
- **Notifikasi: peringatan beban memori tinggi (ambang batas RAM)** — Peringatan beban RAM tinggi ditambahkan ke peringatan beban CPU tinggi. Di grup acara «System» muncul «Memory high (%)» dengan kolom ambang batas sendiri (default 80%); panel setiap menit memeriksa beban RAM dan ketika ambang batas terlampaui, mengirimkan notifikasi ke saluran yang dipilih.

### 15. Basis geo (geoip / geosite dan kustom)
- **Pembaruan basis geo: status per file dan lewati restart jika tidak ada perubahan** — Pembaruan basis geo (geoip/geosite, termasuk set IR dan RU) sekarang menampilkan status per file: diperbarui, sudah terkini, atau kesalahan unduhan. Restart Xray (dan karenanya terputusnya koneksi aktif) hanya terjadi jika setidaknya satu file benar-benar diperbarui; jika tidak ada perubahan, panel tidak di-restart. Perilaku yang sama berlaku untuk perintah x-ui update-all-geofiles.

### 16. Pengoperasian: cadangan, log, pembaruan, CLI
- **Batas IP klien hanya berfungsi jika fail2ban terpasang; kolom diblokir jika tidak ada** — Pembatasan jumlah IP pada klien sekarang hanya berlaku jika fail2ban terpasang di server. Jika tidak ada, kolom «IP Limit» dalam formulir klien dan saat penambahan massal menjadi tidak tersedia dengan tooltip penjelasan (di Windows — pesan terpisah), dan batas yang sebelumnya ditetapkan pada server tersebut secara otomatis diatur ulang ke nol, karena memang tidak diterapkan. Pemblokiran fail2ban sekarang berlaku untuk TCP dan UDP.
- **Instalasi fail2ban otomatis saat instalasi dan pembaruan panel** — Saat menginstal dan memperbarui panel di server biasa, fail2ban sekarang dipasang dan dikonfigurasi secara otomatis (sebelumnya ini hanya terjadi di Docker), agar fitur batas IP berfungsi sejak awal. Perilakunya dikendalikan oleh variabel lingkungan XUI_ENABLE_FAIL2BAN: konfigurasi dilakukan jika variabel tidak ditetapkan atau bernilai true. Peluncuran manual tersedia dengan perintah x-ui setup-fail2ban; kesalahan fail2ban tidak menghentikan instalasi atau pembaruan.
- **Penggantian port panel melalui variabel XUI_PORT** — Variabel lingkungan XUI_PORT ditambahkan, yang menetapkan port panel web hanya selama proses saat ini berjalan, tanpa mengubah nilai webPort yang tersimpan di basis data. Nilai yang valid adalah 1 hingga 65535; nilai kosong, salah, atau di luar rentang diabaikan (webPort digunakan) dengan peringatan di log. Saat menggunakan Docker dengan jaringan bridge, port kontainer yang dipublikasikan harus cocok dengan XUI_PORT, misalnya XUI_PORT=8080 dan ports: «8080:8080».
- **CLI: flag -webCert/-webCertKey sekarang diterapkan dalam subperintah setting** — Dalam CLI, flag -webCert dan -webCertKey sekarang berfungsi dalam subperintah x-ui setting (sebelumnya diam-diam diabaikan dan panel tetap tanpa HTTPS). Dengan menentukannya, Anda dapat langsung menetapkan path ke sertifikat dan kunci panel web tanpa memanggil subperintah cert secara terpisah.
- **Nama file cadangan basis data dibentuk berdasarkan alamat server** — File cadangan basis data sekarang diberi nama berdasarkan alamat server, bukan x-ui.db / x-ui.dump yang tetap. Saat mengunduh dari browser, nama diambil dari alamat panel di bilah alamat, atau dari domain web yang dikonfigurasi, atau jika tidak ada — dari IP publik (IPv4 terlebih dahulu, kemudian IPv6). Dengan cara ini cadangan dari server yang berbeda mudah dibedakan. Ekstensi tetap .db untuk SQLite dan .dump untuk PostgreSQL.
- **Dukungan instalasi dan pembaruan di host hanya dengan IPv6** — Skrip instalasi dan pembaruan sekarang bekerja dengan benar di server yang hanya memiliki IPv6: pengunduhan rilis dan file pembantu tidak lagi memaksa penggunaan IPv4, sehingga panel dapat dipasang dan diperbarui di host tanpa alamat IPv4.

## 1. Pendahuluan, Persyaratan, dan Instalasi

### 1.1. Apa itu 3X-UI

**3X-UI** adalah panel manajemen web sumber terbuka untuk server [Xray-core](https://github.com/XTLS/Xray-core). Panel ini menyediakan antarmuka web multibahasa terpadu untuk men-deploy, mengonfigurasi, dan memantau berbagai protokol proksi dan VPN: mulai dari satu VPS hingga konfigurasi terdistribusi yang terdiri dari beberapa node.

3X-UI adalah fork lanjutan dari proyek X-UI asli. Dibandingkan dengan pendahulunya, versi ini menambahkan dukungan untuk lebih banyak protokol, stabilitas yang lebih baik, pencatatan lalu lintas per klien, dan berbagai fitur yang memudahkan pengelolaan.

Fitur utama:

- **Inbound dengan berbagai protokol** — VLESS, VMess, Trojan, Shadowsocks, WireGuard, Hysteria2, HTTP, SOCKS (Mixed), Dokodemo-door / Tunnel, TUN, dan **MTProto** (proksi Telegram, ditambahkan di versi 3.3.0).
- **Transport dan enkripsi modern** — TCP (Raw), mKCP, WebSocket, gRPC, HTTPUpgrade, dan XHTTP, dilindungi dengan TLS, XTLS, dan REALITY.
- **Fallback** — melayani beberapa protokol pada satu port (misalnya VLESS dan Trojan di port 443) menggunakan mekanisme fallback di Xray.
- **Manajemen per klien** — kuota lalu lintas, tanggal kedaluwarsa, batas IP, tampilan status "online", tautan undangan satu klik, kode QR, dan langganan.
- **Statistik lalu lintas** — per inbound, per klien, dan per outbound, dengan kemampuan reset.
- **Dukungan multi-node** — manajemen dan penskalaan ke beberapa server dari satu panel.
- **Outbound dan routing** — WARP, NordVPN, aturan routing kustom, load balancer, rantai proksi.
- **Server langganan bawaan** dengan beberapa format output.
- **Bot Telegram** untuk pemantauan dan manajemen jarak jauh.
- **REST API** dengan dokumentasi Swagger bawaan.
- **Penyimpanan fleksibel** — SQLite (default) atau PostgreSQL.
- **13 bahasa antarmuka**, tema gelap dan terang.
- **Integrasi dengan Fail2ban** untuk menerapkan batas IP per klien.

> Penting: proyek ini ditujukan hanya untuk penggunaan pribadi. Tidak disarankan untuk digunakan dalam tujuan ilegal atau lingkungan produksi.

### 1.2. Sistem Operasi dan Arsitektur yang Didukung

#### Sistem Operasi

Skrip instalasi mendeteksi distribusi berdasarkan kolom `ID` dari `/etc/os-release` (atau `/usr/lib/os-release`). Yang didukung secara resmi:

Ubuntu, Debian, Armbian, Fedora, CentOS, RHEL, AlmaLinux, Rocky Linux, Oracle Linux, Amazon Linux, Virtuozzo, Arch, Manjaro, Parch, openSUSE (Tumbleweed / Leap), Alpine, serta Windows.

Pada sistem berbasis Alpine, digunakan layanan OpenRC (`rc-service` / `rc-update`), sedangkan pada sistem lainnya digunakan systemd. Untuk CentOS 7, paket diinstal melalui `yum`; untuk versi yang lebih baru menggunakan `dnf`. Jika distribusi tidak dikenali, skrip secara default mencoba menggunakan manajer paket `apt-get`.

#### Arsitektur Prosesor

Arsitektur dideteksi berdasarkan output `uname -m` dan dipetakan ke salah satu nilai yang didukung:

| Nilai `uname -m` | Arsitektur 3X-UI |
| --- | --- |
| `x86_64`, `x64`, `amd64` | `amd64` |
| `i*86`, `x86` | `386` |
| `armv8*`, `arm64`, `aarch64` | `arm64` |
| `armv7*`, `arm` | `armv7` |
| `armv6*` | `armv6` |
| `armv5*` | `armv5` |
| `s390x` | `s390x` |

Jika arsitektur tidak termasuk dalam daftar ini, skrip akan menampilkan pesan "Unsupported CPU architecture!" dan menghentikan instalasi.

#### Dependensi Dasar

Sebelum menginstal panel, skrip secara otomatis menginstal sekumpulan paket dasar (nama paket bervariasi tergantung distribusi): `cron`/`cronie`/`dcron`, `curl`, `tar`, `tzdata`/`timezone`, `socat`, `ca-certificates`, `openssl`.

### 1.3. Metode Instalasi

#### Metode 1. Skrip Instalasi (Direkomendasikan)

Instalasi dilakukan dengan satu perintah sebagai root:

```bash
bash <(curl -Ls https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh)
```

Skrip memerlukan hak root: jika dijalankan bukan sebagai root, akan muncul pesan "Please run this script with root privilege" dan proses akan berhenti dengan error.

Langkah-langkah yang dilakukan penginstal:

1. Mendeteksi OS dan arsitektur.
2. Menginstal dependensi dasar.
3. Mengunduh arsip rilis `x-ui-linux-<arch>.tar.gz` dan mengekstraknya ke direktori `/usr/local/x-ui`.
4. Mengunduh skrip manajemen `x-ui.sh` dan menginstalnya sebagai perintah `/usr/bin/x-ui`.
5. Membuat direktori log `/var/log/x-ui`.
6. Menjalankan konfigurasi awal: pemilihan database, pembuatan kredensial, pemilihan port, konfigurasi SSL opsional.
7. Menginstal dan menjalankan layanan autostart (unit systemd `x-ui.service` atau skrip init OpenRC untuk Alpine).

**Pemilihan database saat instalasi.** Penginstal menawarkan pilihan:

- `1) SQLite` (default, direkomendasikan jika jumlah klien < 500) — satu file `/etc/x-ui/x-ui.db`, tidak memerlukan konfigurasi tambahan.
- `2) PostgreSQL` (direkomendasikan untuk jumlah klien yang besar atau beberapa node). PostgreSQL dapat diinstal secara lokal (pengguna dan database khusus bernama `xui` akan dibuat) atau Anda dapat menentukan DSN ke server yang sudah ada. Parameter koneksi ditulis ke file environment layanan (`/etc/default/x-ui`, `/etc/conf.d/x-ui`, atau `/etc/sysconfig/x-ui` tergantung distribusi) dalam bentuk variabel `XUI_DB_TYPE` dan `XUI_DB_DSN`.

**Contoh: penulisan parameter PostgreSQL ke file environment layanan.** Setelah memilih PostgreSQL dan menentukan DSN, penginstal akan menambahkan baris seperti ini ke file environment:

```bash
XUI_DB_TYPE=postgres
XUI_DB_DSN=postgres://xui:S3cretPass@127.0.0.1:5432/xui?sslmode=disable
```

Di sini `xui` adalah nama pengguna dan database, `127.0.0.1:5432` adalah alamat dan port server, `sslmode=disable` cocok untuk koneksi lokal (untuk server jarak jauh biasanya digunakan `require`).

**Instalasi versi tertentu (lama).** Anda dapat menentukan tag versi secara eksplisit — penginstal akan mengunduh rilis yang sesuai:

```bash
bash <(curl -Ls https://raw.githubusercontent.com/mhsanaei/3x-ui/v2.4.0/install.sh) v2.4.0
```

Versi minimum yang diizinkan untuk instalasi semacam ini adalah `v2.3.5`; jika versi yang lebih lama ditentukan, akan muncul pesan "Please use a newer version (at least v2.3.5)".

#### Metode 2. Docker

Menjalankan dengan database SQLite default:

```bash
docker compose up -d
```

Untuk menjalankan dengan layanan PostgreSQL bawaan, uncomment baris `XUI_DB_*` di `docker-compose.yml` dan jalankan dengan profil:

```bash
docker compose --profile postgres up -d
```

Image mencakup Fail2ban (aktif secara default) untuk menerapkan batas IP per klien. Fail2ban memblokir pelanggar melalui `iptables`, yang memerlukan kapabilitas `NET_ADMIN`. Dalam `docker-compose.yml`, kapabilitas ini sudah diberikan melalui `cap_add`. Saat menjalankan secara manual dengan `docker run`, kapabilitas perlu ditambahkan secara manual, jika tidak blokiran hanya akan dicatat dalam log tetapi tidak diterapkan:

**Contoh: perintah `docker run` lengkap.** Versi minimal dengan penerusan port panel, kapabilitas jaringan, dan volume persisten untuk database:

```bash
docker run -d \
  --name 3x-ui \
  --restart unless-stopped \
  --cap-add=NET_ADMIN --cap-add=NET_RAW \
  -v $PWD/db:/etc/x-ui \
  -v $PWD/cert:/root/cert \
  -p 2053:2053 \
  ghcr.io/mhsanaei/3x-ui:latest
```

Volume `/etc/x-ui` menyimpan file `x-ui.db` antara restart container; tanpanya, pengaturan dan akun akan hilang.

```bash
docker run -d --cap-add=NET_ADMIN --cap-add=NET_RAW ... ghcr.io/mhsanaei/3x-ui
```

Di Docker, panel adalah proses utama container: autostart diatur oleh kebijakan restart container (misalnya `restart: unless-stopped`), bukan oleh layanan di dalam container.

### 1.4. Peluncuran Pertama dan Kredensial Default

Pada instalasi pertama (ketika kredensial default masih digunakan), penginstal **menghasilkan nilai acak** untuk nama pengguna, kata sandi, web path, dan port:

| Parameter | Cara pembuatan saat instalasi | Catatan |
| --- | --- | --- |
| Nama pengguna (Username) | string acak 10 karakter | dibuat secara otomatis |
| Kata sandi (Password) | string acak 10 karakter | dibuat secara otomatis |
| Web path panel (WebBasePath) | string acak 18 karakter | melindungi panel dari deteksi melalui URL root |
| Port panel (Port) | secara default port acak dalam rentang 1024–62000; dapat ditentukan secara manual jika diinginkan | nilai "bawaan pabrik" `webPort` adalah `2053`, tetapi penginstal menimpanya |

Di akhir instalasi, skrip menampilkan ringkasan: nama pengguna, kata sandi, port, web path, token API, dan tautan akses siap pakai (Access URL) dalam format:

```
https://<domain-atau-IP>:<port>/<web-path>
```

Jika sertifikat SSL belum dikonfigurasi, tautan akan menggunakan `http://` dan skrip akan menampilkan peringatan tentang perlunya mengonfigurasi SSL (item menu 19).

> Penggantian kredensial wajib. Karena login dan kata sandi dibuat secara acak, **simpanlah segera setelah instalasi**. Anda dapat menggantinya kapan saja melalui item menu "Reset Username & Password" (lihat di bawah) atau dari antarmuka web di pengaturan panel. Setelah reset, skrip mengingatkan: "Please use the new login username and password to access the X-UI panel. Also remember them!".

Setelah instalasi, gunakan perintah `x-ui` untuk membuka menu manajemen (lihat bagian 1.6).

### 1.5. Lokasi File

| Path | Fungsi |
| --- | --- |
| `/usr/local/x-ui/` | direktori instalasi panel (binary `x-ui`, skrip `x-ui.sh`) |
| `/usr/local/x-ui/bin/xray-linux-<arch>` | binary Xray-core (pada armv5/armv6/armv7 diganti namanya menjadi `xray-linux-arm`) |
| `/usr/bin/x-ui` | skrip manajemen (perintah `x-ui`) |
| `/etc/x-ui/x-ui.db` | file database SQLite (default) |
| `/var/log/x-ui/` | direktori log panel |
| `/etc/systemd/system/x-ui.service` | unit systemd layanan (bukan untuk Alpine) |
| `/etc/init.d/x-ui` | skrip init OpenRC (hanya Alpine) |
| `/etc/default/x-ui` · `/etc/conf.d/x-ui` · `/etc/sysconfig/x-ui` | file variabel environment layanan (path tergantung distribusi); tempat penulisan `XUI_DB_TYPE`/`XUI_DB_DSN` |

Direktori database dapat diubah melalui variabel environment `XUI_DB_FOLDER` (default `/etc/x-ui`), dan direktori binary Xray melalui variabel `XUI_BIN_FOLDER` (default `bin` relatif terhadap direktori panel). Nama file database adalah `x-ui.db`.

**Contoh: memindahkan database ke disk terpisah.** Untuk menyimpan `x-ui.db` bukan di `/etc/x-ui` melainkan, misalnya, di disk yang di-mount di `/data`, tentukan variabel di file environment layanan dan restart panel:

```bash
echo 'XUI_DB_FOLDER=/data/x-ui' >> /etc/default/x-ui
mkdir -p /data/x-ui
systemctl restart x-ui
```

Path lengkap ke database akan menjadi `/data/x-ui/x-ui.db`.

#### Variabel Environment Utama

| Variabel | Fungsi | Default |
| --- | --- | --- |
| `XUI_DB_TYPE` | backend database: `sqlite` atau `postgres` | `sqlite` |
| `XUI_DB_DSN` | string koneksi PostgreSQL (saat `XUI_DB_TYPE=postgres`) | — |
| `XUI_DB_FOLDER` | direktori file database SQLite | `/etc/x-ui` |
| `XUI_INIT_WEB_BASE_PATH` | URI path awal panel web (hanya saat inisialisasi pertama) | `/` |
| `XUI_DB_MAX_OPEN_CONNS` | jumlah maksimum koneksi yang terbuka (pool PostgreSQL) | — |
| `XUI_DB_MAX_IDLE_CONNS` | jumlah maksimum koneksi idle (pool PostgreSQL) | — |
| `XUI_ENABLE_FAIL2BAN` | mengaktifkan penerapan batas IP melalui Fail2ban | `true` |
| `XUI_LOG_LEVEL` | level logging (`debug`, `info`, `warning`, `error`) | `info` |
| `XUI_DEBUG` | mode debug | `false` |

**Contoh: mengaktifkan logging detail sementara.** Untuk mendiagnosis masalah, naikkan level log ke `debug` dan restart layanan:

```bash
echo 'XUI_LOG_LEVEL=debug' >> /etc/default/x-ui
systemctl restart x-ui
x-ui log    # melihat log debug
```

Setelah diagnosis selesai, kembalikan ke nilai `info` agar log tidak membengkak.

**Path awal panel web melalui environment.** Variabel `XUI_INIT_WEB_BASE_PATH` menentukan URI path panel web (`webBasePath`) saat inisialisasi pengaturan pertama kali. Ini berguna saat men-deploy di Docker atau melalui systemd untuk langsung menetapkan path login ke panel. Nilai dinormalisasi secara otomatis — slash awal dan akhir ditambahkan jika diperlukan, dan nilai kosong atau yang hanya terdiri dari spasi diabaikan (dalam hal ini path default `/` yang digunakan). Variabel ini **hanya memengaruhi inisialisasi pertama**: jika pengaturan sudah ada, path diubah melalui antarmuka web atau item menu "Reset Web Base Path".

### 1.6. Perintah Manajemen `x-ui` (Menu Skrip)

Setelah instalasi, perintah `x-ui` (dijalankan sebagai root) membuka menu interaktif "3X-UI Panel Management Script". Item menu dipilih dengan memasukkan nomornya (rentang 0–27). Banyak item juga tersedia sebagai subperintah untuk keperluan skrip (lihat bagian 1.7).

Menu dibagi menjadi beberapa blok tematik.

#### Instalasi dan Pembaruan

- **1. Install** — instalasi panel (menjalankan `install.sh`). Sebelum instalasi, diperiksa apakah panel belum terinstal.
- **2. Update** — memperbarui semua komponen x-ui ke versi terbaru. Data tidak akan hilang; setelah pembaruan, panel di-restart secara otomatis. Memerlukan konfirmasi.
- **3. Update Menu** — memperbarui hanya skrip manajemen (`x-ui.sh` / perintah `x-ui`) ke versi terbaru tanpa menginstal ulang panel.
- **4. Legacy Version** — menginstal versi panel tertentu (lama). Skrip meminta nomor versi (misalnya `2.4.0`) dan mengunduh rilis yang sesuai.
- **5. Uninstall** — menghapus panel **beserta Xray** sepenuhnya. Layanan dihentikan dan dinonaktifkan, direktori `/etc/x-ui/` dan `/usr/local/x-ui/` dihapus, beserta file environment layanan dan skrip manajemen itu sendiri. Memerlukan konfirmasi (default "tidak").

#### Kredensial dan Pengaturan

- **6. Reset Username & Password** — mereset nama pengguna dan kata sandi panel. Anda dapat memasukkan nilai sendiri atau membiarkannya kosong untuk pembuatan acak (nama acak 10 karakter, kata sandi acak 18 karakter). Juga menawarkan opsi untuk menonaktifkan autentikasi dua faktor (2FA) jika dikonfigurasi. Setelah reset, panel di-restart.
- **7. Reset Web Base Path** — mereset web path panel: path acak baru dibuat (18 karakter) dan panel di-restart. Digunakan jika path sebelumnya dikompromikan atau terlupakan.
- **8. Reset Settings** — mereset semua pengaturan panel ke nilai default. **Kredensial (nama pengguna dan kata sandi) serta data akun tidak akan hilang.** Memerlukan konfirmasi; setelah reset, panel di-restart.
- **9. Change Port** — mengubah port panel web. Nomor port diminta (1–65535); setelah diatur, restart diperlukan agar port berlaku.
- **10. View Current Settings** — melihat pengaturan saat ini (`x-ui setting -show`). Menampilkan backend database yang digunakan (SQLite atau PostgreSQL dengan kata sandi ter-mask dalam DSN) dan tautan akses siap pakai (Access URL). Jika SSL belum dikonfigurasi, menawarkan untuk menerbitkan sertifikat Let's Encrypt untuk alamat IP.

#### Manajemen Layanan

- **11. Start** — menjalankan layanan panel. Jika panel sudah berjalan, ditampilkan pesan bahwa restart tidak diperlukan.
- **12. Stop** — menghentikan layanan panel.
- **13. Restart** — me-restart layanan panel.
- **14. Restart Xray** — me-restart hanya inti Xray-core tanpa me-restart panel itu sendiri (melalui `systemctl reload x-ui`, di Docker menggunakan sinyal `USR1` ke proses panel).
- **15. Check Status** — memeriksa status layanan (`systemctl status x-ui` atau `rc-service x-ui status`).
- **16. Logs Management** — manajemen log: melihat log debug (Debug Log, melalui `journalctl`) dan, kecuali Alpine, menghapus semua log (Clear All logs).

#### Autostart

- **17. Enable Autostart** — mengaktifkan autostart panel saat OS boot (`systemctl enable x-ui` atau `rc-update add`).
- **18. Disable Autostart** — menonaktifkan autostart saat OS boot.

Di Docker, autostart diatur oleh kebijakan restart container, sehingga item-item ini hanya menampilkan petunjuk yang relevan.

#### Keamanan dan Jaringan

- **19. SSL Certificate Management** — manajemen sertifikat SSL melalui acme.sh: penerbitan sertifikat untuk domain, pencabutan, pembaruan paksa, melihat domain yang ada, menentukan path sertifikat untuk panel, serta penerbitan sertifikat berumur pendek (~6 hari, dengan pembaruan otomatis) untuk alamat IP.
- **20. Cloudflare SSL Certificate** — penerbitan sertifikat SSL melalui validasi DNS Cloudflare.
- **21. IP Limit Management** — manajemen batas jumlah IP per klien (berbasis Fail2ban): melihat dan menghapus blokiran, dll.
- **22. Firewall Management** — manajemen firewall (membuka/menutup port dan melihat aturan).
- **23. SSH Port Forwarding Management** — konfigurasi penerusan port SSH untuk membuka panel dari mesin lokal melalui tunnel SSH.

#### Performa dan Pemeliharaan

- **24. Enable BBR** — mengaktifkan/menonaktifkan algoritma kontrol kemacetan TCP BBR (submenu dengan item Enable BBR / Disable BBR).
- **25. Update Geo Files** — memperbarui database geo (file `.dat`) dengan pemilihan sumber: Loyalsoldier (`geoip.dat`, `geosite.dat`), chocolate4u (`geoip_IR.dat`, `geosite_IR.dat`), runetfreedom (`geoip_RU.dat`, `geosite_RU.dat`), atau All (semua sekaligus). Setelah pembaruan, panel di-restart.
- **26. Speedtest by Ookla** — menjalankan uji kecepatan jaringan melalui Speedtest by Ookla.
- **27. PostgreSQL Management** — manajemen instans PostgreSQL bawaan/terhubung (aktivasi dan operasi terkait).
- **0. Exit Script** — keluar dari menu.

### 1.7. Subperintah `x-ui` (Tanpa Menu Interaktif)

Untuk digunakan dalam skrip, perintah `x-ui` mendukung subperintah langsung (menjalankan `x-ui` tanpa argumen akan membuka menu):

| Perintah | Tindakan |
| --- | --- |
| `x-ui` | membuka menu manajemen |
| `x-ui start` | menjalankan panel |
| `x-ui stop` | menghentikan panel |
| `x-ui restart` | me-restart panel |
| `x-ui restart-xray` | me-restart Xray |
| `x-ui status` | status layanan saat ini |
| `x-ui settings` | pengaturan saat ini |
| `x-ui enable` | mengaktifkan autostart saat OS boot |
| `x-ui disable` | menonaktifkan autostart |
| `x-ui log` | melihat log |
| `x-ui banlog` | melihat log blokiran Fail2ban |
| `x-ui update` | memperbarui panel |
| `x-ui update-all-geofiles` | memperbarui semua file geo |
| `x-ui migrateDB [file]` | konversi `.db` ↔ `.dump` (SQLite) |
| `x-ui legacy` | menginstal versi lama |
| `x-ui install` | menginstal panel |
| `x-ui uninstall` | menghapus panel |

### 1.8. Migrasi SQLite → PostgreSQL

Instalasi yang ada pada SQLite dapat dimigrasikan ke PostgreSQL:

```bash
x-ui migrate-db --dsn "postgres://xui:password@127.0.0.1:5432/xui?sslmode=disable"
# kemudian tentukan XUI_DB_TYPE dan XUI_DB_DSN di /etc/default/x-ui dan restart:
systemctl restart x-ui
```

File SQLite asli tetap tidak tersentuh — hapus secara manual hanya setelah memverifikasi bahwa backend baru berfungsi dengan benar.

**Contoh: memverifikasi peralihan ke PostgreSQL.** Setelah migrasi, pastikan panel benar-benar berjalan di backend baru dengan perintah melihat pengaturan — output harus menunjukkan PostgreSQL (kata sandi dalam DSN ter-mask):

```bash
x-ui settings | grep -i -E 'db|dsn'
```

Jika panel terbuka dan akun masih ada, `x-ui.db` asli dapat dihapus.

---

## 2. Login Panel dan Keamanan Akses

Bagian ini menjelaskan semua hal yang berkaitan dengan autentikasi administrator panel 3X-UI: formulir login, autentikasi dua faktor (TOTP), perlindungan dari serangan brute-force, penggantian kredensial, perubahan jalur rahasia dan port panel, masa aktif sesi, serta sinkronisasi/autentikasi melalui LDAP.

### 2.1. Formulir Login

Halaman login disajikan di root jalur rahasia panel (`webBasePath`). Jika pengguna sudah terautentikasi, ia akan secara otomatis diarahkan ke `…/panel/`. Halaman ini memiliki pengalih tema, pemilih bahasa antarmuka, dan formulir login itu sendiri.

Kolom formulir:

| Kolom | Label/Judul | Wajib diisi | Deskripsi |
|-------|-------------|-------------|-----------|
| Username | «Username» | Ya | Login administrator. Nilai kosong ditolak di sisi klien, dan di sisi server dengan pesan «Username wajib diisi». |
| Password | «Password» | Ya | Kata sandi administrator. Nilai kosong ditolak dengan pesan «Password wajib diisi». |
| Kode 2FA | «Kode 2FA» | Hanya jika 2FA diaktifkan | Kolom ini muncul **hanya** jika autentikasi dua faktor diaktifkan di panel. Kode 6 digit dari aplikasi autentikator. |

Tombol **«Login»** mengirimkan formulir ke `POST /login`.

Perilaku dan pesan:

- Jika login berhasil, ditampilkan pesan «Login berhasil» dan pengguna diarahkan ke `…/panel/`.
- Jika ada kesalahan kredensial atau kode 2FA yang salah, server mengembalikan **satu** pesan yang sama: «Nama pengguna, kata sandi, atau kode dua faktor tidak valid.» (bahasa Inggris: *Invalid username or password or two-factor code.*). Ini dilakukan dengan sengaja — panel tidak memberi tahu apa yang salah (login, kata sandi, atau kode) agar tidak memudahkan serangan brute-force.
- Kolom «Kode 2FA» ditampilkan atau disembunyikan panel berdasarkan permintaan `POST /getTwoFactorEnable`, yang mengembalikan status 2FA saat ini sebelum autentikasi.
- Jika sesi server telah kedaluwarsa, pada permintaan berikutnya akan ditampilkan «Sesi telah kedaluwarsa. Silakan login kembali», dan pengguna diarahkan ke halaman login.

> Catatan tentang CSRF: sebelum mengirimkan formulir, klien mendapatkan token CSRF (`GET /csrf-token`); permintaan `/login` dan `/logout` dilindungi oleh pemeriksaan CSRF.

**Contoh: login melalui API.** Jika 2FA dinonaktifkan, cukup gunakan username dan password; jika 2FA diaktifkan, tambahkan kolom `twoFactorCode`:

```bash
# Tanpa 2FA
curl -i -X POST https://panel.example.com:2053/мой-секрет/login \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data 'username=admin&password=ВашПароль'

# Dengan 2FA diaktifkan — tambahkan kode 6 digit
curl -i -X POST https://panel.example.com:2053/мой-секрет/login \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data 'username=admin&password=ВашПароль&twoFactorCode=123456'
```

Jika berhasil, server akan mengembalikan `Set-Cookie` dengan cookie sesi — cookie ini perlu disertakan dalam permintaan berikutnya ke `/panel/api/…`.

### 2.2. Autentikasi Dua Faktor (2FA / TOTP)

2FA di 3X-UI diimplementasikan sesuai standar **TOTP** dan kompatibel dengan aplikasi autentikator apa pun (Google Authenticator, Aegis, FreeOTP, dan sejenisnya). Parameter ditetapkan secara tetap: algoritma **SHA1**, **6** digit, periode **30** detik, issuer `3x-ui`, label `Administrator`.

**Contoh: URI otpauth yang dikodekan dalam kode QR.** Jika aplikasi autentikator tidak dapat memindai kamera, token dapat ditambahkan secara manual menggunakan tautan berikut (ganti `JBSWY3DPEHPK3PXP` dengan rahasia Base32 Anda):

```
otpauth://totp/3x-ui:Administrator?secret=JBSWY3DPEHPK3PXP&issuer=3x-ui&algorithm=SHA1&digits=6&period=30
```

Parameter `algorithm=SHA1`, `digits=6`, `period=30` sesuai dengan nilai tetap panel — tidak perlu mengubahnya.

Pengaturan terdapat di bagian **Pengaturan → Akun**, tab **«Autentikasi Dua Faktor»**.

| Elemen | Teks | Deskripsi |
|--------|------|-----------|
| Toggle | «Aktifkan 2FA» | Mengaktifkan/menonaktifkan autentikasi dua faktor. |
| Deskripsi | «Menambahkan lapisan autentikasi tambahan untuk meningkatkan keamanan.» | Petunjuk di bawah toggle. |

#### Cara Mengaktifkan 2FA

Saat toggle diaktifkan, panel **menghasilkan rahasia baru secara lokal** — string acak dalam encoding Base32 (alfabet `A–Z` dan `2–7`). Jendela «Aktifkan Autentikasi Dua Faktor» akan terbuka dengan panduan langkah demi langkah:

1. **«Pindai kode QR ini di aplikasi autentikator atau salin token di sebelah kode QR dan tempelkan ke aplikasi»**. Di bawah kode QR, rahasia ditampilkan dalam bentuk teks — dengan mengklik kode QR, rahasia disalin ke clipboard (muncul pesan «Disalin»).
2. **«Masukkan kode dari aplikasi»** — perlu memasukkan kode 6 digit yang dihasilkan aplikasi. Kode diverifikasi **di sisi browser**: panel sendiri menghitung TOTP saat ini berdasarkan rahasia yang baru dihasilkan dan membandingkannya dengan kode yang dimasukkan. Jika kode salah — «Kode tidak valid»; kolom hanya menerima tepat 6 digit.

Hanya setelah konfirmasi berhasil, rahasia dan flag aktivasi disimpan. Setelah disimpan, ditampilkan pesan «Autentikasi dua faktor berhasil diaktifkan».

Penting: perubahan di bagian pengaturan diterapkan dengan tombol umum **«Simpan»**, setelah itu biasanya diperlukan restart panel («Simpan perubahan dan restart panel untuk menerapkannya»). Saat 2FA pertama kali diaktifkan, server juga akan **menginvalidasi semua sesi aktif** (menaikkan «login epoch»), sehingga setelah menerapkan pengaturan, login ulang diperlukan — kali ini dengan kode 2FA.

#### Cara Menonaktifkan 2FA

Menekan toggle kembali akan membuka jendela «Nonaktifkan Autentikasi Dua Faktor» dengan petunjuk «Masukkan kode dari aplikasi untuk menonaktifkan autentikasi dua faktor.». Setelah memasukkan kode yang benar, flag dan rahasia dihapus, dan ditampilkan pesan «Autentikasi dua faktor berhasil dihapus».

#### Verifikasi Kode saat Login

Saat login, server mengambil rahasia yang tersimpan dan membandingkan TOTP saat ini dengan kode 2FA yang dikirimkan. Ketidakcocokan dianggap sebagai login yang gagal, namun pengguna melihat pesan terpadu yang sama «Nama pengguna, kata sandi, atau kode dua faktor tidak valid.».

#### Pemulihan Akses (recovery)

3X-UI **tidak** memiliki mekanisme «kode pemulihan» tersendiri. Jika akses ke aplikasi autentikator hilang, pemulihan login melalui antarmuka panel tidak dapat dilakukan. Satu-satunya cara adalah menonaktifkan 2FA langsung di database di server: setel kunci `twoFactorEnable` menjadi `false` (dan jika perlu hapus `twoFactorToken`) di tabel pengaturan, lalu restart panel. Oleh karena itu, disarankan untuk menyimpan rahasia (token Base32) di tempat yang aman saat mengaktifkan 2FA.

**Contoh: menonaktifkan 2FA secara darurat di server.** Setelah mendapatkan akses ke server melalui SSH, hentikan panel, setel ulang kunci di tabel pengaturan, dan jalankan panel kembali:

```bash
x-ui stop
sqlite3 /etc/x-ui/x-ui.db "UPDATE settings SET value='false' WHERE key='twoFactorEnable';"
sqlite3 /etc/x-ui/x-ui.db "UPDATE settings SET value='' WHERE key='twoFactorToken';"
x-ui start
```

Setelah itu, login dilakukan hanya dengan username dan password, dan 2FA dapat dikonfigurasi ulang jika diperlukan.

> Kaitan dengan penggantian kredensial: saat mengganti username/password (lihat 2.4), 2FA **secara otomatis dinonaktifkan** di server, agar rahasia lama tidak memblokir akses dengan akun baru.

### 2.3. Pembatasan Percobaan Login (login limiter / perlindungan brute-force)

Panel memiliki pembatas percobaan login gagal bawaan (setara fail2ban pada level aplikasi). Parameter ditetapkan dalam kode dan **tidak dapat dikonfigurasi** melalui antarmuka:

| Parameter | Nilai | Fungsi |
|-----------|-------|--------|
| Maksimum kegagalan | **5** | Berapa banyak percobaan gagal yang diizinkan dalam satu jendela. |
| Jendela perhitungan | **5 menit** | Jendela geser tempat kegagalan terakumulasi (yang lebih lama dibuang). |
| Durasi blokir (cooldown) | **15 menit** | Berapa lama kunci diblokir setelah melebihi ambang batas. |

Cara kerjanya:

- Kunci blokir dibentuk dari **pasangan «IP + username»** (username diubah ke huruf kecil, spasi dipangkas). Artinya, blokir diterapkan pada pasangan alamat + nama pengguna tertentu, bukan pada seluruh panel.
- Setiap percobaan gagal (username/password salah atau kode 2FA salah) menaikkan penghitung. Setelah mencapai **5** kegagalan dalam **5 menit**, kunci diblokir selama **15 menit**. Selama pemblokiran, setiap percobaan dari pasangan tersebut langsung ditolak dengan pesan yang sama «Nama pengguna, kata sandi, atau kode dua faktor tidak valid.», meskipun datanya benar.
- **Login yang berhasil langsung mereset** penghitung dan mencabut blokir untuk pasangan tersebut.
- Alamat IP klien ditentukan dengan mempertimbangkan proxy tepercaya (lihat `trustedProxyCIDRs`): header `X-Real-IP` dan `X-Forwarded-For` diterima hanya jika permintaan berasal dari alamat tepercaya. Jika tidak, digunakan alamat koneksi nyata, dan jika tidak dapat diekstrak — string `unknown`.

Semua percobaan dicatat dalam log. Untuk percobaan gagal, peringatan ditulis ke log server dengan username, IP, alasan, dan jika diblokir — waktu `blocked_until`. Jika notifikasi login melalui bot Telegram diaktifkan (`tgNotifyLogin` — «Notifikasi Login»), administrator juga menerima username, IP, dan waktu untuk percobaan yang berhasil, gagal, maupun diblokir.

**Contoh: notifikasi login di Telegram.** Dengan `tgNotifyLogin` diaktifkan, setelah setiap percobaan administrator menerima pesan yang kira-kira seperti ini:

```
Уведомление о входе
Пользователь: admin
IP: 203.0.113.45
Время: 2026-06-10 14:32:07
Статус: успешно
```

Untuk pasangan «IP + username» yang diblokir, statusnya akan menunjukkan bahwa percobaan ditolak oleh pembatas.

### 2.4. Penggantian Username dan Password Administrator

Bagian **Pengaturan → Akun**, tab **«Kredensial Administrator»**. Kolom:

| Kolom | Teks | Deskripsi |
|-------|------|-----------|
| Username saat ini | «Username saat ini» | Nama pengguna yang aktif. Harus cocok dengan username saat ini, jika tidak perubahan ditolak. |
| Password saat ini | «Password saat ini» | Password aktif untuk konfirmasi identitas. |
| Username baru | «Username baru» | Nama pengguna baru. Tidak boleh kosong. |
| Password baru | «Password baru» | Password baru. Tidak boleh kosong. |

Perubahan diterapkan dengan tombol **«Konfirmasi»** dan dikirim ke `POST /panel/setting/updateUser`.

Logika dan pesan server:

- Jika «Username saat ini» tidak cocok dengan yang sebenarnya atau «Password saat ini» salah — «Terjadi kesalahan saat mengubah kredensial administrator.» dengan penjelasan «Nama pengguna atau kata sandi tidak valid».
- Jika username baru atau password baru kosong — penjelasan «Username baru dan password baru harus diisi».
- Jika berhasil — «Anda berhasil mengubah kredensial administrator.». Password disimpan sebagai bcrypt hash.

**Contoh: penggantian kredensial melalui API.** Permintaan memerlukan cookie sesi yang valid (diperoleh saat login) dan konfirmasi username/password saat ini:

```bash
curl -X POST https://panel.example.com:2053/мой-секрет/panel/setting/updateUser \
  -b 'session=ВАША_СЕССИОННАЯ_COOKIE' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data 'oldUsername=admin&oldPassword=СтарыйПароль&newUsername=root&newPassword=НовыйСложныйПароль'
```

Setelah berhasil, sesi saat ini dihapus — perlu login ulang dengan kredensial baru.

Efek penting dari penggantian kredensial:

- **Semua sesi yang ada dihapus** (penghitung `login_epoch` pengguna dinaikkan), sehingga setelah penggantian panel secara otomatis melakukan logout dan mengarahkan ke halaman login — perlu login ulang.
- Jika **2FA diaktifkan** pada saat penggantian, **2FA secara otomatis dinonaktifkan** (flag dan rahasia dihapus). Autentikasi dua faktor perlu dikonfigurasi ulang setelah mengganti username/password.

Jika 2FA diaktifkan, sebelum mengirimkan formulir akan muncul jendela «Ubah Kredensial» dengan petunjuk «Masukkan kode dari aplikasi untuk mengubah kredensial administrator.» — perubahan kredensial hanya dapat dilakukan setelah mengonfirmasi kode 2FA saat ini.

### 2.5. Jalur Rahasia (URI-path / webBasePath) dan Port Panel

Parameter ini berada di bagian **Pengaturan → Panel** dan secara langsung memengaruhi «ketidakterlihat-an» dan aksesibilitas panel. Diterapkan setelah menyimpan dan **merestart panel**.

| Kolom | Teks | Nilai default | Deskripsi |
|-------|------|---------------|-----------|
| Port panel | «Port panel» (`panelPort`), petunjuk «Port tempat panel berjalan» | **2053** | Port TCP antarmuka web. |
| URI-path | «URI-path» (`panelUrlPath`), petunjuk «Harus dimulai dengan '/' dan diakhiri dengan '/'» | **/** | Jalur dasar rahasia (`webBasePath`). Panel hanya dapat diakses melalui jalur ini (misalnya, `/jalur-rahasia-saya/`). |
| Alamat IP untuk manajemen panel | «Alamat IP untuk manajemen panel» (`panelListeningIP`), petunjuk «Kosongkan untuk menerima koneksi dari IP mana pun» | kosong | Alamat tempat panel mendengarkan. Kosong = semua antarmuka. |
| Domain panel | «Domain panel» (`panelListeningDomain`), petunjuk «Kosongkan untuk menerima koneksi dari domain dan IP mana pun.» | kosong | Pembatasan akses berdasarkan domain (Host). |
| Path public key sertifikat panel | `publicKeyPath`, petunjuk «Masukkan path lengkap yang dimulai dengan '/'» | kosong | Sertifikat TLS untuk akses HTTPS ke panel. |
| Path private key sertifikat panel | `privateKeyPath`, petunjuk yang sama | kosong | Private key TLS. |

Perilaku jalur dasar (`webBasePath`):

- Nilai dinormalisasi secara otomatis: jika tidak dimulai dengan `/`, karakter tersebut ditambahkan di awal; jika tidak diakhiri dengan `/`, ditambahkan di akhir. Artinya, jalur selalu berbentuk `/…/`.
- Jalur dasar diterapkan pada panel itu sendiri, pada aset, dan pada cookie sesi (cookie hanya diterbitkan untuk jalur ini).

> Rekomendasi keamanan (bagian «Peringatan Keamanan»): panel sendiri menampilkan peringatan jika konfigurasi «terlalu publik»:
> - «Panel berjalan dengan HTTP biasa — konfigurasikan TLS untuk produksi.»
> - «Port default 2053 sudah dikenal luas — ubah ke port acak.»
> - «Jalur dasar default "/" sudah dikenal luas — ubah ke jalur acak.»
>
> Dengan kata lain, untuk server produksi perlu menetapkan **port non-standar**, **URI-path yang tidak mudah ditebak**, dan **sertifikat TLS**.

**Contoh: konfigurasi panel «tersembunyi» untuk produksi.** Di bagian **Pengaturan → Panel**, tetapkan nilai seperti berikut:

| Kolom | Nilai |
|-------|-------|
| Port panel | `34571` (acak, bukan 2053) |
| URI-path | `/aXf9Qm2/` (tidak mudah ditebak, dimulai dan diakhiri dengan `/`) |
| Path public key sertifikat panel | `/etc/letsencrypt/live/panel.example.com/fullchain.pem` |
| Path private key sertifikat panel | `/etc/letsencrypt/live/panel.example.com/privkey.pem` |

Setelah menyimpan dan merestart, panel hanya dapat diakses melalui `https://panel.example.com:34571/aXf9Qm2/`, dan peringatan keamanan akan hilang.

### 2.6. Masa Aktif Sesi (timeout)

Kolom **«Durasi Sesi»** (`sessionMaxAge`) terdapat di antara pengaturan panel/interval.

| Kolom | Teks | Nilai default | Satuan | Deskripsi |
|-------|------|---------------|--------|-----------|
| Durasi Sesi | «Durasi Sesi», petunjuk «Durasi sesi dalam sistem (nilai: menit)» | **360** | menit | Masa aktif cookie sesi administrator. |

Perilaku:

- Nilai dimasukkan dalam **menit** (default 360 menit = 6 jam) dan dikonversi ke detik saat cookie dikonfigurasi.
- Jika nilainya **lebih dari 0**, `MaxAge` yang sesuai diatur pada cookie sesi. Setelah jangka waktu ini, cookie tidak lagi berlaku dan pada permintaan berikutnya pengguna mendapatkan «Sesi telah kedaluwarsa. Silakan login kembali».
- Sesi juga menjadi tidak valid lebih awal saat penggantian kredensial atau saat 2FA pertama kali diaktifkan (melalui mekanisme `login_epoch`, lihat 2.4 dan 2.2) dan saat logout eksplisit (`POST /logout`).
- Cookie sesi ditandai `HttpOnly`, dengan kebijakan `SameSite=Lax`; flag `Secure` diatur saat akses langsung HTTPS ke panel.

Selain timeout itu sendiri, ada notifikasi terkait: **«Perbedaan Waktu Notifikasi Kedaluwarsa Sesi»** (`expireTimeDiff`, petunjuk «Menerima notifikasi kedaluwarsa sesi sebelum mencapai nilai ambang batas (nilai: hari)», default `0`) — memungkinkan menerima peringatan lebih awal.

### 2.7. LDAP (Sinkronisasi dan Autentikasi)

Bagian LDAP menyediakan dua kemampuan: (1) mengautentikasi login administrator melalui LDAP jika password lokal tidak cocok, dan (2) menyinkronkan status klien secara berkala (flag VLESS diaktifkan/dinonaktifkan) dari direktori.

Cara digunakan saat login: server pertama-tama memeriksa bcrypt hash password lokal. Jika **tidak cocok** dan LDAP diaktifkan, panel mencoba mengautentikasi pengguna di direktori: dengan `Bind DN` yang ditetapkan, dilakukan service bind, kemudian entri pengguna dicari menggunakan filter dan atribut, lalu dilakukan percobaan bind dengan DN yang ditemukan menggunakan password yang dimasukkan. Jika berhasil, login diterima. (Setelah autentikasi LDAP berhasil, jika 2FA diaktifkan, kode TOTP tetap diperiksa.)

Kolom bagian ini:

| Kolom | Teks | Nilai default | Deskripsi |
|-------|------|---------------|-----------|
| Aktifkan Sinkronisasi LDAP | «Aktifkan Sinkronisasi LDAP» (`enable`) | **false** | Sakelar utama integrasi LDAP. |
| Host LDAP | «Host LDAP» (`host`) | kosong | Alamat server LDAP. |
| Port LDAP | «Port LDAP» (`port`) | **389** | Port. Untuk LDAPS biasanya 636. |
| Gunakan TLS (LDAPS) | «Gunakan TLS (LDAPS)» (`useTls`) | **false** | Jika diaktifkan, skema `ldaps://` digunakan dengan verifikasi sertifikat server (tanpa melewati pemeriksaan). |
| Bind DN | «Bind DN» (`bindDn`) | kosong | DN akun layanan untuk bind/pencarian awal. Jika kosong — bind tidak dilakukan (pencarian anonim). |
| Password bind | petunjuk: «Dikonfigurasi; kosongkan untuk mempertahankan password saat ini.» / «Belum dikonfigurasi.» / «Dikonfigurasi — masukkan nilai baru untuk mengganti» | kosong | Password untuk `Bind DN`. Disimpan terpisah; untuk mempertahankan yang lama, kolom dibiarkan kosong. |
| Base DN | «Base DN» (`baseDn`) | kosong | Root subpohon tempat pencarian dilakukan (pencarian rekursif, seluruh subpohon). |
| Filter pengguna | «Filter pengguna» (`userFilter`) | `(objectClass=person)` | Filter LDAP untuk memilih akun. Saat autentikasi, username dimasukkan ke filter dengan escaping. |
| Atribut pengguna (username/email) | «Atribut pengguna (username/email)» (`userAttr`) | `mail` | Atribut yang dicocokkan dengan username/pengidentifikasi klien (misalnya, `mail` atau `uid`). |
| Atribut flag VLESS | «Atribut flag VLESS» (`vlessField`) | `vless_enabled` | Atribut yang menentukan apakah akses VLESS klien harus diaktifkan. |
| Atribut flag umum (opsional) | «Atribut flag umum (opsional)» (`flagField`), petunjuk «Jika diatur, menggantikan flag VLESS — mis. shadowInactive.» | kosong | Jika diatur, digunakan sebagai pengganti `vless_enabled`. |
| Nilai truthy | «Nilai truthy» (`truthyValues`), petunjuk «Dipisahkan koma; default: true,1,yes,on» | `true,1,yes,on` | Daftar nilai atribut flag yang dianggap sebagai «diaktifkan». |
| Balik flag | «Balik flag» (`invertFlag`), petunjuk «Aktifkan jika atribut berarti «dinonaktifkan» (mis. shadowInactive).» | **false** | Membalik arti flag. |
| Jadwal sinkronisasi | «Jadwal sinkronisasi» (`syncSchedule`), petunjuk «String seperti cron, mis. @every 1m» | `@every 1m` | Frekuensi sinkronisasi dalam format seperti cron. |
| Tag inbound | «Tag inbound» (`inboundTags`), petunjuk «Inbound tempat sinkronisasi LDAP dapat membuat atau menghapus klien secara otomatis.» | kosong | Membatasi inbound mana yang mengizinkan operasi otomatis. Jika tidak ada inbound: «Inbound tidak ditemukan. Buat inbound terlebih dahulu.» |
| Pembuatan klien otomatis | «Pembuatan klien otomatis» (`autoCreate`) | **false** | Membuat klien di inbound yang ditentukan jika klien tersebut muncul di direktori. |
| Penghapusan klien otomatis | «Penghapusan klien otomatis» (`autoDelete`) | **false** | Menghapus klien jika klien tersebut tidak lagi ada di direktori. |
| Volume default (GB) | «Volume default (GB)» (`defaultTotalGb`) | **0** | Batas lalu lintas untuk klien yang dibuat secara otomatis (0 = tanpa batas). |
| Masa berlaku default (hari) | «Masa berlaku default (hari)» (`defaultExpiryDays`) | **0** | Masa berlaku untuk klien yang dibuat secara otomatis (0 = tidak terbatas). |
| Batas IP default | «Batas IP default» (`defaultIpLimit`) | **0** | Batas jumlah IP simultan (0 = tanpa batas). |

Kekhasan logika flag sinkronisasi: saat membaca atribut flag (`flagField`, default `vless_enabled`), nilai dianggap «diaktifkan» jika termasuk dalam daftar nilai truthy; jika inversi diaktifkan, hasilnya dibalik. Atribut pengguna (`userAttr`) digunakan sebagai kunci pencocokan (email/nama) — entri tanpa nilai atribut ini dilewati.

> Keamanan: disarankan untuk mengaktifkan **TLS (LDAPS)** agar password bind dan password yang diperiksa tidak dikirimkan dalam teks biasa, dan untuk `Bind DN` gunakan akun dengan hak baca minimal yang diperlukan.

**Contoh: konfigurasi sinkronisasi LDAP yang umum (Active Directory).** Pengisian kolom bagian ini untuk direktori di mana status akses disimpan dalam atribut mirip flag `userAccountControl`, dan pencocokan dilakukan berdasarkan email:

| Kolom | Nilai |
|-------|-------|
| Host LDAP | `ldap.example.com` |
| Port LDAP | `636` |
| Gunakan TLS (LDAPS) | diaktifkan |
| Bind DN | `CN=svc-3xui,OU=Service,DC=example,DC=com` |
| Base DN | `OU=Users,DC=example,DC=com` |
| Filter pengguna | `(objectClass=person)` |
| Atribut pengguna (username/email) | `mail` |
| Atribut flag VLESS | `vless_enabled` |
| Nilai truthy | `true,1,yes,on` |
| Jadwal sinkronisasi | `@every 5m` |

Dengan konfigurasi ini, setiap 5 menit panel akan menelusuri subpohon `OU=Users`, mencocokkan klien berdasarkan `mail`, dan mengaktifkan/menonaktifkan akses VLESS berdasarkan nilai `vless_enabled`.

---

## 3. Ikhtisar / Dashboard

Dashboard ("Dashboard", dalam antarmuka bahasa Inggris — *Overview*) adalah halaman awal panel. Halaman ini menampilkan status server dan proses Xray secara real-time. Semua indikator dikirim dari sisi server. Penjadwal latar belakang merakit snapshot **setiap 2 detik** dan mendistribusikannya ke semua tab yang terbuka melalui WebSocket; setiap menit, baris metrik yang terakumulasi ditulis ke disk. Endpoint HTTP `GET /status` mengembalikan snapshot terakhir yang di-cache.

Di bawah ini diuraikan setiap indikator dan setiap elemen kontrol pada halaman tersebut.

### 3.1. Prinsip Umum Pengumpulan Data

- Snapshot dikumpulkan oleh library `gopsutil`. Jika pengukuran tertentu gagal, field tersebut tetap bernilai nol dan peringatan ditulis ke log (`get cpu percent failed`, `get uptime failed`, dan sebagainya) — ini tidak merusak seluruh dashboard, hanya tile yang bersangkutan yang akan menampilkan 0/N-A.
- Kecepatan "instan" (CPU %, jaringan, disk I/O) dihitung sebagai selisih antara snapshot saat ini dan sebelumnya, dibagi dengan interval dalam detik. Oleh karena itu, saat pertama kali halaman dimuat, nilai kecepatan mungkin nol sampai pengukuran kedua terkumpul.
- Riwayat dapat dilihat di bagian "Riwayat Sistem" (*System History*) — grafik dibangun berdasarkan baris data yang sama seperti yang dijelaskan di bawah ini (lihat bagian 3.12).

### 3.2. CPU

Tile "CPU" (*CPU*) menampilkan beban prosesor saat ini dalam persentase, serta parameter prosesor itu sendiri.

| Indikator | Deskripsi |
|---|---|
| Beban CPU, % | Proporsi waktu prosesor yang digunakan selama interval terakhir. Dihaluskan dengan rata-rata eksponensial (EMA, koefisien `alpha = 0.3`) agar lonjakan tidak membuat indikator bergetar. Nilai selalu dikunci dalam rentang 0–100%. Pada pengukuran pertama kali, dikembalikan 0 (inisialisasi titik dasar). |
| Prosesor logis | Jumlah core logis — yaitu dengan memperhitungkan Hyper-Threading. |
| Core fisik | Jumlah core fisik. |
| Frekuensi | Frekuensi dasar prosesor dalam MHz. Diminta secara lazy dan di-cache: pengukuran pertama yang berhasil disimpan, percobaan ulang dilakukan tidak lebih dari sekali setiap 5 menit, dan permintaan itu sendiri dibatasi dengan timeout 1,5 detik (pada beberapa sistem permintaan frekuensi merespons dengan lambat). |

Beban CPU secara algoritmik dihitung sebagai berikut: jika implementasi platform native tersedia, maka implementasi tersebut yang digunakan, jika tidak — perhitungan berdasarkan delta counter waktu prosesor (busy / total). Waktu Guest- dan GuestNice dikecualikan agar tidak dihitung dua kali.

### 3.3. Memori (RAM)

Tile "Memori" (*RAM*) menampilkan terpakai dan total. Ditampilkan sebagai "terpakai / total" dan/atau persentase pengisian. Persentase dicatat ke riwayat.

### 3.4. Swap

Tile "Swap" (*Swap*) menampilkan terpakai dan total. Jika file/partisi swap tidak dikonfigurasi (total = 0), indikatornya nol; jika swap tidak ada, 0 ditulis ke baris riwayat.

### 3.5. Disk (Storage)

Tile "Disk" (*Storage*) menampilkan terpakai dan total, dengan mempertimbangkan **hanya partisi root `/`**. Persentase pengisian ditulis ke riwayat "Penggunaan Disk" (*Disk Usage*). Input-output disk (baca / tulis, byte/dtk) dikumpulkan secara terpisah sebagai delta counter selama interval — ditampilkan pada tab "Disk I/O" di riwayat.

### 3.6. Uptime Sistem

Indikator "Uptime Sistem" (*Uptime*). Ini adalah waktu sejak booting **seluruh server** (dalam detik), bukan waktu berjalan panel atau Xray. Uptime proses Xray disimpan secara terpisah (lihat bagian 3.9), begitu pula jumlah thread panel (— "Thread" / *Threads*).

### 3.7. Load Average Sistem

Blok "Beban Sistem" (*System Load*) — array tiga angka `[Load1, Load5, Load15]`. Tooltip: "Rata-rata beban sistem selama 1, 5, dan 15 menit terakhir" (*System load average for the past 1, 5, and 15 minutes*). Grafik riwayat disebut "Rata-rata Beban Sistem (1 / 5 / 15 mnt)". Nilai ditulis ke baris riwayat secara terpisah: `load1`, `load5`, `load15`.

Ini adalah indikator Unix standar: rata-rata jumlah proses yang antri untuk dieksekusi. Acuannya — bandingkan dengan jumlah core: beban yang secara konsisten melebihi jumlah core fisik menunjukkan kelebihan beban.

### 3.8. Jaringan: Kecepatan dan Total Lalu Lintas

Hanya **antarmuka fisik** yang diperhitungkan. Antarmuka virtual dan tunnel dikecualikan: yaitu `lo`/`lo0`, serta semua yang dimulai dengan `loopback`, `docker`, `br-`, `veth`, `virbr`, `tun`, `tap`, `wg`, `tailscale`, `zt`. Nilai dijumlahkan untuk semua antarmuka yang tersisa.

**Kecepatan Keseluruhan** (*Overall Speed*) — kecepatan instan, delta counter selama interval:

| Indikator | Deskripsi |
|---|---|
| Upload (label "Upload" / *Upload*) | Kecepatan keluar, byte/dtk. |
| Download (label "Download" / *Download*) | Kecepatan masuk, byte/dtk. |

**Total Data Lalu Lintas** (*Total Data*) — counter terakumulasi sejak sistem dimulai:

| Indikator | Deskripsi |
|---|---|
| Terkirim (label "Terkirim" / *Sent*) | Total byte yang terkirim. |
| Diterima (label "Diterima" / *Received*) | Total byte yang diterima. |

Selain itu, kecepatan paket (paket/dtk) dan counter paket total dikumpulkan — ditampilkan pada tab "Paket Jaringan" (*Network Packets*) di riwayat. Baris riwayat jaringan: `netUp`, `netDown`, `pktUp`, `pktDown`.

### 3.9. Alamat IP Server

Blok "Alamat IP Server" (*IP Addresses*) menampilkan `IPv4` dan `IPv6`. Alamat eksternal ditentukan melalui layanan pihak ketiga (`api4.ipify.org`, `ipv4.icanhazip.com`, `v4.api.ipinfo.io/ip`, `ipv4.myexternalip.com/raw`, `4.ident.me`, `check-host.net/ip` untuk IPv4 dan yang serupa untuk IPv6). Daftar dicoba satu per satu hingga respons pertama yang berhasil; timeout setiap permintaan — 3 detik.

Hal-hal khusus:
- Hasilnya **di-cache** selama masa hidup proses: alamat yang berhasil ditentukan tidak diminta ulang.
- Jika tidak ada layanan yang merespons, field menampilkan `N/A`. Untuk IPv6, pada `N/A` pertama, permintaan IPv6 dinonaktifkan sepenuhnya agar tidak membuang waktu pada jaringan tanpa IPv6.
- Di sebelahnya terdapat tombol "mata" untuk menyembunyikan/menampilkan alamat — tooltip "Sembunyikan atau tampilkan alamat IP server" (*Toggle visibility of the IP*). Ini hanya penyembunyian visual di antarmuka (misalnya, untuk screenshot), tidak mempengaruhi alamat itu sendiri.

### 3.10. Koneksi TCP/UDP

Blok "Statistik Koneksi" (*Connection Stats*) menampilkan total jumlah koneksi TCP dan UDP aktif di server (di seluruh sistem, bukan hanya Xray). Grafik riwayat — "Koneksi Aktif (TCP / UDP)" (*Active Connections*), baris `tcpCount`, `udpCount`.

### 3.11. Status Xray dan Manajemen Proses

Kartu "Xray" menampilkan status proses Xray-core dan memberikan kontrol atas proses tersebut.

#### Status

| Nilai | Label | Terjemahan | Kapan ditetapkan |
|---|---|---|---|
| `running` | "Berjalan" | *Running* | Proses Xray sedang berjalan. |
| `stop` | "Berhenti" | *Stopped* | Proses tidak berjalan, dan tidak ada error startup yang tercatat. |
| `error` | "Error" | *Error* | Proses tidak berjalan, dan error startup telah tercatat. Teks error ditampilkan di jendela popup dengan judul "Error saat menjalankan Xray" (*An error occurred while running Xray*). |
| — | "Tidak Diketahui" | *Unknown* | Ditampilkan saat status belum diterima. |

**Versi Xray** ditampilkan di sebelah status.

#### Tombol Kontrol

- **Stop** (*Stop*). Memanggil `POST /stopXrayService`. Jika berhasil, panel mendistribusikan status baru `stop` melalui WebSocket dan notifikasi "Xray berhasil dihentikan" (*Xray service has been stopped*); jika error — status `error` dengan teksnya. Penting: jika panel dapat diakses *melalui* Xray itu sendiri, menghentikan Xray dapat memutus koneksi ke panel — tidak ada masalah jika terhubung langsung ke panel.
- **Restart** (*Restart*). Memanggil `POST /restartXrayService`. Sebelum tindakan, ditampilkan konfirmasi "Restart xray?" dengan penjelasan "Memuat ulang layanan xray dengan konfigurasi yang tersimpan". Jika berhasil — status `running` dan notifikasi "Xray berhasil di-restart" (*Xray service has been restarted successfully*). Restart menerapkan konfigurasi tersimpan saat ini — gunakan setelah mengubah pengaturan.

> Catatan. Di fork ini, kontrol penuh Start / Stop / Restart untuk semua jenis otorisasi telah ditambahkan ke dashboard; di UI 3x-ui asli tidak ada tombol "start" terpisah — startup dilakukan melalui restart.

#### Tombol Lihat Log Xray

Di kartu Xray terdapat tombol untuk melihat log Xray (*Logs*). Tombol ini hanya muncul jika access-log dikonfigurasi dalam konfigurasi Xray: viewer bawaan membaca file tersebut, sehingga tanpa access-log tombol disembunyikan. Visibilitas tombol terikat pada flag terpisah `accessLogEnable` dan tidak lagi bergantung pada batas IP — daftar online dan batas IP terus bekerja bahkan tanpa access-log (lihat bagian 8).

#### Pemilihan Versi Xray

Bagian "Pilih Versi" (*Version*) memungkinkan peralihan Xray-core ke rilis lain. Daftar versi dimuat melalui `GET /getXrayVersion`:

- Sumber — GitHub API repositori `XTLS/Xray-core` (`/releases`). Permintaan di-cache selama **15 menit**; jika GitHub gagal, daftar terakhir yang berhasil diperoleh dikembalikan agar picker tidak kosong.
- Hanya rilis dengan format `X.Y.Z` yang **tidak lebih lama dari 26.4.25** yang masuk ke daftar.

Tooltip: "Pilih versi yang ingin Anda alihkan" (*Choose the version you want to switch to.*) dan peringatan "Penting: versi lama mungkin tidak mendukung pengaturan saat ini" (*Choose carefully, as older versions may not be compatible with current configurations.*).

Peralihan: `POST /installXray/:version`. Skenario:

**Contoh.** Beralih ke versi Xray-core tertentu (cookie sesi harus sudah diperoleh melalui otorisasi):

```bash
curl -X POST 'https://panel.example.com:2053/xpanel/installXray/v25.6.8' \
  -b cookie.txt
```

Di sini `v25.6.8` adalah tag dari daftar yang dikembalikan oleh `GET /getXrayVersion`. Versi harus ada dalam daftar ini, jika tidak panel akan menolak.
1. Versi yang dipilih diverifikasi keberadaannya dalam daftar rilis saat ini (jika tidak — ditolak).
2. Xray dihentikan.
3. Arsip `Xray-<os>-<arch>.zip` untuk OS dan arsitektur saat ini diunduh dari GitHub (mendukung amd64/64, arm64-v8a, arm32-v7a/v6/v5, 386/32, s390x; untuk Windows — `xray.exe`). Ukuran arsip dan biner dibatasi 200 MB.
4. Biner diganti secara atomik (melalui file sementara + penggantian nama) dan ditandai sebagai dapat dieksekusi.
5. Xray dimulai kembali.

Sebelum peralihan, ditampilkan dialog "Alihkan versi Xray" (*Do you really want to change the Xray version?*) dengan deskripsi "Ini akan mengubah versi Xray ke #version#". Jika berhasil — notifikasi "Xray berhasil diperbarui" (*Xray updated successfully*).

### 3.12. Pembaruan Panel (3X-UI)

Blok pemeriksaan pembaruan panel. Data diterima melalui `GET /getPanelUpdateInfo`:

| Field | Deskripsi |
|---|---|
| Versi panel saat ini | Versi panel yang terpasang. |
| Versi panel terbaru | Rilis 3x-ui terbaru yang diperoleh dari GitHub. |
| Pembaruan tersedia | Tanda bahwa versi terbaru lebih baru dari versi saat ini. Jika tidak diperlukan pembaruan — ditampilkan "Panel sudah diperbarui" / "Diperbarui". |

Tombol **"Perbarui Panel"** (*Update Panel*) menjalankan `POST /updatePanel`. Tooltip: "Ini akan memperbarui 3X-UI ke rilis terbaru dan me-restart layanan panel". Sebelum memulai — konfirmasi "Apakah Anda benar-benar ingin memperbarui panel?" dengan teks "Ini akan memperbarui 3X-UI ke versi #version# dan me-restart layanan panel".

Hal-hal khusus dan batasan:
- Pembaruan otomatis hanya didukung **di Linux** (pada OS lain dikembalikan error).
- Skrip pembaruan diunduh dari repositori resmi (`raw.githubusercontent.com/MHSanaei/3x-ui/main/update.sh`, batas 2 MB) dan dijalankan melalui `bash`, jika memungkinkan diisolasi melalui `systemd-run`.
- Jika berhasil dimulai, ditampilkan "Pembaruan panel dimulai" (*Panel update started*); jika pemeriksaan pembaruan gagal — "Pemeriksaan pembaruan panel gagal". Selama instalasi, ditampilkan peringatan "Instalasi sedang berlangsung. Jangan refresh halaman".

### 3.13. Pembaruan File Geo (GeoIP / GeoSite)

Tombol/dialog pembaruan basis geo memanggil `POST /updateGeofile` (semua file) atau `POST /updateGeofile/:fileName` (satu file). Pembaruan bekerja dengan daftar putih nama dan sumber yang ketat:

| File | Sumber |
|---|---|
| `geoip.dat`, `geosite.dat` | `Loyalsoldier/v2ray-rules-dat` (latest) |
| `geoip_IR.dat`, `geosite_IR.dat` | `chocolate4u/Iran-v2ray-rules` (latest) |
| `geoip_RU.dat`, `geosite_RU.dat` | `runetfreedom/russia-v2ray-rules-dat` (latest) |

Perilaku:
- Nama file divalidasi: `..`, slash, path absolut dilarang; hanya `[a-zA-Z0-9._-]+.dat` yang diizinkan. File di luar daftar putih tidak diunduh.
- Permintaan kondisional `If-Modified-Since` digunakan: jika file di server sumber tidak berubah (HTTP 304), file tidak diunduh ulang, hanya timestamp yang diperbarui.
- Setelah pengunduhan, Xray **di-restart** (agar mengambil basis data baru).

**Contoh.** Memperbarui hanya basis geo Rusia, tanpa menyentuh file lainnya:

```bash
curl -X POST 'https://panel.example.com:2053/xpanel/updateGeofile/geoip_RU.dat' -b cookie.txt
curl -X POST 'https://panel.example.com:2053/xpanel/updateGeofile/geosite_RU.dat' -b cookie.txt
```

Untuk memperbarui semua file dari daftar putih sekaligus — panggil `POST /updateGeofile` tanpa nama file.
- Dialog: "Apakah Anda benar-benar ingin memperbarui file geo?" dengan "Ini akan memperbarui file #filename#" untuk satu file dan "Ini akan memperbarui semua file geo" untuk tombol "Perbarui Semua". Sukses — "File geo berhasil diperbarui".

### 3.14. Backup dan Pemulihan Database

Blok "Backup & Pemulihan" (*Backup & Restore*). Perilakunya tergantung pada DBMS yang digunakan (SQLite secara default atau PostgreSQL).

#### Ekspor Database (Backup)

Tombol "Ekspor database" / "Backup" (*Back Up*) memanggil `GET /getDb`. File dikirim sebagai lampiran:
- **SQLite**: pertama dilakukan checkpoint (flush WAL), kemudian file `x-ui.db` diunduh. Tooltip: "Klik untuk mengunduh file .db yang berisi backup database Anda saat ini…".
- **PostgreSQL**: dump `x-ui.dump` dalam format kustom diunduh (`pg_dump --format=custom --no-owner --no-privileges`). Alat klien PostgreSQL harus terpasang di server; jika tidak — error tentang tidak adanya `pg_dump`.

#### Impor Database (Pemulihan)

Tombol "Impor database" / "Pemulihan" (*Restore*) mengunggah file melalui `POST /importDB` (field form `db`). Tooltip: "Klik untuk memilih dan mengunggah file .db… untuk memulihkan database dari backup".

Skenario untuk **SQLite** aman, dengan rollback:
1. File diperiksa formatnya sebagai SQLite dan disimpan ke file sementara, kemudian integritas diperiksa.
2. Xray dihentikan, database saat ini ditutup dan diganti namanya menjadi `*.backup` (fallback).
3. File baru menggantikan database kerja, inisialisasi dan migrasi dilakukan. Jika terjadi kesalahan — fallback dipulihkan.
4. Xray dimulai kembali.

Untuk **PostgreSQL**, `.dump` diunggah (tanda tangan `PGDMP` diperiksa) dan diterapkan melalui `pg_restore --clean --if-exists --single-transaction …`. Tooltip secara eksplisit memperingatkan: "Ini akan menggantikan semua data saat ini".

Pesan: "Database berhasil diimpor", "Terjadi kesalahan saat mengimpor database", "…saat membaca database", "…saat menerima database".

#### File Migrasi (antara SQLite dan PostgreSQL)

Tombol "Unduh File Migrasi" (*Download Migration*) memanggil `GET /getMigration` dan membuat ekspor portabel untuk menjalankan panel pada DBMS lain:
- Di **SQLite**, `x-ui.dump` (dump SQL teks) diunduh.
- Di **PostgreSQL**, `x-ui.db` diunduh — database SQLite siap pakai yang dirakit dari data PostgreSQL.

### 3.15. Elemen Antarmuka Tambahan

- **Indikator klien online.** Dashboard memelihara baris `online` (*Online Clients* / "Klien Online") — jumlah klien dengan koneksi aktif. Dihitung saat Xray berjalan (jika tidak, 0) dan dicatat ke riwayat pada siklus 2 detik yang sama. Grafik — tab "Online".
- **Riwayat sistem (grafik).** Tombol/bagian "Grafik" → "Riwayat Sistem" dengan tab: "Bandwidth", "Paket", "Disk I/O", "Online", "Beban", "Koneksi", "Penggunaan Disk". Data diambil melalui `GET /history/:metric/:bucket`; interval agregasi yang diizinkan (bucket, dtk): **2, 30, 60, 120, 180, 300, 720, 1440, 2880** (tiga terakhir sesuai dengan preset **12h**, **24h**, dan **48h** di pemilih interval), hingga 60 titik data diterima per tab. Buffer melingkar metrik menyimpan data selama periode hingga **48 jam**, sehingga grafik (CPU, RAM, lalu lintas, paket, koneksi, disk, online, beban) dapat dilihat selama periode hingga dua hari. Metrik yang diizinkan: `cpu, mem, swap, netUp, netDown, pktUp, pktDown, diskRead, diskWrite, diskUsage, tcpCount, udpCount, online, load1, load5, load15`. Label "2 menit terakhir" sesuai dengan bucket = 2 (mode real-time).

**Contoh.** Mendapatkan baris beban CPU selama ~2 menit terakhir (bucket = 2 dtk, hingga 60 titik) dan baris yang sama teragregasi per 5 menit (bucket = 300 dtk):

  ```bash
  curl 'https://panel.example.com:2053/xpanel/history/cpu/2' -b cookie.txt
  curl 'https://panel.example.com:2053/xpanel/history/cpu/300' -b cookie.txt
  ```

  Metrik dapat diganti dengan metrik yang diizinkan mana pun (`mem`, `netUp`, `tcpCount`, `load1`, dll.). Bucket di luar daftar `2, 30, 60, 120, 180, 300, 720, 1440, 2880` akan ditolak.
- **Metrik Xray** — blok terpisah dengan konsumsi memori dan garbage collection Xray (baris `xrAlloc, xrSys, xrHeapObjects, xrNumGC, xrPauseNs`) dan "Observatory" (status koneksi outbound). Hanya berfungsi jika blok `metrics` dikonfigurasi dalam konfigurasi Xray (`listen 127.0.0.1:11111`, tag `metrics_out`); jika tidak, ditampilkan "Endpoint metrik Xray tidak dikonfigurasi".

**Contoh** blok yang mengaktifkan tile metrik Xray. Di bagian pengaturan Xray, `metrics` (dengan tag) dan inbound yang mendengarkan tag tersebut harus ada secara bersamaan:

  ```json
  {
    "metrics": {
      "tag": "metrics_out"
    },
    "inbounds": [
      {
        "listen": "127.0.0.1",
        "port": 11111,
        "protocol": "dokodemo-door",
        "settings": { "address": "127.0.0.1" },
        "tag": "metrics_out"
      }
    ]
  }
  ```

  Alamat `127.0.0.1:11111` sengaja tidak diekspos ke luar — panel mempollnya secara lokal.
- **Pengalih tema gelap.** Terletak di menu umum/header, bukan di dashboard itu sendiri. Pilihan: "Tema" (*Theme*) dengan opsi "Gelap" dan "Sangat Gelap" (*Ultra Dark*). Ini adalah pengaturan tampilan visual semata, tidak mempengaruhi fungsi panel.
- **Tautan lainnya** di sekitar dashboard (dari menu/panel bawah): "Log", "Konfigurasi" — tampilan JSON Xray final (`GET /getConfigJson`), "Dokumentasi".

---

## 4. Inbounds: pembuatan dan parameter umum

Bagian **«Incoming»** (Inbounds) adalah daftar semua titik masuk Xray yang digunakan klien untuk terhubung. Setiap inbound menyimpan baik field "panel" (catatan, batas lalu lintas, jadwal reset) maupun blok JSON konfigurasi Xray mentah (`settings`, `streamSettings`, `sniffing`).

Pembuatan dilakukan dengan tombol **«Buat Koneksi»** (*Add Inbound*), pengeditan dengan **«Ubah Koneksi»** (*Modify Inbound*). Kedua operasi dikirimkan ke endpoint API `POST /add` dan `POST /update/:id`.

Di bawah ini dijelaskan semua field formulir yang **tidak** berkaitan dengan pengaturan protokol tertentu (klien, enkripsi, REALITY/TLS) dan **tidak** berkaitan dengan transport/stream (tab **«Stream»**, **«Security»**) — ini adalah topik bagian terpisah.

### 4.1. Field formulir umum

#### Remark (Catatan)

| Parameter | Nilai |
|---|---|
| Field | `remark` |
| Tipe | string |
| Default | kosong |

Nama inbound yang dapat dibaca manusia, ditampilkan dalam daftar dan di judul dialog («Hapus koneksi "{remark}"?» dan sejenisnya). Label field — **«Catatan»**. Tidak mempengaruhi cara kerja Xray, hanya diperlukan untuk kemudahan administrasi; disarankan menggunakan nama unik yang bermakna karena nama tersebut digunakan dalam nama file yang diekspor dan dalam konfirmasi operasi massal.

#### Protocol (Protokol)

| Parameter | Nilai |
|---|---|
| Field | `protocol` |
| Label | **«Protokol»** |
| Validasi | `required,oneof=vmess vless trojan shadowsocks wireguard hysteria http mixed tunnel tun` |

Daftar dropdown protokol inbound. Nilai yang diizinkan:

| Nilai | Catatan |
|---|---|
| `vmess` | |
| `vless` | |
| `trojan` | |
| `shadowsocks` | |
| `wireguard` | |
| `hysteria` | Hysteria v2 — ini adalah `hysteria` dengan `streamSettings.version = 2`, tidak ada protokol terpisah |
| `http` | |
| `mixed` | socks/http pada satu port |
| `tunnel` | |
| `tun` | diterima oleh validator, tidak ada konstanta protokol tersendiri |

Field ini wajib diisi (`required`). Pemilihan protokol menentukan field pengaturan klien dan transport mana yang akan tersedia (lihat bagian spesifik protokol).

> Penting: saat menyimpan, layanan menormalkan `streamSettings`. Pengaturan transport hanya dipertahankan untuk protokol `vmess`, `vless`, `trojan`, `shadowsocks`, `hysteria`; untuk yang lain (`http`, `mixed`, `tunnel`, `wireguard`, `tun`) field `streamSettings` **dihapus paksa**.

Untuk inbound bertipe `tunnel`/TProxy yang blok `streamSettings`-nya tidak mengandung kunci `security` (varian tanpa transport), formulir dibuka dan disimpan tanpa error validasi `streamSettings.security Invalid input`.

#### Listen IP (IP yang didengarkan)

| Parameter | Nilai |
|---|---|
| Field | `listen` |
| Tipe | string |
| Default | kosong → Xray mendengarkan pada `0.0.0.0` (semua IP) |

Alamat IP tempat inbound menerima koneksi. Petunjuk field:

> «Biarkan kosong untuk mendengarkan semua alamat IP».

Saat membuat konfigurasi Xray, nilai kosong diganti dengan `0.0.0.0`. Selain IP, field ini juga menerima **jalur Unix socket** — petunjuk:

> «Anda juga dapat menentukan jalur Unix socket (misalnya, /run/xray/in.sock) atau nama abstract socket dengan awalan @ (misalnya, @xray/in.sock) untuk mendengarkan socket alih-alih port TCP — dalam hal ini tetapkan port 0».

Dengan demikian, field menerima dua bentuk Unix socket: jalur di sistem file (`/run/xray/in.sock`) dan nama abstract socket dengan awalan `@` (`@xray/in.sock`). Dalam kedua kasus, tetapkan `Port` ke `0`.

Field ini diubah ketika inbound perlu dibatasi pada satu antarmuka (misalnya, `127.0.0.1` untuk inbound yang hanya berfungsi sebagai target fallback di belakang Nginx) atau ketika inbound mendengarkan Unix socket.

**Contoh.** Inbound yang hanya mendengarkan antarmuka lokal (target fallback tipikal di belakang Nginx) dan Unix socket:

```
listen = 127.0.0.1   port = 8443
listen = /run/xray/in.sock   port = 0
```

#### Port (Port)

| Parameter | Nilai |
|---|---|
| Field | `port` |
| Label | **«Port»** |
| Validasi | `gte=0,lte=65535` |
| Default | — (ditentukan oleh pengguna) |

Port TCP/UDP yang didengarkan. Nilai yang diizinkan dari `0` hingga `65535`. Nilai `0` hanya digunakan berpasangan dengan mendengarkan pada Unix socket (lihat di atas).

Saat menyimpan, layanan memeriksa konflik port: dua inbound tidak dapat secara bersamaan menempati `listen:port` yang tumpang tindih untuk transport yang sama (TCP/UDP). Transport dihitung dari protokol dan `streamSettings`/`settings`: misalnya, `hysteria` dan `wireguard` selalu menempati UDP, `kcp`/`quic` — UDP, dan sebagian besar lainnya — TCP. Jika terjadi konflik, penyimpanan ditolak dengan error.

Secara terpisah, panel tidak mengizinkan penggunaan **port yang dicadangkan untuk API Xray internal** (tag `api`, default `62789` pada `127.0.0.1`): inbound TCP lokal yang alamat dengarnya tumpang tindih dengan port ini pada loopback ditolak dengan error konflik port yang sama. Port API aktual dibaca dari template konfigurasi Xray (dengan nilai fallback `62789`). Pada node, pembatasan ini tidak berlaku — node memiliki Xray sendiri.

> Tag Xray (`Tag`, unik) dibuat secara otomatis dari port dan transport dalam format `in-<port>-<tcp|udp|tcpudp|any>`; untuk inbound yang di-deploy pada node, ditambahkan awalan `n<nodeId>-`. Jika terjadi tabrakan, `-2`, `-3`, dan seterusnya ditambahkan ke tag. Pengguna biasanya tidak mengedit tag.

#### Total traffic (Total lalu lintas, GB)

| Parameter | Nilai |
|---|---|
| Field | `total` (dalam **byte**) |
| Label | **«Total penggunaan»** |
| Default | `0` |

Batas lalu lintas total inbound. Dalam formulir, nilai dimasukkan dalam gigabyte; di database disimpan dalam byte. Petunjuk field:

> «= Tanpa batas. (satuan: GB)».

Artinya, **`0` berarti tanpa batas**. Ini adalah batas di tingkat seluruh inbound (bukan klien individual); lalu lintas yang sebenarnya dikonsumsi disimpan di field `up` (dikirim) dan `down` (diterima) dan dibandingkan dengan `total`.

#### Expiry date / Duration (Tanggal kedaluwarsa / durasi)

| Parameter | Nilai |
|---|---|
| Field | `expiryTime` (Unix timestamp) |
| Label | **«Tanggal kedaluwarsa»** (*Duration*) |
| Default | kosong / `0` |

Masa berlaku inbound. Petunjuk:

> «Biarkan kosong agar tidak terbatas».

Nilai kosong (`0`) berarti inbound tanpa batas waktu. Nilai disimpan sebagai Unix timestamp; formulir memungkinkan pengaturan baik tanggal tertentu maupun durasi dalam hari (penghitungan relatif dari saat ini — label field *Duration*).

#### Enabled (Aktifkan)

| Parameter | Nilai |
|---|---|
| Field | `enable` |
| Label | **«Aktifkan»** (*Enabled*) |
| Default | ditentukan saat pembuatan |

Tanda aktifitas inbound. Peralihan flag ini dalam daftar diproses oleh endpoint "ringan" terpisah `POST /setEnable/:id`, bukan pembaruan penuh — ini dilakukan secara khusus agar tidak harus melakukan serialisasi ulang seluruh blok `settings` (semua klien) setiap kali toggle diklik pada inbound dengan ribuan klien. Saat dinonaktifkan, inbound dihapus dari Xray yang berjalan; saat diaktifkan — ditambahkan kembali.

#### Node / Deploy to (Node / Deploy ke)

| Parameter | Nilai |
|---|---|
| Field | `nodeId` |
| Label | **«Deploy ke»**, **«Panel lokal»** |
| Default | kosong (panel lokal) |

Pilihan di mana inbound beroperasi secara fisik: pada panel lokal atau pada salah satu node yang terdaftar. Fitur implementasi: `nodeId = 0` dinormalisasi menjadi `nil`, karena `0` bukan id node yang valid, melainkan artefak binding formulir; `nil`/`0` berarti panel lokal. Saat menyimpan inbound pada node yang offline, mungkin muncul toast «perubahan akan disinkronkan saat node terhubung kembali».

#### Strategi alamat untuk tautan (Share address strategy)

| Parameter | Nilai |
|---|---|
| Field | strategi + (opsional) alamat kustom |
| Label | **«Strategi alamat untuk tautan»** (*Share address strategy*) |
| Default | **«Alamat dengar inbound»** (*Inbound listen*) |

Daftar dropdown menentukan alamat mana yang dimasukkan ke dalam **tautan berbagi dan kode QR yang diekspor** dari inbound ini. Nilai:

| Nilai | Label | Yang dimasukkan |
|---|---|---|
| `node` | **«Alamat node»** (*Node address*) | alamat node tempat inbound beroperasi |
| `listen` | **«Alamat dengar inbound»** (*Inbound listen*) | alamat dengar inbound itu sendiri |
| `custom` | **«Kustom»** (*Custom*) | alamat sendiri dari field **«Alamat berbagi kustom»** (*Custom share address*) |

Saat memilih **«Kustom»**, muncul field **«Alamat berbagi kustom»**; di sini dimasukkan host atau IP **tanpa skema dan port** (nilai divalidasi). Opsi **«Alamat node»** ditampilkan dalam daftar hanya jika ada node aktif yang dapat menjalankan inbound ini; jika tidak, opsi disembunyikan dan nilainya dikembalikan ke **«Alamat dengar inbound»**.

Strategi ini mempengaruhi **hanya** tautan berbagi langsung dan kode QR. Ini **tidak** mempengaruhi output langganan — di sana alamat masih ditentukan oleh logika panel biasa.

### 4.2. Sniffing (Sniffing)

Tab **«Sniffing»** mengedit blok `sniffing` konfigurasi Xray, yang disimpan sebagai JSON mentah. Sniffing memungkinkan Xray "mengintip" nama domain/protokol nyata di dalam koneksi untuk keperluan routing.

| Subfield | Label | Tujuan |
|---|---|---|
| `enabled` | (toggle tab) | Mengaktifkan/menonaktifkan sniffing untuk inbound |
| `destOverride` | — | Daftar protokol yang alamat tujuannya dicegat: `http`, `tls`, `quic`, `fakedns` |
| `metadataOnly` | **«Hanya metadata»** | Gunakan hanya metadata koneksi, tanpa membaca payload |
| `routeOnly` | **«Hanya routing»** | Terapkan hasil sniffing hanya untuk routing, tanpa menimpa alamat tujuan |
| `domainsExcluded` | **«Domain yang dikecualikan»** | Domain yang dikecualikan dari sniffing |
| (IP yang dikecualikan) | **«IP yang dikecualikan»** | Alamat IP yang dikecualikan dari sniffing |

- **`destOverride`** — kumpulan sniffer: `http` (menentukan domain dari header HTTP Host), `tls` (dari SNI), `quic` (dari QUIC ClientHello), `fakedns` (pencocokan dengan pool FakeDNS). Biasanya `http` dan `tls` diaktifkan untuk menentukan domain.

**Contoh blok `sniffing`** (menentukan domain melalui HTTP dan TLS, gunakan hasil hanya untuk routing, jangan menyentuh jaringan lokal):

```json
{
  "enabled": true,
  "destOverride": ["http", "tls"],
  "routeOnly": true,
  "domainsExcluded": ["courier.push.apple.com"]
}
```
- **`metadataOnly`** — saat diaktifkan, Xray tidak membaca isi paket pertama dan hanya mengandalkan metadata; berguna agar tidak mengganggu protokol yang datanya tidak bisa "diintip".
- **`routeOnly`** — hasil sniffing hanya digunakan oleh aturan routing; alamat koneksi dalam outbound tidak ditimpa dengan domain yang terdeteksi.

> Catatan: panel menyimpan `sniffing` sebagai blok JSON opak dan tidak menambahkan apapun saat menyimpan — semua nilai default untuk checkbox ini dibentuk di sisi aplikasi klien. Dalam bentuk mentah, blok dapat diedit melalui bagian «JSON inbound» (lihat di bawah).

### 4.3. Allocate (strategi alokasi port)

Blok `allocate` dalam `streamSettings` mengontrol bagaimana Xray mendistribusikan port yang didengarkan. Ini adalah bagian dari konfigurasi Xray; panel menyimpan dan meneruskannya sebagai bagian dari `streamSettings`/JSON inbound. Parameter (menurut terminologi Xray-core):

| Subfield | Tujuan | Nilai / default |
|---|---|---|
| `strategy` | Strategi alokasi port | `always` — selalu dengarkan port yang ditentukan (default); `random` — ganti port yang didengarkan secara berkala dalam rentang |
| `refresh` | Interval pergantian port (menit) saat `random` | bilangan bulat menit (disarankan 5; minimum — 2) |
| `concurrency` | Berapa port yang dibuka secara bersamaan saat `random` | bilangan bulat (default 3; tidak lebih dari sepertiga lebar rentang port) |

`strategy: always` membuat inbound tetap pada satu port (mode standar). `strategy: random` diperlukan untuk skenario anti-blocking ketika inbound secara berkala "melompat" melalui rentang port; dalam hal ini `refresh` dan `concurrency` menjadi relevan. Ubah nilai ini hanya saat menggunakan mode port acak secara sadar.

**Contoh blok `allocate`** dalam `streamSettings` (mode port acak: pertahankan 3 port terbuka, ganti setiap 5 menit):

```json
{
  "allocate": {
    "strategy": "random",
    "refresh": 5,
    "concurrency": 3
  }
}
```

Agar ini berfungsi, `port` inbound ditentukan sebagai rentang (misalnya, `20000-20100`).

### 4.4. External Proxy (Proksi eksternal)

Field **«External Proxy»** berkaitan dengan pengaturan pembuatan tautan undangan dan disimpan dalam `streamSettings` inbound. Field ini menentukan daftar alamat eksternal alternatif (host/port, bila perlu dengan TLS paksa — **«TLS Paksa»**) yang dimasukkan ke dalam tautan klien alih-alih `listen:port` inbound yang sebenarnya.

Digunakan ketika klien harus terhubung bukan langsung ke server, tetapi melalui proksi/reverse/CDN eksternal: dalam hal ini tautan bersama menentukan alamat publik frontend tersebut. Ini tidak mempengaruhi proses penerimaan koneksi Xray itu sendiri — ini hanya "kosmetik" untuk tautan yang dihasilkan. Field formulir terkait: **«TLS Paksa»**, **«Fingerprint»**, label setiap entri.

### 4.5. Fallbacks (Fallback)

Bagian **«Fallback»** menentukan aturan pengalihan koneksi yang tidak cocok dengan klien inbound manapun. Tersedia untuk master inbound pada transport TLS (VLESS/Trojan TCP-TLS). Dikelola melalui endpoint `GET /:id/fallbacks` / `POST /:id/fallbacks`.

Petunjuk bagian:

> «Ketika koneksi pada inbound ini tidak cocok dengan klien manapun, koneksi tersebut dialihkan ke tempat lain. Pilih inbound anak di bawah ini agar field routing (SNI / ALPN / Path / xver) terisi otomatis dari transportnya, atau biarkan pilihan kosong dan tentukan Dest secara langsung (misalnya, 8080 atau 127.0.0.1:8080) untuk mengalihkan ke server eksternal seperti Nginx. Setiap inbound anak harus mendengarkan pada 127.0.0.1 dengan security=none».

Bagian fallback hanya ditampilkan untuk inbound VLESS/Trojan di atas RAW (TCP) dengan keamanan TLS atau REALITY. Inbound baru dimulai dengan `security=none`, sehingga bagian ini mungkin terlihat tidak ada pada awalnya. Dalam kondisi ini (VLESS/Trojan, RAW/TCP, keamanan belum dikonfigurasi) alih-alih bagian tersebut ditampilkan petunjuk bawaan: fallback akan tersedia setelah memilih TLS atau Reality pada tab **«Security»**.

#### Field baris fallback

| Field | Default | Deskripsi |
|---|---|---|
| (inbound anak) | — | Pilihan inbound anak (label **«Pilih inbound»**). Jika dipilih, field Name/Alpn/Path/Dest dapat terisi otomatis dari transportnya |
| Name | kosong (= sembarang) | Kondisi pencocokan berdasarkan nama (SNI/nama). Label "sembarang" — **«sembarang»** |
| Alpn | kosong | Kondisi pencocokan berdasarkan ALPN |
| Path | kosong | Kondisi pencocokan berdasarkan path (untuk transport WS/HTTP dari inbound anak) |
| Dest | otomatis | Ke mana dialihkan. Placeholder **«otomatis (listen:port anak)»**. Dapat menentukan port (`8080`) atau `host:port` (`127.0.0.1:8080`) |
| Xver | `0` | Versi PROXY protocol (**«Xver»**): `0` — nonaktif, `1` atau `2` — versi PROXY protocol yang sesuai |
| (urutan) | berdasarkan posisi | Urutan penerapan aturan; ditentukan dengan tombol **«Naik»**/**«Turun»** |

Logika penyimpanan: seluruh daftar fallback master diganti secara atomik. Baris yang tidak memiliki inbound anak yang dipilih (`childId <= 0`) maupun `Dest` yang ditentukan, **dilewati**. Jika inbound anak yang dipilih sama dengan id master, nilainya direset. Saat membuat JSON akhir: jika `Dest` kosong, dihitung dari inbound anak sebagai `listen:port`, di mana `0.0.0.0`/`::`/`::0` diganti dengan `127.0.0.1`; field `name`/`alpn`/`path` yang kosong tidak dimasukkan ke JSON output; `xver` hanya ditambahkan jika nilainya lebih dari 0.

**Contoh `settings.fallbacks` akhir** (lalu lintas dengan `alpn=h2` diarahkan ke target WS pada path `/ws`, semua lainnya ke Nginx lokal pada port 8080):

```json
{
  "fallbacks": [
    { "alpn": "h2", "path": "/ws", "dest": "127.0.0.1:2001", "xver": 1 },
    { "dest": 8080 }
  ]
}
```

Baris terakhir tanpa `name`/`alpn`/`path` adalah aturan "default" yang menangkap semua lainnya.

#### Tombol dan petunjuk bagian fallback

- **«Tambah fallback»** — tambah baris; **«Belum ada fallback»** — kondisi kosong.
- **«Tambah semua yang sesuai dengan cepat»** / **«Tambah semua»** — menambahkan baris fallback untuk setiap inbound yang sesuai yang belum terhubung. Hasilnya: «{n} fallback ditambahkan» atau «Tidak ada inbound baru yang sesuai».
- **«Isi dari anak»** — ambil ulang field routing (SNI/ALPN/Path/xver) dari transport inbound anak yang dipilih; setelah selesai — «Diisi dari anak».
- **«Ubah field routing»** / **«Sembunyikan lanjutan»** — tampilkan/sembunyikan field detail baris.
- Label **«Merutekan ketika»** dan **«Default — menangkap semua lainnya»** menjelaskan kondisi pemicuan setiap baris.

Setelah menyimpan fallback, server memanggil restart Xray agar `settings.fallbacks` baru berlaku.

### 4.6. Reset lalu lintas berkala

Blok **«Reset Lalu Lintas»** mengonfigurasi reset otomatis penghitung lalu lintas inbound sesuai jadwal. Deskripsi:

> «Reset otomatis penghitung lalu lintas pada interval yang ditentukan».

| Parameter | Nilai |
|---|---|
| Field | `trafficReset` |
| Validasi | `omitempty,oneof=never hourly daily weekly monthly` |
| Default | `never` |
| Field terkait | `lastTrafficResetTime` — timestamp reset terakhir (label **«Reset terakhir»**) |

Daftar dropdown:

| Nilai | Label |
|---|---|
| `never` | **«Tidak pernah»** |
| `hourly` | **«Setiap jam»** |
| `daily` | **«Setiap hari»** |
| `weekly` | **«Setiap minggu»** |
| `monthly` | **«Setiap bulan»** |

Untuk setiap periode, cron job terdaftar yang berjalan sesuai jadwal yang sesuai (`@hourly`, `@daily`, `@weekly`, `@monthly`). Job memilih semua inbound dengan `trafficReset` yang ditentukan dan untuk setiap inbound mereset penghitung inbound itu sendiri (`up=0`, `down=0`) **dan** lalu lintas semua kliennya. Artinya, reset berkala mempengaruhi inbound dan klien-kliennya.

**Contoh nilai field.** Agar penghitung direset pada hari pertama setiap bulan, pilih **«Setiap bulan»** dalam formulir, yang disimpan sebagai:

```json
{ "trafficReset": "monthly" }
```

Nilai `never` (default) sepenuhnya menonaktifkan auto-reset.

### 4.7. JSON inbound (lanjutan)

Bagian **«Bagian JSON inbound»** memberikan akses langsung ke blok JSON mentah inbound. Deskripsi:

> «JSON lengkap inbound dan editor terpisah untuk settings, sniffing, dan streamSettings».

Editor yang tersedia:

| Tab | Label | Yang diedit |
|---|---|---|
| **Semua** | «Objek inbound lengkap dengan semua field dalam satu editor» | seluruh objek Inbound |
| **Pengaturan** | «Wrapper blok settings Xray» | field `settings` |
| **Sniffing** | «Wrapper blok sniffing Xray» | field `sniffing` |
| **Stream** | «Wrapper blok stream Xray» | field `streamSettings` |

Field-field ini diserialisasi sebagai objek JSON bersarang: blok kosong dikembalikan sebagai `null`, dan teks yang bukan JSON valid dibungkus dalam string agar data tidak hilang. Error parsing saat menyimpan ditampilkan dengan awalan **«JSON Lanjutan»**.

Jendela tampilan «JSON inbound», seperti jendela impor inbound, menggunakan editor kode lengkap dengan penyorotan sintaks JSON (bukan field teks biasa): tampilan konfigurasi dalam mode baca saja dengan sorotan, sedangkan impor dalam mode yang dapat diedit, yang memudahkan membaca dan mengedit.

### 4.8. Tindakan pada inbound: QR / Edit / Reset / Delete dan statistik

Dalam daftar dan kartu inbound, tindakan berikut tersedia (menu **«Menu»**):

#### Statistik lalu lintas

Ditampilkan lalu lintas agregat inbound: **«Dikirim/diterima»** (field `up`/`down`), **«Total lalu lintas»**, **«Total koneksi»**. Dalam kartu juga — **«Dibuat»**, **«Diperbarui»**, **«Tanggal kedaluwarsa»**.

Dalam daftar inbounds terdapat kolom **Speed** dengan kecepatan lalu lintas saat ini untuk setiap inbound (kirim/unduh), dihitung dari selisih penghitung antara polling; kecepatan langsung yang sama ditampilkan di jendela statistik inbound. Ketika polling berikutnya tidak menghasilkan selisih, nilai kecepatan direset.

Dalam ringkasan klien pada halaman inbounds, status ditentukan berdasarkan prioritas «habis/berakhir»: klien yang masa berlakunya habis atau lalu lintasnya habis (dan yang tugas auto-nya mencabut `enable`) masuk ke status **«Habis/Berakhir»** (*Depleted/Ended*), bukan ke **«Dinonaktifkan»** (*Disabled*) abu-abu, dan tidak dihitung dua kali. Klasifikasi sesuai dengan yang ditampilkan di kartu klien itu sendiri, dan dengan benar memperhitungkan klien yang terikat ke beberapa inbound.

#### Kode QR dan penyalinan tautan

- **«Detail»** — membuka tautan koneksi dan langganan.
- Kode QR klien: petunjuk **«Klik kode QR untuk menyalin»**.
- **«Salin tautan»** (*Copy URL*), **«Ekspor tautan»**.

#### Edit (Ubah)

**«Ubah koneksi»** — membuka formulir pengeditan (`POST /update/:id`). Saat memperbarui, layanan membaca ulang baris yang ada, mentransfer field yang diubah, bila perlu membuat ulang tag (jika tag lama dibuat otomatis) dan menyinkronkan runtime Xray. Sukses — toast **«Koneksi berhasil diperbarui»**.

#### Reset Traffic (Reset lalu lintas)

**«Reset lalu lintas»** — mereset penghitung `up`/`down` inbound ini (`POST /:id/resetTraffic`, menetapkan `up=0, down=0`). Konfirmasi:

> «Reset lalu lintas "{remark}"?» / «Mereset penghitung pengiriman/penerimaan koneksi ini ke 0».

Reset lalu lintas inbound **tidak** menyentuh penghitung klien-kliennya (untuk itu ada tindakan «Reset lalu lintas klien» terpisah). Setelah reset, restart Xray dimulai. Sukses — toast **«Lalu lintas masuk direset»**. Ada juga varian massal — **«Reset lalu lintas semua koneksi»** (`POST /resetAllTraffics`).

#### Delete (Hapus)

**«Hapus koneksi»** (`POST /del/:id`). Konfirmasi:

> «Hapus koneksi "{remark}"?» / «Koneksi dan semua kliennya akan dihapus. Tindakan ini tidak dapat dibatalkan».

Penghapusan melepas inbound dari Xray yang berjalan (bila perlu dengan restart). Sukses — toast **«Koneksi berhasil dihapus»**. Penghapusan massal — `POST /bulkDel`, dengan pelaporan per elemen dan tidak lebih dari satu restart Xray.

#### Tindakan lain pada klien inbound

Dalam menu juga tersedia: **«Klon»** (salinan inbound dengan port baru dan daftar klien kosong), **«Hapus semua klien»** (`POST /:id/delAllClients` — menghapus semua klien, inbound itu sendiri dipertahankan), **«Hapus klien yang dinonaktifkan»**, **«Ikat/Lepas ikat klien»**, **«Impor»**/**«Ekspor koneksi»** (`POST /import`). Detail operasi klien termasuk dalam bagian tentang klien.

---

## 5. Protokol

Saat membuat inbound, langkah pertama adalah memilih **Protokol** («Protocol»). Protokol menentukan metode autentikasi dan enkripsi lalu lintas yang akan diterapkan Xray-core pada inbound tersebut, kumpulan field apa saja di bagian `settings` yang perlu diisi, serta transport (`network`) dan jenis keamanan (TLS / REALITY) apa yang tersedia untuknya.

Field protokol ditetapkan sekali saat pembuatan inbound dan **tidak dapat diubah saat pengeditan** (dropdown dinonaktifkan di formulir pengeditan). Untuk mengganti protokol, buat inbound baru.

### 5.1. Daftar protokol yang didukung

Server menerima kumpulan nilai field `Protocol` berikut:

```
oneof=vmess vless trojan shadowsocks wireguard hysteria http mixed tunnel tun mtproto
```

> Mulai versi **3.3.0**, nilai `mtproto` (proxy Telegram) ditambahkan ke daftar ini.

| Nilai dalam konfigurasi | Fungsi | Model klien |
|---|---|---|
| `vless` | Protokol proxy utama (default saat membuat inbound) | Klien dengan UUID, dukungan flow dan enkripsi post-quantum |
| `vmess` | Protokol proxy klasik Xray | Klien dengan UUID dan parameter `security` |
| `trojan` | Proxy yang menyamar sebagai HTTPS biasa | Klien dengan password |
| `shadowsocks` | Proxy Shadowsocks (termasuk SIP022 / 2022-blake3) | Satu pengguna atau banyak (2022) |
| `wireguard` | Inbound WireGuard | Peer (bukan klien) |
| `hysteria` | Inbound Hysteria (versi 2 secara default) | Klien dengan token `auth` |
| `http` | Proxy HTTP klasik (forward proxy) | Akun user/pass, tanpa pencatatan lalu lintas |
| `mixed` | Proxy gabungan SOCKS + HTTP | Akun user/pass |
| `tunnel` | Forwarder transparan (xray `dokodemo-door`) | Tanpa klien |
| `tun` | Antarmuka TUN (hanya untuk merender yang sudah ada) | Tanpa klien |
| `mtproto` | Proxy Telegram (MTProto), ditambahkan di 3.3.0; dikelola oleh proses `mtg` terpisah, bukan Xray | Tanpa klien (akses via secret) |

> Catatan tentang `tun`: nilai ini tetap ada dalam daftar untuk kompatibilitas dan **tampilan** inbound yang sebelumnya disimpan, namun pada versi saat ini backend tidak merekomendasikan pembuatannya — dukungannya dianggap usang. Membuat inbound baru bertipe ini tidak ada gunanya.

> Catatan tentang Hysteria 2: tidak ada protokol terpisah bernama «hysteria2». Ini adalah protokol `hysteria` dengan field `streamSettings.version = 2`. Skema link `hysteria2://` saat membuat share link dipilih secara otomatis ketika versi stream sama dengan 2.

Tidak semua protokol mendukung distribusi ke node. Hanya berikut yang dapat di-deploy ke node: `vless`, `vmess`, `trojan`, `shadowsocks`, `hysteria`, `wireguard`. Protokol `http`, `mixed`, `tunnel`, `tun`, `mtproto` hanya bekerja pada panel lokal.

### 5.2. Protokol mana yang mendukung TLS / REALITY / transport

Kemampuan untuk mengaktifkan lapisan keamanan atau transport tertentu bergantung pada protokol dan jaringan yang dipilih (`streamSettings.network`):

| Kemampuan | Tersedia untuk protokol | Jaringan yang diizinkan (`network`) |
|---|---|---|
| **TLS** | `vmess`, `vless`, `trojan`, `shadowsocks` (dan selalu untuk `hysteria`) | `tcp`, `ws`, `http`, `grpc`, `httpupgrade`, `xhttp` |
| **REALITY** | `vless`, `trojan` | `tcp`, `http`, `grpc`, `xhttp` |
| **flow (`xtls-rprx-vision`)** | hanya `vless` | hanya `tcp`, dengan `security = tls` atau `reality` |
| **Stream / transport** (tab «Aliran») | `vmess`, `vless`, `trojan`, `shadowsocks`, `hysteria` | — |

Untuk protokol `http`, `mixed`, `tunnel`, `tun`, `wireguard`, tab transport tidak tersedia — protokol-protokol ini tidak memiliki pengaturan stream Xray.

---

### 5.3. VLESS

Fungsi: protokol proxy modern utama. Mendukung XTLS-Vision (`flow`), REALITY, serta enkripsi post-quantum di level VLESS itu sendiri (field `decryption` / `encryption`). Digunakan secara default untuk inbound baru.

Field blok `settings`:

| Field | Nilai default | Deskripsi |
|---|---|---|
| `clients` | `[]` | Daftar klien. Setiap klien memiliki: `id` (UUID), `email` (wajib), `flow`, batas (`limitIp`, `totalGB`, `expiryTime`), `enable`, `tgId`, `subId`, `comment`, `reset` |
| `decryption` | `none` | Parameter dekripsi di sisi server. Label di UI: «Dekripsi» (Inggris: «Decryption») |
| `encryption` | `none` | Parameter enkripsi pasangan (masuk ke link klien). Label: «Enkripsi» (Inggris: «Encryption») |
| `fallbacks` | `[]` | Daftar fallback (lihat bagian tentang fallback); tersedia saat `network = tcp` dan `security` = TLS atau REALITY |
| `testseed` | (4 angka: 900, 500, 900, 256) | «Vision testseed» — 4 bilangan bulat positif untuk padding XTLS-Vision. Hanya diterapkan pada klien dengan flow `xtls-rprx-vision`, jika tidak diabaikan |

#### flow (`xtls-rprx-vision`)

`flow` ditetapkan **pada klien**, bukan pada inbound, dan menerima salah satu dari tiga nilai:

| Nilai | Arti |
|---|---|
| `` (kosong) | Tanpa XTLS-flow (default) |
| `xtls-rprx-vision` | XTLS-Vision — mode yang direkomendasikan untuk VLESS melalui TCP+TLS/REALITY |
| `xtls-rprx-vision-udp443` | Vision yang sama, namun dengan penanganan UDP/443 (QUIC) |

Field `flow` hanya dapat dipilih ketika semua kondisi terpenuhi: protokol `vless`, `network = tcp`, dan `security` = `tls` atau `reality`. Field **Vision testseed** di formulir hanya ditampilkan dalam kondisi yang sama.

> Pengecualian untuk XHTTP: pada VLESS melalui `network = xhttp` dengan autentikasi post-quantum VLESS yang diaktifkan (`encryption`/`decryption`, vlessenc), flow `xtls-rprx-vision` juga diizinkan — terlepas dari lapisan keamanan, termasuk dengan REALITY. Dalam kasus ini, panel meneruskan `xtls-rprx-vision` dengan benar ke share link dan langganan (termasuk format Clash/Mihomo), sehingga klien mendapatkan konfigurasi dengan Vision.

#### Dekripsi / Enkripsi (autentikasi post-quantum VLESS)

Field `decryption` dan `encryption` adalah autentikasi di level VLESS itu sendiri (terpisah dari TLS/REALITY transport). Secara default keduanya bernilai `none`. Di formulir terdapat tiga tombol berdampingan:

- **Autentikasi X25519** (Inggris: «X25519 auth») — membuat pasangan `decryption`/`encryption` berbasis X25519.
- **Autentikasi ML-KEM-768** (Inggris: «ML-KEM-768 auth») — varian post-quantum (Post-Quantum).
- **Hapus** — mereset kedua field kembali ke `none`.

Di bawah tombol ditampilkan baris status «Dipilih: {auth}», di mana nilai ditentukan berdasarkan segmen terakhir string `encryption`: kosong/`none` → «None», kunci sangat panjang (>300 karakter) → ML-KEM-768, pendek → X25519, lainnya «Kustom».

Secara teknis, tombol-tombol tersebut mengakses `GET /panel/api/server/getNewVlessEnc` (pembuatan kunci melalui `xray vlessenc`) dan mengisi **kedua** field dengan nilai berpasangan berupa `mlkem768x25519plus.native.<rtt>.<role>` (misalnya, `decryption = mlkem768x25519plus.native.600s.server-x25519`, `encryption = mlkem768x25519plus.native.0rtt.client-x25519`). Parameter `decryption` tetap di server, `encryption` dikirim ke link klien.

> Penting: saat membuat konfigurasi inbound untuk Xray, panel menghapus yang tidak diperlukan: jika `encryption` (yang mengacu ke sisi klien) tersisa di `settings`, ia **dihapus** dari konfigurasi server. Di server sendiri hanya tersisa `decryption`.

Kapan memilih VLESS: ini adalah pilihan default yang direkomendasikan untuk inbound baru, terutama dikombinasikan dengan REALITY (tanpa sertifikat sendiri) atau dengan TLS + XTLS-Vision.

**Contoh: blok `settings` inbound VLESS dengan satu klien dan XTLS-Vision.** Field `flow` berada di klien, `decryption` tetap di server:

```json
{
  "clients": [
    {
      "id": "d342d11e-d424-4583-b36e-524ab1f0afa4",
      "email": "user1",
      "flow": "xtls-rprx-vision",
      "limitIp": 2,
      "totalGB": 0,
      "expiryTime": 0,
      "enable": true
    }
  ],
  "decryption": "none"
}
```

Untuk kombinasi REALITY, blok `streamSettings` yang sesuai (tab «Transport» → Security: REALITY) terlihat seperti ini:

```json
{
  "network": "tcp",
  "security": "reality",
  "realitySettings": {
    "dest": "www.microsoft.com:443",
    "serverNames": ["www.microsoft.com"],
    "privateKey": "<приватный ключ X25519>",
    "shortIds": ["", "6ba85179e30d4fc2"]
  }
}
```

---

### 5.4. VMess

Fungsi: protokol proxy klasik Xray. Autentikasi menggunakan UUID, di sisi klien dapat dikonfigurasi metode enkripsi payload (`security`).

Field blok `settings`:

| Field | Nilai default | Deskripsi |
|---|---|---|
| `clients` | `[]` | Daftar klien |

Setiap klien VMess (selain field umum `email`, batas, `enable`, `tgId`, `subId`, `comment`, `reset`):

| Field klien | Nilai default | Deskripsi |
|---|---|---|
| `id` | — | UUID klien |
| `security` | `auto` | Metode enkripsi payload VMess. Nilai yang diizinkan: `aes-128-gcm`, `chacha20-poly1305`, `auto`, `none`, `zero` |

Nilai `security`:
- `auto` — Xray memilih cipher sendiri tergantung platform (direkomendasikan);
- `aes-128-gcm`, `chacha20-poly1305` — cipher AEAD tetap;
- `none` — tanpa enkripsi payload (hanya masuk akal di atas TLS);
- `zero` — tanpa enkripsi dan tanpa autentikasi payload.

> Kompatibilitas historis: record lama mungkin menyimpan `security: ""` — saat dibaca, string kosong dikonversi ke `auto`. Saat membuat konfigurasi server, field `security` pada klien VMess **dihapus** dari `settings`, karena tidak diperlukan untuk inbound.

Kapan memilih VMess: untuk kompatibilitas dengan klien lama atau konfigurasi yang sudah ada. Untuk deployment baru, VLESS biasanya lebih diutamakan.

---

### 5.5. Trojan

Fungsi: proxy yang meniru lalu lintas HTTPS biasa. Autentikasi menggunakan password. Seperti VLESS, mendukung fallback dan (ketika `network = tcp`) REALITY/TLS.

Field blok `settings`:

| Field | Nilai default | Deskripsi |
|---|---|---|
| `clients` | `[]` | Daftar klien |
| `fallbacks` | `[]` | Daftar fallback (tersedia saat `network = tcp` dan TLS/REALITY) |

Field utama setiap klien Trojan:

| Field klien | Nilai default | Deskripsi |
|---|---|---|
| `password` | — | Password klien (wajib, minimal 1 karakter) |
| `email` | — | Pengenal unik klien |

Field klien lainnya bersifat umum (`limitIp`, `totalGB`, `expiryTime`, `enable`, `tgId`, `subId`, `comment`, `reset`).

Kapan memilih Trojan: ketika diperlukan penyamaran sebagai HTTPS di port 443, termasuk dengan fallback ke web server (Nginx) untuk koneksi yang tidak diminta.

**Contoh: blok `settings` Trojan dengan fallback ke web server lokal.** Koneksi yang tidak diminta (tanpa password yang valid) diarahkan ke Nginx yang mendengarkan di `127.0.0.1:8080`:

```json
{
  "clients": [
    { "password": "S3cret-Pass-1", "email": "user1" }
  ],
  "fallbacks": [
    { "dest": "127.0.0.1:8080" }
  ]
}
```

Untuk fallback diperlukan `network = tcp` dan Security = TLS atau REALITY; jika tidak, field fallbacks tidak tersedia.

---

### 5.6. Shadowsocks

Fungsi: proxy Shadowsocks ringan. Mendukung cipher AEAD lama maupun metode SIP022 baru (`2022-blake3-*`). Dapat beroperasi dalam mode satu pengguna atau banyak pengguna.

Field blok `settings`:

| Field | Nilai default | Deskripsi |
|---|---|---|
| `method` | `2022-blake3-aes-256-gcm` | Metode enkripsi inbound. Label di UI: «Metode enkripsi» (Inggris: «Encryption method») |
| `password` | `` | Password inbound (untuk metode 2022 dibuat otomatis sesuai metode yang dipilih) |
| `network` | `tcp,udp` | Transport. Label: «Jaringan» (Inggris: «Network»). Pilihan: `tcp,udp` (TCP, UDP), `tcp`, `udp` |
| `clients` | `[]` | Daftar klien |
| `ivCheck` | `false` (nonaktif) | Toggle «ivCheck» — perlindungan dari penggunaan ulang IV |

#### Metode enkripsi (`method`)

Kumpulan yang diizinkan:

| Metode | Kategori |
|---|---|
| `aes-256-gcm` | AEAD usang |
| `chacha20-poly1305` | AEAD usang |
| `chacha20-ietf-poly1305` | AEAD usang |
| `xchacha20-ietf-poly1305` | AEAD usang |
| `2022-blake3-aes-128-gcm` | SS 2022 (direkomendasikan) |
| `2022-blake3-aes-256-gcm` | SS 2022 (default) |
| `2022-blake3-chacha20-poly1305` | SS 2022, satu pengguna |

Logika panel berdasarkan metode:
- **Metode 2022** (`2022-blake3-*`) dianggap sebagai «SS 2022». Metode `2022-blake3-chacha20-poly1305` — **satu pengguna** (multi-user tidak didukung); metode 2022 lainnya mendukung beberapa klien. Field password (dengan tombol pembuatan yang menyesuaikan panjang kunci dengan metode) ditampilkan di formulir khusus untuk metode 2022.
- **Cipher usang** (`aes-*`, `chacha20-*`) bekerja dengan skema klasik «satu metode + satu password».

> Normalisasi sebelum menjalankan Xray: untuk cipher usang, setiap klien harus memiliki `method` yang cocok dengan metode inbound (jika tidak, Xray gagal dengan «unsupported cipher method:»). Untuk metode 2022, sebaliknya — field `method` pada klien harus **kosong** (jika tidak, Xray menolak inbound dengan «users must have empty method»). Panel secara otomatis merapikan data saat metode diubah.

> Pembuatan ulang kunci klien saat ukuran kunci berubah: untuk Shadowsocks-2022, saat metode enkripsi diubah ke metode dengan ukuran kunci berbeda (misalnya antara `2022-blake3-aes-256-gcm` dan `2022-blake3-aes-128-gcm`), panel secara otomatis membuat ulang PSK klien untuk panjang baru saat inbound disimpan. Jika tidak, kunci lama akan tetap dengan panjang sebelumnya, dan Xray akan menolaknya. Konsekuensinya: klien yang terdampak perlu mendapatkan langganan baru — link lama tidak akan dapat terhubung.

Kapan memilih Shadowsocks: untuk deployment sederhana tanpa penyamaran TLS; pilihan modern — metode 2022-blake3.

**Contoh: blok `settings` Shadowsocks untuk metode 2022-blake3 (mode banyak pengguna).** Inbound memiliki passwordnya sendiri (kunci base64 dengan panjang yang sesuai), setiap klien memiliki passwordnya sendiri, field `method` klien **kosong**:

```json
{
  "method": "2022-blake3-aes-256-gcm",
  "password": "d2hhdGV2ZXItMzItYnl0ZS1iYXNlNjQta2V5LWhlcmU=",
  "network": "tcp,udp",
  "clients": [
    {
      "email": "user1",
      "password": "Y2xpZW50LWtleS0zMi1ieXRlcy1iYXNlNjQtaGVyZQ==",
      "method": ""
    }
  ]
}
```

Untuk cipher legacy (`aes-256-gcm` dan sejenisnya) — sebaliknya: satu password untuk inbound, dan `method` klien harus cocok dengan metode inbound.

---

### 5.7. Dokodemo-door / Tunnel (forwarder transparan)

Fungsi: forwarder transparan (di panel — protokol `tunnel`, yang mengimplementasikan perilaku `dokodemo-door`). Menerima lalu lintas dan meneruskannya ke alamat/port tertentu, tanpa autentikasi dan klien.

Field blok `settings`:

| Field | Nilai default | Deskripsi |
|---|---|---|
| `rewriteAddress` | (tidak ada) | «Tulis ulang alamat» (Inggris: «Rewrite address») — alamat tujuan ke mana lalu lintas diarahkan |
| `rewritePort` | (tidak ada) | «Tulis ulang port» (Inggris: «Rewrite port») — port tujuan (0–65535) |
| `allowedNetwork` | `tcp,udp` | «Jaringan yang diizinkan» (Inggris: «Allowed network»). Pilihan: `tcp,udp`, `tcp`, `udp` |
| `portMap` | `{}` | «Pemetaan port» — peta port→port (Record<string,string>) |
| `followRedirect` | `false` (nonaktif) | «Ikuti redirect» (Inggris: «Follow redirect») — gunakan alamat tujuan asli dari koneksi yang dicegat |

> Tab «Transport» untuk Tunnel: inbound tipe ini memiliki tab **«Transport»** yang terbatas pada pengaturan `sockopt` — ini cukup untuk mode **TProxy** (proxy transparan/redirect melalui `sockopt.tproxy`). Dropdown pemilihan transport (`network`) dan tab «Security» untuk Tunnel disembunyikan, karena TLS/REALITY tidak didukung oleh tipe ini.

Kapan memilih: untuk proxy transparan/pengalihan port ke layanan internal.

---

### 5.8. SOCKS / HTTP (protokol `mixed`)

Dalam build ini tidak ada protokol `socks` terpisah — SOCKS dan proxy HTTP digabungkan menjadi protokol **`mixed`** (gabungan SOCKS + HTTP). Selain itu, ada proxy `http` murni yang terpisah.

#### 5.8.1. Mixed (SOCKS + HTTP)

Field blok `settings`:

| Field | Nilai default | Deskripsi |
|---|---|---|
| `auth` | `password` | «Auth» — mode autentikasi. Pilihan: `password` (login/password) atau `noauth` (tanpa otorisasi) |
| `accounts` | (opsional) | «Akun» — daftar pasangan user/pass. Saat `auth = noauth`, field tidak ditulis ke konfigurasi |
| `udp` | `false` (nonaktif) | Toggle «UDP» — dukungan UDP melalui SOCKS |
| `ip` | `127.0.0.1` | «UDP IP» — alamat lokal untuk asosiasi UDP. Field hanya ditampilkan saat `udp` diaktifkan |

Akun ditambahkan dengan tombol «Tambah»; saat ditambahkan, login acak (8 karakter) dan password (12 karakter) dibuat, yang dapat diedit.

#### 5.8.2. HTTP (proxy murni)

Fungsi: forward proxy HTTP klasik. Di level Xray tidak melacak klien sebagai «billing» (tidak ada email/batas) — hanya ada daftar akun.

Field blok `settings`:

| Field | Nilai default | Deskripsi |
|---|---|---|
| `accounts` | `[]` | «Akun» — daftar pasangan user/pass (kedua field wajib) |
| `allowTransparent` | `false` (nonaktif) | «Izinkan transparan» (Inggris: «Allow transparent») — teruskan permintaan dengan header Host asli |

Kapan memilih SOCKS/HTTP: untuk akses proxy lokal atau layanan tanpa penyamaran yang rumit. `mixed` praktis karena satu port melayani klien SOCKS maupun HTTP.

---

### 5.9. WireGuard (inbound)

Fungsi: inbound WireGuard. Berbeda dengan protokol proxy, ia tidak beroperasi dengan «klien» — melainkan dikonfigurasi dengan **peer** (perangkat yang diterima server). Transport dan TLS/REALITY tidak berlaku untuknya.

Field blok `settings`:

| Field | Nilai default | Deskripsi |
|---|---|---|
| `secretKey` | — | Kunci privat server (wajib). Terdapat tombol pembuatan di sampingnya; kunci publik ditampilkan otomatis (field hanya baca) |
| `mtu` | (opsional) | MTU antarmuka |
| `noKernelTun` | `false` (nonaktif) | «TUN tanpa kernel» (Inggris: «No-kernel TUN») — gunakan userspace-TUN alih-alih kernel |
| `domainStrategy` | (opsional) | «Domain Strategy» — strategi resolving domain: `ForceIP`, `ForceIPv4`, `ForceIPv4v6`, `ForceIPv6`, `ForceIPv6v4` |
| `peers` | `[]` | Daftar peer |

Field setiap peer:

| Field peer | Nilai default | Deskripsi |
|---|---|---|
| `privateKey` | (opsional) | Kunci privat klien — disimpan agar panel dapat merender konfigurasi untuk pengguna (hanya untuk inbound peer) |
| `publicKey` | — | Kunci publik peer (wajib) |
| `preSharedKey` (PSK) | (opsional) | Kunci bersama tambahan |
| `allowedIPs` | `[]` | IP yang diizinkan. Saat menambahkan peer baru, panel secara otomatis menyarankan alamat bebas berikutnya (default `10.0.0.2/32`) |
| `keepAlive` | (opsional) | «Keep-alive» — interval pemeliharaan koneksi |
| `comment` | (opsional) | «Comment» — label bebas peer; ditampilkan di samping heading «Peer N» dan dimasukkan ke link berbagi serta ke `remark` file `.conf` |

Tombol «Tambah peer» membuat pasangan kunci baru dan mengisi `allowedIPs` berikutnya. Setiap peer dapat dihapus (penghapusan tidak tersedia untuk peer yang tersisa satu-satunya).

Field «Comment» pada peer membantu membedakan perangkat: teksnya ditampilkan di formulir di samping heading «Peer N», serta masuk ke link berbagi dan ke `remark` file `.conf` yang dibuat, sehingga perangkat mudah dikenali di aplikasi klien. Field ini bersifat panel — xray-core mengabaikan field peer yang tidak dikenal.

#### Domain Strategy dan tab Transport

Selain peer, inbound WireGuard memiliki field **Domain Strategy** (strategi resolving domain: `ForceIP`, `ForceIPv4`, `ForceIPv4v6`, `ForceIPv6`, `ForceIPv6v4`). Field ini opsional dan hanya ditulis ke konfigurasi jika ditetapkan.

> Field **Workers** (`workers`, jumlah thread pekerja) dihapus dari formulir WireGuard (baik inbound maupun outbound): mulai xray-core v26.6.22, mesin tidak lagi menggunakannya dan mengandalkan mekanisme internal wireguard-go. Konfigurasi yang sebelumnya disimpan berfungsi tanpa perubahan — saat diurai, field tersebut diabaikan begitu saja, migrasi tidak diperlukan.

Untuk WireGuard juga tersedia tab **«Transport»** — namun dalam bentuk terbatas: hanya `sockopt` dan obfuskasi **Finalmask** yang dapat dikonfigurasi di sana. Dropdown pemilihan transport (`network`) disembunyikan, karena WireGuard selalu mendengarkan melalui UDP. Dalam entri noise (noise), Finalmask memiliki field terpisah **Rand Range** (rentang byte 0–255, dengan validasi), dan sebagai metode obfuskasi untuk WireGuard dan Hysteria tersedia **Salamander**.

Kapan memilih WireGuard: ketika diperlukan tunnel VPN WireGuard yang sesungguhnya, bukan proxy berkamuflase.

---

### 5.10. Hysteria (default v2)

Fungsi: inbound Hysteria melalui QUIC. Panel secara default bekerja dengan versi 2. Setiap klien diautentikasi dengan token `auth` alih-alih UUID/password. TLS untuk Hysteria selalu tersedia (lihat tabel kemampuan di 5.2).

Field blok `settings`:

| Field | Nilai default | Deskripsi |
|---|---|---|
| `version` | `2` | Versi protokol (minimal 1; default panel 2) |
| `clients` | `[]` | Daftar klien |

Field utama setiap klien adalah `auth` (token, wajib) ditambah field umum (`email`, batas, `enable`, `tgId`, `subId`, `comment`, `reset`).

Parameter tambahan ditetapkan di `streamSettings.hysteriaSettings`:

| Field | Nilai / pilihan | Deskripsi |
|---|---|---|
| `version` | dikunci ke 2 (field dinonaktifkan) | «Versi» (Inggris: «Version») |
| `udpIdleTimeout` | (bilangan bulat ≥ 1, detik) | «UDP idle timeout (detik)» — batas waktu idle UDP |
| `masquerade` | nonaktif secara default | «Masquerade» — penyamaran sebagai web server biasa untuk permintaan «yang tidak diminta» |

Saat `masquerade` diaktifkan, tersedia pilihan tipe (`type`):
- `` — default (halaman 404);
- `proxy` — reverse proxy (field «Upstream URL», «Tulis ulang Host», «Lewati TLS verify»);
- `file` — penyajian direktori (field «Direktori», misalnya `/var/www/html`);
- `string` — respons tetap (field «Kode status», «Body», «Header»).

Kapan memilih Hysteria: ketika diperlukan transport QUIC dan ketahanan pada saluran yang tidak stabil/mobile; masquerade meningkatkan ketersembunyian titik masuk.

---

### 5.11. MTProto (proxy untuk Telegram)

> Ditambahkan pada versi **3.3.0**. Nilai protokol — `mtproto`.

MTProto adalah protokol proxy bawaan Telegram. Dalam 3X-UI, inbound semacam ini **tidak dikelola oleh Xray, melainkan oleh proses `mtg` terpisah** yang dikendalikan panel itu sendiri. Panel secara berkala memeriksa inbound MTProto yang diaktifkan terhadap proses `mtg` yang berjalan: memulai yang hilang, menghentikan yang berlebih, dan mengambil penghitung lalu lintas dari metrik `mtg`. Oleh karena itu, **pencatatan lalu lintas** untuk inbound semacam ini bekerja seperti protokol biasa.

Petunjuk resmi di formulir:

> «MTProto dikelola oleh proses mtg terpisah, bukan Xray. Pengaturan transport dan klien tidak berlaku di sini — bagikan link di bawah melalui Telegram.»

Konsekuensinya:

- Tab **«Transport» (Stream Settings) dan «Klien» tidak berlaku untuk inbound ini** — akses ditentukan oleh satu secret, bukan daftar klien.
- Inbound MTProto hanya berjalan **di panel utama**; inbound ini tidak di-deploy ke node anak (inbound dengan `NodeID` yang ditetapkan dilewati).

- Tab **«Sniffing»** untuk MTProto disembunyikan — protokol ini dikelola oleh proses `mtg`, bukan Xray, sehingga sniffing tidak berlaku untuknya.

**Field.** Disimpan di `settings` inbound:

| Field di UI | Kunci | Deskripsi |
|---|---|---|
| Remark | `remark` | Label inbound. |
| Listen IP | `listen` | IP untuk mendengarkan (kosong = semua antarmuka). |
| Port | `port` | Port proxy. |
| Secret | `settings.secret` | Secret akses dalam format **FakeTLS**. |
| Domain penyamaran (FakeTLS) | `settings.fakeTlsDomain` | Domain yang digunakan sebagai kedok untuk lalu lintas HTTPS proxy. |

**Format secret (FakeTLS).** Panel secara otomatis mengonversi secret ke format yang benar: hasilnya = `ee` + 32 karakter hex + kode hex domain penyamaran, yaitu `ee<hex32><hex(fakeTlsDomain)>`. Prefiks `ee` mengaktifkan mode FakeTLS, dan domain (misalnya, situs terkenal) digunakan untuk menyamarkan lalu lintas sebagai HTTPS biasa. Cukup tentukan domain — panel akan melengkapi sisanya secara otomatis.

#### Domain-fronting dan opsi lanjutan mtg

Inbound MTProto memiliki parameter proses `mtg` tambahan. Field **Domain fronting IP**, **Domain fronting port**, dan **Domain fronting PROXY protocol** menentukan ke mana `mtg` mengirim lalu lintas non-Telegram (misalnya, ke situs NGINX palsu): jika IP dibiarkan kosong, domain FakeTLS digunakan melalui DNS, port default — `443`. Selain itu tersedia **Accept PROXY protocol** (untuk listener), **IP preference** (`prefer-ipv6` / `prefer-ipv4` / `only-ipv6` / `only-ipv4`) dan **Debug logging**. Setiap nilai ditulis ke file `mtg-<id>.toml` hanya jika ditetapkan.

#### Merutekan lalu lintas Telegram melalui Xray

Toggle **«Route through Xray»** (nonaktif secara default) dan field **Outbound** opsional memungkinkan egress Telegram disubordinasikan ke router Xray. Saat diaktifkan, panel menyematkan jembatan SOCKS lokal dengan tag inbound itu sendiri ke dalam konfigurasi Xray, dan `mtg` mengirimkan lalu lintas Telegram melaluinya. Setelah itu, lalu lintas dapat dicocokkan dengan aturan di tab «Routing» atau secara paksa diarahkan ke outbound atau balancer yang dipilih melalui field **Outbound** (jika field kosong, keputusan diambil oleh aturan routing).

**Cara berbagi dengan pengguna.** Untuk inbound MTProto, panel membuat link undangan:

**Contoh: secret FakeTLS dan link siap pakai.** Jika domain penyamaran adalah `www.cloudflare.com`, secret dirakit sebagai `ee` + 32 karakter hex + kode hex domain, misalnya:

```
secret = ee1a2b3c4d5e6f70819293a4b5c6d7e8f7777772e636c6f7564666c6172652e636f6d
```

Link undangan siap pakai (link ini beserta QR code dikirimkan ke pengguna melalui Telegram):

```
tg://proxy?server=203.0.113.10&port=443&secret=ee1a2b3c4d5e6f70819293a4b5c6d7e8f7777772e636c6f7564666c6172652e636f6d
```

```
tg://proxy?server=<адрес>&port=<порт>&secret=<секрет>
```

(ekuivalen — `https://t.me/proxy?server=…&port=…&secret=…`). Link ini dan QR code perlu dikirimkan ke pengguna Telegram — saat dibuka, proxy langsung ditambahkan ke aplikasi. Link juga tersedia melalui server langganan.

**Kapan digunakan.** Cara standar untuk melewati pemblokiran Telegram; masquerade FakeTLS (domain penyamaran) membuat lalu lintas terlihat seperti kunjungan biasa ke situs yang ditentukan.

### 5.12. Ringkasan pemilihan protokol

- **VLESS** — pilihan default; opsi terbaik dengan REALITY atau TLS + XTLS-Vision, mendukung autentikasi post-quantum.
- **Trojan** — penyamaran sebagai HTTPS dengan fallback ke web server.
- **VMess** — kompatibilitas dengan klien lama.
- **Shadowsocks** — proxy sederhana tanpa TLS; pilihan modern — metode `2022-blake3-*`.
- **Hysteria** — QUIC, ketahanan pada saluran buruk.
- **mixed / http** — proxy SOCKS/HTTP untuk layanan.
- **WireGuard** — tunnel VPN lengkap.
- **tunnel** — pengalihan port transparan.
- **MTProto** — proxy untuk melewati pemblokiran Telegram (FakeTLS); proses `mtg` terpisah.

---

## 6. Transport (Stream Settings)

Transport (di antarmuka panel — kolom **«Transport»**, Ingg. *Transmission*) menentukan cara Xray-core mengirimkan data di dalam inbound: protokol jaringan apa yang digunakan di atas TLS/Reality dan bagaimana lalu lintas dibingkai. Parameter ini disimpan dalam objek `streamSettings` konfigurasi Xray dan diatur pada tab transport di editor inbound. Enkripsi (TLS / Reality) dibahas di bagian terpisah — di sini hanya dijelaskan pemilihan jaringan dan parameternya.

### 6.1. Pemilihan Jaringan Transmisi

Jaringan dipilih dari daftar dropdown **«Transport»** (`streamSettings.network`). Nilai default adalah `tcp` (ditampilkan dalam daftar sebagai **RAW**). Opsi yang tersedia:

| Nilai dalam daftar | Kolom `network` | Transport |
| --- | --- | --- |
| RAW | `tcp` | TCP biasa (diganti nama menjadi RAW pada versi Xray terbaru), opsional dengan obfuskasi HTTP |
| mKCP | `kcp` | Transport UDP andal mKCP |
| WebSocket | `ws` | WebSocket di atas HTTP(S) |
| gRPC | `grpc` | Terowongan gRPC (HTTP/2) |
| HTTPUpgrade | `httpupgrade` | HTTP Upgrade |
| XHTTP | `xhttp` | XHTTP / SplitHTTP — transport bermultipleks modern |

Saat nilai diubah, panel mengosongkan blok pengaturan jaringan sebelumnya dan mengisi blok jaringan baru dengan nilai default dari skemanya, sehingga setiap kolom sub-form selalu memiliki nilai awal yang bermakna.

> **Penting.** Pada build panel ini **transport HTTP/2 (`h2`) tidak tersedia dalam daftar** — transport tersebut telah dihapus dari kumpulan jaringan; untuk terowongan dua arah mirip HTTP/2 digunakan gRPC, sedangkan untuk transport modern berbalut HTTP digunakan XHTTP. Transport **Hysteria** (`hysteria`) tidak dipilih melalui daftar ini: transport tersebut terikat erat dengan protokol Hysteria dan muncul secara otomatis ketika inbound dibuat dengan protokol Hysteria (lihat poin 6.8).

Di bawah ini setiap jaringan dan setiap kolomnya dibahas secara terpisah.

---

### 6.2. RAW / TCP (`tcpSettings`)

Transport TCP dasar. Secara default lalu lintas dikirim apa adanya; secara opsional dapat disamarkan sebagai pertukaran HTTP/1.1 biasa.

| Kolom | Nilai default | Deskripsi |
| --- | --- | --- |
| Proxy Protocol (`acceptProxyProtocol`) | `false` (nonaktif) | Menerima header PROXY protocol dari load balancer/proksi hulu |
| Obfuskasi HTTP (`header.type`) | `none` (nonaktif) | Mengaktifkan penyamaran lalu lintas sebagai HTTP/1.1 |

#### Proxy Protocol

Sakelar **«Proxy Protocol»** (`acceptProxyProtocol`). Saat diaktifkan, Xray mengharapkan header PROXY protocol pada koneksi masuk dan mengekstrak IP asli klien darinya. Aktifkan hanya jika terdapat reverse proxy/load balancer di depan panel (misalnya HAProxy atau nginx dengan `send-proxy`) yang menambahkan header tersebut. Dinonaktifkan secara default.

#### Obfuskasi HTTP (camouflage)

Sakelar **«HTTP Obfuskasi»**. Mengontrol kolom `header`:

- **Nonaktif** → `header.type = "none"` (kolom `header` tidak ada pada paket). TCP murni.
- **Aktif** → `header.type = "http"`. Lalu lintas dibingkai menyerupai permintaan dan respons HTTP/1.1. Saat diaktifkan, panel langsung mengisi sub-objek `request` dan `response` dengan nilai default.

Saat obfuskasi HTTP diaktifkan, kolom pengaturan permintaan dan respons yang ditiru menjadi tersedia.

**Header permintaan (`header.request`):**

| Kolom | Kunci | Nilai default | Deskripsi |
| --- | --- | --- | --- |
| Versi permintaan | `request.version` | `1.1` | Versi HTTP dalam baris awal permintaan |
| Metode permintaan | `request.method` | `GET` | Metode HTTP permintaan yang ditiru |
| Path permintaan | `request.path` | `/` | Path. Dimasukkan sebagai daftar nilai yang dipisahkan koma; pada paket berupa array string. Jika dikosongkan, maka digunakan `/` |
| Header permintaan | `request.headers` | `{}` (kosong) | Tabel «Nama/Nilai» header HTTP. Disimpan sebagai peta `nama → [nilai]` (satu nama dapat memiliki beberapa nilai) |

**Header respons (`header.response`):**

| Kolom | Kunci | Nilai default | Deskripsi |
| --- | --- | --- | --- |
| Versi respons | `response.version` | `1.1` | Versi HTTP dalam baris awal respons |
| Status respons | `response.status` | `200` | Kode status HTTP respons yang ditiru |
| Alasan respons | `response.reason` | `OK` | Deskripsi teks status (reason-phrase) |
| Header respons | `response.headers` | `{}` (kosong) | Tabel «Nama/Nilai» header respons (peta `nama → [nilai]`) |

Kolom header diedit baris per baris — setiap baris menentukan nama header (`Nama`) dan nilainya (`Nilai`). Parameter ini hanya digunakan untuk menyamarkan tampilan lalu lintas; tidak memengaruhi kriptografi. Nilai default (`GET / HTTP/1.1`, respons `200 OK`) cocok untuk sebagian besar skenario — ubah hanya jika perlu meniru situs/layanan tertentu.

**Contoh `streamSettings` untuk RAW dengan obfuskasi HTTP:**

```json
{
  "network": "tcp",
  "tcpSettings": {
    "acceptProxyProtocol": false,
    "header": {
      "type": "http",
      "request": {
        "version": "1.1",
        "method": "GET",
        "path": ["/"],
        "headers": {
          "Host": ["www.example.com"]
        }
      },
      "response": {
        "version": "1.1",
        "status": "200",
        "reason": "OK"
      }
    }
  }
}
```

Perhatikan: `path` pada paket adalah array string, dan setiap header adalah array nilai (`Host → ["www.example.com"]`).

---

### 6.3. mKCP (`kcpSettings`)

mKCP adalah transport andal di atas UDP. Berguna pada saluran dengan kehilangan paket dan latensi tinggi, tetapi menghasilkan overhead lalu lintas yang lebih besar. Semua nilai default sesuai dengan yang direkomendasikan oleh xray-core.

| Kolom | Kunci | Default | Nilai yang diizinkan | Deskripsi |
| --- | --- | --- | --- | --- |
| MTU | `mtu` | `1350` | 576–1460 | Ukuran paket maksimum (byte). Kurangi jika terjadi masalah fragmentasi |
| TTI (ms) | `tti` | `20` | 10–100 | Interval transmisi (ms). Lebih kecil = latensi lebih rendah, tetapi overhead lebih besar |
| Uplink (MB/s) | `uplinkCapacity` | `5` | ≥ 0 | Estimasi kapasitas bandwidth upload (MB/s) |
| Downlink (MB/s) | `downlinkCapacity` | `20` | ≥ 0 | Estimasi kapasitas bandwidth download (MB/s) |
| Pengali CWND | `cwndMultiplier` | `1` | ≥ 1 | Pengali congestion window |
| Maks. jendela pengiriman | `maxSendingWindow` | `2097152` | ≥ 0 | Ukuran maksimum jendela pengiriman |

Catatan kolom:
- **Uplink / Downlink capacity** menentukan seberapa agresif mKCP menggunakan saluran. Sesuaikan dengan lebar pita saluran yang sebenarnya: nilai terlalu tinggi menyebabkan lalu lintas berlebih, nilai terlalu rendah menyebabkan saluran tidak dimanfaatkan secara optimal.
- **TTI** secara langsung memengaruhi kompromi «latensi ↔ overhead»: nilai lebih kecil mengurangi latensi tetapi meningkatkan volume paket overhead.
- **MTU** membatasi ukuran satu paket mKCP; pengurangan membantu pada saluran di mana paket UDP besar dipotong atau hilang.

> Pada build ini kolom «seed» (kata sandi obfuskasi mKCP) dan daftar dropdown **jenis header/obfuskasi** (`none`, `srtp`, `utp`, `wechat-video`, `dtls`, `wireguard`) di sub-form mKCP **tidak tersedia sebagai kolom terpisah** — obfuskasi lapisan transport dipindahkan ke mekanisme umum «FinalMask» (termasuk mode `mkcp-legacy`), yang dijelaskan di bagian tersendiri. Parameter «congestion» sebagai kotak centang terpisah juga tidak ditampilkan; kontrol kemacetan diatur melalui `cwndMultiplier` dan `maxSendingWindow`.

---

### 6.4. WebSocket (`wsSettings`)

Transport WebSocket di atas HTTP(S). Melewati CDN dan reverse proxy dengan baik, menyamar sebagai lalu lintas web biasa.

| Kolom | Kunci | Default | Deskripsi |
| --- | --- | --- | --- |
| Proxy Protocol | `acceptProxyProtocol` | `false` | Menerima header PROXY protocol dari proksi hulu (lihat poin 6.2) |
| Host | `host` | `""` (kosong) | Nilai header HTTP `Host`. Tentukan saat bekerja melalui CDN/domain fronting |
| Path | `path` | `/` | Path dalam string permintaan handshake WebSocket |
| Periode heartbeat | `heartbeatPeriod` | `0` | Interval pengiriman frame heartbeat (dalam detik). `0` menonaktifkan heartbeat |
| Header | `headers` | `{}` (kosong) | Header HTTP tambahan untuk handshake. Peta «Nama → Nilai» (hanya nilai string, tanpa array) |

Catatan:
- **Path** harus cocok antara server (inbound) dan klien. Sering kali titik masuk disamarkan di balik path ini pada sisi web server.
- **Host** perlu ditentukan jika inbound berada di balik CDN atau menggunakan domain fronting; jika tidak, bisa dibiarkan kosong.
- **Periode heartbeat** menjaga koneksi «tetap hidup» saat melewati proksi/CDN yang secara agresif memutus sesi tidak aktif. Secara default (`0`) heartbeat dinonaktifkan.
- Berbeda dengan RAW, tabel header WebSocket menggunakan format «datar» `nama → nilai` (satu baris nilai per header).

**Contoh `streamSettings` untuk WebSocket di balik CDN:**

```json
{
  "network": "ws",
  "wsSettings": {
    "acceptProxyProtocol": false,
    "host": "cdn.example.com",
    "path": "/ray",
    "heartbeatPeriod": 0,
    "headers": {
      "User-Agent": "Mozilla/5.0"
    }
  }
}
```

Nilai `host` dan `path` harus cocok di sisi klien; berbeda dengan RAW, nilai header di sini adalah string biasa, bukan array.

---

### 6.5. gRPC (`grpcSettings`)

Transport dengan jumlah parameter paling sedikit. Melakukan tunneling lalu lintas di dalam panggilan gRPC (di atas HTTP/2); kompatibel dengan CDN yang mendukung gRPC. Tidak ada obfuskasi header.

| Kolom | Kunci | Default | Deskripsi |
| --- | --- | --- | --- |
| Nama layanan (`Service Name`) | `serviceName` | `""` (kosong) | Nama layanan gRPC (secara efektif — «path» terowongan). Harus cocok antara server dan klien |
| Authority | `authority` | `""` (kosong) | Nilai pseudo-header `:authority` (setara `Host` untuk HTTP/2). Tentukan saat bekerja melalui CDN/domain |
| Multi Mode | `multiMode` | `false` (nonaktif) | Mengaktifkan multipleksing beberapa aliran gRPC paralel dalam satu koneksi |

Catatan:
- **Service Name** adalah pengenal utama saluran gRPC; harus sama di kedua sisi. Nilai kosong diizinkan, tetapi biasanya digunakan string tidak jelas untuk penyamaran.
- **Authority** memengaruhi `:authority` yang dikirim dalam frame HTTP/2; terutama diperlukan saat melakukan proxy melalui CDN.
- **Multi Mode** memungkinkan beberapa aliran logis melewati satu koneksi fisik; aktifkan untuk meningkatkan performa ketika server dan klien mendukungnya.

**Contoh `streamSettings` untuk gRPC:**

```json
{
  "network": "grpc",
  "grpcSettings": {
    "serviceName": "GunService",
    "authority": "grpc.example.com",
    "multiMode": false
  }
}
```

`serviceName` (di sini `GunService`) berperan sebagai «path» terowongan dan harus cocok antara server dan klien.

---

### 6.6. HTTPUpgrade (`httpupgradeSettings`)

Transport berdasarkan mekanisme HTTP `Upgrade` (seperti WebSocket, tetapi tanpa protokol WebSocket itu sendiri). Juga melewati proksi dan CDN dengan baik. Kumpulan kolom menyerupai WebSocket, tetapi **tanpa** periode heartbeat.

| Kolom | Kunci | Default | Deskripsi |
| --- | --- | --- | --- |
| Proxy Protocol | `acceptProxyProtocol` | `false` | Menerima header PROXY protocol dari proksi hulu |
| Host | `host` | `""` (kosong) | Nilai header HTTP `Host` |
| Path | `path` | `/` | Path permintaan HTTP dengan header `Upgrade` |
| Header | `headers` | `{}` (kosong) | Header HTTP tambahan. Peta «datar» `nama → nilai` (seperti WebSocket) |

Fungsi kolom **Host**, **Path**, dan **Header** sama dengan WebSocket (poin 6.4). Heartbeat tidak tersedia untuk HTTPUpgrade — itu adalah fitur khusus WebSocket.

---

### 6.7. XHTTP / SplitHTTP (`xhttpSettings`)

XHTTP (alias SplitHTTP) adalah transport HTTP bermultipleks modern dari xray-core. Memisahkan aliran uplink dan downlink menjadi permintaan HTTP terpisah, yang sangat cocok untuk CDN dan lingkungan dengan batasan durasi koneksi. Tidak semua kolom ditampilkan sekaligus di editor: sebagian muncul tergantung pada mode yang dipilih (`mode`) dan sakelar yang diaktifkan.

#### Kolom dasar (selalu terlihat)

| Kolom | Kunci | Default | Deskripsi |
| --- | --- | --- | --- |
| Host | `host` | `""` (kosong) | Nilai header HTTP `Host` |
| Path | `path` | `/` | Path dasar permintaan HTTP |
| Mode (`Mode`) | `mode` | `auto` | Mode transmisi (lihat di bawah) |
| Server Max Header Bytes | `serverMaxHeaderBytes` | `0` | Batas ukuran header permintaan di server (byte). `0` — nilai default xray-core |
| Padding Bytes | `xPaddingBytes` | `100-1000` | Rentang padding acak (dalam byte, format `min-maks`) untuk mempersulit analisis ukuran |
| Header | `headers` | `{}` (kosong) | Header HTTP tambahan. Peta «datar» `nama → nilai` |
| Metode HTTP Uplink | `uplinkHTTPMethod` | `""` (Default = POST) | Metode HTTP untuk permintaan uplink. Pilihan: kosong (default POST), `POST`, `PUT`, `GET` (terakhir hanya tersedia dalam mode `packet-up`) |
| Padding Obfs Mode | `xPaddingObfsMode` | `false` (nonaktif) | Mengaktifkan obfuskasi padding lanjutan dan membuka kolom tambahan (lihat di bawah) |
| No SSE Header | `noSSEHeader` | `false` (nonaktif) | Tidak mengirim header `Content-Type: text/event-stream` (SSE). Aktifkan jika header tersebut mengganggu penerusan melalui node perantara |

#### Kolom «Mode» (`mode`)

Daftar dropdown dengan nilai:

| Nilai | Deskripsi |
| --- | --- |
| `auto` | Pemilihan mode otomatis (default) |
| `packet-up` | Aliran uplink dipecah menjadi permintaan HTTP terpisah (satu paket per permintaan) |
| `stream-up` | Aliran uplink dikirim dalam satu permintaan streaming panjang |
| `stream-one` | Satu permintaan streaming dua arah bersama |

Pilihan mode menentukan kolom tambahan mana yang menjadi terlihat.

**Kolom yang terlihat hanya saat `mode = packet-up`:**

| Kolom | Kunci | Default | Deskripsi |
| --- | --- | --- | --- |
| Maks. upload yang di-buffer | `scMaxBufferedPosts` | `30` | Jumlah maksimum permintaan POST uplink yang di-buffer secara bersamaan |
| Maks. ukuran upload (byte) | `scMaxEachPostBytes` | `1000000` | Ukuran maksimum satu permintaan POST uplink (byte) |
| Uplink Data Placement | `uplinkDataPlacement` | `""` (Default = body) | Tempat menempatkan data uplink: `body`, `header`, `cookie`, `query` |
| Uplink Data Key | `uplinkDataKey` | `""` | Nama kunci/header untuk data uplink. Muncul hanya jika `uplinkDataPlacement` ditentukan dan bukan `body` |

**Kolom yang terlihat hanya saat `mode = stream-up`:**

| Kolom | Kunci | Default | Deskripsi |
| --- | --- | --- | --- |
| Stream-Up Server | `scStreamUpServerSecs` | `20-80` | Rentang waktu mempertahankan koneksi streaming server (dalam detik, format `min-maks`) |

#### Kolom obfuskasi padding (terlihat saat `xPaddingObfsMode = aktif`)

| Kolom | Kunci | Default | Deskripsi |
| --- | --- | --- | --- |
| Padding Key | `xPaddingKey` | `""` (placeholder `x_padding`) | Nama kunci untuk padding |
| Padding Header | `xPaddingHeader` | `""` (placeholder `X-Padding`) | Nama header HTTP tempat padding dikirim |
| Padding Placement | `xPaddingPlacement` | `""` (Default = queryInHeader) | Tempat menempatkan padding: `queryInHeader`, `header`, `cookie`, `query` |
| Padding Method | `xPaddingMethod` | `""` (Default = repeat-x) | Metode pembuatan padding: `repeat-x` atau `tokenish` |

#### Penempatan sesi dan urutan (selalu terlihat)

| Kolom | Kunci | Default | Deskripsi |
| --- | --- | --- | --- |
| Session ID Placement | `sessionIDPlacement` | `""` (Default = path) | Tempat mengirimkan ID sesi: `path`, `header`, `cookie`, `query` |
| Session ID Key | `sessionIDKey` | `""` (placeholder `x_session`) | Nama kunci sesi. Muncul hanya jika `sessionIDPlacement` ditentukan dan bukan `path` |
| Session ID Table | `sessionIDTable` | `""` (placeholder `Base62`) | Kumpulan karakter untuk menghasilkan ID sesi. Dapat dipilih dari daftar dropdown autocomplete yang telah ditentukan (`ALPHABET`, `Alphabet`, `BASE36`, `Base62`, `HEX`, `alphabet`, `base36`, `hex`, `number`) atau dimasukkan string ASCII arbitrer. Kosong — nilai default xray-core |
| Session ID Length | `sessionIDLength` | `""` (kosong) | Panjang atau rentang (misalnya `8-16`) ID yang dihasilkan. Ditampilkan hanya saat `Session ID Table` ditentukan; nilai minimum harus lebih dari 0 |
| Sequence Placement | `seqPlacement` | `""` (Default = path) | Tempat mengirimkan nomor urut paket: `path`, `header`, `cookie`, `query` |
| Sequence Key | `seqKey` | `""` (placeholder `x_seq`) | Nama kunci urutan. Muncul hanya jika `seqPlacement` ditentukan dan bukan `path` |

Kolom sesi diganti namanya sesuai xray-core v26.6.22: sebelumnya disebut **Session Placement** / **Session Key** (`sessionPlacement` / `sessionKey`) — sekarang menjadi **Session ID Placement** / **Session ID Key** (`sessionIDPlacement` / `sessionIDKey`); nama lama tidak lagi dipahami oleh core. Inbound yang disimpan sebelum pembaruan dimigrasikan ke kunci baru secara otomatis — tidak perlu disimpan ulang.

Rekomendasi:
- Untuk sebagian besar instalasi, cukup biarkan **Mode = `auto`**, tentukan **Path**/**Host**, dan (saat bekerja melalui CDN) selaraskan dengan klien.
- Kolom penempatan (`*Placement`/`*Key`) dan obfuskasi padding hanya diperlukan untuk penyesuaian halus pada skenario anti-DPI/CDN tertentu; saat nilai dikosongkan, nilai default xray-core yang ditunjukkan dalam tanda kurung akan digunakan.
- Parameter yang berkaitan dengan sisi klien/outbound (misalnya, interval pengiriman ulang POST, ukuran chunk) tidak ditampilkan dalam form inbound — server listener mengabaikannya. Sebaliknya, multipleksor XMUX tersedia dalam form inbound (lihat di bawah).

- **Default layanan tidak diterapkan.** Panel tidak lagi menulis nilai default layanan `scMaxEachPostBytes` dan `scMinPostsIntervalMs` ke konfigurasi XHTTP — nilai internal xray-core yang digunakan. Ini menghilangkan tanda tangan DPI tetap (literal `scMinPostsIntervalMs=30`) yang sebelumnya dapat menyebabkan pemblokiran lalu lintas. Untuk inbound yang sudah disimpan, nilai yang cocok dengan default xray-core tidak ditampilkan dalam tautan dan subscription (tidak perlu menyimpan ulang inbound); nilai yang diatur secara manual tetap tersimpan.

**Contoh `streamSettings` untuk XHTTP (mode `auto`):**

```json
{
  "network": "xhttp",
  "xhttpSettings": {
    "host": "xhttp.example.com",
    "path": "/yourpath",
    "mode": "auto",
    "xPaddingBytes": "100-1000"
  }
}
```

Untuk sebagian besar instalasi, keempat kolom ini sudah cukup; kolom penempatan sesi/urutan dan obfuskasi padding dibiarkan kosong — nilai default xray-core yang akan digunakan.

#### XMUX (multipleksing koneksi)

Sakelar **XMUX** (`enableXmux`) mengaktifkan lapisan multipleksing yang mendistribusikan permintaan paralel ke sejumlah kecil koneksi fisik. Saat diaktifkan, enam kolom konfigurasi tersedia (disimpan dalam `xhttpSettings.xmux`):

| Kolom | Kunci | Default | Deskripsi |
| --- | --- | --- | --- |
| Max Concurrency | `maxConcurrency` | `16-32` | Jumlah maksimum permintaan bersamaan per koneksi (rentang `min-maks`) |
| Max Connections | `maxConnections` | `0` | Jumlah maksimum koneksi fisik (`0` — tanpa batas) |
| Max Reuse Times | `cMaxReuseTimes` | `""` (kosong) | Berapa kali koneksi dapat digunakan kembali |
| Max Request Times | `hMaxRequestTimes` | `600-900` | Jumlah maksimum permintaan per koneksi (rentang) |
| Max Reusable Secs | `hMaxReusableSecs` | `1800-3000` | Waktu koneksi dapat digunakan kembali (detik, rentang) |
| Keep Alive Period | `hKeepAlivePeriod` | `""` (kosong) | Periode keep-alive untuk mempertahankan koneksi |

> **Penting.** Tidak boleh menetapkan **Max Connections** dan **Max Concurrency** secara bersamaan — xray-core akan menolak konfigurasi tersebut. Secara default saat XMUX diaktifkan, panel menetapkan `Max Concurrency = 16-32`; jika Anda menetapkan **Max Connections** (nilai lebih dari `0`), panel akan menghapus nilai default `Max Concurrency` untuk menghindari konflik.

---

### 6.8. Transport Hysteria (`hysteriaSettings`)

Transport **Hysteria** tidak dipilih dari daftar «Transport»: transport ini diaktifkan secara otomatis ketika inbound dibuat dengan protokol Hysteria, dan disembunyikan untuk protokol lain (saat beralih dari protokol Hysteria, jaringan dipaksa kembali ke `tcp`). Parameter:

| Kolom | Kunci | Default | Deskripsi |
| --- | --- | --- | --- |
| Versi | `version` | `2` (tetap, kolom dikunci) | Versi Hysteria. Hanya Hysteria 2 yang didukung |
| UDP idle timeout (s) | `udpIdleTimeout` | `60` | Timeout tidak aktif sesi UDP (detik). Rentang yang diizinkan — 2–600; xray-core menolak nilai di luar rentang ini saat startup |
| Masquerade | `masquerade` | nonaktif (tidak ada) | Mengaktifkan penyamaran listener sebagai server HTTP/3 saat dilakukan probe |

Saat **Masquerade** diaktifkan, pilihan tipe (`type`) dan kolom terkaitnya muncul:

- **`""` — default (404 page)**: mengembalikan halaman 404 standar (tidak memerlukan kolom tambahan).
- **`proxy` (reverse proxy)**: proxy terbalik ke situs eksternal.
  - `url` (**Upstream URL**, placeholder `https://www.example.com`) — alamat tujuan;
  - `rewriteHost` (**Timpa Host**, default `false`) — mengganti header `Host`;
  - `insecure` (**Lewati TLS verify**, default `false`) — tidak memverifikasi sertifikat TLS upstream.
- **`file` (serve directory)**: melayani file dari direktori.
  - `dir` (**Direktori**, placeholder `/var/www/html`).
- **`string` (fixed body)**: respons HTTP tetap.
  - `statusCode` (**Kode status**, default `0`, rentang 0–599);
  - `content` (**Body**) — isi respons;
  - `headers` (**Header**) — peta `nama → nilai`.

Masquerade memungkinkan inbound berbasis Hysteria tampak seperti server HTTP/3 biasa saat dilakukan probe aktif, sehingga meningkatkan penyamaran. Secara default masquerade dinonaktifkan.

**Contoh `hysteriaSettings` dengan reverse proxy (`masquerade` → `proxy`):**

```json
{
  "version": 2,
  "udpIdleTimeout": 60,
  "masquerade": {
    "type": "proxy",
    "url": "https://www.example.com",
    "rewriteHost": true,
    "insecure": false
  }
}
```

Di sini saat dilakukan probe, listener mengembalikan respons dari `https://www.example.com`, menyamar sebagai situs HTTP/3 biasa.

---

### 6.9. Parameter Pelengkap

Selain pemilihan jaringan, pada tab yang sama terdapat dua blok umum yang tidak bergantung pada transport tertentu (detail — di bagian masing-masing):

- **External Proxy** (`externalProxy`) — daftar alamat/port eksternal yang menggantikan alamat panel itu sendiri dalam tautan subscription.
- **Sockopt** (`sockopt`) — opsi socket tingkat rendah (TCP Fast Open, mark, strategi domain, proxy transparan, dll.).

#### Real client IP (menentukan IP asli di balik CDN/relay)

Ketika inbound berada di balik perantara (CDN seperti Cloudflare, terowongan L4/relay, atau panel lain), Xray melihat alamat perantara, bukan pengunjung asli. Alamat ini masuk ke daftar klien online dan dihitung sebagai batas IP per klien, sehingga keduanya menjadi tidak berguna di balik proksi. Untuk memulihkan IP asli, di bagian **Sockopt** pada form inbound terdapat pilihan preset **Real client IP** yang menggabungkan pengaturan `acceptProxyProtocol` dan `trustedXForwardedFor`:

| Preset | Yang dilakukan | Kapan digunakan |
| --- | --- | --- |
| **Off / direct** | Mengosongkan kedua kolom. | Inbound dapat diakses klien secara langsung |
| **Cloudflare CDN** | Menetapkan `sockopt.trustedXForwardedFor = ["CF-Connecting-IP"]`. | WebSocket / HTTPUpgrade / XHTTP / gRPC di balik CDN Cloudflare (ikon awan oranye) |
| **L4 relay / Spectrum (PROXY)** | Mengaktifkan `acceptProxyProtocol = true`. | Terowongan L4/relay di depan inbound atau Cloudflare **Spectrum** |

Preset bersifat saling eksklusif: memilih satu akan mengosongkan kolom yang lain, sehingga `trustedXForwardedFor` yang sudah usang tidak menimpa IP yang dipulihkan melalui PROXY protocol. Di bawah preset, sakelar **Proxy Protocol** dan daftar **Trusted X-Forwarded-For** tetap terlihat — preset hanya mengisinya untuk Anda, dan jika perlu dapat diedit secara manual. Jika preset yang dipilih tidak didukung oleh transport saat ini (misalnya, PROXY protocol pada mKCP), form menampilkan peringatan. Kolom-kolom ini hanya berlaku untuk sisi server dan **tidak pernah dikirim ke klien dalam subscription**.

> **Gunakan salah satu saja.** `acceptProxyProtocol` membaca IP asli dari header PROXY protocol L4, sedangkan `trustedXForwardedFor` dari header HTTP permintaan; menggabungkan keduanya secara manual hanya perlu dilakukan jika rantai perantara Anda memang memerlukannya.
- **FinalMask** (`finalmask`) — mekanisme umum obfuskasi lapisan transport (termasuk obfuskasi legacy mKCP) yang menggantikan kolom terpisah «seed»/«header type» di dalam sub-form jaringan.

---

## 7. Keamanan Koneksi: TLS, XTLS, dan REALITY

Setiap inbound yang mendukung pengiriman melalui transport stream (VMess, VLESS, Trojan, Shadowsocks, Hysteria) memiliki tab **"Keamanan"** di editor. Di sini dikonfigurasi bagaimana channel transport dienkripsi dan disamarkan. Tersedia tiga mode yang dapat dipilih melalui tombol radio:

| Mode | Label di UI | Kapan tersedia |
|------|-------------|----------------|
| `none` | **Tidak Ada** | Selalu (kecuali Hysteria, di mana TLS wajib) |
| `tls` | **TLS** | Untuk VMess/VLESS/Trojan/Shadowsocks pada jaringan `tcp`, `ws`, `http`, `grpc`, `httpupgrade`, `xhttp`; untuk Hysteria — selalu |
| `reality` | **Reality** | Hanya untuk VLESS/Trojan pada jaringan `tcp`, `http`, `grpc`, `xhttp` |

Tombol **Tidak Ada** tidak ditampilkan jika protokolnya adalah Hysteria (TLS wajib untuk protokol ini). Tombol **Reality** muncul hanya pada kombinasi protokol dan jaringan yang diperbolehkan (lihat tabel di atas).

Saat mode diubah, panel sepenuhnya merekonstruksi blok `streamSettings`: `tlsSettings` dan `realitySettings` dari mode sebelumnya dihapus dan diganti dengan nilai default mode yang dipilih. Secara khusus, saat memilih **Reality**, panel secara otomatis langsung: mengisi pasangan acak `target` + `serverNames` (SNI) dari daftar domain populer bawaan, membuat `shortIds` acak, serta membuat permintaan ke server untuk mendapatkan pasangan kunci X25519 terbaru (privateKey/publicKey).

### 7.1. Perbedaan: TLS vs XTLS vs REALITY

- **TLS** — enkripsi transport klasik menggunakan protokol TLS 1.2/1.3. Server harus memiliki sertifikat yang valid (domain sendiri + rantai sertifikat). Traffic terlihat seperti HTTPS biasa, namun bagi sensor aktif, TLS-handshake yang mengarah ke domain Anda mudah dikenali; jika diblokir berdasarkan SNI atau sertifikat tidak dipercaya, koneksi akan diblokir/menghasilkan error.

- **XTLS (Vision)** — bukan mode terpisah dalam daftar "Keamanan", melainkan mekanisme *flow* di atas TLS **atau** Reality. Diaktifkan di sisi klien inbound melalui field **Flow** = `xtls-rprx-vision` (atau `xtls-rprx-vision-udp443`). Vision tersedia untuk VLESS pada jaringan `tcp` dengan `security = tls` atau `security = reality`, serta untuk VLESS di atas transport `xhttp` dengan enkripsi VLESS diaktifkan (vlessenc / ML-KEM) — dalam kasus ini field **Flow** juga dapat disetel ke `xtls-rprx-vision`, dan nilainya dengan benar masuk ke link `vless://` (`flow=xtls-rprx-vision`). Vision mengurangi "enkripsi ganda" (TLS-in-TLS) dengan mengalirkan payload langsung setelah handshake, yang mempercepat transfer dan meningkatkan penyamaran. Oleh karena itu, kombinasi **VLESS + Reality + Flow `xtls-rprx-vision`** dianggap sebagai konfigurasi modern yang direkomendasikan.

- **REALITY** — mekanisme penyamaran tanpa sertifikat sendiri. Server "meminjam" TLS-handshake dari situs pihak ketiga nyata (`target`/`serverNames`), sehingga bagi pengamat koneksi tidak dapat dibedakan dari akses ke situs tersebut, dan sertifikat sama sekali tidak diperlukan. Autentikasi dibangun di atas pasangan kunci X25519 dan sekumpulan `shortIds`. REALITY tahan terhadap active probing dan pemblokiran berdasarkan SNI, karena SNI menunjuk ke domain eksternal yang nyata. Kekurangannya — persyaratan konfigurasi yang lebih ketat (penentuan `target` dengan port yang benar, sinkronisasi kunci dengan klien).

Aturan pemilihan singkat:
- memiliki domain sendiri dan sertifikat valid, cukup tampilan HTTPS biasa → **TLS** (jika memungkinkan, dengan Vision);
- tidak ada domain/sertifikat, atau diperlukan penyembunyian maksimal dari DPI → **REALITY** (dengan Vision untuk VLESS/TCP).

### 7.2. Mode "Tidak Ada" (`none`)

Transport dikirimkan tanpa pembungkus TLS: blok `tlsSettings` dan `realitySettings` dari `streamSettings` dihilangkan. Mode ini tidak memiliki field tambahan. Cocok digunakan ketika:
- inbound hanya mendengarkan di `127.0.0.1` dan berfungsi sebagai target fallback (berdasarkan aturan panel, inbound anak untuk fallback harus mendengarkan di `127.0.0.1` dengan `security=none`);
- enkripsi/penyamaran disediakan oleh lapisan eksternal (misalnya, reverse proxy Nginx di depan panel);
- digunakan protokol dengan enkripsi bawaan (Shadowsocks) di jaringan internal.

Untuk inbound yang dapat diakses dari luar, mode "Tidak Ada" tidak disarankan.

**Contoh: blok `streamSettings` untuk TLS pada jaringan `tcp`** (VLESS/Trojan/VMess). Beginilah tampilan hasilnya setelah memilih mode **TLS** dan mengisi SNI serta path ke sertifikat:

```json
"streamSettings": {
  "network": "tcp",
  "security": "tls",
  "tlsSettings": {
    "serverName": "vpn.example.com",
    "minVersion": "1.2",
    "maxVersion": "1.3",
    "alpn": ["h2", "http/1.1"],
    "settings": { "fingerprint": "chrome" },
    "certificates": [
      {
        "certificateFile": "/root/cert/vpn.example.com.crt",
        "keyFile": "/root/cert/vpn.example.com.key",
        "ocspStapling": 3600,
        "usage": "encipherment"
      }
    ]
  }
}
```

### 7.3. Mode TLS

Field pada blok `tlsSettings`. Nilai default diambil dari skema panel.

#### Parameter Utama

| Field (label) | Nilai default | Deskripsi |
|----------------|--------------|-----------|
| **SNI** (`serverName`) | `""` (kosong) | Server Name Indication — nama domain yang ditampilkan dalam TLS-handshake. Harus sesuai dengan domain sertifikat. Placeholder bahasa Inggris: «Server Name Indication». |
| **Cipher Suites** (`cipherSuites`) | `""` → **Otomatis** | Daftar cipher suite yang diizinkan. Defaultnya kosong — pemilihan diserahkan kepada Xray/Go (opsi **Otomatis**). Ubah hanya jika perlu membatasi cipher secara eksplisit. |
| **Versi Min/Maks** (`minMaxVersion`) | min = `1.2`, max = `1.3` | Versi TLS minimum dan maksimum. Nilai yang tersedia: `1.0`, `1.1`, `1.2`, `1.3`. Disarankan untuk mempertahankan `1.2`–`1.3`; menurunkan minimum ke 1.0/1.1 tidak disarankan (versi lama, tidak aman). |
| **uTLS** (`settings.fingerprint`) | `chrome` (di form — opsi **None** = `""` tersedia) | Fingerprint TLS klien yang ditiru (uTLS fingerprint), agar handshake terlihat seperti dari browser populer. Lihat daftar di bawah. Dalam TLS, item pertama di daftar adalah **None** (`""`), yang menonaktifkan peniruan. |
| **ALPN** (`alpn`) | `["h2", "http/1.1"]` | Daftar protokol lapisan aplikasi yang dinegosiasikan dalam TLS (pilihan ganda). Nilai yang diizinkan: `h3`, `h2`, `http/1.1`. Secara default ditawarkan `h2` dan `http/1.1`. |

Nilai yang mungkin untuk **uTLS fingerprint** (sama untuk TLS dan REALITY): `chrome`, `firefox`, `safari`, `ios`, `android`, `edge`, `360`, `qq`, `random`, `randomized`, `randomizednoalpn`, `unsafe`. Di form TLS juga tersedia opsi kosong **None** (peniruan fingerprint tidak diterapkan).

Nilai yang tersedia untuk **Cipher Suites** (TLS 1.3 dan suite ECDHE): `TLS_AES_128_GCM_SHA256`, `TLS_AES_256_GCM_SHA384`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`.

#### Pengalih TLS

| Pengalih | Default | Deskripsi |
|----------|---------|-----------|
| **Tolak SNI Tidak Dikenal** (`rejectUnknownSni`) | nonaktif (`false`) | Jika diaktifkan, server memutus koneksi ketika SNI yang ditampilkan klien tidak sesuai dengan nama dalam sertifikat. Meningkatkan ketersembunyian (server tidak merespons permintaan "asing"), tetapi memerlukan kecocokan SNI yang tepat di sisi klien. |
| **Nonaktifkan System Root** (`disableSystemRoot`) | nonaktif (`false`) | Menonaktifkan penggunaan penyimpanan sertifikat root tepercaya sistem. |
| **Lanjutkan Sesi** (`enableSessionResumption`) | nonaktif (`false`) | Mengaktifkan lanjutan sesi TLS (session resumption / session tickets). |

#### Parameter TLS Tambahan (vcn, kurva, log kunci, ECH Sockopt)

Di bawah pengaturan TLS utama terdapat field tambahan.

| Field (label) | Default | Deskripsi |
|----------------|---------|-----------|
| **Verify Peer Cert By Name** (`settings.verifyPeerCertByName`) | `""` | Nama-nama (dipisahkan koma) yang digunakan klien untuk memverifikasi sertifikat server sebagai pengganti SNI. Ini adalah pengganti modern dari field `allowInsecure` yang dihapus dari Xray setelah 2026-06-01. Nilai ini hanya untuk panel: tidak ditulis ke konfigurasi xray server, tetapi diteruskan ke link undangan dan langganan (`vcn=…`) agar klien dapat menerapkannya sendiri. Placeholder: `example.com`. |
| **Curve Preferences** (`curvePreferences`) | `""` | Pembatasan dan urutan kurva pertukaran kunci TLS sesuai preferensi (misalnya `X25519MLKEM768`, `X25519`). Kosong — menggunakan nilai default Xray-core. |
| **Master Key Log** (`masterKeyLog`) | `""` | Path untuk mencatat TLS master key dalam format `SSLKEYLOGFILE` (untuk mendekripsi traffic di Wireshark saat debugging). Placeholder: `/path/to/sslkeylog.txt`. Biarkan kosong di produksi — file ini memungkinkan dekripsi seluruh traffic. |
| **ECH Sockopt** (`echSockopt`) | nonaktif | Pengalih dengan parameter socket untuk koneksi yang digunakan Xray untuk meminta daftar ECH config. Saat diaktifkan, tersedia: **Dialer Proxy** (`dialerProxy` — arahkan permintaan melalui outbound tertentu berdasarkan tag), **Domain Strategy** (`domainStrategy`), **TCP Fast Open** (`tcpFastOpen`), **Multipath TCP** (`tcpMptcp`). Biarkan nonaktif jika tidak diperlukan. |

Field `verifyPeerCertByName`, `curvePreferences`, `masterKeyLog`, dan `echSockopt` berada di level atas `tlsSettings` dan bertahan setelah "pemangkasan" field panel saat konfigurasi disimpan.

#### Sertifikat

Bagian **Sertifikat SSL** (judul di UI: «Sertifikat SSL») dikonfigurasi sebagai daftar: tombol **+** menambahkan entri sertifikat baru, tombol **− Hapus** menghapusnya (tombol hapus tersedia hanya jika ada lebih dari satu entri). Secara default saat TLS diaktifkan, dibuat satu entri kosong.

Untuk setiap entri, pengalih mode input (`useFile`):

- **Path ke Sertifikat** (nilai `useFile = true`, default) — menentukan path ke file di server:
  - **Kunci Publik** (`certificateFile`) — path ke file sertifikat (`.crt`/`.pem`);
  - **Kunci Privat** (`keyFile`) — path ke file kunci privat (`.key`).
- **Konten Sertifikat** (nilai `useFile = false`) — konten disisipkan langsung ke field (area teks multibaris):
  - **Kunci Publik** (`certificate`) — konten PEM sertifikat;
  - **Kunci Privat** (`key`) — konten PEM kunci.

Di bawah field mode "Path ke Sertifikat" terdapat dua tombol:
- **Isi sertifikat panel** — mengisi field dengan path ke sertifikat SSL panel itu sendiri. Untuk inbound di panel utama, digunakan sertifikat panel tersebut (`POST /panel/setting/all` → `webCertFile`/`webKeyFile`); untuk inbound yang ditugaskan ke node, digunakan sertifikat node itu sendiri (`GET /panel/api/nodes/webCert/{nodeId}`), karena path panel utama tidak ada di node. Jika sertifikat belum dikonfigurasi, muncul peringatan: «*Sertifikat belum dikonfigurasi untuk panel. Harap konfigurasikan terlebih dahulu di Pengaturan.*» (sertifikat panel itu sendiri dikonfigurasi di bagian «Pengaturan → Keamanan»).
- **Hapus** — mengosongkan kedua path.

Field tambahan untuk setiap entri sertifikat:

| Field | Default | Deskripsi |
|-------|---------|-----------|
| **OCSP Stapling** (`ocspStapling`) | `0` (nonaktif) | Interval pembaruan OCSP stapling dalam detik (minimum `0`). Untuk inbound baru, defaultnya nonaktif (`0`): ini menghilangkan error di log xray untuk sertifikat tanpa OCSP responder (misalnya, Let's Encrypt yang telah menghentikan OCSP). Aktifkan hanya untuk sertifikat yang mendukung stapling. |
| **Muat Sekali** (`oneTimeLoading`) | nonaktif (`false`) | Jika diaktifkan, sertifikat dibaca dari disk sekali saat startup dan tidak dibaca ulang saat file berubah. |
| **Opsi Penggunaan** (`usage`) | `encipherment` | Tujuan sertifikat. Nilai yang diizinkan: `encipherment` (enkripsi — sertifikat server biasa), `verify` (verifikasi), `issue` (penerbitan — server menandatangani/menerbitkan sertifikat sendiri). |
| **Build Chain** (`buildChain`) | nonaktif (`false`) | Ditampilkan **hanya** saat `usage = issue`. Membangun rantai sertifikat. |

> Tidak ada tombol terpisah untuk sertifikat self-signed di editor inbound: panel tidak membuat sertifikat self-signed secara otomatis untuk inbound. Sertifikat harus ditentukan melalui path/konten, atau diambil dari pengaturan panel menggunakan tombol "Isi sertifikat panel". Penerbitan/perolehan sertifikat SSL panel itu sendiri (termasuk upload file dan pengikatan domain) dilakukan di bagian **Pengaturan → Keamanan**; tidak ada endpoint ACME/Let's Encrypt untuk inbound di sini.

#### ECH dan Pemancangan Sertifikat (field TLS lanjutan)

| Field | Default | Deskripsi |
|-------|---------|-----------|
| **ECH key** (`echServerKeys`) | `""` | Kunci server Encrypted Client Hello. |
| **ECH config** (`settings.echConfigList`) | `""` | Daftar ECH config (bagian klien, masuk ke link). |
| **SHA-256 sertifikat peer** (`settings.pinnedPeerCertSha256`) | `[]` | Hash SHA-256 dari sertifikat peer (string hex, dipisahkan koma). Deskripsi verbatim: «*Hash SHA-256 dari sertifikat peer sebagai string heksadesimal (misalnya e8e2d3…), dipisahkan koma. Hanya untuk panel — tidak ditulis ke konfigurasi xray server, tetapi disertakan dalam link undangan agar klien dapat memancangkan sertifikat.*» |

Tombol:
Di samping field **SHA-256 sertifikat peer** terdapat dua tombol pengisian otomatis:
- **Fill from this inbound's certificate** (ikon perisai) — mengisi hash SHA-256 dari sertifikat inbound ini sendiri (diambil secara lokal melalui endpoint `getCertHash`).
- **Fetch the hash by pinging the SNI (xray tls ping)** (ikon unduhan) — mendapatkan hash sertifikat server langsung dengan melakukan koneksi TLS ke SNI yang ditentukan (di server dipanggil `getRemoteCertHash`). Field **SNI** (`serverName`) harus diisi — jika tidak, muncul petunjuk «*Set the SNI (serverName) first to ping the remote certificate.*»

Hash yang diperoleh ditambahkan ke field (dipisahkan koma) dan masuk ke link undangan agar klien dapat memancangkan sertifikat.
- **Dapatkan sertifikat ECH baru** — meminta pasangan ECH baru dari server untuk SNI saat ini (`POST /panel/api/server/getNewEchCert`, di server dijalankan `xray tls ech --serverName <SNI>`); mengisi field **ECH key** dan **ECH config**.
- **Hapus** — mengosongkan kedua field ECH.

### 7.4. Mode REALITY

Field pada blok `realitySettings`. REALITY tidak menggunakan sertifikat SSL: sebagai gantinya digunakan TLS-handshake yang dipinjam dari domain eksternal dan pasangan kunci X25519.

#### Parameter Penyamaran

| Field (label) | Nilai default | Deskripsi |
|----------------|--------------|-----------|
| **Tampilkan** (`show`) | nonaktif (`false`) | Output debug REALITY ke log Xray. Biasanya dibiarkan nonaktif. |
| **Xver** (`xver`) | `0` | Versi protokol PROXY yang diteruskan ke backend (`0` — nonaktif). Minimum `0`. |
| **uTLS** (`settings.fingerprint`) | `chrome` | Fingerprint TLS yang ditiru (daftar yang sama seperti di TLS, tetapi tanpa opsi kosong None). |
| **Target** (`target`) | `""` (panel mengisi nilai acak saat diaktifkan) | **Field wajib.** Domain nyata yang TLS-handshake-nya dipinjam oleh REALITY. Deskripsi verbatim: «*Wajib. Harus menyertakan port (misalnya, example.com:443). Tanpa port, Xray-core tidak akan berjalan.*» Validasi panel memeriksa keberadaan dan kebenaran port; jika tidak, muncul error «Target REALITY wajib» / «Target REALITY harus menyertakan port…» / «Port pada target REALITY tidak valid». Tombol refresh di sampingnya mengisi pasangan acak dari daftar bawaan. |
| **SNI** (`serverNames`) | `[]` (diisi bersamaan dengan target) | Daftar SNI yang diizinkan (input ganda dengan tag). Harus sesuai dengan domain dari **Target**. Tombol refresh mengisi SNI bersamaan dengan target acak. |
| **Perbedaan Waktu Maks (ms)** (`maxTimediff`) | `0` | Perbedaan jam maksimum yang diizinkan antara klien dan server dalam milidetik (`0` — tanpa batas). Minimum `0`. |
| **Versi Klien Min** (`minClientVer`) | `""` | Versi klien Xray minimum (placeholder `25.9.11`). Kosong — tanpa batasan. |
| **Versi Klien Maks** (`maxClientVer`) | `""` | Versi klien Xray maksimum. Kosong — tanpa batasan. |
| **Short IDs** (`shortIds`) | `[]` (dibuat saat diaktifkan) | Daftar pengenal pendek (hex) untuk membedakan klien. Input ganda dengan tag; tombol refresh membuat set acak. |
| **SpiderX** (`settings.spiderX`) | `/` | Path "spider" (bagian klien dari REALITY), digunakan saat meniru akses ke situs eksternal. Masuk ke link undangan. |

**Target** (`target`) dan **SNI** (`serverNames`) saat REALITY diaktifkan dan melalui tombol refresh diisi dengan pasangan acak dari daftar bawaan panel: `www.amazon.com`, `aws.amazon.com`, `www.oracle.com`, `www.nvidia.com`, `www.amd.com`, `www.intel.com`, `www.sony.com` (masing-masing dengan port `:443`). Pilih situs HTTPS pihak ketiga yang besar dan stabil, yang tidak berada di server Anda sendiri.

**Contoh: blok `streamSettings` untuk REALITY pada jaringan `tcp`** (VLESS). Sertifikat tidak diperlukan — sebagai gantinya digunakan domain yang dipinjam dan pasangan kunci X25519:

```json
"streamSettings": {
  "network": "tcp",
  "security": "reality",
  "realitySettings": {
    "show": false,
    "xver": 0,
    "dest": "www.nvidia.com:443",
    "serverNames": ["www.nvidia.com"],
    "privateKey": "YOUR_X25519_PRIVATE_KEY",
    "shortIds": ["", "6ba85179e30d4fc2"],
    "settings": {
      "publicKey": "YOUR_X25519_PUBLIC_KEY",
      "fingerprint": "chrome",
      "spiderX": "/"
    }
  }
}
```

Di sini field **Target** (`target`) di panel sesuai dengan `dest` di konfigurasi Xray yang dihasilkan. Jika inbound REALITY dibuat dengan destination di kunci `dest` (oleh versi panel lama, melalui API, atau alat eksternal), panel saat parsing menormalisasi `dest` → `target` ketika `target` kosong — sehingga inbound tersebut dimuat dengan benar, field **Target** tidak kosong, dan penyimpanan ulang tidak merusak REALITY yang berjalan.

#### Kunci REALITY (X25519)

| Field | Default | Deskripsi |
|-------|---------|-----------|
| **Kunci Publik** (`settings.publicKey`) | `""` | Kunci publik X25519 (yang dimasukkan klien ke konfigurasi/link-nya). |
| **Kunci Privat** (`privateKey`) | `""` | Kunci privat X25519 (hanya disimpan di server). |

Tombol di bawah kunci:
- **Dapatkan sertifikat baru** — meminta pasangan kunci baru dari server (`GET /panel/api/server/getNewX25519Cert`; di server dijalankan `xray x25519`), mengisi **Kunci Privat** dan **Kunci Publik**. Pasangan yang sama secara otomatis dibuat saat mode REALITY pertama kali diaktifkan.

**Contoh: mendapatkan pasangan kunci X25519 melalui API** (di luar form, misalnya untuk skrip). Permintaan mengembalikan kunci privat dan publik:

```bash
curl -s -b cookie.txt https://your-panel:2053/panel/api/server/getNewX25519Cert
# Respons:
# {"success":true,"obj":{"privateKey":"...","publicKey":"..."}}
```

`cookie.txt` — file cookie sesi yang diperoleh setelah login melalui `POST /login`.
- **Hapus** — mengosongkan kedua kunci.

#### Tanda Tangan Pasca-Kuantum ML-DSA-65 (mldsa65)

Lapisan autentikasi pasca-kuantum REALITY yang opsional:

| Field | Default | Deskripsi |
|-------|---------|-----------|
| **mldsa65 Seed** (`mldsa65Seed`) | `""` | Seed kunci ML-DSA-65 sisi server. |
| **mldsa65 Verify** (`settings.mldsa65Verify`) | `""` | Nilai verifikasi (bagian klien, masuk ke link). |

Tombol:
- **Dapatkan Seed baru** — meminta pasangan baru (`GET /panel/api/server/getNewmldsa65`; di server dijalankan `xray mldsa65`), mengisi **mldsa65 Seed** dan **mldsa65 Verify**.
- **Hapus** — mengosongkan kedua field.

#### Pembatasan Kecepatan Fallback dan Log Kunci REALITY

Dalam pengaturan REALITY tersedia pembatasan kecepatan traffic fallback — ini mencegah probe aktif menggunakan server sebagai channel gratis ke domain yang dipinjam. Pengaturan dikonfigurasi secara terpisah untuk dua arah — **Limit Fallback Upload** dan **Limit Fallback Download** (`limitFallbackUpload` / `limitFallbackDownload`), masing-masing dengan set field yang sama:

| Field (label) | Default | Deskripsi |
|----------------|---------|-----------|
| **After Bytes** (`afterBytes`) | `0` | Berapa byte yang diteruskan dengan kecepatan penuh sebelum pembatasan dimulai. `0` — batasi mulai dari byte pertama. |
| **Bytes Per Sec** (`bytesPerSec`) | `0` | Batas kecepatan traffic fallback dalam byte per detik setelah ambang batas. `0` — tanpa batasan (menonaktifkan arah ini). |
| **Burst Bytes Per Sec** (`burstBytesPerSec`) | `0` | Cadangan untuk lonjakan singkat di atas kecepatan konstan (ukuran token-bucket). Jika lebih kecil dari **Bytes Per Sec**, dinaikkan ke nilainya. |

Di sini juga ditambahkan field **Master Key Log** (`masterKeyLog`) — path untuk mencatat TLS master key dalam format `SSLKEYLOGFILE` untuk debugging di Wireshark; biarkan kosong di produksi.

### 7.5. Rekomendasi Konfigurasi Praktis

1. **VLESS + Reality (direkomendasikan):** buat inbound VLESS pada jaringan `tcp`, di tab "Keamanan" pilih **Reality** — panel akan secara otomatis mengisi `target`/SNI acak, `shortIds`, dan membuat kunci X25519. Jika perlu, klik "Dapatkan sertifikat baru" untuk pasangan kunci Anda sendiri. Untuk klien VLESS, aktifkan **Flow** = `xtls-rprx-vision` (XTLS Vision) — ini memberikan performa dan ketersembunyian maksimal.

**Contoh: link klien akhir VLESS + Reality + Vision.** Beginilah tampilan link undangan yang diberikan panel untuk inbound semacam ini (nilai kunci/ID bersifat ilustratif):

```text
vless://uuid-клиента@1.2.3.4:443?type=tcp&security=reality&pbk=ПУБЛИЧНЫЙ_КЛЮЧ&fp=chrome&sni=www.nvidia.com&sid=6ba85179e30d4fc2&spx=%2F&flow=xtls-rprx-vision#my-reality
```

Di sini `pbk` — kunci publik X25519, `sni` — domain yang dipinjam dari **Target**, `sid` — salah satu dari **Short IDs**, `flow=xtls-rprx-vision` — XTLS Vision yang diaktifkan.
2. **TLS dengan domain sendiri:** pilih **TLS**, isi **SNI** dengan nama domain, tambahkan sertifikat (melalui path ke file atau konten), atau klik "Isi sertifikat panel" jika domain dan sertifikat sudah dikonfigurasi di «Pengaturan → Keamanan». Pertahankan **Versi Min/Maks** = `1.2`–`1.3` dan **uTLS** = `chrome` untuk menyamar sebagai browser biasa.
3. Jangan biarkan mode **Tidak Ada** untuk inbound yang terbuka ke luar — gunakan hanya untuk target fallback lokal (`127.0.0.1`) atau ketika TLS disediakan oleh proxy eksternal.
4. Saran dari antarmuka: untuk sebagian besar field lanjutan berlaku petunjuk «*Disarankan untuk mempertahankan pengaturan default*» — ubah hanya jika Anda memahami konsekuensinya.

---

## 8. Klien

Klien adalah akun pengguna VPN: sekumpulan kredensial (UUID atau kata sandi) yang terikat ke satu atau beberapa inbound, dengan kuota traffic, masa berlaku, dan batas koneksi simultan tersendiri. Dalam fork ini, klien merupakan entitas mandiri (tabel `clients`): klien yang sama dapat dikaitkan ke beberapa inbound sekaligus, dengan UUID/kata sandi yang sama dan penghitung traffic bersama. Bagian **Klien** menampilkan semua akun panel terlepas dari inbound, lengkap dengan pencarian, filter, pengurutan, dan operasi massal.

### 8.1. Field klien

Berikut penjelasan setiap field pada editor **Tambah klien** / **Ubah klien**.

Formulir klien dibagi menjadi dua tab: **Utama** (email, penautan ke inbound, batas, masa berlaku, grup, komentar, reverse tag) dan **Kredensial** (UUID/kata sandi/auth, Flow, VMess Security). Pada label field, kuota tertulis sebagai **Batas Traffic (GB)**, dan durasi sebagai **Durasi (hari)** dan **Perpanjang otomatis (hari)**; field **Batas Traffic (GB)** dan **Batas IP** memiliki petunjuk yang menjelaskan bahwa `0` berarti "tanpa batasan". Saat mengedit klien yang sudah ada, tombol buat email acak disembunyikan, dan tombol log IP dipindahkan langsung ke samping field **Batas IP** dengan menampilkan jumlah alamat yang tercatat.

| Field | Kunci JSON | Default | Deskripsi |
|-------|-----------|---------|-----------|
| Email | `email` | — (wajib) | Pengenal unik klien |
| UUID | `id` | dibuat otomatis | Pengenal untuk VMess/VLESS |
| Kata sandi | `password` | dibuat otomatis | Kata sandi untuk Trojan/Shadowsocks |
| Otorisasi | `auth` | dibuat otomatis | Kata sandi untuk Hysteria |
| Flow | `flow` | kosong | Flow control (XTLS), hanya VLESS |
| VMess Security | `security` | `auto` | Metode enkripsi VMess |
| Batas IP | `limitIp` | `0` (tanpa batas) | Maksimum IP simultan |
| Total terkirim/diterima (GB) | `totalGB` | `0` (tanpa batas) | Kuota traffic |
| Masa berlaku | `expiryTime` | `0` (tanpa batas waktu) | Tanggal kedaluwarsa |
| Perpanjang otomatis | `reset` | `0` (nonaktif) | Periode reset traffic, dalam hari |
| ID pengguna Telegram | `tgId` | `0` (tidak ada) | ID numerik Telegram |
| ID langganan | `subId` | dibuat otomatis | Pengenal langganan |
| Grup | `group` | kosong | Label pengelompokan logis |
| Komentar | `comment` | kosong | Catatan bebas |
| Diaktifkan | `enable` | `true` | Apakah akun aktif |

#### Email (pengenal)

Field **Email** adalah pengenal utama dan wajib bagi klien. Meskipun namanya "Email", ini tidak harus berupa alamat email: label teks apa pun bisa digunakan (nama pengguna, nomor). Nilainya harus **unik** dalam lingkup panel; percobaan membuat klien kedua dengan email yang sudah digunakan akan ditolak (`email already in use`), kecuali jika `subId`-nya juga sama (ini dianggap sebagai penautan klien yang sama).

Email **tidak boleh dikosongkan** (`client email is required`) dan **tidak boleh mengandung spasi, karakter `/`, `\`, maupun karakter kontrol** ("Email tidak boleh mengandung spasi, '/', '\', atau karakter kontrol"). Email digunakan dalam penghitungan traffic, log IP, daftar online, dan nama operasi — mengubahnya di kemudian hari tidak disarankan.

#### UUID / Kata sandi / Otorisasi (kredensial)

Field kredensial yang digunakan bergantung pada protokol inbound yang dikaitkan dengan klien. Nilai diisi otomatis jika field dibiarkan kosong:

- **UUID** (field `id`) — untuk protokol **VMess** dan **VLESS**. Jika tidak diisi, UUID v4 acak akan dibuat.
- **Kata sandi** (field `password`) — untuk **Trojan** dan **Shadowsocks**. Untuk Trojan, secara default dibuat UUID tanpa tanda hubung. Untuk Shadowsocks, dibuat kunci dengan panjang yang sesuai dalam Base64 berdasarkan metode enkripsi inbound: 16 byte untuk `2022-blake3-aes-128-gcm`, 32 byte untuk `2022-blake3-aes-256-gcm` dan `2022-blake3-chacha20-poly1305`; untuk metode lainnya — UUID tanpa tanda hubung. Jika kunci yang dimasukkan secara manual tidak sesuai dengan metode 2022-blake3, kunci tersebut akan diganti dengan yang dibuat otomatis.
- **Otorisasi** (field `auth`) — kata sandi untuk **Hysteria**. Default-nya adalah UUID tanpa tanda hubung.

Karena satu klien dapat dikaitkan ke inbound dengan protokol berbeda, record klien dapat sekaligus memiliki UUID, kata sandi, dan auth — masing-masing protokol menggunakan field-nya sendiri.

**Contoh: tampilan kredensial klien dalam `settings` berbagai inbound.** Klien yang sama diidentifikasi melalui `id` di inbound VLESS, melalui `password` di Trojan, dan melalui `password` (kunci Base64) di Shadowsocks:

```json
// fragmen settings.clients pada inbound VLESS
{ "id": "b831381d-6324-4d53-ad4f-8cda48b30811", "email": "user-a", "flow": "xtls-rprx-vision" }

// klien yang sama pada inbound Trojan
{ "password": "b831381d63244d53ad4f8cda48b30811", "email": "user-a" }

// klien yang sama pada inbound Shadowsocks (metode 2022-blake3-aes-256-gcm)
{ "password": "GPyOaA3f7CO0az53eaQ8eqMfRDjmBlOh7v1u3+Z+pHk=", "email": "user-a" }
```

#### Flow

**Flow** (field `flow`) — pengaturan flow control XTLS. Hanya berlaku untuk **VLESS** dan hanya ketika inbound dikonfigurasi untuk XTLS Vision: VLESS melalui transport **TCP** dengan security **`tls`** atau **`reality`**. Nilai yang diizinkan adalah `xtls-rprx-vision` (dan juga `xtls-rprx-vision-udp443` secara historis); nilai kosong berarti tidak ada flow.

Jika inbound tidak mendukung XTLS-flow, flow yang ditentukan akan **dihapus secara diam-diam** saat menyimpan klien: untuk klien yang sama yang dikaitkan ke beberapa inbound, flow hanya diterapkan di tempat yang diizinkan. Ubah hanya jika Anda secara khusus menggunakan VLESS-Vision.

#### VMess Security

**VMess Security** (field `security`) — metode enkripsi payload untuk VMess. Nilai default adalah `auto` (Xray memilih cipher secara otomatis). Nilai yang diizinkan adalah nilai standar VMess: `auto`, `aes-128-gcm`, `chacha20-poly1305`, `none`, `zero`. Field ini tidak digunakan untuk protokol lain.

#### Batas IP (koneksi simultan)

**Batas IP** (field `limitIp`) — jumlah maksimum **alamat IP berbeda** yang dapat terhubung menggunakan klien secara bersamaan. Nilai default adalah `0`, yang berarti **tanpa batasan**. Jika nilainya positif, panel melacak IP aktif klien dan, jika batas terlampaui, menonaktifkan akun melalui tugas latar belakang. (Mulai **3.3.1**, penghitungan IP dilakukan melalui API online-stats inti Xray dan **tidak memerlukan** log akses; pada versi inti yang lebih lama, panel beralih ke membaca log akses, yang harus diaktifkan saat itu.) Gunakan fitur ini untuk mencegah pembagian satu langganan ke banyak perangkat: misalnya, `2` — izinkan dua perangkat.

Batas IP diterapkan menggunakan **Fail2ban**, sehingga field **Batas IP** hanya aktif jika Fail2ban terpasang dan berfungsi (panel memeriksa statusnya melalui `GET /panel/api/server/fail2banStatus`). Jika Fail2ban tidak terpasang, field editor klien (dan formulir penambahan massal) diblokir, dan saat diarahkan ke sana akan muncul petunjuk yang menyarankan instalasi Fail2ban dari menu bash `x-ui` ("Fail2ban is not installed, so the IP limit cannot be enforced. Install Fail2ban from the x-ui bash menu to enable this option."); di Windows, petunjuk menyatakan bahwa Fail2ban tidak tersedia di sana ("Fail2ban is not available on Windows, so the IP limit cannot be enforced."), dan jika fitur dinonaktifkan di server — "The IP limit feature is disabled on this server.". Saat memperbarui panel, batas IP klien di server tanpa Fail2ban direset ke nol oleh migrasi sekali jalan, karena bagaimanapun tidak pernah diterapkan di sana.

**Contoh nilai.** `limitIp: 0` — tanpa batasan; `limitIp: 1` — tepat satu perangkat secara bersamaan; `limitIp: 3` — hingga tiga IP berbeda. Pada IP aktif keempat, tugas latar belakang akan menonaktifkan klien (`enable = false`) sampai Anda menjalankan **Reset Batas IP**.

Operasi terkait: **Log IP** menampilkan daftar IP klien yang tercatat; setiap entri berisi, selain IP itu sendiri, waktu akses terakhir dan label node (`@ nama_node`), yang melaluinya koneksi tercatat — dalam konfigurasi multi-panel, Anda dapat melihat node mana yang digunakan klien untuk terhubung. **Reset Batas IP** menghapus log IP yang terkumpul agar klien dapat terhubung kembali tanpa menunggu entri kedaluwarsa secara alami.

#### Total terkirim/diterima (GB) — kuota traffic

**Total terkirim/diterima (GB)** (field `totalGB`) — kuota traffic total (kirim + terima). Nilai default `0` berarti **tanpa batas**. Ketika kuota tercapai (`up + down >= total`), klien dianggap **habis** (depleted) dan dinonaktifkan. Di UI biasanya dimasukkan dalam gigabyte; di database disimpan dalam byte.

Pada daftar klien, kolom **Traffic** menampilkan bilah penggunaan berwarna: volume traffic yang terpakai, label batas (atau tanda ∞ jika tanpa batas), dan petunjuk saat diarahkan dengan perincian kirim/terima dan sisa. Indikator ringkas yang sama ditampilkan di kartu klien pada tampilan ponsel.

#### Masa berlaku (Expiry)

**Masa berlaku** (field `expiryTime`) menentukan saat kedaluwarsa akun. Field ini memiliki tiga mode:

- **Tanpa batas waktu** — `0`. Klien tidak pernah kedaluwarsa berdasarkan waktu.
- **Tanggal tertentu** — Unix-timestamp positif (dalam milidetik). Saat tercapai (`expiryTime <= sekarang`), klien dianggap kedaluwarsa (expired) dan dinonaktifkan. Di UI biasanya ditentukan dengan memilih tanggal atau memasukkan durasi dalam hari (**Durasi**, satuan **Hari**).
- **Mulai setelah penggunaan pertama** — nilai **negatif** yang mengodekan durasi. Selama klien belum mengirimkan satu byte pun, masa berlaku tetap negatif ("start tertunda"). Pada penghitungan traffic pertama, panel mengonversinya ke tanggal absolut: `sekarang + |durasi|`. Ini memungkinkan penjualan, misalnya, "30 hari sejak koneksi pertama" tanpa mengetahui terlebih dahulu kapan klien akan aktif. Konversi dilakukan satu kali per email agar semua inbound yang dikaitkan mendapat masa berlaku yang sama.

**Contoh pengkodean masa berlaku.** Tanggal tetap 1 Maret 2026, 00:00 UTC → `expiryTime: 1772323200000` (timestamp positif dalam milidetik). "30 hari sejak koneksi pertama" → `expiryTime: -2592000000` (nilai negatif, `30 × 24 × 60 × 60 × 1000`); pada byte traffic pertama, panel akan menggantinya dengan `sekarang + 2592000000`. Tanpa batas waktu → `expiryTime: 0`.

#### Perpanjang otomatis (periode reset traffic klien)

Field **Perpanjang otomatis** (field `reset`) adalah periode perpanjangan/reset otomatis dalam hari. Petunjuk: "Perpanjangan otomatis setelah berakhir. (0 = nonaktif) (satuan: hari)".

- `0` — perpanjangan otomatis **dinonaktifkan** (nilai default). Setelah masa berlaku habis, klien menjadi habis begitu saja.
- `> 0` — tugas latar belakang saat masa berlaku habis akan **mereset penghitung traffic ke nol** (`up = down = 0`), **menggeser masa berlaku ke depan** sebesar `reset` hari (jika perlu beberapa periode, hingga masa berlaku baru jatuh di masa depan), dan jika diperlukan **mengaktifkan kembali** klien. Ini mengimplementasikan langganan berkala (misalnya bulanan). Perpanjangan otomatis **tidak berlaku untuk inbound di node** (`node_id IS NOT NULL`).

Konsekuensi penting: klien dengan `reset > 0` **dikecualikan** dari kategori "habis" dalam operasi penghapusan massal — traffic/masa berlaku mereka yang habis memang diharapkan direset oleh perpanjangan otomatis, bukan menjadikan akun sebagai kandidat penghapusan.

#### ID pengguna Telegram

**ID pengguna Telegram** (field `tgId`) — pengenal numerik Telegram pengguna untuk penautan ke bot Telegram bawaan panel (notifikasi, melihat statistik secara mandiri). Petunjuk: "ID numerik pengguna Telegram (0 = tidak ada)". Nilai default `0` — tidak ada penautan. Field ini tersedia untuk pemfilteran (**Ada** / **Tidak ada**).

#### ID langganan (subId)

**ID langganan** (field `subId`) — pengenal yang digunakan klien untuk disertakan dalam **langganan** (subscription). Semua klien dengan `subId` yang sama akan diberikan melalui satu tautan langganan. Jika field dibiarkan kosong saat pembuatan, panel akan **secara otomatis membuat** `subId` acak (UUID). Nilainya harus **unik** di antara klien dengan email berbeda (`subId already in use`) dan mengikuti pembatasan karakter yang sama dengan email ("ID langganan tidak boleh mengandung spasi, '/', '\', atau karakter kontrol").

Tanpa `subId`, tautan langganan untuk klien tidak tersedia ("Klien ini tidak memiliki subId, tautan berbagi tidak tersedia.").

#### Tab Links (tautan eksternal dan langganan)

Selain tab **Utama** dan **Kredensial**, editor klien memiliki tab ketiga **Links** (petunjuk: "Add third-party share links and remote subscription URLs to include in this client's subscription."). Di tab ini, tombol **Add External Link** digunakan untuk menambahkan share-link pihak ketiga (`vless://`, `vmess://`, `trojan://`, `ss://`, `hysteria2://`, `wireguard://`), sedangkan tombol **Add External Subscription** digunakan untuk menambahkan URL langganan jarak jauh (misalnya, `https://provider.example/sub/…`).

Semua item tersebut dicampur ke dalam output langganan klien ini (format raw, JSON, dan Clash): tautan ditambahkan apa adanya, sedangkan langganan jarak jauh diunduh panel secara berkala (dengan cache dan timeout singkat) dan konfigurasinya digabungkan dengan konfigurasi milik panel sendiri. Dengan cara ini, dalam satu tautan langganan klien, Anda dapat menyertakan konfigurasi eksternal bersama dengan server Anda sendiri.

#### Grup

**Grup** (field `group`) — label logis untuk mengelompokkan klien yang saling berkaitan. Petunjuk: "Label logis untuk mengelompokkan klien yang saling berkaitan (misalnya, tim, pelanggan, wilayah). Dapat difilter dari toolbar.", placeholder — "misalnya, customer-a". Field ini opsional (kosong secara default). Anda dapat memfilter daftar berdasarkan grup dan menjalankan operasi massal; untuk menghapus label dari klien, gunakan aksi **Keluarkan dari grup**.

Anda juga dapat menghapus grup langsung dari editor satu klien: jika Anda mengosongkan field **Grup** dan menyimpan, label akan dihapus dengan benar dan klien tidak akan lagi ditampilkan di bawah grup lama.

#### Komentar

**Komentar** (field `comment`) — catatan teks bebas untuk administrator (kosong secara default). Isinya termasuk dalam pencarian dan tersedia untuk pemfilteran (**Ada** / **Tidak ada** komentar).

#### Diaktifkan

**Diaktifkan** (field `enable`) — flag aktivitas akun. Secara default **diaktifkan** (`true`); saat pembuatan, meskipun flag tidak diteruskan, panel memaksanya menjadi `true`. Klien yang dinonaktifkan (`enable = false`) tidak dapat terhubung dan dalam ringkasan dikategorikan sebagai **tidak aktif** (deactive). Panel secara otomatis menonaktifkan klien yang kuotanya habis, sudah kedaluwarsa, atau melampaui batas IP.

#### Field hanya-baca

Kartu klien juga menampilkan field layanan: **Dibuat** (`created_at`) dan **Diperbarui** (`updated_at`) — stempel waktu pembuatan dan perubahan terakhir, diisi secara otomatis dan tidak dapat diedit. Field **Reverse tag** (`reverse`) — Reverse tag opsional untuk reverse proxy VLESS sederhana ("Reverse tag opsional").

### 8.2. Penautan ke inbound

Setiap klien harus dikaitkan ke setidaknya satu inbound — saat pembuatan diperlukan minimal satu (`at least one inbound is required`). Dalam editor, ini adalah field **Inbound yang ditautkan** dengan petunjuk **Pilih satu atau beberapa inbound**.

- **Tautkan** — tambahkan klien ke inbound yang dipilih (UUID/kata sandi yang sama dan traffic bersama). Penautan yang ada dipertahankan.
- **Lepaskan** — hapus klien dari inbound yang dipilih. Record klien tetap disimpan (untuk penghapusan penuh gunakan **Hapus**). Pasangan di mana klien tidak terkait akan dilewati secara diam-diam.

Saat menyimpan klien yang dikaitkan ke beberapa inbound, field yang tidak kompatibel dengan protokol/transport tertentu (misalnya, Flow di luar VLESS-Vision) secara otomatis disesuaikan ke nilai yang diizinkan untuk setiap inbound.

Di atas daftar pemilihan inbound (dalam formulir klien, saat penambahan klien massal, dan dalam jendela penautkan/pelepasan massal) terdapat tombol **Pilih semua** dan **Hapus pilihan**. Dalam daftar ini, setiap inbound diberi label dengan keterangannya (remark) jika ada, atau dengan tag inbound jika tidak.

### 8.3. Operasi pada klien

Untuk klien individual (melalui kartu **Informasi klien** atau menu konteks **Aksi**) tersedia:

#### Melihat informasi, kode QR, dan tautan

- **Informasi klien** — kartu dengan semua field, traffic yang terpakai/tersisa (**Sisa**), masa berlaku, dan inbound yang ditautkan.

Permintaan klien melalui API (`GET /panel/api/clients/get/:email`) selain field `client` dan `inboundIds` juga mengembalikan `usedTraffic` — traffic yang benar-benar terpakai (terkirim + diterima, termasuk data dari node), yang mempermudah pembandingan penggunaan dengan kuota `totalGB`.
- **Kode QR** dan **Tautan** — tautan konfigurasi klien untuk diimpor ke aplikasi klien. Dibuat berdasarkan semua inbound yang ditautkan dengan protokol yang didukung (`GET /links/:email`). Jika tidak ada tautan yang sesuai: "Tidak ada tautan berbagi — tautkan klien ke inbound dengan protokol yang didukung terlebih dahulu.".
- **Tautan langganan** — URL langganan berdasarkan `subId` (`GET /subLinks/:subId`). Hanya tersedia jika klien memiliki `subId` dan layanan langganan diaktifkan di **Pengaturan panel → Langganan** (jika tidak, "Layanan langganan dinonaktifkan."). Selain itu, **URL langganan JSON** juga tersedia.

#### Reset traffic

**Reset traffic** (`POST /resetTraffic/:email`) mereset penghitung kirim/terima (`up`, `down`) klien tertentu ke nol. Kuota (`totalGB`) dan masa berlaku **tidak terpengaruh** — hanya volume yang terpakai yang direset. Toast: "Traffic direset". Jika klien tidak dikaitkan ke inbound mana pun: "Tautkan klien ini ke inbound terlebih dahulu.".

Tombol **Reset traffic** juga tersedia dari formulir pengeditan klien — di panel bawah, di samping **Batal** / **Simpan** (konfirmasi diminta sebelum reset). Jika klien dinonaktifkan karena traffic habis, reset (baik tunggal maupun massal) secara otomatis **mengaktifkan kembali** klien (`enable = true`) dan segera menyebarkan perubahan ini ke node — Anda tidak perlu lagi mengaktifkan ulang klien secara manual di master dan node.

#### Reset batas IP

Menghapus log IP klien yang terkumpul (`POST /clearIps/:email`) untuk mencabut pemblokiran sementara akibat melampaui batas koneksi simultan. Toast: "Log telah dihapus".

#### Hapus

**Hapus** (`POST /del/:email`) — penghapusan penuh klien. Dialog konfirmasi: judul "Hapus klien {email}?", teks "Klien akan dihapus dari semua inbound yang ditautkan, dan record traffic-nya akan dihancurkan. Tindakan ini tidak dapat dibatalkan.". Penghapusan melepas klien dari **semua** inbound dan menghancurkan record traffic-nya. Toast: "Klien dihapus".

### 8.4. Operasi massal

Dalam daftar klien, Anda dapat mencentang beberapa record (**Pilih semua**, **Hapus semua**); penghitung — "{count} dipilih". Untuk item yang dipilih, tersedia:

- **Hapus ({count})** (`POST /bulkDel`) — penghapusan grup. Konfirmasi: "Hapus {count} klien?", "Setiap klien yang dipilih akan dihapus dari semua inbound yang ditautkan, record traffic-nya dihancurkan. Tindakan ini tidak dapat dibatalkan.". Toast: "Klien dihapus: {count}", jika sebagian gagal — "Dihapus: {ok}, gagal: {failed}".
- **Ubah ({count})** / **Penyesuaian** (`POST /bulkAdjust`) — perubahan massal masa berlaku dan/atau kuota. Dialog "Ubah {count} klien" dengan petunjuk "Nilai positif menambahkan, nilai negatif mengurangi. Klien dengan masa berlaku atau traffic tanpa batas akan dilewati untuk field yang bersangkutan.". Field: **Tambah hari** dan **Tambah traffic (GB)**. Logikanya:
  - **Masa berlaku:** klien dengan masa berlaku tanpa batas (`expiryTime == 0`) dilewati ("unlimited expiry"); untuk klien dengan tanggal, masa berlaku digeser sebesar jumlah hari yang ditentukan; untuk klien dalam mode "setelah penggunaan pertama" (masa berlaku negatif), durasi tunggu disesuaikan. Pengurangan yang melampaui sisa waktu akan dilewati ("reduction exceeds remaining time/delay window").
  - **Traffic:** klien tanpa batas (`totalGB == 0`) dilewati ("unlimited traffic"); jika tidak, kuota diubah sebesar volume yang ditentukan, tidak turun di bawah nol.
  - Jika hari maupun traffic tidak ditentukan: "Tentukan hari atau traffic sebelum menerapkan.". Toast: "Diubah: {count}" / "Diubah: {ok}, dilewati: {skipped}".

**Contoh: perpanjang klien yang dipilih 30 hari dan tambahkan 50 GB.** Dalam dialog **Ubah**, masukkan **Tambah hari** = `30`, **Tambah traffic (GB)** = `50`. Untuk sebaliknya, kurangi seminggu dan pangkas kuota sebesar 10 GB, masukkan nilai negatif: **Tambah hari** = `-7`, **Tambah traffic (GB)** = `-10` (klien dengan masa berlaku tanpa batas atau traffic tanpa batas pada field yang bersangkutan akan dilewati).
- **Tautkan ({count})** / **Lepaskan ({count})** (`POST /bulkAttach` / `bulkDetach`) — penautan/pelepasan massal klien yang dipilih ke inbound yang dipilih. Target hanya inbound multi-pengguna. Hasil pelepasan: "Dilepaskan {detached}, dilewati {skipped}.".
- **Tautan sub ({count})** — tabel ringkasan URL langganan dan langganan JSON dari klien yang dipilih, dengan tombol **Salin semua**. Jika tidak ada yang memiliki subId: "Tidak ada klien yang dipilih yang memiliki ID langganan.".
- **Tambahkan ke grup** dan **Keluarkan dari grup** — menetapkan dan menghapus label grup.

#### Reset traffic dan penghapusan berdasarkan status

- **Reset traffic semua klien** (`POST /resetAllTraffics`) — mereset penghitung `up`/`down` pada **semua** klien panel. Konfirmasi: "Reset traffic semua klien?" dan "Penghitung kirim/terima semua klien akan direset ke nol. Kuota dan masa berlaku tidak terpengaruh. Tindakan ini tidak dapat dibatalkan.". Toast: "Traffic semua klien direset".
- **Hapus yang habis** (`POST /delDepleted`) — menghapus semua klien yang **kuotanya habis** (`total > 0 and up + down >= total`) **atau masa berlakunya kedaluwarsa** (`expiry_time > 0 and expiry_time <= sekarang`), dengan syarat `reset = 0` (klien dengan perpanjangan otomatis tidak tersentuh). Konfirmasi: "Hapus klien yang habis?", "Semua klien yang kuota traffic-nya habis atau masa berlakunya kedaluwarsa akan dihapus. Tindakan ini tidak dapat dibatalkan.". Toast: "Klien yang habis dihapus: {count}".

#### Ekspor, impor, dan penghapusan klien yang tidak terkait

Saat tidak ada yang dipilih, menu **Lainnya** di halaman **Klien** menyediakan tiga operasi.

**Ekspor klien** (`GET /clients/export`) membuka penampil dengan daftar JSON semua klien dalam format `{client, inboundIds}` beserta tombol salin dan unduh (file `clients-export.json`). **Impor klien** (`POST /clients/import`) membuka editor tempat Anda menempelkan JSON yang sama dan menekan **Import**: klien dengan `inboundIds` akan dibuat dan dikaitkan ke inbound, klien tanpa penautan akan dipulihkan sebagai record "kosong" terpisah, sedangkan email yang sudah ada **tidak akan pernah ditimpa** — mereka masuk ke daftar yang dilewati. Toast: "{count} clients imported", "{ok} imported, {failed} skipped".

**Hapus klien yang tidak terkait** (`POST /clients/delOrphans`) — operasi berbahaya: menghapus semua klien yang tidak dikaitkan ke inbound mana pun, beserta record traffic, log IP, dan tautan eksternalnya. Konfirmasi: "Delete clients without an inbound?", "Removes every client that is not attached to any inbound, along with its traffic record. This cannot be undone.". Toast: "{count} unattached clients deleted". Tindakan ini tidak dapat dibatalkan.

### 8.5. Pencarian, filter, dan pengurutan

Di atas daftar terdapat kolom pencarian ("Cari email, komentar, sub ID, UUID, kata sandi, auth…") — mencari berdasarkan email, komentar, subId, UUID, kata sandi, dan auth. Penghitung hasil: "Menampilkan {shown} dari {total}".

Daftar klien diperbarui secara otomatis: panel mengambil halaman saat ini yang terbaru setiap beberapa detik, sehingga klien yang baru terhubung dan urutan pengurutan yang berubah akan muncul tanpa pembaruan manual (indikator pemuatan tidak berkedip saat polling latar belakang berlangsung).

Panel **Filter klien** memungkinkan pemfilteran berdasarkan status (kategori), protokol, inbound yang dikaitkan, rentang masa berlaku, rentang traffic yang digunakan, keberadaan perpanjangan otomatis (**Ada/Tidak ada**), keberadaan ID Telegram dan komentar, serta berdasarkan grup. Pada panel dengan node, muncul multiselect **Node**: Anda dapat membatasi daftar ke klien dari node yang dipilih; item terpisah **Panel lokal** memfilter klien inbound yang tidak terkait ke node (filter hanya terlihat jika ada node). Pengurutan: **Terlama/Terbaru**, **Baru diperbarui**, **Baru online**, **Email A→Z / Z→A**, **Traffic terbanyak**, **Sisa terbanyak**, **Segera kedaluwarsa**.

### 8.6. Ikon dan status

Prioritas status: habis/kedaluwarsa → tidak aktif → segera kedaluwarsa → aktif.

- **Online** / **Offline** — klien dengan koneksi aktif (ada dalam daftar online saat ini) dan **diaktifkan**. Daftar online diperbarui dengan permintaan terpisah (`/onlines`, `/onlinesByGuid`).
- **Habis** (depleted) — kuota terpakai (`up + down >= totalGB`) **atau** masa berlaku kedaluwarsa (`expiryTime <= sekarang`). Klien tersebut secara otomatis dinonaktifkan dan menjadi subjek aksi **Hapus yang habis**.
- **Segera kedaluwarsa / hampir habis** (expiring) — klien yang diaktifkan, dengan sisa waktu hingga kedaluwarsa kurang dari interval ambang batas **atau** sisa kuota traffic kurang dari volume ambang batas (ambang batas ditentukan di pengaturan panel). Tidak berlaku jika klien sudah habis/dinonaktifkan.
- **Tidak aktif** (deactive) — klien dengan `enable = false` (dinonaktifkan secara manual atau oleh tugas latar belakang).
- **Aktif** (active) — diaktifkan, tidak habis, masa berlaku belum kedaluwarsa, dan masih jauh dari ambang batas.

---

## 9. Grup Klien

> Ini adalah fitur fork 3X-UI ini. Pada proyek 3x-ui asli (MHSanaei) tidak ada konsep "grup klien" — di sini ditambahkan tabel grup tersendiri, halaman **Grup** di menu panel, dan metode API yang sesuai. Jika Anda memindahkan konfigurasi ke 3x-ui asli, label grup hanya tidak akan diperhitungkan di mana pun.

### 9.1. Apa itu grup klien dan untuk apa

**Grup** adalah label logis bernama (label) yang dapat ditempelkan pada satu atau beberapa klien. Grup tidak membuat cara koneksi baru dan bukan merupakan inbound maupun node — ini murni label organisasi yang memudahkan penyaringan dan pemrosesan massal klien.

Ide utama model klien di fork ini: **klien adalah entitas tingkat atas yang diidentifikasi berdasarkan email** (kolom `email` di tabel `clients` memiliki indeks unik). Klien yang sama (satu email dengan kredensial yang sama) dapat terdaftar di beberapa inbound sekaligus dan bahkan di beberapa node, termasuk dengan protokol yang berbeda. Label grup disimpan **satu kali per klien**, sehingga secara otomatis berlaku untuk semua binding klien ke inbound sekaligus.

Label grup adalah label logis untuk pengelompokan:

| Lapisan | Tempat penyimpanan | Kolom |
|------|--------------|------|
| Catatan klien (DB) | tabel `clients` | `group_name` (defaultnya string kosong `''`) |
| Daftar referensi grup (DB) | tabel `client_groups` | `name` (indeks unik, tidak boleh kosong) |
| Pengaturan inbound (Xray) | JSON `settings.clients[].group` | diduplikasi ke setiap objek klien di setiap inbound tempat klien terdaftar |

Mengapa ini diperlukan dalam praktik:

- **Satu klien di beberapa inbound/node.** Jika klien "dijual" sebagai akses ke beberapa inbound sekaligus (misalnya protokol berbeda atau node berbeda), grup memungkinkan pengelolaan sebagai satu kesatuan: mereset traffic, menghapus, mengganti nama label — dalam satu operasi untuk semua inbound-nya.
- **Operasi massal dan penyaringan.** Di halaman **Klien**, daftar dapat difilter berdasarkan grup; di halaman **Grup** tersedia tindakan massal terhadap semua anggota grup.
- **Pengorganisasian kumpulan klien yang besar.** Label seperti `vip`, `trial`, `team-A` membantu menempatkan ribuan klien ke dalam keranjang logis tanpa harus membuat banyak inbound terpisah.

### 9.2. Hubungan grup dengan klien, inbound, node, dan protokol

Ini adalah subbagian terpenting untuk dipahami, karena sinkronisasi label tidaklah sepele.

**Grup mendeskripsikan klien, bukan inbound.** Label hidup di catatan klien (`clients.group_name`). Ketika klien terdaftar di beberapa inbound, setiap kali grup berubah, panel menelusuri **semua** inbound tempat klien tersebut terdaftar dan menetapkan/menghapus kolom `group` di dalam pengaturan Xray-nya (`settings.clients[]`). Secara teknis ini dilakukan sebagai berikut: berdasarkan email klien, semua inbound tempat klien terdaftar ditemukan, lalu objek klien dengan email tersebut diperbaiki di JSON pengaturan masing-masing inbound. Oleh karena itu:

- Grup **tidak bergantung pada protokol.** Satu email bisa menjadi klien VLESS di satu inbound dan klien Hysteria di inbound lain — label grup tetap satu dan akan diterapkan ke keduanya (kredensial untuk setiap protokol berbeda dan disimpan secara terpisah).
- Grup **mencakup node.** Inbound yang dimiliki node berbeda dari inbound panel utama berdasarkan kolom `nodeId` (pada inbound panel utama nilainya `null`/`0`). Label grup disebarkan ke objek klien di inbound terlepas dari apakah itu inbound utama atau inbound node — selama klien dengan email tersebut ada di sana.

**Label grup tahan terhadap sinkronisasi dari node dan terhadap pembangunan ulang pengaturan.** Perilaku ini dirancang secara khusus:

- Ketika node mengirimkan snapshot traffic, datanya **tidak menimpa** `group_name` dan `comment` lokal klien di DB panel. Grup dan komentar dianggap sebagai kolom "lokal panel" — node tidak mengelolanya.
- Saat pembangunan ulang pengaturan inbound, nilai `group` kosong dalam data yang masuk **tidak mereset** label yang sudah tersimpan. Grup dikelola khusus melalui halaman **Grup** (bukan melalui pengeditan pengaturan Xray inbound), sehingga "grup kosong" pada pembangunan ulang pengaturan biasa diartikan sebagai "jangan diubah", bukan "hapus".

Kesimpulan praktis: satu-satunya operasi yang **secara sengaja menghapus** label adalah penghapusan grup dan penghapusan klien dari grup secara eksplisit (lihat di bawah). Pengeditan inbound biasa atau sinkronisasi latar belakang dengan node tidak akan menghilangkan grup.

### 9.3. Daftar referensi grup dan grup "kosong"

Daftar grup di halaman dibentuk dari penggabungan dua sumber:

1. **Grup turunan (derived)** — semua nilai `group_name` tidak kosong yang benar-benar ditemukan pada klien, dengan hitungan jumlah klien.
2. **Grup tersimpan (stored)** — catatan dari tabel `client_groups`.

Penggabungan ini menghasilkan efek penting: grup dapat ada **tanpa satu pun klien**. Grup seperti itu dibuat melalui tombol "Tambah Grup" yang eksplisit (catatan di `client_groups`) dan ditampilkan dalam daftar dengan penghitung `0`. Catatan inilah yang disebut **grup kosong**. Daftar selalu diurutkan berdasarkan nama tanpa memperhatikan huruf kapital.

Penghitung ringkasan di halaman:

| Kolom (RU) | Yang ditampilkan |
|-----------|----------------|
| Всего групп | Jumlah total grup (tersimpan dan turunan digabungkan). |
| Клиенты с группой | Berapa banyak klien yang memiliki label grup tidak kosong. |
| Пустые группы | Berapa banyak grup yang ada tanpa klien (penghitung `0`). |
| Клиентов в группе | Jumlah klien di grup tertentu (kolom tabel). |

### 9.4. Kolom dan bidang grup

Catatan grup di tabel `client_groups` berisi:

| Kolom | Tipe | Default | Deskripsi |
|------|-----|--------------|----------|
| `Id` | int | auto-increment | Kunci primer catatan grup. |
| `Name` | string | — (wajib diisi) | Nama grup. Indeks unik, tidak boleh kosong. Di UI — kolom **Nama**. |
| `CreatedAt` | int64 (ms) | waktu pembuatan | Waktu pembuatan catatan grup. |
| `UpdatedAt` | int64 (ms) | waktu perubahan | Waktu perubahan terakhir. |

Tabel di halaman menampilkan setidaknya kolom **Nama** dan **Jumlah Klien di Grup**, serta tombol tindakan (lihat di bawah).

### 9.5. Membuat grup

Tombol **Tambah Grup**.

Langkah-langkah:
1. Klik **Tambah Grup**.
2. Masukkan nama grup.
3. Konfirmasi.

Perilaku backend (`POST /panel/api/clients/groups/create`, body `{"name": "..."}`):
- Nama dipangkas spasi di kedua ujung. Nama kosong ditolak dengan error "group name is required".
- Jika grup dengan nama tersebut sudah ada — error "group already exists".
- Jika berhasil, catatan dibuat di `client_groups` (awalnya tanpa klien — ini adalah grup kosong).

Pesan sukses: **«Grup «{name}» telah dibuat.»**

**Contoh: membuat grup kosong melalui API.** Siapkan sekumpulan label terlebih dahulu, sebelum diisi klien:

```bash
curl -s 'https://panel.example.com:2053/panel/api/clients/groups/create' \
  -H 'Content-Type: application/json' \
  -b cookie.txt \
  -d '{"name": "vip"}'
```

Respons jika berhasil:

```json
{ "success": true, "msg": "Группа «vip» создана.", "obj": null }
```

Pemanggilan ulang dengan nama yang sama akan mengembalikan `"success": false` dan pesan `group already exists`.

> Membuat grup kosong terlebih dahulu berguna ketika Anda ingin menyiapkan sekumpulan label dan kemudian mengisinya dengan klien melalui "Tambahkan klien…".

### 9.6. Mengganti nama grup

Tombol **Ganti Nama**, judul dialog — **«Ganti nama {name}»**.

Perilaku (`POST /panel/api/clients/groups/rename`, body `{"oldName": "...", "newName": "..."}`):
- Kedua nama dipangkas spasi. Nama lama kosong — error "old group name is required", nama baru kosong — "new group name is required".
- Jika nama baru sama dengan nama lama — tidak ada yang dilakukan (0 klien terpengaruh).
- Selain itu, penggantian nama dilakukan secara atomik:
  - catatan di `client_groups` diubah namanya;
  - pada semua klien dengan `group_name = oldName`, kolom diperbarui ke `newName`;
  - di **semua inbound** tempat klien yang terpengaruh terdaftar (termasuk node), nilai `group` di pengaturan Xray diubah dari yang lama ke yang baru.
- Setelah penggantian nama, panel menandai Xray sebagai memerlukan restart dan mengirimkan notifikasi perubahan klien.

Pesan:
- Sukses: **«Grup diganti nama untuk {count} klien.»**
- Konflik nama di UI: **«Grup dengan nama «{name}» sudah ada.»**

### 9.7. Menambahkan klien ke grup

Tombol **Tambahkan klien…**, judul — **«Tambahkan klien ke grup «{name}»»**.

Keterangan persis di dialog:

> «Pilih klien untuk ditambahkan ke grup ini. Binding yang ada ke inbound tetap dipertahankan; hanya label grup yang berubah. Klien yang sudah termasuk dalam grup ini tidak ditampilkan.»

Jika tidak ada yang bisa ditambahkan, ditampilkan **«Tidak ada klien lain untuk ditambahkan.»**

Perilaku (`POST /panel/api/clients/groups/bulkAdd`, body `{"emails": [...], "group": "..."}`):
- Nama grup wajib diisi (jika tidak, error "group name is required"); daftar email kosong — operasi tidak melakukan apa pun.
- Jika grup tersebut belum ada di `client_groups` maupun di antara grup turunan — grup akan dibuat secara otomatis.
- Untuk email yang dipilih, `group_name = group` ditetapkan pada klien; **binding klien ke inbound tidak berubah** — hanya label yang terpengaruh. Kemudian kolom `group` ditetapkan di semua inbound klien tersebut.
- Mengembalikan jumlah catatan klien yang terpengaruh; Xray ditandai untuk di-restart.

Pesan sukses: **«{count} klien ditambahkan ke {name}.»**

**Contoh: menandai beberapa klien dengan grup dalam satu permintaan.** Klien ditentukan berdasarkan email, binding ke inbound tidak berubah:

```bash
curl -s 'https://panel.example.com:2053/panel/api/clients/groups/bulkAdd' \
  -H 'Content-Type: application/json' \
  -b cookie.txt \
  -d '{"emails": ["alice@example.com", "bob@example.com"], "group": "vip"}'
```

Jika grup `vip` belum ada, grup akan dibuat secara otomatis. Setelah permintaan, klien-klien ini akan memiliki `group_name = "vip"` di catatannya, dan objek klien di pengaturan Xray setiap inbound mereka akan mendapat kolom `"group": "vip"`:

```json
{ "id": "6f1b...", "email": "alice@example.com", "group": "vip", "enable": true }
```

### 9.8. Menghapus klien dari grup (tanpa menghapus klien itu sendiri)

Tombol **Hapus klien…**, judul — **«Hapus klien dari grup «{name}»»**.

Keterangan persis:

> «Pilih anggota untuk dihapus dari grup ini. Klien itu sendiri tetap dipertahankan (gunakan "Hapus klien grup" untuk penghapusan penuh).»

Perilaku (`POST /panel/api/clients/groups/bulkRemove`, body `{"emails": [...]}`): secara teknis ini sama seperti "Tambahkan ke grup" dengan grup kosong. Pada klien yang dipilih, `group_name` dihapus, dan kolom `group` dihapus dari pengaturan Xray inbound mereka. Klien itu sendiri dan binding mereka ke inbound tetap dipertahankan.

Pesan sukses: **«{count} klien dihapus dari {name}.»**

### 9.9. Mereset traffic grup

Tombol **Reset Traffic**.

Dialog konfirmasi:
- Judul: **«Reset traffic grup {name}?»**
- Teks: **«Ini akan mengatur ulang up/down untuk semua {count} klien di grup ini.»**

Perilaku: untuk semua email anggota grup, `up` dan `down` di tabel traffic diatur ke nol dan kolom `enable` diatur ke `true` (klien diaktifkan). Operasi dilakukan dalam batch di dalam transaksi.

Pesan sukses: **«Traffic {count} klien telah direset.»**

### 9.10. Menghapus grup dan menghapus klien grup

Di halaman terdapat **dua operasi penghapusan yang pada dasarnya berbeda** — mudah tertukar, sehingga perbedaannya sangat penting.

#### 9.10.1. Hapus grup (pertahankan klien)

Tombol **«Hapus grup (pertahankan klien)»**.

Dialog:
- Judul: **«Hapus grup {name}?»**
- Teks: **«Ini menghapus grup dan menghapus labelnya dari {count} klien. Klien itu sendiri tidak dihapus.»**

Perilaku (`POST /panel/api/clients/groups/delete`, body `{"name": "..."}`): catatan grup dihapus dari `client_groups`, `group_name` semua kliennya dihapus, dan kolom `group` dihapus dari inbound mereka. **Klien, koneksi, dan traffic mereka tetap dipertahankan.** Xray ditandai untuk di-restart.

Pesan sukses: **«Grup dihapus dari {count} klien.»**

#### 9.10.2. Hapus klien grup (penghapusan penuh)

Tombol **«Hapus klien grup»**.

Dialog:
- Judul: **«Hapus semua klien di {name}?»**
- Teks: **«Ini menghapus {count} klien secara permanen beserta catatan traffic mereka. Label grup juga dihapus. Tindakan ini tidak dapat dibatalkan.»**

Ini adalah operasi destruktif: operasi ini menghapus klien itu sendiri (melalui penghapusan massal berdasarkan email, endpoint `POST /panel/api/clients/bulkDel`), termasuk catatan traffic mereka, sehingga menghapus mereka dari semua inbound.

Pesan:
- Sukses: **«{count} klien dihapus.»**
- Hasil parsial: **«{ok} dihapus, {failed} dilewati»**

> Jika grup kosong, tindakan terhadap anggotanya tidak tersedia — ditampilkan **«Grup ini belum memiliki klien.»**

### 9.11. Hubungan dengan halaman "Klien"

Label grup terlihat dan digunakan di luar halaman **Grup** juga:

- Dalam catatan kompak klien terdapat kolom `group`, sehingga keanggotaan grup ditampilkan dalam daftar klien.
- Daftar klien (`/panel/api/clients/list/paged`) menerima parameter filter `group`: dapat diteruskan satu nama atau beberapa nama yang dipisahkan koma. Pencocokan dilakukan berdasarkan prinsip "ATAU" di dalam kolom, tanpa memperhatikan huruf kapital. Kasus khusus: elemen kosong dalam daftar grup filter berarti "klien tanpa grup" (yang `group`-nya kosong).
- Dalam respons halaman klien, array `groups` dikembalikan — daftar lengkap nama grup yang ada, agar UI dapat membuat dropdown filter.

**Contoh: memfilter klien berdasarkan grup.** Permintaan mengembalikan hanya klien dengan label `vip` atau `trial` (beberapa nama — dipisahkan koma, "ATAU"):

```
GET /panel/api/clients/list/paged?group=vip,trial
```

Untuk mendapatkan klien **tanpa** grup, teruskan elemen kosong dalam daftar — misalnya, nilai filter `group=` (string kosong) atau `group=vip,` (label `vip` ditambah klien tanpa grup).

### 9.12. Ringkasan endpoint API

Semua rute grup dipasang di bawah `/panel/api/clients`:

| Metode dan path | Tujuan | Body permintaan |
|--------------|-----------|--------------|
| `GET /panel/api/clients/groups` | Daftar grup dengan penghitung klien | — |
| `GET /panel/api/clients/groups/:name/emails` | Email semua anggota grup (diurutkan berdasarkan email) | — |
| `POST /panel/api/clients/groups/create` | Membuat grup kosong | `{"name"}` |
| `POST /panel/api/clients/groups/rename` | Mengganti nama grup | `{"oldName","newName"}` |
| `POST /panel/api/clients/groups/delete` | Menghapus grup, mempertahankan klien (menghapus label) | `{"name"}` |
| `POST /panel/api/clients/groups/bulkAdd` | Menambahkan klien ke grup (berdasarkan email) | `{"emails":[...],"group"}` |
| `POST /panel/api/clients/groups/bulkRemove` | Menghapus klien dari grup (menghapus label) | `{"emails":[...]}` |
| `POST /panel/api/clients/bulkDel` | Penghapusan penuh klien (digunakan oleh "Hapus klien grup") | `{"emails":[...],"keepTraffic"}` |

**Contoh: skenario tipikal siklus hidup grup melalui API.**

```bash
# 1. Buat label trial
curl -s .../panel/api/clients/groups/create   -d '{"name":"trial"}'

# 2. Tempelkan ke dua klien
curl -s .../panel/api/clients/groups/bulkAdd  -d '{"emails":["u1@example.com","u2@example.com"],"group":"trial"}'

# 3. Nolkan traffic semua anggota (berdasarkan email dari /groups/trial/emails)
curl -s .../panel/api/clients/groups/bulkRemove -d '{"emails":["u2@example.com"]}'

# 4. Hapus grup, tapi pertahankan klien (hanya menghapus label)
curl -s .../panel/api/clients/groups/delete   -d '{"name":"trial"}'
```

Langkah 4 menghapus catatan grup dan menghapus `group_name` pada kliennya, tetapi klien itu sendiri, koneksi, dan traffic mereka tetap ada. Untuk penghapusan permanen klien itu sendiri, gunakan `bulkDel`.

Operasi yang mengubah label pada klien (`rename`, `delete`, `bulkAdd`, `bulkRemove`) menandai Xray sebagai memerlukan restart dan mengirimkan notifikasi perubahan klien.

### 9.13. Traffic per grup

Fitur baru versi 3.3.0: di bagian **Grup** (halaman "Klien", tab manajemen grup) tabel grup kini menampilkan tidak hanya jumlah klien di setiap grup, tetapi juga total traffic yang telah digunakan oleh grup. Kolom diberi label **«Traffic yang Digunakan»**.

#### Apa yang ditampilkan kolom ini

Untuk setiap baris grup ditampilkan jumlah traffic dari semua klien yang termasuk dalam grup tersebut — yaitu `up + down` (traffic terkirim + diterima) yang dijumlahkan dari semua anggotanya. Ini memberikan jawaban cepat atas pertanyaan "berapa total yang diunduh/diunggah oleh seluruh grup", tanpa perlu membuka klien satu per satu dan menjumlahkan secara manual.

Di samping itu, dalam tabel grup ditampilkan:

| Kolom | Artinya |
|---|---|
| Nama | Nama grup |
| Klien | Berapa banyak klien yang ditandai dengan grup ini (sebelumnya kolom disebut "Jumlah Klien di Grup") |
| Terkirim | Total `up` (traffic terkirim) dari semua klien grup |
| Diterima | Total `down` (traffic diterima) dari semua klien grup |
| Traffic yang Digunakan | Total `up + down` dari semua klien grup |

Traffic terkirim dan diterima ditampilkan dalam kolom terpisah **Terkirim** dan **Diterima**, sedangkan kolom **Traffic yang Digunakan** menampilkan jumlahnya. Kolom jumlah klien cukup disebut **Klien**.

Ringkasan di atas tabel juga menampilkan agregat dari semua grup — **«Total grup»** dan **«Klien dengan grup»**, sementara total traffic dibagi menjadi dua kartu: **«Total terkirim / diterima»** (dengan panah atas/bawah — traffic terkirim dan diterima semua grup secara terpisah) dan **«Total traffic»** (dengan ikon diagram — total gabungannya).

#### Cara penghitungan

Penghitungan dilakukan dengan satu kueri SQL ke tabel klien dengan join (`LEFT JOIN`) tabel pencatatan traffic:

- berdasarkan kolom label grup (`group_name`), klien dikelompokkan dan jumlahnya dihitung — itulah "Jumlah Klien di Grup";
- traffic diambil sebagai jumlah `up + down` dari tabel `client_traffics` yang di-join. Artinya, byte terkirim (`up`) dan byte diterima (`down`) dijumlahkan untuk setiap klien;
- karena email unik di tabel klien maupun di tabel traffic, join tidak menduplikasi traffic satu klien.

Kekhususan nilai:

- **Klien tanpa catatan traffic** dihitung dalam penghitung anggota, tetapi menambahkan 0 ke jumlah, sehingga grup yang baru dibuat menampilkan traffic `0`.
- **Grup kosong** (dibuat tetapi tanpa klien) juga ada dalam daftar dengan penghitung nol dan traffic nol: selain grup yang "diturunkan" dari label klien, grup yang tersimpan secara eksplisit dimasukkan ke dalam hasil, setelah itu daftar diurutkan berdasarkan nama tanpa memperhatikan huruf kapital.
- Klien tanpa label grup (`group_name` kosong) tidak masuk dalam penghitungan.

#### Tindakan terkait

Dari tabel grup, tindakan terhadap grup secara keseluruhan tetap tersedia, termasuk **«Reset Traffic»** — mengatur nol `up`/`down` semua klien di grup yang dipilih. Setelah reset tersebut, kolom "Traffic yang Digunakan" untuk grup ini menampilkan `0`.

---

## 10. Langganan (Subscription)

Langganan (subscription) adalah mekanisme yang memungkinkan Anda memberikan satu tautan tetap (URL) kepada klien, di mana aplikasi VPN secara otomatis mengunduh dan memperbarui secara berkala seluruh kumpulan konfigurasi. Alih-alih mengirimkan tautan terpisah untuk setiap inbound secara manual, pengguna cukup mendapatkan satu alamat seperti `https://domain:port/sub/<subId>`. Melalui alamat ini, panel secara dinamis mengumpulkan semua konfigurasi yang terhubung ke klien tersebut dan mengirimkannya dalam format yang dibutuhkan klien. Ketika pengaturan di server berubah (alamat baru, rotasi kunci Reality, penambahan inbound), klien akan mendapatkan konfigurasi terbaru pada pembaruan otomatis berikutnya tanpa memerlukan tindakan apa pun dari pengguna.

Langganan dilayani oleh server HTTP/HTTPS tersendiri di dalam panel, yang berjalan secara independen dari panel web dan mendengarkan pada portnya sendiri. Hal ini dilakukan demi alasan keamanan: port langganan dapat dibuka ke luar tanpa harus membuka port panel itu sendiri.

### 10.1. Apa itu subId dan bagaimana tautan terbentuk

Setiap klien di dalam inbound memiliki field `subId` (di antarmuka disebut «ID Langganan»). Nilai inilah yang menjadi kunci langganan: panel mencari di semua inbound klien yang nilai `subId`-nya cocok dengan yang diminta, lalu menggabungkan konfigurasi mereka menjadi satu respons.

- Jika beberapa klien (dalam satu inbound maupun inbound yang berbeda) memiliki `subId` yang sama, konfigurasi mereka akan masuk ke dalam satu langganan. Ini adalah cara standar untuk memberikan satu tautan kepada pengguna yang mencakup beberapa server/protokol sekaligus.

**Contoh: satu pengguna — dua server dalam satu tautan.** Misalkan ada dua inbound (VLESS di server A dan Trojan di server B). Untuk memberikan kedua konfigurasi kepada pengguna dalam satu tautan, tetapkan `subId` yang sama pada kedua kliennya:

```
Inbound 1 (VLESS):  email = ivan@vpn,  subId = ivan2025
Inbound 2 (Trojan): email = ivan@vpn,  subId = ivan2025
```

Maka melalui alamat `https://sub.example.com:2096/sub/ivan2025` panel akan mengirimkan kedua konfigurasi sekaligus. Jika Anda menambahkan inbound ketiga dengan `subId` yang sama di kemudian hari, inbound tersebut akan muncul pada pengguna saat pembaruan langganan berikutnya, tanpa perlu mengirimkan tautan baru.
- Jika field `subId` klien kosong, tautan untuk akses bersama tidak tersedia. Antarmuka menunjukkan petunjuk: «Klien ini tidak memiliki subId, tautan akses bersama tidak tersedia.»

#### Tautan eksternal dan langganan klien (tab «Links»)

Di formulir klien terdapat tab **«Links»**, di mana untuk klien tertentu Anda dapat melampirkan sumber konfigurasi tambahan yang dicampurkan khusus ke dalam langganannya (format RAW, JSON, dan Clash):

- **Add External Link** — tautan berbagi pihak ketiga (`vless://`, `trojan://`, `ss://`, dll.). Ditambahkan ke output apa adanya, dan untuk JSON/Clash juga diuraikan menjadi konfigurasi.
- **Add External Subscription** — alamat langganan eksternal. Panel mengunduhnya secara otomatis (dengan caching dan timeout singkat) lalu menggabungkan konfigurasi yang diperoleh ke dalam daftar umum klien.

Fitur ini berguna untuk memberikan klien server tambahan di luar inbound Anda melalui tautan tunggal yang sama. Jika respons dari langganan jarak jauh terlalu besar, kini tidak lagi dipotong diam-diam: panel mengembalikan error dan tetap menggunakan nilai yang terakhir berhasil di-cache.
- Nilai `subId` tidak dapat ditetapkan secara sembarangan: saat menyimpan, sistem memverifikasi bahwa nilainya tidak mengandung spasi, karakter `/`, `\`, atau karakter kontrol. Petunjuk validasi yang sesuai: «ID Langganan tidak boleh mengandung spasi, '/', '\', atau karakter kontrol».

Tautan akhir dibentuk sebagai `<basis>/<subPath>/<subId>` (lihat bagian tentang pengaturan server langganan dan field «URI reverse proxy»). Jika tidak ditemukan satu pun klien berdasarkan `subId` (klien dihapus, `subId` tidak ada), server mengembalikan HTTP 404 tanpa body. Saat terjadi error internal — HTTP 500. Klien VPN hanya memperhatikan kode respons, sehingga body error sengaja dikosongkan.

#### Urutan tautan inbound dalam langganan

Setiap inbound memiliki field **«Urutan dalam langganan»** (`subSortIndex`) — angka mulai dari 1 yang menentukan posisi tautan inbound tersebut dalam output langganan. Nilai yang lebih kecil tampil lebih dulu; jika nilainya sama, urutan pembuatan asli (berdasarkan id) dipertahankan. Urutan ini berlaku untuk semua format output — teks mentah, halaman langganan, JSON, dan Clash. Field ini tidak memengaruhi urutan inbound di panel itu sendiri.

Field ini dapat diedit di formulir inbound di sebelah pengaturan alamat tautan (share address) dan disinkronkan ke node sesuai aturan yang berlaku. Jika setidaknya satu inbound memiliki urutan selain 1, kolom **«Urutan»** yang ringkas akan muncul di daftar Inbounds.

### 10.2. Pengaturan server langganan

Semua parameter langganan terdapat di bagian pengaturan panel pada tab **«Langganan»**. Di bawah ini setiap parameter dijelaskan satu per satu; nama kunci pengaturan internal dan nilai defaultnya ditampilkan dalam tanda kurung.

Bagian ini sendiri dibagi menjadi beberapa tab: **«Pengaturan Panel»**, **«Informasi»**, **«Profil»**, **«Sertifikat»**, **«Happ»**, dan **«Clash / Mihomo»**. Field judul langganan, URL dukungan, halaman profil, pengumuman, dan direktori tema terdapat di tab «Profil»; aturan routing Happ dan Clash/Mihomo berada di tab masing-masing; interval pembaruan langganan berada di tab «Informasi».

#### Parameter utama

| Field (UI) | Kunci | Nilai default | Deskripsi |
|---|---|---|---|
| Aktifkan langganan | `subEnable` | `true` (aktif) | Menjalankan server langganan terpisah. Petunjuk: «Fitur langganan dengan konfigurasi terpisah». Jika dinonaktifkan — server langganan tidak berjalan, dan tidak satu pun tautan yang berfungsi. |
| IP yang didengarkan | `subListen` | kosong | Alamat IP tempat server langganan menerima koneksi. Petunjuk: «Biarkan kosong secara default untuk memantau semua alamat IP». |
| Port langganan | `subPort` | `2096` | Port TCP server langganan. Petunjuk: «Nomor port untuk melayani layanan langganan tidak boleh digunakan di server» — port harus bebas dan tidak berkonflik dengan panel atau Xray. |
| URI path | `subPath` | `/sub/` | Path tempat langganan biasa dikirimkan. Petunjuk: «Harus diawali dengan '/' dan diakhiri dengan '/'». |
| Domain yang didengarkan | `subDomain` | kosong | Domain yang diizinkan mengakses langganan (validasi Host). Petunjuk: «Biarkan kosong secara default untuk mendengarkan semua domain dan alamat IP». Jika diisi — permintaan dengan Host yang berbeda akan ditolak. |

**Catatan keamanan penting:** path default `/sub/` (dan `/json/` untuk JSON) sudah umum diketahui dan mudah ditebak. Panel menampilkan peringatan: «Path langganan default "/sub/" sudah dikenal luas — ubahnya.» dan peringatan serupa untuk JSON. Disarankan untuk menetapkan path kustom yang tidak mudah ditebak.

#### TLS / Sertifikat

| Field (UI) | Kunci | Default | Deskripsi |
|---|---|---|---|
| Path file kunci publik sertifikat langganan | `subCertFile` | kosong | Path lengkap ke file sertifikat (`.crt`/`fullchain`). Petunjuk: «Masukkan path lengkap yang diawali dengan '/'». |
| Path file kunci privat sertifikat langganan | `subKeyFile` | kosong | Path lengkap ke file kunci privat. Petunjuk: «Masukkan path lengkap yang diawali dengan '/'». |

Jika kedua path diisi dan sertifikat berhasil dimuat, server langganan berjalan melalui **HTTPS**. Jika field kosong atau sertifikat tidak dapat dibaca — server kembali ke **HTTP** (error dicatat di log). Adanya TLS yang valid juga memengaruhi pembentukan URL dasar: pada port 443 dengan TLS dan port 80 tanpa TLS, nomor port dihilangkan dari tautan.

#### Interval pembaruan

| Field (UI) | Kunci | Default | Deskripsi |
|---|---|---|---|
| Interval pembaruan langganan | `subUpdates` | `12` | Seberapa sering (dalam jam) aplikasi klien harus meminta ulang langganan. Petunjuk: «Interval antara pembaruan di aplikasi klien (dalam jam)». |

Nilai ini dikirimkan ke klien dalam header HTTP `Profile-Update-Interval`; klien modern menggunakannya sebagai periode pembaruan otomatis konfigurasi.

#### Format dan informasi dalam respons

| Field (UI) | Kunci | Default | Deskripsi |
|---|---|---|---|
| Enkripsi | `subEncrypt` | `true` | Petunjuk: «Enkripsi konfigurasi yang dikembalikan dalam langganan». Secara teknis ini bukan enkripsi, melainkan **encoding Base64** dari seluruh body langganan biasa (format yang diharapkan oleh sebagian besar klien). Jika dinonaktifkan, tautan dikirimkan dalam teks biasa, satu per baris. |
| Tampilkan informasi penggunaan | `subShowInfo` | `true` | Petunjuk: «Tampilkan sisa traffic dan tanggal kedaluwarsa setelah nama konfigurasi». Jika aktif, penanda sisa traffic (📊) dan masa berlaku (misalnya `5D,3H⏳`) ditambahkan ke nama (remark) setiap konfigurasi; untuk klien yang sudah kedaluwarsa/tidak tersedia ditampilkan `⛔️N/A`. |
| Sertakan Email dalam nama | `subEmailInRemark` | `true` | Petunjuk: «Sertakan email klien dalam nama profil langganan.». Menambahkan email klien ke remark profil. |

#### Template remark (Remark Template)

Nama tampilan (remark) setiap konfigurasi dalam langganan dibentuk berdasarkan **template remark** — field **«Template catatan»** (`remarkTemplate`) di tab **«Informasi»** pengaturan langganan. Pembuat model catatan sebelumnya (pemilihan bagian inbound/email/external proxy dan karakter pemisah secara terpisah) telah dihapus dari antarmuka; sekarang Anda menulis format nama bebas dan menyisipkan variabel ke dalamnya. Nilai default adalah `{{INBOUND}}|📊{{TRAFFIC_LEFT}}|⏳{{DAYS_LEFT}}D`. Jika field dikosongkan, model remark lama (yang tidak dapat dikonfigurasi melalui antarmuka) digunakan sebagai cadangan.

Variabel dikelompokkan ke dalam bagian **Client**, **Traffic**, dan **Time & status** dan ditampilkan di sebelah field sebagai chip yang dapat diklik `{{VAR}}` dengan tooltip saat kursor diarahkan; klik menyisipkan token ke dalam template, tersedia pratinjau langsung. Setiap variabel disubstitusi secara individual untuk klien tertentu pada saat pembuatan langganan. Penulisan sederhana dengan tanda kurung tunggal juga didukung (`{DATA_LEFT}`, `{EXPIRE_DATE}`, `{PROTOCOL}`, `{TRANSPORT}`, dll.) — panel secara otomatis mengubahnya ke format internal `{{...}}`.

Variabel yang tersedia:

- **Identifikasi klien:** `{{EMAIL}}`, `{{INBOUND}}` (remark inbound itu sendiri), `{{HOST}}` (remark host), `{{ID}}` (UUID), `{{SHORT_ID}}` (8 karakter pertama UUID), `{{SUB_ID}}`, `{{COMMENT}}`, `{{TELEGRAM_ID}}`, `{{PROTOCOL}}`, `{{TRANSPORT}}`.
- **Traffic:** `{{TRAFFIC_USED}}`, `{{TRAFFIC_LEFT}}`, `{{TRAFFIC_TOTAL}}` (beserta varian `*_BYTES`-nya dalam byte yang tepat), `{{UP}}`, `{{DOWN}}`, `{{USAGE_PERCENTAGE}}`.
- **Masa berlaku dan status:** `{{DAYS_LEFT}}`, `{{TIME_LEFT}}`, `{{EXPIRE_DATE}}` (`YYYY-MM-DD`), `{{JALALI_EXPIRE_DATE}}` (tanggal dalam kalender Jalali), `{{EXPIRE_UNIX}}`, `{{CREATED_UNIX}}`, `{{RESET_DAYS}}`, `{{STATUS}}` (active / expired / disabled / depleted), `{{STATUS_EMOJI}}`.

Template dapat dibagi menjadi segmen menggunakan karakter pemisah vertikal `|`. Segmen yang variabelnya menghasilkan nilai «tidak terbatas» (`∞`) — misalnya `{{TRAFFIC_LEFT}}` atau `{{DAYS_LEFT}}` pada klien tanpa batas — secara otomatis disembunyikan. Selain itu, blok penggunaan traffic dan masa berlaku ditampilkan satu kali, pada tautan pertama klien, agar tidak duplikat di setiap konfigurasi.

**Contoh.** Template `{{EMAIL}}|📊{{TRAFFIC_LEFT}}|⏳{{DAYS_LEFT}}D` akan menghasilkan nama seperti `ivan@vpn 📊42.00GB ⏳7D` untuk klien dengan sisa 42 GB dan 7 hari, sementara untuk klien tanpa batas hanya `ivan@vpn` (segmen dengan `∞` dihilangkan).
| Template remark | `remarkTemplate` | `{{INBOUND}}|📊{{TRAFFIC_LEFT}}|⏳{{DAYS_LEFT}}D` | Template bebas untuk nama tampilan (remark) setiap konfigurasi dengan substitusi variabel `{{VAR}}`. Disubstitusi secara individual untuk setiap klien saat pembuatan langganan. Pembuat «model catatan» sebelumnya (pemilihan inbound/email/external proxy dan pemisah) telah dihapus dari antarmuka dan hanya digunakan sebagai cadangan jika field dikosongkan. Selengkapnya — lihat «Template remark (Remark Template)» di bawah. |

#### Metadata profil (header respons)

String-string ini dikirimkan ke klien dalam header HTTP respons dan ditampilkan di aplikasi VPN sebagai metadata profil. Semuanya kosong secara default.

| Field (UI) | Kunci | Header | Deskripsi |
|---|---|---|---|
| Judul langganan | `subTitle` | `Profile-Title` (dalam Base64) | «Nama langganan yang dilihat klien di aplikasi VPN». Untuk Clash juga digunakan sebagai nama profil yang diimpor melalui `Content-Disposition`. |
| URL dukungan | `subSupportUrl` | `Support-Url` | «Tautan ke dukungan teknis yang ditampilkan di aplikasi VPN». |
| URL profil | `subProfileUrl` | `Profile-Web-Page-Url` | «Tautan ke situs Anda yang ditampilkan di aplikasi VPN». Jika tidak diisi, URL permintaan langganan yang sebenarnya digunakan sebagai penggantinya. |
| Pengumuman | `subAnnounce` | `Announce` (dalam Base64) | «Teks pengumuman yang ditampilkan di aplikasi VPN». |

Selain itu, setiap respons menyertakan header `Subscription-Userinfo` dengan data traffic agregat klien: `upload`, `download`, `total`, dan `expire` (waktu kedaluwarsa dalam detik). Berdasarkan header ini klien menampilkan sisa traffic dan masa berlaku.

#### Routing (hanya untuk klien Happ)

| Field (UI) | Kunci | Default | Deskripsi |
|---|---|---|---|
| Aktifkan routing | `subEnableRouting` | `false` | «Pengaturan global untuk mengaktifkan routing di aplikasi VPN klien. (Hanya untuk Happ)». Dikirimkan dalam header `Routing-Enable`. |
| Aturan routing | `subRoutingRules` | kosong | «Aturan routing global untuk aplikasi VPN klien. (Hanya untuk Happ)». Dikirimkan dalam header `Routing`. |

| Sembunyikan pengaturan server | `subHideSettings` | `false` | «Sembunyikan pengaturan server dalam langganan (hanya untuk Happ)». Jika diaktifkan, klien Happ menyembunyikan kemampuan untuk melihat dan mengubah parameter server. Opsi ini hanya berlaku untuk klien Happ. |

#### URI reverse proxy

| Field (UI) | Kunci | Default | Deskripsi |
|---|---|---|---|
| URI reverse proxy | `subURI` | kosong | «Ubah URI dasar URL alamat langganan untuk digunakan di balik proxy server». |

Jika field kosong, alamat dasar tautan dibangun secara otomatis oleh panel dari domain dan port langganan (dengan mempertimbangkan TLS). Namun jika langganan didistribusikan melalui reverse proxy/CDN eksternal pada domain atau path yang berbeda, URI dasar akhir dimasukkan ke dalam field ini, dan semua tautan akan dibangun berdasarkannya. Field terpisah serupa juga tersedia untuk JSON (`subJsonURI`) dan Clash (`subClashURI`).

Jika hanya `subURI` umum yang diisi sedangkan field terpisah untuk JSON dan Clash dikosongkan, tautan format tersebut di halaman langganan mewarisi skema dan host dari `subURI` (bukan port sub-server dan `http`) — sehingga tautan tersebut sesuai dengan alamat reverse proxy.

**Contoh: langganan di balik reverse proxy.** Langganan sendiri mendengarkan pada `2096`, tetapi dari luar dapat diakses melalui nginx/CDN pada `https://cfg.example.com/u/`. Agar tautan dalam respons dibangun dari alamat eksternal, bukan dari `domain:2096` internal, URI dasar akhir dimasukkan ke field «Reverse proxy URI»:

```
Reverse proxy URI: https://cfg.example.com/u
```

Maka tautan akhir akan berbentuk `https://cfg.example.com/u/ivan2025`. Untuk format JSON dan Clash, field terpisah `subJsonURI` dan `subClashURI` diisi dengan cara yang sama jika diperlukan.

### 10.3. Format output

Langganan dapat dikirimkan dalam tiga format independen, masing-masing dengan endpoint-nya sendiri yang dapat diaktifkan/dinonaktifkan secara terpisah.

#### Alamat server dan node dalam output

Alamat server dalam tautan langganan disubstitusi menggunakan strategi alamat tautan yang sama seperti tautan biasa dan QR code di panel: «listen» — alamat binding yang dapat dirutekan, «custom» — alamat kustom yang ditentukan pengguna (`shareAddr`), «node» (default) — alamat node. Untuk inbound tanpa strategi yang ditetapkan secara eksplisit, output langganan tidak berubah. Hal ini memungkinkan inbound node yang terikat ke IP publik tertentu untuk mengirimkan alamat yang dapat dicapai kepada klien. Strategi ini berlaku untuk format mentah, JSON, dan Clash.

Nama node (Node) tidak ditambahkan ke nama (remark) profil dalam langganan: di aplikasi klien hanya remark inbound yang ditetapkan administrator yang ditampilkan, tanpa sufiks internal seperti `@nama-node`. Untuk membedakan entri dengan nama yang sama dalam langganan multi-node, tetapkan remark yang berbeda secara manual atau gunakan Hosts terkelola dengan Remark mereka sendiri.

Jika karena ketidaksinkronan antar-node klien yang sama masuk ke inbound JSON layanan dua kali, output langganan secara otomatis menghilangkan duplikat tersebut berdasarkan email di semua tiga format, sehingga profil yang duplikat tidak muncul dalam output.

#### Host terkelola (Hosts)

Bagian **Hosts** (item menu samping; halaman ringkasan dengan jumlah Total/Enabled/Disabled dan daftar) menetapkan penggantian alamat untuk tautan langganan. Untuk setiap inbound, Anda dapat menambahkan satu atau beberapa **host** — endpoint yang disubstitusi ke dalam tautan langganan yang dikirimkan kepada klien **menggantikan alamat, port, dan parameter TLS inbound itu sendiri**. Fitur ini berguna untuk mendistribusikan traffic melalui CDN atau relay tanpa mengubah inbound itu sendiri.

Setiap host memiliki:

- **Remark** dan deskripsi (Description), keterkaitan dengan **Inbound** tertentu, sakelar **Enable**, dan penugasan ke node (**Nodes**).
- **Address** (kosong — mewarisi alamat inbound) dan **Port** (`0` — mewarisi port inbound); **Tags** (hanya diperhitungkan dalam langganan RAW).
- Tab **Security** — `same` / `tls` / `none` / `reality` dengan SNI, fingerprint, ALPN, pinned-cert, `allowInsecure`, dan ECH.
- Tab **Advanced** — Host header, Path, rute VLESS, Mux, Sockopt, Final Mask, dan pengecualian host dari format langganan tertentu (raw / json / clash).
- Tab **Clash (mihomo)** — versi IP, Mihomo X25519, pengacakan host (Shuffle host).

Host diurutkan dalam inbound masing-masing dan mendukung aktivasi, penonaktifan, serta penghapusan massal. Host terkelola menggantikan array External Proxy yang sebelumnya.

#### Tautan biasa (SUB) — Base64 / teks biasa

Format dasar, endpoint `subPath` (default `/sub/`). Selalu aktif (ketika langganan secara keseluruhan diaktifkan). Mengembalikan daftar tautan Xray (`vless://`, `vmess://`, `trojan://`, `ss://`, dll.) — satu per baris. Jika opsi «Enkripsi» (`subEncrypt`) aktif, seluruh daftar dikodekan dalam Base64; jika tidak aktif — dikirimkan dalam teks biasa. Format ini didukung oleh hampir semua klien (v2rayNG, V2RayTun, Sing-box, NekoBox, Streisand, Shadowrocket, Happ, dll.).

**Contoh: body respons dengan «Enkripsi» dinonaktifkan.** Dengan `subEncrypt = false` endpoint `/sub/` mengirimkan teks biasa — satu tautan per baris:

```
vless://3c8f...@a.example.com:443?security=reality&...#srvA-ivan
trojan://p4ss@b.example.com:443?security=tls&...#srvB-ivan
```

Dengan `subEncrypt = true` (default) daftar yang sama seluruhnya dikodekan dalam Base64 dan dikirimkan sebagai satu baris — inilah format yang diharapkan oleh sebagian besar klien.

#### Langganan JSON (sing-box dan yang kompatibel)

Endpoint `subJsonPath` (default `/json/`), diaktifkan dengan centang terpisah.

| Field (UI) | Kunci | Default | Deskripsi |
|---|---|---|---|
| Langganan JSON | `subJsonEnable` | `false` | «Aktifkan/nonaktifkan endpoint JSON langganan secara independen.». |

Mengembalikan konfigurasi JSON lengkap (format yang dipahami oleh sing-box dan klien turunannya — Podkop, OpenWRT sing-box, Karing, NekoBox). Untuk format ini tersedia parameter tambahan (tab `subFormats`):

- **Mux** (`subJsonMux`, default kosong) — pengaturan JSON multiplexing (Mux) yang disematkan ke dalam outbound setiap stream langganan JSON. «Transmisi beberapa stream data independen dalam satu koneksi.».
- **Final Mask** (`subJsonFinalMask`, default kosong) — «Mask finalmask xray (TCP/UDP) dan pengaturan QUIC yang ditambahkan ke setiap stream langganan JSON. Memerlukan versi xray terbaru di sisi klien.». Dikonfigurasi melalui sub-field: «Paket» (`packets`), «Panjang» (`length`), «Interval» (`interval`), «Maks. pemisahan» (`maxSplit`), «Noise» (`noises`: «Tipe»/`type`, «Paket»/`packet`, «Penundaan (ms)»/`delayMs`, «Terapkan ke»/`applyTo`, tombol «+ Noise»), serta «Konkurensi» (`concurrency`), «Konkurensi xudp» (`xudpConcurrency`), dan «xudp UDP 443» (`xudpUdp443`).
- **Aturan routing** (`subJsonRules`, default kosong) — aturan global yang ditambahkan ke konfigurasi JSON.

#### Langganan Clash / Mihomo (YAML)

Endpoint `subClashPath` (default `/clash/`), diaktifkan dengan centang terpisah.

| Field (UI) | Kunci | Default | Deskripsi |
|---|---|---|---|
| Langganan Clash / Mihomo | `subClashEnable` | `false` | Mengaktifkan pembuatan konfigurasi YAML untuk klien Clash dan Mihomo. |
| Aktifkan routing | `subClashEnableRouting` | `false` | «Tambahkan aturan routing global Clash/Mihomo ke langganan YAML yang dihasilkan.». |
| Aturan routing global | `subClashRules` | kosong | «Aturan Clash/Mihomo yang ditambahkan di awal setiap langganan YAML sebelum MATCH,PROXY.». |

Respons dikirimkan dengan tipe `application/yaml; charset=utf-8`. Jika «Judul langganan» (`subTitle`) diisi, judul tersebut juga dikirimkan dalam header `Content-Disposition` (`attachment; filename*=UTF-8''<title>`), agar klien Clash memberi nama profil yang diimpor sesuai judul tersebut.

Format tautan dan YAML yang dihasilkan selalu diperbarui untuk klien modern: Shadowsocks-2022 (SS2022) tidak lagi mengkodekan userinfo dalam Base64; tautan Shadowsocks dengan obfuskasi http dikirimkan dalam format SIP002 dengan plugin `obfs-local`; untuk langganan Clash/Mihomo diterapkan set field XHTTP yang lengkap. Hal ini tidak memerlukan pengaturan terpisah — tautan hanya dikenali lebih tepat oleh klien.

> Catatan: dalam build ini didukung tepat tiga format — tautan biasa (Base64/teks), JSON (kompatibel dengan sing-box), dan Clash/Mihomo (YAML). Format Outline terpisah tidak tersedia di server langganan.

### 10.4. Halaman informasi langganan dan QR code

Jika Anda membuka tautan langganan di browser (atau secara eksplisit menambahkan parameter `?html=1` atau `?view=html` ke URL, atau mengirimkan header `Accept: text/html`), server alih-alih mengirimkan respons «mentah» akan menampilkan **halaman informasi langganan** visual («Informasi Langganan»). Klien VPN tetap mendapatkan respons mesin, karena mereka tidak meminta HTML.

Halaman (aplikasi satu halaman yang dibangun dengan Vite) menampilkan:

- **Informasi langganan** (blok Descriptions):
  - «ID Langganan» — nilai `subId`;
  - «Status» — «Aktif», «Tidak Aktif», atau «Tidak Terbatas». Status «tidak aktif» ditetapkan jika klien dinonaktifkan, telah menghabiskan batas traffic, atau masa berlakunya telah kedaluwarsa;
  - «Diunduh» dan «Dikirim» — volume traffic;
  - «Batas total» — batas traffic atau `∞` jika tidak dibatasi;
  - «Masa berlaku» — tanggal kedaluwarsa atau «Tanpa batas»;
  - sisa traffic dan waktu online terakhir.
  - Tanggal ditampilkan dalam kalender Gregorian atau Jalali tergantung pengaturan «Calendar Type» panel (`datepicker`, default `gregorian`).
- **Tautan langganan**: untuk setiap format yang diaktifkan — baris terpisah dengan tag berwarna (hijau **SUB**, ungu **JSON**, emas **CLASH**), tombol salin, dan tombol **QR code** (jendela popup, ukuran 240 px). Baris JSON dan CLASH hanya muncul jika format yang bersangkutan diaktifkan dalam pengaturan.
- **Tautan individual** («Salin tautan»): daftar lengkap konfigurasi individual yang termasuk dalam langganan, masing-masing dengan tag protokol, tombol salin, dan QR code (untuk tautan post-quantum, QR code tidak dibuat).

- **Tombol «Salin semua konfigurasi»** (di atas daftar tautan individual): dengan satu klik menyalin semua tautan konfigurasi ke clipboard (masing-masing di baris baru), tanpa perlu menyalinnya satu per satu; setelah selesai muncul notifikasi «Semua konfigurasi disalin».
- **Tombol impor cepat ke aplikasi** (menu dropdown per platform): untuk Android — v2box, v2rayNG (deep-link `v2rayng://install-config?url=…`), Sing-box, V2RayTun, NPV Tunnel, Happ (`happ://add/…`); untuk iOS — Shadowrocket (melalui parameter `flag=shadowrocket`), v2box (`v2box://install-sub?url=…&name=…`), Streisand (`streisand://import/…`), V2RayTun, NPV Tunnel, Happ. Tombol-tombol ini membuka deep-link aplikasi yang diperlukan dengan alamat langganan yang sudah dimasukkan, atau menyalin tautan ke clipboard.

Halaman informasi dikirimkan dengan header larangan cache (`Cache-Control: no-cache`), sehingga klien selalu melihat data traffic dan masa berlaku terkini.

### 10.5. Template kustom halaman langganan

Mulai versi 3.3.0, Anda dapat mengganti halaman landing langganan standar dengan template HTML kustom. Secara default, halaman bawaan ditampilkan pada alamat langganan, tetapi jika direktori dengan template kustom ditentukan, panel akan merendernya dan mengisi data klien terkini ke dalamnya (traffic, masa berlaku, tautan, dll.).

Penting: panel **tidak menyertakan** template siap pakai. Repositori hanya berisi direktori `sub_templates/` dengan file instruksi `sub_templates/README.md`; tema Anda sendiri harus dibuat dari awal.

#### Di mana diaktifkan

Direktori tema ditentukan dalam pengaturan panel:

**Pengaturan → Langganan → bagian «Informasi Langganan»**, field **«Direktori tema langganan»** (`subThemeDir`).

Deskripsi field di antarmuka:
«Path absolut ke folder dengan template kustom (index.html/sub.html) untuk halaman langganan (misalnya, /etc/3x-ui/sub_templates/my-theme/). Biarkan kosong untuk menggunakan halaman default.»

Di bagian yang sama terdapat pengaturan terkait yang nilainya tersedia dalam template:

Di deskripsi field «Direktori tema langganan» terdapat tautan **«Panduan Template ↗»** ke dokumentasi pembuatan template tampilan halaman langganan kustom.
- **«Judul langganan»** (`subTitle`) — nama yang terlihat oleh klien;
- **«URL dukungan»** (`subSupportUrl`) — tautan ke dukungan teknis.

#### Parameter pengaturan

| Parameter | Nilai default | Tujuan |
|---|---|---|
| `subThemeDir` | `""` (kosong) | Path absolut ke direktori dengan template HTML Anda. Kosong = halaman bawaan default. |

#### Cara menerapkan template kustom

1. Buat folder untuk tema di server (di mana saja), misalnya `/etc/3x-ui/sub_templates/my-theme/`.
2. Letakkan file HTML dengan nama `index.html` atau `sub.html` di dalamnya.

**Contoh: path ke tema.** Tata letak akhir di server dan nilai field dalam pengaturan:

```
/etc/3x-ui/sub_templates/my-theme/
└── index.html        (atau sub.html — ia memiliki prioritas)
```

```
Pengaturan → Langganan → «Direktori tema langganan»:
/etc/3x-ui/sub_templates/my-theme/
```

Path harus berupa **path absolut** (diawali dengan `/`). Jika di dalam folder tidak ada `index.html` maupun `sub.html`, panel akan menampilkan halaman bawaan.
3. Di panel, buka **Pengaturan → Langganan** dan masukkan path **absolut** ke folder tersebut di field «Direktori tema langganan».
4. Simpan pengaturan.

Perilaku pemilihan file dan rendering:
- Jika direktori berisi `sub.html`, file tersebut yang digunakan; jika tidak ada, `index.html` yang diambil. Artinya `sub.html` memiliki prioritas atas `index.html`.
- Template dirender menggunakan engine Go standar `html/template`.
- Template yang sudah diurai **di-cache** dan hanya dibaca ulang dari disk ketika waktu modifikasi file berubah. Oleh karena itu perubahan pada template diterapkan tanpa perlu me-restart panel, namun tanpa overhead baca/parse pada setiap permintaan.
- Respons dibentuk sepenuhnya dalam buffer dan baru dikirimkan ke klien setelahnya: jika template gagal saat eksekusi, halaman yang sebagian dibuat (rusak) tidak akan dikirimkan ke pengguna.

#### Perilaku default dan fallback

- Field kosong → halaman SPA bawaan ditampilkan (data disematkan ke dalam `window.__SUB_PAGE_DATA__`).
- Path tidak ada atau bukan direktori → halaman default yang digunakan.
- Direktori tidak memiliki `index.html` maupun `sub.html` → peringatan «subThemeDir set but no usable template found» dicatat di log, halaman default ditampilkan.
- File template ada tetapi gagal diurai → error «custom template parse failed» dicatat di log, halaman default ditampilkan.
- Error saat eksekusi template → «custom template execution failed» dicatat di log, halaman default ditampilkan.

Artinya, setiap masalah dengan template kustom tidak «merusak» langganan — panel selalu kembali ke halaman bawaan. Semua halaman langganan (baik kustom maupun standar) dikirimkan dengan header larangan cache (`Cache-Control: no-cache, no-store, must-revalidate`), sehingga klien selalu mendapatkan data traffic dan masa berlaku terbaru.

#### Variabel template yang tersedia

Sekumpulan data klien langganan diteruskan ke konteks template. Pengaksesan melalui `{{ .nama }}`:

| Variabel | Tipe | Deskripsi |
|---|---|---|
| `{{ .sId }}` | string | ID langganan (UUID). |
| `{{ .enabled }}` | bool | Apakah klien/langganan aktif. |
| `{{ .download }}` | string | Volume unduhan yang diformat (misalnya «2.5 GB»). |
| `{{ .upload }}` | string | Volume pengiriman yang diformat. |
| `{{ .total }}` | string | Batas traffic total yang diformat. |
| `{{ .used }}` | string | Traffic yang telah digunakan dan diformat (download + upload). |
| `{{ .remained }}` | string | Sisa traffic yang diformat. |
| `{{ .expire }}` | int64 | Masa berlaku — Unix time dalam **detik** (`0` = tanpa batas). Untuk `Date` JavaScript kalikan dengan 1000. |
| `{{ .lastOnline }}` | int64 | Waktu online terakhir — Unix time dalam **milidetik** (`0` = belum pernah). |
| `{{ .downloadByte }}` | int64 | Unduhan dalam byte yang tepat. |
| `{{ .uploadByte }}` | int64 | Pengiriman dalam byte yang tepat. |
| `{{ .totalByte }}` | int64 | Batas total dalam byte yang tepat. |
| `{{ .subUrl }}` | string | URL halaman langganan. |
| `{{ .subJsonUrl }}` | string | URL konfigurasi JSON langganan. |
| `{{ .subClashUrl }}` | string | URL konfigurasi Clash/Mihomo. |
| `{{ .subTitle }}` | string | Judul langganan dari pengaturan (bisa kosong). |
| `{{ .subSupportUrl }}` | string | URL dukungan dari pengaturan (bisa kosong). |
| `{{ .links }}` | []string | Daftar string konfigurasi (VMess, VLESS, dll.). Iterasi: `{{ range .links }} … {{ end }}`. |
| `{{ .emails }}` | []string | Daftar email yang terkait dengan langganan. |
| `{{ .datepicker }}` | string | Format kalender panel saat ini: `gregorian` atau `jalali` (diambil dari pengaturan «Tipe Kalender»; jika kosong — `gregorian`). |

Contoh minimal body template yang menggunakan sebagian variabel:

```html
<h1>{{ .subTitle }}</h1>
<p>Digunakan: {{ .used }} dari {{ .total }} (sisa {{ .remained }})</p>
{{ range .links }}<div>{{ . }}</div>{{ end }}

**Contoh: tanggal kedaluwarsa dari `expire`.** Field `{{ .expire }}` adalah Unix time dalam **detik**, sehingga untuk JavaScript dikali 1000; nilai `0` berarti «tanpa batas»:

```html
<script>
  var exp = {{ .expire }};
  document.write(exp === 0
    ? 'Tanpa batas'
    : 'Hingga ' + new Date(exp * 1000).toLocaleDateString());
</script>
```

Perhatikan: `{{ .lastOnline }}` sudah dalam **milidetik** — tidak perlu dikali 1000.
```

---

## 11. Xray: routing, outbounds, DNS, dan ekstensi

Bagian **«Pengaturan Xray»** adalah editor template konfigurasi Xray-core yang menjadi dasar panel dalam menghasilkan `config.json` akhir untuk menjalankan inti. Keterangan untuk bagian template: *«Berdasarkan template ini, file konfigurasi Xray dibuat.»* Berbeda dengan inbounds (yang disimpan terpisah di database dan disisipkan ke template saat konfigurasi dirakit), semua yang lain — log, routing, outbounds, DNS, policy, statistik — ditentukan di sini.

> Penting: nilai template disimpan di database dengan kunci `xrayTemplateConfig`. Saat disimpan, panel menjalankannya melalui serangkaian transformasi otomatis (lihat [11.10](#1110-penyimpanan-restart-dan-transformasi-otomatis)). JSON yang secara sintaksis tidak valid akan ditolak dengan pesan kesalahan *«xray template config invalid»*.

#### Lokasi di menu: «Outbound» dan «Routing»

**«Outbound» (Outbounds)** dan **«Routing» (Routing)** adalah item menu samping yang terpisah (tepat di bawah «Hosts», di atas «Pengaturan Panel»), masing-masing memiliki alamat sendiri: `/outbound` dan `/routing`. Tautan langsung ke halaman-halaman ini dan pemuatan ulang halaman bekerja seperti yang diharapkan. Submenu **«Konfigurasi Xray»** hanya berisi: Dasar, Balancer, DNS, dan Template Lanjutan. Dalam deskripsi di bawah, bagian [11.3](#113-aturan-routing-routing) dan [11.4](#114-outbounds-koneksi-keluar) bersesuaian dengan halaman «Routing» dan «Outbound».

### 11.1. Struktur editor: tab/mode

Editor menawarkan beberapa mode tampilan template (filter berdasarkan bagian JSON):

| Mode | Apa yang ditampilkan |
|---|---|
| **Dasar** | Bagian dasar (Log, routing dasar, pengaturan utama) |
| **Template Lanjutan** | Template JSON Xray lengkap |
| **Semua** | Semua bagian sekaligus |

Kelompok logis pengaturan di dalam editor:

- **Pengaturan Utama** (keterangan: *«Parameter ini menjelaskan pengaturan umum»*).
- **Log** (lihat [11.9](#119-log-dan-statistik-stats-metrics)).
- **Koneksi Dasar**: pemblokiran dan rute langsung.
- **Inbound** (keterangan: *«Mengubah template konfigurasi untuk menghubungkan klien tertentu»*).
- **Outbound** (lihat [11.4](#114-outbounds-koneksi-keluar)).
- **Balancer** (lihat [11.5](#115-balancer-balancers)).
- **Routing** (keterangan: *«Prioritas setiap aturan sangat penting!»*, lihat [11.3](#113-aturan-routing-routing)).
- **DNS / Fake DNS** (lihat [11.6](#116-dns)).

### 11.2. Pengaturan Utama (General)

#### Freedom Protocol Strategy

| Kolom | Label | Deskripsi | Default |
|---|---|---|---|
| `FreedomStrategy` | **Pengaturan Strategi Protokol Freedom** | Strategi output jaringan untuk outbound langsung (freedom). Keterangan: *«Mengatur strategi output jaringan dalam protokol Freedom»*. Mengontrol kolom `domainStrategy` di dalam `settings` dari outbound dengan protokol `freedom`. | Pada template referensi, `domainStrategy` untuk freedom-outbound `direct` adalah **`AsIs`** (alamat tidak di-resolve, diteruskan dalam bentuk aslinya). |

`domainStrategy` untuk freedom (nilai Xray-core): `AsIs` (tidak me-resolve domain di sisi server), serta keluarga `UseIP` / `UseIPv4` / `UseIPv6` dan varian «paksa» mereka `ForceIP*`, yang memaksa server keluar me-resolve domain dan terhubung melalui IP yang diperoleh. Ubah ke `UseIPv4` jika server keluar tidak memiliki IPv6 atau perlu paksa hanya menggunakan IPv4.

#### Freedom Happy Eyeballs (IPv4/IPv6)

| Kolom | Label | Deskripsi |
|---|---|---|
| `FreedomHappyEyeballs` | **Freedom Happy Eyeballs (IPv4/IPv6)** | Keterangan: *«Dual-stack dial untuk outbound langsung (freedom) — berguna di server keluar dengan IPv4 dan IPv6.»* Mengaktifkan algoritma Happy Eyeballs (percobaan simultan pada kedua keluarga alamat) untuk freedom-outbound. |
| try delay | (keterangan) | *«Milidetik sebelum mencoba keluarga alamat lain. 150–250 ms adalah titik awal yang baik.»* Penundaan sebelum beralih ke keluarga alamat alternatif. Rentang yang disarankan — 150–250 ms. |

#### Overall Routing Strategy

| Kolom | Label | Deskripsi | Default |
|---|---|---|---|
| `RoutingStrategy` | **Pengaturan Routing Domain** | Strategi resolusi DNS keseluruhan untuk routing. Keterangan: *«Mengatur strategi routing resolusi DNS secara keseluruhan»*. Mengontrol kolom `routing.domainStrategy`. | Pada template referensi, `routing.domainStrategy` = **`AsIs`**. |

`routing.domainStrategy` menentukan bagaimana aturan routing IP dicocokkan dengan permintaan domain: `AsIs` (hanya aturan domain, tanpa resolve), `IPIfNonMatch` (jika domain tidak cocok dengan aturan — resolve dan periksa aturan IP), `IPOnDemand` (resolve segera saat menemukan aturan IP). Agar aturan IP (misalnya, `geoip:*`) berfungsi untuk permintaan domain, biasanya dibutuhkan `IPIfNonMatch`.

#### Outbound Test URL

| Kolom | Label | Deskripsi | Default |
|---|---|---|---|
| `outboundTestUrl` | **URL untuk Pengujian Outbound** | URL untuk memeriksa konektivitas saat menguji outbound. Keterangan: *«URL untuk memeriksa koneksi outbound»*. Disimpan terpisah dari template, dengan kunci `xrayOutboundTestUrl`. | **`https://www.google.com/generate_204`** |

Nilai melewati sanitasi. Saat pengujian outbound yang sebenarnya, nilai ini juga diverifikasi sebagai URL publik — ini adalah perlindungan dari SSRF: pengguna tidak dapat menyisipkan URL sembarang (termasuk internal) melalui klien, URL pengujian selalu diambil dari pengaturan server. Nilai kosong saat disimpan/diuji digantikan dengan `generate_204` default.

#### Block BitTorrent

| Kolom | Label | Deskripsi |
|---|---|---|
| `Torrent` | **Blokir BitTorrent** | Menambahkan aturan ke `routing.rules` yang mengirim lalu lintas dengan `protocol: ["bittorrent"]` ke outbound `blocked`. Pada template referensi, aturan ini hadir secara default. |

#### Batas Koneksi (Connection Limits)

Keterangan: *«Kebijakan tingkat koneksi untuk pengguna tingkat 0. Biarkan kolom kosong untuk menggunakan nilai default Xray.»* Parameter ini ditulis ke `policy.levels.0`.

| Kolom | Label | Deskripsi | Default |
|---|---|---|---|
| `connIdle` | **Timeout Idle** (detik) | *«Menutup koneksi setelah idle selama jumlah detik yang ditentukan. Mengurangi nilai ini akan membebaskan memori dan file descriptor lebih cepat di server dengan beban tinggi (default Xray: 300).»* | kosong → default Xray **300** |
| `bufferSize` | **Ukuran Buffer** (KB) | *«Ukuran buffer internal per koneksi dalam KB. Tetapkan 0 untuk meminimalkan penggunaan memori di server dengan RAM kecil (nilai default Xray bergantung pada platform).»* Placeholder: **«auto»**. | kosong → bergantung pada platform; `0` — minimalisasi |

**Contoh (`policy.levels.0`).** Kolom dari grup ini ditulis ke policy tingkat 0. Pada server dengan beban tinggi dan RAM kecil, Anda dapat mempercepat pembebasan sumber daya seperti ini:

```json
"policy": {
  "levels": {
    "0": {
      "connIdle": 120,
      "bufferSize": 0
    }
  }
}
```

Di sini koneksi ditutup setelah 120 detik idle (bukan default 300), dan `bufferSize: 0` meminimalkan konsumsi memori untuk buffer. Kolom yang dibiarkan kosong di form tidak akan masuk ke JSON — dan Xray akan menerapkan nilai defaultnya sendiri.

### 11.3. Aturan Routing (routing)

Daftar aturan `routing.rules`. **Urutan sangat kritis** (*«Prioritas setiap aturan sangat penting!»*): aturan dievaluasi dari atas ke bawah, yang pertama cocok akan dieksekusi. Keterangan: *«Seret untuk mengubah urutan»*. Tombol kontrol urutan: **Pertama**, **Terakhir**, **Naik**, **Turun**.

Setiap aturan memiliki `type: "field"`. Tombol: **Buat Aturan**, **Edit Aturan**. Keterangan untuk kolom daftar: *«Elemen dipisahkan dengan koma»*.

Pada halaman «Routing», tombol **«Impor Aturan»** dan **«Ekspor Aturan»** dikumpulkan dalam menu dropdown **«lainnya»** (more) — seperti halnya pada halaman «Outbound». Tombol **«Ekspor Aturan»** tidak langsung mengunduh file, melainkan membuka jendela modal dengan pratinjau JSON dan tombol **«Salin»** dan **«Unduh»**: konten dapat ditinjau sebelum disimpan. Ekspor outbound pada halaman «Outbound» bekerja dengan cara yang sama.

#### Route Tester (penguji rute)

Pada tab Routing terdapat sub-tab **Route Tester** — ia menanyakan kepada Xray yang sedang berjalan, outbound mana yang akan memproses koneksi tertentu, tanpa mengirimkan lalu lintas nyata. Masukkan domain atau IP, port, jaringan (TCP/UDP), dan jika perlu, inbound dan protokol yang terdeteksi (`http`/`tls`/`quic`/`bittorrent`), lalu tekan **Test Route**. Keputusan diambil langsung dari mesin routing yang berjalan.

Respons menampilkan outbound yang dipilih, dan saat menggunakan balancer — juga tag balancer. Jika tidak ada aturan yang cocok, penguji memberi tahu bahwa lalu lintas menuju outbound default (yang pertama dalam daftar `outbounds`). Ini berguna untuk memverifikasi urutan aturan sebelum mengandalkannya.

#### Mengaktifkan dan menonaktifkan aturan individual

Aturan routing individual dapat dinonaktifkan sementara dengan toggle, tanpa menghapusnya. Dalam tabel aturan terdapat kolom **«Aktifkan»** dengan toggle (Switch), dan dalam form aturan kolom **«Aktifkan»** — juga toggle. Aturan yang dinonaktifkan tidak masuk ke konfigurasi Xray akhir, tetapi disimpan dalam template dan dapat diaktifkan kembali kapan saja.

Aturan layanan statistik (`inboundTag: ["api"] → outboundTag: "api"`) tidak dapat dinonaktifkan — togglenya dikunci agar tidak merusak penghitungan lalu lintas panel (lihat [11.10](#1110-penyimpanan-restart-dan-transformasi-otomatis)).

#### Kolom form aturan

| Kolom form | Label | Kolom JSON | Deskripsi |
|---|---|---|---|
| Sumber | **Sumber** | `source` | Alamat IP/subnet sumber. Daftar dipisah koma. |
| Port Sumber | **Port Sumber** | `sourcePort` | Port sumber. |
| Tujuan | **Tujuan** | `domain` + `ip` + `port` | Domain, IP, dan port target. Domain mendukung prefiks `domain:`, `full:`, `regexp:`, `keyword:`, serta `geosite:*`; IP — `geoip:*` dan CIDR. |
| Jaringan | — | `network` | `tcp`, `udp`, atau `tcp,udp`. |
| Protokol | — | `protocol` | `http`, `tls`, `bittorrent` (ditentukan melalui sniffing). |
| Pengguna | **Pengguna** | `user` | Filter berdasarkan email/pengidentifikasi pengguna. |
| Atribut / Nilai | **Atribut** / **Nilai** | `attrs` | Atribut header HTTP untuk pencocokan. |
| VLESS route | **VLESS route** | — | Routing berdasarkan kolom route untuk VLESS. |
| Tag inbound | **Tag inbound** | `inboundTag` | Satu atau lebih tag inbound yang aturannya diterapkan (termasuk `api` bawaan, dan tag DNS dari pengaturan DNS). Dalam daftar inbound ditampilkan sebagai «tag (remark)» jika inbound memiliki catatan terpisah, jika tidak — hanya tag; dalam aturan yang disimpan hanya tag yang disimpan. |
| Tag outbound | **Tag outbound** / **Koneksi Keluar** | `outboundTag` | Ke mana mengarahkan lalu lintas yang cocok. |
| Tag balancer | **Tag balancer** / **Balancer** | `balancerTag` | Keterangan: *«Mengarahkan lalu lintas melalui salah satu balancer beban yang dikonfigurasi»*. |

> Saling eksklusif antara `outboundTag` dan `balancerTag`: *«Tidak mungkin menggunakan balancerTag dan outboundTag secara bersamaan. Jika digunakan bersamaan, hanya outboundTag yang akan berfungsi.»* Dalam satu aturan, tentukan tag outbound atau tag balancer — bukan keduanya.

#### Aturan bawaan template referensi

Dalam `config.json` standar, bagian `routing` berisi tiga aturan (dalam urutan ini):

1. `inboundTag: ["api"] → outboundTag: "api"` — aturan layanan untuk gRPC-API statistik panel.
2. `ip: ["geoip:private"] → outboundTag: "blocked"` — pemblokiran rentang privat.
3. `protocol: ["bittorrent"] → outboundTag: "blocked"` — pemblokiran BitTorrent.

> Aturan `api → api` selalu secara otomatis dinaikkan ke posisi 0 saat disimpan (lihat [11.10](#1110-penyimpanan-restart-dan-transformasi-otomatis)), agar permintaan statistik tidak «dimakan» oleh aturan catch-all yang ada di atasnya.

**Contoh aturan.** Mengirim semua lalu lintas ke situs Rusia dan jaringan privat secara langsung (melewati proxy), sementara sisanya — ke balancer. Urutan penting: aturan «arahkan langsung» harus berada di atas catch-all. Dalam `routing.rules`:

```json
{
  "type": "field",
  "domain": ["geosite:category-ru", "domain:example.ru"],
  "ip": ["geoip:ru", "geoip:private"],
  "outboundTag": "direct"
}
```

Agar aturan IP (`geoip:ru`) juga berfungsi untuk permintaan domain, biasanya diperlukan `routing.domainStrategy: "IPIfNonMatch"` di tingkat atas routing (lihat [11.2](#112-pengaturan-utama-general)).

#### Grup routing yang telah dikonfigurasi sebelumnya (Koneksi Dasar)

Dalam mode «Koneksi Dasar», panel membantu menyusun aturan umum dari daftar yang sudah tersedia:

| Grup | Kolom | Keterangan |
|---|---|---|
| Pemblokiran berdasarkan protokol/situs | — | *«Konfigurasikan agar klien tidak memiliki akses ke protokol tertentu»* |
| Pemblokiran berdasarkan negara | **IP yang Diblokir**, **Domain yang Diblokir** | *«Parameter ini akan memblokir lalu lintas berdasarkan negara tujuan.»* |
| Koneksi langsung | **IP Langsung**, **Domain Langsung** | *«Koneksi langsung berarti lalu lintas tertentu tidak akan diarahkan melalui server lain.»* |
| Aturan IPv4 | — | *«Parameter ini memungkinkan klien melakukan routing ke domain target hanya melalui IPv4»* |
| Aturan WARP | — | *«Opsi ini akan mengarahkan lalu lintas berdasarkan tujuan tertentu melalui WARP.»* |
| Routing NordVPN | — | *«Opsi ini akan mengarahkan lalu lintas berdasarkan tujuan tertentu melalui NordVPN.»* |

#### MTProto-inbound: routing lalu lintas Telegram melalui Xray

MTProto-inbound memiliki toggle **«Route through Xray»** (default nonaktif) dan pilihan **Outbound** opsional. Saat diaktifkan, panel menambahkan jembatan SOCKS loopback ke konfigurasi Xray dengan tag inbound itu sendiri, dan mtg mengarahkan lalu lintas Telegram melaluinya. Setelah itu, lalu lintas Telegram keluar dikendalikan oleh router: dapat dicocokkan dengan aturan biasa di tab Routing berdasarkan tag inbound atau diarahkan paksa ke outbound atau balancer yang dipilih melalui kolom **Outbound**. Biarkan **Outbound** kosong agar keputusan dibuat oleh aturan routing.

### 11.4. Outbounds (koneksi keluar)

Daftar `outbounds`. Tombol: **Buat Koneksi Keluar**, **Edit Koneksi Keluar**. Keterangan: *«Mengubah template konfigurasi untuk mendefinisikan koneksi keluar bagi server ini»*.

Pada template referensi terdapat dua outbound wajib:

- `protocol: "freedom"`, `tag: "direct"` — keluar langsung ke internet (dengan `domainStrategy: "AsIs"` dan `finalRules: [{action: "allow"}]`);
- `protocol: "blackhole"`, `tag: "blocked"` — «lubang hitam» untuk lalu lintas yang diblokir.

#### Kolom form outbound umum

| Kolom | Label | Deskripsi |
|---|---|---|
| Tag | **Tag** (keterangan: *«Tag unik»*) | Pengenal unik outbound. Placeholder: *«tag-unik»*. Validasi: *«Tag wajib diisi»*, *«Tag sudah digunakan oleh outbound lain»*. |
| Protokol | — | Tipe outbound (lihat di bawah). |
| Alamat / Port | **Alamat** / Port | Target koneksi. Alamat dan port wajib diisi. |
| Kirim Melalui | **Kirim Melalui** | Alamat IP lokal antarmuka keluar (`sendThrough`). Placeholder: *«IP lokal»*. |
| Dialer proxy (rantai) | — | Keterangan: *«Hubungkan outbound ini melalui outbound lain (berdasarkan tag) untuk membangun rantai proxy. Biarkan kosong untuk koneksi langsung.»* Placeholder: *«Pilih outbound untuk rantai»*. Diimplementasikan melalui `streamSettings.sockopt.dialerProxy`. |

#### Protokol outbound yang didukung

Protokol yang didukung oleh form:

- **`freedom`** — keluar langsung. Kolom `settings.domainStrategy`, `finalRules` (lihat di bawah), Happy Eyeballs. Tidak dapat diuji (*«Outbound has no testable endpoint»*).
- **`blackhole`** — membuang lalu lintas. Kolom **Tipe Respons**. Tidak dapat diuji.
- **`socks`**, **`http`** — daftar `settings.servers[]` dengan `address`/`port`; kolom **Kata Sandi Otorisasi**.
- **`vmess`** — `settings.vnext[]` (`address`/`port`).
- **`vless`** — `settings.address`/`settings.port`.
- **`trojan`**, **`shadowsocks`** — `settings.servers[]`.
- **`wireguard`** — `settings.peers[]` dengan `endpoint`, plus kunci (lihat [11.7](#117-wireguard--warp--nordvpn)).
- **`hysteria`** — `settings.address`/`settings.port` (transport UDP).

Untuk outbound tipe **loopback** tersedia blok **Sniffing** dengan parameter yang sama seperti pada inbound: aktifkan, **destOverride**, **Metadata Only**, **Route Only**, dan daftar **domain yang dikecualikan**.

Dalam mask **UDP** (FinalMask) untuk **Hysteria2** tersedia mode tambahan. Mask **Salamander** memiliki selektor **Mode** dengan nilai **Salamander** dan **Gecko**: mode Gecko menambahkan padding acak pada paket dengan kolom ukuran **Min**/**Max** (`packetSize`, rentang 1–2048, default 512–1200) — ini melindungi dari fingerprinting berdasarkan panjang paket. Mask **Realm** (UDP hole-punching) memiliki blok **TLS Config** opsional dengan kolom **Server Name** (SNI), **ALPN** (`h3`/`h2`/`http/1.1`), **Fingerprint** (uTLS), dan toggle **Allow Insecure**.

**Contoh: rantai melalui SOCKS upstream.** Outbound `upstream` terhubung ke proxy SOCKS5 eksternal, dan `chained` mengirimkan lalu lintasnya melaluinya (`dialerProxy`), membentuk rantai. Dalam `outbounds`:

```json
[
  {
    "tag": "upstream",
    "protocol": "socks",
    "settings": {
      "servers": [{ "address": "203.0.113.10", "port": 1080 }]
    }
  },
  {
    "tag": "chained",
    "protocol": "freedom",
    "streamSettings": {
      "sockopt": { "dialerProxy": "upstream" }
    }
  }
]
```

Sekarang aturan routing dengan `outboundTag: "chained"` akan mengeluarkan lalu lintas ke internet melalui `upstream`.

#### Impor outbound dari tautan share

Outbound dapat diimpor dari tautan share (`vless://`, `vmess://`, dll.). Saat impor, pengaturan multiplexer **xmux** (XHTTP) yang diteruskan dalam blok `extra=` tautan juga disimpan: setelah impor, nilainya dimasukkan ke dalam subform **XMUX** dari outbound yang dibuat.

#### Kolom Mux (multiplexing)

**Paralelisme Maks.**, **Koneksi Maks.**, **Penggunaan Ulang Maks.**, **Permintaan Maks.**, **Detik Penggunaan Ulang Maks.**, **Periode keep alive**. Parameter ini mengonfigurasi perilaku mux/XUDP dari outbound.

#### Sockopts (pengaturan socket)

Grup **Sockopts**: **Interval keep alive**, **Mark (fwmark)**, **Antarmuka**, **Hanya IPv6**, **Terima proxy protocol**, **Proxy protocol**, **TCP user timeout (ms)**, **TCP keep-alive idle (s)**. Di sini juga dikonfigurasi dialer-proxy rantai.

#### Freedom finalRules (mengganti pemblokiran IP privat)

Untuk freedom-outbound tersedia grup **Aturan Final**:

| Kolom | Label | Deskripsi |
|---|---|---|
| `overrideXrayPrivateIp` | **Ganti Blokir IP Privat Default Xray** | Menghapus larangan bawaan Xray untuk koneksi keluar ke IP privat. |
| `action` | **Tindakan** | `allow` (seperti pada template referensi: `finalRules: [{action: "allow"}]`), `redirect` (**Redirect**), atau lainnya. |
| `blockDelay` | **Penundaan Blokir (ms)** | Penundaan sebelum membuang koneksi. |
| `redirect` / `fragment` | **Redirect** / **Fragment** | Tindakan pengalihan dan fragmentasi lalu lintas. |

#### Mask fragment: Lengths dan Delays per fragmen

Dalam mask **fragment** (tipe fragment pada FinalMask, untuk TCP), kolom Length dan Delay tunggal digantikan oleh daftar **Lengths** dan **Delays**: untuk setiap segmen dapat ditentukan rentang panjang tersendiri (misalnya `100-200`) dan penundaan dalam milidetik (misalnya `10-20` atau `0`). Baris daftar dapat ditambahkan dan dihapus; nilai tunggal yang sebelumnya disimpan dipindahkan ke array dengan satu elemen secara otomatis.

#### Kolom form lainnya

- **UDP over TCP** dan **Versi UoT** — untuk protokol mirip shadowsocks.
- **Tanpa Header gRPC**, **Ukuran Chunk Uplink** — parameter transport gRPC.
- Kolom TLS/uTLS: **Verifikasi Nama Peer**, **Pinned SHA256**, **Short ID**, **Vision testpre**, placeholder «nama server».

#### Pengujian outbound

Tombol: **Uji**, **Uji Semua**. Status: **Menguji koneksi...**, **Pengujian berhasil**, **Pengujian gagal**, **Gagal menguji koneksi keluar**. Hasil: **Hasil Pengujian**, latensi dalam milidetik.

Dua mode (keterangan: *«TCP: probe dial-only cepat. HTTP: permintaan penuh melalui xray.»*):

- **TCP** (`mode=tcp`) — dial sederhana ke `host:port`, dijalankan secara paralel untuk semua endpoint, ~timeout 5 detik. Hanya memeriksa keterjangkauan TCP, tidak memvalidasi protokol proxy. Untuk `freedom`/`blackhole`/tag `blocked` akan mengembalikan *«Outbound has no testable endpoint»*.
- **HTTP** (`mode=http` atau kosong) — menjalankan instans Xray sementara, mengirim permintaan HTTP nyata (probe URL = `outboundTestUrl` server), mengukur latensi nyata. Mode otoritatif tetapi mahal: diserialisasi dengan kunci global (*«Another outbound test is already running, please wait»*). Timeout satu percobaan — 10 detik, jendela tunggu hasil — 15 detik (ditingkatkan agar outbound yang sehat pada saluran lambat atau terterowongi tidak ditandai sebagai «Failed»). Saat gagal, penyebab nyata (kesalahan DNS, connection refused, deadline terlampaui, kesalahan TLS, dll.) ditulis ke log panel/Xray, yang ditunjuk oleh pesan timeout umum.

> Protokol UDP (`wireguard`, `hysteria`) dan transport UDP (`kcp`, `quic`, `hysteria`) **selalu** diuji dalam mode HTTP, bahkan jika TCP diminta — dial UDP murni tidak membedakan endpoint «hidup» dari «mati». Untuk wireguard dalam konfigurasi pengujian, `noKernelTun: true` dipaksa.

#### Pemeriksaan batch dan perincian per tahap

**Uji** dan **Uji Semua** dalam mode HTTP menjalankan satu instans Xray sementara bersama untuk sekelompok outbound, membuat loopback SOCKS-inbound dengan aturan untuk masing-masing, dan mengirimkan permintaan HTTP nyata secara paralel melaluinya; **Uji Semua** memeriksa outbound dalam batch. **Uji Semua** juga memeriksa outbound yang diperoleh dari subscription (tabel «dari subscription», hanya baca) — barisnya juga disorot dengan hasil pengujian. Sementara itu, outbound `freedom` («direct») dan `dns` tidak diuji dalam mode apa pun (ini bukan proxy): tombol uji tidak tersedia untuk mereka, **Uji Semua** melewatinya, dan perlindungan server melarang pengujian HTTP mereka bahkan saat API dipanggil langsung. Selain berhasil/gagal, popup hasil menampilkan status HTTP respons dan perincian waktu per tahap: **Proxy connect** (koneksi ke proxy), **TLS via outbound** (TLS melalui outbound), dan **First byte** (waktu ke byte pertama) — ini membantu memahami pada langkah mana terjadi latensi atau kegagalan.

#### Statistik lalu lintas outbound

Panel menyimpan penghitung lalu lintas berdasarkan tag (`up`/`down`/`total`). Tombol reset mengatur ulang penghitung untuk tag tertentu atau untuk semua (`tag = "-alltags-"`). Kolom **Informasi Akun** dan **Status Koneksi Keluar** menampilkan ringkasan.

### 11.5. Balancer (Balancers)

Daftar `routing.balancers`. Tombol: **Buat Balancer**, **Edit Balancer**.

Pada tab Balancers terdapat kolom status langsung: **Live Target** menampilkan target aktif saat ini dari balancer dalam Xray yang berjalan, dan **Override** memungkinkan penggantian target secara manual (nilai **Auto (strategy)** mengembalikan pemilihan berdasarkan strategi). Status diperbarui dengan tombol terpisah. Jika balancer belum aktif dalam Xray yang berjalan, panel akan menyarankan untuk menyimpan perubahan atau menjalankan Xray terlebih dahulu.

| Kolom | Label | Deskripsi |
|---|---|---|
| Tag | **Tag** (keterangan: *«Tag unik»*) | Pengenal unik. Placeholder: *«tag balancer unik»*. Validasi: *«Tag wajib diisi»*, *«Tag sudah digunakan oleh balancer lain»*. |
| Selektor | **Selektor** | Daftar tag outbound (berdasarkan substring) di antara mana balancer memilih keluar. Setidaknya satu harus dipilih: *«Pilih setidaknya satu outbound»*. |
| Fallback | **Fallback** | Tag outbound cadangan jika tidak ada selektor yang cocok. |
| Strategi | **Strategi** | Algoritma pemilihan (lihat di bawah). |

#### Strategi dan parameter observasi

Strategi (`strategy.type`) menentukan bagaimana balancer memilih outbound dari selektor. Nilai Xray-core: `random` (acak), `roundRobin` (bergilir), `leastPing` (latensi minimum berdasarkan hasil observatory), `leastLoad` (beban minimum). Untuk `leastLoad`/`leastPing` digunakan parameter dari `strategy.settings`:

| Kolom | Label | Deskripsi |
|---|---|---|
| `expected` | **Ekspektasi** | Placeholder: *«jumlah node optimal»* — jumlah node hidup yang ditargetkan. |
| `maxRtt` | **RTT Maks.** | Batas atas RTT yang dapat diterima saat memilih kandidat. |
| `tolerance` | **Toleransi** | Toleransi saat membandingkan latensi/beban. |
| `baselines` | **Baselines** | Nilai ambang batas latensi untuk pengelompokan node. |
| `costs` | **Costs** | Koefisien bobot (cost) untuk tag individual. |

**Contoh strategi.** Blok `strategy` berada di dalam balancer (dalam JSON — berdampingan dengan `tag` dan `selector`):

```json
"strategy": { "type": "random" }      // pemilihan acak dari selektor
"strategy": { "type": "roundRobin" }  // bergilir, bergantian
"strategy": { "type": "leastPing" }   // latensi minimum (memerlukan observer)
```

Untuk `leastLoad`, parameter ditentukan dalam `settings`:

```json
"strategy": {
  "type": "leastLoad",
  "settings": {
    "expected": 2,
    "maxRTT": "1s",
    "tolerance": 0.05,
    "baselines": ["500ms", "1s", "2s"],
    "costs": [
      { "regexp": false, "match": "proxy-premium",   "value": 0.1 },
      { "regexp": true,  "match": "^proxy-cheap-.+$", "value": 5 }
    ]
  }
}
```

**Cara kerjanya (contoh).** Misalkan observer mengukur latensi untuk keluar: `A = 250 ms`, `B = 280 ms`, `C = 700 ms`, `D = 1500 ms`. Dengan pengaturan di atas, pemilihannya berjalan seperti ini:

1. **`maxRTT: "1s"`** — keluar dengan latensi di atas 1 detik dieliminasi: `D` (1500 ms) gugur. Tersisa `A`, `B`, `C`.
2. **`baselines` + `expected`** — keluar dikelompokkan berdasarkan ambang batas latensi, dan diambil ambang batas **terkecil** yang mencakup setidaknya `expected` keluar. Ambang `500ms` sudah berisi `A` dan `B` — ini 2 (= `expected`), jadi kelompok {`A`, `B`} dipilih. `C` (700 ms) tidak masuk pemilihan selama yang cepat masih cukup (ia adalah «cadangan panas»).
3. **`tolerance: 0.05`** — dalam kelompok yang dipilih, keluar yang latensinya tidak berbeda lebih dari 5% dianggap setara, dan beban dibagi merata di antara mereka. `A` (250) dan `B` (280) berbeda sekitar 12% (> 5%), jadi jika semua sama `A` yang lebih cepat yang diutamakan; jika perbedaannya dalam 5% — lalu lintas akan mengalir melalui `A` dan `B`.
4. **`costs`** — sebelum perbandingan, «biaya» keluar individual disesuaikan: `value` lebih kecil membuat keluar lebih menarik, lebih besar — sebaliknya. Dalam contoh, `proxy-premium` mendapat `0.1` (menjadi «lebih murah» dan lebih sering dipilih), dan semua `proxy-cheap-*` (berdasarkan ekspresi reguler, `regexp: true`) — `5` (menjadi «lebih mahal» dan digunakan terakhir). Ini memungkinkan memprioritaskan keluar secara halus tanpa mengecualikannya secara ketat.

Hasil: lalu lintas sebagian besar akan mengalir melalui `A` (jika latensinya dekat — merata dengan `B`), `C` tetap sebagai cadangan, `D` dikecualikan selama RTT-nya tidak turun di bawah `maxRTT`.

#### Observer: `observatory` dan `burstObservatory` (pengukuran untuk `leastPing` / `leastLoad`)

Strategi `leastPing` dan `leastLoad` sendiri tidak mengukur apa pun — mereka memerlukan data tentang latensi dan ketersediaan setiap outbound. Data ini dikumpulkan oleh **observer** (observatory): ia secara berkala «meping» setiap outbound yang dipantau dan mencatat waktu respons dan ketersediaan. Data yang sama ditampilkan pada tab **«Observatory»** (status **Aktif / Tidak Tersedia**, **«Aktivitas Terakhir»**, **«Percobaan Terakhir»**).

Tidak ada form terpisah untuk observer di panel — blok ditambahkan **secara manual** di editor konfigurasi Xray, pada level atas konfigurasi (berdampingan dengan `routing` dan `outbounds`), setelah itu perlu **restart Xray**.

Tersedia dua varian:

- **`observatory`** — sederhana: `subjectSelector` + `probeURL` + `probeInterval`.
- **`burstObservatory`** — lanjutan, dengan konfigurasi ping yang terperinci melalui `pingConfig`; nyaman untuk beberapa keluar.

Contoh blok `burstObservatory`:

```json
{
  "subjectSelector": ["WS-SE", "WS-FR", "WS-PL"],
  "pingConfig": {
    "destination": "https://www.google.com/generate_204",
    "interval": "1m",
    "connectivity": "http://connectivitycheck.platform.hicloud.com/generate_204",
    "timeout": "5s",
    "sampling": 2
  }
}
```

Arti kolom:

| Kolom | Fungsi |
|---|---|
| `subjectSelector` | Daftar **prefiks tag** outbound untuk dipantau. Xray mengambil semua outbound yang tagnya dimulai dengan string yang ditentukan. Dalam contoh, keluar `WS-SE…`, `WS-FR…`, `WS-PL…` yang dipantau. Tag ini harus sesuai dengan yang dipilih di **Selektor** balancer. |
| `pingConfig.destination` | URL yang diminta **melalui setiap outbound** untuk mengukur latensi. Gunakan halaman «ringan» yang merespons `204` tanpa body — misalnya `https://www.google.com/generate_204`. Waktu hingga respons adalah latensi yang diukur. |
| `pingConfig.interval` | Seberapa sering meping setiap outbound. String durasi: `"1m"` — sekali per menit, juga `"30s"`, `"5m"`, dll. Lebih sering — data lebih segar, tetapi lebih banyak lalu lintas latar belakang. |
| `pingConfig.connectivity` | (opsional) URL pemeriksaan **konektivitas dasar** server itu sendiri. Jika tidak tersedia — berarti masalahnya ada pada jaringan server, dan observer **tidak** menandai outbound sebagai tidak tersedia (perlindungan dari false positive saat terjadi kegagalan lokal). Biasanya juga endpoint yang merespons `204`. |
| `pingConfig.timeout` | Berapa lama menunggu respons untuk satu ping sebelum menganggap percobaan gagal (misalnya `"5s"`). |
| `pingConfig.sampling` | Berapa banyak pengukuran terakhir yang disimpan dan dirata-rata untuk setiap outbound. `2` — memperhitungkan dua ping terakhir (memuluskan lonjakan acak). |

Cara menghubungkan semuanya:

1. Di editor Xray, tambahkan blok `burstObservatory` dengan `subjectSelector` yang diperlukan.
2. Buat balancer: **Strategi** = `leastPing`, di **Selektor** tentukan tag outbound yang sama (`WS-SE`, `WS-FR`, `WS-PL`).
3. Arahkan lalu lintas ke sana dengan aturan routing (kolom **Tag balancer**, lihat [11.3](#113-aturan-routing-routing)).
4. Restart Xray. Pada tab **«Observatory»** akan muncul status keluar, dan balancer akan mulai memilih yang tercepat dari yang hidup.

> Dalam satu aturan tidak mungkin sekaligus menentukan `balancerTag` dan `outboundTag` — hanya `outboundTag` yang akan berfungsi.

### 11.6. DNS

Bagian `dns`. Aktifkan: **Aktifkan DNS** (keterangan: *«Aktifkan server DNS bawaan»*).

#### Parameter DNS Umum

| Kolom | Label | JSON | Deskripsi / keterangan |
|---|---|---|---|
| `tag` | **Nama Tag DNS** | `dns.tag` | *«Tag ini akan tersedia sebagai tag inbound dalam aturan routing.»* Memungkinkan routing permintaan DNS itu sendiri melalui `inboundTag`. |
| `clientIp` | **IP Klien** | `dns.clientIp` | *«Digunakan untuk memberi tahu server tentang lokasi IP yang ditentukan selama permintaan DNS»* (EDNS Client Subnet). |
| `strategy` | **Strategi Permintaan** | `dns.queryStrategy` | *«Strategi umum resolusi nama domain»*. Nilai: `UseIP`, `UseIPv4`, `UseIPv6`. |
| `disableCache` | **Nonaktifkan Cache** | `dns.disableCache` | *«Menonaktifkan cache DNS»*. |
| `disableFallback` | **Nonaktifkan DNS Cadangan** | `dns.disableFallback` | *«Menonaktifkan permintaan DNS cadangan»*. |
| `disableFallbackIfMatch` | **Nonaktifkan DNS Cadangan Jika Cocok** | `dns.disableFallbackIfMatch` | *«Menonaktifkan permintaan DNS cadangan jika daftar domain server DNS cocok»*. |
| `enableParallelQuery` | **Aktifkan Permintaan Paralel** | — | *«Aktifkan permintaan DNS paralel ke beberapa server untuk resolusi lebih cepat»*. |
| `useSystemHosts` | **Gunakan Hosts Sistem** | `dns.useSystemHosts` | *«Gunakan file hosts dari sistem yang terinstal»*. |

**Contoh blok `dns`.** Permintaan ke domain Google di-resolve melalui server DoH Cloudflare, sisanya melalui `1.1.1.1`; untuk permintaan Google hanya IP non-privat yang diharapkan. Pada level atas konfigurasi:

```json
"dns": {
  "tag": "dns-inbound",
  "queryStrategy": "UseIPv4",
  "servers": [
    {
      "address": "https://cloudflare-dns.com/dns-query",
      "domains": ["geosite:google"],
      "expectIPs": ["geoip:!private"]
    },
    "1.1.1.1"
  ]
}
```

String server (`"1.1.1.1"`) tanpa kolom — ini adalah server default untuk semua domain lainnya. Tag `dns-inbound` kemudian dapat digunakan sebagai `inboundTag` dalam aturan routing untuk mengarahkan permintaan DNS itu sendiri melalui outbound yang diperlukan.

#### Cache catatan yang kedaluwarsa

| Kolom | Label | Deskripsi |
|---|---|---|
| `serveStale` | **Gunakan Yang Kedaluwarsa** | *«Kembalikan hasil yang kedaluwarsa dari cache saat melakukan pembaruan di latar belakang»*. |
| `serveExpiredTTL` | **TTL Kedaluwarsa** | *«Masa berlaku (detik) catatan cache yang kedaluwarsa; 0 = tanpa batas»*. |

#### Server DNS (daftar `dns.servers`)

Tombol: **Buat DNS**, **Edit DNS**, **Hapus Semua** (konfirmasi: *«Semua server DNS akan dihapus dari daftar. Tindakan ini tidak dapat dibatalkan.»*). Template: **Gunakan Template**, jendela **Template DNS**, termasuk preset **Keluarga**.

Saat menekan **Edit DNS** pada entri server DNS (seperti pada entri Fake DNS), jendela edit mengisi nilai server yang disimpan, bukan nilai default.

Kolom server DNS:

| Kolom | Label | Deskripsi |
|---|---|---|
| address | — | Alamat DNS (IP, URL DoH, `localhost`, `fakedns`, dll.). |
| `domains` | **Domain** | Daftar domain yang menggunakan server ini. |
| `expectIPs` | **IP yang Diharapkan** | Terima respons hanya jika IP masuk dalam daftar. |
| `unexpectIPs` | **IP yang Tidak Diharapkan** | Buang respons dengan IP yang ditentukan. |
| `skipFallback` | **Lewati Fallback** | Jangan gunakan server ini sebagai fallback. |
| `finalQuery` | **Permintaan Final** | Menandai server sebagai final dalam rantai. |
| `timeoutMs` | **Timeout (ms)** | Timeout permintaan ke server. |

#### Hosts (catatan statis)

Grup **Hosts** (`dns.hosts`). Tombol **Tambah Host**; status kosong **Host tidak ditentukan**. Kolom: domain (placeholder: *«Domain (mis. domain:example.com)»*) dan nilai (placeholder: *«IP atau domain — masukkan dan tekan Enter»*).

#### Log DNS

Lihat [11.9](#119-log-dan-statistik-stats-metrics): flag **Log DNS** (`dnsLog`) di bagian logging.

### 11.7. Fake DNS

Bagian `fakedns`. Tombol: **Buat Fake DNS**, **Edit Fake DNS**.

| Kolom | Label | Deskripsi |
|---|---|---|
| `ipPool` | **Subnet Pool IP** | Rentang CIDR dari mana IP fiktif dikeluarkan (misalnya `198.18.0.0/15`). |
| `poolSize` | **Ukuran Pool** | Berapa banyak alamat yang disimpan dalam pool siklik. |

Fake DNS digunakan bersama dengan sniffing pada inbound: inti memberikan IP fiktif kepada klien, mengingat korespondensi domain↔IP dan memulihkan domain saat routing. Agar Fake DNS berfungsi, server DNS dengan alamat `fakedns` harus ditambahkan ke daftar server DNS.

**Contoh: kombinasi Fake DNS + server DNS.** Pertama kita tentukan pool alamat fiktif, lalu tambahkan server DNS `fakedns` agar permintaan domain mendapat IP dari pool ini:

```json
"fakedns": [
  { "ipPool": "198.18.0.0/15", "poolSize": 65535 }
],
"dns": {
  "servers": [
    { "address": "fakedns", "domains": ["geosite:geolocation-!cn"] },
    "1.1.1.1"
  ]
}
```

Selain itu, pada inbound perlu mengaktifkan sniffing dengan `destOverride: ["fakedns"]`, jika tidak, inti tidak memiliki cara untuk mendapatkan domain nyata untuk pemulihan.

### 11.8. WireGuard / WARP / NordVPN

#### Kolom WireGuard (`wireguard`)

| Kolom | Label | Deskripsi |
|---|---|---|
| `secretKey` | **Kunci Rahasia** | Kunci privat antarmuka lokal. |
| `publicKey` | **Kunci Publik** | Kunci publik peer. |
| `psk` | **Kunci Bersama** | PreShared Key (opsional). |
| `allowedIPs` | **IP yang Diizinkan** | Rentang yang diarahkan ke dalam tunnel. |
| `endpoint` | **Endpoint** | `host:port` peer. |
| `domainStrategy` | **Strategi Domain** | Strategi resolve untuk WireGuard-outbound. |

#### Cloudflare WARP (`warp`)

Integrasi menggunakan API `https://api.cloudflareclient.com/v0a4005` (client-version `a-6.30-3596`). Tindakan controller (`/xray/warp/:action`): `config`, `reg`, `license`, `data`, `del`.

Langkah demi langkah:

1. **Buat akun WARP** → `reg`: panel membuat/menerima kunci privat (`privateKey`) dan publik (`publicKey`), mendaftarkan perangkat di Cloudflare dan menyimpan `access_token`, `device_id`, `license_key`, `private_key` (serta `client_id`) dalam pengaturan `warp`.
2. **Kunci lisensi WARP / WARP+** → `license`: pengaturan kunci WARP+ 26 karakter (placeholder: *«kunci WARP+ 26 karakter»*). Jika terjadi kesalahan: *«Gagal mengatur lisensi WARP.»* Jika konfigurasi belum diperoleh: *«Dapatkan konfigurasi WARP terlebih dahulu.»*
3. **Informasi akun**: **Nama Perangkat**, **Model Perangkat**, **Perangkat Diaktifkan**, **Jenis Akun**, **Peran**, **Data WARP+**, **Kuota**, **Penggunaan**.
4. **Tambah outbound** — membuat WireGuard-outbound dengan kunci dan endpoint Cloudflare yang diperoleh.
5. **Hapus akun** → `del`: menghapus data WARP yang tersimpan.

#### NordVPN (`nord` / `nordvpn`)

Integrasi menggunakan NordLynx (= WireGuard). Tindakan controller (`/xray/nord/:action`): `countries`, `servers`, `reg`, `setKey`, `data`, `del`.

Langkah demi langkah:

1. **Token akses** → `reg`: panel meminta kredensial NordLynx dari `api.nordvpn.com` dan mengekstrak `nordlynx_private_key`. Menyimpan `private_key` dan `token` dalam pengaturan `nord`. Alternatifnya — `setKey`: masukkan **Kunci Privat** secara langsung (tidak boleh kosong).
2. **Negara** → `countries` memuat daftar negara; **Kota** (atau **Semua Kota**).
3. **Server** → `servers` memuat server dari negara yang dipilih (`countryId` divalidasi sebagai angka — perlindungan dari injeksi). Filter: hanya server dengan **Beban** > 7% yang ditampilkan. Jika tidak ada server: *«Server untuk negara yang dipilih tidak ditemukan»*. Jika server tidak memiliki kunci publik NordLynx: *«Server yang dipilih tidak melaporkan kunci publik NordLynx.»*
4. Pembuatan/pembaruan outbound: toast *«Outbound NordVPN ditambahkan»* / *«Outbound NordVPN diperbarui»*.

#### Prioritas IPv4 dan userspace TUN

WireGuard-outbound yang dihasilkan oleh wizard WARP dan NordVPN menggunakan `domainStrategy: "ForceIPv4v6"` (prioritas IPv4 dengan fallback ke IPv6 di host hanya-v6) alih-alih `ForceIP` — ini menghilangkan «penggantungan» handshake di host dengan IPv6 yang setengah dikonfigurasi, saat rekaman AAAA endpoint Cloudflare dipilih. Selain itu, userspace TUN (`noKernelTun: true`) diaktifkan untuk mereka alih-alih kernel TUN: yang terakhir memerlukan hak dan routing fwmark serta gagal secara senyap di banyak VPS, sementara pemeriksaan koneksi bawaan panel selalu diuji melalui userspace TUN — kini lalu lintas nyata dan pemeriksaan menggunakan jalur yang sama. Perubahan hanya berlaku untuk outbound yang baru ditambahkan atau yang direset; template yang sudah disimpan mempertahankan pengaturannya.

### 11.9. Reverse-proxy dan TUN

#### Reverse (reverse-proxy)

Bagian `reverse` dari konfigurasi Xray. Dalam form outbound terdapat toggle untuk tipe **Reverse-proxy**. Tombol: **Buat Reverse-proxy**, **Edit Reverse-proxy**.

| Kolom | Label | Deskripsi |
|---|---|---|
| Tipe | **Tipe** | **Bridge** atau **Portal** — dua peran reverse-proxy Xray. |
| Domain | **Domain** | Domain label layanan untuk pasangan bridge↔portal. |
| Tag / Koneksi | **Tag** / **Koneksi** | Tag untuk menghubungkan bridge dan portal. |
| Reverse Tag | **Tag Reverse-proxy** | Keterangan: *«Tag koneksi keluar untuk reverse-proxy VLESS sederhana. Biarkan kosong untuk menonaktifkan.»* Placeholder: *«tag outbound (kosong = nonaktif)»*. Mengimplementasikan VLESS reverse yang disederhanakan. |

Dalam form outbound juga terdapat kolom aliran balik: **Sniffing balik**, **Worker**, **Dicadangkan**, **Interval Upload Min (ms)**, **Ukuran Upload Maks (byte)**.

#### TUN (`tun`)

| Kolom | Label | Deskripsi | Default |
|---|---|---|---|
| name | — | *«Nama antarmuka TUN.»* | **`xray0`** |
| mtu | — | *«Maximum Transmission Unit. Ukuran maksimum paket data.»* | **1500** |
| `userLevel` | **Level Pengguna** | *«Semua koneksi yang dibuat melalui aliran masuk ini akan menggunakan level pengguna ini.»* | **0** |

### 11.10. Log dan Statistik (Stats, metrics)

#### Log (`log`)

Keterangan: *«Log dapat memperlambat server. Aktifkan hanya jenis log yang Anda butuhkan saat diperlukan!»* Bagian `log` dari template referensi: `access: "none"`, `error: ""`, `loglevel: "warning"`, `dnsLog: false`, `maskAddress: ""`.

| Kolom | Label | JSON | Deskripsi | Default |
|---|---|---|---|---|
| `logLevel` | **Level Log** | `loglevel` | *«Level jurnal untuk log kesalahan…»* Nilai: `debug`, `info`, `warning`, `error`, `none`. | **`warning`** |
| `accessLog` | **Log Akses** | `access` | *«Jalur ke file log akses. Nilai khusus «none» menonaktifkan log akses.»* | **`none`** |
| `errorLog` | **Log Kesalahan** | `error` | *«Jalur ke file log kesalahan. Nilai khusus «none» menonaktifkan log kesalahan.»* | **`""`** (default) |
| `dnsLog` | **Log DNS** | `dnsLog` | *«Aktifkan log permintaan DNS»* | **false** |
| `maskAddress` | **Penyamaran Alamat** | `maskAddress` | *«Saat diaktifkan, alamat IP nyata diganti dengan alamat penyamaran dalam log.»* | **`""`** (nonaktif) |

#### Statistik (`stats` / `policy`)

Grup **Statistik**. Mengaktifkan penghitung di `policy.system` dan `policy.levels`. Dalam template referensi: `statsInboundUplink: true`, `statsInboundDownlink: true`, `statsOutboundUplink: false`, `statsOutboundDownlink: false`; untuk level `0` — `statsUserUplink: true`, `statsUserDownlink: true`.

| Kolom | Label | Deskripsi | Default |
|---|---|---|---|
| `statsInboundUplink` | **Statistik Uplink Inbound** | *«Mengaktifkan pengumpulan statistik untuk lalu lintas keluar dari semua proxy inbound.»* | **true** |
| `statsInboundDownlink` | **Statistik Downlink Inbound** | *«Mengaktifkan pengumpulan statistik untuk lalu lintas masuk dari semua proxy inbound.»* | **true** |
| `statsOutboundUplink` | **Statistik Uplink Outbound** | *«Mengaktifkan pengumpulan statistik untuk lalu lintas keluar dari semua proxy outbound.»* | **false** |
| `statsOutboundDownlink` | **Statistik Downlink Outbound** | *«Mengaktifkan pengumpulan statistik untuk lalu lintas masuk dari semua proxy outbound.»* | **false** |

> Statistik klien dan inbound (uplink/downlink) — merupakan dasar tampilan lalu lintas di dashboard dan di klien; tidak disarankan untuk menonaktifkannya. Statistik outbound dinonaktifkan secara default dan hanya diperlukan jika Anda memantau lalu lintas berdasarkan tag outbound.

#### Metrics

Dalam template referensi terdapat bagian `metrics` (`listen: "127.0.0.1:11111"`, `tag: "metrics_out"`) dan API `metrics_out` yang sesuai. Panel menggunakan listener ini untuk mengumpulkan metrik dan snapshot observatory: ia mem-parse `metrics.listen` dari template, menanyakan `/debug/vars`, dan mengagregasi riwayat latensi berdasarkan tag. Jika Anda mengubah alamat/port `metrics.listen`, panel akan mengakses alamat baru; menghapus bagian `metrics` akan menonaktifkan pengumpulan grafik observatory.

> Pengujian outbound dalam mode HTTP menjalankan **instans Xray sementara yang terpisah** dengan listener `metrics`-nya sendiri pada port acak — ini bukan listener yang sama seperti pada konfigurasi utama.

### 11.11. Penyimpanan, restart, dan transformasi otomatis

#### Tombol

| Tombol | Tindakan |
|---|---|
| **Simpan** | `POST /xray/update`: memvalidasi dan menyimpan template + `outboundTestUrl`. |
| **Restart Xray** | Memuat ulang layanan dengan konfigurasi yang disimpan. Konfirmasi: *«Restart xray?»* / *«Memuat ulang layanan xray dengan konfigurasi yang disimpan.»* |

Toast: berhasil — *«Xray berhasil di-restart»*, *«Xray berhasil dihentikan»*; kesalahan — *«Terjadi kesalahan saat me-restart Xray.»*, *«Terjadi kesalahan saat menghentikan Xray.»* Jendela **Output Restart Xray** menampilkan output diagnostik inti.

#### Penerapan perubahan secara langsung (tanpa restart penuh)

Perubahan inbounds, outbounds, dan aturan routing diterapkan «langsung»: saat menekan **Simpan**, panel menghitung perbedaan antara konfigurasi lama dan baru dan menerapkan hanya bagian yang berubah melalui gRPC-API Xray (HandlerService/RoutingService), tanpa me-restart proses. Restart penuh hanya dilakukan secara otomatis ketika bagian-bagian tanpa API hot-reload berubah (`log`, `dns`, `policy`, `observatory`, dll.). Oleh karena itu, pada halaman Xray tidak diperlukan tombol terpisah «Restart» — **Simpan** sendiri yang menerapkan perubahan. Restart inti jika diperlukan tetap dilakukan secara otomatis (lihat juga auto-reload saat memperbarui subscription dan rotasi WARP).

#### Pemulihan template default

Endpoint `GET /xray/getDefaultJsonConfig` mengembalikan template referensi (`config.json`, yang tertanam dalam binari). Dengan ini Anda dapat mengatur ulang konfigurasi ke pengaturan pabrik.

#### Transformasi otomatis saat penyimpanan

Saat menyimpan pengaturan Xray, panel melakukan (dalam urutan ini):

1. **Penghapusan pembungkus** — menghapus pembungkus dalam bentuk `{ "xraySetting": <config>, "inboundTags": …, "outboundTestUrl": … }` jika secara tidak sengaja masuk ke nilai (jika tidak, lapisan akan menumpuk setiap kali disimpan). Hingga 8 lapisan dihapus.
2. **Verifikasi konfigurasi** — JSON diurai ke dalam struktur konfigurasi Xray; jika terjadi kesalahan — ditolak dengan *«xray template config invalid»*.
3. **Jaminan aturan statistik** — aturan `inboundTag: ["api"] → outboundTag: "api"` secara paksa dinaikkan ke posisi 0 dalam `routing.rules` (atau ditambahkan jika tidak ada). Ini memastikan bahwa permintaan gRPC-statistik panel tidak akan dicegat oleh aturan catch-all yang ada di atasnya (jika tidak, klien dapat ditampilkan sebagai offline dengan lalu lintas nol saat proxy berjalan).

> Karena poin 3, jangan mencoba menghapus atau memindahkan aturan `api → api` — panel akan mengembalikannya ke tempatnya pada penyimpanan berikutnya. Ini adalah infrastruktur layanan statistik, bukan rute pengguna.

### 11.12. Outbound dari subscription (dengan auto-update)

Mulai versi 3.3.0, panel dapat mengimpor `outbound` langsung dari URL subscription — format yang sama seperti yang diberikan penyedia VPN untuk aplikasi klien. Subscription dibaca ulang secara berkala di latar belakang, sehingga set `outbound` di server selalu diperbarui tanpa perlu mengedit template konfigurasi secara manual.

Bagian ini disebut **«Subscription Outbound»**, dengan deskripsi: «Impor outbound dari URL subscription jarak jauh (vmess/vless/trojan/ss/...). Tag tetap tidak berubah untuk digunakan dalam balancer dan aturan routing. Pembaruan dilakukan secara otomatis.» Bagian ini terletak di halaman Xray, di atas panel pengaturan `outbound`.

#### Cara kerjanya

Subscription disimpan terpisah dari template konfigurasi Xray. Template **tidak pernah ditimpa**: `outbound` yang diperoleh dari subscription ditambahkan ke konfigurasi akhir secara langsung saat setiap pembuatan konfigurasi Xray.

#### Menambahkan subscription

Dalam form «Tambah Subscription» tersedia kolom berikut:

| Kolom | Kunci | Default | Fungsi |
|------|------|--------------|------------|
| URL Subscription | `url` | — (wajib) | Alamat subscription. Placeholder: «https://... (daftar tautan dalam base64)». Hanya HTTP(S) yang diterima; alamat diperiksa keamanannya. |
| Catatan | `remark` | kosong | Label sembarang (placeholder «mis. node HK»). |
| Prefiks Tag | `tagPrefix` | `subN-` | Prefiks yang mengawali tag `outbound` yang diimpor. Jika dibiarkan kosong, panel akan memilih nomor bebas terkecil seperti `sub1-`, `sub2-`, dll. |
| Interval Pembaruan | `updateInterval` | 600 detik (10 menit) | Seberapa sering subscription dibaca ulang. Di UI ditentukan dalam jam/menit. |
| Aktif | `enabled` | ya (`true`) | Hanya subscription yang aktif yang masuk ke konfigurasi dan diperbarui secara otomatis. |
| Izinkan alamat privat | `allowPrivate` | tidak (`false`) | Mengizinkan URL di localhost, LAN, dan IP privat. Nonaktif secara default untuk perlindungan dari SSRF — aktifkan hanya untuk sumber lokal yang terpercaya. |
| Sebelum outbound manual | `prepend` | tidak (`false`) | Jika diaktifkan, `outbound` dari subscription ini ditempatkan **sebelum** `outbound` manual dari template, dan salah satunya bisa menjadi `outbound` default. Jika tidak, mereka ditambahkan **setelah**. |

Tombol **«Pratinjau»** (`POST /outbound-subs/parse`) memungkinkan pengunduhan dan penguraian URL sebelum disimpan dan melihat `outbound` serta tag apa yang akan dihasilkan; tidak ada yang ditulis ke database pada saat itu. Jika tidak ada yang dikenali dari URL, pesan «Tidak ada outbound yang ditemukan di URL ini.» ditampilkan.

Urutan beberapa subscription dalam daftar `outbound` keseluruhan ditentukan oleh prioritas (`priority`) dan diubah dengan panah atas/bawah (`POST /outbound-subs/:id/move`).

#### Format subscription yang diterima

Isi respons dari URL diproses sebagai berikut:

- Konten pertama kali dicoba sebagai **base64** (varian standar dan URL-safe, dengan auto-padding dan penghapusan spasi/newline). Jika ini base64 — didekode; jika tidak — diambil apa adanya.
- Kemudian isi dipecah menjadi baris. Setiap baris yang tidak kosong dan tidak dimulai dengan `#` diurai sebagai tautan. Baris yang tidak dikenali (komentar, protokol yang tidak didukung) dilewati secara senyap.
- Skema tautan yang didukung: `vmess://`, `vless://`, `trojan://`, `ss://` (Shadowsocks), `hysteria2://` / `hy2://`, `wireguard://` / `wg://`.

Artinya, subscription biasa dalam bentuk «daftar tautan yang dikodekan dalam base64», seperti yang digunakan sebagian besar penyedia, dapat diterima.

#### Tag yang stabil

Setiap tautan dihitung «identitasnya» yang stabil (URI inti tanpa fragmen catatan; untuk vmess — JSON internal tanpa kolom `ps`). Korespondensi «identitas → tag» disimpan, dan pada pembaruan berikutnya server yang sama mendapatkan tag yang sama, bahkan jika catatan atau parameter sekunder berubah. Ini sengaja dirancang agar balancer dan aturan routing tetap berfungsi setelah pembaruan:

- Tag yang tepat dalam balancer/aturan akan terus menunjuk ke server yang sama.
- Selektor prefiks/wildcard (misalnya, `hk-*`) secara otomatis akan menangkap server baru yang dikembalikan subscription nanti — ini adalah cara yang disarankan untuk «berlangganan ke pool».
- Jika server menghilang dari subscription, tagnya hanya hilang dari array `outbound` akhir; jika balancer memiliki `fallbackTag`, Xray akan menggunakannya.
- Jika penyedia mengubah UUID/host/kredensial server, identitasnya berubah — ini dianggap sebagai `outbound` baru dengan tag baru.

Dalam satu ekspor, tag dideduplikasi dengan sufiks `-N`. Tag dari subscription mempertahankan karakter non-ASCII dan tetap dapat dibaca: huruf dan angka Unicode dipertahankan dalam slug, dan tanda baca digantikan dengan tanda hubung.

#### Cara kerja auto-update

- Tugas latar belakang pembaruan subscription dijalankan sesuai jadwal **setiap 5 menit**.
- Pada setiap jalannya, ia memeriksa semua subscription yang aktif dan hanya memperbarui yang intervalnya telah habis: subscription diperbarui jika belum pernah diperbarui atau jika sudah berlalu setidaknya `updateInterval` sejak pembaruan terakhir. Dengan demikian tugas memeriksa subscription dengan sering, tetapi setiap subscription tertentu dibaca ulang tidak lebih sering dari `updateInterval`-nya (default 10 menit). Ini tercermin dalam keterangan UI yang sesuai.
- Pembaruan: URL diperiksa ulang keamanannya sebagai publik (alamat privat diblokir kecuali subscription memiliki `allowPrivate`), permintaan dikirim melalui klien proxy panel dengan header `User-Agent: 3x-ui-outbound-sub/1.0`. Rantai pengalihan dibatasi 10 hop, dan setiap hop juga diperiksa privasinya (perlindungan dari SSRF). HTTP 200 diharapkan; jika tidak, kesalahan dicatat.
- Setelah penguraian yang berhasil, hasilnya disimpan, waktu pembaruan terakhir dicatat, kesalahan dihapus. Jika terjadi kesalahan, teksnya terlihat di UI sebagai «Kesalahan Terakhir», dan `outbound` yang sebelumnya diperoleh tetap berlaku.
- Jika setidaknya satu subscription benar-benar diperbarui, tugas menandai Xray untuk restart dan mengirimkan invalidasi UI agar antarmuka mengambil `outbound` baru. Restart Xray yang sebenarnya terjadi pada siklus 30 detik terdekat dari manager.

Pembaruan manual satu subscription — tombol **«Perbarui Sekarang»** (`POST /outbound-subs/:id/refresh`); ia juga menandai Xray untuk restart. Penambahan, perubahan, penghapusan subscription juga mengatur flag restart Xray (saat dihapus, `outbound`-nya keluar dari konfigurasi pada reload berikutnya). UI memberi tahu: «Setelah menambahkan atau memperbarui, restart Xray (atau tunggu auto-reload berikutnya) agar outbound menjadi aktif.»

#### Cara masuk ke konfigurasi Xray

Pada setiap pembuatan konfigurasi Xray, `outbound` subscription yang aktif dibagi menjadi dua kelompok — `prepend` (flag «Sebelum outbound manual») dan lainnya — dan digabungkan dengan template: `[subscription prepend] + [outbound template] + [subscription lainnya]`. Dalam setiap kelompok, subscription diurutkan berdasarkan prioritas. `outbound` manual dari template tidak terpengaruh; jika karena suatu alasan array `outbound` template tidak dapat diurai, `outbound` subscription tidak dicampurkan ke dalamnya (agar tidak kehilangan yang manual).

`outbound` yang diimpor juga ditampilkan di panel `outbound` itu sendiri dalam blok terpisah **«Dari Subscription Outbound (hanya baca)»** — tidak dapat diedit di sana, pengelolaan hanya melalui bagian «Subscription Outbound».

### 11.13. Rotasi IP WARP

Di 3X-UI Anda dapat menjalankan WARP-outbound — koneksi WireGuard keluar ke Cloudflare WARP (tag `warp` dalam konfigurasi Xray). Panel sendiri mendaftarkan akun perangkat di server Cloudflare, mendapatkan kunci WireGuard dan alamat, serta memasukkannya ke outbound dengan tag `warp`. Melalui outbound tersebut, lalu lintas keluar ke internet melalui alamat IP Cloudflare WARP. Fitur baru versi 3.3.0 — kemampuan untuk mengubah IP keluar ini secara manual atau terjadwal, tanpa perlu membuat ulang akun WARP secara manual.

Pengelolaan terdapat di bagian **Xray** di kartu WARP (setelah menekan «Buat Akun WARP» dan mendapatkan konfigurasi; sebelum itu, tindakan tidak tersedia — panel akan memberi tahu «Dapatkan konfigurasi WARP terlebih dahulu»).

#### Apa yang terjadi saat mengganti IP

Tombol **«Ganti IP»** memulai penggantian IP. Logikanya:

1. Pasangan kunci WireGuard baru dibuat.
2. Dengan kunci baru, perangkat WARP didaftarkan ulang di server Cloudflare (`device_id`, `access_token`, alamat, dan data peer baru).
3. Data baru ditulis ke WARP-outbound konfigurasi Xray: `secretKey`, `address` (v4 `/32` dan v6 `/128`), `reserved` (dari `client_id`), serta `publicKey` dan `endpoint` pada peer diperbarui.
4. Jika sebelumnya kunci lisensi WARP+ telah ditentukan (panjang setidaknya 26 karakter), kunci tersebut secara otomatis dipasang ulang ke akun baru. Jika gagal, ini hanya peringatan di log — penggantian IP tidak dibatalkan.
5. Setelah penggantian berhasil, Xray ditandai sebagai memerlukan restart agar outbound baru berlaku.

Saat berhasil, antarmuka menampilkan «Alamat IP WARP berhasil diubah!».

#### Rotasi otomatis terjadwal

Dalam kartu WARP terdapat toggle **«Pembaruan IP Otomatis»** dan kolom **«Interval (hari)»**. Keterangan: «0 — nonaktifkan. Ubah alamat IP secara otomatis.»

| Parameter | Nilai |
|---|---|
| Pengaturan di DB | `warpUpdateInterval` (bilangan bulat, ≥ 0) |
| Nilai default | `0` (rotasi otomatis dinonaktifkan) |
| Satuan | hari |
| `0` | menonaktifkan penggantian otomatis |
| `> 0` | ganti IP setiap N hari |

Menyimpan interval menyimpan `warpUpdateInterval`, dan jika nilainya lebih dari 0, «waktu pembaruan terakhir» diatur ulang ke saat ini — jika tidak, scheduler akan mengganti IP pada tick terdekat.

Jadwal dieksekusi oleh tugas latar belakang yang berjalan sekali per jam — artinya panel memeriksa setiap jam apakah sudah waktunya untuk rotasi. Algoritma pemeriksaan:

- jika interval ≤ 0 — tidak melakukan apa pun;
- jika «waktu pembaruan terakhir» sama dengan 0 (misalnya, interval ditetapkan dengan pengeditan langsung DB) — ini adalah jalannya pertama: tugas hanya mencatat cap waktu dasar dan TIDAK langsung mengganti IP;
- jika sudah berlalu setidaknya `interval × 24 × 3600` detik sejak pembaruan terakhir — penggantian IP yang sama dilakukan, cap waktu diperbarui, dan restart Xray dijadwalkan.

Detail penting: penggantian manual melalui tombol «Ganti IP» juga mengatur ulang cap waktu pembaruan terakhir. Oleh karena itu, setelah rotasi manual, hitungan mundur interval otomatis dimulai dari awal dan penggantian terjadwal tidak akan segera terpicu.

#### «Melalui proxy panel»

> **Diubah di 3.3.1.** Pengaturan terpisah «Proxy Jaringan Panel» (`panelProxy`) telah dihapus. Lalu lintas keluar panel itu sendiri (termasuk permintaan ke WARP API) sekarang diarahkan melalui **outbound lalu lintas panel** yang dipilih — Xray-outbound atau balancer (lihat bagian [13](#13-pengaturan-panel)). Deskripsi di bawah ini berlaku untuk versi sebelum 3.3.1.

Semua permintaan ke API Cloudflare WARP (pendaftaran, mendapatkan konfigurasi, mengatur lisensi, mengganti IP) tidak dilakukan secara langsung, tetapi melalui klien HTTP panel dengan timeout 15 detik. Klien ini menghormati pengaturan **«Proxy Jaringan Panel»** (`panelProxy`) dari pengaturan panel.

Dari deskripsi pengaturan: proxy merutekan permintaan keluar panel itu sendiri (pembaruan basis geo, pemeriksaan versi Xray/panel, Telegram, dan kini juga akses ke WARP) — untuk melewati pemfilteran server. Alamat dalam format `socks5://` atau `http(s)://` diterima, misalnya inbound SOCKS lokal dari Xray itu sendiri. Jika kolom kosong atau proxy tidak valid — koneksi langsung digunakan (perilaku tidak rusak).

Manfaat untuk WARP: jika server tidak dapat langsung mengakses `api.cloudflareclient.com`, pendaftaran dan rotasi dulu akan gagal. Sekarang, dengan menentukan proxy yang berfungsi di `panelProxy` (termasuk inbound Xray Anda sendiri), Anda dapat menjamin ketersediaan WARP API dan fungsionalitas tombol manual maupun rotasi terjadwal.

#### Kapan ini berguna

- Pergantian IP keluar secara berkala untuk outbound yang berjalan melalui WARP — mengurangi risiko pemblokiran dan pelacakan dari satu alamat.
- «Menyegarkan» IP secara manual jika alamat Cloudflare saat ini masuk dalam daftar hitam atau bekerja lambat.
- Server yang tidak memiliki akses langsung ke Cloudflare WARP API: merutekan permintaan melalui `panelProxy` membuat pendaftaran dan rotasi menjadi fungsional.

---

## 12. Node (multipanel, master/slave)

Bagian **Node** mengubah instalasi 3X-UI biasa menjadi **panel pusat (master)** yang memantau dan mengelola panel 3X-UI lain (panel anak) dari jarak jauh. Setiap node adalah instalasi 3X-UI terpisah di servernya sendiri; master menghubunginya melalui HTTP API-nya sendiri, mengambil statusnya, serta menyinkronkan inbound dan klien yang ditetapkan ke node tersebut. Inilah kemampuan **multipanel**: alih-alih masuk ke setiap panel secara terpisah, Anda melihat semua server dalam satu daftar dan mengelolanya secara terpusat.

Prinsip penting: **node bukan agen, melainkan panel 3X-UI lengkap.** Master tidak "menginstal" apa pun di sana — ia hanya terhubung ke API-nya menggunakan token. Menghapus node dari daftar hanya menghentikan pemantauan; panel jarak jauh itu sendiri tidak terpengaruh (keterangan: "Ini akan menghentikan pemantauan node. Panel jarak jauh itu sendiri tidak akan terpengaruh").

### 12.1. Ringkasan di bagian atas daftar

Di atas tabel node ditampilkan penghitung agregat:

| Kolom | Deskripsi |
|---|---|
| Total node | Jumlah total node dalam daftar. |
| Online | Berapa banyak node dengan status `online`. |
| Offline | Berapa banyak node dengan status `offline`. |
| Rata-rata latensi | Rata-rata latensi (ping) ke node, dalam milidetik. |

### 12.2. Menambahkan dan mengedit node

Tombol **Tambah node** dan **Edit node** membuka formulir dengan kolom-kolom node.

Kolom yang wajib diisi (keterangan: "Nama, alamat, port, dan token API wajib diisi") adalah **Nama**, **Alamat**, **Port**, dan **Token API**.

Saat menekan "Simpan" (baik saat menambahkan maupun mengedit), panel terlebih dahulu **memverifikasi keterjangkauan node** dengan batas waktu 6 detik. Jika node tidak merespons, catatan tidak disimpan dan ditampilkan pesan kesalahan. Artinya, node yang jelas tidak dapat dijangkau tidak dapat ditambahkan.

#### Kolom formulir

| Kolom | Default | Nilai yang diizinkan | Deskripsi |
|---|---|---|---|
| Nama | — (wajib) | string tidak kosong, **unik** | Nama internal node. Kolom nama memiliki batasan keunikan — dua node dengan nama yang sama tidak dapat dibuat. Placeholder keterangan: `contoh. de-frankfurt-1`. Saat menyimpan, spasi di tepi dipangkas. |
| Catatan | kosong | string apa pun | Catatan/deskripsi node opsional. Tidak memengaruhi operasi. |
| Skema | `https` | `http` / `https` | Protokol koneksi ke panel jarak jauh. Jika dikosongkan atau nilai yang tidak valid ditentukan, normalisasi akan menetapkan `https`. Jika node merespons melalui HTTP biasa tetapi skema diatur ke `https`, panel akan menampilkan keterangan yang jelas: "the server speaks HTTP, not HTTPS; set the node scheme to http". |
| Alamat | — (wajib) | host atau IP | Alamat panel jarak jauh. Placeholder: `panel.example.com atau 1.2.3.4`. Alamat dinormalisasi; secara default alamat privat/lokal dilarang untuk perlindungan dari SSRF — lihat "Izinkan alamat privat". |
| Port | — (wajib) | bilangan bulat **1–65535** | Port panel web node jarak jauh. Nilai di luar rentang ditolak ("node port must be 1-65535"). |
| Jalur dasar | `/` | string jalur | Jalur dasar (web base path) panel jarak jauh, jika ditetapkan. Dinormalisasi: dijamin dimulai dan diakhiri dengan `/` (nilai kosong → `/`). Panel menambahkan `panel/api/server/status` ke dalamnya saat melakukan polling. |
| Token API | — (wajib) | token panel jarak jauh | Token Bearer untuk akses ke API node. Dikirimkan dalam header `Authorization: Bearer <token>`. Placeholder: "Token dari halaman Pengaturan panel jarak jauh". Keterangan: "Panel jarak jauh menampilkan token API-nya di bagian Pengaturan → Token API". Artinya, token harus dibuat **pada node itu sendiri** (Pengaturan → Token API), lalu ditempelkan di sini. |
| Diaktifkan | `true` | ya/tidak | Mengaktifkan pemantauan dan sinkronisasi node. Node yang dinonaktifkan **tidak di-polling** oleh tugas latar belakang (heartbeat dan traffic-sync melewatinya) dan tidak berpartisipasi dalam pembaruan panel massal. |
| Izinkan alamat privat | `false` | ya/tidak | Menonaktifkan perlindungan SSRF dan mengizinkan koneksi ke node melalui alamat privat/lokal. Keterangan: "Aktifkan hanya untuk node di jaringan privat atau VPN". Aktifkan hanya ketika node benar-benar berada di jaringan privat atau dapat diakses melalui VPN. |

#### Mendapatkan dan meregenerasi token di sisi node

Token diambil dari panel jarak jauh di bagian **Pengaturan → Token API**. Di sana Anda juga dapat menerbitkan ulang: tombol **Buat ulang token** dengan peringatan: "Regenerasi akan membatalkan token saat ini. Panel pusat mana pun yang menggunakannya akan kehilangan akses hingga diperbarui. Lanjutkan?". Setelah regenerasi, token lama di panel master tidak akan berfungsi lagi — perlu diperbarui di formulir node.

#### Koneksi keluar (Connection outbound)

Kolom **Connection outbound** (Koneksi keluar, `outboundTag`) menentukan bagaimana lalu lintas permintaan master ke API node ini keluar dari server. Jika Anda memilih tag Xray-outbound di dalamnya, permintaan panel ke node tidak akan dilakukan secara langsung tetapi melalui outbound yang ditentukan; panel itu sendiri akan menambahkan bridge-inbound pada loopback ke konfigurasi yang sedang berjalan dan menerapkan perubahan secara langsung, tanpa restart. Keterangan: "Route this node's panel API traffic through the selected Xray outbound. A loopback bridge inbound is added to the running config automatically and applied live. Leave empty for a direct connection".

Selektor ini berfungsi seperti pilihan outbound panel: tag dikelompokkan menjadi **Outbounds** (outbound biasa) dan **Balancers** (penyeimbang beban), outbound blackhole disembunyikan dari daftar. Nilai kosong (placeholder "Direct connection") = koneksi langsung ke node.

#### Import inbound (memilih inbound yang disinkronkan)

Di formulir node terdapat pengaturan **Import inbound** (`inboundSyncMode`) dengan dua mode: **Semua inbound** (`all`, default) dan **Dipilih** (`selected`). Secara default master menyinkronkan ke node semua inbound yang memilih node tersebut; node yang sudah ada terus bekerja dalam mode "Semua inbound".

Dalam mode **Dipilih**, di bawah kolom muncul pemilihan multi-tag inbound. Klik **Muat inbound** — master akan meminta daftar inbound-nya dari node berdasarkan parameter koneksi yang dimasukkan (belum disimpan) (endpoint `POST /panel/api/nodes/inbounds`) dan menampilkan tag-nya; pilih yang diperlukan. Panel akan menyinkronkan dan menerapkan ke node hanya tag yang dipilih, sementara inbound lain yang ada langsung di node akan dibiarkan tidak tersentuh — master tidak menghapus atau mengelolanya.

**Contoh: meminta daftar inbound node untuk import selektif.** Isi permintaan berisi parameter koneksi yang belum disimpan; respons berisi tag inbound yang tersedia di node:

```
POST /panel/api/nodes/inbounds
Content-Type: application/json

{ "name": "de-fra-1", "scheme": "https", "address": "node1.example.com",
  "port": 2053, "basePath": "/", "apiToken": "abcdef..." }
```

### 12.3. Verifikasi TLS (untuk node https)

Kelompok kolom menentukan bagaimana master memverifikasi sertifikat HTTPS node. Pengaturan ini **hanya relevan untuk skema `https`**; untuk node `http` pengaturan ini diabaikan.

**Verifikasi TLS** — daftar dropdown, keterangan: "Bagaimana panel memverifikasi sertifikat HTTPS node. Pinning atau Lewati — untuk sertifikat self-signed (hanya node https)".

| Mode | Nilai | Default | Deskripsi |
|---|---|---|---|
| Verifikasi (CA standar) | `verify` | ya (default) | Verifikasi rantai sertifikat normal menggunakan CA tepercaya. Cocok untuk node dengan sertifikat publik/Let's Encrypt. Juga digunakan untuk semua node `http`. |
| Pin sertifikat (SHA-256) | `pin` | — | Rantai CA tidak diverifikasi, tetapi SHA-256 sertifikat leaf node dibandingkan dengan fingerprint yang tersimpan (perbandingan constant-time). Mempertahankan perlindungan dari MITM untuk sertifikat **self-signed**. Membutuhkan pengisian kolom fingerprint. |
| Lewati verifikasi | `skip` | — | Verifikasi sertifikat dinonaktifkan sepenuhnya. Peringatan: "Melewati verifikasi menghilangkan perlindungan dari serangan man-in-the-middle — token API dapat dicegat. Lebih baik pin sertifikat". |

Selain tiga mode di atas, pada 3.4.0 ditambahkan mode keempat — **Mutual TLS (client certificate)** (`mtls`), tersedia, seperti yang lainnya, hanya untuk skema `https`.

| Mode | Nilai | Default | Deskripsi |
|---|---|---|---|
| Mutual TLS (sertifikat klien) | `mtls` | — | Selain memverifikasi sertifikat node, master juga mengautentikasi dirinya ke node dengan **sertifikat klien** yang diterbitkan oleh CA-nya sendiri. Untuk node dalam mode ini, **token API menjadi opsional** — node mengenali master berdasarkan sertifikat. Saat mode ini dipilih, keterangan ini ditampilkan: "This node authenticates the panel with a client certificate. Copy this panel's CA from the Node mTLS section onto the node, set its Trusted parent CA, then restart it". |

Untuk mengaktifkan mutual TLS untuk node: di sisi node, atur mode **Mutual TLS**, salin CA dari panel pengelola di bagian **Node mTLS** (lihat di bawah), tetapkan sebagai **CA induk tepercaya** di node dan restart node tersebut.

Jika nilai apa pun selain `skip`, `pin`, atau `mtls` dipilih, normalisasi akan memaksa penetapan `verify`.

#### Pinning sertifikat

Saat **Pin sertifikat** dipilih, muncul:

- **SHA-256 sertifikat yang di-pin** — kolom input. Menerima fingerprint dalam **base64** (format `pinnedPeerCertSha256` dari Xray) atau dalam **hex** dengan titik dua atau tanpa (gaya `openssl -fingerprint`). Keterangan: "SHA-256 sertifikat node dalam base64 atau hex. Klik 'Ambil' untuk membacanya dari node sekarang". Placeholder: "SHA-256 dalam base64 atau hex". Saat `pin` dipilih, fingerprint kosong atau tidak valid menyebabkan kesalahan validasi saat menyimpan.

**Contoh: fingerprint yang sama dalam dua format.** Kolom menerima format mana pun — keduanya mewakili sertifikat yang sama:

```
# base64 (format pinnedPeerCertSha256 dari Xray)
6O7TNg3l2k0pq8R1sT2uV3wX4yZ5a6B7c8D9e0F1g2=

# hex dengan titik dua (gaya openssl x509 -fingerprint -sha256)
E8:E2:D3:60:DE:5D:9A:4D:29:AB:CF:11:B2:7C:34:...
```

Jika fingerprint belum diketahui, klik **Ambil** — master akan membacanya dari node melalui HTTPS dan mengisinya ke kolom.
- Tombol **Ambil** — terhubung ke node melalui HTTPS tanpa verifikasi sertifikat dan membaca SHA-256 sertifikat leaf saat ini (endpoint `POST /certFingerprint`), mengisinya ke kolom. Setelah berhasil — "Sertifikat node saat ini berhasil diambil"; jika gagal — "Gagal mengambil sertifikat". Hanya tersedia untuk node https.

#### Node mTLS (mutual TLS authentication antar panel)

Di halaman **Node** terdapat bagian terpisah **Node mTLS** — pengaturan mutual TLS authentication yang menambahkan faktor kedua (sertifikat klien) di atas token API untuk panggilan "panel → node". Mutual TLS bersifat opsional; jika kolom bagian ini kosong, node bekerja dengan skema sebelumnya — **hanya dengan token API** (keterangan: "Mutual TLS adds a client-certificate factor on top of the API token for node-to-node calls. It is opt-in: leave it empty to keep token-only auth"). Bagian ini memiliki dua operasi:

- **Salin CA panel ini** (`POST /panel/api/nodes/mtls/ca`) — menyalin sertifikat root (CA) panel ini ke clipboard. CA ini perlu diteruskan ke node yang dikelola agar mereka mempercayai sertifikat klien panel; pada node itu sendiri kemudian mode verifikasi TLS **Mutual TLS** ditetapkan (keterangan: "Hand this CA to the nodes this panel manages, then set their TLS verification to Mutual TLS"). Setelah disalin — "CA certificate copied to clipboard".
- **CA induk tepercaya** (`Trusted parent CA`, `POST /panel/api/nodes/mtls/trustCA`) — kolom yang digunakan ketika panel ini sendiri berperan sebagai node untuk panel pengelola (induk). Tempelkan CA panel pengelola di sini untuk meminta sertifikat kliennya, lalu klik **Save trust CA**. Perubahan ini memerlukan **restart panel** (keterangan: "When this panel is itself a node, paste the managing panel's CA here to require its client certificate. Restart the panel to apply").

### 12.4. Apa yang ditampilkan untuk setiap node

Kolom tabel dan kolom kartu node (status yang diamati, diisi pada setiap polling heartbeat):

| Kolom | Deskripsi |
|---|---|
| Status | `online` / `offline` / `unknown` — lihat di bawah. |
| CPU | Beban prosesor server jarak jauh dalam persen. |
| Memori | Penggunaan RAM dalam persen (dihitung sebagai `current/total*100`). |
| Uptime | Waktu operasi server yang berkelanjutan (dalam detik). |
| Latensi | Waktu respons node pada polling terakhir (ms). |
| Ping terakhir | Waktu heartbeat sukses terakhir (unix-detik; `0` = "tidak pernah"; nilai terbaru ditampilkan sebagai "baru saja"). |
| Versi Xray | Versi Xray-core yang berjalan di node. |
| Versi panel | Versi 3X-UI di node — dibandingkan dengan yang terbaru untuk indikator pembaruan. |
| (inbound) | Berapa banyak inbound yang secara fisik ditempatkan di node ini. |
| (klien) | Jumlah klien di inbound node. |
| (online) | Berapa banyak klien node yang sedang online. |
| (habis) | Berapa banyak klien node yang **kedaluwarsa atau telah mencapai batas lalu lintas**. Klien yang dinonaktifkan secara manual tidak termasuk dalam penghitung ini. |
| (kecepatan) | Kecepatan transfer saat ini (langsung) di inbound yang ditempatkan di node. |

Penghitung inbound/klien/online dikaitkan dengan node berdasarkan GUID stabilnya (`panelGuid`), bukan berdasarkan id lokal — agar klien di subnode dihitung tepat di bawah subnode tersebut, bukan di bawah node perantara yang melaluinya sinkronisasi dilakukan.

Untuk inbound yang ditempatkan di node, halaman menampilkan klien online, penghitung, dan **kecepatan transfer saat ini**. Pengaitan berdasarkan GUID stabil secara benar memisahkan node "yang di-klon" dengan `panelGuid` yang sama.

#### Status node

| Status | Kapan ditetapkan |
|---|---|
| `online` | Node merespons `success=true` pada polling `panel/api/server/status`. |
| `offline` | Node tidak merespons, mengembalikan kesalahan HTTP, `success=false`, atau respons yang tidak dapat dikenali. |
| `unknown` | Nilai awal, saat node belum pernah di-polling sebelumnya. |

Ketika polling gagal, teks kesalahan disimpan dan ditampilkan dengan kalimat yang jelas, membantu mendiagnosis penyebab "offline".

### 12.5. Tindakan pada node

- **Uji koneksi** (`POST /test`) — di formulir node, menguji konektivitas berdasarkan parameter yang dimasukkan (belum disimpan) dengan batas waktu 6 detik. Hasil: "Koneksi berhasil ({ms} ms)" atau "Gagal terhubung". Berguna untuk men-debug alamat/port/token/TLS sebelum menyimpan.
- **Periksa sekarang** (tombol "Periksa sekarang", `POST /probe/:id`) — polling tidak terjadwal dari node yang sudah disimpan; segera memperbarui status dan metrik (CPU/memori/uptime/latensi/versi) dan mencatat heartbeat. Jika gagal — "Pemeriksaan gagal".

**Contoh: menguji dan memeriksa node melalui API master.** "Uji koneksi" menguji parameter yang belum disimpan dari formulir:

```
POST /panel/api/nodes/test
Content-Type: application/json

{ "scheme": "https", "address": "de-frankfurt-1.example.com", "port": 2053,
  "basePath": "/", "apiToken": "eyJhbGci...", "tlsMode": "verify" }
```

Polling tidak terjadwal dari node yang sudah disimpan dengan id 7:

```
POST /panel/api/nodes/probe/7
```
- **Perbarui panel** (`POST /updatePanel` dengan isi `{ids:[…]}`) — menjalankan pembaruan otomatis standar di node: node mengunduh rilis terbaru 3X-UI dan melakukan restart dengan versi tersebut. Tombol **Perbarui yang dipilih ({count})** melakukan ini untuk beberapa node yang dipilih sekaligus. Di samping node ditampilkan indikator: **Pembaruan tersedia** atau **Sudah terbaru**, berdasarkan perbandingan versi panel node dengan versi terbaru.

**Contoh: memperbarui beberapa node dengan satu permintaan.** Isi berisi id node yang dipilih; hanya node yang diaktifkan dan `online` yang akan diperbarui, sisanya akan dikembalikan sebagai dilewati.

```
POST /panel/api/nodes/updatePanel
Content-Type: application/json

{ "ids": [3, 7, 12] }
```

Respons seperti "Pembaruan dimulai pada 2 node, 1 gagal": node 12, misalnya, mungkin offline dan karenanya dilewati.
  - Konfirmasi: "Perbarui {count} node ke versi terbaru? Setiap node yang dipilih akan mengunduh rilis terbaru dan melakukan restart. Hanya node yang diaktifkan dan online yang diperbarui".
  - **Hanya node yang diaktifkan dengan status `online` yang diperbarui.** Node yang dinonaktifkan dalam hasil ditandai "node is disabled", offline — "node is offline". Hasil: "Pembaruan dimulai pada {ok} node, {failed} gagal". Jika tidak ada node yang sesuai yang dipilih — "Pilih setidaknya satu node yang diaktifkan dan online".
- **Set Cert from Panel** (tambahan, `GET /webCert/:id`) — saat membuat inbound di node, memungkinkan pengisian jalur ke sertifikat web-TLS **milik** node itu sendiri (bukan panel pusat), agar file-file tersebut ada tepat di node. Memerlukan node diaktifkan dan dapat dijangkau.
- **Hapus node** (`POST /del/:id`) — konfirmasi: "Hapus node "{name}"? Ini akan menghentikan pemantauan node. Panel jarak jauh itu sendiri tidak akan terpengaruh". Menghapus catatan node dan statistik lalu lintas yang terakumulasi; panel jarak jauh terus berjalan seperti biasa. **Node hanya dapat dihapus setelah semua inbound dilepaskan darinya.** Jika setidaknya satu inbound masih terkait dengan node (melalui `node_id`), panel akan menolak penghapusan dengan kesalahan seperti "cannot delete node: N inbound(s) still attached to it; detach or delete them first" — lepaskan atau hapus inbound tersebut terlebih dahulu, kemudian hapus node. Ini mencegah inbound "yatim piatu" dengan referensi menggantung ke node yang dihapus.

### 12.6. Riwayat metrik

Tombol/grafik riwayat mengakses `GET /history/:id/:metric/:bucket`. Metrik yang tersedia: **`cpu`** dan **`mem`** — keduanya terakumulasi pada setiap heartbeat yang berhasil. Ukuran interval agregasi (`bucket`, dalam detik) dibatasi oleh daftar putih:

**Contoh: permintaan riwayat.** Grafik beban CPU node 7 dengan agregasi berdasarkan interval 60 detik (mengembalikan hingga 60 titik):

```
GET /panel/api/nodes/history/7/cpu/60
```

Untuk memori dan mode "real-time" (2 detik) — masing-masing `…/7/mem/60` dan `…/7/cpu/2`. Nilai di luar daftar putih ditolak ("invalid metric" / "invalid bucket").

| Bucket (detik) | Tujuan |
|---|---|
| 2 | Mode real-time |
| 30 | Interval per 30 detik |
| 60 | Interval per 1 menit |
| 120 | Interval per 2 menit |
| 180 | Interval per 3 menit |
| 300 | Interval per 5 menit |

Mengembalikan hingga 60 titik. Metrik atau bucket yang tidak valid ditolak ("invalid metric" / "invalid bucket").

### 12.7. Cara inbound dan klien disinkronkan

Inbound "dimiliki" oleh node melalui kolom `node_id` (di editor inbound, node dipilih):

**Contoh: token di formulir node.** Token diambil dari panel anak (Pengaturan → Token API) dan ditempelkan ke kolom **Token API** master. Pada setiap polling, master mengirimkannya di header:

```
GET https://panel.example.com:2053/panel/api/server/status
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.abc123...
```

Jika panel anak memiliki **jalur dasar** (web base path) yang ditetapkan, misalnya `/secret/`, master secara otomatis akan menambahkannya sebelum `panel/api/server/status` → `https://panel.example.com:2053/secret/panel/api/server/status`.

1. **Penerapan konfigurasi (reconcile).** Saat ada perubahan pada inbound/klien yang terkait dengan node, node ditandai sebagai "kotor". Tugas latar belakang untuk setiap node yang diaktifkan **dengan status `online`** jika ada perubahan, menerapkan inbound-nya ke node (berdasarkan `node_id`) dan kemudian mereset tanda "kotor". Node yang dinonaktifkan, offline, atau "kotor" dianggap "menunggu" — penerapan ke node tersebut ditunda hingga koneksi pulih.
2. **Pengumpulan lalu lintas.** Tugas yang sama meminta snapshot lalu lintas dari node dan menggabungkannya ke statistik lokal. Berdasarkan lalu lintas yang digabung, pemeriksaan habisnya batas/masa berlaku dilakukan dan klien dinonaktifkan jika diperlukan; penghitung "habis" per node mencerminkan hal ini. Jika node tidak dapat dijangkau, klien online-nya dihapus.

   Untuk klien yang terhubung ke beberapa panel sekaligus, master dalam tugas yang sama juga mendistribusikan ke node **total konsumsi lalu lintas** klien tersebut di semua panel (dalam tabel terpisah di node, kunci — GUID master; ditimpa pada setiap pengiriman, sehingga reset di sisi master juga disebarkan). Di node, nilai yang lebih besar dari keduanya ditampilkan dalam lalu lintas klien — lokal atau yang dikirimkan — dan ketika kuota total terlampaui, klien dinonaktifkan **secara lokal di node itu sendiri** (melalui mekanisme restart Xray yang sama saat penonaktifan otomatis, yang memutus koneksi yang sudah ada). Ini menghilangkan situasi di mana node hanya melihat bagiannya sendiri dari lalu lintas, mencatat konsumsi yang kurang, dan terus melayani klien yang telah melampaui batas total. Saat mereset lalu lintas, perpanjangan otomatis, atau penghapusan klien, penghitung yang dikirimkan dihapus.
3. **Heartbeat.** Tugas latar belakang terpisah secara berkala melakukan polling ke semua node yang **diaktifkan** (dengan pembatasan paralelisme) melalui `panel/api/server/status`, memperbarui status/metrik/versi dan, jika ada klien web, mendistribusikan pohon node yang diperbarui melalui WebSocket.

### 12.8. Rantai node (subnode / node transitif)

Topologi tidak harus datar: node itu sendiri dapat menjadi master untuk node-nya sendiri. Panel bawahan seperti itu ditampilkan kepada Anda sebagai **Subnode** — ini adalah **proyeksi hanya-baca** yang diterima dari node langsung.

- Keterangan: "Hanya baca: node bawahan yang dapat diakses melalui {induk}. Kelola dari panel {induk} sendiri". Artinya, subnode tidak dapat diedit, dihapus, atau diperbarui di sini — semua operasi padanya dilakukan dari panel induk langsungnya.
- Identitas subnode ditentukan oleh GUID-nya; berkat ini, klien online dan inbound dihitung tepat di bawah node fisik yang menghostingnya, bahkan dalam rantai `Node1 → Node2 → Node3` (master "melewati" satu level lebih dalam melalui setiap node langsung).
- Jika node langsung menjadi tidak dapat dijangkau, cache subnodenya dihapus, dan subnode menghilang dari pohon hingga koneksi pulih.

### 12.9. Node: hal baru di 3.3.0

Pada versi 3.3.0, bagian **Node** mendapat tiga peningkatan signifikan: atribusi lalu lintas dan klien online yang benar dalam topologi multi-level (multi-hop), sinkronisasi client-IP antar node, dan indikator status terpisah untuk kasus di mana panel node online tetapi inti Xray-nya jatuh. Kata-kata inbound/outbound selanjutnya tidak diterjemahkan.

#### 1. Multi-hop: atribusi lalu lintas yang benar dalam rantai subnode

Sebelumnya penghitung (jumlah inbound, klien online, habis) dihitung di tingkat node "langsung". Jika Anda memiliki rantai `Master → Node1 → Node2 → Node3`, semua yang secara fisik ada di `Node2`/`Node3` salah diatribusikan ke `Node1`, yang melaluinya data tersebut sampai ke master. Pada 3.3.0, atribusi berdasarkan sumber nyata.

Cara kerjanya:

- **Subnode menjadi terlihat sebagai baris terpisah.** Setiap panel mempublikasikan daftar node langsungnya; hanya node dengan `Guid` yang diketahui yang disertakan — identitas stabil diperlukan untuk mengaitkan node satu "lompatan" ke atas. Master secara berkala (dari tugas heartbeat) mengambil daftar ini dan menyimpannya dalam cache, kemudian menambahkan subnode "transitif" ke node langsung.
- **Node transitif bersifat hanya-baca.** Di UI mereka ditandai sebagai **"Subnode"** dengan keterangan: *"Hanya baca: node bawahan yang dapat diakses melalui {induk}. Kelola dari panel {induk} sendiri."* Tidak ada tombol kontrol untuk baris tersebut — node dikelola dari panel induk langsungnya.
- **Hierarki melalui GUID.** Node langsung memiliki `ParentGuid` — GUID master itu sendiri; untuk yang transitif — GUID node induknya. Dengan cara ini pohon dibangun.
- **Sumber kebenaran untuk penghitung adalah `origin_node_guid` pada inbound.** Ini adalah `panelGuid` node yang secara fisik memegang inbound tersebut. Ini ditetapkan saat sinkronisasi inbound dari node dan **dipertahankan apa adanya pada lompatan selanjutnya**, sehingga inbound yang sangat bersarang diatribusikan ke node nyata, bukan ke node perantara. Berdasarkan GUID ini penghitung jumlah inbound, klien online, dan klien habis dihitung ulang. Logika pemilihan kunci:

  | Status inbound | Diatribusikan ke |
  |---|---|
  | `origin_node_guid` ditetapkan | GUID ini (node sumber nyata) |
  | kosong, tetapi `node_id` ditetapkan | GUID sintetis node (build lama, belum melaporkan `panelGuid`-nya) |
  | kosong dan `node_id` kosong | GUID master sendiri (inbound di Xray lokal) |

  Klien online juga dikelompokkan berdasarkan GUID, sehingga setiap baris node hanya menampilkan mereka yang benar-benar terhubung ke node tersebut.

**Yang dilihat pengguna:** dalam topologi datar (node langsung di bawah master) tidak ada perubahan — penghitung berdasarkan GUID dan berdasarkan `id` sesuai. Namun begitu ada rantai node, baris "Subnode" muncul dalam daftar, dan angka inbound/online/habis untuk setiap node sekarang mencerminkan beban kerjanya sendiri, bukan jumlah semua yang melewatinya dalam transit.

#### 2. Sinkronisasi client-IP dari access.log antar node

Batas IP (`limitIp` pada klien) bergantung pada alamat yang ditulis Xray di access.log-nya. Sebelumnya setiap node hanya melihat koneksi ke dirinya sendiri, sehingga pembatasan "tidak lebih dari N IP per klien" tidak berfungsi di kluster: klien bisa terhubung ke node yang berbeda dan melewati batas. Pada 3.3.0, IP yang diamati disinkronkan di seluruh kluster.

Cara kerjanya:

- Di setiap node, tugas latar belakang mengurai access.log, mengekstrak per baris IP, email klien, dan cap waktu, dan menyimpannya dalam tabel lokal (satu catatan per email, IP disimpan sebagai JSON array `{ip, timestamp}`). Alamat lokal `127.0.0.1` dan `::1` dibuang.
- Sinkronisasi **setiap 10 detik** melakukan pertukaran dua arah per setiap node yang diaktifkan dalam jaringan: mengambil IP dari node dan menggabungkannya ke tabel lokal, kemudian memberikan gambaran ringkasan master ke node.
- Penggabungan mengkombinasikan observasi lama dan masuk **tanpa penghitungan ganda** satu IP yang terlihat di beberapa node, dan **tanpa menghidupkan kembali** catatan yang sudah kedaluwarsa: ambang batas kedaluwarsa yang sama diterapkan seperti pada tugas lokal — **30 menit**. Untuk setiap IP, cap waktu paling baru disimpan. Catatan dari node lain mendapat id lokal baru (ruang id node independen); penyisipan bersamaan dari email yang sama dilindungi dari duplikat.
- Saat menghitung batas, IP dianggap "hidup" jika diamati dalam pemindaian lokal saat ini, atau memiliki cap waktu yang sangat baru dari basis yang disinkronkan (**dalam 2 menit**). Inilah yang membuat batas berfungsi di skala seluruh kluster, bahkan jika alamat itu terlihat di node lain. Ketika batas terlampaui, IP "hidup" tertua dikirim ke log fail2ban, dan koneksi diputus paksa (remove/re-add klien melalui Xray API).

**Yang dilihat pengguna:** batasan jumlah IP sekarang berlaku untuk seluruh kluster, bukan setiap node secara individual; di panel untuk klien terlihat IP yang diamati di node mana pun (dalam jendela 30 menit). Tidak ada tombol/pengaturan terpisah untuk ini — sinkronisasi berjalan otomatis di latar belakang, dengan syarat bahwa access.log node diaktifkan dan dapat diakses (untuk batas itu sendiri, Fail2Ban pada node juga diperlukan).

#### 3. Indikator status terpisah: panel node online, tetapi Xray jatuh

Sebelumnya status node pada dasarnya adalah "online / offline". Jika panel node merespons, node dianggap online — bahkan ketika inti Xray di dalamnya tidak berjalan, dan klien sebenarnya tidak dapat terhubung. Pada 3.3.0, kesehatan panel dan kesehatan inti Xray dipisahkan.

Cara kerjanya:

- Saat melakukan polling node, master mengambil dari respons `/panel/api/server/status` jarak jauh kolom `xray.state` dan `xray.errorMsg` dan menyimpannya di node. Kolom-kolom ini diisi bahkan saat ping panel berhasil, ketika inti tidak sehat — justru untuk membedakan ketersediaan panel dari status Xray.
- Nilai `xray.state`: `"running"` (berjalan), `"stop"` (dihentikan), `"error"` (kesalahan).
- Nilai-nilai ini diterjemahkan ke status node. Status baru ditambahkan ke yang sudah dikenal:

  | Kunci status | Saat ditampilkan |
  |---|---|
  | `online` | panel merespons, Xray berjalan (`running`) |
  | `offline` | panel tidak dapat dijangkau / ping gagal |
  | `unknown` | status belum ditentukan |
  | `xrayError` | panel online, tetapi inti Xray dalam status `error` (ada `errorMsg`) |
  | `xrayStopped` | panel online, tetapi Xray dihentikan (`stop`) |

- Untuk status seperti itu di UI digunakan **indikator ungu terpisah** (warna yang berbeda dari hijau "online" dan merah "offline"). Ungu langsung memberi sinyal: node dapat dihubungi, masalahnya ada di inti Xray itu sendiri, bukan di jaringan atau panel.

**Yang dilihat pengguna:** alih-alih "hijau" yang menyesatkan saat inti jatuh, node disorot dengan **ungu** dengan status **"Kesalahan Xray"** atau **"Dihentikan"**. Ini segera menunjukkan bahwa yang perlu diperbaiki adalah Xray di node (restart inti, lihat `errorMsg`), bukan menyelidiki keterjangkauan node itu sendiri. `xrayState`/`xrayError` yang sama juga diteruskan ke subnode transitif (lihat poin 1), sehingga status inti yang tidak normal terlihat di seluruh rantai.

---

## 13. Pengaturan Panel

Bagian "Pengaturan" (judul halaman — **Pengaturan**, Ingg. *Panel Settings*) mengontrol perilaku panel web 3X-UI itu sendiri: di alamat dan port mana ia mendengarkan, bagaimana ia diamankan, bagaimana ia berinteraksi dengan bot Telegram dan layanan eksternal, serta di zona waktu mana ia menjalankan tugas terjadwal. Setiap parameter disimpan dalam tabel `settings` database sebagai pasangan "kunci — nilai"; jika nilai tidak ada di database, nilai default akan digunakan.

> **Penting — penerapan perubahan.** Setiap perubahan di halaman ini harus disimpan dengan tombol **Simpan** (*Save*), lalu panel harus di-restart agar perubahan berlaku. Petunjuk resminya: "Simpan perubahan dan restart panel untuk menerapkannya." Saat menyimpan, muncul notifikasi "Pengaturan telah diubah".

### 13.1. Menyimpan dan Me-restart Panel

| Elemen | Fungsi |
| --- | --- |
| **Simpan** (*Save*) | Menyimpan semua kolom formulir ke database (`POST /panel/setting/update`). Sebelum disimpan, nilai-nilai divalidasi — alamat, port, atau jalur yang tidak valid akan ditolak, dan panel akan mengembalikan error. |
| **Restart Panel** (*Restart Panel*) | Me-restart server web panel (`POST /panel/setting/restartPanel`). Restart dilakukan dengan jeda 3 detik. Petunjuknya: "Apakah Anda yakin ingin me-restart panel? Konfirmasi, dan restart akan terjadi dalam 3 detik. Jika panel tidak dapat diakses, periksa log server." Jika berhasil — "Panel berhasil di-restart." |
| **Reset ke Default** (*Reset to Default*) | Menghapus semua pengaturan yang tersimpan di database, setelah itu panel menggunakan nilai default. Kredensial administrator tidak direset oleh operasi ini. |

Restart dilakukan dengan mengirimkan sinyal `SIGHUP` ke proses panel (atau melalui hook restart yang terdaftar). Di Windows, restart otomatis melalui sinyal tidak didukung. **Perubahan pada parameter listening (IP, port, jalur, domain, sertifikat, zona waktu) hanya diterapkan setelah panel di-restart.**

### 13.2. Pengaturan Umum (tab "Panel" / *General*)

#### Bahasa Antarmuka (*Language*)

Bahasa antarmuka web panel. Bahasa yang tersedia: `en-US` (Inggris), `ru-RU` (Rusia), `zh-CN`, `zh-TW`, `fa-IR`, `ar-EG`, `es-ES`, `id-ID`, `ja-JP`, `pt-BR`, `tr-TR`, `uk-UA`, `vi-VN`. Ini adalah pengaturan tampilan dan tidak memengaruhi cara kerja Xray.

#### Jenis Kalender (*Calendar Type*)

- **Kunci:** `datepicker`
- **Nilai default:** `gregorian` (Gregorian).
- **Fungsi:** jenis kalender yang digunakan dalam pemilihan tanggal (misalnya, saat menetapkan masa berlaku klien). Petunjuk: "Tugas terjadwal akan dijalankan sesuai dengan kalender ini." Nilai alternatif — kalender Persia (Jalali), yang populer di kalangan pengguna panel dari Iran.

#### Ukuran Paginasi (*Pagination Size*)

- **Kunci:** `pageSize`
- **Nilai default:** `25`
- **Nilai yang diizinkan:** bilangan bulat dari `0` hingga `1000`.
- **Fungsi:** jumlah baris per halaman dalam tabel (daftar koneksi/inbound). Petunjuk: "Tentukan ukuran halaman untuk tabel koneksi. Setel ke 0 untuk menonaktifkan" — jika `0`, tampilan halaman dinonaktifkan dan semua entri ditampilkan dalam satu daftar.
- **Restart panel tidak diperlukan** (pengaturan tampilan).

#### Restart Xray Setelah Penonaktifan Otomatis (*Restart Xray After Auto Disable*)

- **Kunci:** `restartXrayOnClientDisable`
- **Nilai default:** `true`
- **Fungsi:** saat klien dinonaktifkan secara otomatis (karena masa berlaku habis atau batas trafik tercapai), Xray di-restart untuk memutus koneksi yang sudah dibuat oleh klien tersebut. Petunjuk: "Saat klien dinonaktifkan secara otomatis karena masa berlaku habis atau batas trafik, restart Xray." Fungsionalitasnya tidak berubah — tombol toggle hanya berada di tab "Panel" (*General*) bersama pengaturan umum lainnya.

#### Model Keterangan dan Karakter Pemisah (*Remark Model & Separation Character*)

- **Kunci:** `remarkModel`
- **Nilai default:** `-ieo`
- **Fungsi:** menentukan bagaimana nama (remark) konfigurasi dalam subscription dibentuk. String terdiri dari **karakter pertama** — pemisah, diikuti **urutan huruf**:
  - `i` — keterangan inbound (*inbound remark*);
  - `e` — email klien;
  - `o` — label tambahan (*extra*).
  
  Dengan nilai default `-ieo`, pemisahnya adalah `-`, dan urutan bagiannya: inbound → email → extra (misalnya, `MyInbound-user@mail-extra`). Bagian yang kosong akan dilewati. Kolom "Contoh Keterangan" (*Sample Remark*) di antarmuka menampilkan pratinjau nama yang dibentuk. Penyertaan email dalam nama juga bergantung pada parameter "Sertakan Email dalam nama" di pengaturan subscription (bagian tentang subscription).

**Contoh: bagaimana nilai `remarkModel` memengaruhi nama konfigurasi.** Misalkan inbound bernama `VLESS-Reality`, email klien — `alex@vpn`, dan label tambahan — `RU`. Maka:

| Nilai kolom | Nama akhir (remark) |
| --- | --- |
| `-ieo` (default) | `VLESS-Reality-alex@vpn-RU` |
| `_ie` | `VLESS-Reality_alex@vpn` |
| `-ei` | `alex@vpn-VLESS-Reality` |
| ` o` (spasi sebagai pemisah, hanya label) | `RU` |

Karakter pertama string selalu menjadi pemisah; huruf-huruf selanjutnya menentukan bagian mana dan dalam urutan apa yang akan masuk ke nama.

### 13.3. Akses ke Panel: IP, Port, Jalur, Domain, Sertifikat

Grup ini menentukan titik masuk jaringan panel. **Semua perubahan di sini hanya diterapkan setelah panel di-restart.**

| Kolom | Kunci | Nilai default | Deskripsi |
| --- | --- | --- | --- |
| Alamat IP untuk manajemen panel (*Listen IP*) | `webListen` | `""` (kosong) | IP tempat panel web mendengarkan. Kosong = mendengarkan di semua IP. Petunjuk: "Biarkan kosong untuk koneksi dari IP mana pun". Jika diisi, harus berupa alamat IP yang valid (jika tidak, penyimpanan akan ditolak). |
| Domain panel (*Listen Domain*) | `webDomain` | `""` (kosong) | Nama domain panel untuk memverifikasi permintaan berdasarkan domain. Kosong = menerima koneksi dari domain dan IP mana pun. Petunjuk: "Biarkan kosong untuk koneksi dari domain dan IP mana pun." |
| Port panel (*Listen Port*) | `webPort` | `2053` | Port tempat panel beroperasi. Petunjuk: "Port tempat panel beroperasi". Diizinkan `1–65535`. Port harus bebas; panel dan layanan subscription tidak dapat menggunakan pasangan `IP:port` yang sama secara bersamaan. |
| Jalur URI (*URI Path*) | `webBasePath` | `/` | Jalur URL dasar panel (basePath). Petunjuk: "Harus dimulai dengan '/' dan diakhiri dengan '/'". Saat menyimpan, panel secara otomatis menambahkan `/` di awal dan akhir jika tidak ada. Karakter yang dilarang dalam jalur akan ditolak. |

##### Sertifikat Panel (TLS / HTTPS)

| Kolom | Kunci | Nilai default | Deskripsi |
| --- | --- | --- | --- |
| Jalur file kunci publik sertifikat panel (*Public Key Path*) | `webCertFile` | `""` | Jalur lengkap ke file sertifikat (rantai). Petunjuk: "Masukkan jalur lengkap yang dimulai dengan '/'". |
| Jalur file kunci privat sertifikat panel (*Private Key Path*) | `webKeyFile` | `""` | Jalur lengkap ke file kunci privat. Petunjuk: "Masukkan jalur lengkap yang dimulai dengan '/'". |

Jika **setidaknya satu** dari jalur sertifikat/kunci diisi, panel saat menyimpan akan mencoba memuat pasangan "sertifikat + kunci"; jika terjadi error (file tidak ada, kunci dan sertifikat tidak cocok), penyimpanan akan ditolak. Jika kedua jalur yang valid diisi, panel beralih ke HTTPS. Keduanya kosong = panel beroperasi dengan HTTP biasa.

> **Peringatan keamanan** (*Security warnings*). Panel menampilkan blok "Panel Anda mungkin terbuka:" dengan peringatan jika konfigurasi yang tidak aman terdeteksi:
> - beroperasi dengan HTTP biasa — "konfigurasikan TLS untuk produksi";
> - port standar 2053 — "ubah ke port acak";
> - jalur dasar default `/` — "ubah ke jalur acak";
> - jalur subscription standar `/sub/` dan JSON-subscription `/json/` — "ubah ini".
> Ini adalah rekomendasi, bukan pemblokiran.

### 13.4. Sesi, Proxy Panel, dan Proxy Tepercaya (tab "Proxy dan Server" / *Proxy and Server*)

#### Durasi Sesi (*Session Duration*)

- **Kunci:** `sessionMaxAge`
- **Nilai default:** `360` (menit, yaitu 6 jam).
- **Nilai yang diizinkan:** dari `1` hingga `525600` menit (1 tahun).
- **Fungsi:** berapa lama administrator tetap terautentikasi tanpa login ulang. Satuannya — **menit**. Petunjuk: "Durasi sesi dalam sistem (nilai: menit)".

#### Outbound untuk Trafik Panel (*Panel Traffic Outbound*)

- **Kunci:** `panelOutbound`
- **Nilai default:** `""` (kosong = koneksi langsung).
- **Fungsi:** menentukan **outbound** Xray yang digunakan panel untuk mengirimkan **permintaannya sendiri** — pemeriksaan versi dan pengunduhan panel/Xray, permintaan ke Telegram, pembaruan biasa file geo — untuk melewati pemfilteran server GitHub/Telegram. Kolom ini berupa **daftar dropdown**: berisi outbound dari template konfigurasi Xray, outbound dari subscription ke outbound, serta **balancer** rute (dalam grup terpisah). Outbound bertipe `blackhole` dikecualikan dari daftar — mengarahkan unduhan ke "lubang hitam" tidak masuk akal. Petunjuk resminya: "Merutekan permintaan internal panel sendiri — pemeriksaan versi dan unduhan panel/Xray, Telegram, dan pembaruan biasa file geo — melalui outbound Xray ini untuk melewati pemfilteran server GitHub/Telegram. Inbound loopback bridge ditambahkan ke konfigurasi aktif secara otomatis dan diterapkan secara langsung. Pembaruan otomatis Geodata bawaan Xray tidak terpengaruh; ia memiliki outbound sendiri untuk pengunduhan. Biarkan kosong untuk koneksi langsung."

> **Cara kerjanya.** Saat outbound dipilih, panel sendiri menambahkan ke konfigurasi aktif sebuah inbound loopback layanan (SOCKS bridge dengan tag `panel-egress`) dan aturan routing yang mengarahkan trafik HTTP internal panel ke outbound yang dipilih. Jika balancer dipilih, `balancerTag` dimasukkan ke aturan, dan trafik panel didistribusikan di antara anggota-anggotanya. Bridge dan aturan diterapkan **secara langsung**, tanpa restart penuh panel. Biarkan kolom kosong untuk koneksi langsung. Pembaruan otomatis geodata bawaan Xray **tidak terpengaruh** oleh pengaturan ini — ia memiliki outbound sendiri di dalam routing Xray.
- **Format:** `socks5://` (atau `socks5h://`) atau `http(s)://`, dengan otorisasi jika diperlukan dalam bentuk `socks5://user:pass@host:port`. Skema yang didukung secara ketat: `socks5`, `socks5h`, `http`, `https` — skema lain dianggap tidak valid, dan panel akan kembali ke koneksi langsung. Contoh umum — inbound SOCKS lokal Xray itu sendiri.
- Petunjuk resminya: "Merutekan permintaan keluar panel sendiri (pembaruan geo, pemeriksaan versi Xray/panel, Telegram) melalui proxy ini untuk melewati pemfilteran server GitHub/Telegram. Menerima socks5:// atau http(s)://, misalnya inbound SOCKS lokal Xray. Biarkan kosong untuk koneksi langsung."
- Proxy yang tidak valid tidak menyebabkan error saat menyimpan — panel hanya menggunakan koneksi langsung dan mencatat peringatan di log.

**Contoh nilai kolom.** Jika server sudah memiliki inbound SOCKS lokal Xray di port `10808`, arahkan permintaan internal panel melaluinya:

```
socks5://127.0.0.1:10808
```

Untuk proxy HTTP eksternal dengan otorisasi:

```
http://user:pass@proxy.example.com:8080
```

Setelah menyimpan dan me-restart, panel akan mengunduh pembaruan database geo, memeriksa versi, dan menghubungi Telegram melalui proxy yang ditentukan.

#### CIDR Proxy Tepercaya (*Trusted proxy CIDRs*)

- **Kunci:** `trustedProxyCIDRs`
- **Nilai default:** `127.0.0.1/32,::1/128` (hanya localhost).
- **Format:** daftar alamat IP atau subnet CIDR yang dipisahkan koma (misalnya `10.0.0.0/8, 192.168.1.5`). Setiap elemen diverifikasi sebagai IP atau CIDR — nilai yang tidak valid ditolak saat menyimpan.
- **Fungsi:** mencantumkan sumber yang diizinkan untuk menetapkan header `X-Forwarded-Host`, `X-Forwarded-Proto`, dan header IP klien nyata. Petunjuk: "IP/CIDR yang dipisahkan koma, yang diizinkan untuk menetapkan header forwarded host, proto, dan client IP." Perlu dikonfigurasi jika panel beroperasi di belakang reverse proxy (nginx, Caddy, dll.) agar IP klien dan skema teridentifikasi dengan benar.

**Contoh: panel di belakang reverse proxy.** Jika nginx berada di host yang sama dan mem-proxy permintaan ke panel, biarkan kepercayaan hanya ke localhost (nilai default):

```
127.0.0.1/32,::1/128
```

Jika proxy berada di server terpisah di jaringan internal `10.0.0.0/8`, tambahkan subnetnya, jika tidak panel akan mengabaikan header yang dikirim olehnya dan akan melihat IP proxy alih-alih klien nyata:

```
127.0.0.1/32,::1/128,10.0.0.0/8
```

Contoh blok nginx yang sesuai yang meneruskan IP nyata dan skema:

```nginx
proxy_set_header X-Real-IP        $remote_addr;
proxy_set_header X-Forwarded-For  $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header X-Forwarded-Host $host;
```

### 13.5. Bot Telegram (tab "Bot Telegram" / *Telegram Bot*)

#### Aktifkan Bot Telegram (*Enable Telegram Bot*)

- **Kunci:** `tgBotEnable`
- **Tipe/default:** boolean, `false`.
- **Fungsi:** mengaktifkan bot Telegram. Petunjuk: "Akses fitur panel melalui bot Telegram".

#### Token Telegram (*Telegram Token*)

- **Kunci:** `tgBotToken`
- **Default:** `""`.
- **Fungsi:** token bot. Petunjuk: "Anda perlu mendapatkan token dari manajer bot Telegram @botfather".
- **Fitur keamanan:** token termasuk nilai rahasia. Dalam respons panel saat membaca pengaturan, token tidak dikembalikan (kolom dikosongkan, hanya flag "dikonfigurasi/tidak dikonfigurasi" yang dikembalikan). Jika kolom dibiarkan kosong saat menyimpan, token yang tersimpan sebelumnya **tetap disimpan** (tidak dihapus).

#### Bahasa Bot Telegram (*Telegram Bot Language*)

- **Kunci:** `tgLang`
- **Default:** `en-US`.
- **Fungsi:** bahasa pesan bot (terlepas dari bahasa antarmuka web). Daftar bahasa yang tersedia sama dengan bahasa panel.

#### User ID Administrator Bot (*Admin Chat ID*)

- **Kunci:** `tgBotChatId`
- **Default:** `""`.
- **Format:** satu atau beberapa Telegram User ID numerik **dipisahkan koma**.
- **Fungsi:** penerima notifikasi dan administrator yang diizinkan mengelola panel melalui bot. Petunjuk: "Satu atau beberapa User ID administrator bot Telegram. Untuk mendapatkan User ID, gunakan @userinfobot atau perintah '/id' di bot."

#### Frekuensi Notifikasi (*Notification Time*)

- **Kunci:** `tgRunTime`
- **Default:** `@daily` (sekali sehari).
- **Format:** string dalam format **Crontab** (mendukung ekspresi cron standar maupun singkatan seperti `@daily`, `@hourly`, `@every 1h`). Petunjuk: "Tentukan interval notifikasi dalam format Crontab". Mengontrol laporan berkala bot.

**Contoh nilai kolom.**

| Nilai | Kapan bot mengirim laporan |
| --- | --- |
| `@daily` | sekali sehari pada tengah malam (default) |
| `@hourly` | setiap jam |
| `@every 6h` | setiap 6 jam |
| `0 9 * * *` | setiap hari pukul 09:00 |
| `30 8 * * 1` | setiap Senin pukul 08:30 |

Waktu dihitung dalam zona waktu dari pengaturan "Zona Waktu" (p. 13.6).

#### SOCKS Proxy (*SOCKS Proxy*)

- **Kunci:** `tgBotProxy`
- **Default:** `""`.
- **Fungsi:** SOCKS5 proxy khusus untuk koneksi bot ke Telegram. Petunjuk: "Jika Anda membutuhkan proxy Socks5 untuk terhubung ke Telegram, konfigurasikan parameternya sesuai panduan." Berlaku khusus untuk trafik bot (berbeda dari "Proxy Jaringan Panel" umum dari p. 13.4).

#### Telegram API Server (*Telegram API Server*)

- **Kunci:** `tgBotAPIServer`
- **Default:** `""` (gunakan server standar `api.telegram.org`).
- **Format:** URL `http(s)://…`; saat menyimpan, validitas URL diperiksa — alamat yang tidak valid ditolak. Petunjuk: "Server API Telegram yang digunakan. Biarkan kosong untuk menggunakan server default." Diperlukan untuk Telegram Bot API server yang di-deploy sendiri.

#### Notifikasi Bot (grup "Notifikasi" / *Notifications*)

| Kolom | Kunci | Default | Deskripsi |
| --- | --- | --- | --- |
| Pencadangan Database (*Database Backup*) | `tgBotBackup` | `false` | Kirim file cadangan database ke Telegram bersama laporan. Petunjuk: "Kirim notifikasi dengan file cadangan database". |
| Notifikasi Login (*Login Notification*) | `tgBotLoginNotify` | `true` | Beri notifikasi saat ada upaya login ke panel. Petunjuk: "Menampilkan nama pengguna, alamat IP, dan waktu saat seseorang mencoba login ke panel Anda." |
| Jeda Notifikasi Kedaluwarsa Sesi (*Expiration Date Notification*) | `expireDiff` | `0` | Berapa **hari** sebelum masa berlaku klien habis untuk mengirim notifikasi. `0` — dinonaktifkan. Diizinkan `>= 0`. Petunjuk: "Terima notifikasi tentang kedaluwarsa sesi sebelum nilai ambang batas tercapai (nilai: hari)". |
| Ambang Batas Trafik untuk Notifikasi (*Traffic Cap Notification*) | `trafficDiff` | `0` | Ambang batas sisa trafik untuk notifikasi. Petunjuk: "Terima notifikasi tentang trafik yang habis sebelum ambang batas tercapai (nilai: GB)". Diizinkan `0–100`. |
| Ambang Batas Beban CPU (*CPU Load Notification*) | `tgCpu` | `80` | Beri notifikasi kepada administrator jika beban CPU melebihi ambang batas (dalam **%**). Diizinkan `0–100`. Petunjuk: "Beri notifikasi kepada administrator di Telegram jika beban CPU melebihi ambang batas ini (nilai: %)". |

### 13.6. Tanggal dan Waktu (tab "Tanggal dan Waktu" / *Date and Time*)

#### Zona Waktu (*Time Zone*)

- **Kunci:** `timeLocation`
- **Nilai default:** `Local` (zona waktu sistem server).
- **Format:** nama zona dari database IANA tz (misalnya, `Europe/Moscow`, `UTC`, `Asia/Tehran`).
- **Fungsi:** zona waktu tempat panel menjalankan tugas terjadwal (laporan bot, reset/pemeriksaan trafik, kedaluwarsa masa berlaku). Petunjuk: "Tugas terjadwal dijalankan sesuai waktu di zona waktu ini".
- **Validasi:** zona waktu diperiksa saat menyimpan — zona yang tidak ada ditolak. Jika nilai yang tidak valid ditemukan di database di kemudian hari, panel akan kembali ke `Local` saat runtime, dan jika itu pun tidak tersedia — ke `UTC`.

### 13.7. Trafik Eksternal dan Perilaku Xray (tab "Trafik Eksternal" / *External Traffic*)

| Kolom | Kunci | Default | Deskripsi |
| --- | --- | --- | --- |
| Informasi Trafik Eksternal (*External Traffic Inform*) | `externalTrafficInformEnable` | `false` | Beri notifikasi ke API eksternal setiap kali trafik diperbarui. Petunjuk: "Beri notifikasi ke API eksternal setiap kali trafik diperbarui." |
| URI Informasi Trafik Eksternal (*External Traffic Inform URI*) | `externalTrafficInformURI` | `""` | URL tempat panel mengirimkan pembaruan trafik. Melewati pemeriksaan validitas URL saat menyimpan. Petunjuk: "Pembaruan trafik dikirimkan ke URI ini". |
| Restart Xray Setelah Penonaktifan Otomatis (*Restart Xray After Auto Disable*) | `restartXrayOnClientDisable` | `true` | Restart Xray saat klien dinonaktifkan secara otomatis karena masa berlaku habis atau batas trafik terlampaui. Petunjuk: "Saat klien dinonaktifkan secara otomatis karena masa berlaku habis atau batas trafik, restart Xray." **Tombol toggle berada di tab "Panel" (*General*)** — lihat p. 13.2; dicantumkan di sini untuk kelengkapan. |

### 13.8. Lainnya: Template Konfigurasi Xray dan URL Pengujian

#### Template Konfigurasi Xray (*xrayTemplateConfig*)

- **Kunci:** `xrayTemplateConfig`
- **Default:** template JSON bawaan (embedded) yang disertakan dengan build.
- **Fungsi:** template JSON dasar konfigurasi Xray-core, di atas mana panel membangun inbound/outbound. Nilai ini **tidak dikembalikan** dalam output pengaturan biasa dan diedit di halaman konfigurasi Xray terpisah, bukan dalam daftar kolom pengaturan panel umum. Template standar default tersedia melalui `GET /panel/setting/getDefaultJsonConfig`.

#### URL Pengujian Outbound (*xrayOutboundTestUrl*)

- **Kunci:** `xrayOutboundTestUrl`
- **Default:** `https://www.google.com/generate_204`
- **Fungsi:** URL yang digunakan saat memeriksa ketersediaan koneksi outbound. Saat ditetapkan, melewati sanitasi sebagai URL HTTP(S).

### 13.9. Akun Administrator dan Token API

Parameter ini berada di tab terkait ("Akun" / *Authentication*) dan dibahas secara rinci di bagian keamanan; berikut adalah ringkasan singkat kunci-kuncinya.

- **Perubahan kredensial** (kolom "Login Saat Ini", "Kata Sandi Saat Ini", "Login Baru", "Kata Sandi Baru") disimpan dengan permintaan terpisah `POST /panel/setting/updateUser`. Memerlukan login dan kata sandi saat ini yang benar; login dan kata sandi baru tidak boleh kosong. Pesan: "Anda berhasil mengubah kredensial administrator." / "Nama pengguna atau kata sandi salah".
- **Autentikasi dua faktor (2FA)** — kunci `twoFactorEnable` (default `false`) dan rahasia `twoFactorToken`. Token adalah rahasia: saat 2FA diaktifkan, kolom yang dikosongkan saat menyimpan tidak menghapus token yang ada. Saat 2FA **pertama kali** diaktifkan, panel menginvalidasi sesi saat ini (meningkatkan "era login").
- **Token API** dikelola oleh endpoint terpisah (`/panel/setting/apiTokens…`): daftar, pembuatan (`apiTokens/create`), penghapusan, pengaktifan/penonaktifan. Token itu sendiri **hanya ditampilkan sekali saat pembuatan** dan tidak disimpan dalam format yang dapat dibaca: "Salin token ini sekarang. Demi keamanan, token tidak disimpan dalam format yang dapat dibaca dan tidak akan ditampilkan lagi."

Detail mengenai 2FA, kata sandi, sinkronisasi LDAP, dan format subscription (JSON/Clash, fragmentation, noises, mux) dibahas di bagian panduan terpisah yang sesuai.

### 13.10. Perubahan API di 3.3.0 (penting untuk integrasi)

Pada versi 3.3.0, struktur jalur API server berubah. Jika Anda memiliki integrasi eksternal (skrip, bot, panel pusat, tugas CI) yang mengakses panel melalui HTTP, integrasi tersebut **perlu diperbarui**, jika tidak akan berhenti berfungsi.

#### ⚠️ BREAKING CHANGE: endpoint `/panel/setting/*` dan `/panel/xray/*` pindah ke bawah `/panel/api`

Sebelumnya, manajemen pengaturan panel dan konfigurasi Xray berada secara terpisah, di bawah jalur `/panel/setting/*` dan `/panel/xray/*`. Sekarang keduanya terdaftar di dalam grup API umum `/panel/api`. Jalur lama **dihapus sepenuhnya** — permintaan ke jalur tersebut akan mengembalikan 404.

Alasan perubahan ini: seluruh grup `/panel/api` melewati pemeriksaan akses terpadu, artinya endpoint ini sekarang menerima header `Authorization: Bearer <token>` yang sama dengan API lainnya. Token API adalah akses administratif penuh, sehingga seluruh permukaan API menjadi seragam.

**Yang TIDAK berubah:** halaman antarmuka web (rute SPA) `/panel/settings` dan `/panel/xray` tetap di tempatnya — ini hanya tentang endpoint API server.

#### Tabel Korespondensi Jalur (lama → baru)

Prefiks untuk semua jalur di bawah — hanya ditambahkan `api/` setelah `/panel/`.

| Sebelumnya (≤ 3.2.x) | Sekarang (3.3.0) | Metode |
|---|---|---|
| `/panel/setting/all` | `/panel/api/setting/all` | POST |
| `/panel/setting/defaultSettings` | `/panel/api/setting/defaultSettings` | POST |
| `/panel/setting/update` | `/panel/api/setting/update` | POST |
| `/panel/setting/updateUser` | `/panel/api/setting/updateUser` | POST |
| `/panel/setting/restartPanel` | `/panel/api/setting/restartPanel` | POST |
| `/panel/setting/getDefaultJsonConfig` | `/panel/api/setting/getDefaultJsonConfig` | GET |
| `/panel/setting/apiTokens` | `/panel/api/setting/apiTokens` | GET |
| `/panel/setting/apiTokens/create` | `/panel/api/setting/apiTokens/create` | POST |
| `/panel/setting/apiTokens/delete/:id` | `/panel/api/setting/apiTokens/delete/:id` | POST |
| `/panel/setting/apiTokens/setEnabled/:id` | `/panel/api/setting/apiTokens/setEnabled/:id` | POST |
| `/panel/xray/` | `/panel/api/xray/` | POST |
| `/panel/xray/update` | `/panel/api/xray/update` | POST |
| `/panel/xray/getDefaultJsonConfig` | `/panel/api/xray/getDefaultJsonConfig` | GET |
| `/panel/xray/getXrayResult` | `/panel/api/xray/getXrayResult` | GET |
| `/panel/xray/getOutboundsTraffic` | `/panel/api/xray/getOutboundsTraffic` | GET |
| `/panel/xray/resetOutboundsTraffic` | `/panel/api/xray/resetOutboundsTraffic` | POST |
| `/panel/xray/testOutbound` | `/panel/api/xray/testOutbound` | POST |
| `/panel/xray/warp/:action` | `/panel/api/xray/warp/:action` | POST |
| `/panel/xray/nord/:action` | `/panel/api/xray/nord/:action` | POST |
| `/panel/xray/outbound-subs` (dan `/outbound-subs/*`) | `/panel/api/xray/outbound-subs` (dan `/outbound-subs/*`) | GET/POST/DELETE |

Sub-jalur, isi permintaan, dan format respons tidak berubah — hanya **prefiks** yang berubah.

#### Cara Memperbaiki Integrasi yang Ada

1. Temukan semua kemunculan `/panel/setting/` dan `/panel/xray/` dalam skrip/konfigurasi Anda.
2. Ganti prefiks: tambahkan `api/` tepat setelah `/panel/` (misalnya, `/panel/setting/all` → `/panel/api/setting/all`).
3. Isi permintaan, parameter, dan format respons tidak perlu diubah — hanya URL yang berubah.
4. Karena pengaturan dan konfigurasi Xray sekarang berada di bawah `/panel/api`, keduanya dapat (dan harus) diakses menggunakan token API `Authorization: Bearer <token>` yang sama dengan `/panel/api/inbounds/*` dan endpoint lainnya. Ingat middleware CSRF yang diaktifkan untuk seluruh grup `/panel/api`.

**Contoh: membaca semua pengaturan melalui API.** Sebelumnya (≤ 3.2.x):

```bash
curl -sk -X POST "https://panel.example.com:2053/MyPath/panel/setting/all" \
  -H "Authorization: Bearer <token>"
```

Sekarang (3.3.0) — tambahkan `api/` setelah `/panel/`:

```bash
curl -sk -X POST "https://panel.example.com:2053/MyPath/panel/api/setting/all" \
  -H "Authorization: Bearer <token>"
```

Demikian pula restart panel: `POST /panel/api/setting/restartPanel`. Jalur lama `/panel/setting/restartPanel` sekarang akan mengembalikan 404.

#### API Bertipe: Skema dan Dokumentasi (Swagger / OpenAPI)

Di 3.3.0 spesifikasi OpenAPI menjadi bertipe penuh. Sebelumnya respons bertipe dijelaskan dengan objek kosong `{}`; kini komponen dan skema (`components.schemas`) dibuat langsung dari model data. Berkat ini:

- Swagger UI menampilkan model data nyata, bukan placeholder kosong.
- Generator eksternal (`openapi-generator`, dll.) dapat membangun klien siap pakai dalam bahasa yang diperlukan berdasarkan spesifikasi.
- Setiap respons bertipe dilampiri `$ref` ke model tertentu dan disertai contoh respons.

Tempat melihat dokumentasi API:

- **Halaman Swagger bawaan.** Di menu panel — item **"Dokumentasi API"** (rute SPA `/panel/api-docs`). Di sini semua endpoint tercantum secara interaktif dengan deskripsi, isi permintaan, dan contoh respons.
- **Spesifikasi OpenAPI 3.0 mentah** tersedia di `/panel/api/openapi.json`. URL ini dapat langsung dimasukkan ke Postman, Insomnia, atau `openapi-generator`. Spesifikasi tertanam dalam biner pada saat build; saat panel beroperasi dengan `webBasePath` non-standar, kolom `servers` dalam spesifikasi secara otomatis disesuaikan dengan jalur dasar saat ini, agar tombol "Try it out" dan generator eksternal mengarah ke prefiks yang benar.

---

## 14. Bot Telegram

Panel 3X-UI dilengkapi bot Telegram bawaan yang memungkinkan Anda menerima notifikasi tentang status server dan klien, serta mengelola klien tertentu langsung dari messenger. Bot bekerja menggunakan teknologi long polling (pengambilan data Telegram secara berkelanjutan), sehingga tidak memerlukan domain eksternal atau port yang terbuka — cukup akses keluar ke server Telegram.

Bot membedakan dua jenis pengguna:

- **Administrator** — pengguna yang Telegram User ID-nya dicantumkan di pengaturan bot (kolom «User ID администратора бота»). Memiliki akses ke semua fitur: statistik server, backup, manajemen klien, restart Xray.
- **Klien** — pengguna lain yang Telegram User ID-nya terhubung ke klien inbound tertentu (kolom `tgId` pada klien). Hanya dapat melihat informasi langganannya sendiri.

**Contoh: menghubungkan klien ke Telegram.** Agar pengguna dapat menerima statistik langganannya, Telegram User ID numerik pengguna tersebut dicatat di kolom `tgId` klien. Dalam pengaturan JSON klien, tampaknya seperti ini:

```json
{
  "email": "ivan",
  "id": "6f1e6b1a-0c3d-4f2a-9b7e-1a2b3c4d5e6f",
  "tgId": "123456789",
  "enable": true,
  "limitIp": 2,
  "totalGB": 53687091200,
  "expiryTime": 0
}
```

Setelah itu, pengguna dengan User ID `123456789` dapat meminta `/usage ivan` kepada bot dan melihat statistiknya. ID yang sama dapat diatur oleh administrator melalui tombol «👤 Установить пользователя Telegram» di kartu klien — tidak perlu mengedit JSON secara manual.

### 14.1. Mengaktifkan dan mengonfigurasi bot

Semua parameter bot diatur di panel pada bagian **Настройки → Telegram-бот**. Setelah mengubah pengaturan, simpan perubahan dan restart panel — bot diinisialisasi saat server web dimulai.

| Kolom (UI) | Kunci pengaturan | Nilai default | Deskripsi |
|---|---|---|---|
| Включить Telegram бота | `tgBotEnable` | `false` | Tombol utama. Petunjuk: «Доступ к функциям панели через Telegram-бота». Selama dinonaktifkan, bot tidak berjalan dan tugas notifikasi tidak dijadwalkan. |
| Telegram-токен | `tgBotToken` | (kosong) | Token bot. Petunjuk: «Необходимо получить токен у менеджера ботов Telegram @botfather». Tanpa token yang terisi, bot tidak akan berjalan. |
| SOCKS-прокси | `tgBotProxy` | (kosong) | Proxy untuk koneksi ke Telegram. Petunjuk: «Если для подключения к Telegram вам нужен прокси Socks5, настройте его параметры согласно руководству». |
| Telegram API Server | `tgBotAPIServer` | (kosong) | Server API Telegram alternatif. Petunjuk: «Используемый API-сервер Telegram. Оставьте пустым, чтобы использовать сервер по умолчанию». |
| User ID администратора бота | `tgBotChatId` | (kosong) | Satu atau beberapa Telegram User ID administrator, dipisahkan koma. Petunjuk: «Для получения User ID используйте @userinfobot или команду `/id` в боте». |
| Частота уведомлений для администраторов от бота | `tgRunTime` | `@daily` | Jadwal laporan berkala dalam format crontab. Petunjuk: «Укажите интервал уведомлений в формате Crontab». |
| Резервное копирование базы данных | `tgBotBackup` | `false` | Petunjuk: «Отправлять уведомление с файлом резервной копии базы данных». Melampirkan backup ke laporan berkala. |
| Уведомление о входе | `tgBotLoginNotify` | `true` | Petunjuk: «Отображает имя пользователя, IP-адрес и время, когда кто-то пытается войти в вашу панель». |
| Порог нагрузки на ЦП для уведомления | `tgCpu` | `80` | Ambang batas penggunaan CPU dalam persen (validasi 0–100). Petunjuk: «Уведомление администраторов в Telegram, если нагрузка на ЦП превышает этот порог (значение: %)». Jika nilainya 0, pemeriksaan CPU dinonaktifkan. |
| Язык Telegram-бота | — | — | Bahasa yang digunakan bot untuk menyusun semua pesan. |

#### Mendapatkan token melalui @BotFather

1. Buka percakapan dengan **@BotFather** di Telegram.
2. Kirim perintah `/newbot` dan ikuti instruksinya (nama bot dan `username` unik yang diakhiri dengan `bot`).
3. BotFather akan memberikan token dengan format `123456789:AA...`. Salin ke kolom **Telegram-токен**.

#### Mendapatkan User ID administrator

User ID adalah identifikator numerik akun (bukan username). Ada dua cara untuk mengetahuinya:

- Tulis pesan ke bot **@userinfobot**.
- Jalankan bot yang sudah dikonfigurasi dan kirim perintah **`/id`** — bot akan mengembalikan ID Anda.

Masukkan angka yang diperoleh ke kolom **User ID администратора бота**. Untuk menambahkan beberapa administrator, cantumkan ID mereka dipisahkan koma (misalnya, `11111111,22222222`). Setiap ID divalidasi sebagai bilangan bulat; nilai yang tidak valid akan menyebabkan error saat bot dimulai.

**Contoh: nilai kolom «User ID администратора бота».** Satu administrator — cukup satu angka:

```
123456789
```

Dua administrator dipisahkan koma (spasi tidak diperlukan):

```
123456789,987654321
```

Setiap nilai harus berupa bilangan bulat. Format `@username` atau `123 456` (dengan spasi di dalam angka) tidak valid — bot tidak akan berjalan.

#### Proxy

Skema `socks5://`, `http://`, dan `https://` didukung. Jika kolom proxy dikosongkan, bot akan mencoba menggunakan proxy umum panel (jika sudah diatur dan skemanya didukung). URL dengan skema yang tidak didukung atau sintaksis yang tidak valid diabaikan — bot terhubung langsung. Proxy berguna ketika akses langsung ke API Telegram dari server diblokir.

#### Notifikasi email (SMTP)

Selain Telegram, event yang sama dapat diterima melalui email. Kanal ini dikonfigurasi di bagian **Настройки → Email** pada tab **SMTP Settings**:

| Kolom (UI) | Kunci pengaturan | Nilai default | Deskripsi |
|---|---|---|---|
| Enable Email Notifications | `smtpEnable` | `false` | Tombol utama notifikasi email melalui SMTP. |
| SMTP Host | `smtpHost` | (kosong) | Host server SMTP (misalnya, `smtp.gmail.com`). |
| SMTP Port | `smtpPort` | `587` | Port server SMTP. |
| SMTP Username | `smtpUsername` | (kosong) | Nama pengguna untuk autentikasi SMTP. Juga digunakan sebagai alamat pengirim (From). |
| SMTP Password | `smtpPassword` | (kosong) | Kata sandi untuk autentikasi SMTP. Disimpan tersembunyi; jika kata sandi sudah diatur, kolom menampilkan indikator «sudah dikonfigurasi», dan dapat dikosongkan untuk mempertahankan nilai saat ini. |
| Recipients | `smtpTo` | (kosong) | Daftar penerima dipisahkan koma (misalnya, `admin@example.com, ops@example.com`). |
| Encryption | `smtpEncryptionType` | `starttls` | Jenis enkripsi koneksi: `none` (tanpa enkripsi), `starttls` (STARTTLS), atau `tls` (TLS implisit). |

Tombol **Send Test Email** mengirimkan email percobaan dan menampilkan hasil per tahap: **Connection** (koneksi), **Authentication** (autentikasi), dan **Send** (pengiriman). Jika ada masalah, diagnostik menunjukkan di tahap mana error terjadi (misalnya, «Authentication failed — check username and password» atau «Server requires STARTTLS — change encryption type»), sehingga memudahkan penyesuaian parameter.

Pada tab kedua (**Notifications**) dipilih event mana saja yang akan dikirimkan melalui email — dengan kartu-kartu kelompok yang sama seperti untuk Telegram (lihat «Kanal event dan pemilihan notifikasi» di bagian 14.5).

#### Server API Telegram

Secara default, bot menggunakan API Telegram resmi. Di kolom **Telegram API Server** dapat diisi alamat server Bot API sendiri (`telegram-bot-api`). URL diperiksa keamanannya; alamat yang diblokir atau tidak valid diabaikan, dan server default akan digunakan.

### 14.2. Menu utama dan tombol

Menu dipanggil dengan perintah **`/start`**. Tombol-tombol berupa inline keyboard yang dilampirkan ke pesan; rangkaian tombol tergantung pada apakah Anda administrator atau klien.

#### Menu administrator

| Tombol | Tindakan |
|---|---|
| 📊 Отсортированный отчёт об использовании трафика | Menampilkan daftar semua klien, diurutkan berdasarkan traffic, dengan penggunaan masing-masing; email ekstra tanpa data ditandai «❗ Нет результатов». |
| 💻 Состояние сервера | Ringkasan server (lihat bagian 14.5). Tombol «🔄 Обновить» memuat ulang data. |
| Сбросить весь трафик | Mereset penghitung traffic **semua** klien. Meminta konfirmasi («Вы уверены? 🤔»), kemudian menampilkan «✅ Успешно» atau «❌ Неудача» untuk setiap klien, dan di akhir — «🔚 Сброс трафика завершён для всех клиентов». |
| 📂 Бэкап БД | Mengirimkan file database dan `config.json` (lihat bagian 14.6). |
| 📄 Лог банов | Mengirimkan file log alamat IP yang diblokir karena melampaui batas IP. |
| 🔌 Входящие подключения | Ringkasan semua inbound: Remark, port, traffic, jumlah klien, tanggal kedaluwarsa. |
| ⚠️ Скоро конец | Daftar inbound dan klien yang traffic atau masa aktifnya akan segera habis (lihat bagian 14.5). |
| 🖱️ Команды | Menampilkan bantuan perintah administrator. |
| 🟢 Онлайн | Jumlah dan daftar klien yang sedang online; mengetuk email membuka kartu klien. Tombol «🔄 Обновить». |
| 👥 Все клиенты | Membuka pilihan inbound, lalu daftar kliennya — untuk melihat/mengelola. |
| ➕ Новый клиент | Memulai wizard penambahan klien (pilih inbound → draf → konfirmasi). |
| Настройки подписки / индивидуальные ссылки / QR-код | Pilih inbound dan klien untuk mendapatkan tautan langganan, tautan individual, atau kode QR. |

#### Menu klien

Klien memiliki rangkaian tombol yang terbatas:

| Tombol | Tindakan |
|---|---|
| Статистика клиента | Menampilkan data semua langganan yang terhubung ke Telegram User ID klien. |
| 🖱️ Команды | Menampilkan bantuan perintah klien. |
| Настройки подписки | Pilih klien Anda → tautan langganan. |
| Индивидуальные ссылки | Pilih klien Anda → tautan individual. |
| QR-код | Pilih klien Anda → kode QR. |

Jika pengguna tidak memiliki klien dengan Telegram User ID-nya, bot menjawab: «❌ Ваша конфигурация не найдена! 💭 Пожалуйста, попросите администратора использовать ваш Telegram User ID в конфигурации. 🆔 Ваш User ID: …». ID ini perlu diberikan ke administrator agar dimasukkan ke kolom klien.

### 14.3. Perintah bot

Bot memiliki empat perintah terdaftar yang terlihat di menu «/» Telegram:

| Perintah | Deskripsi (dari menu) | Akses | Fungsi |
|---|---|---|---|
| `/start` | Tampilkan menu utama | semua | Sambutan; administrator juga ditampilkan «🤖 Добро пожаловать в бота управления <Host>!» dan menu utama. |
| `/help` | Bantuan bot | semua | Menampilkan sambutan umum dan ajakan memilih menu. |
| `/status` | Periksa status bot | semua | Menjawab «✅ Бот функционирует нормально». |
| `/id` | Tampilkan Telegram ID Anda | semua | Mengembalikan «🆔 Ваш User ID: <code>…</code>». Berguna untuk mengetahui User ID sendiri. |

Selain perintah terdaftar, ada tiga perintah argumen tambahan (tidak muncul di menu «/», tetapi berfungsi):

- **`/usage [Email]`** — pencarian klien berdasarkan email.
  - Untuk **administrator** menampilkan kartu klien lengkap (dengan tombol manajemen).
  - Untuk **klien** hanya menampilkan langganannya sendiri dengan email yang ditentukan (berdasarkan Telegram User ID yang terhubung). Tanpa argumen, bot meminta email: «❗ Пожалуйста, укажите email для поиска».
- **`/inbound [nama koneksi]`** — hanya untuk administrator. Mencari inbound berdasarkan Remark dan menampilkan parameternya beserta statistik semua klien. Tanpa argumen (atau untuk klien) — «❗ Неизвестная команда».
- **`/restart`** — hanya untuk administrator. Restart Xray Core. Kemungkinan jawaban: «✅ Ядро Xray успешно перезапущено», «❗ Xray Core не запущен» (jika inti tidak berjalan), «❗ Ошибка при перезапуске Xray-core. <Ошибка>». Argumen apapun setelah `/restart` akan menghasilkan pesan perintah tidak dikenal dengan petunjuk `/restart`.

Di obrolan grup, perintah dengan format `/perintah@botusername` hanya diproses jika username cocok dengan nama bot saat ini.

Bantuan administrator (tombol «Команды»):

```
🔃 Для перезапуска Xray Core: /restart
🔎 Для поиска клиента по email: /usage [Email]
📊 Для поиска входящих подключений (со статистикой клиентов): /inbound [имя подключения]
🆔 Ваш Telegram User ID: /id
```

Bantuan klien:

```
💲 Для просмотра информации о вашей подписке: /usage [Email]
🆔 Ваш Telegram User ID: /id
```

### 14.4. Manajemen klien (hanya administrator)

Setelah membuka kartu klien (melalui «Все клиенты», «Онлайн», «Скоро конец», atau `/usage`), administrator melihat informasi klien (email, inbound yang terhubung, status «Aktif», status koneksi, tanggal kedaluwarsa, penggunaan traffic) dan tombol manajemen inline:

| Tombol | Fungsi |
|---|---|
| 🔄 Обновить | Muat ulang kartu klien. |
| 📈 Сбросить трафик | Nolkan penghitung traffic klien. Memerlukan konfirmasi «✅ Подтвердить сброс трафика?». |
| 🚧 Лимит трафика | Atur batas traffic. Nilai tersedia: ♾ Безлимит (0), 1/5/10/20/30/40/50/60/80/100/150/200 GB, atau «🔢 Своё» — input angka di keyboard numerik bawaan (tombol 0–9, «🔄» — reset ke 0, «⬅️» — hapus digit terakhir, «✅ Подтвердить: N»). Nilai diatur dalam gigabyte. |
| 📅 Изменить дату окончания | Pilihan tersedia: ♾ Безлимит, «🔢 Своё», tambah 7/10/14/20 hari, 1/3/6/12 bulan. Angka positif memperpanjang masa aktif (menambahkan hari ke tanggal kedaluwarsa saat ini atau ke «sekarang» jika sudah kedaluwarsa); 0 menghapus batas waktu. |
| 🔢 Лог IP | Menampilkan alamat IP klien yang tercatat (dengan cap waktu, jika ada). Dari log tersedia «🔄 Обновить» dan «❌ Очистить IP» (dengan konfirmasi «✅ Подтвердить очистку IP?»). |
| 🔢 Лимит IP | Batasi jumlah IP simultan. Pilihan: ♾ Безлимит (0), 1–10, atau «🔢 Своё» (keyboard numerik). |
| 👤 Установить пользователя Telegram | Menampilkan Telegram User ID klien yang saat ini terhubung; memungkinkan menghapus koneksi («❌ Удалить пользователя Telegram» dengan konfirmasi). Menghubungkan pengguna baru dilakukan melalui pemilihan kontak Telegram sistem. |
| 🔘 Вкл./Выкл. | Mengaktifkan atau menonaktifkan klien. Memerlukan konfirmasi «✅ Подтвердить вкл/выкл пользователя?». |

Semua operasi yang mengubah konfigurasi (batas traffic/IP, tanggal kedaluwarsa, menghubungkan/melepas pengguna Telegram, aktifkan/nonaktifkan) akan menandai Xray untuk restart jika diperlukan agar perubahan berlaku. Setelah operasi berhasil, bot menampilkan konfirmasi berupa «✅ <email>: …» dan menampilkan kembali kartu klien.

Setiap input angka di wizard dibatasi pada nilai < 999999.

### 14.5. Notifikasi dan laporan

Notifikasi dikirimkan ke semua administrator (semua User ID dari `tgBotChatId`).

#### Kanal event dan pemilihan notifikasi

Notifikasi dibangun di atas bus event tunggal, dengan dua kanal pengiriman — **Telegram** dan **email (SMTP)**. Untuk setiap kanal, Anda memilih secara terpisah event mana yang akan diberitahukan. Di **Настройки → Telegram** ini dilakukan pada tab **Notifications**, di **Настройки → Email** — pada tab dengan nama yang sama.

Event dikelompokkan dalam kartu; setiap kelompok memiliki tombol master dengan penghitung event yang diaktifkan (n/total) dan status antara ketika hanya sebagian yang dipilih. Kelompok yang tersedia:

- **Outbound** — «Down» (`outbound.down`) dan «Up» (`outbound.up`): outbound turun dan pulih.
- **Xray Core** — «Crash» (`xray.crash`): inti Xray berhenti secara tidak terduga.
- **Nodes** — «Down» (`node.down`) dan «Up» (`node.up`): node menjadi tidak tersedia atau pulih.
- **System** — «CPU high (%)» (`cpu.high`) dan «Memory high (%)» (`memory.high`): penggunaan CPU dan RAM yang tinggi. Kedua event memiliki kolom ambang batas inline dalam persen di sebelahnya.
- **Security** — «Login attempt» (`login.attempt`): percobaan masuk ke panel.

Kumpulan event yang diaktifkan disimpan secara terpisah: untuk Telegram — di `tgEnabledEvents`, untuk Email — di `smtpEnabledEvents`. Secara default, «Login attempt» dan «CPU high» diaktifkan di kedua kanal (nilai `login.attempt,cpu.high`).

#### Notifikasi login panel

Dikendalikan oleh opsi **Уведомление о входе** (`tgBotLoginNotify`, diaktifkan secara default). Setiap kali ada percobaan masuk ke panel web, administrator menerima pesan:

- Jika berhasil: «✅ Успешный вход в панель.» + host, nama pengguna, IP, waktu.
- Jika gagal: «❗️ Ошибка входа в панель.» + host, **alasan** (misalnya, «Ошибка 2FA» jika faktor kedua salah), nama pengguna, IP, waktu.

#### Penggunaan CPU dan memori yang tinggi

Setiap menit, panel memeriksa penggunaan CPU dan RAM. Jika ambang batas **`tgCpu`** > 0 dan rata-rata penggunaan CPU per menit melebihinya, administrator menerima: «🔴 Загрузка процессора составляет N%, что превышает пороговое значение M%». Secara serupa, penggunaan RAM diperiksa terhadap ambang batas **`tgMemory`** (80% secara default) — event «Memory high (%)».

Kedua ambang batas diatur melalui kolom inline di sebelah event «CPU high (%)» dan «Memory high (%)» dalam kelompok **System** pada tab Notifications (lihat «Kanal event dan pemilihan notifikasi» di atas). Untuk kanal Email, digunakan kunci terpisah `smtpCpu` dan `smtpMemory`. Jika nilai ambang batas 0, pemeriksaan yang bersangkutan dinonaktifkan.

#### Laporan berkala (terjadwal)

Dijadwalkan berdasarkan ekspresi cron dari kolom **Частота уведомлений** (`tgRunTime`, default `@daily`). Jika nilainya kosong atau tidak valid, `@daily` digunakan. Laporan mencakup:

#### Pembuat jadwal

Kolom **Частота уведомлений для администраторов от бота** tidak diisi secara manual sebagai string, melainkan melalui pembuat jadwal. Pertama, mode dipilih dari daftar dropdown:

- **`@every` — ulangi dengan interval** — muncul kolom angka dan pilihan unit (**Секунды** / **Минуты** / **Часы**); hasilnya digabungkan menjadi ekspresi seperti `@every 6h`.
- **`@hourly` — setiap jam**, **`@daily` — setiap hari pukul 00:00**, **`@weekly` — setiap minggu**, **`@monthly` — setiap bulan** — preset siap pakai yang disimpan sebagai makro terkait (`@hourly`, `@daily`, `@weekly`, `@monthly`).
- **Произвольный (crontab)** — kolom untuk ekspresi crontab kustom. Penjadwal panel bekerja dengan detik yang diaktifkan, sehingga ekspresi kustom terdiri dari **6 kolom**: detik, menit, jam, hari dalam bulan, bulan, hari dalam minggu (misalnya, `0 30 8 * * *` — setiap hari pukul 08:30:00). Saat beralih ke mode ini, kolom diisi dengan ekspresi crontab setara dari pilihan saat ini sebagai titik awal.

**Contoh: nilai kolom «Частота уведомлений» (`tgRunTime`).** Singkatan siap pakai maupun format crontab lengkap didukung:

| Nilai | Kapan dijalankan |
|---|---|
| `@daily` | sekali sehari pada tengah malam (nilai default) |
| `@hourly` | setiap jam |
| `@every 6h` | setiap 6 jam |
| `0 9 * * *` | setiap hari pukul 09:00 |
| `0 9 * * 1` | setiap Senin pukul 09:00 |
| `0 */12 * * *` | setiap 12 jam (pukul 00:00 dan 12:00) |

Urutan kolom dalam crontab: menit, jam, hari dalam bulan, bulan, hari dalam minggu.

1. Baris «🕰 Запланированные отчёты: <jadwal>» dan tanggal/waktu saat ini.
2. **Status server** (lihat di bawah).
3. Blok «Скоро конец» untuk inbound dan klien.
4. Notifikasi personal kepada klien yang memiliki Telegram User ID terhubung — setiap klien non-admin menerima daftar langganannya yang traffic atau masa aktifnya akan segera habis (termasuk yang dinonaktifkan).
5. Jika **Резервное копирование базы данных** (`tgBotBackup`) diaktifkan — backup database dikirim ke administrator.

**Status server** berisi: host, versi 3X-UI dan Xray, IPv4/IPv6, uptime (dalam hari), rata-rata beban (Load1/2/3), RAM (saat ini/total), jumlah klien online, penghitung koneksi TCP/UDP, total traffic jaringan (↑/↓), dan status Xray.

**«Скоро конец»** menampilkan:

- untuk inbound: jumlah yang dinonaktifkan dan jumlah yang akan segera habis, lalu daftar inbound tersebut (Remark, port, traffic, tanggal kedaluwarsa);
- untuk klien: hal yang sama, ditambah kartu klien dan tombol dengan email mereka (mengetuk membuka kartu klien).

Ambang batas «akan segera habis» diambil dari pengaturan umum panel: cadangan traffic (dalam GB) dan cadangan masa aktif (dalam hari). inbound/klien dianggap «akan segera habis» jika sisa traffic hingga batas kurang dari ambang batas ATAU sisa waktu hingga tanggal kedaluwarsa kurang dari ambang batas.

### 14.6. Backup dan log

- **Backup database** (tombol «📂 Бэкап БД» atau opsi dalam laporan berkala): bot mengirimkan waktu backup, file database (`x-ui.db`, atau `x-ui.dump` untuk PostgreSQL), dan file konfigurasi Xray `config.json`.
- **Log ban** (tombol «📄 Лог банов»): mengirimkan file log saat ini dan sebelumnya dari alamat IP yang diblokir karena melampaui batas IP. File kosong tidak dikirimkan.

### 14.7. Fitur operasional

- **Pesan panjang** dipecah menjadi beberapa bagian (ambang batas ~2000 karakter), inline keyboard dilampirkan ke bagian terakhir.
- **Konkurensi**: perintah dan penekanan tombol diproses secara bersamaan (pool hingga 10 handler simultan).
- **Keandalan pengiriman**: saat terjadi error koneksi, pesan dikirim ulang dengan penundaan eksponensial (1 detik/2 detik/4 detik, hingga 3 percobaan).
- **Cache**: data «Status server» di-cache agar penekanan «Обновить» yang sering tidak membebani sistem.
- **Restart bot**: saat pengaturan disimpan dan panel di-restart, siklus polling sebelumnya dihentikan dengan benar, dan yang baru dimulai — hanya satu instance penerimaan pembaruan yang berjalan bersamaan.

---

## 15. Basis Geo (geoip / geosite dan kustom)

Basis geo adalah file biner `.dat` yang digunakan Xray-core untuk merutekan dan memfilter lalu lintas berdasarkan kepemilikan negara (rentang IP) atau kategori domain. Panel dapat mengunduh dan memperbarui baik set file geo standar maupun sumber kustom yang ditentukan oleh pengguna melalui URL. Semua file disimpan di direktori `bin` yang berdekatan dengan biner Xray (jalur default `bin`, dapat diganti dengan variabel lingkungan `XUI_BIN_FOLDER`).

### 15.1. Apa itu geoip.dat dan geosite.dat

- **geoip.dat** — basis pemetaan "alamat IP → kode negara/wilayah". Digunakan dalam aturan perutean dalam bentuk `geoip:<kode>`, misalnya `geoip:ru`, `geoip:cn`, serta untuk label khusus `geoip:private` (jaringan privat/lokal). Secara semantis ini menjawab pertanyaan "di negara mana IP ini berada".
- **geosite.dat** — basis pemetaan "domain → kategori/daftar". Digunakan dalam bentuk `geosite:<kategori>`, misalnya `geosite:category-ads-all` (domain iklan), `geosite:google`, `geosite:ru`. Secara semantis ini adalah daftar domain yang dikelompokkan.

File-file ini diperlukan untuk membangun aturan seperti "semua lalu lintas ke IP/domain Rusia — langsung, sisanya — melalui outbound" dan sejenisnya. Aturan itu sendiri dikonfigurasi di bagian perutean Xray; basis geo hanya menyediakan data untuk aturan tersebut. Tanpa file geo yang mutakhir, aturan yang merujuk `geoip:`/`geosite:` tidak akan berfungsi atau akan mengandalkan daftar yang sudah usang.

**Contoh: aturan "domain dan IP Rusia — langsung".** Aturan seperti ini di bagian perutean mengarahkan semua lalu lintas ke sumber daya Rusia ke outbound dengan tag `direct`:

```json
{
  "type": "field",
  "domain": ["geosite:category-ru"],
  "ip": ["geoip:ru"],
  "outboundTag": "direct"
}
```

### 15.2. File geo standar dan pembaruannya

Panel berisi "daftar putih" (allowlist) tetap dari enam file standar dengan sumber unduhan yang telah dikodekan secara permanen. Pembaruan dilakukan melalui `POST /panel/api/server/updateGeofile/:fileName` (atau tanpa nama file — untuk memperbarui semua sekaligus).

**Contoh: memperbarui satu file dan semua sekaligus melalui API.** Memperbarui hanya `geoip_RU.dat`:

```bash
curl -X POST 'https://panel.example.com:2053/panel/api/server/updateGeofile/geoip_RU.dat' \
  -H 'Cookie: 3x-ui=<session-cookie>'
```

Memperbarui semua enam file standar dalam satu permintaan (nama file tidak ditentukan):

```bash
curl -X POST 'https://panel.example.com:2053/panel/api/server/updateGeofile' \
  -H 'Cookie: 3x-ui=<session-cookie>'
```

Respons sukses:

```json
{ "success": true, "msg": "Geofile updated successfully", "obj": null }
```

| Nama file | Sumber (repositori rilis) |
|---|---|
| `geoip.dat` | `github.com/Loyalsoldier/v2ray-rules-dat` (geoip.dat) |
| `geosite.dat` | `github.com/Loyalsoldier/v2ray-rules-dat` (geosite.dat) |
| `geoip_IR.dat` | `github.com/chocolate4u/Iran-v2ray-rules` (geoip.dat) |
| `geosite_IR.dat` | `github.com/chocolate4u/Iran-v2ray-rules` (geosite.dat) |
| `geoip_RU.dat` | `github.com/runetfreedom/russia-v2ray-rules-dat` (geoip.dat) |
| `geosite_RU.dat` | `github.com/runetfreedom/russia-v2ray-rules-dat` (geosite.dat) |

Kekhususan pembaruan file standar:

- **Tombol pembaruan satu file.** Sebelum mengunduh, ditampilkan konfirmasi: "Do you really want to update the geofile? This will update the #filename# file." Jika berhasil, muncul notifikasi "Geofile updated successfully".
- **Tombol "Update all"** mengunduh semua enam file. Konfirmasi: "This will update all geofiles."
- **Unduhan bersyarat.** Jika file lokal sudah ada, header `If-Modified-Since` dengan waktu modifikasi file disertakan dalam permintaan. Respons server `304 Not Modified` berarti file tidak berubah — file tidak diunduh ulang, hanya cap waktu file yang diperbarui.
- **Keamanan nama file.** Hanya nama-nama dari allowlist yang diterima; nama diperiksa untuk memastikan tidak mengandung `..`, pemisah jalur `/` dan `\`, jalur absolut, dan harus sesuai pola `^[a-zA-Z0-9._-]+\.dat$`. Nama apa pun di luar daftar ditolak dengan kesalahan "Invalid geofile name".
- **Restart Xray.** Setelah mengunduh file geo, Xray-core di-restart agar membaca ulang basis yang diperbarui. Jika restart gagal, pesan kesalahan yang sesuai ditambahkan.

#### Memperbarui basis geo dari baris perintah (x-ui)

Basis geo juga dapat diperbarui tanpa panel — melalui menu interaktif `x-ui` (item pembaruan file geo) atau dengan perintah non-interaktif `x-ui update-all-geofiles`. Untuk setiap file dalam set (geoip/geosite, termasuk set IR dan RU) ditampilkan status terpisah: "diperbarui", "sudah terkini", atau "gagal mengunduh". Jika pengunduhan gagal, pesan sukses palsu tidak dicetak. Restart Xray (dan pemutusan koneksi aktif) hanya terjadi jika setidaknya satu file benar-benar telah diperbarui; jika tidak ada file yang berubah (semua mengembalikan `304 Not Modified`), panel dan Xray tidak di-restart.

### 15.3. Pembaruan otomatis data geo melalui Xray (Geodata Auto-Update)

Sumber `.dat` tambahan dari URL sembarang tidak ditambahkan melalui fasilitas panel, melainkan melalui seksi native `geodata` Xray-core. Seksi yang bersangkutan ditempatkan di jendela modal pembaruan Xray (Dashboard → pembaruan Xray, `xrayUpdates`) — ini adalah tab "Geodata Auto-Update". Panel di sini hanya mengedit kunci `geodata` dalam template konfigurasi Xray; pengunduhan, verifikasi, dan pemuatan ulang file secara langsung ditangani oleh inti Xray itu sendiri.

Di bagian atas seksi ditampilkan petunjuk: "Xray downloads these files on schedule and hot-reloads them without a restart. URLs must be HTTPS. Each file must already exist in the bin folder once before Xray can update it."

#### Kolom dan field seksi

- **Schedule (cron)** — string cron 5 field; nilai default `0 4 * * *` (setiap hari pukul 04:00). Saat menyimpan, diperiksa bahwa string berisi tepat 5 field, jika tidak ditampilkan kesalahan "Cron must contain 5 fields, e.g. 0 4 * * *".
- **Download through outbound (optional)** — daftar dropdown dengan tag outbound yang tersedia (plus outbound langganan), yang melaluinya Xray akan mengunduh file; outbound dengan protokol `blackhole` tidak masuk ke daftar. Field ini boleh dikosongkan — dalam hal ini koneksi langsung digunakan. Pilihan ini tidak bergantung pada outbound untuk permintaan panel sendiri (lihat §11): pembaruan otomatis geodata memiliki outbound tersendiri untuk pengunduhan.
- **Daftar file** — setiap baris menentukan pasangan "URL + File name". URL harus dimulai dengan `https://` (jika tidak: "Each file needs an HTTPS URL."). Nama file ditentukan secara sederhana, tanpa jalur dan pemisah — hanya karakter `^[A-Za-z0-9._-]+$` (jika tidak: "File name must be simple, e.g. geosite_custom.dat (no paths)."). Saat memasukkan URL, panel mencoba mengisi nama file secara otomatis dari segmen jalur terakhir. Tombol "Add file" menambah baris, tombol keranjang menghapusnya.

Jika daftar kosong, ditampilkan petunjuk: "No files configured. Reference files in routing rules as ext:geosite_custom.dat:category."

#### Menyimpan

Tombol "Save & Restart Xray" menampilkan konfirmasi "Save geodata settings?" dengan penjelasan "This updates the Xray config template and restarts Xray." Setelah menyimpan, kunci `geodata` ditulis ke template konfigurasi (`POST /panel/api/xray/update`) dan Xray di-restart (`POST /panel/api/server/restartXrayService`). Jika daftar file kosong, kunci `geodata` dihapus dari template.

Hal-hal penting:

- **File harus sudah ada di `bin`.** Xray hanya memperbarui file `.dat` yang sudah ada di folder `bin` saat startup. Oleh karena itu, file kustom baru pertama-tama ditempatkan ke `bin` secara manual (atau setidaknya dibuat di sana versi kosong/usang dengan nama yang diinginkan), dan baru setelah itu Xray mulai memeliharanya agar tetap terkini sesuai jadwal.
- **Pemuatan ulang langsung (hot-reload).** Setelah pengunduhan terjadwal, Xray membaca ulang basis yang diperbarui tanpa me-restart proses secara penuh.
- **Kompatibilitas.** File geo yang sebelumnya diunduh (baik standar maupun kustom) terus bekerja dalam aturan perutean dengan sintaks `ext:` tanpa perubahan.

Jika daftar kosong, ditampilkan petunjuk: "No custom geo sources yet — click Add to create one".

#### Kolom tabel dan field sumber

| Field (UI) | JSON | Nilai default | Keterangan |
|---|---|---|---|
| Type | `type` | — (wajib) | Jenis sumber daya: hanya `geosite` atau `geoip`. Menentukan nama file hasil akhir. |
| Alias | `alias` | — (wajib) | Pengenal singkat sumber. Nama file dibentuk dari alias dan type. |
| URL | `url` | — (wajib) | Tautan langsung ke file `.dat` (http/https). |
| Enabled | — | — | Tanda aktif sumber dalam daftar. |
| Last updated | `lastUpdatedAt` | `0` | Waktu pembaruan terakhir yang berhasil (waktu Unix; `0` — belum pernah diperbarui). |
| Routing (ext:…) | — | — | String siap pakai untuk aturan perutean: `ext:<file.dat>:tag`. |
| Actions | — | — | Tombol "Edit", "Delete", "Update now". |

Selain itu, field layanan berikut disimpan dalam basis data: `localPath` (jalur aktual ke file di direktori `bin`), `lastModified` (nilai header `Last-Modified` dari server, digunakan untuk unduhan bersyarat), `createdAt` dan `updatedAt`.

#### Penamaan file

Nama file hasil akhir dibentuk secara otomatis dari type dan alias:

- type `geoip` → `geoip_<alias>.dat`;
- type `geosite` → `geosite_<alias>.dat`.

Misalnya, sumber dengan type `geosite` dan alias `myads` akan membuat file `geosite_myads.dat`.

**Contoh: menambahkan sumber melalui API.** Menambahkan daftar domain iklan kustom sebagai sumber daya `geosite` dengan alias `myads`:

```bash
curl -X POST 'https://panel.example.com:2053/panel/api/server/customGeo/add' \
  -H 'Cookie: 3x-ui=<session-cookie>' \
  -H 'Content-Type: application/json' \
  -d '{
    "type": "geosite",
    "alias": "myads",
    "url": "https://example.com/lists/myads.dat"
  }'
```

Panel akan mengunduh file ke direktori `bin` sebagai `geosite_myads.dat`, menyimpan catatan, dan me-restart Xray.

#### Tombol dan tindakan

- **Add** — membuka formulir "Add custom geo". Tombol simpan — "Save". API: `POST /add`.
- **Edit** — formulir "Edit custom geo". API: `POST /update/:id`. Saat type atau alias berubah, file lama dihapus dan yang baru diunduh ulang.
- **Delete** — konfirmasi "Delete this custom geo source?". Menghapus catatan dari basis data dan file `.dat` itu sendiri. API: `POST /delete/:id`. Jika berhasil: "Pользовательский geo-файл «<nama>» удалён" — file geo kustom "<nama>" telah dihapus.
- **Update now** — mengunduh ulang sumber tertentu dan memperbarui cap waktu. API: `POST /download/:id`. Jika berhasil: "Geofile «<nama>» diperbarui".
- **Update all** — memperbarui semua sumber kustom sekaligus. API: `POST /update-all`. Jika semua berhasil: "All custom geo sources updated". Jika setidaknya satu sumber gagal diperbarui, operasi dianggap sebagian gagal dengan pesan "One or more custom geo sources failed to update", dan dalam respons dicantumkan sumber yang berhasil dan yang gagal.

Setelah tindakan apa pun (penambahan, pengeditan, penghapusan, pembaruan, pembaruan semua jika ada yang berhasil) Xray-core di-restart.

#### Langkah demi langkah: menambahkan sumber

1. Klik "Add".
2. Di field "Type", pilih `geosite` atau `geoip`.
3. Di field "Alias", masukkan pengenal (hanya huruf latin kecil, angka, `-` dan `_`; placeholder petunjuk: `a-z 0-9 _ -`).
4. Di field "URL", tentukan tautan langsung ke file `.dat` (harus dimulai dengan `http://` atau `https://`).
5. Klik "Save". Panel akan segera mengunduh file ke direktori `bin`, menyimpan catatan, dan me-restart Xray.

### 15.4. Validasi dan batasan

Saat membuat dan mengubah sumber, pemeriksaan ketat dilakukan. Pesan kesalahan:

| Kondisi | Pesan (ID) | Pesan (EN) |
|---|---|---|
| Type bukan `geosite`/`geoip` | Type harus geosite atau geoip | *Type must be geosite or geoip* |
| Alias kosong | Tentukan alias | *Alias is required* |
| Karakter tidak diizinkan dalam alias (bukan `^[a-z0-9_-]+$`) | Alias mengandung karakter yang tidak diizinkan | *Alias must match allowed characters* |
| Alias dicadangkan | Alias ini dicadangkan | *This alias is reserved* |
| URL kosong | Tentukan URL | *URL is required* |
| URL tidak dapat diurai | URL tidak valid | *URL is invalid* |
| Skema bukan http/https | URL harus menggunakan http atau https | *URL must use http or https* |
| Host kosong/tidak valid, atau diblokir proteksi SSRF | Host URL tidak valid | *URL host is invalid* |
| Duplikat "type + alias" | Alias ini sudah digunakan untuk type ini | *This alias is already used for this type* |
| Sumber tidak ditemukan | Sumber tidak ditemukan | *Custom geo source not found* |
| Kesalahan pengunduhan | Gagal mengunduh | *Download failed* |

Petunjuk dalam formulir (validasi di sisi klien): "Alias may only contain lowercase letters, digits, - and _" dan "URL must start with http:// or https://".

Batasan teknis tambahan:

- **Alias yang dicadangkan.** Alias yang berkonflik dengan file standar tidak dapat digunakan. Yang dicadangkan (perbandingan tidak peka huruf besar-kecil, tanda hubung disamakan dengan garis bawah): `geoip`, `geosite`, `geoip_ir`, `geosite_ir`, `geoip_ru`, `geosite_ru`. Misalnya, `geosite-ru` akan ditolak sebagai `geosite_ru`.
- **Proteksi SSRF.** Host URL di-resolve ke IP, dan jika mengarah ke alamat privat/internal, pengunduhan diblokir (pengguna melihat "Host URL tidak valid"). Ini mencegah panel digunakan untuk mengakses layanan internal.
- **Proteksi path traversal.** Jalur akhir file harus berada di dalam direktori `bin` (dengan resolusi symlink); upaya keluar dari batasnya ditolak.
- **Ukuran file minimum.** File yang diunduh dianggap valid hanya jika tidak kurang dari 64 byte; file yang terlalu kecil ditolak dengan kesalahan unduhan.
- **Proxy dan unduhan bersyarat.** Jika proxy dikonfigurasi dalam pengaturan panel, pengunduhan dilakukan melaluinya; dalam kasus lain, koneksi langsung dengan transport aman SSRF digunakan. Seperti untuk file standar, `If-Modified-Since`/`304 Not Modified` diterapkan (file yang tidak berubah tidak diunduh ulang). Batas waktu pengunduhan — 10 menit, pemeriksaan ketersediaan URL (HEAD, jika perlu — GET parsial) — 12 detik.

### 15.5. Pemeriksaan otomatis saat panel dijalankan

Saat startup, panel memeriksa semua sumber kustom dan untuk masing-masing memeriksa keberadaan dan integritas file lokal (file tidak ada, merupakan direktori, atau berukuran kurang dari 64 byte). Jika file tidak ada atau rusak, pemeriksaan sumber dilakukan dan pengunduhan ulang dicoba. Ini memastikan bahwa setelah instalasi ulang atau kehilangan direktori `bin`, file geo kustom akan dipulihkan secara otomatis.

### 15.6. Penggunaan basis geo dalam aturan perutean

Dalam aturan perutean Xray, basis geo digunakan di field seperti `domain`/`ip` melalui prefix:

- **geoip:** untuk basis IP — `geoip:<kode>`. Contoh: `geoip:ru`, `geoip:cn`, `geoip:private`. Diambil dari `geoip.dat` (atau `geoip_RU.dat` dan sejenisnya, jika aturan menunjuk ke file tertentu).
- **geosite:** untuk basis domain — `geosite:<kategori>`. Contoh: `geosite:category-ads-all`, `geosite:google`, `geosite:ru`. Diambil dari `geosite.dat`.

**Contoh: pemblokiran iklan melalui geosite.** Aturan yang mengirimkan semua domain iklan ke "lubang hitam" (diasumsikan outbound dengan tag `blocked` dan protokol `blackhole`):

```json
{
  "type": "field",
  "domain": ["geosite:category-ads-all"],
  "outboundTag": "blocked"
}
```

Untuk file **kustom**, digunakan sintaks file eksternal `ext:`. Petunjuk di UI: "In routing rules use the value column as ext:file.dat:tag (replace tag)." Formatnya:

```
ext:<nama_file.dat>:<tag>
```

di mana `<nama_file.dat>` adalah `geoip_<alias>.dat` atau `geosite_<alias>.dat`, dan `<tag>` adalah daftar/kategori tertentu di dalam file. Panel di kolom "Routing (ext:…)" menampilkan template siap pakai seperti `ext:geosite_myads.dat:tag` — tinggal ganti `tag` dengan tag yang diinginkan. Nama file tersebut ditentukan di bagian "Geodata Auto-Update" (lihat §15.3) di field "File name" — misalnya `geosite_custom.dat`; dirujuk dalam aturan sebagai `ext:geosite_custom.dat:category`.

**Contoh: aturan berbasis file kustom.** Jika sumber dengan type `geosite` dan alias `myads` ditambahkan, dan di dalam file `.dat` daftarnya diberi tag `ads`, aturan peruteannya terlihat seperti ini:

```json
{
  "type": "field",
  "domain": ["ext:geosite_myads.dat:ads"],
  "outboundTag": "blocked"
}
```

Untuk sumber IP (type `geoip`, alias `mycorp`, tag `office`) fieldnya adalah `"ip": ["ext:geoip_mycorp.dat:office"]`.

---

## 16. Operasional: Backup, Log, Pembaruan, CLI

Bagian ini mencakup pemeliharaan panel sehari-hari: membuat dan memulihkan cadangan database, melihat log panel dan Xray, me-restart dan menghentikan layanan, memperbarui Xray dan panel itu sendiri, tugas berkala (cron), dan menghapus panel. Sebagian operasi dilakukan dari antarmuka web (tab di halaman «Dashboard» dan «Pengaturan Panel»), sebagian lagi dari menu konsol `x-ui` di server.

### 16.1. Backup dan Pemulihan Database

Semua data panel (inbound, klien, grup, node, pengaturan) tersimpan dalam satu database. Manajemen backup tersedia di halaman **«Dashboard»** pada tab **«Cadangan»**, dengan judul blok **«Backup dan Pemulihan»**.

Panel mendukung dua mesin database, dan perilaku backup bergantung pada pilihan tersebut:

- **SQLite** (pilihan default) — data tersimpan dalam file `x-ui.db`.
- **PostgreSQL** — jika panel dikonfigurasi menggunakan PostgreSQL, blok ini menampilkan petunjuk:
  > «Panel ini berjalan di PostgreSQL. «Cadangan» mengunduh arsip pg_dump (.dump), sedangkan «Pemulihan» mengunggahnya kembali melalui pg_restore. Alat klien PostgreSQL (pg_dump dan pg_restore) harus terinstal di server.»

#### Ekspor (membuat salinan)

Tombol **«Ekspor database»** (inggris: `Back Up`) mengunduh file cadangan ke perangkat Anda.

| Mesin Database | Nama File | Yang Terjadi di Server |
|----------------|-----------|------------------------|
| SQLite | `x-ui.db` | WAL checkpoint dijalankan terlebih dahulu agar file berisi catatan terbaru, lalu file dibaca seluruhnya dan dikirim untuk diunduh |
| PostgreSQL | `x-ui.dump` | `pg_dump` dijalankan, arsipnya dikirim untuk diunduh |

Petunjuk di antarmuka:
- SQLite: «Klik untuk mengunduh file .db yang berisi cadangan database Anda saat ini ke perangkat Anda.»
- PostgreSQL: «Klik untuk mengunduh dump PostgreSQL (.dump) dari database saat ini ke perangkat Anda.»

Secara teknis, ekspor adalah permintaan `GET /panel/api/server/getDb`. Nama lampiran dibentuk oleh server (`Content-Disposition`) tergantung mesin database yang digunakan.

Nama file cadangan dibentuk berdasarkan alamat server, bukan tetap `x-ui.db` / `x-ui.dump`. Saat diunduh dari browser, nama diambil dari alamat panel di bilah alamat (host permintaan); jika tidak tersedia, diambil dari domain web yang dikonfigurasi; jika domain web tidak ada, diambil dari IP publik server (IPv4 terlebih dahulu, lalu IPv6), dengan fallback ke `x-ui`. Dengan cara ini, backup dari server yang berbeda mudah dibedakan. Ekstensi tetap `.db` untuk SQLite dan `.dump` untuk PostgreSQL; backup melalui Telegram juga diberi nama berdasarkan domain/IP yang sama.

**Contoh: mengunduh backup melalui API.** Ekspor yang sama dapat diperoleh melalui permintaan dari konsol — misalnya, untuk skrip backup otomatis. Diperlukan sesi yang diautentikasi (cookie login):

```bash
# 1) Login dan simpan cookie sesi
curl -s -c cookies.txt \
     -d 'username=admin&password=admin' \
     https://panel.example.com:2053/panel/login

# 2) Unduh file database (nama ditentukan server: x-ui.db atau x-ui.dump)
curl -s -b cookies.txt -OJ \
     https://panel.example.com:2053/panel/api/server/getDb
```

Jika panel diakses melalui base path (Web Base Path), tambahkan ke URL: `…:2053/<base_path>/panel/api/server/getDb`.

#### Impor (pemulihan)

Tombol **«Impor database»** (inggris: `Restore`) membuka pemilih file dan mengunggahnya ke server untuk dipulihkan (`POST /panel/api/server/importDB`, field formulir `db`).

Petunjuk di antarmuka:
- SQLite: «Klik untuk memilih dan mengunggah file .db dari perangkat Anda guna memulihkan database dari cadangan.»
- PostgreSQL: «Klik untuk memilih dan mengunggah file .dump guna memulihkan database PostgreSQL. Ini akan menggantikan semua data saat ini.»

**Proses impor untuk SQLite (penting untuk dipahami: bersifat atomik dan mendukung rollback):**
1. File yang diunggah diperiksa formatnya — harus berupa database SQLite yang valid; jika tidak, dikembalikan error «Invalid db file format».
2. File disimpan sementara sebagai `x-ui.db.temp` dan menjalani pemeriksaan integritas.
3. **Xray dihentikan** sebelum database diganti.
4. Database saat ini diganti namanya menjadi cadangan `x-ui.db.backup` (fallback).
5. File sementara dipindahkan ke posisi database aktif, dilakukan inisialisasi dan migrasi skema, kemudian migrasi inbound.
6. **Jika langkah mana pun gagal** — rollback dilakukan: database lama dipulihkan dari `x-ui.db.backup`, dan Xray di-restart menggunakan data lama.
7. Jika berhasil, file fallback dihapus, dan **Xray di-restart otomatis** dengan data yang telah dipulihkan.

Pesan antarmuka berdasarkan hasil:

| Hasil | Teks |
|-------|------|
| Berhasil | «Database berhasil diimpor» |
| Error impor | «Terjadi kesalahan saat mengimpor database» |
| Error membaca file | «Terjadi kesalahan saat membaca database» |

> Pemulihan sepenuhnya menggantikan data saat ini. Karena Xray berhenti sejenak selama proses berlangsung, koneksi klien yang ada akan terputus sementara selama impor.

#### File migrasi antar mesin database (SQLite ⇄ PostgreSQL)

Terpisah dari backup biasa, terdapat fungsi **«Unduh File Migrasi»** (`Download Migration`, permintaan `GET /panel/api/server/getMigration`). Fungsi ini menghasilkan file portabel untuk berpindah ke mesin database lain:

| Mesin Saat Ini | Yang Diunduh | Nama File | Tujuan |
|----------------|--------------|-----------|--------|
| SQLite | Dump SQL portabel (teks) | `x-ui.dump` | Mengisi PostgreSQL dengan data Anda |
| PostgreSQL | Database SQLite yang dibangun dari data PostgreSQL | `x-ui.db` | Mengembalikan panel ke SQLite |

Petunjuk:
- Pada SQLite: «Klik untuk mengunduh ekspor .dump portabel (teks SQL) dari database SQLite Anda.»
- Pada PostgreSQL: «Klik untuk mengunduh database SQLite (.db) yang dibangun dari data PostgreSQL Anda dan siap untuk menjalankan panel di SQLite.»

Konversi `.db ⇄ .dump` untuk SQLite juga dapat dilakukan dari CLI menggunakan perintah `x-ui migrateDB [file]` (lihat bagian 16.7).

#### Backup melalui bot Telegram

Jika bot Telegram telah dikonfigurasi (lihat bagian tentang notifikasi), bot dapat mengirimkan cadangan langsung ke obrolan administrator. Backup melalui Telegram menyertakan **dua file**: database itu sendiri (`x-ui.db`, atau `x-ui.dump` untuk PostgreSQL) dan konfigurasi Xray `config.json`. Pesan didahului dengan baris «🗄 Waktu backup: …».

Ada dua cara menerima backup di Telegram:

1. **Sesuai permintaan.** Tombol **«📂 Backup DB»** di menu bot — bot segera mengirimkan file ke obrolan saat ini.
2. **Otomatis bersama laporan.** Di pengaturan bot terdapat sakelar **«Backup Database»** (`Database Backup`) dengan deskripsi «Kirim notifikasi dengan file cadangan database». Ketika diaktifkan, setiap kali laporan berkala dikirimkan, bot akan mengirimkan cadangan kepada semua administrator setelah laporan. Periode pengiriman laporan diatur oleh jadwal cron bot (lihat bagian 16.6). Bot memberikan jeda antar file dan antar administrator agar tidak melampaui batas Telegram.

> Backup melalui bot hanya dikirimkan jika bot sedang berjalan; pada PostgreSQL, backup ini juga memerlukan keberadaan `pg_dump` di server.

### 16.2. Melihat Log

Panel memiliki dua alat penampil log yang independen, keduanya dapat diakses dari tab **«Log»** di «Dashboard». Setiap jendela dapat diperbarui (ikon «refresh» di header) dan mengunduh tampilan saat ini ke file `x-ui.log` (tombol dengan ikon unduhan).

#### Log Panel (aplikasi / syslog)

Jendela log panel (`POST /panel/api/server/logs/{count}`). Kontrol yang tersedia:

| Elemen | Nilai Default | Deskripsi |
|--------|---------------|-----------|
| Jumlah baris | `20` | Daftar tarik-turun: 10 / 20 / 50 / 100 / 500 |
| Level | `Info` | Level minimum: Debug / Info / Notice / Warning / Error |
| SysLog (centang) | dinonaktifkan | Sumber log: dari buffer aplikasi atau dari jurnal sistem |

Perilakunya tergantung pada centang **SysLog**:

- **Dinonaktifkan (default):** log diambil dari buffer ring internal panel, difilter berdasarkan level yang dipilih. Entri ditampilkan dengan level (DEBUG / INFO / NOTICE / WARNING / ERROR) dan sumber: `X-UI:` — pesan dari panel itu sendiri, `XRAY:` — pesan yang diteruskan dari Xray.
- **Diaktifkan:** panel menjalankan `journalctl -u x-ui --no-pager -n <count> -p <level>` di server, yaitu menampilkan jurnal sistem layanan `x-ui`. Jumlah baris yang diizinkan: 1 hingga 10000; level menerima nilai syslog (`emerg/0`, `alert/1`, `crit/2`, `err/3`, `warning/4`, `notice/5`, `info/6`, `debug/7`). Di Windows, mode SysLog tidak didukung — akan muncul peringatan bahwa centang harus dihilangkan dan log aplikasi yang digunakan. Jika `systemd`/layanan tidak tersedia, akan muncul pesan error saat menjalankan `journalctl`.

**Contoh: jurnal yang sama dari konsol server.** Ketika panel tidak dapat diakses (misalnya, tidak dapat dimulai), jurnal sistem dapat dibaca langsung — ini persis perintah yang dijalankan panel dalam mode SysLog:

```bash
# 100 baris terakhir dengan level warning ke atas
journalctl -u x-ui --no-pager -n 100 -p warning

# Memantau jurnal secara real-time
journalctl -u x-ui -f
```

> Level di jendela ini memfilter **keluaran**. Level minimum apa yang sebenarnya ditulis ke konsol/syslog ditentukan oleh level logging panel (variabel lingkungan, default `Info`; ke file, panel selalu menulis pada level `DEBUG`).

#### Log Xray (log akses)

Jendela terpisah untuk access-log Xray (`POST /panel/api/server/xraylogs/{count}`). Jendela ini mengurai baris jurnal akses Xray dan menampilkannya dalam tabel: **Date, From, To, Inbound, Outbound, Email**.

| Elemen | Nilai Default | Deskripsi |
|--------|---------------|-----------|
| Jumlah baris | `20` | 10 / 20 / 50 / 100 / 500 |
| **Filter** | kosong | Pencarian teks berdasarkan substring (diterapkan dengan menekan Enter) |
| **Direct** (centang) | diaktifkan | Tampilkan koneksi langsung (traffic melalui freedom-outbound) |
| **Blocked** (centang) | diaktifkan | Tampilkan koneksi yang diblokir (traffic ke blackhole-outbound) |
| **Proxy** (centang) | diaktifkan | Tampilkan traffic yang diproksikan |

Jenis kejadian ditentukan secara otomatis berdasarkan tag koneksi outbound dalam baris log: yang sesuai dengan tag freedom → «DIRECT» (hijau), blackhole → «BLOCKED» (merah), yang lain → «PROXY» (biru). Baris `api -> api` dan baris kosong dilewati.

> Agar jendela ini menampilkan entri, Xray harus mengaktifkan **log akses** dengan jalur ke file (bukan `none`) — lihat di bawah. Jika access-log dinonaktifkan atau file tidak dapat diakses, jendela akan kosong («No Record...»).

### 16.3. Level dan Konfigurasi Logging Xray

Parameter logging Xray itu sendiri dikonfigurasi di halaman **«Konfigurasi Xray»** dalam blok **«Log»** (`Log`) dengan peringatan:
> «Log dapat memperlambat kinerja server. Aktifkan hanya jenis log yang Anda butuhkan bila diperlukan!»

| Kolom | Terjemahan | Nilai Default | Deskripsi |
|-------|-----------|---------------|-----------|
| **Level log** (`logLevel`) | Log Level | `warning` | Level detail log error Xray. Nilai yang diizinkan: `debug`, `info`, `notice`, `warning`, `error`. Petunjuk: «Level log untuk log error, menunjukkan informasi yang perlu dicatat.» |
| **Log akses** (`accessLog`) | Access Log | `none` | Jalur ke file log akses. Nilai khusus `none` menonaktifkan log akses. Petunjuk: «Jalur ke file log akses. Nilai khusus «none» menonaktifkan log akses.» |
| **Log error** (`errorLog`) | Error Log | kosong (jalur default) | Jalur ke file log error; `none` menonaktifkannya. Petunjuk: «Jalur ke file log error. Nilai khusus «none» menonaktifkan log error.» |
| **Log DNS** (`dnsLog`) | DNS Log | `false` (nonaktif) | Aktifkan logging permintaan DNS. Petunjuk: «Aktifkan log permintaan DNS». |
| **Masking alamat** (`maskAddress`) | Mask Address | kosong (nonaktif) | Saat diaktifkan, alamat IP asli secara otomatis diganti dengan alamat palsu dalam log. Petunjuk: «Saat diaktifkan, alamat IP asli diganti dengan alamat palsu dalam log.» |

> Karena secara default **«Log akses» = `none`**, jendela «Log Xray» (bagian 16.2) awalnya kosong. Agar berfungsi, tentukan jalur ke access-log di sini dan restart Xray.

> Perhatikan: access-log kosong hanya memengaruhi jendela ini. Daftar klien online di «Dashboard» dan batas jumlah IP di formulir klien **tidak bergantung** pada access-log — panel menentukan klien online dan menghitung alamat IP mereka melalui API statistik online inti Xray (statistik koneksi). Pada versi inti lama yang tidak memiliki API ini, panel secara otomatis beralih ke metode lama (membaca access-log), dan dalam kasus itu jalur ke access-log di sini tetap diperlukan untuk batas IP.

> **Batas jumlah IP dan fail2ban.** Pembatasan jumlah IP klien itu sendiri (kolom «IP Limit» di formulir klien dan saat penambahan massal) hanya berlaku di server jika **fail2ban** terinstal — dialah yang memblokir alamat yang melebihi batas. Panel memeriksa keberadaan fail2ban (`GET /panel/api/server/fail2banStatus`); jika tidak ada, kolom «IP Limit» menjadi tidak tersedia dengan petunjuk penjelasan (di Windows — dengan pesan terpisah), dan batas yang sebelumnya ditetapkan di server tersebut secara otomatis diatur ke nol karena tidak berlaku. Pemblokiran fail2ban berlaku untuk TCP maupun UDP. Di server biasa, fail2ban kini diinstal secara otomatis saat instalasi dan pembaruan panel (lihat bagian 16.5).

**Contoh: blok `log` yang akan membuat jendela «Log Xray» menampilkan entri.** Dalam konfigurasi JSON Xray tampilannya seperti ini:

```json
{
  "log": {
    "loglevel": "warning",
    "access": "./access.log",
    "error": "",
    "dnsLog": false,
    "maskAddress": ""
  }
}
```

Yang terpenting — ganti `"access": "none"` dengan jalur ke file (misalnya, `"./access.log"`). Setelah disimpan, restart Xray, dan tabel di jendela «Log Xray» akan terisi baris.

### 16.4. Mengelola Xray: Menghentikan dan Me-restart

Status Xray dikelola dari kartu Xray di «Dashboard». Status saat ini ditampilkan dengan salah satu nilai: **Berjalan** (`Running`), **Berhenti** (`Stopped`), **Tidak Diketahui** (`Unknown`), **Error** (`Error`). Saat terjadi error, tersedia tooltip «Error saat memulai Xray».

| Tombol | Terjemahan | Endpoint | Tindakan |
|--------|-----------|----------|----------|
| **Stop** | `Stop` | `POST /panel/api/server/stopXrayService` | Menghentikan proses Xray. Jika berhasil — notifikasi peringatan «Xray service has been stopped». |
| **Restart** | `Restart` | `POST /panel/api/server/restartXrayService` | Me-restart (atau memulai) Xray dengan menerapkan konfigurasi saat ini. Jika berhasil — notifikasi «Xray service has been restarted successfully». |

Setelah salah satu operasi, panel menyiarkan status baru melalui WebSocket, sehingga status di «Dashboard» diperbarui tanpa memuat ulang halaman. Jika operasi gagal, status Xray menjadi «Error», dan teks error masuk ke notifikasi.

> Selain restart manual, panel sendiri memeriksa apakah Xray perlu di-restart (tugas latar belakang setiap 30 detik) dan apakah proses telah crash (pemeriksaan setiap detik) — lihat bagian 16.6.

### 16.5. Me-restart dan Memperbarui Panel

#### Me-restart Panel

Di halaman **«Pengaturan Panel»** terdapat tindakan **«Restart Panel»** (`Restart Panel`, `POST /panel/api/setting/restartPanel`). Setelah konfirmasi, panel di-restart **dalam 3 detik**.

Pesan:
- Konfirmasi: «Apakah Anda yakin ingin me-restart panel? Konfirmasi, dan restart akan terjadi dalam 3 detik. Jika panel tidak dapat diakses, periksa log server.»
- Berhasil: «Panel berhasil di-restart».

Secara teknis, di Linux restart dilakukan dengan mengirimkan sinyal `SIGHUP` ke proses panel (atau melalui hook yang terdaftar). Di Windows, pengiriman `SIGHUP` tidak didukung.

#### Pembaruan Mandiri Panel (Update Panel)

Di «Dashboard» tersedia fungsi **«Update Panel»** (`Update Panel`) — memperbarui 3X-UI ke rilis terbaru langsung dari antarmuka web.

Sebelum pembaruan, panel membandingkan versi (`GET /panel/api/server/getPanelUpdateInfo`), meminta rilis terbaru 3x-ui dari GitHub:

| Kolom | Terjemahan |
|-------|-----------|
| **Versi panel saat ini** | Current panel version |
| **Versi panel terbaru** | Latest panel version |
| **Panel sudah diperbarui** / «Terkini» | Panel is up to date / Up to date — ditampilkan jika tidak ada versi baru |

Memulai pembaruan — `POST /panel/api/server/updatePanel`. Dialog konfirmasi:
- «Apakah Anda benar-benar ingin memperbarui panel?»
- «Ini akan memperbarui 3X-UI ke versi #version# dan me-restart layanan panel.»

Setelah dimulai — pesan pop-up «Panel update started»; jika pemeriksaan versi gagal — «Panel update check failed».

**Yang terjadi di server:** pembaruan mandiri hanya didukung **di Linux** (di OS lain akan dikembalikan error «panel web update is supported only on Linux installations»). Panel mengunduh skrip resmi `update.sh` dari GitHub (`raw.githubusercontent.com/MHSanaei/3x-ui/main/update.sh`) dan menjalankannya sebagai proses terpisah: lebih disukai melalui `systemd-run` dalam unit terpisah (`x-ui-web-update-<timestamp>`), dan jika systemd tidak tersedia — sebagai proses terpisah yang terlepas. Setelah selesai, skrip memperbarui komponen dan me-restart layanan panel. Diperlukan `bash` untuk menjalankan.

Jika selama pembaruan skrip menghasilkan Web Base Path baru yang acak, layanan `x-ui` di-restart secara otomatis agar path baru segera berlaku. (Tanpa restart, server akan terus menyajikan path lama sementara antarmuka menampilkan yang baru, dan alamat baru tidak akan dapat diakses hingga restart manual.)

> Di node, panel 3x-ui yang sama diperbarui secara terpusat melalui `POST /panel/api/nodes/updatePanel` — lihat bagian tentang node.

#### Instalasi Otomatis fail2ban

Agar batas jumlah IP klien (bagian 16.3) berfungsi langsung dari kotak, saat instalasi dan pembaruan panel di server biasa, `fail2ban` kini diinstal dan dikonfigurasi secara otomatis (sebelumnya ini hanya terjadi di image Docker). Perilaku ini dikendalikan oleh variabel lingkungan `XUI_ENABLE_FAIL2BAN`: konfigurasi dilakukan jika variabel tidak ditetapkan atau sama dengan `true`. Eksekusi manual tersedia dengan perintah `x-ui setup-fail2ban`. Kegagalan konfigurasi fail2ban tidak mengganggu instalasi atau pembaruan panel.

#### Instalasi dan Pembaruan di Host Khusus IPv6

Skrip `install.sh` dan `update.sh` kini bekerja dengan benar di server yang hanya memiliki IPv6: pengunduhan rilis, skrip `x-ui.sh`, dan file layanan tidak lagi memaksa IPv4 (`curl -4`), melainkan menggunakan protokol yang tersedia. Oleh karena itu, panel dapat diinstal dan diperbarui bahkan di host tanpa alamat IPv4.

#### Mengganti Port Panel dengan Variabel `XUI_PORT`

Port listening antarmuka web panel dapat diganti dengan variabel lingkungan `XUI_PORT` — variabel ini hanya berlaku selama proses saat ini berjalan dan **tidak mengubah** nilai `webPort` yang tersimpan dalam database. Nilai yang diizinkan adalah `1` hingga `65535`; nilai kosong, tidak valid, atau di luar rentang diabaikan (digunakan `webPort`) dengan peringatan di log. Ini berguna saat deployment, terutama di Docker: saat menggunakan bridge network, port yang dipublikasikan container harus sesuai dengan `XUI_PORT` — misalnya, `XUI_PORT=8080` dan `ports: "8080:8080"`.

#### Memperbarui dan Beralih Versi Xray-core

Di «Dashboard» yang sama, Anda juga dapat mengelola versi Xray-core secara terpisah dari panel.

- **Pembaruan Xray** (`Xray Updates`) / **Pilih Versi** (`Version`) — daftar tarik-turun versi yang tersedia. Petunjuk: «Pilih versi yang diperlukan» dan peringatan «Penting: versi lama mungkin tidak mendukung pengaturan saat ini».
- Instalasi/penggantian versi — `POST /panel/api/server/installXray/{version}`. Dialog: «Ganti Versi Xray» / «Apakah Anda yakin ingin mengganti versi Xray?». Jika berhasil — «Xray berhasil diperbarui».

**Contoh: mengganti versi Xray-core melalui permintaan API.** Versi ditentukan dengan tag rilis dari XTLS/Xray-core (dengan awalan `v`). Misalnya, beralih ke `v1.8.24`:

```bash
curl -s -b cookies.txt -X POST \
     https://panel.example.com:2053/panel/api/server/installXray/v1.8.24
```

(`cookies.txt` — file cookie dari contoh di bagian 16.1.) Setelah instalasi, Xray akan di-restart otomatis dengan versi yang dipilih.

Di server, saat versi diganti, Xray pertama-tama dihentikan, arsip versi yang diinginkan diunduh dari GitHub (XTLS/Xray-core), binari diekstrak dan diganti, setelah itu Xray di-restart dengan verifikasi checksum arsip/binari.

### 16.6. Tugas Berkala (cron)

Panel mendaftarkan sejumlah tugas latar belakang saat startup. Jadwalnya tetap (tidak dapat dikonfigurasi di UI, kecuali jadwal laporan Telegram dan sinkronisasi LDAP). Berikut adalah tugas yang terkait dengan operasional.

| Tugas | Jadwal | Tujuan |
|-------|--------|--------|
| Pemeriksaan status Xray | setiap 1 detik | Memantau bahwa proses Xray berjalan |
| Pemeriksaan kebutuhan restart Xray | setiap 30 detik | Restart jika konfigurasi ditandai sebagai berubah |
| Pengumpulan traffic Xray | setiap 5 detik (mulai 5 detik setelah startup) | Pencatatan traffic inbound/klien |
| Pemeriksaan IP klien | setiap 10 detik | Kontrol batas IP berdasarkan log |
| Heartbeat dan sinkronisasi traffic node | setiap 5 detik | Pertukaran data dengan node |
| **Pembersihan log** | **harian** (`@daily`) | Membersihkan log batas IP dan access-log persisten, merotasi log saat ini ke `*.prev.log` |
| **Reset traffic per periode** | `@hourly`, `@daily`, `@weekly`, `@monthly` | Mereset penghitung traffic untuk inbound (dan kliennya) yang memiliki periode reset otomatis yang sesuai |
| Laporan Telegram | ditentukan di pengaturan bot (default `@daily`) | Pengiriman laporan ke administrator; jika opsi diaktifkan — disertai cadangan database (bagian 16.1) |
| Reset penyimpanan hash Telegram | setiap 2 menit | Hanya jika bot diaktifkan |
| Pemantauan beban CPU untuk Telegram | setiap 10 detik | Hanya jika ambang CPU > 0 ditetapkan |

Tambahan:

- **Reset traffic berkala** hanya dipicu untuk inbound yang memiliki mode reset otomatis yang sesuai (per jam/per hari/per minggu/per bulan). Tugas ini mereset traffic inbound itu sendiri dan semua kliennya.
- **Pemeriksaan kedaluwarsa dan habis batas.** Penonaktifan klien yang masa berlakunya habis atau batas trafficnya tercapai dilakukan dalam kerangka pencatatan traffic: klien dengan `expiry_time` yang telah lewat atau volume yang habis ditandai dan dinonaktifkan, bila perlu dihitung jadwal berikutnya (untuk batas siklus dan mode «hitung dari penggunaan pertama»). Di «Dashboard» dan daftar, ini tercermin dengan status «Kedaluwarsa»/«Habis»/«Segera Habis».
- **Backup otomatis ke Telegram** adalah efek samping dari tugas laporan; tidak ada jadwal cron terpisah khusus untuk backup. Oleh karena itu, frekuensi backup otomatis sama dengan frekuensi laporan bot.

### 16.7. Menu Konsol dan CLI (`x-ui`)

Di server, panel dikelola dengan perintah `x-ui`. Tanpa argumen, menu interaktif «3X-UI Panel Management Script» terbuka; dengan argumen, subperintah tertentu dijalankan. Poin menu yang terkait dengan operasional:

| No. di menu | Poin | Tindakan |
|-------------|------|----------|
| 1 | Install | Instalasi panel (mengunduh dan menjalankan `install.sh`) |
| 2 | Update | Memperbarui semua komponen x-ui ke versi terbaru tanpa kehilangan data; setelahnya — restart otomatis |
| 3 | Update Menu | Memperbarui hanya skrip menu `x-ui` itu sendiri |
| 4 | Legacy Version | Menginstal versi panel tertentu (lama) berdasarkan nomor yang dimasukkan (misalnya, `2.4.0`) |
| 5 | Uninstall | Penghapusan lengkap panel dan Xray (lihat 16.8) |
| 6 | Reset Username & Password | Reset login/kata sandi administrator |
| 7 | Reset Web Base Path | Reset base path antarmuka web panel |
| 8 | Reset Settings | Reset pengaturan ke nilai default |
| 9 | Change Port | Mengganti port panel |
| 10 | View Current Settings | Melihat pengaturan saat ini |
| 11–13 | Start / Stop / Restart | Memulai, menghentikan, me-restart layanan panel |
| 14 | Restart Xray | Me-restart Xray saja |
| 15 | Check Status | Status layanan saat ini |
| 16 | Logs Management | Melihat dan membersihkan log (lihat di bawah) |
| 17–18 | Enable / Disable Autostart | Mengaktifkan/menonaktifkan autostart layanan saat OS dimulai |
| 25 | Update Geo Files | Memperbarui file geo (GeoIP/GeoSite) |
| 27 | PostgreSQL Management | Manajemen PostgreSQL |

#### Manajemen Log di CLI (poin 16)

Di submenu «Logs Management»:
- **Debug Log** — tampilan streaming jurnal layanan: `journalctl -u x-ui -e --no-pager -f -p debug` (di Alpine — `grep` pada `/var/log/messages`).
- **Clear All logs** — membersihkan jurnal sistem: `journalctl --rotate` + `journalctl --vacuum-time=1s`, setelah itu layanan di-restart. (Tidak tersedia di Alpine.)

#### Subperintah Langsung `x-ui`

Semua subperintah yang tersedia:

| Perintah | Deskripsi |
|---------|-----------|
| `x-ui` | Membuka menu administrasi |
| `x-ui start` | Memulai panel |
| `x-ui stop` | Menghentikan panel |
| `x-ui restart` | Me-restart panel |
| `x-ui restart-xray` | Me-restart Xray |
| `x-ui status` | Status saat ini |
| `x-ui settings` | Menampilkan pengaturan saat ini |
| `x-ui enable` | Mengaktifkan autostart saat OS dimulai |
| `x-ui disable` | Menonaktifkan autostart |
| `x-ui log` | Melihat log |
| `x-ui banlog` | Melihat log ban Fail2ban |
| `x-ui setup-fail2ban` | Menginstal dan mengonfigurasi fail2ban untuk batas IP (lihat 16.5) |
| `x-ui update` | Memperbarui panel |
| `x-ui update-all-geofiles` | Memperbarui semua file geo (diikuti restart) |
| `x-ui migrateDB [file]` | Konversi database `.db ⇄ .dump` (SQLite) |
| `x-ui legacy` | Menginstal versi lama |
| `x-ui install` | Menginstal panel |
| `x-ui uninstall` | Menghapus panel |

> Perintah `x-ui update` mengunduh dan menjalankan `update.sh` resmi (sama dengan pembaruan web dari bagian 16.5), meminta konfirmasi: «This function will update all x-ui components to the latest version, and the data will not be lost.» Setelah selesai, panel di-restart otomatis.

> **Flag `-webCert` / `-webCertKey` dalam subperintah `setting`.** Jalur ke sertifikat dan kunci privat antarmuka web panel dapat ditentukan langsung dalam subperintah `x-ui setting -webCert <jalur> -webCertKey <jalur>` — menentukan salah satu flag ini menyimpan jalur yang sesuai (sama seperti subperintah `cert` terpisah), dan panel segera beralih ke HTTPS.

#### Mendapatkan Token API melalui CLI

Perintah untuk mendapatkan token API melalui CLI (poin menu/perintah `x-ui`) tidak menampilkan token yang sudah dikeluarkan sebelumnya. Token API disimpan hanya dalam bentuk hash, sehingga token yang sudah ada tidak dapat diperoleh dalam bentuk teks biasa. Jika token sudah dikonfigurasi, perintah memberitahu jumlahnya, menyarankan untuk mengelola token di panel (**Settings → API Tokens**, lihat bagian tentang token API) dan langsung menghasilkan **token cadangan baru** dengan nama seperti `cli-fallback-<timestamp>` serta menampilkannya, agar CLI tetap berguna tanpa harus masuk ke antarmuka.

### 16.8. Menghapus Panel

Penghapusan dilakukan dari CLI — poin menu **5 (Uninstall)** atau perintah `x-ui uninstall`. Sebelum penghapusan, diminta konfirmasi (default «tidak»): «Are you sure you want to uninstall the panel? xray will also uninstalled!».

Setelah dikonfirmasi, skrip:
1. Menghentikan layanan dan menonaktifkan autostart-nya (`systemctl stop/disable x-ui`, atau di Alpine — `rc-service`/`rc-update`), menghapus file unit layanan, dan memuat ulang konfigurasi systemd.
2. Menghapus direktori data dan aplikasi (`/etc/x-ui/`, direktori instalasi) dan file env layanan (`/etc/default/x-ui`, `/etc/conf.d/x-ui`, atau `/etc/sysconfig/x-ui` — tergantung distribusi).
3. Menghapus skrip `x-ui` itu sendiri dan menampilkan pesan «Uninstalled Successfully.», serta perintah untuk instalasi ulang.

> Penghapusan bersifat permanen: bersama panel, Xray dan semua data (termasuk database) juga dihapus. Jika data mungkin masih diperlukan, lakukan ekspor database terlebih dahulu (bagian 16.1).

### 16.9. Perintah `x-ui migrateDB`

Mulai dari versi 3.3.0, skrip pengelola `x-ui.sh` mendapatkan subperintah `migrateDB` — pembungkus di sekitar binari bawaan `x-ui` (`x-ui migrate-db`) untuk mengonversi database panel SQLite antara dua format: binari `.db` dan dump teks portabel `.dump` (teks SQL biasa).

#### Yang Dilakukan Perintah

Perintah bekerja dalam dua arah, dan arahnya ditentukan **secara otomatis** berdasarkan file input:

| Arah | Nama | Yang Terjadi |
|------|------|--------------|
| `.db → .dump` | dump (ekspor) | database SQLite binari diekspor ke file teks SQL |
| `.dump → .db` | restore (pemulihan) | database SQLite binari dibangun ulang dari file teks SQL |

Di balik layar, skrip memanggil binari panel:
- ekspor: `x-ui migrate-db --src <input> --dump <output>`
- pemulihan: `x-ui migrate-db --restore <input> --out <output>`

#### Sintaks Pemanggilan

```
x-ui migrateDB [file.db|file.dump] [output]
```

- **`[file.db|file.dump]`** — file input (argumen pertama). Jika tidak ditentukan, digunakan database panel yang terinstal secara default: `/etc/x-ui/x-ui.db`.
- **`[output]`** — jalur ke file output (argumen kedua). Opsional: jika tidak ada, nama dipilih secara otomatis di samping file input (lihat di bawah).

Contoh:

```
x-ui migrateDB                              # ekspor /etc/x-ui/x-ui.db -> /etc/x-ui/x-ui.dump
x-ui migrateDB /etc/x-ui/x-ui.db backup.dump
x-ui migrateDB backup.dump restored.db      # bangun .db dari dump
```

#### Cara Menentukan Arah

Skrip melihat ekstensi file input:
- `*.db`, `*.sqlite`, `*.sqlite3` → mode **dump** (ekspor ke teks);
- `*.dump`, `*.sql` → mode **restore** (membangun database).

Jika ekstensi tidak dikenali, skrip membaca 16 byte pertama file: tanda tangan `SQLite format 3` menandakan database binari (mode dump), selain itu file dianggap sebagai dump (mode restore).

Nama file output, jika argumen kedua tidak ditetapkan:
- saat ekspor — nama yang sama dengan input, dengan ekstensi `.dump`;
- saat pemulihan — nama yang sama dengan ekstensi `.db`.

#### Pemeriksaan Keamanan dan Perilaku

- **Keberadaan binari.** Jika binari `x-ui` tidak ditemukan atau tidak dapat dieksekusi — ditampilkan error «x-ui binary not found … Is the panel installed?».
- **Dukungan fungsi dalam build.** Skrip memeriksa bahwa binari mendukung `migrate-db --dump/--restore` (melalui `x-ui migrate-db -h`). Jika tidak — disarankan untuk terlebih dahulu memperbarui panel dengan perintah `x-ui update`.
- **Keberadaan file input.** Jika file input tidak ada, ditampilkan error dan baris sintaks pemanggilan.
- **Penimpaan output.** Jika file output sudah ada, diminta konfirmasi (default «tidak»); tanpa konfirmasi, operasi dibatalkan. Saat pemulihan, file output lama dihapus terlebih dahulu.
- **Perlindungan database aktif.** Saat memulihkan ke database default `/etc/x-ui/x-ui.db` ketika panel sedang berjalan, operasi ditolak dengan permintaan untuk terlebih dahulu menghentikan panel (`x-ui stop`) atau memilih jalur output lain. Ini mencegah penimpaan database aktif layanan yang sedang berjalan.
- Jika pembangunan database gagal, file output yang tidak selesai ditulis dihapus.

#### Kegunaan

- **Backup.** File `.dump` teks mudah dibaca manusia, nyaman untuk disimpan dalam sistem kontrol versi, dan untuk melihat konten database secara diferensial.
- **Migrasi.** Dump portabel antar mesin dan tahan terhadap perbedaan versi format file SQLite — di server baru, dari dump tersebut dapat dibangun `.db` yang siap pakai.
- **Diagnostik.** Dari `.dump`, struktur dan data panel dapat dilihat langsung tanpa memerlukan alat SQLite.

#### Mode Interaktif

Selain pemanggilan langsung, konversi tersedia dari menu interaktif. Di submenu PostgreSQL (`x-ui` → bagian manajemen PostgreSQL) terdapat poin **9. Convert SQLite `.db <-> .dump`**: ini menanyakan jalur ke file input (default `/etc/x-ui/x-ui.db`) dan ke file output (bisa dikosongkan untuk penamaan otomatis), sementara arahnya, seperti dalam mode CLI, ditentukan secara otomatis.

---

*Dokumen ini disusun berdasarkan kode sumber 3X-UI. Jika ada poin antarmuka yang berbeda
di versi Anda — perilaku panel dan petunjuk di UI itu sendiri yang menjadi acuan.*
