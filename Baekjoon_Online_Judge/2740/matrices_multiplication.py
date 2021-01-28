n, m = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(n)]
m, k = map(int, input().split())
B = [[*map(int, input().split())] for _ in range(m)]
C = [[sum([A[i][e]*B[e][j] for e in range(m)]) for j in range(k)] for i in range(n)]
for i in range(len(C)):
    print(*C[i])