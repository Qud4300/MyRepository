import sys

n = int(input())
l = [int(sys.stdin.readline().rstrip()) for i in range(n)]
for i in sorted(l):
    print(i)
