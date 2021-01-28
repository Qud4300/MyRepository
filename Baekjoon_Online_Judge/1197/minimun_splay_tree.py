# BOJ 1197 Minimum Spanning Tree
import sys
input = sys.stdin.readline


def Find(x):
    if p[x] == x:
        return x
    else:
        y = Find(p[x])
        p[x] = y
        return y


def Union(x, y):
    x = Find(x)
    y = Find(y)
    if x != y:
        p[y] = x


v, e = map(int, input().split())
edges=[]
p=[i for i in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append([c,a,b])

edges.sort(key=lambda x: x[0])

edge_count = 0
cost = 0
for i in range(e):
    c, start, end = edges[i]
    if Find(start)!=Find(end):
        Union(start,end)
        cost += c
        edge_count += 1
    if edge_count==v-1:
        break

print(cost)
