# BOJ 2581 Prime Number
m = int(input())
n = int(input())

arr = [i for i in range(0,n+1)]
arr[0],arr[1] = 0, 0
for i in range(2,n+1):
    if arr[i] != 0:
        for j in range(2, n//i+1):
            arr[i*j]=0
res = arr[m:n+1]
acc = sum(res)
print(acc if acc else -1)
if acc:
    res = set(arr[m:n+1])
    res.remove(0)
    print(min(res))