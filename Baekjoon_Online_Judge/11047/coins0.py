# BOJ 11047 Coins 0 
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
count = 0
for i in range(n-1, -1, -1):
  if arr[i]<=k:
    count += k//arr[i]
    k %= arr[i]
print(count)