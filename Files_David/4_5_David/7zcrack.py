import subprocess

# Path to the encrypted 7z file
zip_file_path = "challenge493.7z"
# Path to the dictionary file (wordlist)
wordlist_path = "wordlist.txt"

def extract_7z(zip_file, password):
    """Try extracting a 7-Zip file with a given password using the 7z command-line tool."""
    command = f'7z x {zip_file} -p{password} -oextracted_files/ -y'
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if "Everything is Ok" in result.stdout.decode():
        print(f"Success! Password: {password}")
        return True
    return False

# Attempt passwords from the wordlist
with open(wordlist_path, "r", encoding="utf-8") as f:
    for line in f:
        password = line.strip()
        if extract_7z(zip_file_path, password):
            break

