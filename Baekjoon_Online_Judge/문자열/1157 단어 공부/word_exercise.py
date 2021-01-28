# BOJ 1157 Word Exercise
from collections import Counter

word = Counter(input().lower())
counts = Counter(word.values())
if counts[max(counts.keys())] > 1:
    print('?')
else:
    print(word.most_common()[0][0].upper())
