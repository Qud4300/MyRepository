# BOJ 13305 Gas Station

n = int(input())
road = [*map(int, input().split())]
price = [*map(int, input().split())]
cur_min = price[0]
total = 0

for i in range(n-1):
    cur_min = min(cur_min, price[i])
    total += cur_min*road[i]

print(total)
