# BOJ 3009 fourth point
import sys
input = sys.stdin.readline
x = []
y = []
res = ''
for _ in range(3):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)
res += str(min(x) if x.count(min(x))==1 else max(x)) +' '+ str(min(y) if y.count(min(y))==1 else max(y))
print(res)
