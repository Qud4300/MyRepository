# BOJ 7576 Tomato
import sys
input = sys.stdin.readline


def bfs(arr, box, row, col, ripe, empty):
    global visited
    count = -1  # starting from day:0
    new_ripen = 0
    while len(ripen):
        stage = ripen.pop()
        next_stage = []
        count += 1
        while len(stage):
            z, y, x = stage.pop()
            if z > 0 and not visited[z - 1][y][x] and arr[z - 1][y][x] == 0:
                next_stage.append((z - 1, y, x))
                new_ripen += 1
                arr[z - 1][y][x] = 1
                visited[z - 1][y][x] = 1
            if z < box - 1 and not visited[z + 1][y][x] and arr[z + 1][y][x] == 0:
                next_stage.append((z + 1, y, x))
                new_ripen += 1
                arr[z + 1][y][x] = 1
                visited[z + 1][y][x] = 1
            if y > 0 and not visited[z][y - 1][x] and arr[z][y - 1][x] == 0:
                next_stage.append((z, y - 1, x))
                new_ripen += 1
                arr[z][y - 1][x] = 1
                visited[z][y - 1][x] = 1
            if y < row - 1 and not visited[z][y + 1][x] and arr[z][y + 1][x] == 0:
                next_stage.append((z, y + 1, x))
                new_ripen += 1
                arr[z][y + 1][x] = 1
                visited[z][y + 1][x] = 1
            if x > 0 and not visited[z][y][x - 1] and arr[z][y][x - 1] == 0:
                next_stage.append((z, y, x - 1))
                new_ripen += 1
                arr[z][y][x - 1] = 1
                visited[z][y][x - 1] = 1
            if x < col - 1 and not visited[z][y][x + 1] and arr[z][y][x + 1] == 0:
                next_stage.append((z, y, x + 1))
                new_ripen += 1
                arr[z][y][x + 1] = 1
                visited[z][y][x + 1] = 1
        if next_stage:
            ripen.append(next_stage)
    if new_ripen != box * row * col - ripe - empty:
        return -1
    return count


m, n, h = map(int, input().split())
tomato = []
ripen = [[]]
empty = 0
for level in range(h):
    box = []
    for i in range(n):
        row = [*map(int, input().split())]
        box.append(row)
        for j in range(len(row)):
            if row[j] == 1:
                ripen[0].append((level, i, j))
            if row[j] == -1:
                empty += 1
    tomato.append(box)
visited = [[[0] * m for _ in range(n)] for __ in range(h)]
print(bfs(tomato, h, n, m, len(ripen[0]), empty))
