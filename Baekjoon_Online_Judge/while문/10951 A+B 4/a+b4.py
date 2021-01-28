#BOJ 10951 A+B 4

import sys
input = sys.stdin.readline

res = ""

while True:
    try:
        a,b = map(int, input().split())
        res += str(a+b)+"\n"
    except:
        break

print(res)