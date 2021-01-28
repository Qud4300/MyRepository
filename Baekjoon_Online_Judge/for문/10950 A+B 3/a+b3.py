#BOJ 10950 A+B 3
import sys
input = sys.stdin.readline
n = int(input())
res = ""
for _ in range(n):
    a, b = map(int, input().split())
    res += str(a+b)+"\n"
print(res)