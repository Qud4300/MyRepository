L = list(input())
for i in range(len(L)):
    if i>0 and i%10 == 0: print("")
    print(L[i], end='')
