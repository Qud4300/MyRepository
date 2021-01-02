# BOJ 13913 Hide 'n Seek 4
n, k = map(int, input().split())

dp = [[-1, None] for _ in range(100001)]
dp[n] = [0, None]
queue = [n]


def route(a, b):
    res = ''
    v = b
    while dp[v][1] is not None:
        res = str(v) + ' ' + res
        v = dp[v][1]
    res = str(a)+' '+res
    return res.rstrip()


if n == k:
    print(0, n, sep='\n')
    exit(0)

while queue:
    next_stage = []
    for i in queue:
        cur = dp[i][0]
        if k == i + 1 or k == i - 1 or k == i * 2:
            dp[k] = cur + 1, i
            print(cur + 1)
            print(route(n, k))
            exit(0)
        if i < 99999 and dp[i + 1][0] == -1:
            dp[i + 1] = cur + 1, i
            next_stage.append(i + 1)
        if i > 0 and dp[i - 1][0] == -1:
            dp[i - 1] = cur + 1, i
            next_stage.append(i - 1)
        if i * 2 < 100001 and dp[i * 2][0] == -1:
            dp[i * 2] = cur + 1, i
            next_stage.append(i * 2)
    queue = next_stage
