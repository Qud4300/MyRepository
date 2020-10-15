# BOJ 10828 Stack
import sys
input = sys.stdin.readline

stack = []
res = ""
n = int(input())
for _ in range(n):
    com = input().split()
    if com[0]=='push':
        stack.append(int(com[1]))
    elif com[0]=='pop':
        res += str(-1 if len(stack)<1 else stack.pop())+'\n'
    elif com[0]=='size':
        res += str(len(stack))+'\n'
    elif com[0]=='empty':
        res += str(int(len(stack)==0))+'\n'
    elif com[0]=='top':
        res += str(-1 if len(stack)<1 else stack[-1]) + '\n'
print(res.rstrip())