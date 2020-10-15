# BOJ 7576 Tomato
import sys
input = sys.stdin.readline

def bfs(arr, row, col, ripe, empty):
    global visited
    count = -1  # starting from day:0
    new_ripen = 0
    while len(ripen):
        stage = ripen.pop()
        next_stage = []
        count += 1
        while len(stage):
            y, x = stage.pop()
            if y > 0 and not visited[y - 1][x] and arr[y - 1][x] == 0:
                next_stage.append((y - 1, x))
                new_ripen += 1
                arr[y-1][x] = 1
                visited[y-1][x] = 1
            if y < row - 1 and not visited[y + 1][x] and arr[y + 1][x] == 0:
                next_stage.append((y + 1, x))
                new_ripen += 1
                arr[y + 1][x] = 1
                visited[y+1][x] = 1
            if x > 0 and not visited[y][x - 1] and arr[y][x - 1] == 0:
                next_stage.append((y, x - 1))
                new_ripen += 1
                arr[y][x-1] = 1
                visited[y][x-1] = 1
            if x < col - 1 and not visited[y][x + 1] and arr[y][x + 1] == 0:
                next_stage.append((y, x + 1))
                new_ripen += 1
                arr[y][x+1] = 1
                visited[y][x+1] = 1
        if next_stage:
            ripen.append(next_stage)
    if new_ripen!=row*col-ripe-empty:
        return -1
    return count


m, n = map(int, input().split())
tomato = []
ripen = [[]]
empty = 0
for i in range(n):
    row = [*map(int, input().split())]
    tomato.append(row)
    for j in range(len(row)):
        if row[j] == 1:
            ripen[0].append((i, j))
        if row[j] == -1:
            empty += 1
visited = [[0] * m for _ in range(n)]
print(bfs(tomato, n, m, len(ripen[0]), empty))
