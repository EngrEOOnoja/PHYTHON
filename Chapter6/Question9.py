def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    stack = []
    for char in cleaned:
        stack.append(char)
    for char in cleaned:
        if char != stack.pop():
            return False
    return text


word = "radar"
print(is_palindrome(word)
)