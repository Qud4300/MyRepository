# BOJ 2178 Maze Search
import sys
input = sys.stdin.readline

def bfs(arr, row, col):
    visited = [[0] * col for _ in range(row)]
    count = 0
    queue = [[(0, 0)]]
    visited[0][0] = 1
    while len(queue):
        count += 1
        stage = queue.pop()
        next_stage = []
        while len(stage):
            y, x = stage.pop()
            if (y, x) == (row - 1, col - 1):
                return count
            if y > 0 and not visited[y - 1][x] and arr[y - 1][x] == '1':
                next_stage.append((y - 1, x))
                visited[y-1][x] = 1
            if y < row - 1 and not visited[y + 1][x] and arr[y + 1][x] == '1':
                next_stage.append((y + 1, x))
                visited[y+1][x] = 1
            if x > 0 and not visited[y][x - 1] and arr[y][x - 1] == '1':
                next_stage.append((y, x - 1))
                visited[y][x-1] = 1
            if x < col - 1 and not visited[y][x + 1] and arr[y][x + 1] == '1':
                next_stage.append((y, x + 1))
                visited[y][x+1] = 1
        if next_stage:
            queue.append(next_stage)
    return count


n, m = map(int, input().split())
maze = [input() for _ in range(n)]
print(bfs(maze, n, m))
