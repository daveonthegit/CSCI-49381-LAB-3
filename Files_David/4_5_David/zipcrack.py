import zipfile

# Path to the encrypted ZIP file
zip_file_path = "challenge493.zip"
# Path to the dictionary file (wordlist)
wordlist_path = "wordlist.txt"

def extract_zip(zip_file, password):
    """Try extracting a ZIP file with a given password."""
    try:
        with zipfile.ZipFile(zip_file, 'r') as zf:
            zf.extractall(pwd=password.encode())
        print(f"Success! Password: {password}")
        return True
    except RuntimeError:
        return False
    except zipfile.BadZipFile:
        print("Corrupted ZIP file.")
        return False

# Attempt passwords from the wordlist
with open(wordlist_path, "r", encoding="utf-8") as f:
    for line in f:
        password = line.strip()
        if extract_zip(zip_file_path, password):
            break

