import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n ,m = map(int,input().split())
    arr = list(map(int,input().split()))
    check = [0 for _ in range(n)]
    check[m] = 1
    myPri = arr[m]
    count = 0
    while True:
        if arr[0] == max(arr):
            count+=1
            if check[0] == 1:
                break
            else:
                arr.pop(0)
                check.pop(0)
        else:
            arr.append(arr.pop(0))
            check.append(check.pop(0))
    print(count)