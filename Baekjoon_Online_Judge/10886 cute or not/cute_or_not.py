# BOJ 10886 cute or not

n = int(input())
total = 0

for _ in range(n):
    total += int(input())

if total > n-total:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
