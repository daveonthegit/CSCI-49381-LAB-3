import hmac
import hashlib

# Replace these with the found key and text
key = "Adele"
text = "Miller"

# Target hash to verify against
target_hash = "8b5a3e95656026f9ce2f405e279adf06"

# Compute HMAC-MD5
computed_hash = hmac.new(key.encode(), text.encode(), hashlib.md5).hexdigest()

# Print and Compare
print(f"Computed Hash: {computed_hash}")
print(f"Matches Target? {computed_hash == target_hash}")

