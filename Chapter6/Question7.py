def count_letters(sentence):
    sentence = sentence.lower().replace(" ", "")
    letter_counts = {}

    for char in sentence:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1

    print(f"{'Letter':<8}{'Count'}")
    print('=' * 15)

    for letter in sorted(letter_counts):
        print(f"{letter:<8}{letter_counts[letter]}")


    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    present_letters = set(letter_counts.keys())
    missing_letters = alphabet - present_letters

    print("\nMissing letters from the alphabet:")
    if(missing_letters < 1 ):
        print("\n No Missing letters from the alphabet.")
    print(" ".join(sorted(missing_letters)))


# Get input from the user
user_input = input("Enter a sentence (no punctuation): ")
count_letters(user_input)
