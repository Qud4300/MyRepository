import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())

if(B>=C):
    print(-1)
else:
    x = A/(C-B)
    print(int(x)+1)
