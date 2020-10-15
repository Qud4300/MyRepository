# BOJ 11054 Longest Bitonic Subsequence
import sys
input = sys.stdin.readline

n = int(input())
arr = [*map(int, input().split())]

dpF = [0 for _ in range(n)]  # search forward; increasing order
dpB = [0 for _ in range(n)]  # search backward; decreasing order
dp = [0 for _ in range(n)]  # merge dpF and dpB
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dpF[i] < dpF[j]:
            dpF[i] = dpF[j]
    dpF[i] += 1
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if arr[j] < arr[i] and dpB[i] < dpB[j]:
            dpB[i] = dpB[j]
    dpB[i] += 1
for i in range(n):
    dp[i] = dpF[i] + dpB[i] -1
print(max(dp))