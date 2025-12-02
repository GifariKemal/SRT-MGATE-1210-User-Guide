# CLAUDE.md - Knowledge Base untuk User Guide SRT-MGATE-1210

**Tujuan:** File ini adalah RAG (Retrieval-Augmented Generation) context untuk AI assistant dalam membuat dan menjawab pertanyaan seputar panduan pengguna SRT-MGATE-1210 Gateway dan Gateway Config App.

---

## 1. OVERVIEW PRODUK

### SRT-MGATE-1210 Gateway
- **Nama Produk:** Suriota Modbus Gateway IIoT (SRT-MGate1210)
- **Fungsi:** Industrial IoT Gateway untuk akuisisi data Modbus RTU/TCP dan kirim ke cloud via MQTT/HTTP
- **Deskripsi:** Solusi gateway berstandar industri yang dirancang untuk mengintegrasikan sistem otomasi berbasis Modbus ke dalam ekosistem IoT (Internet of Things)
- **Manufacturer:** PT Surya Inovasi Prioritas (SURIOTA), Batam, Indonesia
- **Platform:** ESP32-S3-WROOM-1 (Dual-core 240MHz, 512KB SRAM, 8MB PSRAM, 16MB Flash)
- **Protokol:** Modbus RTU (2x RS485), Modbus TCP, BLE 5.0, MQTT, HTTP/HTTPS
- **Jaringan:** WiFi 2.4GHz + Ethernet dengan auto-failover
- **Firmware Version:** v2.5.11+ (November 2025)

### Keunggulan Utama
- **Multi-Protocol Support:** Modbus RTU ↔ Modbus TCP/IP ↔ MQTT/HTTP
- **Dual Connectivity:** WiFi + Ethernet dengan auto-failover
- **No-Code Configuration:** Konfigurasi via aplikasi mobile (Android/iOS)
- **Industrial Grade:** Tahan suhu ekstrem (-40°C hingga 75°C)
- **Secure:** TLS/SSL encryption untuk keamanan data

### Varian Produk

#### Standard Version
| Spesifikasi | Detail |
|-------------|--------|
| Network Port | RJ45 Ethernet 10/100 Mbps |
| Power Supply | Screw Terminal 12~48 VDC |
| PoE Support | Tidak ada |
| Target Environment | Indoor/controlled environments |
| Harga | Rp 4.500.000 - Rp 5.500.000 |

#### PoE Version (Power over Ethernet)
| Spesifikasi | Detail |
|-------------|--------|
| Network Port | RJ45 Ethernet 10/100 Mbps + PoE |
| Power Supply | Screw Terminal 12~48 VDC atau 9W PoE PD |
| PoE Standard | IEEE 802.3af/at (36~57 VDC) |
| Target Environment | Outdoor/industrial area |
| Harga | Rp 5.500.000 - Rp 6.500.000 |

### Gateway Config App (Mobile)
- **Nama:** Suriota Gateway Config App
- **Fungsi:** Aplikasi smartphone untuk konfigurasi gateway via Bluetooth
- **Framework:** Flutter 3.22+, Dart
- **State Management:** GetX
- **BLE Library:** flutter_blue_plus 1.35+
- **Platform:** Android 5.0+ / iOS 12+
- **Koneksi:** Bluetooth Low Energy (BLE 5.0)
- **Jangkauan:** Hingga 50m (line of sight)
- **Package Name:** gateway_config

**Fungsi Aplikasi:**
1. **Device Discovery** - Temukan gateway terdekat via BLE
2. **Login & Security** - Akses aman ke perangkat
3. **Device Communication** - Setup parameter komunikasi
4. **Modbus Configuration** - Atur register dan mapping
5. **Server Configuration** - Setup MQTT/HTTP server
6. **Data Logging** - Atur interval dan retention

---

## 2. ARSITEKTUR SISTEM

### Hardware Layer (Gateway)
```
Industrial Devices (Sensor/PLC)
    ↓
RS485 / Ethernet
    ↓
SRT-MGATE-1210 Gateway
    ├── Modbus RTU Service (2 port serial)
    ├── Modbus TCP Service
    ├── BLE Manager (konfigurasi)
    ├── Network Manager (WiFi/Ethernet failover)
    ├── MQTT Manager (publish data)
    └── HTTP Manager (REST API)
    ↓
Cloud Server (MQTT Broker / HTTP API)
```

