import hashlib

# Path to RockYou.txt or another wordlist
wordlist_path = "realuniq.lst"  # Change this if needed

# Target double SHA-256 hash
target_hash = "e7bbf1785686f9583c228ec6d26c9129130d5cd9e5761563fb3a2dee2cad196a"

# Function to compute SHA-256 twice
def double_sha256(text):
    return hashlib.sha256(hashlib.sha256(text.encode()).digest()).hexdigest()

# Brute-force search
try:
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
        for count, line in enumerate(f, 1):
            word = line.strip()
            computed_hash = double_sha256(word)

            if computed_hash == target_hash:
                print(f"\n Match found! Original input: {word}")
                exit()

            # Print progress every 100,000 words
            if count % 100000 == 0:
                print(f"Checked {count} words... No match yet.")

except FileNotFoundError:
    print(f" Error: Wordlist file '{wordlist_path}' not found. Please check the path.")

print("\n No match found in the provided wordlist.")

