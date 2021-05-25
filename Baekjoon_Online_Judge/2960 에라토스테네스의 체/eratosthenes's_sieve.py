# BOJ 2960 Eratosthenes's Sieve

n, k = map(int, input().split())

sieve = [True]*(n+1)
seq = 1

for i in range(2, n+1):
    if sieve[i] is True:
        if seq == k:
            print(i)
            exit()
        seq += 1
        for j in range(i+i, n+1, i):
            if sieve[j] is True:
                if seq == k:
                    print(j)
                    exit()
                sieve[j] = False
                seq += 1
