#BOJ 2178 Maze Search
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
visited = [[0]*m for _ in range(n)]
s = [[(0, 0)]]
res = []
curMin = n*m

def bfs(stack):
    global curMin
    while len(stack[-1]):
        y, x = stack[-1].pop()
        visited[y][x] = 1
        if (y, x) == (n-1, m-1):
            res.append(len(stack))
            curMin = min(res)
        else:
            new_stack = []
            for i in range(-1, 2, 2):
                if m > x+i >= 0 and arr[y][x+i] == '1' and visited[y][x+i] == 0:
                    new_stack.append((y, x+i))
                if n > y+i >= 0 and arr[y+i][x] == '1' and visited[y+i][x] == 0:
                    new_stack.append((y+i, x))
            if len(new_stack):
                stack.append(new_stack)
                bfs(stack)
        visited[y][x] = 0
        if len(stack) >= curMin:
            break
    stack.pop()
    return


bfs(s)
print(min(res))
