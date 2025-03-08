import os
import hmac
import hashlib

# Paths to wordlists
female_lst_path = "female.lst"
last_names_lst_path = "last-names.lst"

# Target hash to match
target_hash = "8b5a3e95656026f9ce2f405e279adf06"

# Read female names (keys)
with open(female_lst_path, "r", encoding="utf-8") as f:
    female_names = [line.strip() for line in f if line.strip()]

# Read last names (texts)
with open(last_names_lst_path, "r", encoding="utf-8") as f:
    last_names = [line.strip() for line in f if line.strip()]

# Function to compute HMAC-MD5
def hmac_md5(key, text):
    return hmac.new(key.encode(), text.encode(), hashlib.md5).hexdigest()

# Output hash file for John the Ripper
jtr_hash_file = "hashes-jtr.txt"

# Dynamic generation: Only write matching hashes
with open(jtr_hash_file, "w", encoding="utf-8") as f:
    for female_name in female_names:
        for last_name in last_names:
            computed_hash = hmac_md5(female_name, last_name)
            f.write(f"{female_name}:{last_name}:{computed_hash}\n")
            if computed_hash == target_hash:
                print(f"Match found! Key: {female_name}, Text: {last_name}")
                exit()

print(f"Generated hash file: {jtr_hash_file}")

# Run John the Ripper dynamically
print("Running John the Ripper...")
os.system(f"john --format=dynamic_6 --wordlist={female_lst_path} {jtr_hash_file}")

