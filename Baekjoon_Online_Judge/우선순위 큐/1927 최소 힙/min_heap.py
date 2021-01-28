import sys
import heapq

h = []
res = ""
for _ in range(int(input())):
    val = int(sys.stdin.readline())
    if val == 0:
        if len(h):
            res += str(heapq.heappop(h)) + "\n"
        else:
            res += '0\n'
    else:
        heapq.heappush(h, val)
print(res)
