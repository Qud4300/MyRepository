# BOJ 1707 Bipartite Graph
import sys
input = sys.stdin.readline


def bfs(stage):
    while stage:
        next_stage = []
        for vertex in stage:
            g = -group[vertex]
            for i in adj[vertex]:
                if group[i] == -g:
                    return True
                elif group[i] == 0:
                    group[i] = g
                    next_stage.append(i)
        stage = next_stage
    return False


for K in range(int(input())):
    v, e = map(int, input().split())
    adj = [[] for _ in range(v + 1)]
    edges = []
    group = [0 for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        edges.append([a, b])
        adj[a].append(b)
        adj[b].append(a)
    flag = True
    for a, b in edges:
        if group[a] != 0 and group[b] != 0 and group[a] == group[b]:
            flag = True
            break
        elif group[a] != group[b] != 0:
            continue
        elif group[a] == group[b] == 0:
            group[a] = 1
            q = [a]
        elif group[a] == 0:
            group[a] = -group[b]
            q = [a]
        elif group[b] == 0:
            group[b] = -group[a]
            q = [b]
        flag = bfs(q)
    print('NO' if flag else 'YES')
