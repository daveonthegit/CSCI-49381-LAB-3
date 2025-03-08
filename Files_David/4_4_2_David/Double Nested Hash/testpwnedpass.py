import hashlib

# File paths
input_file = "pwnedpass.txt"
hash_to_match = "e7bbf1785686f9583c228ec6d26c9129130d5cd9e5761563fb3a2dee2cad196a"

# Function to compute nested SHA-256 hash
def nested_sha256(password: str) -> str:
    first_hash = hashlib.sha256(password.encode()).hexdigest()
    second_hash = hashlib.sha256(first_hash.encode()).hexdigest()
    return second_hash

# Process the input file and compare hashes
with open(input_file, "r", encoding="utf-8") as infile:
    for line in infile:
        password = line.strip()
        if password:  # Ensure no empty lines are processed
            hashed_password = nested_sha256(password)
            if hashed_password == hash_to_match:
                print(f"Match found: {password}")
                break
    else:
        print("No match found.")

