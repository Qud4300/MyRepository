m, n = map(int, input().split())
sieve = [1 for _ in range(n+1)] # 1 for prime numbers, 0 for non-prime numbers.
res = ""
for i in range(2, n+1):
    if sieve[i]:# i is prime.
        x = 2 * i
        while x <= n:
            sieve[x] = 0
            x += i
        if i >= m:
            res += str(i)+'\n'
print(res)