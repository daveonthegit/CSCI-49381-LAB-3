import PyPDF2

# Path to the PDF file
pdf_path = "lab-crypto2.pdf"
wordlist_output = "wordlist.txt"

# Extract text from PDF
with open(pdf_path, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

# Process and save words
words = set(text.split())  # Remove duplicates
with open(wordlist_output, "w", encoding="utf-8") as f:
    f.write("\n".join(words))

print(f"Generated wordlist: {wordlist_output}")

