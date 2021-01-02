# BOJ 12015 LIS 2

n = int(input())
arr = [*map(int, input().split())]

bs = []

for i in range(n):
    a = arr[i]
    l, r = 0, len(bs)-1
    while l<=r:
        mid = (l+r)//2
        if bs[mid] < arr[i]:
            l = mid+1
        else:
            r = mid-1
    if len(bs)<=l:
        bs.append(arr[i])
    else:
        bs[l] = arr[i]

print(len(bs))
