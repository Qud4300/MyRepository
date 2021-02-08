# BOJ 9184 Exciting function execution
import sys
input = sys.stdin.readline


def w(a, b, c):
    if mem[a + 50][b + 50][c + 50] is None:
        if a <= 0 or b <= 0 or c <= 0:
            mem[a + 50][b + 50][c + 50] = 1
        elif a > 20 or b > 20 or c > 20:
            mem[a + 50][b + 50][c + 50] = w(20, 20, 20)
        elif a < b < c:
            mem[a + 50][b + 50][c + 50] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        else:
            mem[a + 50][b + 50][c + 50] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1,
                                                                                                       c - 1)

    return mem[a + 50][b + 50][c + 50]


mem = [[[None] * 101 for _ in range(101)] for __ in range(101)]
while True:
    A, B, C = map(int, input().split())
    if A == B == C == -1:
        break
    print("w("+str(A)+", "+str(B)+", "+str(C)+") = "+str(w(A, B, C)))
