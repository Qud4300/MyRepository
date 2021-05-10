# BOJ 7869 Two Circles
import math
import sys

input = sys.stdin.readline

a, b, r1, c, d, r2 = map(float, input().split())
dist = math.dist((a, b), (c, d))
M, m = max(r1, r2), min(r1, r2)

if r1+r2 <= dist:
    res = 0.0
elif M-m >= dist:
    res = math.pi * m**2
else:  #using Cosine Law
    t1 = math.acos((r1**2 + dist**2 - r2**2) / (2 * r1 * dist))
    t2 = math.acos((r2**2 + dist**2 - r1**2) / (2 * r2 * dist))

    s1 = (r1 * r1 * 2 * t1) / 2 - r1 * r1 * math.sin(2 * t1) / 2
    s2 = (r2 * r2 * 2 * t2) / 2 - r2 * r2 * math.sin(2 * t2) / 2
    res = s1 + s2
print('%.3f' % res)
