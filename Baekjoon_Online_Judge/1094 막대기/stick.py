# BOJ 1094 막대기

a = int(input())
total = 64
cur = 64
count = 1

while total > a and cur > 0:
    cur = cur // 2
    count += 1
    if total - cur >= a:
        total -= cur
        count -= 1

print(count)
