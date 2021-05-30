# BOJ 1748 수 이어 쓰기 1

n = int(input())
l = len(str(n))
res = 0
for i in range(1, l):
    res += i*(10**i - 10**(i-1))
res += l*(n - 10**(l-1) + 1)
print(res)