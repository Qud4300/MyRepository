curVal = 0b0
n: int
m: int


def myPrint(num, visited):
    for i in range(1, num+1):
        if visited & 1<<i:
            print(i, end=' ')
    print()


def dfs(num):
    global curVal
    for i in range(1, num+1):
        if not curVal & 1 << i:
            curVal = curVal | 1 << i
            if bin(curVal).count('1') < m:
                dfs(num)
            elif not res[curVal>>1]:
                res[curVal>>1] = True
                myPrint(num, curVal)
            curVal = curVal ^ 1 << i
        else: continue


n, m = map(int,input().split())
res = [False for _ in range(2**n)]
dfs(n)

