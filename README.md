# Brute Force Login Script

Script ini digunakan untuk melakukan brute force login pada halaman web tertentu yang menggunakan CAPTCHA sederhana dan PIN sebagai password.
serta sebagai pengingat untuk website diluar sana yang masih memakai captcha dan password yang lemah xixixixi

## Fitur
- Input URL, username, dan range PIN langsung dari terminal
- Proses brute force berjalan cepat dengan multithreading
- Otomatis berhenti jika password ditemukan
- Output status setiap percobaan PIN di terminal

## Cara Pakai
1. Pastikan Python 3 sudah terinstall.
2. Install dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```
3. Jalankan script:
   ```bash
   python 1.py
   ```
4. Masukkan data sesuai prompt:
   - `masukan url :` (contoh: https:login_page.com)
   - `username :` (contoh: 2308*****)
masukan range
   - `masukan  PIN awal :` (contoh: dari 60000)
   - `masukan PIN akhir :` (contoh: sampai 70000)

## Catatan Penting
- Gunakan script ini hanya untuk tujuan edukasi dan pengujian keamanan milik sendiri.
- Jangan gunakan untuk menyerang sistem tanpa izin, karena melanggar hukum.
- Terlalu banyak thread atau request bisa menyebabkan IP Anda diblokir oleh server target.

## Dependencies
- requests
- beautifulsoup4

## Lisensi
Script ini hanya untuk pembelajaran dan tanggung jawab penggunaan ada pada pengguna. 
