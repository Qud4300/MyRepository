# BOJ 2167 sum of 2D array
import sys
input = sys.stdin.readline
res = ""
n, m = map(int, input().split())
dp = [[0] * (m+1) for _ in range(n+1)]
arr = [[*map(int, input().split())] for _ in range(n)]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i][j-1] + dp[i - 1][j] + arr[i-1][j-1] - dp[i-1][j-1]
for k in range(int(input())):
    a, b, c, d = map(int, input().split())
    res += str(dp[c][d] - dp[c][b-1] - dp[a-1][d] + dp[a-1][b-1]) + '\n'
print(res.rstrip())
