#BOJ 2908 Sangsu
a, b = map(lambda x: int(x[::-1]), input().split())
print(max(a,b))