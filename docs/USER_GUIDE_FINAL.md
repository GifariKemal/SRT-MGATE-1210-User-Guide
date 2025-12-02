# 📱 Panduan Lengkap Pengguna: Gateway Config App

Dokumen ini adalah panduan visual mendetail untuk menggunakan aplikasi **Gateway Config App**. Setiap langkah dilengkapi dengan gambar dan penjelasan fitur secara rinci untuk memastikan Anda dapat mengonfigurasi Gateway dengan benar.

---

## 1. Menghubungkan Aplikasi ke Gateway

Langkah pertama adalah menghubungkan smartphone Anda ke perangkat Gateway menggunakan Bluetooth.

### A. Memulai Aplikasi
![Home Screen](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.13.jpeg){width=2.3in}
**Fitur Halaman Utama:**
*   **Daftar Perangkat:** Area kosong di tengah akan menampilkan daftar gateway yang pernah terhubung sebelumnya (History).
*   **Tombol Tambah (+):** Terletak di pojok kanan bawah, tombol ini berfungsi untuk memulai pencarian perangkat gateway baru di sekitar Anda.
*   **Menu Bar:** Navigasi di bawah untuk berpindah antara halaman "Home" dan "Settings".

### B. Menu Pemindaian (Scan)
![Scan Menu](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.13%20(1).jpeg){width=2.3in}
**Fitur Halaman Scan:**
*   **Tombol Scan:** Tekan tombol ini untuk memerintahkan HP mencari sinyal Bluetooth dari Gateway.
*   **Status Indikator:** Menunjukkan apakah Bluetooth di HP Anda sudah aktif atau belum.

### C. Proses Pencarian
![Scanning](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.13%20(2).jpeg){width=2.3in}
**Keterangan:**
*   Aplikasi sedang bekerja mencari perangkat.
*   Akan muncul animasi loading.
*   **Tips:** Pastikan Anda berada dalam jarak maksimal 10 meter dari Gateway agar sinyal terdeteksi.

### D. Hasil Pencarian
![Device Found](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.13%20(3).jpeg){width=2.3in}
**Fitur:**
*   **Daftar Perangkat Ditemukan:** Menampilkan nama-nama perangkat Bluetooth yang terdeteksi.
*   **Identifikasi Gateway:** Cari perangkat dengan nama **"SURIOTA GW"** atau yang serupa.
*   **Kekuatan Sinyal (RSSI):** Angka negatif (misal -60dBm) menunjukkan kekuatan sinyal. Semakin kecil angkanya (mendekati 0), semakin dekat jaraknya.

### E. Memilih Perangkat
![Select Device](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.14.jpeg){width=2.3in}
**Tindakan:**
*   Tekan tombol **Connect** pada nama perangkat gateway yang sesuai.
*   Aplikasi akan mencoba membangun koneksi aman (pairing) dengan gateway.

### F. Status Terhubung
![Connected](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.17.jpeg){width=2.3in}
**Indikator Keberhasilan:**
*   Status pada nama perangkat berubah menjadi **"Bonded"** atau **"Connected"**.
*   Muncul notifikasi atau pop-up konfirmasi bahwa koneksi berhasil.
*   Tombol berubah menjadi **Disconnect** (untuk memutus koneksi).

### G. Dashboard Utama Gateway
![Dashboard](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.17%20(1).jpeg){width=2.3in}
**Fitur Dashboard:**
*   **Device Communications:** Menu untuk mengatur sensor/meteran yang terpasang.
*   **Modbus Configurations:** Menu untuk mengatur alamat data (register) yang akan dibaca.
*   **Server Configurations:** Menu untuk mengatur koneksi internet (WiFi/LAN) dan tujuan pengiriman data (MQTT).
*   **Status:** Menu untuk melihat info sistem dan update firmware.
*   **Settings:** Menu untuk backup dan reset konfigurasi gateway.

---

## 2. Mengatur Perangkat Sensor (Device Communications)

Di sini Anda mendaftarkan sensor apa saja yang kabelnya tercolok ke Gateway.

### A. Daftar Perangkat
![Device List](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.19.jpeg){width=2.3in}
**Fitur:**
*   Menampilkan list sensor yang sudah didaftarkan.
*   Jika belum ada, tampilan akan kosong.
*   **Tombol (+):** Di pojok kanan atas untuk menambah sensor baru.

### B. Form Tambah Perangkat
![Add Device](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.20.jpeg){width=2.3in}
**Kolom Isian:**
*   **Device Name:** Ketik nama bebas untuk menamai sensor (contoh: "Sensor Suhu 1").
*   **Slave ID:** Masukkan ID Modbus sensor (angka 1-247). Harus sesuai dengan settingan di fisik sensornya.

### C. Input Detail
![Input Detail](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.20%20(1).jpeg){width=2.3in}
**Keterangan:**
*   Pastikan nama tidak mengandung karakter aneh agar mudah dibaca.
*   Slave ID tidak boleh kembar dengan sensor lain dalam satu jalur kabel yang sama.

