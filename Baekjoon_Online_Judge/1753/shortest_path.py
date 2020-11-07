# BOJ 1753 Shortest Path
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

INF = sys.maxsize
v, e = map(int, input().split())
s = int(input())
edges = [[]for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])

queue = [(0, s)]
cost = [INF] * (v + 1)
cost[s] = 0

while len(queue):
    weight, node = heappop(queue)
    for t, c in edges[node]:
        new_cost = weight+c
        if new_cost < cost[t]:
            cost[t] = new_cost
            heappush(queue, (new_cost, t))

res = ''
for c in cost[1:]:
    res += str(c if c != INF else 'INF') + '\n'
print(res.rstrip())