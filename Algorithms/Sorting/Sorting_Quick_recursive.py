def QuickSort(A):
    if len(A) <= 1: return A
    pivot = A[0]
    S,M,L = [],[],[]
    for x in A:
        if x < pivot: S.append(x)
        elif x > pivot : L.append(x)
        else: M.append(x)
    return QuickSort(S)+M+QuickSort(L)

A = list(input().split())
Q = QuickSort(A)
print( Q[1] )
