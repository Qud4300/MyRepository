# BOJ 2156 Wine Tasting
import sys
input = sys.stdin.readline

n = int(input())
arr = [0]+[int(input()) for _ in range(n)]
dp = [0]
dp.append(arr[1])
if n>1: dp.append(arr[1]+arr[2])
for i in range(3,n+1):
    dp.append(max(dp[i-2]+arr[i], dp[i-1], dp[i-3]+arr[i-1]+arr[i]))
print(dp[-1])
