import hashlib
import multiprocessing
import os

# 🔹 Path to CrackStation wordlist
wordlist_path = "realuniq.lst"  # Change this if needed

# 🔹 Target double SHA-256 hash
target_hash = "e7bbf1785686f9583c228ec6d26c9129130d5cd9e5761563fb3a2dee2cad196a"

# 🔹 Number of CPU cores to use
num_workers = multiprocessing.cpu_count()

# 🔹 Flag to stop all processes when a match is found
found_match = multiprocessing.Value("b", 0)

# 🔹 Function to compute SHA-256 twice
def double_sha256(word):
    """Computes SHA-256 twice and checks against the target hash."""
    if found_match.value == 1:
        return  # Stop processing if match is already found

    word = word.strip()
    computed_hash = hashlib.sha256(hashlib.sha256(word.encode()).digest()).hexdigest()

    if computed_hash == target_hash:
        with found_match.get_lock():  # Ensure only one process modifies the flag
            found_match.value = 1
        print(f"\n✅ Match found! Original input: {word}")

        # Force stop all processes
        os._exit(0)

# 🔹 Function to process a batch of words in parallel
def process_batch(words):
    """Processes a batch of words in parallel."""
    with multiprocessing.Pool(num_workers) as pool:
        pool.map(double_sha256, words)

# 🔹 Stream and process the wordlist efficiently
def crack_hash():
    """Streams and processes the wordlist without overloading memory."""
    batch_size = 100000  # Process 100,000 words at a time
    batch = []

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for count, line in enumerate(f, 1):
                if found_match.value == 1:
                    break  # Stop if match already found

                batch.append(line.strip())

                # Process batch when it reaches batch_size
                if count % batch_size == 0:
                    process_batch(batch)
                    batch = []  # Reset batch

                # Print progress every 10 million words
                if count % 10000000 == 0:
                    print(f"🔍 Checked {count:,} words... No match yet.")

        # Process remaining words in the last batch
        if batch and found_match.value == 0:
            process_batch(batch)

    except FileNotFoundError:
        print(f"❌ Error: Wordlist file '{wordlist_path}' not found. Please check the path.")

    if found_match.value == 0:
        print("\n❌ No match found in the provided wordlist.")

# 🔹 Run the Brute-Forcer
if __name__ == "__main__":
    crack_hash()

