# SRT-MGATE-1210 User Guide Project

## Project Overview

Proyek ini berisi dokumentasi panduan pengguna untuk **SRT-MGATE-1210 Modbus IIoT Gateway** (Suriota Modbus Gateway IIoT) dan aplikasi mobile **Gateway Config App**.

**Produk:** PT Surya Inovasi Prioritas (SURIOTA)

---

## Komponen Sistem

### 1. Hardware: SRT-MGATE-1210 Gateway

**Industrial IoT Gateway** untuk akuisisi data Modbus RTU/TCP dengan konektivitas cloud. Solusi gateway berstandar industri yang dirancang untuk mengintegrasikan sistem otomasi berbasis Modbus ke dalam ekosistem IoT.

| Spesifikasi | Detail |
|-------------|--------|
| **Platform** | ESP32-S3-WROOM-1 (Dual-core 240MHz) |
| **Memory** | 512KB SRAM + 8MB PSRAM + 16MB Flash |
| **Protokol** | Modbus RTU (2x RS485), Modbus TCP, BLE 5.0, MQTT, HTTP |
| **Jaringan** | WiFi 2.4GHz + Ethernet (auto-failover) |
| **Operating Temp** | -40°C hingga 75°C |
| **Power** | 12-48V DC (Terminal Block) |
| **Firmware** | v2.5.11+ |

**Keunggulan Utama:**
- **Multi-Protocol Support:** Modbus RTU ↔ Modbus TCP/IP ↔ MQTT/HTTP
- **Dual Connectivity:** WiFi + Ethernet dengan auto-failover
- **No-Code Configuration:** Konfigurasi via aplikasi mobile (Android/iOS)
- **Industrial Grade:** Tahan suhu ekstrem (-40°C hingga 75°C)
- **Secure:** TLS/SSL encryption untuk keamanan data
- **High Capacity:** Hingga 32 perangkat Modbus RTU per port (dual RS-485)
- **Local Data Logging:** MicroSD slot untuk backup data (CSV/JSON) saat offline

### Varian Produk

| Varian | Harga | Fitur Utama |
|--------|-------|-------------|
| Standard Version | Rp 4.5-5.5 juta | Ethernet 10/100 Mbps, Power 12-48 VDC |
| PoE Version | Rp 5.5-6.5 juta | + IEEE 802.3af/at PoE support |

### 2. Software: Suriota Gateway Config App (Mobile)

**Aplikasi Flutter** untuk konfigurasi gateway via Bluetooth Low Energy (BLE).

| Spesifikasi | Detail |
|-------------|--------|
| **Framework** | Flutter 3.22+ |
| **Language** | Dart |
| **State Management** | GetX |
| **BLE Library** | flutter_blue_plus 1.35+ |
| **Platform** | Android 5.0+ / iOS 12+ |
| **Jangkauan BLE** | Hingga 50m (line of sight) |

**Fitur Aplikasi:**
1. **Device Discovery** - Temukan gateway terdekat via BLE
2. **Login & Security** - Akses aman ke perangkat
3. **Device Communication** - Setup parameter komunikasi Modbus
4. **Modbus Configuration** - Atur register dan mapping data
5. **Server Configuration** - Setup MQTT/HTTP server dan network
6. **Data Logging** - Atur interval dan retention
7. **Backup & Restore** - Simpan dan restore konfigurasi
8. **OTA Firmware Update** - Update firmware via BLE

---

## Struktur Dokumentasi

```
SRT-MGATE-1210-User-Guide/
├── README.md                          # File ini (overview proyek)
├── CLAUDE.md                          # Knowledge base untuk AI assistant
│
├── docs/                              # 📚 Dokumentasi utama
│   ├── USER_GUIDE.md                  # ⭐ Panduan pengguna lengkap (FINAL)
│   └── USER_GUIDE_FINAL.md            # Referensi panduan asli
│
├── assets/                            # 🖼️ Aset media
│   ├── screenshots/                   # 46 screenshot UI aplikasi
│   │   └── WhatsApp Image *.jpeg      # Gambar-gambar UI
│   └── product/                       # Dokumen produk
│       └── Product_Suriota_Modbus_Gateway_IIoT.pdf
│
└── archive/                           # 📦 Arsip file lama
    ├── *.docx                         # Dokumen Word draft
    └── *.md                           # Markdown draft lama
```

### File Utama

| File | Deskripsi |
|------|-----------|
| `docs/USER_GUIDE.md` | **Panduan Pengguna Final** - Dokumentasi lengkap dengan 46 screenshot, panduan step-by-step, troubleshooting, dan flowchart |
| `CLAUDE.md` | Knowledge base untuk AI assistant (RAG) |
| `assets/screenshots/` | 46 gambar UI aplikasi Gateway Config |
| `assets/product/` | PDF dokumen produk resmi |

---

## Alur Penggunaan Sistem

### Langkah 1: Koneksi ke Gateway
1. Buka aplikasi Gateway Config App
2. Tekan tombol (+) untuk scan perangkat
3. Cari "SURIOTA GW" di daftar perangkat
4. Tekan Connect untuk terhubung

