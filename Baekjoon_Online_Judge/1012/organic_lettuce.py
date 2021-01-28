# BOJ 1012 Organic Lettuce
import sys
input = sys.stdin.readline


def dfs(y, x):
    global arr
    global visited
    global cols, rows
    if visited[y][x] == 1:
        return 0
    else:
        queue = [(y,x)]
        while len(queue):
            a, b = queue.pop()
            visited[a][b] = 1
            if arr[a][b]:
                for i in range(-1, 2, 2):
                    if 0 <= a + i < rows and not visited[a + i][b]:
                        queue.append((a+i, b))
                    if 0 <= b + i < cols and not visited[a][b + i]:
                        queue.append((a, b+i))
    return 1


for t in range(int(input())):
    cols, rows, k = map(int, input().split())
    visited = [[0]*cols for row in range(rows)]
    arr = [[0]*cols for row in range(rows)]
    pts = []
    res = 0
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
        pts.append([y,x])
    for y,x in pts:
        res += dfs(y,x)
    print(res)