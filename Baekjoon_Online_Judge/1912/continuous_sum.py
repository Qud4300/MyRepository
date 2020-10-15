# BOJ 1912 Continuous Sum
import sys
input = sys.stdin.readline

n = int(input())
arr = [*map(int, input().split())]
dp = [0] * n
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1]+arr[i])
print(max(dp))