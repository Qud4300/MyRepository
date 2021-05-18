# BOJ 2576 홀수

cur_min = 101
total = 0
for _ in range(7):
    cur = int(input())
    if cur % 2 == 1:
        total += cur
        cur_min = min(cur, cur_min)

if total != 0: 
    print(total)
print(cur_min if cur_min != 101 else -1)
