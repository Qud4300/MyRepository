# BOJ 10814 Age sort
import sys
input = sys.stdin.readline
n = int(input())
arr = [(i, input().split()) for i in range(n)]
for e in sorted(arr, key=lambda p: (int(p[1][0]), p[0])):
    print(e[1][0], e[1][1], sep=' ')
