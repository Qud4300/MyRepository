import sys

input = sys.stdin.readline

n = int(input())
arr = [input() for _ in range(n)]
visited = [[0] * n for _ in range(n)]
queue = []
complex = []

for row in range(n):
    for col in range(n):
        if arr[row][col] == '1' and visited[row][col] == 0:
            visited[row][col] = 1
            queue = [(row, col)]
            com = 1
            while len(queue) > 0:
                a, b = queue.pop(0)
                for d in range(-1, 2, 2):
                    if n > (a + d) >= 0 and arr[a+d][b] == '1' and visited[a+d][b] == 0:
                        queue.append((a + d, b))
                        com += 1
                        visited[a + d][b] = 1
                    if n > (b + d) >= 0 and arr[a][b+d] == '1' and visited[a][b+d] == 0:
                        queue.append((a, b+d))
                        com += 1
                        visited[a][b+d] = 1
            complex.append(com)

print(len(complex))
for com in sorted(complex):
    print(com)

