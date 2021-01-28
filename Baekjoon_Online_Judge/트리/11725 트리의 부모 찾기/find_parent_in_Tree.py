# BOJ 11725 Find Parent in Tree

import sys
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n+1)]
par = [0 for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(nodes):
    global arr, par
    queue = [[1]]
    visited = [False for _ in range(nodes+1)]
    while queue:
        stage = queue.pop()
        next_stage = []
        for i in stage:
            for j in arr[i]:
                if not visited[j]:
                    par[j] = i
                    next_stage.append(j)
                    visited[j] = True
        if next_stage:
            queue.append(next_stage)
    return

bfs(n)
for i in range(2,n+1):
    print(par[i])