### D. Memilih Tipe Koneksi
![Connection Type](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.20%20(2).jpeg){width=2.3in}
**Pilihan:**
*   **Modbus RTU:** Pilih ini jika sensor menggunakan kabel serial (RS485) dua kawat (A/B).
*   **Modbus TCP:** Pilih ini jika sensor menggunakan kabel LAN/Ethernet.

### E. Setting Serial (Khusus RTU)
![Serial Settings](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.20%20(3).jpeg){width=2.3in}
**Parameter Komunikasi:**
*   **Baudrate:** Kecepatan data (Standar: 9600).
*   **Parity:** Pengecekan error (None/Even/Odd).
*   **Stop Bits:** Bit penutup (1 atau 2).
*   **Data Bits:** Jumlah bit data (biasanya 8).
*   *Semua setting ini harus SAMA PERSIS dengan spesifikasi sensor.*

### F. Menyimpan Perangkat
![Save Device](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.21.jpeg){width=2.3in}
**Tindakan:**
*   Tekan tombol **Save Device Configuration**.
*   Tunggu hingga muncul pesan "Success".

### G. Perangkat Berhasil Ditambah
![Device Added](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.21%20(1).jpeg){width=2.3in}
**Tampilan:**
*   Kartu perangkat baru muncul di daftar.
*   Menampilkan ringkasan: Nama, ID, dan Tipe Koneksi.

### H. Mengaktifkan Perangkat
![Toggle Active](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.21%20(2).jpeg){width=2.3in}
**Fitur Toggle:**
*   **Switch ON/OFF:** Geser tombol di kanan kartu untuk mengaktifkan atau mematikan pembacaan sensor tersebut tanpa perlu menghapusnya.

---

## 3. Mengatur Data (Modbus Configurations)

Setelah sensor didaftarkan, tentukan data apa yang mau diambil (Suhu? Kelembaban? Voltase?).

### A. Menu Konfigurasi Modbus
![Modbus Menu](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.22.jpeg){width=2.3in}
**Fitur:**
*   Halaman ini mengatur "Register" atau alamat memori data.
*   Awalnya kosong jika belum memilih perangkat.

### B. Memilih Perangkat Target
![Select Device](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.22%20(1).jpeg){width=2.3in}
**Tindakan:**
*   Klik dropdown di atas.
*   Pilih nama sensor yang tadi sudah dibuat (misal: "Sensor Suhu 1").

### C. Form Tambah Data
![Add Register](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.23.jpeg){width=2.3in}
**Tombol (+):**
*   Tekan tombol tambah untuk memasukkan data baru yang ingin dibaca.

### D. Detail Register
![Register Detail](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.23%20(1).jpeg){width=2.3in}
**Kolom Isian:**
*   **Data Name:** Beri label data (contoh: "Temp_Ruang").
*   **Address:** Alamat memori (Lihat manual sensor, misal: 40001 ditulis 0 atau 1 tergantung sensor).
*   **Function Code:** Cara baca (03 untuk Holding Register, 04 untuk Input Register).

### E. Tipe Data
![Data Type](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.23%20(2).jpeg){width=2.3in}
**Pilihan Format:**
*   **INT16:** Angka bulat kecil.
*   **FLOAT32:** Angka desimal (koma).
*   **UINT16:** Angka bulat positif saja.
*   *Pilih sesuai manual sensor agar angka tidak acak.*

### F. Kalibrasi (Opsional)
![Calibration](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.24.jpeg){width=2.3in}
**Fitur Matematika:**
*   **Scale (Pengali):** Misal data mentah 250 ingin jadi 25.0, isi Scale dengan `0.1`.
*   **Offset (Penambah):** Untuk koreksi nilai (+/-).

### G. Simpan Data
![Save Register](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.24%20(1).jpeg){width=2.3in}
**Tindakan:**
*   Tekan **Save**. Data akan disimpan ke memori Gateway.

### H. Daftar Data
![Register List](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.24%20(2).jpeg){width=2.3in}
**Tampilan:**
*   Menampilkan list data yang akan dibaca dari sensor tersebut.
*   Bisa diedit (ikon pensil) atau dihapus (ikon sampah).

---

## 4. Koneksi Internet & Server (Server Configurations)

Mengatur jalan keluar data menuju internet.

### A. Menu Server
![Server Menu](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.25.jpeg){width=2.3in}
**Fitur:**
*   Tab **Network:** Mengatur WiFi/LAN.
*   Tab **MQTT:** Mengatur tujuan pengiriman data.

### B. Setting WiFi
![WiFi Config](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.25%20(1).jpeg){width=2.3in}
**Kolom Isian:**
*   **Enable WiFi:** Geser ke ON.
*   **SSID:** Ketik nama WiFi di lokasi Anda.
*   **Password:** Ketik kata sandi WiFi.

### C. Setting Ethernet (LAN)
![Ethernet Config](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.25%20(2).jpeg){width=2.3in}
**Pilihan:**
*   **DHCP:** Otomatis dapat IP (Disarankan).
*   **Static:** Isi IP manual jika jaringan mengharuskan.

