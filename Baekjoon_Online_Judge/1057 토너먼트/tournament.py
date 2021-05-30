# BOJ 1057 Tournament
import math


def nextEntry(k):
    return (k + 1) // 2


n, a, b = map(int, input().split())
flag = False
for i in range(1, math.ceil(math.log2(n)) + 1):
    if max(a, b) - min(a, b) == 1 and max(a, b) % 2 == 0:
        flag = True
        print(i)
        break
    a = nextEntry(a)
    b = nextEntry(b)
if not flag:
    print(-1)
