# BOJ 1934 LCM
import sys
input = sys.stdin.readline


# Euclidean algorithm
def GCD(a, b):
    while a != 0 and b != 0:
        if a < b:
            a, b = b, a
        a, b = b, a % b
    return a


for T in range(int(input())):
    a, b = map(int, input().split())
    print(a * b // GCD(a, b))
