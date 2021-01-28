#BOJ 15552 Fast A+B
import sys
input = sys.stdin.readline
n = int(input())
res = ""
for _ in range(n):
    a, b = map(int, input().split())
    res += str(a+b)+"\n"
print(res)