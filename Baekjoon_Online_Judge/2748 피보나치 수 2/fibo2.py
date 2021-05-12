# BOJ 2748 Fibo 2
n = int(input())
fib = [0]*(n+1)
fib[1] = 1
for i in range(2, n+1):
    fib[i] = fib[i-1]+fib[i-2]
print(fib[n])