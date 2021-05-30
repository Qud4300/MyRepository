# BOJ 1735 분수 합

def GCD(a, b):
    while a % b:
        a, b = b, a % b
    return b


def fraction_sum(n1, d1, n2, d2):
    g1 = GCD(d1, d2)
    lcm = d1*d2//g1
    res = n1*d2//g1 + n2*d1//g1
    g2 = GCD(res, lcm)
    return res//g2, lcm//g2


A, B = map(int, input().split())
C, D = map(int, input().split())

print(*fraction_sum(A, B, C, D))
