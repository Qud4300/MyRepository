# BOJ 11404 Floyd Warshall
import sys
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
arr = [[INF for __ in range(n)] for _ in range(n)]

for _ in range(m):
    a,b,c = map(int, input().split())
    if arr[a-1][b-1] > c:
        arr[a-1][b-1] = c

for t in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][t]+arr[t][j] < arr[i][j]:
                arr[i][j] = arr[i][t]+arr[t][j]

res = ""
for i in range(n):
    for j in range(n):
        if i==j or arr[i][j]==INF:
            arr[i][j] = 0
    print(*arr[i])