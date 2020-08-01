def quadTree(m, k):
    white = 0
    blue = 0
    count = 0
    while white & blue == 0 and count < (k**2):
        if m[count // k][count % k] == 1:
            blue += 1
        else:
            white += 1
        count += 1
    if white & blue == 0:
        return int(bool(white)), int(bool(blue))
    else:
        w1, b1 = quadTree([i[0:k // 2] for i in m[0:k // 2]], k // 2)
        w2, b2 = quadTree([i[k // 2:k] for i in m[0:k // 2]], k // 2)
        w3, b3 = quadTree([i[0:k // 2] for i in m[k // 2:k]], k // 2)
        w4, b4 = quadTree([i[k // 2:k] for i in m[k // 2:k]], k // 2)
        return w1 + w2 + w3 + w4, b1 + b2 + b3 + b4


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
white, blue = quadTree(arr, n)
print(white, blue, sep="\n")