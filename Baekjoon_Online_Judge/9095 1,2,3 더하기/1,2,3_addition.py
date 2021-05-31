# BOJ 9095 1,2,3 더하기
import sys
from math import factorial

input = sys.stdin.readline
fac = factorial

two = lambda x: x // 2
three = lambda x: x // 3

for TEST_CASE in range(int(input())):
    n = int(input())
    total = 0
    for i in range(three(n)+1):
        for j in range(two(n-3*i)+1):
            total += fac(n-3*i-2*j+i+j)//(fac(i)*fac(j)*fac(n-3*i-2*j))
    print(total)
