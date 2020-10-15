# BOJ 1300 K'th number
n = int(input())
k = int(input())

l, r = 1, k
res = 0
while l <= r:
    mid = (l+r)//2
    temp = 0
    for i in range(1,n+1):
        temp += min(mid//i, n)
    if temp >= k:
        res = mid
        r = mid-1
    else:
        l = mid+1
print(res)