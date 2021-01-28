#BOJ 11022 A+B 8
import sys
input = sys.stdin.readline
n = int(input())
res = ""
for i in range(n):
    a, b = map(int, input().split())
    res += "Case #"+str(i+1)+": "+str(a)+" + "+str(b)+" = "+str(a+b)+"\n"
print(res)