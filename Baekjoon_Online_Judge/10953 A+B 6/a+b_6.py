# BOJ 10953 A+B 6

import sys
input = sys.stdin.readline

for TEST_CASE in range(int(input())):
    a, b = map(int, input().split(','))
    print(a+b)
