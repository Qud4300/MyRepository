# BOJ 9375 Fashionista ShinHaebin
import sys
from functools import reduce
input = sys.stdin.readline

n = int(input())
res = ""
for _ in range(n):
    d = dict()
    for i in range(int(input())):
        a, b = input().split()
        try:
            d[b] += 1
        except KeyError:
            d[b] = 1
    res += str(reduce(lambda acc, idx: acc * (d[idx]+1), d, 1)-1) + '\n'
print(res.rstrip())
