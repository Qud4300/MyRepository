# BOJ 17386 Line Cross 1


def ccw(A, B, C):
    if (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0]) < 0:
        return 1
    else:
        return -1


a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())

abc = ccw([a, b], [c, d], [e, f])
abd = ccw([a, b], [c, d], [g, h])
cda = ccw([e, f], [g, h], [a, b])
cdb = ccw([e, f], [g, h], [c, d])

if abc * abd <= 0 and cda * cdb <= 0:
    print(1)
else:
    print(0)
