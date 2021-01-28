# BOJ 1717 Disjoint Set
import sys

input = sys.stdin.readline


def findParent(v):
    if parent[v] == v:
        return v
    else:
        cur = parent[v]
        while cur != parent[cur]:
            cur = parent[cur]
        return cur


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for _ in range(m):
    o, a, b = map(int, input().split())
    if o == 0:
        a_par = findParent(a)
        b_par = findParent(b)
        if a_par != b_par:
            parent[min(a_par, b_par)] = max(a_par, b_par)
    else:
        print('YES' if findParent(a) == findParent(b) else 'NO')
