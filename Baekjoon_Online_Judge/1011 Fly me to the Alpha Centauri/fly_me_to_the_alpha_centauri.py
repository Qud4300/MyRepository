# BOJ 1011 Fly me to the Alpha Centauri
import sys
input = sys.stdin.readline

for TEST_CASE in range(int(input())):
    x, y = map(int, input().split())
    dist = y-x
    move = 0
    cur = 1
    total = 0
    while total < dist:
        move += 1
        total += cur
        if move % 2 == 0:
            cur += 1
    print(move)
