# BOJ 2805 Cutting Tree -pypy3
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [*map(int, input().split())]

curMax = 0
l, r = m//n, max(arr)
while l <= r:
    cut = (l + r) // 2
    total = sum([max(0, tree - cut) for tree in arr])
    if total < m:
        r = cut - 1
    else:
        l = cut + 1
        curMax = cut
        if total == m:
            break

print(curMax)