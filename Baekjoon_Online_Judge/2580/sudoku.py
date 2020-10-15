# BOJ 2580 Sudoku
import sys
input = sys.stdin.readline

# arr = [[0, 3, 5, 4, 6, 9, 2, 7, 8],
#        [7, 8, 2, 1, 0, 5, 6, 0, 9],
#        [0, 6, 0, 2, 7, 8, 1, 3, 5],
#        [3, 2, 1, 0, 4, 6, 8, 9, 7],
#        [8, 0, 4, 9, 1, 3, 5, 0, 6],
#        [5, 9, 6, 8, 2, 0, 4, 1, 3],
#        [9, 1, 7, 6, 5, 2, 0, 8, 0],
#        [6, 0, 3, 7, 0, 1, 9, 5, 2],
#        [2, 5, 8, 3, 9, 4, 7, 6, 0]]
arr = [[*map(int, input().split())] for _ in range(9)]
zero = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]


def getPossible(y,x):
    global arr
    cell = [arr[i][j] for i in range((y//3)*3,(y//3)*3+3) for j in range((x//3)*3,(x//3)*3+3)]
    possible = [i for i in range(1,10)]
    for i in range(9):
        if cell[i]: possible[cell[i]-1] = 0
        if arr[i][x]: possible[arr[i][x]-1] = 0
        if arr[y][i]: possible[arr[y][i]-1] = 0
    possible = set(possible)
    if 0 in possible: possible.remove(0)
    return list(possible)


def sudoku(idx):
    global arr
    if idx == len(zero):
        for row in arr:
            print(*row)
        exit(0)
    else:
        y, x = zero[idx][0], zero[idx][1]
        possible = getPossible(y, x)
        for p in possible:
            arr[y][x] = p
            sudoku(idx+1)
            arr[y][x] = 0
    return


sudoku(0)
