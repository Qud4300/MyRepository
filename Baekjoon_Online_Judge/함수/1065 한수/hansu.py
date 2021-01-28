n = int(input())
count = 0
cur = 0
for i in range(1,n+1):
    a = str(i)
    flag = True
    ex = 0
    for j in range(1,len(a)):
        cur = int(a[j]) - int(a[j-1])
        if j == 1:
            ex = cur
            continue
        if cur != ex:
            flag = False
            break
    if flag:
        count += 1
print(count)