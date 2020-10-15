# BOJ 12865 knapsack
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
w = [0]
v = [0]
dp = [[0]*(k+1) for i in range(n+1)]
for i in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)
for i in range(1, n+1):
    for j in range(k, 0 , -1):
        if j - w[i] >= 0:
            dp[i][j] = max(dp[i-1][j], v[i] + dp[i-1][j-w[i]])
        else:
            dp[i][j] = dp[i-1][j]
print(max(dp[n]))
