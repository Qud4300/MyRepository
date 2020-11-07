# BOJ 2206 Breakthrough
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [input() for _ in range(n)]
visited = []


def bfs(arr, rows, cols):
    global visited
    visited = [[[0] * 2 for __ in range(m)] for _ in range(n)]
    visited[0][0] = [1, 1]
    queue = [[(0, 0, 0)]]
    count = 0
    while len(queue):
        count += 1
        stage = queue.pop()
        next_stage = []
        while len(stage):
            y, x, breach = stage.pop()
            if y == rows - 1 and x == cols - 1:
                #  because it is BFS solution, result is always a smallest count.
                return count
            for a, b in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
                if 0 <= a < rows and 0 <= b < cols and not visited[a][b][breach]:
                    # if next step is available, whether breach is available or not, just add to next stage.
                    if arr[a][b] == '0':
                        next_stage.append((a, b, breach))
                        visited[a][b][breach] = count
                    # if next step isn't available but worth breaching and also available, then add to next stage.
                    elif arr[a][b] == '1' and breach == 0:
                        for c, d in {(a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)} - {(y, x)}:
                            if 0 <= c < rows and 0 <= d < cols and not visited[c][d][1] and arr[c][d] == '0':
                                next_stage.append((a, b, 1))
                                visited[a][b][1] = count
                                break
        if len(next_stage):
            queue.append(next_stage)
    return -1


print(bfs(maze, n, m))
