# BOJ 2565 Electric Wire
import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([[*map(int, input().split())] for _ in range(n)], key =lambda x: x[0])
dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if arr[i][1] > arr[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(n - max(dp))