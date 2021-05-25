# BOJ 2480 주사위 세개

arr = [*map(int, input().split())]
count = [0 for _ in range(7)]

for i in arr:
    count[i] += 1
m = max(count)
idx = 0
for i in range(len(count)):
    if count[i] == m:
        idx = i
        break

if m == 3:
    res = 10000 + idx * 1000
elif m == 2:
    res = 1000 + idx * 100
else:
    res = max(arr) * 100

print(res)
