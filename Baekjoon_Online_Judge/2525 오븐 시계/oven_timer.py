# BOJ 2525 Oven Timer

a, b = map(int, input().split())
c = int(input())


hour = 60
day = 24 * hour
res = (a*hour + b + d) % day

res_hour = res // hour
res %= hour
res_min = res

print(res_hour, res_min)
