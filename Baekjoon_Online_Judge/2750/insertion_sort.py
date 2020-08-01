n = int(input())
L = []
for i in range(n):
    L.append(int(input()))
#insertion sort
for i in range(n):
    p=i
    for j in range(i+1,n):
        if L[j] < L[p]:
            p = j
    L[i],L[p] = L[p],L[i]
for i in range(n):
    print(L[i])