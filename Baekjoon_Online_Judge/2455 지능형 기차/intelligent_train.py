# BOJ 2455 Intelligent Train

station = [0]*4
cur = 0
MAX = 0
for _ in range(4):
    land, board = map(int, input().split())
    cur = cur - land + board
    MAX = max(MAX, cur)
print(MAX)
