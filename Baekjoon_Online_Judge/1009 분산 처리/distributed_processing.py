# BOJ 1009 Distributed Processing
import sys
input = sys.stdin.readline

for TEST_CASE in range(int(input())):
    a, b = map(int, input().split())
    remain = []
    arr = [False]*10
    cur = 1
    count = 0
    for i in range(b):
        cur = (cur * a) % 10
        if arr[cur]:
            break
        else:
            count += 1
            arr[cur] = True
            remain.append(cur)

    res = remain[(b-1) % count]
    print(res if res != 0 else 10)
