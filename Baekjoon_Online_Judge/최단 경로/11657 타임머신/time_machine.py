# BOJ 11657 Time machine
import sys

input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
edges = [[[] for __ in range(n+1)] if _ != 0 else [] for _ in range(n+1)]
# edges[0]: a list of edges' index.
# Actual weight of edge(u,v) is stored in edges[u][v].

for _ in range(m):
    a,b,c = map(int, input().split())
    if edges[a][b]:
        edges[a][b] = min(edges[a][b], c)
    else:
        edges[a][b] = c
        edges[0].append([a, b])


cost = [INF] * (n + 1)
cost[1] = 0
FLAG = False

for RELAXATION_CYCLE in range(n):
    for u, v in edges[0]:
        if cost[u] != INF and cost[v] > cost[u] + edges[u][v]:
            if RELAXATION_CYCLE == n-1: FLAG = True
            cost[v] = cost[u] + edges[u][v]
# Verification Phase
if FLAG:
    print(-1)
    exit(0)
# Print Phase
res = ""
for i in range(2, n + 1):
    res += str(cost[i] if cost[i] != INF else -1) + '\n'
print(res.rstrip())
