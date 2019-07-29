def binary_search(A, k):
    if len(A)<1 : return None
    m = int((len(A)-1)//2)
    if A[m] == k: return m
    elif A[m] > k:
        return binary_search(A[:m],k)
    else :
        res = binary_search(A[m+1:], k)
        return res+m+1 if res!=None else None

def binary_search_2(A,i,j,k):
    if i>j: return None
    m = (i+j)//2
    if k == A[m]: return m
    elif x<A[m] : return binary_search_2(A,i,m-1,k)
    else : return binary_search_2(A,m+1,j,k)
    
A = [2*i for i in range(11)]
print(A)
while True:
    x = int(input("x = "))
    if x == -1 : break
    res = binary_search(A, x)
    #res = binary_search(A, 0, len(A), x)
    if res == None: print("Not Found!")
    else : print(x," is found at index ",res)
print("end")
