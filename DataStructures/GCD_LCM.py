def find_gcd_lcm(a, b):
    A = a; B = b;
    while A*B != 0:
        if A>B :
            A %= B
        else :
            B %= A
    GCD = int(A+B)
    LCM = int(a*b/(A+B))
    return GCD, LCM

a ,b = input().split()
a = int(a); b = int(b)
print(find_gcd_lcm(a, b))
