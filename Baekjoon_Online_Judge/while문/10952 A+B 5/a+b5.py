#BOJ 10952 A+B 5

import sys
input = sys.stdin.readline

res = ""
a,b = map(int, input().split())

while a!=0 and b!=0:
    res += str(a+b)+"\n"
    a,b = map(int, input().split())

print(res)