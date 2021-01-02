# BOJ 9252 LCS 2

a = input()
b = input()

dp = [[[0,''] for j in range(len(b)+1)] for i in range(len(a)+1)]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            dp[i+1][j+1][0] = dp[i][j][0] + 1
            dp[i+1][j+1][1] = dp[i][j][1] + a[i]
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], key=lambda x: x[0])

l, lcs = dp[len(a)][len(b)]
print(l)
if l:
    print(lcs)
