# BOJ 1655 tell the median
import sys
from heapq import *
input = sys.stdin.readline

minHeap = []
maxHeap = []
res = ""
for _ in range(int(input())):
    a = int(input())
    if len(maxHeap) == len(minHeap):
        mid = a
        if minHeap and maxHeap:
            b,c = -heappop(maxHeap), heappop(minHeap)
            m,M = min(a,b,c),max(a,b,c)
            mid = a+b+c-m-M
            heappush(minHeap, M)
            heappush(maxHeap, -m)
        heappush(minHeap, mid)
        res += str(minHeap[0]) + '\n'
    else:
        b = heappop(minHeap)
        m,M = min(a,b), max(a,b)
        heappush(maxHeap, -m)
        heappush(minHeap, M)
        res += str(-maxHeap[0]) + '\n'

print(res.rstrip())