### Software Layer (Mobile App)
```
Gateway Config App
    ├── BLE Controller (flutter_blue_plus)
    ├── Device Management (CRUD devices)
    ├── Register Configuration (Modbus registers)
    ├── Server Configuration (Network + MQTT)
    ├── Firmware Update (OTA via BLE)
    └── Backup/Restore System
```

---

## 3. FITUR UTAMA

### 3.1 Device Communications (Sensor Management)
**Lokasi UI:** Menu "Device Communications" di dashboard

**Fungsi:**
- Tambah/edit/hapus sensor Modbus
- Enable/disable sensor tanpa menghapus
- Support Modbus RTU dan TCP

**Parameter Device:**
| Field | Deskripsi | Contoh |
|-------|-----------|--------|
| Device Name | Nama bebas sensor | "Sensor Suhu 1" |
| Slave ID | Alamat Modbus (1-247) | 1 |
| Protocol | RTU atau TCP | RTU |
| Serial Port | Port RS485 (1 atau 2) | 1 |
| Baud Rate | Kecepatan serial | 9600 |
| Parity | Error checking | None/Even/Odd |
| Stop Bits | Bit penutup | 1 atau 2 |
| Data Bits | Jumlah bit data | 8 |
| Timeout | Waktu tunggu response (ms) | 3000 |
| Retry Count | Jumlah percobaan ulang | 3 |
| Refresh Rate | Interval polling (ms) | 5000 |

### 3.2 Modbus Configurations (Register Management)
**Lokasi UI:** Menu "Modbus Configurations" di dashboard

**Fungsi:**
- Definisi data yang dibaca dari sensor
- Mapping alamat register Modbus
- Konfigurasi tipe data dan kalibrasi

**Parameter Register:**
| Field | Deskripsi | Contoh |
|-------|-----------|--------|
| Data Name | Label data | "Temperature" |
| Address | Alamat register | 0 (untuk 40001) |
| Function Code | Cara baca | 03 (Holding Register) |
| Data Type | Format data | FLOAT32_ABCD |
| Quantity | Jumlah register | 2 (untuk 32-bit) |
| Scale | Pengali kalibrasi | 0.1 |
| Offset | Penambah kalibrasi | 0 |

**Supported Function Codes:**
- FC 01: Read Coils (discrete output)
- FC 02: Read Discrete Inputs
- FC 03: Read Holding Registers (paling umum)
- FC 04: Read Input Registers

**Supported Data Types (40+ tipe):**
- INT16, UINT16 (1 register)
- INT32, UINT32 (2 register)
- FLOAT32_ABCD, FLOAT32_DCBA, FLOAT32_BADC, FLOAT32_CDAB
- FLOAT64 (4 register)
- String ASCII

### 3.3 Server Configurations
**Lokasi UI:** Menu "Server Configurations" di dashboard

#### Tab Network (WiFi/Ethernet)
**WiFi Settings:**
| Field | Deskripsi |
|-------|-----------|
| Enable WiFi | ON/OFF |
| SSID | Nama jaringan WiFi |
| Password | Kata sandi WiFi |

**Ethernet Settings:**
| Field | Deskripsi |
|-------|-----------|
| DHCP | ON (otomatis) / OFF (manual) |
| IP Address | Alamat IP (jika static) |
| Gateway | Gateway IP |
| Subnet Mask | Subnet |
| DNS | DNS server |

#### Tab MQTT
| Field | Deskripsi | Default |
|-------|-----------|---------|
| Broker Address | URL/IP server | - |
| Port | Port MQTT | 1883 |
| Client ID | ID unik gateway | - |
| Username | Jika broker butuh auth | - |
| Password | Jika broker butuh auth | - |
| Topic | Alamat publish | suriota/data |
| QoS | Quality of Service | 1 |
| Publish Interval | Frekuensi kirim (ms) | 5000 |

### 3.4 Status & Monitoring
**Lokasi UI:** Menu "Status" di dashboard

