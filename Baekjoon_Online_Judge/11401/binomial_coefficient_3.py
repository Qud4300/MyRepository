# BOJ 11401 Binomial Coefficient 3 - Fermat's little theorem
def power(A, B):
    if B % 2 > 0:
        return power(A, B - 1) * A
    elif B == 0:
        return 1
    else:
        res = power(A, B // 2)
        return res ** 2 % p


n, k = map(int, input().split())
p = 1000000007

fac = [1 for _ in range(n + 1)]
for i in range(2, n+1):
    fac[i] = fac[i-1] * i % p
N, NK = fac[n], fac[n-k]*fac[k]%p
NK = power(NK, p - 2) % p
result = N * NK % p
print(result)
