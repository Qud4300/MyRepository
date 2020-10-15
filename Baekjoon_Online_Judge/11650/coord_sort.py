# BOJ 11650 Coord sort
import sys
input = sys.stdin.readline
res = ''
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
for x,y in sorted(arr):
    res += str(x) + ' ' + str(y) + '\n'
print(res.rstrip())