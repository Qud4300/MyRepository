# BOJ 2010 Plug
import sys
input = sys.stdin.readline

n = int(input())
res = 0
for _ in range(n):
    res += int(input())
print(res-n+1)
