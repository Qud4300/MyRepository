# BOJ 17404 RGB Distance 2

import sys

input = sys.stdin.readline


def RGB(n, cost):
    res = sys.maxsize
    for t in range(3):
        dp = [[0 for _ in range(3)] for __ in range(n)]
        # init first color
        for color in range(3):
            if color == t:
                dp[0][color] = cost[0][color]
            else:
                dp[0][color] = sys.maxsize
        for i in range(1, n):
            dp[i][0] = cost[i][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = cost[i][2] + min(dp[i - 1][1], dp[i - 1][0])

        for i in range(3):
            if i == t:
                continue
            res = min(res, dp[-1][i])

    return res


N = int(input())
C = [[*map(int, input().split())] for _ in range(N)]
print(RGB(N, C))
