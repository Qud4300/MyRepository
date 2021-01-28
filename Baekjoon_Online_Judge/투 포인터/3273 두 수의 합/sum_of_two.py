# BOJ 3273 Sum of Two Numbers

n = int(input())
arr = sorted([*map(int, input().split())])
x = int(input())

res = 0

i = 0
j = n - 1

while i < j:
    t = arr[i] + arr[j]
    if t == x:
        res += 1
    if t < x:
        i += 1
        continue
    j -= 1

print(res)
