import sys
input = sys.stdin.readline

def gen(a):
    return a + sum([int(_) for _ in str(a)])
def gen_check(n):
    for i in range(max(n-54, 1),n):
        if gen(i) == n:
            return i
    return 0

n = int(input())
print(gen_check(n))
