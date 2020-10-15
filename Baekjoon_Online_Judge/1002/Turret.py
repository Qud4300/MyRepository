# BOJ 1002 Turret
import sys
import math
input = sys.stdin.readline
res = ''
n = int(input())
for _ in range(n):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if dist == 0 and r1 == r2:
        res += "-1\n"
    elif dist == r1+r2 or dist == max(r1,r2)-min(r1,r2):
        res += "1\n"
    elif max(r1,r2)-min(r1,r2) < dist < r1+r2:
        res += "2\n"
    else:
        res += "0\n"
print(res.rstrip())