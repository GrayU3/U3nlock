import os
from datetime import datetime
os.makedirs("results", exist_ok=True)

def log_success(message, filepath="results/found_passwords.txt"):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(f"{message}\n")
    print(f"[✔] {message}")

def log_info(msg):
    print(f"[INFO {timestamp()}] {msg}")

def log_error(msg):
    print(f"[ERROR {timestamp()}] {msg}")

def timestamp():
    return datetime.now().strftime("%H:%M:%S")
