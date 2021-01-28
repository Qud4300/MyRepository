# BOJ 2470 Two Solutions
import sys

n = int(input())
arr = sorted([*map(int, input().split())])

sol = sys.maxsize
l, r = 0, n-1
res = arr[l], arr[r]

while l < r:
    a, b = arr[l], arr[r]
    ab = abs(a+b)
    if ab < sol:
        sol = ab
        res = [a, b]
        if ab == 0:
            break
    if abs(arr[l+1] + b) < abs(a + arr[r-1]):
        l += 1
    else:
        r -= 1

print(*res)
