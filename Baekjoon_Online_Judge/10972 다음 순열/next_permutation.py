# BOJ 10972 Next Permutation

n = int(input())
arr = [*map(int, input().split())]

count = 0
res = [-1]

if len(arr) > 1:
    u, v = None, None
    for i in range(n-2, -1, -1):
        if arr[i] < arr[i+1]:
            u = i
            break
    if u is not None:
        for i in range(n-1, -1, -1):
            if arr[u] < arr[i]:
                v = i
                break
        arr[u], arr[v] = arr[v], arr[u]
        res = arr[:u+1] + sorted(arr[u+1:])
print(*res)
