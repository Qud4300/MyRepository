# BOJ 4949 Balanced World
import sys

input = sys.stdin.readline
res = ""
while True:
    i = input().rstrip()
    if i == ".":
        break
    stack = []
    flag = True
    for c in i:
        if c == '(' or c == '[':
            stack.append(c)
        if c == ')' or c == ']':
            if len(stack) == 0 or \
                    (c == ')' and stack[-1] == '[') or \
                    (c == ']' and stack[-1] == '('):
                flag = False
                break
            else:
                stack.pop()
    if len(stack) == 0 and flag:
        res += 'yes\n'
    else:
        res += 'no\n'
print(res.rstrip())
