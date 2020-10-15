# BOJ 2447 Star - 10
from collections import deque
size = int(input())
q = deque()
arr = [['*' for x in range(size)] for y in range(size)]
q.append((0,0,size))
while len(q):
    y,x,n = q.popleft()
    for i in range(n//3, n*2//3):
        for j in range(n//3, n*2//3):
            arr[y+i][x+j] = ' '
    if n>3:
        for i in range(3):
            for j in range(3):
                q.append((x+n*i//3,y+n*j//3,n//3))
for i in range(size):
    print(*arr[i], sep = '')