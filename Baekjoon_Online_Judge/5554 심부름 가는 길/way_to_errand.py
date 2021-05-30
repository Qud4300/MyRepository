# BOJ 5554 Way to run an errand

total = 0
for _ in range(4):
    total += int(input())

print(total//60, total%60, sep='\n')
