L = list(map(int, input().split()))
flag = 0
for i in range(1,len(L)):
    if i == 1:
        flag = L[i]-L[i-1]
        continue
    elif flag == 1 and L[i]-L[i-1]==1:
        continue
    elif flag == -1 and L[i]-L[i-1]==-1:
        continue
    else :
        flag = 0
if flag == 1:
    print("ascending")
if flag == -1:
    print("descending")
if flag == 0:
    print("mixed")