#BOJ 2293 Coin 1
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

res = [0 for _ in range(k+1)]
res[0] = 1
for coin in coins:
    for i in range(1,k+1):
        if i-coin >= 0:
            res[i] += res[i-coin]
print(res[k])