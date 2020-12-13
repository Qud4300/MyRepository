# BOJ 1967 Diameter of Tree 2
import sys
input = sys.stdin.readline

n = int(input())
edges = [[] for _ in range(n + 1)]
for _ in range(n-1):
    a,b,c = map(int, input().split())
    edges[a].append([b,c])
    edges[b].append([a,c])


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
