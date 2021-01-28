# BOJ 2110 router install
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])
l, r = 1, arr[-1] - arr[0]
res = 0
while l <= r:
    mid = (l + r) // 2
    count = 1
    cur = arr[0]
    for i in range(1, n):
        if cur + mid <= arr[i]:
            count += 1
            cur = arr[i]
    if count >= c:
        res = mid
        l = mid + 1
    else:
        r = mid - 1

print(res)
