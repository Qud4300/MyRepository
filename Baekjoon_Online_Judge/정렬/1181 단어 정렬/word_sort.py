# BOJ 1181 Word sort
import sys
input = sys.stdin.readline
n = int(input())
arr = set(input() for _ in range(n))
for word in sorted(arr, key = lambda w: (len(w), w)):
    print(word, end = '')