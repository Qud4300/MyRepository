# BOJ 1316 Group-Word Checker
import sys
input = sys.stdin.readline

count = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        count += 1
print(count)