# BOJ 1504 Specific shortest path
import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = sys.maxsize

n, e = map(int, input().split())
edges = [[] for _ in range(n+1)]
cost = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

v1, v2 = map(int, input().split())


def dijkstra(s):
    heap = []
    cost[s][s] = 0  # don't forget it! 
    heappush(heap, (0, s, s))
    while heap:
        w, u, v = heappop(heap)
        for t, c in edges[v]:
            if w + c < cost[u][t]:
                cost[u][t] = w + c
                cost[t][u] = w + c
                heappush(heap, (w + c, u, t))


dijkstra(1)
dijkstra(v1)
dijkstra(v2)

p1, p2 = INF, INF
if cost[1][v1] != INF and cost[v1][v2] != INF and cost[v2][n] != INF:
    p1 = cost[1][v1] + cost[v1][v2] + cost[v2][n]
if cost[1][v2] != INF and cost[v2][v1] != INF and cost[v1][n] != INF:
    p2 = cost[1][v2] + cost[v2][v1] + cost[v1][n]

print(-1 if p1 == p2 == INF else min(p1, p2))
