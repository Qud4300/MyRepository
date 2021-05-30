# BOJ 2530 인공지능 시계

a, b, c = map(int, input().split())
d = int(input())

minute = 60
hour = 60 * minute
day = 24 * hour
res = (a*hour + b*minute + c + d) % day

res_hour = res // hour
res %= hour
res_min = res // minute
res %= minute
res_sec = res

print(res_hour, res_min, res_sec)
