# BOJ 1010 다리 놓기
import math, sys
input = sys.stdin.readline
fac = math.factorial

for T in range(int(input())):
    a, b = map(int, input().split())
    print(fac(b)//fac(b-a)//fac(a))
