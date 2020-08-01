res: [int]
n: int
m: int


def myPrint(arr):
    for i in range(len(arr)):
        print(res[i], end=' ')
    print()


def dfs(num, count):
    for i in range(1, num+1):
        res.append(i)
        count += 1
        if count < m:
            dfs(num, count)
        else:
            myPrint(res)
        res.pop()
        count -= 1


n, m = map(int,input().split())
count = 0
res = []
dfs(n, count)