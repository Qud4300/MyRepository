# BOJ 9019 DSLR
import sys
input = sys.stdin.readline


def DSLR(n):
    d = 2 * n % 10000
    s = (n - 1) % 10000
    l = n * 10 % 10000 + (n * 10) // 10000
    r = (n % 10) * 1000 + n // 10
    return d, s, l, r


for T in range(int(input())):
    a, b = map(int, input().split())
    dp = [None for _ in range(10000)]
    dp[a] = ['', None]
    res = ''
    queue = [a]
    while queue:
        next_stage = []
        for i in queue:
            D, S, L, R = DSLR(i)
            if dp[D] is None:
                dp[D] = 'D', i
                next_stage.append(D)
            if dp[S] is None:
                dp[S] = 'S', i
                next_stage.append(S)
            if dp[L] is None:
                dp[L] = 'L', i
                next_stage.append(L)
            if dp[R] is None:
                dp[R] = 'R', i
                next_stage.append(R)
            if b in (D, S, L, R):
                cur = b
                while cur is not None:
                    res = dp[cur][0] + res
                    cur = dp[cur][1]
                print(res)
                next_stage = None
                break
        queue = next_stage
