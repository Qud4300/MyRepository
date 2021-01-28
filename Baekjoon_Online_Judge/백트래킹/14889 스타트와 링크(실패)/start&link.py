# BOJ 14889 Start&Link
import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
for i in range(n - 1):
    for j in range(i + 1, n):  # this creates the upper-side triangle array
        arr[i][j] = arr[i][j] + arr[j][i]
        arr[j][i] = 0
cur_min = sys.maxsize
total = set(range(n))
cases = list(set(combinations(total, n // 2)))
for i in range(len(cases) // 2):
    start = cases[i]
    link = total - set(start)
    sum_start, sum_link = 0, 0
    for s_com in combinations(start, 2):
        sum_start += arr[s_com[0]][s_com[1]]
    for l_com in combinations(link, 2):
        sum_link += arr[l_com[0]][l_com[1]]
    cur_min = min(cur_min, abs(sum_start - sum_link))
print(cur_min)
