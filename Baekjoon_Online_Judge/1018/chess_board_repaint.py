import sys

n, m = map(int,input().split())
arr = [sys.stdin.readline().rstrip() for i in range(n)]
res = []
for i in range(n-7):
    for j in range(m-7):
        count = 0
        for y in range(8):
            for x in range(8):
                if (bool((x+y) % 2)*'W' + bool((x+y+1) % 2)*'B') != arr[i+y][j+x]:
                    count += 1
        res.append(min(count, 64-count))
print(min(res))