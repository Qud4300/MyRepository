def returnMax(L):
    M = L[0]
    for i in range(1,len(L)):
        if M > L[i] : continue
        else: M = L[i]
    return M
def returnMin(L):
    M = L[0]
    for i in range(1,len(L)):
        if M < L[i] : continue
        else: M = L[i]
    return M

n = int(input()) #n개의 정수 카드.
A = list(input().split()) #정수 카드들의 입력.
A = list((int(x) for x in A)) #String 타입을 int타입으로 변환하여 저장.

L = list() #최대3값, 최소3값을 저장할 리스트.

L.append(returnMax(A))
A.remove(L[0])
L.append(returnMax(A))
A.remove(L[1])
L.append(returnMax(A))
A.remove(L[2])
count = 0
while(len(A) > 0 and count < 3):
    L.append(returnMin(A))
    A.remove(L[3+count])
    count += 1
#mul2에는 2항곱의 최대값이 저장되고, mul3에는 3항곱의 최대값이 저장된다.
mul2 = list( L[i]*L[j] for i in range(len(L)) for j in range(i+1, len(L)) )
mul3 = list( L[i]*L[j]*L[k] for i in range(len(L)) for j in range(i+1, len(L)) for k in range(j+1, len(L)) ) 
if returnMax(mul2) > returnMax(mul3) : M = returnMax(mul2)
else : M = returnMax(mul3)
print(M)
