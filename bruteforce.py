import hashlib
import itertools
import string

# 🔹 Target double SHA-256 hash
target_hash = "e7bbf1785686f9583c228ec6d26c9129130d5cd9e5761563fb3a2dee2cad196a"

# 🔹 Define character set (modify for efficiency)
charset = string.ascii_lowercase + string.digits  # a-z, 0-9
max_length = 6  # Adjust this to test longer passwords

# 🔹 Function to compute SHA-256 twice
def double_sha256(text):
    return hashlib.sha256(hashlib.sha256(text.encode()).digest()).hexdigest()

# 🔹 Brute-force search
for length in range(1, max_length + 1):
    for attempt in itertools.product(charset, repeat=length):
        candidate = ''.join(attempt)
        if double_sha256(candidate) == target_hash:
            print(f"\n✅ Match found! Original input: {candidate}")
            exit()

print("\n❌ No match found within the given constraints.")

