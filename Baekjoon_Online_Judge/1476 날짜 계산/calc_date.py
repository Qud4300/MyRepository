# BOJ 1476 날짜 계산
E, S, M = map(int, input().split())
cur = 1
while cur < 7981:
    if (cur - E) % 15 == (cur - S) % 28 == (cur - M) % 19 == 0:
        print(cur)
        break
    cur += 1
