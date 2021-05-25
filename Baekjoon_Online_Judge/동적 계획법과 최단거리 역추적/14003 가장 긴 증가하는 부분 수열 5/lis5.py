# BOJ 14003 LIS 5

n = int(input())
arr = [*map(int, input().split())]

lis = []
track = [-1 for _ in range(n)]

for i in range(n):
    a = arr[i]
    l, r = 0, len(lis) - 1
    while l <= r:
        mid = (l + r) // 2
        if lis[mid][0] == a:
            l = mid
            break
        elif lis[mid][0] < a:
            l = mid + 1
        else:
            r = mid - 1
    if len(lis) <= l:
        track[i] = lis[-1][1] if len(lis) else -1
        lis.append([a, i])
    else:
        if lis[l][0] == a:
            continue
        lis[l] = [a, i]
        track[i] = lis[l-1][1] if l > 0 else -1


print(len(lis))
cur = lis[-1][1]
res = []
while cur != -1:
    res.append(arr[cur])
    cur = track[cur]
print(*reversed(res))