**Informasi yang ditampilkan:**
- Uptime: Lama gateway menyala
- Free RAM: Sisa memori
- WiFi Signal: Kekuatan sinyal (jika pakai WiFi)
- Firmware Version: Versi software

### 3.5 Firmware Update (OTA)
**Lokasi UI:** Menu "Status" → Update

**Proses:**
1. Tekan "Select Firmware"
2. Pilih file .bin dari HP
3. Tunggu upload 100%
4. Gateway restart otomatis

**PERINGATAN:** JANGAN matikan gateway selama proses update!

### 3.6 Backup & Restore
**Lokasi UI:** Menu "Settings" → Gateway Settings

**Fitur:**
- Download All Config: Simpan semua konfigurasi ke HP
- Import Config: Restore konfigurasi dari HP ke gateway
- Clear Configuration: Reset ke factory default

---

## 4. ALUR PENGGUNAAN (STEP-BY-STEP)

### 4.1 Koneksi Pertama Kali
```
1. Buka aplikasi Gateway Config App
2. Di halaman Home, tekan tombol (+) di pojok kanan bawah
3. Tekan tombol "Scan" untuk mencari perangkat
4. Tunggu hingga muncul "SURIOTA GW" di daftar
5. Tekan "Connect" pada perangkat tersebut
6. Tunggu status berubah menjadi "Bonded" atau "Connected"
7. Masuk ke Dashboard utama gateway
```

### 4.2 Menambah Sensor Baru
```
1. Di Dashboard, pilih "Device Communications"
2. Tekan tombol (+) di pojok kanan atas
3. Isi Device Name (contoh: "Sensor Suhu Ruang 1")
4. Isi Slave ID sesuai setting di sensor fisik
5. Pilih tipe koneksi:
   - Modbus RTU: untuk sensor dengan kabel RS485
   - Modbus TCP: untuk sensor dengan kabel Ethernet
6. Jika RTU, atur parameter serial:
   - Baudrate: sesuai spesifikasi sensor (umumnya 9600)
   - Parity: None/Even/Odd (lihat manual sensor)
   - Stop Bits: 1 atau 2
   - Data Bits: 8
7. Tekan "Save Device Configuration"
8. Tunggu pesan "Success"
```

### 4.3 Menambah Data Register
```
1. Di Dashboard, pilih "Modbus Configurations"
2. Pilih device dari dropdown di atas
3. Tekan tombol (+) untuk tambah register
4. Isi kolom:
   - Data Name: Label data (contoh: "Suhu")
   - Address: Alamat register (lihat manual sensor)
   - Function Code: 03 untuk Holding Register
   - Data Type: sesuai format data sensor
5. (Opsional) Isi kalibrasi:
   - Scale: pengali (contoh: 0.1 untuk bagi 10)
   - Offset: penambah/pengurang
6. Tekan "Save"
```

### 4.4 Konfigurasi Jaringan & Server
```
1. Di Dashboard, pilih "Server Configurations"
2. Tab Network - WiFi:
   - Enable WiFi: ON
   - SSID: ketik nama WiFi
   - Password: ketik password WiFi
3. Tab Network - Ethernet (opsional):
   - DHCP: ON untuk otomatis
   - Atau isi IP static jika diperlukan
4. Tab MQTT:
   - Broker Address: alamat server MQTT
   - Port: 1883 (default)
   - Client ID: identifier unik
   - Topic: alamat publish data
   - Publish Interval: 5000 (5 detik)
5. Tekan "Save Configuration"
```

---

## 5. LED INDIKATOR GATEWAY

| LED | Status | Arti |
|-----|--------|------|
| LED NET | OFF | Tidak ada koneksi jaringan |
| LED NET | Kedip lambat | Mencoba koneksi |
| LED NET | Kedip cepat | Koneksi bermasalah |
| LED NET | Menyala stabil | Terhubung ke jaringan |
| LED STATUS | Kedip normal | Mode running |
| LED STATUS | Kedip sangat lambat (3s) | Mode konfigurasi (BLE aktif) |

---

## 6. TOMBOL GATEWAY

| Aksi | Fungsi |
|------|--------|
| Tekan lama (>2 detik) | Aktifkan BLE (masuk mode konfigurasi) |
| Double click | Matikan BLE (keluar mode konfigurasi) |

