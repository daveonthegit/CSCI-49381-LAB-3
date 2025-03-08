import hmac
import hashlib
from itertools import product

# Load female names
with open("female.lst", "r", encoding="utf-8") as f:
    female_names = [line.strip() for line in f if line.strip()]

# Load author last names (up to 6 characters)
with open("last-names.lst", "r", encoding="utf-8") as f:
    last_names = [line.strip() for line in f if line.strip() and len(line.strip()) <= 6]

# Target hash
target_hash = "8b5a3e95656026f9ce2f405e279adf06"

# Function to compute HMAC-MD5
def hmac_md5(key, text):
    return hmac.new(key.encode(), text.encode(), hashlib.md5).hexdigest()

# Brute-force search
for key, text in product(female_names, last_names):
    computed_hash = hmac_md5(key, text)
    print(f"Testing:Key: {key}, Text: {text}")
    if computed_hash == target_hash:
        print(f"Match found! Key: {key}, Text: {text}")
        break

