import re
from collections import Counter
text = "My email is hamza@gmail.com My email is hamza@gmail.com ok My email is hamza@gmail.com call me at +9200000000000"

words = text.split()
unique_words = 0

frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
        continue
    frequency[word] = 1


# print(frequency)


# 1. Regex for Email Addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# 2. Regex for Phone Numbers (supports international, hyphens, dots, and parens)
phone_pattern = r'\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)
common_word = Counter(words).most_common(2)


print(f"Emails found: {emails}")
print(f"Phone numbers found: {phones}")
print(f"Total Words: {len(words)}")
print(f"Common Words: {common_word}")
print(f"Unique Words: {len(frequency)}")