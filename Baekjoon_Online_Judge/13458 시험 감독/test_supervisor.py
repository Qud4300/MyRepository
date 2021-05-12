# BOJ 13458 시험 감독
import math
import sys

input = sys.stdin.readline

n = int(input())
arr = [*map(int, input().split())]
b,c = map(int, input().split())
res = 0
for i in range(n):
    if arr[i] > b:
        res += math.ceil((arr[i]-b)/c)
    res += 1
print(res)
