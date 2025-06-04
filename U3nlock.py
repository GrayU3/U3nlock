import argparse
import sys
import os

from crackers.zip_cracker import crack_zip
from crackers.pdf_cracker import crack_pdf
from crackers.login_cracker import crack_login
from utils.file_utils import file_exists, is_zip_file
from utils.log_utils import log_error

def main():

    if "-help" in sys.argv:
        sys.argv[sys.argv.index("-help")] = "--help"

    parser = argparse.ArgumentParser(
        description="U3nlock: Multi-format File & Web Login Cracker",
        epilog="""
Contoh Penggunaan:

   Cracking file ZIP:
    python U3nlock.py -z ./files/sample.zip -w ./wordlists/lists.txt

   Cracking file PDF:
    python U3nlock.py -p ./files/secret.pdf -w ./wordlists/lists.txt

   Cracking form login :
    python U3nlock.py --login http://localhost/login -U users.txt -P passwords.txt

   Catatan:
    - Gunakan hanya untuk pengujian sistem milik sendiri.
    - Output akan disimpan di: results/found_passwords.txt
    resource: https://github.com/GrayU3/U3nlock
""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-z", "--zip", help="Path ke file ZIP")
    parser.add_argument("-p", "--pdf", help="Path ke file PDF (encrypted)")
    parser.add_argument("-w", "--wordlist", help="Path ke wordlist")
    parser.add_argument("--login", help="Target URL login form web")
    parser.add_argument("-U", "--userlist", help="Path ke wordlist username")
    parser.add_argument("-P", "--passlist", help="Path ke wordlist password")


    args = parser.parse_args()

    # Crack LOGIN if provided
    if args.login:
        if not args.userlist or not args.passlist:
            log_error("Login membutuhkan userlist dan passlist.")
            return
        if not file_exists(args.userlist) or not file_exists(args.passlist):
            log_error("Userlist atau Passlist tidak ditemukan.")
            return
        crack_login(args.login, args.userlist, args.passlist)
        return  

    # Crack ZIP if provided
    if args.zip:
        if not args.wordlist:
            log_error("Wordlist dibutuhkan untuk ZIP cracking.")
            return
        if not file_exists(args.wordlist):
            log_error("Wordlist tidak ditemukan!")
            return
        if not file_exists(args.zip):
            log_error("File ZIP tidak ditemukan!")
            return
        if not is_zip_file(args.zip):
            log_error("File yang dimasukkan bukan file ZIP.")
            return
        crack_zip(args.zip, args.wordlist)

    # Crack PDF if provided
    if args.pdf:
        if not args.wordlist:
            log_error("Wordlist dibutuhkan untuk PDF cracking.")
            return
        if not file_exists(args.wordlist):
            log_error("Wordlist tidak ditemukan!")
            return
        if not file_exists(args.pdf):
            log_error("File PDF tidak ditemukan!")
            return
        crack_pdf(args.pdf, args.wordlist)

    # No target provided
    if not args.zip and not args.pdf and not args.login:
        log_error("Minimal harus ada salah satu target: ZIP, PDF, atau login form.")

if __name__ == "__main__":
    main()
