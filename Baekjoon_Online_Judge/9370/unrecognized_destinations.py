# BOJ 9370 Unrecognized Destination
import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = sys.maxsize
res = ""


def dijkstra(start):
    global cost
    cost[start][start] = 0
    heap = []
    heappush(heap, (0, start))
    while heap:
        w, u = heappop(heap)
        for v, c in edges[u]:
            if cost[start][v] > w + c:
                cost[start][v] = w + c
                cost[v][start] = w + c
                heappush(heap, (w + c, v))


for TestCase in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    edges = [[] for _ in range(n + 1)]

    for road in range(m):
        a, b, d = map(int, input().split())
        edges[a].append([b, d])
        edges[b].append([a, d])

    target = [int(input()) for _ in range(t)]
    cost = [[INF] * (n + 1) for _ in range(n + 1)]
    dest = []
    dijkstra(s)
    dijkstra(g)
    dijkstra(h)
    p1, p2 = cost[s][g] + cost[g][h], cost[s][h] + cost[h][g]
    for tar in target:
        if cost[s][tar] in (p1 + cost[h][tar], p2 + cost[g][tar]):
            dest.append(tar)
    print(*sorted(dest), sep=' ')
