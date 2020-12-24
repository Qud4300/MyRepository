# BOJ 2098 Traveling Salesman Problem
import sys
input = sys.stdin.readline
INF = sys.maxsize


def TSP(prev, bitmask):
    global n
    if bitmask == (1 << n) - 1: # if n==3, maximum mask is 111 == 7 == 2**3-1
        # visited all cities.
        return w[prev][0] if w[prev][0] else INF

    if dp[prev][bitmask]:
        return dp[prev][bitmask]

    res = INF
    for city in range(n):
        if bitmask & (1 << city) == 0 and w[prev][city] != 0:
            # not visited and way exists
            res = min(res, TSP(city, bitmask | (1 << city)) + w[prev][city])
    dp[prev][bitmask] = res
    return res


n = int(sys.stdin.readline())
w = [[*map(int, input().split())] for _ in range(n)]
dp = [[None] * (1 << n) for _ in range(n)]

print(TSP(0, 1 << 0))
