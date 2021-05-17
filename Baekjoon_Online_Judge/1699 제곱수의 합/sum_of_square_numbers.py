# BOJ 1699 제곱수의 합

def makeNumber(a, arr):
    count = a
    for i in reversed(arr):
        count = min(dp[i] + dp[a-i], count)
        if count == 2:
            break
    return count


n = int(input())
dp = [None for i in range(n + 1)]
dp[1] = 1
squares = [1]

for i in range(2, n + 1):
    if i == int(i ** 0.5) ** 2:
        dp[i] = 1
        squares.append(i)
    else:
        dp[i] = makeNumber(i, squares)

print(dp[-1])
