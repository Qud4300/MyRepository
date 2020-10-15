# BOJ 1931 Meeting room assignment
import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([[*map(int, input().split())] for _ in range(n)], key=lambda x: (x[1],x[0]))

res = 0
cur_end = 0
for s, e in arr:
    if cur_end <= s:
        cur_end = e
        res += 1
print(res)