### D. Detail IP Static
![Static IP](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.25%20(3).jpeg){width=2.3in}
**Kolom:**
*   IP Address, Gateway, Subnet Mask, DNS.

### E. Setting MQTT (Cloud)
![MQTT Config](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.26.jpeg){width=2.3in}
**Kolom Utama:**
*   **Broker Address:** Alamat server (URL atau IP).
*   **Port:** Pintu masuk server (Default: 1883).

### F. Identitas Client
![Client ID](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.26%20(1).jpeg){width=2.3in}
**Kolom:**
*   **Client ID:** Identitas unik gateway ini (jangan sama dengan gateway lain).
*   **Username/Password:** Jika server butuh login.

### G. Interval Pengiriman
![Interval](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.26%20(2).jpeg){width=2.3in}
**Fitur:**
*   **Publish Interval:** Seberapa sering data dikirim (misal: 5000 ms = 5 detik).
*   **Topic:** Alamat kotak surat di server tempat data ditaruh.

### H. Simpan Konfigurasi Server
![Save Server](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.27.jpeg){width=2.3in}
**Tindakan:**
*   Tekan **Save Configuration**.

### I. Konfirmasi Simpan
![Saved](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.27%20(1).jpeg){width=2.3in}
**Indikator:**
*   Muncul pesan sukses. Gateway akan restart koneksi jaringannya.

### J. Cek Koneksi
![Network Check](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.27%20(2).jpeg){width=2.3in}
**Tips:**
*   Pastikan lampu indikator di fisik Gateway menyala stabil (tidak kedip cepat terus menerus) yang menandakan sudah terhubung internet.

---

## 5. Status Sistem & Update Firmware

Memantau kesehatan alat.

### A. Menu Status
![Status Menu](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.28.jpeg){width=2.3in}
**Informasi:**
*   Menampilkan ringkasan kondisi sistem saat ini.

### B. Info Detail
![System Info](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.28%20(1).jpeg){width=2.3in}
**Parameter:**
*   **Uptime:** Berapa lama alat sudah menyala.
*   **Free RAM:** Sisa memori kerja.
*   **WiFi Signal:** Kekuatan sinyal WiFi (jika pakai WiFi).

### C. Versi Firmware
![Version](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.28%20(2).jpeg){width=2.3in}
**Fitur:**
*   Mengetahui versi software yang sedang berjalan (misal: v1.0.2).

### D. Menu Update
![Update Menu](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.29.jpeg){width=2.3in}
**Fungsi:**
*   Tombol **Select Firmware** untuk memilih file update (.bin) dari penyimpanan HP.

### E. Memilih File
![Select File](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.29%20(1).jpeg){width=2.3in}
**Tindakan:**
*   Cari file firmware yang sudah Anda download sebelumnya.

### F. Proses Upload
![Uploading](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.29%20(2).jpeg){width=2.3in}
**Peringatan:**
*   Tunggu persentase sampai 100%.
*   **JANGAN MATIKAN GATEWAY** selama proses ini.

### G. Update Selesai
![Update Done](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.29%20(3).jpeg){width=2.3in}
**Hasil:**
*   Gateway akan restart otomatis dengan fitur baru.

---

## 6. Pengaturan Aplikasi & Backup (Settings)

Mengamankan konfigurasi Anda.

### A. Menu Settings Gateway
![Gateway Settings](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.30.jpeg){width=2.3in}
**Fitur:**
*   Tempat manajemen file konfigurasi.

### B. Backup & Restore
![Backup Restore](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.30%20(1).jpeg){width=2.3in}
**Tombol:**
*   **Download All Config:** Menyalin semua settingan (Sensor, Modbus, Server) dari Gateway ke HP. Berguna sebagai cadangan.
*   **Import Config:** Mengembalikan settingan dari HP ke Gateway. Berguna jika ganti alat baru.

### C. Reset Pabrik
![Factory Reset](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.30%20(2).jpeg){width=2.3in}
**Tombol:**
*   **Clear Configuration:** Menghapus SEMUA data di Gateway. Alat kembali seperti baru beli. Hati-hati!

### D. Menu Settings Aplikasi
![App Settings](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.31.jpeg){width=2.3in}
**Fitur:**
*   Pengaturan yang berhubungan dengan aplikasi di HP, bukan alat Gateway.

### E. Profil Pengguna
![User Profile](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.31%20(1).jpeg){width=2.3in}
**Fitur:**
*   Mengubah nama pengguna atau foto profil aplikasi.

### F. Tentang Aplikasi
![About App](UI/WhatsApp%20Image%202025-11-30%20at%2015.08.31%20(2).jpeg){width=2.3in}
**Informasi:**
*   Versi Aplikasi Android/iOS.
*   Kontak Developer/Support.

---
*Dokumen ini dibuat otomatis untuk memudahkan pengguna dalam mengoperasikan SRT-MGATE-1210.*
