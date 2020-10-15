# BOJ 11066 Merging Files -pypy3
import sys
input = sys.stdin.readline
res = ""
for _ in range(int(input())):
    k = int(input())
    page = [*map(int, input().split())]
    dp = [[0] * k for _ in range(k)]
    for i in range(k - 1):
        dp[i][i + 1] = page[i] + page[i + 1]
        for j in range(i + 2, k):
            dp[i][j] = dp[i][j - 1] + page[j]
    for d in range(2, k):
        for i in range(k-d):
            j = i+d
            minimum = [dp[i][k] + dp[k + 1][j] for k in range(i, j)]
            dp[i][j] += min(minimum)
    res += str(dp[0][k - 1]) + '\n'

print(res.rstrip())