# BOJ 11779 Minimum Cost 2 - SPFA
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
start, end = map(int, input().split())
route = [[sys.maxsize, -1] for i in range(n+1)]
route[start] = [0, -1]
queue = [start]

while queue:
    next_stage = []
    for u in queue:
        for v, c in arr[u]:
            if route[v][0] > route[u][0] + c:
                route[v] = [route[u][0] + c, u]
                if v not in next_stage:
                    next_stage.append(v)
    queue = next_stage

cur = end
count = 0
res = ""
while cur != -1:
    res = str(cur) + ' ' + res
    cur = route[cur][1]
    count += 1

print(route[end][0])
print(count)
print(res.rstrip())
