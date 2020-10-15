# BOJ 2981 Check
import sys
import math
input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)])
temp = []
res = []
m = 0
for i in range(1, n):
    m = math.gcd(m, arr[i] - arr[i - 1])
for i in range(2, int(m**0.5) + 1):
    if m % i == 0:
        res.append(i)
        res.append(m // i)
print(*sorted([*set(res + [m])]), sep=' ')
