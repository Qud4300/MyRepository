# BOJ 11049 Matmul
import sys
input = sys.stdin.readline
INF = 2**31
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
for i in range(1, n):
    for j in range(n - i):
        a = j + i
        dp[j][a] = INF
        for k in range(j, a):
            dp[j][a] = min(dp[j][a], dp[j][k] + dp[k + 1][a] + s[j][0] * s[k][1] * s[a][1])
print(dp[0][n - 1])