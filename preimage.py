import hashlib

# Given hashes
md5_hashes = {
    "6c5c9ab391ebb120755269083208a9dc": None,
    "d5e1c7bdd57c6f832e0842309e56d77d": None
}

sha3_384_hashes = {
    "1916a518c207238c8008df950ca0aa3fbeb883d167c861331e5752630daf1b55629509be70c74c10d17ffe40b4f3fc8c": None,
    "127b1718d97717cafa427295ccbb4ba3e8b5607d1155e40769bb2404fd1f887eeb813f393b5ed7fcc2b969e8e8bba03a": None
}

# Path to your wordlist (modify this to match your file location)
wordlist_path = "rockyou.txt"
output_file = "found_hashes.txt"

def find_preimage(target_hashes, hash_function, hash_type):
    """Find the preimage for given hashes using a dictionary attack."""
    found = {}
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for word in f:
                word = word.strip()
                
                # Simulating OpenSSL hashing: `echo textgoeshere | openssl md5`
                # This includes a newline (\n) at the end
                hashed_word = hash_function((word + "\n").encode()).hexdigest()
                
                if hashed_word in target_hashes:
                    found[hashed_word] = word
                    print(f"Match found: {word} -> {hashed_word}")
                    
                    # Write match to a file
                    with open(output_file, "a", encoding="utf-8") as out_file:
                        out_file.write(f"{hash_type}: {word} -> {hashed_word}\n")
                    
                    if len(found) == len(target_hashes):
                        return found  # Stop when all hashes are found
    except FileNotFoundError:
        print("Wordlist file not found. Please provide a valid wordlist.")
    return found

# Finding MD5 preimages
print("Cracking MD5 hashes...")
md5_preimages = find_preimage(md5_hashes, hashlib.md5, "MD5")

# Finding SHA3-384 preimages
print("Cracking SHA3-384 hashes...")
sha3_384_preimages = find_preimage(sha3_384_hashes, hashlib.sha3_384, "SHA3-384")

print("\nMD5 Results:", md5_preimages)
print("\nSHA3-384 Results:", sha3_384_preimages)

