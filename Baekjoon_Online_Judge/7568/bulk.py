n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
for i in arr:  # 0
    rank = 1  # 1
    for n in arr:
        if (i[0] != n[0]) & (i[1] != n[1]):
            if (i[0] < n[0]) & (i[1] < n[1]):
                rank += 1
    print(rank)

