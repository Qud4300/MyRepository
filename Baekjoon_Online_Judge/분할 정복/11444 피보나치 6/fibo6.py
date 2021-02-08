# BOJ 11444 Fibonacci 6

def matmul(a, b):
    result = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    for i in range(2):
        for j in range(2):
            result[i][j] %= 1000000007
    return result


n = int(input())
matrix = [[1,1],[1,0]]
B = bin(n-1)[2:]

result = matrix
for i in range(len(B)):
    if B[-i - 1] == '1':
        temp = matrix[:]
        while i != 0:
            temp = matmul(temp, temp)
            i -= 1
        result = matmul(result, temp)

print(result[1][0])
