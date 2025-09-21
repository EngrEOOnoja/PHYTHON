import string
def summarize_letters(text):
    text = text.lower()


    cleaned = [ch for ch in text if ch.isalpha()]

    freq = {}
    for ch in cleaned:
        freq[ch] = freq.get(ch, 0) + 1

    summary = sorted(freq.items())

    return summary



sentence = "The quick brown fox jumps over the lazy dog!"
summary = summarize_letters(sentence)

for letter, count in summary:
    print(f"{letter}: {count}")

alphabet = set(string.ascii_lowercase)
contains_all = alphabet.issubset(set(ch for ch, _ in summary))

if contains_all:
    print("\nThe string has all the letters of the alphabet (a pangram).")
else:
    print("\nThe string does not contain all the letters of the alphabet.")
