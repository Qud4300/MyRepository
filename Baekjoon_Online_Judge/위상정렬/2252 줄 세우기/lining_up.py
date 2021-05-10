# BOJ 2252 Lining up
import sys
input = sys.stdin.readline


def findParent(v: int, edges: dict):
    cur = v
    while cur in edges and edges[cur]:
        cur = edges[cur][0]
    return cur


n, m = map(int, input().split())
pre = dict()
post = dict()
for _ in range(m):
    a, b = map(int, input().split())
    if b not in pre:
        pre[b] = []
    if a not in post:
        post[a] = []
    pre[b].append(a)
    post[a].append(b)

targets = [i for i in range(1, n+1)]
sequence = []

while targets:
    node = findParent(targets[0], pre)
    while node in post and post[node]:
        sequence.append(node)
        targets.remove(node)
        for i in post[node]:
            pre[i].remove(node)
        node = findParent(post[node][0], pre)
    sequence.append(node)
    targets.remove(node)

print(*sequence)
