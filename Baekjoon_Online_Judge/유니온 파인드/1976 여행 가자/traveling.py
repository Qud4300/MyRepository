# BOJ 1976 Traveling
import sys
input = sys.stdin.readline


def findParent(v):
    if par[v] == v:
        return v
    else:
        cur = par[v]
        while par[cur] != cur:
            cur = par[cur]
        return cur


n = int(input())
m = int(input())
par = [i for i in range(n+1)]
arr = [[0]*(n+1)]+[[0, *map(int, input().split())] for _ in range(n)]
for i in range(1,n+1):
    for j in range(i+1, n+1):
        i_par = findParent(i)
        j_par = findParent(j)
        if i_par != j_par and arr[i][j] == 1:
            par[j_par] = i_par
PAR = None
for r in [*map(int, input().split())]:
    if PAR is None:
        PAR = findParent(r)
        continue
    else:
        if PAR != findParent(r):
            print('NO')
            exit(0)
print('YES')
