def count_duplicate_words(sentence):
    words = sentence.lower().split()
    print(set(words))

sentence = "This is a test This test is only a test"
count_duplicate_words(sentence)
