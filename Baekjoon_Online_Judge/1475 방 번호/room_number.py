n = input()
L = [0]*10
for x in n:
    if x == '9':
        L[6] += 1
    else: L[int(x)] += 1
L[6] = L[6]//2+L[6]%2
print(max(L))