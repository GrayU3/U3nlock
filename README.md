# U3nlock: Offline Brute Force Tool for ZIP, PDF & Web Logins

U3nlock is a Python-based tool that allows you to perform brute-force attacks on password-protected ZIP files, PDF documents, and web login forms using an offline wordlist.

### feature:

- Crack ZIP archives
- Crack PDF files
- Crack web login forms
- Progress tracking with 'tqdm'
- Automatic logging with timestamps
- Modular design & easy to extend and maintain

## How to Use

### Crack ZIP files:
`python U3nlock.py -z ./files/sample.zip -w ./wordlists/lists.txt`

### Crack PDF files:
`python U3nlock.py -p ./files/secret.pdf -w ./wordlists/lists.txt`

### Crack Web Login Forms:
`python U3nlock.py --login http://localhost/login -U ./wordlists/users.txt -P ./wordlists/passwords.txt`

## Output Logs
Cracked credentials or passwords will be saved automatically to:
results/found_passwords.txt

## Credits 
Created as a learning project in Python and cybersecurity.

For educational and legal system testing purposes only.
Do not use this tool for unauthorized or malicious activities.
