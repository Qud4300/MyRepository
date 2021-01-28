# BOJ 11286 absolute heap
import sys
from heapq import *
input = sys.stdin.readline

heap = []
res = ""
for _ in range(int(input())):
    a = int(input())
    if a == 0:
        try:
            res += str(heappop(heap)[1]) + '\n'
        except IndexError:
            res += "0\n"
    else:
        heappush(heap, (abs(a), a))
print(res)
