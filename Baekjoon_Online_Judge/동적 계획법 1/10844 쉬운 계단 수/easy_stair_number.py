# BOJ 10844 Easy Stair-numbers
def dp(a):
    arr = [[0 for i in range(10)] for j in range(100)]
    arr[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(1, a):
        for j in range(10):
            if j > 0: arr[i][j] += arr[i-1][j - 1]
            if j < 9: arr[i][j] += arr[i-1][j + 1]
    return sum(arr[a-1]) % 1000000000


if __name__ == "__main__":
    print(dp(int(input())))
