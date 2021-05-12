# BOJ 6603 Lotto
import sys
from itertools import combinations as comb
input = sys.stdin.readline

tc = []
while True:
    arr = [*map(int, input().split())]
    if arr[0] == 0:
        break
    tc.append(arr)

for i in range(len(tc)):
    res = list(comb(tc[i][1:], 6))
    for c in res:
        print(*c)
    if i < len(tc)-1:
        print()
