import os
import magic

os.makedirs("results", exist_ok=True)

def log_success(message, filepath="results/found_passwords.txt"):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(f"{message}\n")
    print(f"[✔] {message}")

def file_exists(path):
    """Cek apakah file ada dan bisa dibaca"""
    return os.path.isfile(path)

def detect_file_type(path):
    """Gunakan libmagic untuk deteksi MIME-type file"""
    mime = magic.Magic(mime=True)
    return mime.from_file(path)

def is_zip_file(path):
    """Cek apakah file adalah ZIP berdasarkan ekstensi"""
    return path.lower().endswith('.zip')
