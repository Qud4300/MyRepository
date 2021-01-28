# BOJ 18258 Queue 2
import sys
input = sys.stdin.readline

q = []
front = 0
res = ""

for _ in range(int(input())):
    com = input().rstrip().split()
    if com[0]=='push':
        q.append(com[1])
    elif com[0]=='pop':
        if len(q)>front:
            res+=(str(q[front])+'\n')
            front += 1
        else: res+=(str(-1)+'\n')
    elif com[0]=='size':
        res+=(str(len(q)-front)+'\n')
    elif com[0]=='empty':
        res+=(str(1 if len(q)==front else 0)+'\n')
    elif com[0]=='front':
        res+=(str(q[front] if len(q)>front else -1)+'\n')
    elif com[0]=='back':
        res+=(str(q[-1] if len(q)>front else -1)+'\n')

print(res.rstrip())