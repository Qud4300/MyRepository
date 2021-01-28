# BOJ 3036 Ring
from math import gcd

n = int(input())
arr = [*map(int, input().split())]
for i in range(1, n):
    m = gcd(arr[0], arr[i])
    print(str(arr[0] // m) + '/' + str(arr[i] // m))
