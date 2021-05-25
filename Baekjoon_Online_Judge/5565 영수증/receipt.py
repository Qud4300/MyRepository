# BOJ 5565 Receipt

total = int(input())
partSum = 0
for _ in range(9):
    partSum += int(input())

print(total - partSum)
