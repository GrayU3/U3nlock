# 🔓 Multi-Cracker: Offline Brute Force Tool for ZIP & PDF

Multi-Cracker adalah sebuah tool Python yang memungkinkan kamu melakukan brute-force attack terhadap file ZIP dan PDF yang diproteksi password, menggunakan wordlist offline.

### ✅ Fitur:

- 🗂️ Cracking file ZIP
- 📄 Cracking file PDF
- 📊 Progress bar dengan `tqdm`
- 📝 Output logging dengan timestamp
- 🧩 Modular & mudah dikembangkan

### Jalankan Tool

### Cracking file ZIP
python main.py -z ./files/sample.zip -w ./wordlists/lists.txt

### Cracking file PDF

python main.py -p ./files/secret.pdf -w ./wordlists/lists.txt

### Cracking login

python main.py --login urltargethere -U ./wordlists/users.txt -P ./wordlists/passwords.txt

### 📁 Output log

Hasil akan tersimpan otomatis ke:
results/found_passwords.txt

### 🧠 Kredit 
Dibuat sebagai latihan Python dan cybersecurity.

Gunakan hanya untuk edukasi dan pengujian sistem milik sendiri.
- ⚠️ Jangan digunakan untuk aktivitas ilegal.
