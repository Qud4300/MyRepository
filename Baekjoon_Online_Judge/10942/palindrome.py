# BOJ 10942 Palindrome?
import sys
input = sys.stdin.readline

n = int(input())
num = [0]+[*map(int, input().split())]
pal = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    pal[i][i] = 1
    if i < n and num[i] == num[i+1]:
        pal[i][i+1] = 1
        
for dis in range(0, n+1):
    for i in range(1, n+1):
        if i+dis <= n and pal[i][i+dis] == 0:
            if pal[i+1][i+dis-1] == 1 and num[i] == num[i+dis]:
                pal[i][i+dis] = 1

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(pal[a][b])

