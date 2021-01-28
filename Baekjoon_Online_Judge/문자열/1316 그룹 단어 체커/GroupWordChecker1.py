# BOJ 1316 Group-Word Checker
import sys
input = sys.stdin.readline

n = int(input())
count = 0
for _ in range(n):
    word = input()
    prev = None
    characters = []
    for c in word:
        if prev != c:
            prev = c
            characters.append(c)
    if len(characters) == len(set(characters)):
        count += 1
print(count)