import zipfile
from tqdm import tqdm
from utils.log_utils import log_success

def crack_zip(zip_path, wordlist_path):
    
    try:
        zip_file = zipfile.ZipFile(zip_path)
    except zipfile.BadZipFile:
        print("[!] File ZIP rusak atau tidak valid.")
        return

    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
        passwords = [line.strip() for line in f]

    print(f"[i] Total password yang akan dicoba: {len(passwords)}\n")

    for pwd in tqdm(passwords, desc="🔐 Mencoba password"):
        try:
            zip_file.extractall(pwd=bytes(pwd, 'utf-8'))
            print(f"\n[✓] Password ditemukan: {pwd}")
            log_success(f"[ZIP] Password ditemukan: {pwd} untuk file {zip_path}")
            return pwd
        except:
            continue

    print("\n[✗] Password tidak ditemukan dalam wordlist.")
    return None

    
