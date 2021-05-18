# BOJ 2525 Oven Timer

a, b = map(int, input().split())
c = int(input())

hour = 60
day = 24 * hour

res_min = (b + (c % hour)) % hour
res_hour = (a * hour + b + c) % day // hour
print(res_hour, res_min)
