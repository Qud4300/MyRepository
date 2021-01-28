import sys
arr = [*map(lambda x: int(x)%42, sys.stdin.read().rstrip().split('\n'))]
print(len(set(arr)))
