# BOJ 7579 App
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mem = [*map(int, input().split())]
cost = [*map(int, input().split())]

cost_max = sum(cost)
dp = [-1] * (cost_max+1)
dp[0] = 0
for i in range(n):
    for j in range(cost_max - cost[i], -1,-1):
        if dp[j] != -1:
            dp[j + cost[i]] = max(dp[j + cost[i]], dp[j] + mem[i])

for i in range(cost_max + 1):
    if dp[i] >= m:
        print(i)
        break
