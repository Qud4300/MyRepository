while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0: break
    print("multiple" if a % b == 0 else "factor" if b%a==0 else "neither")