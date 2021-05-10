# BOJ 2581 소수

def sieve(a, b):
    arr = [i for i in range(b+1)]
    arr[0], arr[1] = False, False
    for i in range(2, int(b**0.5+1)):
        if arr[i] != 0:
            for j in range(i+i, b+1, i):
                arr[j] = 0
    return arr[a:b+1]


m = int(input())
n = int(input())
res = set(sieve(m, n))
if 0 in res:
    res.remove(0)
if len(res)>0:
    print(sum(res))
    print(min(res))
else:
    print(-1)