**Catatan:** Pada mode Production, BLE default OFF untuk keamanan. Harus ditekan lama untuk mengaktifkan.

---

## 7. TROUBLESHOOTING

### 7.1 BLE/Bluetooth
| Masalah | Solusi |
|---------|--------|
| Tidak menemukan "SURIOTA GW" | Pastikan dalam jarak 10m, cek Bluetooth HP aktif |
| Tidak bisa connect | Restart aplikasi, restart gateway |
| Connection timeout | Update ke app versi terbaru (MTU optimization) |

### 7.2 Modbus
| Masalah | Solusi |
|---------|--------|
| Sensor tidak response | Cek wiring RS485 (A/B), cek Slave ID |
| Data timeout | Tingkatkan nilai Timeout (ms) |
| Data tidak konsisten | Cek baudrate sesuai spesifikasi sensor |

### 7.3 Network
| Masalah | Solusi |
|---------|--------|
| WiFi tidak connect | Verifikasi SSID dan password |
| MQTT tidak publish | Cek broker address, port, dan koneksi internet |
| Data hilang | Pastikan retain=true di MQTT settings |

### 7.4 Data
| Masalah | Solusi |
|---------|--------|
| Nilai sensor aneh/acak | Cek Data Type sesuai manual sensor |
| Nilai tidak sesuai range | Gunakan Scale/Offset untuk kalibrasi |
| Nilai selalu 0 | Verifikasi Address register |

---

## 8. SPESIFIKASI TEKNIS DETAIL

### 8.1 BLE Protocol
```json
// Format Command (dari App ke Gateway)
<START>{"op":"create","type":"device","config":{...}}<END>

// Format Response (dari Gateway ke App)
{"status":"ok","device_id":"ABC123","data":{...}}
```

**Operations (op):**
- `create`: Tambah device/register
- `read`: Baca konfigurasi
- `update`: Update konfigurasi
- `delete`: Hapus device/register
- `control`: Enable/disable device

**Types:**
- `device`: Konfigurasi sensor
- `register`: Konfigurasi data register
- `server_config`: Konfigurasi MQTT/HTTP
- `network_config`: Konfigurasi WiFi/Ethernet
- `devices_with_registers`: Baca semua device + register

### 8.2 Data Type Mapping
| Data Type | Register Count | Byte Order |
|-----------|----------------|------------|
| INT16 | 1 | Big Endian |
| UINT16 | 1 | Big Endian |
| INT32 | 2 | Big Endian |
| UINT32 | 2 | Big Endian |
| FLOAT32_ABCD | 2 | Big Endian |
| FLOAT32_DCBA | 2 | Little Endian |
| FLOAT32_BADC | 2 | Mid-Big Endian |
| FLOAT32_CDAB | 2 | Mid-Little Endian |

### 8.3 Kalibrasi Register
```
Nilai_Final = (Nilai_Mentah × Scale) + Offset
```

Contoh:
- Sensor memberikan nilai 250
- Ingin hasil 25.0
- Set Scale = 0.1, Offset = 0
- Hasil: 250 × 0.1 + 0 = 25.0

---

## 9. KAPASITAS SISTEM

| Parameter | Limit |
|-----------|-------|
| Max Devices | 70 |
| Max Registers per Device | 70 |
| Max Total Registers | 4900 |
| Max Modbus RTU Devices | 32 per port (total 64 dengan dual RS-485) |
| Max Modbus TCP Clients | 32 |
| BLE Response Size | 200KB |
| BLE Transmission Speed | 21KB dalam 2.1 detik |
| Network Failover Time | <5 detik |
| MicroSD Storage | Hingga 32GB (format CSV/JSON) |

---

## 10. SPESIFIKASI TEKNIS HARDWARE

### Interface
| Komponen | Spesifikasi |
|----------|-------------|
| Ethernet | 1x RJ45 10/100 Mbps dengan Magnetic Isolation |
| USB | 1x Type-C (Debugging/Firmware update) |
| SD Card | 1x Micro SD Card Slot (hingga 32GB) |
| Modbus RTU | 2x Isolated RS-485 (2kV isolation), hingga 32 device per port |
| Modbus TCP/IP | Port 502 (default), hingga 32 client TCP |
| WiFi | 2.4 GHz, 802.11 b/g/n, WPA3-PSK, mode Station/AP/AP+Station |
| Bluetooth | BLE 5.0, jangkauan hingga 50m (Line of Sight) |
| LED Indicators | 8x LED |
| Button | 1x Config Button |
| RTC | Real-Time Clock dengan akurasi tinggi |

