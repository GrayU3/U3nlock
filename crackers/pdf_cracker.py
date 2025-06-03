from PyPDF2 import PdfReader
from tqdm import tqdm
from utils.log_utils import log_success

def crack_pdf(pdf_path, wordlist_path):
    try:
        with open(pdf_path, "rb") as file:
            reader = PdfReader(file)
            if not reader.is_encrypted:
                print("[✓] PDF tidak diproteksi dengan password.")
                return

            with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as wordlist:
                passwords = wordlist.readlines()

                print(f"[i] Mencoba {len(passwords)} password...")

                for pwd in tqdm(passwords, desc="🔓 Cracking PDF"):
                    password = pwd.strip()
                    try:
                        if reader.decrypt(password):  # returns 0 or 1
                            print("\n[✓] Password ditemukan!")
                            print(f"[+] Password: {password}")
                            log_success(f"[ZIP] Password ditemukan: {password} untuk file {pdf_path}")
                            return
                    except Exception:
                        continue

                print("\n[✗] Password tidak ditemukan dalam wordlist.")
    except FileNotFoundError:
        print("[!] File tidak ditemukan.")
    except Exception as e:
        print(f"[!] Terjadi kesalahan: {e}")
