# BOJ 15652 N & M 2
def sol(stack: list, seq, max, size):
    start = 1 if seq == 0 else stack[seq - 1]
    for i in range(start, max+1):
        stack.append(i)
        if seq == size-1:
            print(*stack, sep=' ')
        else:
            sol(stack, seq + 1, max, size)
        stack.pop()


n, m = map(int, input().split())
arr = list()
sol(arr, 0, n, m)
