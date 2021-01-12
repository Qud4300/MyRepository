# BOJ 1644 Consecutive sum of prime numbers
def primes(a):
    # Sieve of Eratosthenes
    sieve = [True] * (a + 1)
    m = int(a ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i * 2, a + 1, i):
                sieve[j] = False
    return [i for i in range(2, a + 1) if sieve[i]]


n = int(input())
p = primes(n)
if not len(p):
    print(0)
    exit(0)

l, r = 0, 0
cur = p[0]
count = 0
while l < len(p):
    if cur == n:
        count += 1
    if cur < n and r < len(p) - 1:
        r += 1
        cur += p[r]
    else:
        cur -= p[l]
        l += 1

print(count)
