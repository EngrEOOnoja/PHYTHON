def count_duplicate_words(sentence):
    words = sentence.lower().split()

    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    duplicates = {word: count for word, count in word_counts.items() if count > 1}

    print("Duplicate words and their counts:")
    for word, count in duplicates.items():
        print(f"{word}: {count}")

    print(f"\nTotal number of duplicate words: {len(duplicates)}")

sentence = "This is a test This test is only a test"
count_duplicate_words(sentence)
