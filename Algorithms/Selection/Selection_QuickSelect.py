def QuickSelect(L,k):
    p = L[0]
    A,B,M = list(),list(),list()
    M.append(p)
    for i in range(1, len(L)):
        if L[i] < p : A.append(L[i])
        elif L[i] > p : B.append(L[i])
        else : M.append(L[i])
    if len(A) >= k:
        return QuickSelect(A,k)
    elif len(A) + len(M) < k :
        return QuickSelect(B, k-len(A)-len(M))
    else : return p
    
n, k = map(int, input().split())
L = list(map(int, input().split()))
print(QuickSelect(L, k))
