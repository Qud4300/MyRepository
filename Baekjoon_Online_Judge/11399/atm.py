# BOJ 11399 ATM
import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([*map(int, input().split())])
res = 0
for i in range(n):
    res += (n-i)*arr[i]
print(res)