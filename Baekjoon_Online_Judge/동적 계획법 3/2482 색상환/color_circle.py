#BOJ 2482 ColorCircle
import sys

sys.setrecursionlimit(10000000)
D = 1000000003
n = int(input())
k = int(input())
dp = [[0] * (n + 1) for i in range(n + 1)]


def ColorCircle(n, k):
    if n == k*2:
        return 2
    if k == 1:
        return n
    if dp[n][k] == 0:
        total = (ColorCircle(n - 1, k) + ColorCircle(n - 2, k - 1)) % D
        dp[n][k] = total
        return total
    else:
        return dp[n][k]


if n < k*2:
    print(0)
else:
    print(ColorCircle(n, k))
