m = int(input())

neg = 0
zero = 0
pos = 0

arr = [[*map(int, input().split())] for _ in range(m)]


def check_nine(y, x, k):
    global neg, zero, pos
    num = arr[y][x]
    for i in range(k):
        for j in range(k):
            if arr[y + i][x + j] != num:
                # when arr[y,x] is not complete rect, call check_nine 9 times and return.
                for a in range(3):
                    for b in range(3):
                        check_nine(y + a * k // 3, x + b * k // 3, k // 3)
                return
    # if arr[y,x] is complete, just add a proper count.
    if num == -1:
        neg += 1
    elif num == 0:
        zero += 1
    else:
        pos += 1
    return


check_nine(0, 0, m)
print(neg, zero, pos, sep='\n')
