# BOJ 1874 Stack Sequence
import sys
input = sys.stdin.readline

n = int(input())
seq = [int(input()) for _ in range(n)]

stack = []
op = []
count = 1
flag = True

for i in seq:
    while count <= i:
        stack.append(count)
        op.append('+')
        count += 1
    if stack[-1] == i:
        stack.pop()
        op.append('-')
    else:
        flag = False
if not flag:
    print('NO')
else:
    print(*op, sep='\n')
