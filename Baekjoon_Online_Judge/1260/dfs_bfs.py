import sys
from collections import deque
input = sys.stdin.readline

#DFS
def DFS(n, E, s):
    visited = [False]*(n+1)
    parent = [None]*(n+1)
    Stack = []
    res = ""
    Stack.append( (None,s) )
    while len(Stack) > 0:
        p, v = Stack.pop()
        if visited[v] == True:
            continue
        parent[v] = p
        visited[v] = True
        res+=(str(v)+" ")
        for w in reversed(E[v]):
            if visited[w] is False:
                Stack.append( (v,w) )
    return res


#BFS
def BFS(n, E, s):
    visited = [False]*(n+1)
    parent = [None]*(n+1)
    dist = [0]*(n+1)
    res = ""
    Queue = deque()
    Queue.append(s)
    while len(Queue) > 0 :
        v = Queue.popleft()
        if visited[v] == True:
            continue
        visited[v] = True
        res+=(str(v)+" ")
        for  w in E[v]:
            if visited[w] == False:
                Queue.append(w)
                parent[w] = v
                dist[w] = dist[v]+1
    return res


n, m, s = map(int, input().split())
E = []
for i in range(n+1):
    E.append([])# E[ [0]~[n]  ]
for i in range(m):
    a,b = map(int,input().split())
    E[a].append(b)
    E[b].append(a)
for i in E:
    i.sort()
print(DFS(n,E,s).strip())
print(BFS(n,E,s).strip())
