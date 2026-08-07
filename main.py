#!/usr/bin/env python3
"""
Skrip sederhana untuk melakukan scraping web menggunakan ScrapingBee API.
Hasil HTML akan disimpan di folder data/.
"""

import os
import sys
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse

# Muat variabel dari file .env
load_dotenv()

# Ambil API key dari environment
SCRAPINGBEE_API_KEY = os.getenv("SCRAPINGBEE_API_KEY")
if not SCRAPINGBEE_API_KEY:
    print("Error: SCRAPINGBEE_API_KEY tidak ditemukan di file .env.")
    print("Pastikan Anda telah menyalin .env.example ke .env dan mengisinya dengan API key.")
    sys.exit(1)

def scrape_url(url, output_dir="data", extra_params=None):
    """
    Melakukan scraping URL menggunakan ScrapingBee dan menyimpan hasilnya.

    Parameters
    ----------
    url : str
        URL target yang akan di-scrape.
    output_dir : str
        Folder untuk menyimpan file output (default: data).
    extra_params : dict, optional
        Parameter tambahan untuk ScrapingBee API (render_js, premium_proxy, dll).
    
    Returns
    -------
    str atau None
        Konten HTML hasil scraping jika berhasil, None jika gagal.
    """
    api_endpoint = "https://app.scrapingbee.com/api/v1/"
    
    # Parameter dasar
    params = {
        "api_key": SCRAPINGBEE_API_KEY,
        "url": url,
    }
    
    # Gabungkan parameter tambahan jika ada
    if extra_params:
        params.update(extra_params)
    
    try:
        response = requests.get(api_endpoint, params=params, timeout=60)
        response.raise_for_status()  # Akan memunculkan exception jika status code bukan 200
    except requests.exceptions.RequestException as e:
        print(f"Error saat mengakses API: {e}")
        return None

    # Buat nama file dari domain
    domain = urlparse(url).netloc.replace(":", "_")  # Hindari karakter ilegal di nama file
    filename = f"{domain}.html"
    
    # Pastikan folder output ada
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    
    # Simpan konten ke file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(response.text)
    
    print(f"Berhasil! Hasil disimpan di: {filepath}")
    return response.text

def main():
    """Fungsi utama: meminta input URL dan menjalankan scraping."""
    # Ambil URL dari argumen command line, jika tidak ada, minta input
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
    else:
        target_url = input("Masukkan URL yang ingin di-scrape: ").strip()
        if not target_url:
            print("URL tidak boleh kosong.")
            sys.exit(1)
    
    # Parameter tambahan untuk ScrapingBee (opsional, sesuaikan kebutuhan)
    scrape_params = {
        "render_js": "false",      # Ubah menjadi "true" jika halaman membutuhkan JavaScript
        "premium_proxy": "false",  # Gunakan proxy premium jika diperlukan
        "country_code": "id",      # Kode negara (opsional)
        "block_resources": "false",# Blokir resource seperti gambar/CSS untuk kecepatan
    }
    
    print(f"Memulai scraping untuk: {target_url}")
    result = scrape_url(target_url, extra_params=scrape_params)
    
    if result:
        print("Scraping selesai.")
    else:
        print("Scraping gagal.")

if __name__ == "__main__":
    main()
