# ScrapingBee API Client (Python)

Proyek sederhana untuk melakukan web scraping menggunakan layanan [ScrapingBee](https://www.scrapingbee.com/) melalui API mereka. Skrip akan mengambil konten HTML dari URL target dan menyimpannya di folder `data/`.

---

# 📁 Struktur Proyek

```text
scrapingbee_project/
├── .env.example          # Template file environment (contoh API key)
├── .gitignore            # Abaikan file sensitif dan output Git
├── requirements.txt      # Library Python yang dibutuhkan
├── data/                 # Folder output hasil scraping (dibuat otomatis)
│   └── example.com.html
├── main.py               # Skrip utama
└── README.md             # Dokumentasi proyek
```

---

# 🔧 Persiapan Awal

## 1. Dapatkan API Key ScrapingBee

- Daftar atau login ke https://app.scrapingbee.com/
- Salin **API Key** Anda dari halaman dashboard.

---

## 2. Clone atau Unduh Proyek

Anda dapat membuat folder proyek secara manual dan menyalin file-file yang telah disediakan, atau menggunakan Git:

```bash
git clone <repository-url> scrapingbee_project
cd scrapingbee_project
```

---

## 3. Buat File `.env`

Salin template `.env.example` menjadi `.env`:

```bash
cp .env.example .env
```

Buka file `.env` menggunakan editor favorit Anda:

```bash
nano .env
```

Isi dengan API Key Anda:

```env
SCRAPINGBEE_API_KEY=ABCD1234YOURAPIKEY5678EFGH
```

> **⚠️ Penting:** Jangan pernah melakukan commit file `.env` ke repository publik.

---

## 4. Buat Virtual Environment (Disarankan)

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows (CMD)

```cmd
venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 5. Install Dependensi

```bash
pip install -r requirements.txt
```

---

# 🚀 Cara Menggunakan

## Opsi 1 — Memberikan URL melalui Command Line

```bash
python main.py https://example.com
```

---

## Opsi 2 — Input Interaktif

Jalankan:

```bash
python main.py
```

Kemudian masukkan URL ketika diminta:

```text
Masukkan URL yang ingin di-scrape:
https://example.com
```

---

# 📄 Hasil

File HTML hasil scraping akan disimpan di folder `data/`.

Contoh:

```text
data/example.com.html
```

---

# ⚙️ Konfigurasi Tambahan

Di dalam `main.py`, Anda dapat mengubah parameter scraping melalui dictionary `scrape_params`.

Contoh:

```python
scrape_params = {
    "render_js": "true",
    "premium_proxy": "true",
    "country_code": "us",
}
```

## Parameter yang Tersedia

| Parameter | Deskripsi | Default |
|-----------|-----------|---------|
| `render_js` | Render halaman menggunakan JavaScript | `false` |
| `premium_proxy` | Gunakan Premium Proxy | `false` |
| `country_code` | Negara asal proxy (contoh: `id`, `us`) | `id` |
| `block_resources` | Blok gambar, CSS, font agar scraping lebih cepat | `false` |

Dokumentasi lengkap parameter tersedia di:

https://www.scrapingbee.com/documentation/

---

# 🛡️ Keamanan

- Simpan API Key hanya di file `.env`.
- Jangan pernah mengunggah file `.env` ke GitHub.
- File `.gitignore` sudah disiapkan untuk mengabaikan file tersebut.
- Pada environment production (VPS, Docker, Railway, dll.), sebaiknya gunakan Environment Variables daripada file `.env`.

---

# ❓ Troubleshooting

## `SCRAPINGBEE_API_KEY` tidak ditemukan

Pastikan:

- File `.env` sudah dibuat dari `.env.example`.
- Variabel ditulis persis seperti berikut:

```env
SCRAPINGBEE_API_KEY=YOUR_API_KEY
```

- API Key yang digunakan masih aktif.

---

## `ModuleNotFoundError: No module named 'requests'`

Install dependensi:

```bash
pip install -r requirements.txt
```

Pastikan virtual environment sudah aktif.

---

## Hasil scraping kosong atau tidak sesuai

Beberapa website membutuhkan JavaScript untuk merender halaman.

Coba aktifkan:

```python
scrape_params = {
    "render_js": "true"
}
```

Jika website memiliki proteksi tinggi, aktifkan Premium Proxy:

```python
scrape_params = {
    "premium_proxy": "true"
}
```

Lihat juga dokumentasi status code dan parameter API ScrapingBee.

---

# 📚 Referensi

- **ScrapingBee Documentation**  
  https://www.scrapingbee.com/documentation/

- **ScrapingBee Dashboard**  
  https://app.scrapingbee.com/

- **python-dotenv**  
  https://github.com/theskumar/python-dotenv
