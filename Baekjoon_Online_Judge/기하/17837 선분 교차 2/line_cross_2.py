# BOJ 17387 Line Cross 2

def ccw(A, B, C):
    res = (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])
    if res < 0:
        return -1
    elif res == 0:
        return 0
    else:
        return 1


a, b, c, d = map(int, input().split())
u, v = [a, b], [c, d]
e, f, g, h = map(int, input().split())
w, x = [e, f], [g, h]

if u==w or u==x or v==w or v==x:
    print(1)
else:
    abc = ccw(u, v, w)
    abd = ccw(u, v, x)
    cda = ccw(w, x, u)
    cdb = ccw(w, x, v)
    if abc * abd <= 0 and cda * cdb <= 0:
        if (abc == abd == 0 and ((a < e and a < g and c < e and c < g) or (e < a and g < a and e < c and g < c))) \
                or (abc == abd == 0 and ((b < f and b < h and d < f and d < h) or (f < b and h < b and f < d and h < d))):
            print(0)
        else:
            print(1)
    else:
        print(0)
