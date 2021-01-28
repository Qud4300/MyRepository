import sys
from collections import deque
input = sys.stdin.readline

n ,m = map(int, input().split())
Q = deque()
res = []
for i in range(1,n+1):
    Q.append(i)
for i in range(n):
    for j in range(m-1):
        Q.append(Q.popleft())
    res.append(Q.popleft())
    L = ""
L+=('<')
for i in range(n):
    L+=(str(res[i]))
    if i < n-1:
        L+=(", ")
L+=('>')
print(L)