### Power Specification
| Parameter | Spesifikasi |
|-----------|-------------|
| Input Voltage | 12V-48V DC (Terminal Block) |
| PoE | IEEE 802.3af standard 9W (36V-57V DC) - khusus varian PoE |
| Power Redundancy | Auto-switch dual power input |

### Environmental
| Parameter | Spesifikasi |
|-----------|-------------|
| Operating Temp | -40°C hingga 75°C |
| Storage Temp | -40°C hingga 85°C |
| Humidity | 10~95% RH |

### Sertifikasi
| Standard | Keterangan |
|----------|------------|
| EMC | EN 55032 |
| EMI | FCC Part 15 |
| EMS | IEC 61000-4-2/4/5 |
| Maritime | DNV-GL |
| Safety | UL 60950-1, UL/cUL 62368-1, RoHS |

---

## 11. FITUR TAMBAHAN

### Local Data Logging
- **Storage:** MicroSD slot untuk backup data (CSV/JSON) saat offline
- **Format:** CSV atau JSON
- **Kapasitas:** Hingga 32GB
- **Auto-sync:** Saat koneksi online kembali

### Security Features
- **Encryption:** TLS/SSL untuk keamanan data
- **Firewall:** Firewall rules
- **BLE Security:** Akses aman ke perangkat

### Dashboard Support
- Grafana
- Aveva
- Suriota Dashboard (proprietary)

### Communication Protocols
| Protokol | Spesifikasi |
|----------|-------------|
| MQTT | ISO/IEC 20922 compliant |
| HTTP/HTTPS | RESTful API support |
| Modbus RTU | Via RS-485 (9.6-115.2 kbps) |
| Modbus TCP/IP | Port 502 |

### Data Format
- JSON payload
- Custom MQTT topics
- CSV logging

---

## 12. USE CASES & APLIKASI

### Target Industri
1. **Manufacturing** - Monitor mesin produksi
2. **Oil & Gas** - Monitor pressure, flow, temperature
3. **Marine/Shipyard** - Integrasi sistem kapal
4. **Agriculture** - Smart farming & irrigation
5. **Building Automation** - HVAC, lighting control
6. **Energy Management** - Monitor konsumsi listrik

### Contoh Implementasi

#### 1. Factory Floor Monitoring
- Baca data dari PLC mesin
- Kirim ke cloud via MQTT
- Dashboard real-time di Grafana

#### 2. Remote Tank Monitoring
- Sensor level via Modbus RTU
- Data logging lokal saat offline
- Auto-sync saat online

#### 3. Energy Metering
- Baca power meter Modbus
- Aggregate data dari multiple site
- Report via HTTP API

---

## 13. QUICK START GUIDE

### Langkah Instalasi
1. **Power On** - Hubungkan power 12-48VDC
2. **Download App** - Suriota Config di Play Store/App Store
3. **Connect BLE** - Scan dan pilih device
4. **Configure Network** - Setup WiFi atau Ethernet
5. **Setup Modbus** - Atur baud rate, parity, device ID
6. **Configure Server** - Input MQTT broker atau HTTP endpoint
7. **Test & Deploy** - Verifikasi data flow

---

## 14. LED INDIKATOR DETAIL

| LED | Warna/Status | Arti |
|-----|--------------|------|
| Power | Hijau | Normal |
| Power | Merah | Error |
| Network | Biru berkedip | Connecting |
| Network | Biru solid | Connected |
| RS485-1/2 | Kuning | Data activity |
| System | Hijau | Running |
| System | Merah | Fault |

---

## 15. INFORMASI PEMESANAN

### Package Contents
- 1x Suriota Modbus Gateway
- 1x Power Terminal Block Connector
- 1x Quick Start Guide
- 1x Warranty Card

### Minimum Order
- Sample: 1 unit
- Bulk: 10 units (diskon 10-15%)
- Enterprise: 50+ units (diskon 20-25%)

