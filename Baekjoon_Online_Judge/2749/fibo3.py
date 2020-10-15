# BOJ 2749 Fibo 3
def matmul(a, b):
    res = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += (a[i][k] * b[k][j])
                res[i][j] %= 1000000
    return res

def fibo(n):
    ZERO = [[1, 0], [0, 1]]
    BASE = [[1, 1], [1, 0]]

    matrix = ZERO.copy()
    k = 0
    tmp = BASE.copy()
    while 2 ** k <= n:
        if n & (1 << k) != 0:
            matrix = matmul(matrix, tmp)
        k += 1
        tmp = matmul(tmp, tmp)
    return matrix[1][0]


print(fibo(int(input())))