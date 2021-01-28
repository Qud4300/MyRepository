# BOJ 14002 LIS 4

n = int(input())
arr = [*map(int, input().split())]

dp = [[0, []] for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j]:
            # apply if there a LIS smaller than arr[i] exists.
            # at last, always the longest one will take the place.
            dp[i][0] = dp[j][0]
            dp[i][1] = [*dp[j][1]]  # array copy
    dp[i][0] += 1
    dp[i][1].append(arr[i])

l, lis = max(dp, key=lambda x: x[0])
print(l)
print(*lis)
