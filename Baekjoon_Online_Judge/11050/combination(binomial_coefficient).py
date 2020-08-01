def fac(a):
    res = 1
    while a>1:
        res *= a
        a -= 1
    return res


n, k = map(int, input().split())
if k < 0 or k > n:
    print(0)
else:
    print(fac(n)//(fac(k)*fac(n-k)))