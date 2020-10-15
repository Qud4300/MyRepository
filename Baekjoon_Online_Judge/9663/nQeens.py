# BOJ 9663 N-Queen
def nQueens(k):
    global sol
    if k > n:
        sol += 1
        return
    for col in range(1, n + 1):
        flag = True
        for i in range(1, k):
            if x[i] == col or abs(k - i) == abs(col - x[i]):
                flag = False
                break
        if flag:
            x[k] = col
            nQueens(k + 1)


n = int(input())
x = [0] * (n + 1)  # write solutions
sol = 0  # count number of solutions
nQueens(1)
print(sol)
