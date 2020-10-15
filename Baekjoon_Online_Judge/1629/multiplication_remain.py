# BOJ 1629 Multiplication
a, b, c = map(int, input().split())

def solve(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a%c
    elif b % 2 == 1:
        return solve(a,b-1)*a%c
    else:
        half = solve(a,b//2)
        return (half%c)**2%c

print(solve(a,b))