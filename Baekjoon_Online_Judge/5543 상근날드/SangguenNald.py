# BOJ 5543 상근날드

a, b = 2000, 2000
for burger in range(3):
    a = min(a, int(input()))
for beverage in range(2):
    b = min(b, int(input()))

print(a+b-50)
