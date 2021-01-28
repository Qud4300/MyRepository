# BOJ 2166 Polygon Area(신발끈공식)
import sys
input = sys.stdin.readline

n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
arr.append(arr[0])
res = 0
for i in range(n):
    res += arr[i][0]*arr[i+1][1] - arr[i][1]*arr[i+1][0]
print(abs(round(res/2,1)))
