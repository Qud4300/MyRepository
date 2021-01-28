#BOJ 2562 Max index
import sys
arr = [*map(int, sys.stdin.read().rstrip().split('\n'))]
m = max(arr)
print(m)
print(arr.index(m)+1)