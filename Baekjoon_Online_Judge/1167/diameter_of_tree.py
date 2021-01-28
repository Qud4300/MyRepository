# BOJ 1167 Tree's diameter
import sys
input = sys.stdin.readline

n = int(input())
m = 0
edges = [[] for _ in range(n + 1)]


for _ in range(n):
    L = [*map(int, input().split())]
    for i in range(1, len(L) - 2, 2):
        edges[L[0]].append([L[i], L[i + 1]])


def bfs(a, size):
    global edges
    cost = [0 for _ in range(n + 1)]
    visited = [False]*(size+1)
    visited[a] = True
    M = [a,0]
    queue = [[a]]
    while queue:
        stage = queue.pop()
        new_stage = []
        while stage:
            i = stage.pop()
            for u,w in edges[i]:
                if not visited[u]:
                    visited[u] = True
                    cost[u] = cost[i] + w
                    if cost[u] > M[1]:
                        M = [u,cost[u]]
                    new_stage.append(u)
        if new_stage:
            queue.append(new_stage)
    return M


x,a = bfs(1,n)
y,b = bfs(x,n)

print(b)
