# BOJ 9020 Goldbach's conjecture
import sys
input = sys.stdin.readline

arr = [True for _ in range(10001)]
arr[0],arr[1] = False, False
for i in range(2, 101):
    if arr[i]==True:
        for j in range(i*2, 10001, i):
            if arr[j]: arr[j] = False
primes = [i for i in range(2, 10001) if arr[i]]

n = int(input())
res = ""


def find(x):
    global primes
    res = ""
    m = max([i for i in range(len(primes)) if primes[i] <= x // 2])
    for i in range(m, -1, -1):  # move down from [m]
        for j in range(m, len(primes)):  # move up from [m]
            if primes[i] + primes[j] == x:
                res += str(primes[i]) + ' ' + str(primes[j]) + '\n'
                return res


for _ in range(n):
    x = int(input())
    res += find(x)
print(res)
