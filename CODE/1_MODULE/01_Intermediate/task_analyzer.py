import re
from collections import Counter


# -------------------- INPUT TEXT --------------------
text = (
    "My email is hamza@gmail.com "
    "My email is hamza@gmail.com ok "
    "My email is hamza@gmail.com "
    "call me at +9200000000000"
)


# -------------------- WORD PROCESSING --------------------
# Split text into words
words = text.split()

# Dictionary to store word frequencies
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1


# -------------------- REGEX PATTERNS --------------------
# Email pattern
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Phone number pattern (international support)
phone_pattern = r"\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"


# -------------------- REGEX SEARCH --------------------
emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)


# -------------------- ANALYSIS --------------------
common_words = Counter(words).most_common(2)
total_words = len(words)
unique_words = len(frequency)


# -------------------- OUTPUT --------------------
print("Text Analysis Report")
print("-" * 25)

print(f"Emails found       : {emails}")
print(f"Phone numbers found: {phones}")
print(f"Total words        : {total_words}")
print(f"Unique words       : {unique_words}")
print(f"Most common words  : {common_words}")
