# BOJ 15681 Tree and Query
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def countSubtree(u):
    global visited, count

    visited[u] = True
    for v in edge[u]:
        if not visited[v]:
            countSubtree(v)
            count[u] += count[v]
    return count[u]


n, r, q = map(int, input().split())
edge = [[] for _ in range(n+1)]
visited = [False]*(n+1)
count = [1]*(n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

countSubtree(r)

for _ in range(q):
    print(count[int(input())])
