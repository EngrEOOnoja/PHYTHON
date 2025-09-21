from collections import Counter

text = 'to be or not to be that is the question'
counter = Counter(text.split())

for words, count in sorted(counter.items()):
    print(f'{words:<12} {count}')


