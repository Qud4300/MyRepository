# BOJ 20040 Cycle Game
import sys
input = sys.stdin.readline


def findParent(v):
    while par[v] != v:
        v = par[v]
    return v


n, m = map(int, input().split())
par = [i for i in range(n)]
size = [1 for _ in range(n)]

for i in range(1,m+1):
    a, b = map(int, input().split())
    a_par, b_par = findParent(a), findParent(b)
    if a_par != b_par:
        if size[a_par] > size[b_par]:
            a_par, b_par = b_par, a_par
        par[a_par] = b_par
        size[b_par] = max(size[b_par], size[a_par]+1)
    else:
        print(i)
        exit(0)

print(0)
