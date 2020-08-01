n = int(input())
arr = sorted([*map(int, input().split())])
k = int(input())
keys = [*map(int, input().split())]

for key in keys:
    left = 0
    right = n-1
    mid = (left+right)//2
    while left <= right:
        mid = (left + right) // 2
        if key < arr[mid]:
            right = mid-1
        elif arr[mid] < key:
            left = mid+1
        else:
            print(1)
            break
    if not left <= right:
        print(0)
