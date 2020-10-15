# BOJ 4153 Right-Triangle
import sys
input = sys.stdin.readline
res = ''
while True:
    a,b,c = map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    if 2*max(a,b,c)**2 == a**2+b**2+c**2:
        res += "right\n"
    else:
        res += "wrong\n"
print(res.rstrip())