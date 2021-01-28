# BOJ 9251 LCS
import sys
input = sys.stdin.readline
a = input().rstrip()
b = input().rstrip()
dp = [[0]*(len(b)+1) for i in range(len(a)+1)]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

print(dp[len(a)][len(b)])
