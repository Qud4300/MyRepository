def quadTree(arr, k):
    if k == 1:
        return arr[0][0]
    count = 1
    flag = True
    while count < k**2:
        if arr[count//k][count%k]!=arr[(count-1)//k][(count-1)%k]:
            flag = False
            break
        count += 1
    if flag:
        return arr[0][0]
    else:
        q1 = quadTree([i[0:k // 2] for i in arr[0:k // 2]], k // 2)
        q2 = quadTree([i[k // 2:k] for i in arr[0:k // 2]], k // 2)
        q3 = quadTree([i[0:k // 2] for i in arr[k // 2:k]], k // 2)
        q4 = quadTree([i[k // 2:k] for i in arr[k // 2:k]], k // 2)
        return "(" + q1 + q2 + q3 + q4 + ")"


n = int(input())
arr = [[*input()] for _ in range(n)]
print(quadTree(arr,n))