### Lead Time
- Stock: 1-3 hari kerja
- Custom order: 2-4 minggu

### Warranty
- Standard: 1 tahun parts & service
- Extended: Hingga 3 tahun (opsional)

---

## 16. COMPETITIVE ADVANTAGES

1. **Price Competitiveness:** 30-50% lebih murah dari kompetitor internasional
2. **Local Support:** Technical support dalam Bahasa Indonesia
3. **Mobile-First Configuration:** BLE app untuk setup tanpa laptop
4. **Dual Connectivity:** WiFi + Ethernet dengan auto-failover
5. **Fast Lead Time:** 1-3 hari vs 2-8 minggu kompetitor import

### Perbandingan dengan Kompetitor

| Feature | Suriota MGate1210 | Moxa MGate MB3180 | Advantech WISE-4012E | Red Lion DA30D |
|---------|-------------------|-------------------|---------------------|----------------|
| Price Range | Rp 4.5-6.5M | Rp 8-12M | Rp 7-10M | Rp 9-15M |
| Mobile Config | BLE App | Web only | Web only | Web only |
| Local Support | Indonesia | Singapore | Taiwan | USA |
| PoE Support | Optional | Standard | Standard | Standard |
| Temperature Range | -40°C to 75°C | -40°C to 75°C | -25°C to 70°C | -40°C to 70°C |
| Dual RS-485 | 2 ports | 2 ports | 1 port | 2 ports |
| Local Data Logging | MicroSD | Internal | Internal | Internal |
| WiFi + Ethernet | Dual | Ethernet only | Dual | Ethernet only |

---

## 17. TECHNICAL SUPPORT

### Bantuan Teknis
- **Email:** support@suriota.com
- **WhatsApp:** +62 858-3567-2476
- **Documentation:** docs.suriota.com/gateway
- **Video Tutorial:** YouTube @suriota.official

---

## 18. REFERENSI

### Repository
- Firmware: https://github.com/GifariKemal/GatewaySuriotaPOC
- Mobile App: https://github.com/dickykhusnaedy/suriota_mobile_app

### Dokumentasi Firmware
- API.md: BLE CRUD API lengkap
- MODBUS_DATATYPES.md: 40+ tipe data
- TROUBLESHOOTING.md: Panduan troubleshooting detail
- FAQ.md: 60+ pertanyaan umum
- QUICKSTART.md: Panduan cepat 5 menit

### Dokumentasi Mobile App
- UI_COMPONENTS_GUIDE.md: Komponen UI
- enable_disable_device.md: Fitur enable/disable
- FIRMWARE_PAGINATION_SPEC.md: Spesifikasi pagination
- CARD_STYLING_GUIDE.md: Styling card component
- LARGE_DATA_LOADING_GUIDE.md: Loading data besar

### Dokumen Produk
- Product_Suriota Modbus Gateway IIoT.pdf: Informasi produk lengkap

---

## 19. KONTAK SUPPORT

**PT Surya Inovasi Prioritas (SURIOTA)**
- Alamat: Batam Centre, Jl. Legenda Malaka, Baloi Permai, Kec. Batam Kota, Kota Batam, Kepulauan Riau 29431
- Telepon: 0858-3567-2476
- Email: support@suriota.com
- Website: www.suriota.com

---

## 20. SCREENSHOT UI APLIKASI

Folder `UI/` berisi 46 screenshot aplikasi mobile dengan urutan:
1. Home Screen & Scan
2. Proses koneksi BLE
3. Dashboard gateway
4. Device Communications (tambah/edit sensor)
5. Modbus Configurations (register)
6. Server Configurations (network/MQTT)
7. Status & Firmware Update
8. Settings & Backup

---

**Last Updated:** Desember 2025
**Version:** 1.1.0

*Dokumen ini digunakan sebagai knowledge base untuk AI assistant dalam membuat panduan pengguna SRT-MGATE-1210.*

**Sumber Referensi:**
- Repository Firmware GatewaySuriotaPOC
- Repository Mobile App suriota_mobile_app
- Product_Suriota Modbus Gateway IIoT.pdf
- USER_GUIDE_FINAL.md (dengan 46 screenshot UI)
