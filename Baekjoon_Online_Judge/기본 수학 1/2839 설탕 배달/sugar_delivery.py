def makeup_3or5(n):
    for a in range(n//5, -1, -1):
        b = (n-a*5)//3
        if a*5 + b*3 == n:
            return a+b
    return -1

n = int(input())
print(makeup_3or5(n))
