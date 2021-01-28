# BOJ 9461 Padovan Sequence
import sys

input = sys.stdin.readline
arr = [0 for _ in range(101)]
arr[1], arr[2], arr[3] = 1, 1, 1
s = 4
res = ""
n = int(input())
for _ in range(n):
    t = int(input())
    if t < s:
        res += str(arr[t])+'\n'
        continue
    else:
        for i in range(s, t+1):
            arr[i] = arr[i - 2] + arr[i - 3]
        res += str(arr[t])+'\n'
print(res.rstrip())
