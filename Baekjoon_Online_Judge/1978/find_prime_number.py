import math as M
def isPrime(a):
    if a == 1 : return False
    root = M.floor(M.sqrt(a))
    for i in range(2, root+1):
        if a%i == 0 and a//i != 1 :
            return False
    return True

n = int(input())
L = list(map(int, input().split()))
P = []
for i in range(n):
    if isPrime(L[i]):
        P.append(L[i])
print(len(P))
