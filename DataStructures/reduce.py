from functools import reduce

A = [int(x) for x in input().split()]
maximum = reduce(lambda x, y: x if x> y else y, A)
minimum = reduce(lambda x, y: x if x< y else y, A)
print(maximum, minimum)
