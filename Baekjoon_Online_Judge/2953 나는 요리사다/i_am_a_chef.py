# BOJ 3953 나는 요리사다

m = 0
who = 0
cur = 0
for i in range(1, 6):
    cur = sum([*map(int, input().split())])
    if m < cur:
        m = cur
        who = i

print(who, m)
