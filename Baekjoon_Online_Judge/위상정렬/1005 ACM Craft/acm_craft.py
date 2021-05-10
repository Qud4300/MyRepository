# BOJ 1005 ACM Craft
import sys, copy
input = sys.stdin.readline


def make_sequence(node, size):
    last_level = []
    visited = [False] * (size + 1)
    visited[node] = True
    cur_level = [node]
    while cur_level:
        next_level = []
        for u in cur_level:
            if u in req:
                for v in req[u]:
                    if not visited[v]:
                        if v not in req:
                            last_level.append(v)
                        else:
                            next_level.append(v)
                        visited[v] = True
        cur_level = next_level

    edges = copy.deepcopy(req)
    sequence = last_level.copy()
    while last_level:
        next_level = []
        for i in last_level:
            if i in suf:
                for j in suf[i]:
                    edges[j].remove(i)
                    if len(edges[j]) == 0:
                        sequence.append(j)
                        next_level.append(j)
        last_level = next_level
    return sequence


def time_required(seq: list, target):
    dp = [time[i] for i in range(len(time))]
    for i in seq:
        dp[i] = time[i]
        if i in req:
            dp[i] += max([dp[j] for j in req[i]])
        if i == target:
            break
    return dp[target]


for TEST_CASE in range(int(input())):
    n, k = map(int, input().split())
    time = [0]+[*map(int, input().split())]
    suf = dict()
    req = dict()
    for _ in range(k):
        x, y = map(int, input().split())
        if x not in suf:
            suf[x] = set()
        if y not in req:
            req[y] = set()
        suf[x].add(y)
        req[y].add(x)
    w = int(input())
    print(time_required(make_sequence(w, n), w))
