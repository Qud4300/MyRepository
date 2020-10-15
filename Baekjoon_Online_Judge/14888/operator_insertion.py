# BOJ 14888 Operator Insertion
import sys
from itertools import permutations

input = sys.stdin.readline
operators = [(lambda x, y: x + y),
             (lambda x, y: x - y),
             (lambda x, y: x * y),
             (lambda x, y: x // y if (x > 0 and y > 0) or (x < 0 and y < 0) else -(abs(x) // abs(y)))]
n = int(input())
num = [*map(int, input().split())]
ops = [*map(int, input().split())]
# op_list = [operators[i] for i in range(4) for _ in range(ops[i])]
op_list = list(set([*permutations([operators[i] for i in range(4) for _ in range(ops[i])])]))
cur_max = -(sys.maxsize + 1)
cur_min = sys.maxsize
for op in op_list:
    temp = num[0]
    for i in range(n - 1):
        temp = op[i](temp, num[i + 1])
    if temp > cur_max:
        cur_max = temp
    if temp < cur_min:
        cur_min = temp
print(cur_max, cur_min, sep='\n')
