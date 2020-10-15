# BOJ 1654 Cutting Lan-Cable
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = sorted([int(input()) for _ in range(k)])

curMax = 0
l, r = 1, arr[-1]
while l <= r:
    mid = (l+r)//2
    count = sum([l//mid for l in arr])
    if count < n:
        r = mid-1
    else:
        l = mid+1
        curMax = max(curMax, mid)

print(curMax)