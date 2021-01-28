A, B, V = map(int, input().split())
x = (V - A)/(A - B)
x = int(x) if x == int(x) else int(x)+1
print(x + 1)
