L = list(map(int, input()))
for i in range(len(L)):
    max = i
    for j in range(i+1,len(L)):
        if L[max] < L[j]:
            max = j
    L[i], L[max] = L[max], L[i]
            
for i in range(len(L)):
        print(L[i], end='')
