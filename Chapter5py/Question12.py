from itertools import product

# Mapping digits to letters
digit_to_letters = {
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ"
}

def phone_words(phone_number):

    if len(phone_number) != 7 or any(d in "01" for d in phone_number):
        raise ValueError("Phone number must be 7 digits and cannot contain 0 or 1")


    letters_lists = [digit_to_letters[d] for d in phone_number]


    combos = product(*letters_lists)


    words = ["".join(c) for c in combos]

    return words



number = "7382273"
words = phone_words(number)

print(f"Total combinations: {len(words)}")
print("First 20 words:", words[:20])
