import hashlib
import subprocess

# Paths to input and output files
wordlist_path = "rockyou.txt"  # Change if needed
precomputed_sha256_path = "rockyou_sha256.txt"
hash_file_path = "john_hash.txt"
formatted_hash_path = "formatted_john_hash.txt"
jtr_format = "raw-sha256"

# Step 1: Precompute SHA-256 for each word in the wordlist
print("🔹 Step 1: Precomputing first SHA-256 layer...")
with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as infile, open(precomputed_sha256_path, "w", encoding="utf-8") as outfile:
    for line in infile:
        word = line.strip()
        if word:
            sha256_hash = hashlib.sha256(word.encode()).hexdigest()
            outfile.write(sha256_hash + "\n")

print(f"✅ SHA-256 precomputed wordlist saved to {precomputed_sha256_path}")

# Step 2: Extract valid SHA-256 hashes from input file
print("🔹 Step 2: Extracting valid SHA-256 hashes...")

valid_hashes = []
with open(hash_file_path, "r", encoding="utf-8") as hash_file:
    for line in hash_file:
        hash_candidate = line.strip().split(":")[-1]  # Extract last part (handles user:hash format)
        if len(hash_candidate) == 64 and all(c in "0123456789abcdefABCDEF" for c in hash_candidate):
            valid_hashes.append(hash_candidate)

# Check if we found valid hashes
if not valid_hashes:
    print("❌ No valid SHA-256 hashes found! Check your input file.")
else:
    with open(formatted_hash_path, "w", encoding="utf-8") as formatted_file:
        formatted_file.write("\n".join(valid_hashes) + "\n")
    print(f"✅ Extracted {len(valid_hashes)} valid SHA-256 hashes.")

# Step 3: Run John the Ripper if we have valid hashes
if valid_hashes:
    print("🔹 Step 3: Running John the Ripper...")
    jtr_command = ["john", "--wordlist=" + precomputed_sha256_path, "--format=" + jtr_format, formatted_hash_path]

    try:
        subprocess.run(jtr_command, check=True)
        print("✅ John the Ripper execution completed!")
    except subprocess.CalledProcessError as e:
        print("❌ Error running John the Ripper:", e)
