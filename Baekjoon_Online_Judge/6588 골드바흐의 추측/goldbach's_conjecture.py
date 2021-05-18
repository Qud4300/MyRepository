# BOJ Goldbach's Conjecture
import sys
input = sys.stdin.readline

sieve = [True for _ in range(1000000)]
primes = []
count = 0
sieve[0], sieve[1] = False, False

for i in range(2, 1000000):
    if sieve[i] is True:
        primes.append(i)
        sieve[i] = count
        count += 1
        for j in range(i+i, 1000000, i):
            sieve[j] = False
    else:
        sieve[i] = sieve[i - 1]

while True:
    n = int(input())
    flag = False
    if n == 0:
        break
    else:
        cur_max = sieve[i-1]
        for i in primes:
            if i > n//2:
                break
            if i + primes[sieve[n-i]] == n:
                flag = True
                print('%d = %d + %d' % (n, i, primes[sieve[n-i]]))
                break
        if not flag:
            print("Goldbach's conjecture is wrong.")
            continue

