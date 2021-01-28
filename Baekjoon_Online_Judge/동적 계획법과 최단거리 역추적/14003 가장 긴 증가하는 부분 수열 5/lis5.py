# BOJ 14003 LIS 5

n = int(input())
arr = [*map(int, input().split())]

dp = []

for i in range(n):
    a = arr[i]
    l, r = 0, len(dp) - 1
    while l <= r:
        mid = (l + r) // 2
        if dp[mid][0] == arr[i]:
            l = mid
            break
        elif dp[mid][0] < arr[i]:
            l = mid + 1
        else:
            r = mid - 1
    if len(dp) <= l:
        dp.append([arr[i], dp[-1][1] + [arr[i]] if len(dp) else [arr[i]]])
    else:
        dp[l][0] = arr[i]
        dp[l][1] = dp[l-1][1]+[arr[i]] if l>0 else [arr[i]]

print(len(dp))
print(*dp[-1][1])
