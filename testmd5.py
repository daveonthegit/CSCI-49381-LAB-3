import hashlib

# Test word
test_word = "tactical"

# Simulate OpenSSL hashing behavior
# Equivalent to: echo textgoeshere | openssl md5  (with newline)
md5_with_newline = hashlib.md5((test_word + "\n").encode()).hexdigest()

# Equivalent to: echo -n textgoeshere | openssl md5  (no newline)
md5_without_newline = hashlib.md5(test_word.encode()).hexdigest()

print(f"MD5 with newline: {md5_with_newline}")
print(f"MD5 without newline: {md5_without_newline}")

