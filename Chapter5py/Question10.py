def anagrams(s):
    if len(s) <= 1:
        return [s]

    result = []
    for i, char in enumerate(s):
        remaining = s[:i] + s[i+1:]

        for anagram in anagrams(remaining):
            result.append(char + anagram)

    return result

