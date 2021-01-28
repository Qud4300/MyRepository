# BOJ 1956 Exercise

import sys

input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
route = [[INF] * (v + 1) for _ in range(v + 1)]
edges = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    edges[a].append(b)
    route[a][b] = min(route[a][b], c)
# using Floyd-Warshall algorithm
for k in range(1, v + 1):
    for i in range(1, v + 1):
        if i == k: continue
        for j in edges[k]:
            route[i][j] = min(route[i][j], route[i][k] + route[k][j])

cur_min = INF
for i in range(1, v + 1):
    if route[i][i] < cur_min:
        cur_min = route[i][i]

print(cur_min if cur_min != INF else -1)
