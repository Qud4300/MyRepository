# BOJ 2217 Rope
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)

cur_max = 0
count = 1
for i in arr:
    cur_max = max(cur_max, count*i)
    count += 1
print(cur_max)
