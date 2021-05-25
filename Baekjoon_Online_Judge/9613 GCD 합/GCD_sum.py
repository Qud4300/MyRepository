# BOJ 9613 GCD 합
import sys
input = sys.stdin.readline


def GCD(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


for TEST_CASE in range(int(input())):
    arr = [*map(int, input().split())]
    total = 0
    for i in range(1, len(arr)):
        for j in range(i+1, len(arr)):
            total += GCD(arr[i], arr[j])
    print(total)
