# BOJ 11780 Floyd 2
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
route = [[[sys.maxsize, []] for __ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    route[i][i][0] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    if route[a][b][0] > c:
        route[a][b][0] = c
        route[a][b][1] = [a, b]

for k in range(1, n+1):
    for i in range(1, n + 1):
        if i == k:
            continue
        for j in range(1, n + 1):
            if j == k or j == i:
                continue
            ikj = route[i][k][0]+route[k][j][0]
            if route[i][j][0] > ikj:
                route[i][j][0] = ikj
                route[i][j][1] = route[i][k][1] + route[k][j][1][1:]

for i in range(1,n+1):
    print(*[route[i][j][0] if route[i][j][0] != sys.maxsize else 0 for j in range(1, n+1)])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(len(route[i][j][1]), *route[i][j][1])

