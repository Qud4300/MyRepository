visited: [bool]
res: [int]
n: int
m: int


def myPrint(arr):
    for i in range(len(arr)):
        print(res[i], end=' ')
    print()


def dfs(num, count):
    for i in range(1, num+1):
        if not visited[i-1]:
            visited[i-1] = True
            res.append(i)
            count += 1
            if count < m:
                dfs(num, count)
            else:
                myPrint(res)
            visited[i-1] = False
            res.pop()
            count -= 1
        else: continue


n, m = map(int,input().split())
count = 0
visited = [False for _ in range(n)]
res = []
dfs(n, count)

