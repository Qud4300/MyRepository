# BOJ 1520 Downhill
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    if x == 0 and y == 0:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if arr[x][y] < arr[nx][ny]:
                    dp[x][y] += dfs(nx, ny)
    return dp[x][y]

dp = [[-1] * n for i in range(m)]
print(dfs(m - 1, n - 1))