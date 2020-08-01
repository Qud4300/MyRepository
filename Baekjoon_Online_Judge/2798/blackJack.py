n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())), reverse=True)
flag = False  # a flag to escape out of for-loop
res = 0
for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            cur = lst[i]+lst[j]+lst[k]
            if m >= cur > res: res = cur
print(res)