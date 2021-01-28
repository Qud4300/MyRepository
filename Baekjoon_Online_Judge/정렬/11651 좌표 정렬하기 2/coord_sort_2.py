# BOJ 11651 coord sort 2
import sys
input = sys.stdin.readline
res = ''
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
for a,b in sorted(arr,key = lambda x: (x[1],x[0])):
    res += str(a) + ' ' + str(b) + '\n'
print(res.rstrip())