### Langkah 2: Konfigurasi Device (Sensor)
1. Masuk menu "Device Communications"
2. Tekan (+) untuk tambah device
3. Isi: Device Name, Slave ID
4. Pilih tipe: Modbus RTU atau TCP
5. Untuk RTU: set Baudrate, Parity, Stop Bits
6. Save Device Configuration

### Langkah 3: Konfigurasi Register (Data)
1. Masuk menu "Modbus Configurations"
2. Pilih device dari dropdown
3. Tekan (+) untuk tambah register
4. Isi: Data Name, Address, Function Code
5. Pilih Data Type (INT16, FLOAT32, dll)
6. Optional: Set Scale & Offset untuk kalibrasi
7. Save

### Langkah 4: Konfigurasi Server
1. Masuk menu "Server Configurations"
2. Tab Network: Setup WiFi (SSID, Password) atau Ethernet
3. Tab MQTT: Setup Broker Address, Port, Topic
4. Set Publish Interval
5. Save Configuration

### Langkah 5: Monitoring
1. Masuk menu "Status" untuk cek sistem
2. Lihat: Uptime, Free RAM, WiFi Signal
3. Cek versi firmware

---

## Spesifikasi Teknis

### Modbus Communication

**Supported Function Codes:**
- FC 01: Read Coils
- FC 02: Read Discrete Inputs
- FC 03: Read Holding Registers
- FC 04: Read Input Registers

**Supported Data Types:**
- INT16, UINT16, INT32, UINT32
- FLOAT32 (dengan berbagai endianness: ABCD, DCBA, BADC, CDAB)
- FLOAT64
- String (ASCII)

### BLE Protocol

- **Device Name:** SURIOTA GW
- **MTU:** 244 bytes (optimized)
- **Command Format:** JSON dengan markers `<START>` dan `<END>`
- **Response Size:** Max 200KB

### Network Configuration

**WiFi:**
- Support WPA2/WPA3
- DHCP atau Static IP

**Ethernet:**
- W5500 chip
- DHCP atau Static IP
- Auto-failover dari WiFi

### MQTT Settings

| Parameter | Deskripsi |
|-----------|-----------|
| Broker Address | URL/IP server MQTT |
| Port | Default: 1883 (non-TLS), 8883 (TLS) |
| Client ID | Identifier unik gateway |
| Topic | Alamat publish data |
| QoS | Quality of Service (0, 1, 2) |
| Publish Interval | Frekuensi kirim data (ms) |

---

## Troubleshooting

### BLE Tidak Terdeteksi
- Pastikan Bluetooth HP aktif
- Jarak maksimal 10 meter dari gateway
- Production mode: Tekan lama tombol di gateway untuk aktifkan BLE

### Modbus Tidak Response
- Cek wiring RS485 (A/B)
- Pastikan Slave ID tidak duplikat
- Verifikasi baudrate sesuai spesifikasi sensor

### Data Tidak Terkirim ke Server
- Cek koneksi internet gateway (LED NET)
- Verifikasi MQTT broker address dan port
- Cek username/password jika diperlukan

### Nilai Sensor Aneh/Acak
- Cek Data Type sesuai manual sensor
- Verifikasi Address register
- Gunakan Scale/Offset untuk kalibrasi

---

## Use Cases & Target Industri

| Industri | Aplikasi |
|----------|----------|
| Manufacturing | Monitor mesin produksi, PLC |
| Oil & Gas | Monitor pressure, flow, temperature |
| Marine/Shipyard | Integrasi sistem kapal |
| Agriculture | Smart farming & irrigation |
| Building Automation | HVAC, lighting control |
| Energy Management | Monitor konsumsi listrik |

---

## Resources

### Repository

- **Firmware:** https://github.com/GifariKemal/GatewaySuriotaPOC
- **Mobile App:** https://github.com/dickykhusnaedy/suriota_mobile_app

### Dokumentasi Firmware

- `Documentation/API_Reference/API.md` - BLE CRUD API
- `Documentation/Technical_Guides/MODBUS_DATATYPES.md` - 40+ tipe data
- `Documentation/QUICKSTART.md` - Panduan cepat
- `Documentation/FAQ.md` - 60+ pertanyaan umum

### Dokumentasi Mobile App

- `docs/UI_COMPONENTS_GUIDE.md` - Komponen UI
- `docs/enable_disable_device.md` - Fitur enable/disable device
- `docs/FIRMWARE_PAGINATION_SPEC.md` - Spesifikasi pagination

### Dokumen Produk

- `assets/product/Product_Suriota_Modbus_Gateway_IIoT.pdf` - Informasi produk lengkap (spesifikasi, harga, use cases)

---

## Kontak Support

**PT Surya Inovasi Prioritas (SURIOTA)**

- **Alamat:** Batam Centre, Jl. Legenda Malaka, Baloi Permai, Kec. Batam Kota, Kota Batam, Kepulauan Riau 29431
- **Telepon:** 0858-3567-2476
- **WhatsApp:** +62 858-3567-2476
- **Email:** support@suriota.com
- **Website:** www.suriota.com
- **Documentation:** docs.suriota.com/gateway
- **Video Tutorial:** YouTube @suriota.official

### Warranty
- Standard: 1 tahun parts & service
- Extended: Hingga 3 tahun (opsional)

---

**Made with by SURIOTA R&D Team**
*Empowering Industrial IoT Solutions*
