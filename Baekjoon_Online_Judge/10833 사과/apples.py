# BOJ 10833 사과
import sys
input = sys.stdin.readline

res = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    res += max(b%a, 0)

print(res)
